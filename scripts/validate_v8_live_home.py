#!/usr/bin/env python3
"""Post-deploy smoke for the persisted W5 v8 Home.

Validates the actually served root and critical local assets without claiming any
external capability. The deployed Home must preserve legacy SEO bridges for the
three noindex pilots and keep RC02 non-linked.
"""
from __future__ import annotations

from urllib.parse import urljoin
from urllib.request import Request, urlopen
import os
import sys

DEFAULT_BASE = "https://arendon7.github.io/MERDIANOLEGAL/"
BASE = os.environ.get("MERIDIANO_BASE_URL", DEFAULT_BASE)
BASE = BASE if BASE.endswith("/") else BASE + "/"


def get(path: str) -> str:
    url = urljoin(BASE, path)
    request = Request(url, headers={"User-Agent": "Meridiano-W5-Live-Smoke/1.0"})
    with urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"{url}: HTTP {response.status}")
        return response.read().decode("utf-8")


def main() -> int:
    errors: list[str] = []
    try:
        home = get("")
    except Exception as exc:
        print(f"V8 LIVE HOME SMOKE FAIL: {exc}", file=sys.stderr)
        return 1

    required = (
        'data-v8-home-candidate="persisted"',
        'data-experience-system="v8"',
        'data-v8-home-shell="persisted-candidate"',
        'name="robots" content="index,follow,max-image-preview:large"',
        'rel="canonical" href="https://arendon7.github.io/MERDIANOLEGAL/"',
        "Derecho empresarial para decisiones que necesitan avanzar.",
        'id="contact-form"',
        'href="productos/sistema-contractual-empresarial.html"',
        'href="servicios/sociedades-gobierno-inversion.html"',
        'href="servicios/direccion-juridica-externa.html"',
        'src="assets/js/v8/measurement.js"',
        'src="assets/js/v8/navigation.js"',
        'src="assets/js/v8/contact.js"',
    )
    for marker in required:
        if marker not in home:
            errors.append(f"/: missing {marker!r}")

    forbidden = (
        'href="soluciones/sistema-contractual-empresarial.html"',
        'href="practicas/corporativo-societario-gobierno.html"',
        'href="servicios-continuos/direccion-juridica-externa.html"',
        "servicios-continuos/meridiano-contratos.html",
        "site-v3.css",
        "commercial-intake-v59.js",
    )
    for marker in forbidden:
        if marker in home:
            errors.append(f"/: forbidden pre-handoff/sediment marker {marker!r}")

    contact_count = home.count('id="contact-form"')
    if contact_count != 1:
        errors.append(f"/: expected one contact form, found {contact_count}")
    section_count = home.count('data-v8-home-section="H')
    if section_count != 12:
        errors.append(f"/: expected H01-H12 exactly once each, found {section_count} sections")

    for path, markers in {
        "runtime-config.js": ("window",),
        "assets/js/v8/measurement.js": ("formContentAllowed: false",),
        "assets/js/v8/navigation.js": ("data-ml-mega-toggle",),
        "assets/js/v8/contact.js": ("piiInMeasurement: false", "wa.me"),
        "assets/css/v8/home-persisted.css": ("ml-home-contact",),
        "privacidad.html": ("Privacidad",),
        "productos/sistema-contractual-empresarial.html": ("Sistema Contractual",),
        "servicios/direccion-juridica-externa.html": ("Dirección",),
    }.items():
        try:
            body = get(path)
            for marker in markers:
                if marker not in body:
                    errors.append(f"{path}: missing {marker!r}")
        except Exception as exc:
            errors.append(str(exc))

    if errors:
        print("V8 LIVE HOME SMOKE FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"V8 LIVE HOME SMOKE OK: {BASE} serves persisted H01-H12, one privacy-first intake, "
        "critical v8 assets, legacy SEO bridges and no RC02/public pilot handoff."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

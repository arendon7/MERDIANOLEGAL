#!/usr/bin/env python3
"""Fail-closed static contract for the exact future-root W5.0E Home candidate."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import sys
from urllib.parse import urlsplit

from render_v8_home_persisted import CANONICAL_URL, PUBLIC_BRIDGES, render_document
from v8_shell import load_model

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_HOME = ROOT / "index.html"
EXPECTED_SECTIONS = [f"H{i:02d}" for i in range(1, 13)]
EXPECTED_STYLES = [
    "assets/css/v8/tokens.css",
    "assets/css/v8/base.css",
    "assets/css/v8/components.css",
    "assets/css/v8/surfaces.css",
    "assets/css/v8/home-persisted.css",
]
EXPECTED_SCRIPTS = [
    "runtime-config.js",
    "assets/js/v6/analytics-adapter-v61.js",
    "assets/js/v8/measurement.js",
    "assets/js/v8/navigation.js",
    "assets/js/v8/contact.js",
]
FORBIDDEN_LEGACY_ASSETS = (
    "site-v3.css", "clarity-v31.css", "commercial-v43.css", "visual-v39.css", "ux-v45.css",
    "growth-v51.css", "decision-v58.css", "commercial-intake-v59.css", "site-v3.js",
    "commercial-conversion-v44.js", "commercial-intake-v59.js", "handoff-continuity-v517.js",
)
V8_PILOT_TARGETS = (
    "practicas/corporativo-societario-gobierno.html",
    "soluciones/sistema-contractual-empresarial.html",
    "servicios-continuos/direccion-juridica-externa.html",
)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1 = 0
        self.forms = 0
        self.contact_ids = 0
        self.sections: list[str] = []
        self.links: list[str] = []
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.robots: list[str] = []
        self.canonicals: list[str] = []
        self.form_fields: set[str] = set()
        self.inline_styles = 0
        self.inline_scripts = 0
        self._script_inline: list[bool] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag == "h1":
            self.h1 += 1
        if tag == "form":
            self.forms += 1
        if data.get("id") == "contacto":
            self.contact_ids += 1
        if data.get("data-v8-home-section"):
            self.sections.append(data["data-v8-home-section"])
        if tag == "a" and data.get("href"):
            self.links.append(data["href"])
        if tag == "link" and data.get("rel") == "stylesheet":
            self.styles.append(data.get("href", ""))
        if tag == "link" and data.get("rel") == "canonical":
            self.canonicals.append(data.get("href", ""))
        if tag == "meta" and data.get("name") == "robots":
            self.robots.append(data.get("content", ""))
        if tag in {"input", "select", "textarea"} and data.get("name"):
            self.form_fields.add(data["name"])
        if tag == "script":
            src = data.get("src", "")
            self._script_inline.append(not bool(src))
            if src:
                self.scripts.append(src)
        if tag == "style":
            self.inline_styles += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_inline:
            self._script_inline.pop()

    def handle_data(self, data: str) -> None:
        if self._script_inline and self._script_inline[-1] and data.strip():
            if '"@context":"https://schema.org"' not in data:
                self.inline_scripts += 1


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    model = load_model()
    first = render_document(model)
    second = render_document(model)
    if first != second:
        fail("persisted renderer is not deterministic")

    parser = Parser()
    parser.feed(first)
    if parser.h1 != 1:
        fail(f"future root must contain exactly one h1; found {parser.h1}")
    if parser.forms != 1 or first.count('id="contact-form"') != 1:
        fail("future root must contain exactly one contact form")
    if parser.contact_ids != 1:
        fail("future root must contain exactly one #contacto")
    if parser.sections != EXPECTED_SECTIONS:
        fail(f"H01-H12 order drifted: {parser.sections}")
    if parser.robots != ["index,follow,max-image-preview:large"]:
        fail(f"future root robots contract drifted: {parser.robots}")
    if parser.canonicals != [CANONICAL_URL]:
        fail(f"future root canonical drifted: {parser.canonicals}")
    if parser.styles != EXPECTED_STYLES:
        fail(f"future root stylesheet budget drifted: {parser.styles}")
    if parser.scripts != EXPECTED_SCRIPTS:
        fail(f"future root runtime budget/order drifted: {parser.scripts}")
    if parser.inline_styles or parser.inline_scripts:
        fail("future root introduces inline style/script sedimentation")

    required_fields = {"website", "name", "company", "email", "need", "decision_stage", "urgency", "budget", "message", "privacy"}
    if parser.form_fields != required_fields:
        fail(f"contact intake field contract drifted: {sorted(parser.form_fields)}")
    if 'name="website" tabindex="-1" autocomplete="off"' not in first:
        fail("contact honeypot contract missing")
    if 'data-v8-handoff hidden' not in first:
        fail("manual handoff/stale-draft panel missing")
    if "no crea automáticamente una relación abogado-cliente" not in first:
        fail("professional relationship disclaimer missing")

    for forbidden in FORBIDDEN_LEGACY_ASSETS:
        if forbidden in first:
            fail(f"future root reintroduced legacy asset sedimentation: {forbidden}")
    for target in V8_PILOT_TARGETS:
        if f'href="{target}"' in first:
            fail(f"future root links noindex pilot before SEO handoff: {target}")
    for code, bridge in PUBLIC_BRIDGES.items():
        if f'href="{bridge}"' not in first:
            fail(f"{code} does not preserve certified legacy bridge {bridge}")
    if "servicios-continuos/meridiano-contratos.html" in first:
        fail("RC02 remains non-materialized and must not be linked")

    for href in parser.links:
        parts = urlsplit(href)
        if parts.scheme or parts.netloc:
            fail(f"future root must not hard-code external navigation links: {href}")
        if href.startswith("#"):
            continue
        target = ROOT / parts.path
        if not target.is_file():
            fail(f"future root local href does not resolve physically: {href}")

    contact_js = (ROOT / "assets/js/v8/contact.js").read_text(encoding="utf-8")
    measurement_js = (ROOT / "assets/js/v8/measurement.js").read_text(encoding="utf-8")
    for marker in ("localStorage", "sessionStorage", "document.cookie", "fetch("):
        if marker in contact_js or marker in measurement_js:
            fail(f"v8 contact/measurement introduces forbidden persistence or direct transport: {marker}")
    if "piiInMeasurement: false" not in contact_js:
        fail("v8 contact privacy declaration missing")
    if "formContentAllowed: false" not in measurement_js:
        fail("v8 measurement privacy declaration missing")
    if "https://wa.me/${WHATSAPP}?text=" not in contact_js:
        fail("manual WhatsApp handoff target missing")

    canonical = CANONICAL_HOME.read_text(encoding="utf-8")
    if 'data-v8-home-candidate="persisted"' in canonical:
        fail("W5.0E E1 must not persist future root into index.html before browser gate")
    if len(list(ROOT.rglob("*.html"))) != 49:
        fail("W5.0E E1 source tree must remain at certified 49 HTML baseline")

    print("VALIDATE V8 W5.0E PERSISTED HOME OK: deterministic future root; indexable canonical; 5 CSS/5 JS budget; one privacy-first form; three legacy SEO bridges; RC02 non-linked; production Home untouched.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 W5.0E PERSISTED HOME FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

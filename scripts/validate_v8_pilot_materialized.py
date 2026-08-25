#!/usr/bin/env python3
"""Valida los tres targets W4.4/W4.5 después de materialización.

Además del contrato estructural, todo enlace local visible de los targets debe
resolver a un recurso físico existente. Esto permite rollout parcial: un
relacionado puede usar target v8 si ya está materializado o fallback legacy si
su target futuro todavía no existe, pero nunca puede producir 404.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "assets/data/v8/experience-model-v80.json"
SITE = ROOT / "site-config.json"
MANIFEST = ROOT / ".v8-pilot-materialization.json"

CSS_REFS = [
    "../assets/css/v8/tokens.css",
    "../assets/css/v8/base.css",
    "../assets/css/v8/components.css",
    "../assets/css/v8/surfaces.css",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def target_path(route: str) -> Path:
    return ROOT / route.lstrip("/")


def validate_local_links(page: Path, html: str, pilot_id: str) -> None:
    hrefs = re.findall(r'<a\b[^>]*\bhref="([^"]+)"', html, flags=re.I)
    if not hrefs:
        fail(f"{pilot_id}: target no contiene enlaces")
    for href in hrefs:
        if href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            continue
        path = unquote(parsed.path)
        if not path:
            continue
        resolved = (page.parent / path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError as exc:
            raise AssertionError(f"{pilot_id}: link sale del repositorio {href}") from exc
        if not resolved.exists():
            fail(f"{pilot_id}: enlace local roto {href} -> {resolved.relative_to(ROOT)}")


def main() -> int:
    model = json.loads(MODEL.read_text(encoding="utf-8"))
    site = json.loads(SITE.read_text(encoding="utf-8"))
    if not MANIFEST.exists():
        fail("falta .v8-pilot-materialization.json")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("status") != "ephemeral-candidate" or manifest.get("count") != 3:
        fail("manifest W4.4 inválido")
    if manifest.get("link_policy") != "target-if-materialized-else-legacy":
        fail("manifest no declara política transicional de enlaces")

    pilots = model.get("pilots") or []
    expected_targets = {pilot["target_route"].lstrip("/") for pilot in pilots}
    if set(manifest.get("targets") or []) != expected_targets:
        fail("manifest targets diverge de experience model")

    html_files = sorted(ROOT.rglob("*.html"))
    if len(html_files) != 49:
        fail(f"W4.4/W4.5 materializado debe tener 49 HTML (46+3); encontró {len(html_files)}")

    base_url = site["base_url"]
    for pilot in pilots:
        path = target_path(pilot["target_route"])
        if not path.exists():
            fail(f"target ausente {pilot['target_route']}")
        html = path.read_text(encoding="utf-8")
        expected_canonical = base_url + pilot["target_route"].lstrip("/")
        required = [
            '<meta name="robots" content="noindex,follow">',
            f'<link rel="canonical" href="{expected_canonical}">',
            f'data-v8-pilot="{pilot["id"]}"',
            f'data-source-catalog-id="{pilot["catalog_id"]}"',
            '<main id="contenido">',
            'class="ml-disclosure"',
        ] + [f'href="{ref}"' for ref in CSS_REFS]
        missing = [needle for needle in required if needle not in html]
        if missing:
            fail(f"{pilot['id']}: target incompleto {missing}")
        if len(re.findall(r"<h1\b", html)) != 1:
            fail(f"{pilot['id']}: debe existir exactamente un h1")
        if re.search(r"<form\b", html, flags=re.I):
            fail(f"{pilot['id']}: no puede existir form físico")
        validate_local_links(path, html, pilot["id"])

    for pilot in pilots:
        legacy = ROOT / pilot["legacy_route"].lstrip("/")
        if not legacy.exists():
            fail(f"legacy piloto desapareció {pilot['legacy_route']}")

    print("VALIDATE V8 PILOT MATERIALIZED OK: 3 targets noindex + 46 legacy, canonical candidate y cero enlaces locales rotos.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PILOT MATERIALIZED FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

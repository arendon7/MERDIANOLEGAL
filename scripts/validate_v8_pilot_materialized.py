#!/usr/bin/env python3
"""Valida los tres targets W4.4 después de materialización efímera."""
from __future__ import annotations

from pathlib import Path
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


def main() -> int:
    model = json.loads(MODEL.read_text(encoding="utf-8"))
    site = json.loads(SITE.read_text(encoding="utf-8"))
    if not MANIFEST.exists():
        fail("falta .v8-pilot-materialization.json")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("status") != "ephemeral-candidate" or manifest.get("count") != 3:
        fail("manifest W4.4 inválido")

    pilots = model.get("pilots") or []
    expected_targets = {pilot["target_route"].lstrip("/") for pilot in pilots}
    if set(manifest.get("targets") or []) != expected_targets:
        fail("manifest targets diverge de experience model")

    html_files = sorted(ROOT.rglob("*.html"))
    if len(html_files) != 49:
        fail(f"W4.4 efímero debe tener 49 HTML (46+3); encontró {len(html_files)}")

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
        if re.search(r'href="(?:\.\./)?(?:productos|servicios)/', html):
            fail(f"{pilot['id']}: target conserva internal link a familia legacy")

    for pilot in pilots:
        legacy = ROOT / pilot["legacy_route"].lstrip("/")
        if not legacy.exists():
            fail(f"legacy piloto desapareció {pilot['legacy_route']}")

    print("VALIDATE V8 PILOT MATERIALIZED OK: 3 targets noindex + 46 legacy, canonical candidate y links target coherentes.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PILOT MATERIALIZED FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Smoke post-deploy v5.3: conserva v5.2, autoridad/medición y extensiones posteriores."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

from validate_live_v52 import BASE, get, main as validate_v52

R = Path(__file__).resolve().parents[1]
AUTH = json.loads((R / "authority-v53.json").read_text(encoding="utf-8"))
V51 = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
SOLUTIONS = {item["slug"]: item for item in V51["solutions"]}
CONFIG_BASE = json.loads((R / "site-config.json").read_text(encoding="utf-8"))["base_url"]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "0.0.0")


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def main() -> int:
    if validate_v52() != 0:
        return 1

    errors: list[str] = []

    try:
        home = get("")
        for marker in (
            '"logo":{"@type":"ImageObject"',
            '"knowsAbout":[',
            "Legal Operations",
            "Tecnología e inteligencia artificial",
        ):
            if marker not in home:
                errors.append(f"/: falta {marker!r}")
    except Exception as exc:
        errors.append(str(exc))

    try:
        hub = get("soluciones/")
        if 'data-authority-v53="item-list"' not in hub:
            errors.append("soluciones/: falta ItemList v5.3")
        for slug in SOLUTIONS:
            if f'"url":"{CONFIG_BASE}soluciones/{slug}.html"' not in hub:
                errors.append(f"soluciones/: ItemList no incluye {slug}")
    except Exception as exc:
        errors.append(str(exc))

    for slug, item in SOLUTIONS.items():
        path = f"soluciones/{slug}.html"
        try:
            body = get(path)
            for marker in (
                f'data-solution-slug="{slug}"',
                f'data-page-need="{item["need"]}"',
                'data-authority-v53="item-list"',
                "../measurement-v53.js",
                "MEASUREMENT-V53:START",
            ):
                if marker not in body:
                    errors.append(f"{path}: falta {marker!r}")
        except Exception as exc:
            errors.append(str(exc))

    for entry in AUTH["perspectives"]:
        try:
            body = get(entry["path"])
            for marker in (
                "DE LA LECTURA A LA DECISIÓN",
                "../measurement-v53.js",
                'data-authority-v53="item-list"',
            ):
                if marker not in body:
                    errors.append(f"{entry['path']}: falta {marker!r}")
            for related in entry["solutions"]:
                if f'data-authority-solution="{related["slug"]}"' not in body:
                    errors.append(f"{entry['path']}: falta solución {related['slug']}")
        except Exception as exc:
            errors.append(str(exc))

    for entry in AUTH["sectors"]:
        try:
            body = get(entry["path"])
            for marker in (
                "RUTAS POR SITUACIÓN",
                "../measurement-v53.js",
                'data-authority-v53="item-list"',
            ):
                if marker not in body:
                    errors.append(f"{entry['path']}: falta {marker!r}")
            for related in entry["solutions"]:
                if f'data-authority-solution="{related["slug"]}"' not in body:
                    errors.append(f"{entry['path']}: falta solución {related['slug']}")
        except Exception as exc:
            errors.append(str(exc))

    try:
        js = get("measurement-v53.js")
        for marker in (
            "solution_view",
            "authority_open",
            "evidence_open",
            "route_open",
            "faq_open",
            "contact_intent",
            "piiAllowed: false",
            "networkTransport: false",
        ):
            if marker not in js:
                errors.append(f"measurement-v53.js: falta {marker!r}")
    except Exception as exc:
        errors.append(str(exc))

    if errors:
        print("SMOKE PÚBLICO V5.3 FALLIDO")
        for error in errors:
            print(f"- {error}")
        return 1

    if semver(VERSION) >= (5, 22, 0):
        from validate_live_v522 import wait_for_coherent_generation
        if wait_for_coherent_generation() != 0:
            return 1

    print(
        f"SMOKE PÚBLICO V5.3 OK: {BASE} sirve autoridad bidireccional, schema de descubrimiento, "
        "medición CRO sin PII y coherencia de generación cuando la release lo exige."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

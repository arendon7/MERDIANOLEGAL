#!/usr/bin/env python3
"""Smoke post-deploy v5.1: conserva v5.0 y verifica rutas comerciales nuevas."""
from __future__ import annotations

from pathlib import Path
import json
import sys

from validate_live_v50 import BASE, CONFIG_BASE, get, main as validate_v50

R = Path(__file__).resolve().parents[1]
DATA = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
SOLUTIONS = DATA["solutions"]


def main() -> int:
    if validate_v50() != 0:
        return 1
    errors: list[str] = []
    checks = {
        "": [
            "Empiece por la situación empresarial, no por el nombre del servicio.",
            "La prueba pública debe poder revisarse, no solo prometerse.",
            "growth-v51.css",
            "soluciones/",
        ],
        "soluciones/": [
            "SOLUCIONES POR SITUACIÓN EMPRESARIAL",
            "Empiece por la decisión. La modalidad jurídica viene después.",
            f'<link rel="canonical" href="{CONFIG_BASE}soluciones/">',
            f'<meta property="og:url" content="{CONFIG_BASE}soluciones/">',
            "../telemetry-v50.js",
        ],
    }
    for item in SOLUTIONS:
        path = f'soluciones/{item["slug"]}.html'
        checks[path] = [
            item["title"],
            "CUÁNDO CONVIENE ACTUAR",
            "MODALIDAD ADECUADA",
            "REVISAR ANTES DE CONTACTAR",
            f'<link rel="canonical" href="{CONFIG_BASE}{path}">',
            "../telemetry-v50.js",
        ]
    for path, markers in checks.items():
        try:
            body = get(path)
            for marker in markers:
                if marker not in body:
                    errors.append(f"{path or '/'}: falta {marker!r}")
        except Exception as exc:
            errors.append(str(exc))
    try:
        sitemap = get("sitemap.xml")
        for relative in ["soluciones/", *(f'soluciones/{item["slug"]}.html' for item in SOLUTIONS)]:
            if f"{CONFIG_BASE}{relative}" not in sitemap:
                errors.append(f"sitemap.xml: falta {relative}")
    except Exception as exc:
        errors.append(str(exc))
    if errors:
        print("SMOKE PÚBLICO V5.1 FALLIDO")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SMOKE PÚBLICO V5.1 OK: {BASE} sirve hub y 6 rutas comerciales con canonical e interlinking íntegros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

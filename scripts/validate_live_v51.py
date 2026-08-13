#!/usr/bin/env python3
"""Smoke post-deploy v5.1: conserva v5.0 y verifica rutas comerciales nuevas."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

from validate_live_v50 import BASE, CONFIG_BASE, get, main as validate_v50

R = Path(__file__).resolve().parents[1]
DATA = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "0.0.0")
SOLUTIONS = DATA["solutions"]


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def main() -> int:
    if validate_v50() != 0:
        return 1
    errors: list[str] = []
    home_markers = [
        "Empiece por la situación empresarial, no por el nombre del servicio.",
        "growth-v51.css",
        "soluciones/",
    ]
    if semver(VERSION) < (5, 22, 0):
        home_markers.append("La prueba pública debe poder revisarse, no solo prometerse.")
    else:
        home_markers.extend((
            "CÓMO SE VE EL CRITERIO SENIOR",
            "La experiencia se demuestra en las preguntas, el alcance y la capacidad de ejecutar.",
            "Antes de contratar, revise si la propuesta identifica régimen, fuentes, supuestos, responsables, límites, entregables y cierre.",
        ))

    checks = {
        "": home_markers,
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
    print(
        f"SMOKE PÚBLICO V5.1 OK: {BASE} sirve hub y 6 rutas comerciales con canonical, "
        f"interlinking y narrativa compatible con {VERSION}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

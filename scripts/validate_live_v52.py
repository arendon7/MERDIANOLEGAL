#!/usr/bin/env python3
"""Smoke post-deploy v5.2: conserva v5.1 y verifica CRO/SEO live en soluciones."""
from __future__ import annotations

from pathlib import Path
import json
import sys

from validate_live_v51 import BASE, get, main as validate_v51

R = Path(__file__).resolve().parents[1]
DATA = json.loads((R / "cro-solutions-v52.json").read_text(encoding="utf-8"))


def main() -> int:
    if validate_v51() != 0:
        return 1
    errors: list[str] = []
    try:
        hub = get("soluciones/")
        for marker in (
            "Identifique la decisión jurídica antes de escoger el servicio.",
            "cro-v52.css",
            "CRO-V52-HUB-GUIDE:START",
        ):
            if marker not in hub:
                errors.append(f"soluciones/: falta {marker!r}")
    except Exception as exc:
        errors.append(str(exc))

    for item in DATA["solutions"]:
        path = f'soluciones/{item["slug"]}.html'
        try:
            body = get(path)
            markers = (
                item["seo_title"],
                item["decision_label"],
                "OBJECIONES FRECUENTES",
                "ALCANCE Y HONORARIOS",
                "PREGUNTAS FRECUENTES",
                'data-cro-v52="faq"',
                item["cta_title"],
            )
            for marker in markers:
                if marker not in body:
                    errors.append(f"{path}: falta {marker!r}")
        except Exception as exc:
            errors.append(str(exc))

    if errors:
        print("SMOKE PÚBLICO V5.2 FALLIDO")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SMOKE PÚBLICO V5.2 OK: {BASE} sirve 6 landings CRO/SEO con FAQ estructurado y continuidad v5.1.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

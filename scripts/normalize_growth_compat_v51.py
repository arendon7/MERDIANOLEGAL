#!/usr/bin/env python3
"""Normaliza compatibilidad de la portada v5.1 antes de ejecutar capas históricas."""
from __future__ import annotations

from pathlib import Path
import json
import re

R = Path(__file__).resolve().parents[1]
INDEX = R / "index.html"
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8"))["version"]


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def main() -> int:
    if semver(VERSION) < (5, 1, 0):
        return 0
    text = INDEX.read_text(encoding="utf-8")
    legacy = 'class="growth-route-card-v51" href="soluciones/'
    canonical = 'class="need-card growth-route-card-v51" href="soluciones/'
    if legacy in text:
        text = text.replace(legacy, canonical)
        INDEX.write_text(text, encoding="utf-8")
    count = text.count(canonical)
    if "GROWTH-V51-PROOF:START" in text and count != 6:
        raise RuntimeError(f"index.html: v5.1 esperaba 6 rutas compatibles y encontró {count}")
    print(f"Compatibilidad previa v5.1 normalizada; rutas detectadas: {count}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

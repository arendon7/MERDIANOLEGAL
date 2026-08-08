#!/usr/bin/env python3
"""Aplica v5.3 y normaliza de forma determinista sus bloques gestionados."""
from __future__ import annotations

from pathlib import Path
import re

from apply_authority_v53_core import main as apply_core

R = Path(__file__).resolve().parents[1]
BLOCKS = (
    "AUTHORITY-V53-PERSPECTIVE",
    "AUTHORITY-V53-SECTOR",
    "AUTHORITY-V53-SCHEMA",
    "MEASUREMENT-V53",
)


def normalize_text(text: str) -> str:
    for name in BLOCKS:
        start = f"<!-- {name}:START -->"
        end = f"<!-- {name}:END -->"
        text = re.sub(rf"\s*{re.escape(start)}", "\n" + start, text)
        text = re.sub(rf"{re.escape(end)}\s*", end + "\n", text)
    return text


def normalize_outputs() -> int:
    paths = [
        *(R / "soluciones").glob("*.html"),
        *(R / "perspectivas").glob("*.html"),
        *(R / "sectores").glob("*.html"),
    ]
    changed = 0
    for path in sorted(paths):
        before = path.read_text(encoding="utf-8")
        after = normalize_text(before)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed += 1
    print(f"Formato v5.3 normalizado de forma determinista; archivos ajustados: {changed}.")
    return 0


def main() -> int:
    result = apply_core()
    if result != 0:
        return result
    return normalize_outputs()


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Aplica v5.3 y, desde v5.4, normaliza integración runtime y CTA demo móvil."""
from __future__ import annotations

from pathlib import Path
import json
import re

from apply_authority_v53_core import main as apply_core

R = Path(__file__).resolve().parents[1]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "")
BLOCKS = (
    "AUTHORITY-V53-PERSPECTIVE",
    "AUTHORITY-V53-SECTOR",
    "AUTHORITY-V53-SCHEMA",
    "MEASUREMENT-V53",
)
BROWSER_V54_STYLE = (
    '<!-- BROWSER-V54-DEMO:START -->\n'
    '<style data-browser-v54="demo-mobile">'
    '@media (max-width:760px){'
    '.demo-page .portal-header{gap:12px;flex-wrap:wrap}'
    '.demo-page .portal-header-actions{display:flex;align-items:center;justify-content:flex-end;gap:8px;flex-wrap:wrap}'
    '.demo-page .portal-header-actions .btn{display:inline-flex;padding:9px 12px;font-size:.68rem;white-space:nowrap}'
    '}'
    '</style>\n'
    '<!-- BROWSER-V54-DEMO:END -->'
)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


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
    return changed


def finalize_browser_v54() -> int:
    measurement_changed = 0
    paths = [
        *(R / "soluciones").glob("*.html"),
        *(R / "perspectivas").glob("*.html"),
        *(R / "sectores").glob("*.html"),
    ]
    for path in sorted(paths):
        before = path.read_text(encoding="utf-8")
        if "MEASUREMENT-V53:START" not in before:
            continue
        after = re.sub(
            r'<script(?:\s+defer)?\s+src="([^\"]*measurement-v53\.js)"></script>',
            r'<script defer src="\1"></script>',
            before,
        )
        if after != before:
            path.write_text(after, encoding="utf-8")
            measurement_changed += 1

    demo_path = R / "demo.html"
    before_demo = demo_path.read_text(encoding="utf-8")
    demo = re.sub(
        r'\s*<!-- BROWSER-V54-DEMO:START -->[\s\S]*?<!-- BROWSER-V54-DEMO:END -->\s*',
        "\n",
        before_demo,
    )
    if "</head>" not in demo:
        raise RuntimeError("demo.html: falta </head>")
    demo = demo.replace("</head>", BROWSER_V54_STYLE + "\n</head>", 1)
    demo_changed = demo != before_demo
    if demo_changed:
        demo_path.write_text(demo, encoding="utf-8")

    print(
        f"Compatibilidad Browser v5.4 aplicada: measurement defer en {measurement_changed} páginas; "
        f"CTA demo móvil {'normalizado' if demo_changed else 'ya vigente'}."
    )
    return 0


def main() -> int:
    result = apply_core()
    if result != 0:
        return result
    normalize_outputs()
    if semver(VERSION) >= (5, 4, 0):
        return finalize_browser_v54()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

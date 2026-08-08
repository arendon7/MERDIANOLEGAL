#!/usr/bin/env python3
"""Normaliza únicamente el formato de las 18 salidas administradas por UX/UI v4.7."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ROOT / 'firma.html',
    ROOT / 'perspectivas.html',
    ROOT / 'experiencia.html',
    ROOT / 'demo.html',
    *sorted((ROOT / 'perspectivas').glob('*.html')),
    *sorted((ROOT / 'sectores').glob('*.html')),
]

MARKERS = (
    '<!-- EDITORIAL-V47-MENU:START -->',
    '<!-- EDITORIAL-V47-MENU:END -->',
    '<!-- EDITORIAL-V47-MOBILE:START -->',
    '<!-- EDITORIAL-V47-MOBILE:END -->',
    '<!-- EDITORIAL-V47-SECTOR-NAV:START -->',
    '<!-- EDITORIAL-V47-SECTOR-NAV:END -->',
    '<!-- EDITORIAL-V47-CONVERSION:START -->',
    '<!-- EDITORIAL-V47-CONVERSION:END -->',
    '<!-- EDITORIAL-V47-TRUST:START -->',
    '<!-- EDITORIAL-V47-TRUST:END -->',
    '<!-- EDITORIAL-V47-DEMO-GUIDE:START -->',
    '<!-- EDITORIAL-V47-DEMO-GUIDE:END -->',
)


def normalize(text: str) -> str:
    # Los bloques administrados quedan siempre en línea propia, tanto si el
    # HTML anterior era minificado como si estaba indentado en varias líneas.
    for marker in MARKERS:
        text = re.sub(
            r'[ \t]*(?:\r?\n[ \t]*)?' + re.escape(marker),
            '\n' + marker,
            text,
        )

    # Elimina líneas compuestas solo por indentación y líneas vacías
    # acumulativas. No modifica texto, atributos ni contenido jurídico.
    text = re.sub(r'[ \t]+\n', '\n', text)
    text = re.sub(r'\n(?:[ \t]*\n)+', '\n', text)

    # Mantiene una terminación POSIX única y reproducible.
    return text.rstrip() + '\n'


def main() -> int:
    if len(TARGETS) != 18:
        raise RuntimeError(f'Se esperaban 18 salidas v4.7 y se encontraron {len(TARGETS)}')
    changed = 0
    for path in TARGETS:
        current = path.read_text(encoding='utf-8')
        updated = normalize(current)
        if updated != current:
            path.write_text(updated, encoding='utf-8')
            changed += 1
    print(f'Formato v4.7 normalizado en 18 páginas; archivos ajustados: {changed}.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

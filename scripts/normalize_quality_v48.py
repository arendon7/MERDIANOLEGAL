#!/usr/bin/env python3
"""Normaliza únicamente whitespace administrado por la capa de calidad v4.8."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'index.html'
START = '<!-- QUALITY-V48-SEO:START -->'

text = INDEX.read_text(encoding='utf-8')
updated = re.sub(r'\n(?:[ \t]*\n)+(?=' + re.escape(START) + r')', '\n', text)
if updated != text:
    INDEX.write_text(updated, encoding='utf-8')
    print('Formato v4.8 normalizado en index.html.')
else:
    print('Formato v4.8 ya normalizado.')

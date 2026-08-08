#!/usr/bin/env python3
"""Normaliza únicamente residuos administrados por la capa de calidad v4.8."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / 'index.html'
SITE = ROOT / 'site-v3.js'
START = '<!-- QUALITY-V48-SEO:START -->'

index_text = INDEX.read_text(encoding='utf-8')
index_updated = re.sub(r'\n(?:[ \t]*\n)+(?=' + re.escape(START) + r')', '\n', index_text)
if index_updated != index_text:
    INDEX.write_text(index_updated, encoding='utf-8')
    print('Formato v4.8 normalizado en index.html.')
else:
    print('Formato v4.8 de index.html ya normalizado.')

site_text = SITE.read_text(encoding='utf-8')
site_updated = site_text.replace("tab.removeAttribute('aria-selected'); ", '')
if site_updated != site_text:
    SITE.write_text(site_updated, encoding='utf-8')
    print('Semántica ARIA v4.8 normalizada en site-v3.js.')
else:
    print('Semántica ARIA v4.8 de site-v3.js ya normalizada.')

#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
required = [
    'assets/brand/meridiano-monogram.svg',
    'assets/brand/meridiano-logo-horizontal-dark.svg',
    'assets/brand/meridiano-logo-horizontal-light.svg',
    'assets/brand/favicon.svg',
    'assets/images/global/home-hero.webp',
    'visual-v39.css',
    'visual-v39.js',
]
for rel in required:
    p = ROOT / rel
    if not p.exists() or p.stat().st_size < 100:
        errors.append(f'Falta o está vacío: {rel}')

img = ROOT / 'assets/images/global/home-hero.webp'
if img.exists():
    b = img.read_bytes()
    if not (b.startswith(b'RIFF') and b[8:12] == b'WEBP'):
        errors.append('home-hero.webp no es WebP válido por cabecera')

for rel in ['index.html', 'firma.html', 'perspectivas.html', 'experiencia.html', 'demo.html']:
    p = ROOT / rel
    if p.exists():
        t = p.read_text(encoding='utf-8')
        if 'visual-v39.css' not in t or 'visual-v39.js' not in t:
            errors.append(f'{rel}: falta carga del sistema visual canónico')
        if 'assets/logo-meridiano.svg' in t:
            errors.append(f'{rel}: conserva logo legado')

index = (ROOT / 'index.html').read_text(encoding='utf-8')
for marker in ['assets/brand/favicon.svg', 'assets/images/global/home-hero.webp']:
    if marker not in index:
        errors.append(f'index.html: falta {marker}')

version = json.loads((ROOT / 'version.json').read_text(encoding='utf-8'))
version_value = str(version.get('version', '')).strip()
if not re.fullmatch(r'\d+\.\d+\.\d+', version_value):
    errors.append('version.json no contiene una versión semántica válida')
elif f'Web demostrativa v{version_value}' not in index:
    errors.append(f'index.html no refleja la versión canónica {version_value}')

if errors:
    print('VALIDACIÓN VISUAL FALLIDA')
    print('\n'.join(f'- {e}' for e in errors))
    sys.exit(1)
print(f'VALIDACIÓN VISUAL OK · versión {version_value}')

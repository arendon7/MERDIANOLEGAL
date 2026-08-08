#!/usr/bin/env python3
"""Valida la capa transversal de UX/UI editorial y demostrativa v4.7."""

from pathlib import Path
from packaging.version import Version
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = Version(json.loads((ROOT / 'version.json').read_text(encoding='utf-8'))['version'])
PERSPECTIVES = sorted((ROOT / 'perspectivas').glob('*.html'))
SECTORS = sorted((ROOT / 'sectores').glob('*.html'))
ROOT_PAGES = [ROOT / 'firma.html', ROOT / 'perspectivas.html', ROOT / 'experiencia.html', ROOT / 'demo.html']
TARGETS = ROOT_PAGES + PERSPECTIVES + SECTORS


def fail(message: str) -> None:
    print(f'ERROR v4.7: {message}', file=sys.stderr)
    raise SystemExit(1)


if VERSION < Version('4.7.0'):
    fail(f'version.json está en {VERSION}, se requiere >= 4.7.0')
if len(PERSPECTIVES) != 6 or len(SECTORS) != 8 or len(TARGETS) != 18:
    fail(f'conteo inesperado: perspectivas={len(PERSPECTIVES)}, sectores={len(SECTORS)}, total={len(TARGETS)}')

css = ROOT / 'editorial-v47.css'
js = ROOT / 'editorial-v47.js'
applicator = ROOT / 'scripts' / 'apply_editorial_ux_v47.py'
for path in (css, js, applicator):
    if not path.exists() or path.stat().st_size < 500:
        fail(f'falta recurso sustantivo {path.relative_to(ROOT)}')

for path in TARGETS:
    text = path.read_text(encoding='utf-8')
    prefix = '../' if path.parent != ROOT else ''
    if text.count(f'href="{prefix}editorial-v47.css"') != 1:
        fail(f'{path.relative_to(ROOT)} no carga editorial-v47.css exactamente una vez')
    if text.count(f'src="{prefix}editorial-v47.js"') != 1:
        fail(f'{path.relative_to(ROOT)} no carga editorial-v47.js exactamente una vez')
    if text.count('data-editorial-v47="true"') != 1:
        fail(f'{path.relative_to(ROOT)} no declara data-editorial-v47')
    if path.name != 'demo.html':
        if text.count('EDITORIAL-V47-MENU:START') != 1 or text.count('editorial-menu-toggle-v47') != 1:
            fail(f'{path.relative_to(ROOT)} no tiene menú móvil v4.7')
        if text.count('id="editorial-nav-v47"') != 1:
            fail(f'{path.relative_to(ROOT)} no tiene navegación accesible v4.7')
    if text.count('EDITORIAL-V47-MOBILE:START') != 1 or text.count('editorial-mobile-cta-v47') != 1:
        fail(f'{path.relative_to(ROOT)} no tiene CTA móvil v4.7')

firm = (ROOT / 'firma.html').read_text(encoding='utf-8')
if firm.count('firm-sector-link-v47') != 8:
    fail('firma.html debe enlazar exactamente 8 enfoques sectoriales')
if 'director-mark v47-mark' not in firm or 'meridiano-monogram.svg' not in firm:
    fail('firma.html no usa el monograma canónico en la tarjeta de dirección')

library = (ROOT / 'perspectivas.html').read_text(encoding='utf-8')
slugs = [
    'gobierno-juridico-inteligencia-artificial.html',
    'contratos-administrables.html',
    'proyectos-regulados-secuencia-viabilidad.html',
    'propiedad-intelectual-cadena-titularidad.html',
    'socios-inversion-gobierno.html',
    'legal-operations-modelo-operativo.html',
]
for slug in slugs:
    count = library.count(f'perspectivas/{slug}')
    if count != 1:
        fail(f'perspectivas.html debe enlazar {slug} exactamente una vez y tiene {count}')
if library.count('<a class="insight-card"') != 5:
    # Dos de las cinco tarjetas insight están en el bloque destacado y tres en la biblioteca.
    fail('perspectivas.html debe conservar 5 tarjetas insight sin duplicar las 3 lecturas destacadas')

for path in PERSPECTIVES:
    text = path.read_text(encoding='utf-8')
    if text.count('EDITORIAL-V47-CONVERSION:START') != 1 or 'editorial-conversion-v47' not in text:
        fail(f'{path.relative_to(ROOT)} no tiene cierre de conversión editorial')
    if '<nav class="article-toc"' not in text:
        fail(f'{path.relative_to(ROOT)} perdió el índice del artículo')

for path in SECTORS:
    text = path.read_text(encoding='utf-8')
    if text.count('EDITORIAL-V47-SECTOR-NAV:START') != 1 or text.count('sector-quicknav-v47') != 1:
        fail(f'{path.relative_to(ROOT)} no tiene recorrido sectorial v4.7')
    for marker in ('id="sector-enfoque"', 'id="sector-decisiones"', 'id="sector-riesgos"', 'id="sector-contacto"'):
        if text.count(marker) != 1:
            fail(f'{path.relative_to(ROOT)} debe contener exactamente una vez {marker}')
    if 'EDITORIAL-SEQUENCE:START' not in text:
        fail(f'{path.relative_to(ROOT)} perdió navegación anterior/siguiente')

experience = (ROOT / 'experiencia.html').read_text(encoding='utf-8')
for marker in ('EDITORIAL-V47-TRUST:START', 'experience-trust-v47', 'EDITORIAL-V47-CONVERSION:START', 'experience-conversion-v47'):
    if marker not in experience:
        fail(f'experiencia.html no contiene {marker}')
for panel in ('recorrido', 'entregables', 'caso', 'simulador', 'empresas'):
    if f'data-panel="{panel}"' not in experience:
        fail(f'experiencia.html perdió el panel {panel}')

demo = (ROOT / 'demo.html').read_text(encoding='utf-8')
if demo.count('EDITORIAL-V47-DEMO-GUIDE:START') != 1 or 'demo-guide-v47' not in demo:
    fail('demo.html no contiene guía de uso v4.7')
for panel in ('dashboard', 'tickets', 'expedientes', 'documentos', 'archivos', 'obligaciones', 'calendario', 'riesgos', 'analitica'):
    if f'data-panel="{panel}"' not in demo:
        fail(f'demo.html perdió el módulo {panel}')
if 'Cliente2026!' not in demo or 'Abogado2026!' not in demo or 'Meridiano2026!' not in demo:
    fail('demo.html perdió los perfiles demostrativos')

css_text = css.read_text(encoding='utf-8')
for marker in ('editorial-menu-toggle-v47', 'editorial-mobile-cta-v47', 'sector-quicknav-v47', 'demo-guide-v47', 'reading-progress-v47'):
    if marker not in css_text:
        fail(f'editorial-v47.css no contiene {marker}')

js_text = js.read_text(encoding='utf-8')
for marker in ('reading-progress-v47', 'editorial-menu-toggle-v47', 'IntersectionObserver', 'portal-nav'):
    if marker not in js_text:
        fail(f'editorial-v47.js no contiene {marker}')

result = subprocess.run(['node', '--check', str(js)], capture_output=True, text=True)
if result.returncode != 0:
    fail('editorial-v47.js no supera node --check: ' + result.stderr.strip())

print('OK: UX/UI editorial y demostrativa v4.7 validada en 18 páginas.')

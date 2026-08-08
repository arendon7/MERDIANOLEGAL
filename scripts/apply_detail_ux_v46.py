#!/usr/bin/env python3
"""Aplica la capa transversal de UX/UI v4.6 a las 16 fichas profundas."""

from pathlib import Path
from urllib.parse import quote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'version.json').read_text(encoding='utf-8'))['version']
TARGETS = sorted((ROOT / 'servicios').glob('*.html')) + sorted((ROOT / 'productos').glob('*.html'))
STYLE = '<link rel="stylesheet" href="../detail-v46.css">'
SCRIPT = '<script defer src="../detail-v46.js"></script>'
NAV_START = '<!-- DETAIL-V46-NAV:START -->'
NAV_END = '<!-- DETAIL-V46-NAV:END -->'
MOBILE_START = '<!-- DETAIL-V46-MOBILE:START -->'
MOBILE_END = '<!-- DETAIL-V46-MOBILE:END -->'

HEADER_NAV = '''<nav class="detail-nav" id="detail-nav" aria-label="Navegación principal"><a href="../index.html#servicios">Servicios</a><a href="../index.html#productos">Productos</a><a href="../index.html#planes">Planes y precios</a><a href="../index.html#sectores">Sectores</a><a href="../firma.html">Firma</a></nav>'''
HEADER_ACTIONS = '''<div class="detail-header-actions"><a class="btn btn-outline" href="../experiencia.html">Centro demo</a><a class="btn btn-navy" href="#contacto">Presentar necesidad</a></div>'''
TOC = '''<!-- DETAIL-V46-NAV:START -->
<nav class="detail-toc-v46" aria-label="Navegación de la ficha"><div class="container detail-toc-inner-v46"><div class="detail-toc-label-v46"><span>RECORRIDO</span><strong>Ir directo a</strong></div><div class="detail-toc-links-v46"><a href="#pregunta-title">Decisión</a><a href="#alcance-title">Alcance</a><a href="#entregables-title">Entregables</a><a href="#cronograma-title">Implementación</a><a href="#limites-title">Límites</a><a href="#contacto-title">Siguiente paso</a></div><a class="detail-toc-cta-v46" href="#contacto">Presentar necesidad →</a></div></nav>
<!-- DETAIL-V46-NAV:END -->'''


def remove_managed_block(text: str, start: str, end: str) -> str:
    pattern = (
        r'(?ms)^[ \t]*' + re.escape(start) + r'[ \t]*\r?\n'
        r'.*?'
        r'^[ \t]*' + re.escape(end) + r'[ \t]*(?:\r?\n)?'
    )
    return re.sub(pattern, '', text, count=1)


def remove_managed_line(text: str, tag: str) -> str:
    return re.sub(r'(?m)^[ \t]*' + re.escape(tag) + r'[ \t]*(?:\r?\n)?', '', text)


def replace_one(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, lambda _m: replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'No se pudo actualizar {label}')
    return updated


def patch(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    text = replace_one(
        text,
        r'<nav class="detail-nav" id="detail-nav" aria-label="Navegación principal">[\s\S]*?</nav>',
        HEADER_NAV,
        f'navegación de {path.name}',
    )
    text = replace_one(
        text,
        r'<div class="detail-header-actions">[\s\S]*?</div>',
        HEADER_ACTIONS,
        f'acciones de cabecera de {path.name}',
    )

    text = remove_managed_block(text, NAV_START, NAV_END)
    hero_anchor = '<!-- STATIC-CATALOG-HERO:END --></section>'
    if hero_anchor not in text:
        raise RuntimeError(f'{path.name}: falta cierre canónico del hero')
    text = text.replace(hero_anchor, hero_anchor + '\n' + TOC, 1)

    text = remove_managed_block(text, MOBILE_START, MOBILE_END)
    title_match = re.search(r'data-page-title="([^"]+)"', text)
    title = title_match.group(1) if title_match else 'esta solución'
    message = quote(f'Hola, revisé {title} en Meridiano Legal y quiero evaluar si aplica a mi necesidad.')
    mobile = f'''  <!-- DETAIL-V46-MOBILE:START -->\n  <div class="detail-mobile-cta-v46" aria-label="Acciones rápidas de la ficha"><a href="#contacto">Presentar necesidad</a><a href="https://wa.me/573008507813?text={message}" target="_blank" rel="noopener noreferrer">WhatsApp</a></div>\n  <!-- DETAIL-V46-MOBILE:END -->'''
    floating = '  <div class="floating-detail">'
    if floating not in text:
        raise RuntimeError(f'{path.name}: falta control flotante canónico')
    text = text.replace(floating, mobile + '\n' + floating, 1)

    text = re.sub(r'Ficha v\d+\.\d+\.\d+', f'Ficha v{VERSION}', text)

    text = remove_managed_line(text, STYLE)
    text = text.replace('</head>', f'  {STYLE}\n</head>', 1)
    text = remove_managed_line(text, SCRIPT)
    text = text.replace('</body>', f'  {SCRIPT}\n</body>', 1)

    path.write_text(text, encoding='utf-8')


def main() -> int:
    if len(TARGETS) != 16:
        raise RuntimeError(f'Se esperaban 16 fichas profundas y se encontraron {len(TARGETS)}')
    for path in TARGETS:
        patch(path)
    print(f'UX/UI profunda v{VERSION} aplicada en {len(TARGETS)} fichas de servicios y productos.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

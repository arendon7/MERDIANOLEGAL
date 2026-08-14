#!/usr/bin/env python3
"""Valida v5.26: menor redundancia visible y activos visuales físicamente resolubles."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'index.html'
CONTRACT = ROOT / 'visual-assets-v526.json'
CSS = ROOT / 'integral-v526.css'
START = '<!-- INTEGRAL-V526-HOME:START -->'
END = '<!-- INTEGRAL-V526-HOME:END -->'
MOBILE_REGION = 'class="home-signal-meta-v526" data-mobile-scrollable-v516="true" tabindex="0" role="region" aria-label="Cobertura pública de Meridiano Legal"'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f'INTEGRAL VISUAL V5.26 FAIL: {message}')


def validate_local_images(text: str) -> None:
    sources = re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', text, re.I)
    require(len(sources) >= 2, 'la portada debe materializar al menos hero + mapa visual')
    for src in sources:
        parsed = urlsplit(src)
        if parsed.scheme or src.startswith('//') or src.startswith('data:'):
            continue
        clean = parsed.path.lstrip('/')
        require((ROOT / clean).is_file(), f'imagen local inexistente referenciada por index.html: {src}')


def validate() -> None:
    data = json.loads(CONTRACT.read_text(encoding='utf-8'))
    require(data.get('version') == '5.26.0', 'contrato visual debe declarar 5.26.0')
    assets = data.get('assets') or []
    require(len(assets) >= 3, 'inventario visual debe registrar activos reales/reutilizables')
    for asset in assets:
        require((ROOT / asset['path']).is_file(), f'activo inexistente: {asset["path"]}')
    external = data.get('external_references') or []
    require(len(external) >= 3, 'deben registrarse referencias visuales externas aún no ingeridas')
    require(all(item.get('status') == 'reference_only_pending_binary_ingest' for item in external), 'las referencias externas no pueden declararse como activos públicos')
    pending = [slot for slot in data.get('slots', []) if str(slot.get('state', '')).startswith('pending')]
    require(pending and all(slot.get('public_render') is False and slot.get('asset') is None for slot in pending), 'slots pendientes deben permanecer fuera del HTML público')

    text = HOME.read_text(encoding='utf-8')
    require(text.count(START) == 1 and text.count(END) == 1, 'portada debe contener exactamente una capa v5.26')
    require(text.count('<link rel="stylesheet" href="integral-v526.css">') == 1, 'CSS v5.26 debe cargarse exactamente una vez')
    require('class="principles"' not in text, 'la banda histórica de métricas debe quedar consolidada')
    require('class="audience-strip"' not in text, 'la banda histórica de audiencias debe quedar consolidada')
    require(text.count('data-integral-v526="signal"') == 1, 'debe existir una sola señal editorial v5.26')
    require(text.count(MOBILE_REGION) == 1, 'la señal v5.26 debe aportar exactamente una región móvil accesible y enfocada')
    for marker in (
        'Menos capas. Más criterio aplicable.',
        '8 servicios + 8 productos',
        '16 fichas con alcance verificable',
        '5 planes + 5 modalidades de contratación',
        '8 sectores · 8 lecturas sectoriales',
        'assets/decision-map-v526.svg',
        'id="necesidades"',
        'data-home-decision-v520="true"',
        'GROWTH-V51-PROOF:START',
        'data-professional-authority-v525="home"',
    ):
        require(marker in text, f'portada pierde contrato material: {marker}')
    require(text.count('class="need-card" href="soluciones/') == 6, 'deben preservarse las seis rutas de necesidad')
    require(text.count('data-proof-model-v512=') == 5, 'deben preservarse las cinco modalidades canónicas')
    require(text.find('data-integral-v526="signal"') < text.find('id="necesidades"') < text.find('data-home-decision-v520="true"'), 'la jerarquía debe ser señal → necesidad → modalidad')
    for ref in external:
        require(ref['title'] not in text, f'una referencia externa sin binario llegó al HTML: {ref["title"]}')
    validate_local_images(text)

    css = CSS.read_text(encoding='utf-8')
    for marker in ('.home-signal-v526', '.home-signal-grid-v526', '.home-signal-map-v526', 'display:block!important', 'overflow-x:auto', '@media(max-width:900px)', '@media(max-width:620px)'):
        require(marker in css, f'CSS v5.26 carece de {marker}')
    for forbidden in ('animation:', '@keyframes', 'filter:blur', 'backdrop-filter'):
        require(forbidden not in css, f'v5.26 no debe añadir efecto decorativo innecesario: {forbidden}')


def main() -> int:
    validate()
    print('INTEGRAL VISUAL V5.26 OK: jerarquía compacta, hero móvil visible, región accesible propia y activos locales íntegros.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

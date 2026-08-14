#!/usr/bin/env python3
"""v5.26: reduce capas visibles redundantes e integra activos visuales reales."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "visual-assets-v526.json"
CSS_LINK = '<link rel="stylesheet" href="integral-v526.css">'
START = '<!-- INTEGRAL-V526-HOME:START -->'
END = '<!-- INTEGRAL-V526-HOME:END -->'


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def ensure_css(text: str) -> str:
    text = re.sub(r'(?m)^\s*' + re.escape(CSS_LINK) + r'\s*$', '', text)
    if '</head>' not in text:
        raise RuntimeError('index.html sin </head>')
    return text.replace('</head>', f'  {CSS_LINK}\n</head>', 1)


def remove_managed(text: str) -> str:
    return re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'(?:\r?\n)?', '', text, count=1, flags=re.S)


def remove_redundant_band(text: str, class_name: str) -> str:
    pattern = re.compile(r'\s*<section class="' + re.escape(class_name) + r'"[^>]*>.*?</section>\s*', re.S)
    text, count = pattern.subn('\n', text, count=1)
    if count not in (0, 1):
        raise RuntimeError(f'index.html: estado inesperado para {class_name}')
    return text


def validate_assets(contract: dict) -> None:
    if contract.get('version') != '5.26.0':
        raise RuntimeError('visual-assets-v526.json debe declarar 5.26.0')
    for asset in contract.get('assets', []):
        path = ROOT / str(asset.get('path', ''))
        if not path.is_file():
            raise RuntimeError(f'activo v5.26 inexistente: {asset.get("path")}')
    pending = [slot for slot in contract.get('slots', []) if str(slot.get('state', '')).startswith('pending')]
    if any(slot.get('public_render') is not False for slot in pending):
        raise RuntimeError('todo slot pendiente debe declarar public_render=false')


def signal_block() -> str:
    return f'''{START}
<section class="home-signal-v526" data-integral-v526="signal" aria-labelledby="home-signal-v526-title">
  <div class="container home-signal-grid-v526">
    <div class="home-signal-copy-v526">
      <p class="eyebrow dark">UNA FIRMA PARA DECISIONES COMPLEJAS</p>
      <h2 id="home-signal-v526-title">Menos capas. Más criterio aplicable.</h2>
      <p>Meridiano es especialmente útil cuando una decisión jurídica cruza crecimiento, inversión, operación, tecnología o regulación. El punto de entrada es la necesidad empresarial; no tiene que adivinar primero el nombre del servicio.</p>
      <div class="home-signal-meta-v526" data-mobile-scrollable-v516="true" tabindex="0" role="region" aria-label="Cobertura pública de Meridiano Legal">
        <span>8 servicios + 8 productos · 16 fichas con alcance verificable</span><span>5 planes + 5 modalidades de contratación</span><span>8 sectores · 8 lecturas sectoriales</span>
      </div>
    </div>
    <figure class="home-signal-map-v526">
      <img src="assets/decision-map-v526.svg" alt="Ruta Meridiano: comprender, calificar, estructurar, implementar y seguir" width="1200" height="430" loading="lazy" decoding="async">
      <figcaption>Una misma lógica de trabajo conecta la comprensión del problema con alcance, implementación, responsables y memoria.</figcaption>
    </figure>
  </div>
</section>
{END}'''


def main() -> int:
    version = json.loads(VERSION.read_text(encoding='utf-8')).get('version', '0.0.0')
    if semver(version) < (5, 26, 0):
        return 0
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_assets(contract)

    text = HOME.read_text(encoding='utf-8')
    text = remove_managed(text)
    text = ensure_css(text)
    text = remove_redundant_band(text, 'principles')
    text = remove_redundant_band(text, 'audience-strip')

    anchor = '<section class="section needs-section" id="necesidades">'
    if text.count(anchor) != 1:
        raise RuntimeError('index.html: se esperaba un único #necesidades canónico')
    text = text.replace(anchor, signal_block() + '\n' + anchor, 1)
    HOME.write_text(text, encoding='utf-8')

    from validate_integral_visual_v526 import validate
    validate()
    print('INTEGRAL VISUAL V5.26 OK: dos bandas redundantes consolidadas, mapa histórico recuperado y activos pendientes sin URLs rotas.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

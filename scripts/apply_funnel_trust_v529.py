#!/usr/bin/env python3
"""v5.29: unifica observabilidad del funnel y acerca confianza verificable al contacto."""
from __future__ import annotations

from html import escape
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
VERSION = ROOT / "version.json"
AUTHORITY = ROOT / "professional-authority-v525.json"
CONTRACT = ROOT / "funnel-contract-v529.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
CSS_LINK = '<link rel="stylesheet" href="funnel-trust-v529.css">'
CSS_ANCHOR = '<link rel="stylesheet" href="conversion-path-v528.css">'
HOME_SCRIPT = '<script defer src="funnel-observability-v529.js"></script>'
HOME_SCRIPT_ANCHOR = '<script defer src="handoff-observability-v518.js"></script>'
DETAIL_SCRIPT = '<script defer src="../funnel-observability-v529.js"></script>'
DETAIL_SCRIPT_ANCHOR = '<script defer src="../telemetry-v50.js"></script>'
START = '<!-- FUNNEL-TRUST-V529:START -->'
END = '<!-- FUNNEL-TRUST-V529:END -->'
COMMERCIAL_END = '<!-- COMMERCIAL-V43:END -->'
VISUAL_CSS = '<link rel="stylesheet" href="visual-v39.css">'
COMMERCIAL_CSS = '<link rel="stylesheet" href="commercial-v43.css">'


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def strip_block(text: str) -> str:
    return re.sub(
        r'\s*' + re.escape(START) + r'.*?' + re.escape(END) + r'\s*',
        '\n',
        text,
        count=1,
        flags=re.S,
    )


def ensure_link(text: str, link: str, anchor: str) -> str:
    # Solo consume sangría horizontal y el salto de la propia línea. Usar \s aquí
    # permitiría absorber saltos adyacentes y producir deriva de formato entre pasadas.
    text = re.sub(
        r'(?m)^[ \t]*' + re.escape(link) + r'[ \t]*(?:\r?\n)?',
        '',
        text,
    )
    if anchor not in text:
        raise RuntimeError(f'falta ancla para {link}')
    return text.replace(anchor, anchor + '\n  ' + link, 1)


def normalize_home_head(text: str) -> str:
    """Fija el separador commercial-v43 → visual-v39 tras renderers históricos."""
    pattern = re.escape(COMMERCIAL_CSS) + r'[ \t]*(?:\r?\n)(?:[ \t]*(?:\r?\n))*[ \t]*' + re.escape(VISUAL_CSS)
    replacement = COMMERCIAL_CSS + '\n  ' + VISUAL_CSS
    text, count = re.subn(pattern, replacement, text, count=1)
    if count != 1:
        raise RuntimeError('index.html: no se pudo normalizar commercial-v43.css → visual-v39.css')
    return text


def trust_block(source: dict) -> str:
    director = source['director']
    degree = director['education'][0]
    role = source['roles'][0]
    matters = source['representative_matters']
    boundary = source['boundaries']['copy']
    return f'''{START}
<aside class="decision-trust-v529" data-funnel-trust-v529="true" aria-labelledby="decision-trust-v529-title">
  <div class="container decision-trust-inner-v529">
    <div class="decision-trust-copy-v529">
      <span>RESPALDO DEL CRITERIO</span>
      <strong id="decision-trust-v529-title">Antes de presentar la necesidad, puede verificar quién dirige el criterio jurídico.</strong>
      <p>La confianza aquí se apoya en formación, roles y tipos de asuntos documentados; no en logos, testimonios ni resultados atribuidos sin soporte.</p>
    </div>
    <div class="decision-trust-evidence-v529" tabindex="0" role="region" aria-label="Evidencia profesional resumida">
      <article><b>Formación</b><strong>{escape(str(degree['credential']))} · {escape(str(degree['institution']))}</strong><small>Graduado en {escape(str(degree['year']))}</small></article>
      <article><b>Práctica actual</b><strong>{escape(str(role['role']))}</strong><small>{escape(str(role['organization']))} · {escape(str(role['period']))}</small></article>
      <article><b>Asuntos documentados</b><strong>{escape(str(matters[0]['title']))}</strong><small>{escape(str(matters[1]['title']))} · {escape(str(matters[3]['title']))}</small></article>
    </div>
    <div class="decision-trust-actions-v529">
      <p class="decision-trust-boundary-v529">{escape(str(boundary))}</p>
      <a class="decision-trust-link-v529" href="firma.html#trayectoria">Ver trayectoria completa →</a>
    </div>
  </div>
</aside>
{END}'''


def patch_home(source: dict) -> None:
    text = HOME.read_text(encoding='utf-8')
    text = strip_block(text)
    text = ensure_link(text, CSS_LINK, CSS_ANCHOR)
    text = ensure_link(text, HOME_SCRIPT, HOME_SCRIPT_ANCHOR)
    if text.count(COMMERCIAL_END) != 1:
        raise RuntimeError('index.html: el cierre comercial debe existir exactamente una vez')
    text = text.replace(COMMERCIAL_END, COMMERCIAL_END + '\n' + trust_block(source), 1)
    text = normalize_home_head(text)
    HOME.write_text(text, encoding='utf-8')


def patch_details() -> None:
    if len(DETAIL_TARGETS) != 16:
        raise RuntimeError(f'se esperaban 16 fichas profundas y se encontraron {len(DETAIL_TARGETS)}')
    for path in DETAIL_TARGETS:
        text = path.read_text(encoding='utf-8')
        text = ensure_link(text, DETAIL_SCRIPT, DETAIL_SCRIPT_ANCHOR)
        path.write_text(text, encoding='utf-8')


def validate_materialized() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / 'scripts/validate_funnel_trust_v529.py')],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if completed.returncode:
        detail = (completed.stderr or completed.stdout).strip()
        raise RuntimeError(f'v5.29 no supera validator: {detail}')
    if completed.stdout.strip():
        print(completed.stdout.strip())


def main() -> int:
    version = json.loads(VERSION.read_text(encoding='utf-8')).get('version', '0.0.0')
    if semver(version) < (5, 29, 0):
        return 0
    source = json.loads(AUTHORITY.read_text(encoding='utf-8'))
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    if source.get('version') != '5.25.0':
        raise RuntimeError('professional-authority-v525.json deja de ser fuente válida')
    if contract.get('version') != '5.29.0':
        raise RuntimeError('funnel-contract-v529.json debe declarar 5.29.0')
    patch_home(source)
    patch_details()
    validate_materialized()
    print('FUNNEL + TRUST V5.29 OK: observabilidad no PII en home + 16 fichas y confianza verificable materializadas.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

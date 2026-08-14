#!/usr/bin/env python3
"""Valida v5.29: funnel semántico sin PII y confianza derivada de autoridad v5.25."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'index.html'
VERSION = ROOT / 'version.json'
CONTRACT = ROOT / 'funnel-contract-v529.json'
AUTHORITY = ROOT / 'professional-authority-v525.json'
SCRIPT = ROOT / 'funnel-observability-v529.js'
CSS = ROOT / 'funnel-trust-v529.css'
DETAIL_TARGETS = sorted((ROOT / 'servicios').glob('*.html')) + sorted((ROOT / 'productos').glob('*.html'))


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r'(\d+)\.(\d+)\.(\d+)', str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f'FUNNEL + TRUST V5.29 FAIL: {message}')


def main() -> int:
    version = json.loads(VERSION.read_text(encoding='utf-8')).get('version', '0.0.0')
    if semver(version) < (5, 29, 0):
        print('FUNNEL + TRUST V5.29 SKIP: version anterior a 5.29.0')
        return 0

    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    authority = json.loads(AUTHORITY.read_text(encoding='utf-8'))
    text = HOME.read_text(encoding='utf-8')
    js = SCRIPT.read_text(encoding='utf-8')
    css = CSS.read_text(encoding='utf-8')

    require(contract.get('version') == '5.29.0', 'contrato debe declarar 5.29.0')
    privacy = contract.get('privacy', {})
    for key in ('pii_allowed', 'form_content_allowed', 'network_transport_introduced', 'persistent_storage', 'cross_session_identifier', 'fingerprinting'):
        require(privacy.get(key) is False, f'privacy.{key} debe ser false')
    require(privacy.get('uses_existing_telemetry_adapter') is True, 'debe reutilizar el adaptador de telemetría existente')
    limits = contract.get('semantic_limits', {})
    require(limits and all(value is False for value in limits.values()), 'ningún resultado externo puede declararse conocido')
    observation = contract.get('observation', {})
    threshold = observation.get('minimum_intersection_ratio')
    require(threshold == 0.05, 'el umbral observable debe permanecer en 0.05')
    require('viewport móvil' in observation.get('meaning', ''), 'el contrato debe explicar la geometría móvil')

    stages = contract.get('stages', [])
    require([item.get('code') for item in stages] == ['awareness','need','offer','evidence','decision','contact','handoff'], 'orden semántico del funnel inválido')
    require([item.get('rank') for item in stages] == list(range(7)), 'ranks del funnel inválidos')

    require(text.count('<link rel="stylesheet" href="funnel-trust-v529.css">') == 1, 'CSS v5.29 debe cargarse una vez')
    require(text.count('<script defer src="funnel-observability-v529.js"></script>') == 1, 'runtime home v5.29 debe cargarse una vez')
    require(text.count('data-funnel-trust-v529="true"') == 1, 'debe existir una sola señal de confianza')
    require('<aside class="decision-trust-v529"' in text, 'la confianza debe ser aside contextual, no una nueva section')
    commercial = text.find('<!-- COMMERCIAL-V43:END -->')
    trust = text.find('data-funnel-trust-v529="true"')
    contact = text.find('id="contacto" data-conversion-path-v528="true"')
    sectors = text.find('id="sectores"')
    require(min(commercial, trust, contact, sectors) >= 0 and commercial < trust < contact < sectors, 'orden debe ser contratación → confianza → contacto → profundidad')

    director = authority['director']
    degree = director['education'][0]
    role = authority['roles'][0]
    for expected in (degree['credential'], degree['institution'], degree['year'], role['role'], role['organization'], role['period'], authority['boundaries']['copy']):
        require(str(expected) in text, f'la señal de confianza no refleja la fuente v5.25: {expected}')
    require('lista de clientes' in text.lower(), 'debe conservarse frontera explícita sobre clientes')
    require('resultados' in text.lower(), 'debe conservarse frontera explícita sobre resultados')

    anchor = '<script defer src="handoff-observability-v518.js"></script>'
    runtime = '<script defer src="funnel-observability-v529.js"></script>'
    require(text.find(anchor) < text.find(runtime), 'runtime home v5.29 debe cargar después de observabilidad v5.18')
    require(len(DETAIL_TARGETS) == 16, f'se esperaban 16 fichas y hay {len(DETAIL_TARGETS)}')
    for path in DETAIL_TARGETS:
        detail = path.read_text(encoding='utf-8')
        detail_anchor = '<script defer src="../telemetry-v50.js"></script>'
        detail_runtime = '<script defer src="../funnel-observability-v529.js"></script>'
        require(detail.count(detail_runtime) == 1, f'{path.name}: runtime v5.29 debe cargarse una vez')
        require(detail.find(detail_anchor) < detail.find(detail_runtime), f'{path.name}: runtime debe cargar después de telemetry-v50')
        require('data-catalog-id=' in detail, f'{path.name}: falta identidad canónica de oferta')

    for marker in ('window.MeridianoFunnelV529', "'funnel_checkpoint'", 'IntersectionObserver', 'telemetry.snapshot()', "window.addEventListener('meridiano:telemetry'", 'dataset.catalogId', "target: `offer:${catalogId}`", 'const CHECKPOINT_THRESHOLD = 0.05', 'threshold: [CHECKPOINT_THRESHOLD]'):
        require(marker in js, f'runtime carece de {marker}')
    require('intersectionRatio < CHECKPOINT_THRESHOLD' in js, 'runtime debe aplicar el umbral contractual')
    require('intersectionRatio < 0.25' not in js and 'threshold: [0.25]' not in js, 'no debe reaparecer el umbral incompatible con secciones móviles altas')
    for forbidden in ('localStorage', 'sessionStorage', 'indexedDB', 'document.cookie', 'navigator.sendBeacon', 'XMLHttpRequest', 'crypto.randomUUID', 'crypto.getRandomValues'):
        require(forbidden not in js, f'runtime no puede usar {forbidden}')
    require(re.search(r'\bfetch\s*\(', js) is None, 'runtime v5.29 no puede introducir fetch')
    # `contact-form` es una etiqueta semántica heredada de CTA v5.0 y se permite.
    # Lo prohibido es inspeccionar controles o leer valores del formulario.
    for forbidden in ('FormData', 'textarea', 'HTMLInputElement', 'HTMLTextAreaElement', 'HTMLSelectElement', '.value', '.elements', 'querySelector(\'form', 'querySelector("form'):
        require(forbidden not in js, f'runtime v5.29 no puede leer contenido de formulario: {forbidden}')

    for marker in ('.decision-trust-v529', '.decision-trust-evidence-v529', '@media(max-width:760px)', 'overflow-x:auto', 'scroll-snap-type:x proximity'):
        require(marker in css, f'CSS v5.29 carece de {marker}')
    for forbidden in ('display:none', 'visibility:hidden', 'content-visibility:hidden'):
        require(forbidden not in css, f'v5.29 no puede ocultar evidencia con {forbidden}')

    print('FUNNEL + TRUST V5.29 OK: funnel acotado en home + 16 fichas, umbral móvil observable, cero PII/persistencia propia y confianza trazable antes del contacto.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

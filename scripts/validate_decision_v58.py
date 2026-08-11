#!/usr/bin/env python3
"""Valida v5.8: arquitectura de decisión sin duplicar ni contradecir las fuentes jurídicas."""

from __future__ import annotations

from html import escape
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'index.html'
TARGETS = sorted((ROOT / 'servicios').glob('*.html')) + sorted((ROOT / 'productos').glob('*.html'))


def fail(message: str) -> None:
    raise SystemExit(f'DECISION V5.8 FAIL: {message}')


def load_catalog() -> dict[str, dict]:
    out: dict[str, dict] = {}
    paths = sorted((ROOT / 'catalog-products-v41').glob('*.json')) + sorted((ROOT / 'catalog-services-v42').glob('*.json'))
    for path in paths:
        payload = json.loads(path.read_text(encoding='utf-8'))
        if len(payload) != 1:
            fail(f'{path.name} no contiene exactamente una ficha')
        key, value = next(iter(payload.items()))
        out[key] = value
    if len(out) != 16:
        fail(f'se esperaban 16 fuentes y se encontraron {len(out)}')
    return out


def first_title(values) -> str:
    if not values:
        fail('fuente sin datos para resumen ejecutivo')
    item = values[0]
    if isinstance(item, list) and item:
        return str(item[0])
    return str(item)


def validate_home() -> None:
    text = HOME.read_text(encoding='utf-8')
    if text.count('<!-- DECISION-V58-HOME:START -->') != 1 or text.count('<!-- DECISION-V58-HOME:END -->') != 1:
        fail('index.html no contiene exactamente un bloque administrado de portada')
    if text.count('class="engagement-router-card-v58"') != 4:
        fail('la portada debe contener exactamente 4 modalidades de contratación v5.8')
    if 'data-engagement-router-v58="true"' not in text:
        fail('falta selector estable data-engagement-router-v58')
    if '<link rel="stylesheet" href="decision-v58.css">' not in text:
        fail('falta decision-v58.css en portada')
    expected_links = [
        'servicios/diagnostico-juridico-empresarial.html',
        '#productos',
        'servicios/direccion-juridica-externa.html',
        '#servicios',
    ]
    for href in expected_links:
        if f'href="{href}"' not in text:
            fail(f'falta ruta de contratación {href}')
    if 'Objetivo, perímetro, entregables, cronograma, responsabilidades, supuestos, exclusiones y mecanismo de cierre.' not in text:
        fail('falta contrato mínimo de propuesta seria')


def validate_detail(path: Path, catalog: dict[str, dict]) -> None:
    text = path.read_text(encoding='utf-8')
    if text.count('<!-- DECISION-V58-DETAIL:START -->') != 1 or text.count('<!-- DECISION-V58-DETAIL:END -->') != 1:
        fail(f'{path}: bloque v5.8 duplicado o ausente')
    if text.count('class="buying-clarity-card-v58') != 5:
        fail(f'{path}: se esperaban 5 tarjetas de claridad')
    if 'data-buying-clarity-v58="true"' not in text or 'data-decision-v58-cta="true"' not in text:
        fail(f'{path}: faltan selectores estables v5.8')
    if '<link rel="stylesheet" href="../decision-v58.css">' not in text:
        fail(f'{path}: falta decision-v58.css')

    match = re.search(r'data-catalog-id="([^"]+)"', text)
    if not match:
        fail(f'{path}: falta data-catalog-id')
    catalog_id = match.group(1)
    data = catalog.get(catalog_id)
    if data is None:
        fail(f'{path}: {catalog_id} no existe en fuentes')

    checks = [
        ('situations', 'encaje'),
        ('perimeter', 'perímetro'),
        ('deliverables', 'entregables'),
        ('requirements', 'participación del cliente'),
        ('limits', 'límites'),
    ]
    for field, label in checks:
        expected = escape(first_title(data.get(field)))
        if expected not in text:
            fail(f'{path}: el resumen de {label} no coincide con la fuente {field}')

    duration = escape(str(data.get('duration', '')))
    modality = escape(str(data.get('modality', '')))
    audience = escape(str(data.get('audience', '')))
    for value, label in [(duration, 'duración'), (modality, 'modalidad'), (audience, 'audiencia')]:
        if not value or value not in text:
            fail(f'{path}: falta {label} fuente en metadatos v5.8')


def main() -> int:
    if not (ROOT / 'decision-v58.css').exists():
        fail('falta decision-v58.css')
    if len(TARGETS) != 16:
        fail(f'se esperaban 16 fichas HTML y se encontraron {len(TARGETS)}')
    catalog = load_catalog()
    validate_home()
    for path in TARGETS:
        validate_detail(path, catalog)
    print('DECISION V5.8 OK: portada + 16 fichas preservan fuente, alcance y rutas de contratación.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Valida v5.8 y su continuidad semántica en la portada compactada v5.20."""

from __future__ import annotations

from html import escape, unescape
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'index.html'
VERSION = ROOT / 'version.json'
TARGETS = sorted((ROOT / 'servicios').glob('*.html')) + sorted((ROOT / 'productos').glob('*.html'))


def fail(message: str) -> None:
    raise SystemExit(f'DECISION V5.8 FAIL: {message}')


def version_at_least(major: int, minor: int) -> bool:
    payload = json.loads(VERSION.read_text(encoding='utf-8'))
    raw = str(payload.get('version', '0.0.0')).split('.')
    try:
        return (int(raw[0]), int(raw[1])) >= (major, minor)
    except (ValueError, IndexError):
        return False


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


def route_keys(block: str) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for raw_href in re.findall(r'href="([^"]+)"', block):
        parts = urlsplit(unescape(raw_href))
        keys.add((parts.path, parts.fragment))
    return keys


def validate_unified_home_v520(text: str) -> None:
    if text.count('<!-- DECISION-V58-HOME:START -->') or text.count('<!-- DECISION-V58-HOME:END -->'):
        fail('v5.20 final no debe conservar un bloque de decisión v5.8 separado en portada')
    if text.count('data-home-decision-v520="true"') != 1:
        fail('v5.20 final debe contener una única superficie unificada de decisión')
    if text.count('data-engagement-router-v58="true"') != 1:
        fail('v5.20 final debe preservar el selector estable de entrada v5.8 en la superficie unificada')
    if text.count('class="home-decision-entry-v520 engagement-router-card-v58"') != 4:
        fail('v5.20 final debe preservar exactamente cuatro entradas semánticas heredadas de v5.8')
    block_match = re.search(r'<section class="home-decision-v520".*?</section>', text, re.S)
    if not block_match:
        fail('no se pudo aislar la superficie v5.20')
    routes = route_keys(block_match.group(0))
    expected_routes = {
        ('servicios/diagnostico-juridico-empresarial.html', ''),
        ('', 'productos'),
        ('servicios/direccion-juridica-externa.html', ''),
        ('', 'servicios'),
    }
    missing = expected_routes - routes
    if missing:
        fail(f'faltan rutas de contratación heredadas: {sorted(missing)}')


def validate_historical_home_v58(text: str) -> None:
    expected_links = [
        'servicios/diagnostico-juridico-empresarial.html',
        '#productos',
        'servicios/direccion-juridica-externa.html',
        '#servicios',
    ]
    if text.count('<!-- DECISION-V58-HOME:START -->') != 1 or text.count('<!-- DECISION-V58-HOME:END -->') != 1:
        fail('index.html no contiene exactamente un bloque administrado de portada')
    if text.count('class="engagement-router-card-v58"') != 4:
        fail('la portada debe contener exactamente 4 modalidades de contratación v5.8')
    if 'data-engagement-router-v58="true"' not in text:
        fail('falta selector estable data-engagement-router-v58')
    for href in expected_links:
        if f'href="{href}"' not in text:
            fail(f'falta ruta de contratación {href}')


def validate_home() -> None:
    text = HOME.read_text(encoding='utf-8')
    if '<link rel="stylesheet" href="decision-v58.css">' not in text:
        fail('falta decision-v58.css en portada')

    # Release Governance valida v5.8 inmediatamente después de aplicar su capa,
    # antes de que v5.15/v5.20 compacte la portada. Pages valida la salida final.
    # Ambos estados deben conservar el contrato semántico real de v5.8.
    if version_at_least(5, 20) and 'data-home-decision-v520="true"' in text:
        validate_unified_home_v520(text)
    else:
        validate_historical_home_v58(text)

    if 'Objetivo, perímetro, entregables, cronograma, responsabilidades, supuestos, exclusiones y mecanismo de cierre.' not in text:
        fail('falta contrato mínimo de propuesta seria')


def validate_detail(path: Path, catalog: dict[str, dict]) -> None:
    text = path.read_text(encoding='utf-8')
    if text.count('<!-- DECISION-V58-DETAIL:START -->') != 1 or text.count('<!-- DECISION-V58-DETAIL:END -->') != 1:
        fail(f'{path}: bloque v5.8 duplicado o ausente')
    card_count = len(re.findall(r'class="buying-clarity-card-v58(?:\s+[^"]*)?"', text))
    if card_count != 5:
        fail(f'{path}: se esperaban 5 tarjetas de claridad y se encontraron {card_count}')
    if 'data-buying-clarity-v58="true"' not in text or 'data-decision-v58-cta="true"' not in text:
        fail(f'{path}: faltan selectores estables v5.8')
    if '<link rel="stylesheet" href="../decision-v58.css">' not in text:
        fail(f'{path}: falta decision-v58.css')

    runtime_safe = re.search(
        r'<main id="contenido">\s*'
        r'<!-- DECISION-V58-DETAIL:START -->[\s\S]*?<!-- DECISION-V58-DETAIL:END -->\s*'
        r'<div id="detail-page" data-static-catalog="true">',
        text,
    )
    if not runtime_safe:
        fail(f'{path}: el bloque v5.8 debe ser hermano anterior de #detail-page para sobrevivir al render JavaScript')

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
    print('DECISION V5.8 OK: fichas preservadas y continuidad semántica de compra verificada en composición intermedia/final.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

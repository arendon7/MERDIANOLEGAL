#!/usr/bin/env python3
"""Aplica v5.8: arquitectura de decisión de compra sobre portada y 16 fichas profundas."""

from __future__ import annotations

from html import escape
from pathlib import Path
from urllib.parse import quote_plus
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DETAIL_TARGETS = sorted((ROOT / 'servicios').glob('*.html')) + sorted((ROOT / 'productos').glob('*.html'))
HOME = ROOT / 'index.html'
VERSION = ROOT / 'version.json'

HOME_START = '<!-- DECISION-V58-HOME:START -->'
HOME_END = '<!-- DECISION-V58-HOME:END -->'
DETAIL_START = '<!-- DECISION-V58-DETAIL:START -->'
DETAIL_END = '<!-- DECISION-V58-DETAIL:END -->'
HOME_STYLE = '<link rel="stylesheet" href="decision-v58.css">'
DETAIL_STYLE = '<link rel="stylesheet" href="../decision-v58.css">'


def remove_managed_block(text: str, start: str, end: str) -> str:
    pattern = (
        r'(?ms)^[ \t]*' + re.escape(start) + r'[ \t]*\r?\n'
        r'.*?'
        r'^[ \t]*' + re.escape(end) + r'[ \t]*(?:\r?\n)?'
    )
    return re.sub(pattern, '', text, count=1)


def ensure_style(text: str, style: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(style) + r'[ \t]*(?:\r?\n)?', '', text)
    if '</head>' not in text:
        raise RuntimeError('Documento sin cierre </head>')
    return text.replace('</head>', f'  {style}\n</head>', 1)


def version_at_least(major: int, minor: int) -> bool:
    payload = json.loads(VERSION.read_text(encoding='utf-8'))
    raw = str(payload.get('version', '0.0.0')).split('.')
    try:
        return (int(raw[0]), int(raw[1])) >= (major, minor)
    except (ValueError, IndexError):
        return False


def load_catalog() -> dict[str, dict]:
    catalog: dict[str, dict] = {}
    paths = sorted((ROOT / 'catalog-products-v41').glob('*.json')) + sorted((ROOT / 'catalog-services-v42').glob('*.json'))
    for path in paths:
        payload = json.loads(path.read_text(encoding='utf-8'))
        if len(payload) != 1:
            raise RuntimeError(f'{path.name}: se esperaba exactamente una ficha')
        key, value = next(iter(payload.items()))
        if key in catalog:
            raise RuntimeError(f'ID de catálogo duplicado: {key}')
        catalog[key] = value
    if len(catalog) != 16:
        raise RuntimeError(f'Se esperaban 16 fichas fuente y se encontraron {len(catalog)}')
    return catalog


def tuple_titles(values, limit: int) -> list[str]:
    out: list[str] = []
    for item in values or []:
        if isinstance(item, list) and item:
            out.append(str(item[0]))
        elif isinstance(item, str):
            out.append(item)
        if len(out) >= limit:
            break
    return out


def bullet_list(items: list[str]) -> str:
    if not items:
        raise RuntimeError('Bloque v5.8 sin elementos')
    return '<ul>' + ''.join(f'<li>{escape(item)}</li>' for item in items) + '</ul>'


def build_detail_block(data: dict) -> str:
    title = str(data['title'])
    type_label = str(data.get('type', 'Solución jurídica'))
    duration = str(data.get('duration', 'Por definir'))
    modality = str(data.get('modality', 'Alcance por definir'))
    audience = str(data.get('audience', 'Empresa'))

    fit = tuple_titles(data.get('situations'), 2)
    perimeter = tuple_titles(data.get('perimeter'), 3)
    deliverables = tuple_titles(data.get('deliverables'), 3)
    requirements = tuple_titles(data.get('requirements'), 2)
    limits = tuple_titles(data.get('limits'), 2)

    context = quote_plus(f'{type_label}: {title}')
    need = quote_plus(title)
    cta = f'../index.html?context={context}&need={need}#contacto'

    return f'''{DETAIL_START}
<section class="buying-clarity-v58" data-buying-clarity-v58="true" aria-labelledby="buying-clarity-v58-title">
  <div class="container">
    <div class="buying-clarity-head-v58">
      <div>
        <p class="eyebrow">LECTURA EJECUTIVA DEL ALCANCE</p>
        <h2 id="buying-clarity-v58-title">¿Es esta la modalidad correcta para su necesidad?</h2>
        <p>Antes del detalle técnico, este resumen muestra encaje, perímetro, salidas, participación del cliente y límites usando exactamente la fuente jurídica de esta ficha.</p>
      </div>
      <a class="buying-clarity-cta-v58" data-decision-v58-cta="true" href="{cta}">Solicitar propuesta con este alcance →</a>
    </div>
    <div class="buying-clarity-grid-v58">
      <article class="buying-clarity-card-v58"><span>01 · ENCAJA SI</span><h3>Hay una necesidad reconocible</h3>{bullet_list(fit)}</article>
      <article class="buying-clarity-card-v58"><span>02 · QUÉ COMPRA</span><h3>Perímetro estándar</h3>{bullet_list(perimeter)}</article>
      <article class="buying-clarity-card-v58"><span>03 · QUÉ RECIBE</span><h3>Salidas verificables</h3>{bullet_list(deliverables)}</article>
      <article class="buying-clarity-card-v58"><span>04 · QUÉ APORTA</span><h3>Participación del cliente</h3>{bullet_list(requirements)}</article>
      <article class="buying-clarity-card-v58 is-boundary"><span>05 · QUÉ NO ASUMIR</span><h3>Límites principales</h3>{bullet_list(limits)}</article>
    </div>
    <div class="buying-clarity-meta-v58" aria-label="Datos de contratación"><span>{escape(duration)}</span><span>{escape(modality)}</span><span>{escape(audience)}</span></div>
  </div>
</section>
{DETAIL_END}'''


def patch_detail(path: Path, catalog: dict[str, dict]) -> None:
    text = path.read_text(encoding='utf-8')
    match = re.search(r'data-catalog-id="([^"]+)"', text)
    if not match:
        raise RuntimeError(f'{path.name}: falta data-catalog-id')
    catalog_id = match.group(1)
    if catalog_id not in catalog:
        raise RuntimeError(f'{path.name}: ID {catalog_id} no existe en las fuentes')

    # Una composición futura puede conservar v5.8 dentro de profundidad progresiva.
    # En ese caso v5.8 ya está materializado y no debe intentar volver a insertarse
    # sobre el wrapper futuro; el validator histórico sigue comprobando el bloque.
    if 'data-experience-system="v6"' in text:
        if text.count(DETAIL_START) != 1 or text.count(DETAIL_END) != 1:
            raise RuntimeError(f'{path.name}: v6 debe preservar exactamente un bloque v5.8')
        text = ensure_style(text, DETAIL_STYLE)
        path.write_text(text, encoding='utf-8')
        return

    text = remove_managed_block(text, DETAIL_START, DETAIL_END)
    anchor = re.compile(r'<main id="contenido">\s*<div id="detail-page" data-static-catalog="true">')
    replacement = (
        '<main id="contenido">\n'
        + build_detail_block(catalog[catalog_id])
        + '\n<div id="detail-page" data-static-catalog="true">'
    )
    text, count = anchor.subn(lambda _match: replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f'{path.name}: falta ancla canónica del cuerpo')
    text = ensure_style(text, DETAIL_STYLE)
    path.write_text(text, encoding='utf-8')


def home_block() -> str:
    return f'''{HOME_START}
<section class="engagement-router-v58" data-engagement-router-v58="true" aria-labelledby="engagement-router-v58-title">
  <div class="container">
    <div class="section-heading centered">
      <p class="eyebrow dark">FORMA DE CONTRATAR</p>
      <h2 id="engagement-router-v58-title">No todas las necesidades jurídicas deben comprarse de la misma manera.</h2>
      <p>Elija el punto de entrada según el grado de claridad que ya tiene, el resultado que necesita y si la demanda es puntual o recurrente.</p>
    </div>
    <div class="engagement-router-grid-v58">
      <a class="engagement-router-card-v58" href="servicios/diagnostico-juridico-empresarial.html"><span>Explorar primero</span><h3>Necesito entender el problema</h3><p>Hay señales, riesgos o decisiones pendientes, pero todavía no está claro el perímetro correcto ni qué trabajo debe contratarse.</p><b>Ver Diagnóstico Jurídico Empresarial →</b></a>
      <a class="engagement-router-card-v58" href="#productos"><span>Resultado cerrado</span><h3>Sé qué resultado quiero recibir</h3><p>La necesidad permite definir cantidades, entregables, cronograma, criterios de aceptación y límites desde el inicio.</p><b>Comparar productos de alcance cerrado →</b></a>
      <a class="engagement-router-card-v58" href="servicios/direccion-juridica-externa.html"><span>Capacidad recurrente</span><h3>Necesito dirección jurídica continua</h3><p>La empresa tiene una demanda periódica que exige priorización, seguimiento y criterio integrado, no una colección de consultas aisladas.</p><b>Ver Dirección Jurídica Externa →</b></a>
      <a class="engagement-router-card-v58" href="#servicios"><span>Asunto especializado</span><h3>Tengo una decisión o proyecto complejo</h3><p>El objetivo está identificado, pero el alcance debe adaptarse a hechos, negociación, regulación, actores o especialidades del caso.</p><b>Explorar servicios especializados →</b></a>
    </div>
    <div class="engagement-router-note-v58"><strong>Qué debe traer una propuesta seria</strong><p>Objetivo, perímetro, entregables, cronograma, responsabilidades, supuestos, exclusiones y mecanismo de cierre. Meridiano usa esos elementos para que el cliente pueda comparar alcance y no solo una cifra.</p></div>
  </div>
</section>
{HOME_END}'''


def patch_home() -> None:
    text = HOME.read_text(encoding='utf-8')
    # En v6 el bloque v5.8 vive dentro de la profundidad legacy. No lo removemos.
    if 'data-experience-system="v6"' in text:
        if text.count(HOME_START) != 1 or text.count(HOME_END) != 1:
            raise RuntimeError('index.html: v6 debe preservar exactamente un bloque Home v5.8')
        text = ensure_style(text, HOME_STYLE)
        HOME.write_text(text, encoding='utf-8')
        return

    text = remove_managed_block(text, HOME_START, HOME_END)
    if version_at_least(5, 20) and 'data-home-decision-v520="true"' in text:
        text = ensure_style(text, HOME_STYLE)
        HOME.write_text(text, encoding='utf-8')
        return
    anchor = '<section class="section needs-section" id="necesidades">'
    if anchor not in text:
        raise RuntimeError('index.html: falta ancla de necesidades')
    text = text.replace(anchor, home_block() + '\n' + anchor, 1)
    text = ensure_style(text, HOME_STYLE)
    HOME.write_text(text, encoding='utf-8')


def main() -> int:
    if len(DETAIL_TARGETS) != 16:
        raise RuntimeError(f'Se esperaban 16 fichas profundas y se encontraron {len(DETAIL_TARGETS)}')
    catalog = load_catalog()
    patch_home()
    for path in DETAIL_TARGETS:
        patch_detail(path, catalog)
    print('DECISION V5.8 OK: portada + 16 fichas con arquitectura ejecutiva de compra.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Materializa v5.25: autoridad profesional visible y trazable sin social proof ficticio."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
FIRM = ROOT / "firma.html"
SOURCE = ROOT / "professional-authority-v525.json"
CONFIG = ROOT / "site-config.json"
CSS_HOME = '<link rel="stylesheet" href="professional-authority-v525.css">'
CSS_FIRM = '<link rel="stylesheet" href="professional-authority-v525.css">'
HOME_START = '<!-- PROFESSIONAL-AUTHORITY-V525-HOME:START -->'
HOME_END = '<!-- PROFESSIONAL-AUTHORITY-V525-HOME:END -->'
FIRM_START = '<!-- PROFESSIONAL-AUTHORITY-V525-FIRM:START -->'
FIRM_END = '<!-- PROFESSIONAL-AUTHORITY-V525-FIRM:END -->'


def strip_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r'.*?' + re.escape(end) + r'\s*', '', text, flags=re.S)


def ensure_css(text: str) -> str:
    text = re.sub(r'(?m)^\s*' + re.escape(CSS_HOME) + r'\s*$', '', text)
    return text.replace('</head>', f'  {CSS_HOME}\n</head>', 1)


def esc(value: object) -> str:
    import html
    return html.escape(str(value), quote=True)


def home_block(data: dict) -> str:
    director = data['director']
    roles = data['roles']
    degree = director['education'][0]
    return f'''{HOME_START}
<div class="professional-proof-v525 authority-home-v525" data-professional-authority-v525="home" aria-label="Trayectoria profesional del director">
  <div class="professional-proof-grid-v525">
    <article><strong>{esc(degree['credential'])} · {esc(degree['institution'])}</strong><span>Graduado en {esc(degree['year'])}</span></article>
    <article><strong>{esc(roles[0]['role'])}</strong><span>{esc(roles[0]['organization'])} · {esc(roles[0]['period'])}</span></article>
    <article><strong>Gerencia y consultoría de proyectos</strong><span>{esc(roles[1]['organization'])} · {esc(roles[2]['organization'])}</span></article>
  </div>
  <p class="professional-proof-note-v525">Trayectoria profesional del director; no corresponde a una lista de clientes de Meridiano Legal.</p>
  <a class="professional-proof-link-v525" href="firma.html#trayectoria">Ver trayectoria profesional →</a>
</div>
{HOME_END}'''


def firm_block(data: dict) -> str:
    director = data['director']
    edu = director['education']
    roles_html = ''.join(
        f'''<article class="authority-role-v525"><span>{esc(item['period'])}</span><div><h3>{esc(item['organization'])}<small>{esc(item['role'])} · {esc(item['sector'])}</small></h3><p>{esc(item['focus'])}</p></div></article>'''
        for item in data['roles']
    )
    matters_html = ''.join(
        f'''<article><strong>{esc(item['title'])}</strong><p>{esc(item['copy'])}</p></article>'''
        for item in data['representative_matters']
    )
    return f'''{FIRM_START}
<section class="section professional-authority-v525" id="trayectoria" data-professional-authority-v525="firm">
  <div class="container">
    <div class="authority-intro-v525"><div><p class="eyebrow dark">TRAYECTORIA PROFESIONAL</p><h2>La experiencia que informa el criterio de Meridiano.</h2></div><div class="prose"><p class="intro">La práctica del director combina experiencia desde funciones jurídicas internas, gerencia y consultoría de proyectos. La trayectoria se presenta por roles y asuntos documentados, sin convertirla en una colección de logos o resultados no atribuibles.</p><p>Esta experiencia antecede y acompaña la construcción de Meridiano Legal; no implica que todas las organizaciones o asuntos hayan sido clientes de la firma.</p></div></div>
    <div class="authority-credentials-v525" aria-label="Credenciales profesionales">
      <article><b>Formación</b><strong>{esc(edu[0]['credential'])}</strong><span>{esc(edu[0]['institution'])} · {esc(edu[0]['year'])}</span></article>
      <article><b>Formación de posgrado</b><strong>{esc(edu[1]['credential'])}</strong><span>{esc(edu[1]['institution'])}</span></article>
      <article><b>Idiomas</b><strong>{esc(' · '.join(director['languages']))}</strong><span>{esc(director['base'])}</span></article>
    </div>
    <div class="authority-timeline-v525" aria-label="Trayectoria seleccionada">{roles_html}</div>
    <div class="authority-matters-v525"><p class="eyebrow dark">ASUNTOS REPRESENTATIVOS DE LA TRAYECTORIA</p><div class="authority-matters-grid-v525">{matters_html}</div></div>
    <div class="authority-boundary-v525"><strong>Alcance de esta información.</strong> {esc(data['boundaries']['copy'])}</div>
  </div>
</section>
{FIRM_END}'''


def update_person_schema(text: str, data: dict, base_url: str) -> str:
    pattern = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
    director_id = base_url + '#director'
    organization_id = base_url + '#organization'
    matters = [item['title'] for item in data['representative_matters']]
    director = data['director']
    degree = director['education'][0]

    for match in pattern.finditer(text):
        try:
            payload = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue
        graph = payload.get('@graph') if isinstance(payload, dict) else None
        if not isinstance(graph, list):
            continue
        org = next((item for item in graph if isinstance(item, dict) and item.get('@id') == organization_id), None)
        person = next((item for item in graph if isinstance(item, dict) and item.get('@id') == director_id), None)
        if org is None:
            continue
        org['founder'] = {'@id': director_id}
        if person is None:
            person = {'@type': 'Person', '@id': director_id}
            graph.append(person)
        person.update({
            'name': director['name'],
            'jobTitle': director['role'],
            'worksFor': {'@id': organization_id},
            'alumniOf': {'@type': 'CollegeOrUniversity', 'name': degree['institution']},
            'knowsAbout': matters,
            'address': {'@type': 'PostalAddress', 'addressLocality': 'Medellín', 'addressCountry': 'CO'},
        })
        rendered = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))
        return text[:match.start()] + f'<script type="application/ld+json">{rendered}</script>' + text[match.end():]
    raise RuntimeError('No se encontró Organization JSON-LD para enlazar autoridad v5.25')


def main() -> int:
    data = json.loads(SOURCE.read_text(encoding='utf-8'))
    if data.get('version') != '5.25.0':
        raise RuntimeError('professional-authority-v525.json debe declarar 5.25.0')
    base_url = json.loads(CONFIG.read_text(encoding='utf-8'))['base_url'].rstrip('/') + '/'

    home = strip_block(HOME.read_text(encoding='utf-8'), HOME_START, HOME_END)
    home = ensure_css(home)
    anchor = '<div class="statement-grid">'
    if anchor not in home:
        raise RuntimeError('index.html: no se encontró statement-grid de La firma')
    home = home.replace(anchor, home_block(data) + '\n' + anchor, 1)
    home = home.replace('href="firma.html">Conocer la firma y su método</a>', 'href="firma.html#trayectoria">Ver trayectoria y método</a>', 1)
    home = update_person_schema(home, data, base_url)
    HOME.write_text(home, encoding='utf-8')

    firm = strip_block(FIRM.read_text(encoding='utf-8'), FIRM_START, FIRM_END)
    firm = ensure_css(firm)
    firm = firm.replace('<a href="#enfoque">Enfoque</a>', '<a href="#enfoque">Enfoque</a><a href="#trayectoria">Trayectoria</a>', 1)
    firm = firm.replace('href="experiencia.html">Ver experiencia demostrativa</a>', 'href="#trayectoria">Ver trayectoria profesional</a>', 1)
    firm_anchor = '    <section class="section" id="enfoque">'
    if firm_anchor not in firm:
        raise RuntimeError('firma.html: no se encontró sección de enfoque')
    firm = firm.replace(firm_anchor, firm_block(data) + '\n' + firm_anchor, 1)
    firm = update_person_schema(firm, data, base_url)
    FIRM.write_text(firm, encoding='utf-8')

    from validate_professional_authority_v525 import validate_materialized
    validate_materialized(data)
    print('PROFESSIONAL AUTHORITY V5.25 OK: fuente trazable materializada en portada y firma sin social proof ficticio.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Valida v5.25: autoridad profesional trazable sin clientes, testimonios o resultados inventados."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'index.html'
FIRM = ROOT / 'firma.html'
DEMO = ROOT / 'experiencia.html'
SOURCE = ROOT / 'professional-authority-v525.json'
CONFIG = ROOT / 'site-config.json'
HOME_START = '<!-- PROFESSIONAL-AUTHORITY-V525-HOME:START -->'
HOME_END = '<!-- PROFESSIONAL-AUTHORITY-V525-HOME:END -->'
FIRM_START = '<!-- PROFESSIONAL-AUTHORITY-V525-FIRM:START -->'
FIRM_END = '<!-- PROFESSIONAL-AUTHORITY-V525-FIRM:END -->'
FORBIDDEN = (
    'casos de éxito',
    'clientes satisfechos',
    'mejor firma',
    'líder del mercado',
    'garantizamos resultados',
    'garantía de resultado',
    'años de experiencia',
)
EXPECTED_ROLES = (
    ('2023–actualidad', 'Greenatics S.A.S.', 'Director Jurídico y Administrativo'),
    ('2022–2023', 'Herbalgem S.A.S.', 'Gerente General'),
    ('2020–2023', 'Grupo Pineal S.A.S.', 'Consultor Jurídico y de Proyectos'),
    ('2018–2019', 'Incubik', 'Experiencia profesional'),
    ('2017–2018', 'Compañía de Empaques', 'Experiencia profesional'),
)


def fail(message: str) -> None:
    raise SystemExit(f'PROFESSIONAL AUTHORITY V5.25 ERROR: {message}')


def extract(text: str, start: str, end: str) -> str:
    match = re.search(re.escape(start) + r'(.*?)' + re.escape(end), text, re.S)
    if not match:
        fail(f'falta bloque {start}')
    return match.group(1)


def jsonld_graphs(text: str) -> list[list[dict]]:
    graphs: list[list[dict]] = []
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue
        graph = payload.get('@graph') if isinstance(payload, dict) else None
        if isinstance(graph, list):
            graphs.append(graph)
    return graphs


def validate_source(data: dict) -> None:
    if data.get('version') != '5.25.0':
        fail('la fuente debe declarar version 5.25.0')
    director = data.get('director') or {}
    if director.get('name') != 'Agustín Rendón Calle':
        fail('nombre del director inesperado')
    education = director.get('education') or []
    if len(education) != 2:
        fail('se esperaban dos entradas de formación')
    if education[0].get('institution') != 'Universidad EAFIT' or education[0].get('year') != '2018':
        fail('credencial EAFIT 2018 ausente o alterada')
    if education[1].get('institution') != 'UNIR, España' or education[1].get('status') != 'postgraduate_training':
        fail('la formación de posgrado debe mantenerse como formación, no como título completado')
    roles = data.get('roles') or []
    if len(roles) != len(EXPECTED_ROLES):
        fail('la trayectoria debe contener exactamente cinco entradas documentadas')
    observed = tuple((r.get('period'), r.get('organization'), r.get('role')) for r in roles)
    if observed != EXPECTED_ROLES:
        fail('periodos, organizaciones o roles se apartaron de la fuente aprobada')
    matters = data.get('representative_matters') or []
    if len(matters) != 4 or not all(m.get('title') and m.get('copy') for m in matters):
        fail('se requieren exactamente cuatro grupos de asuntos representativos')
    boundaries = data.get('boundaries') or {}
    for key in ('not_client_list', 'no_testimonials', 'no_success_metrics', 'no_result_guarantees'):
        if boundaries.get(key) is not True:
            fail(f'boundary {key} debe permanecer activa')
    corpus = json.dumps(data, ensure_ascii=False).lower()
    for phrase in FORBIDDEN:
        if phrase in corpus:
            fail(f'claim prohibido en fuente: {phrase}')


def validate_schema(text: str, data: dict, label: str) -> None:
    base = json.loads(CONFIG.read_text(encoding='utf-8'))['base_url'].rstrip('/') + '/'
    director_id = base + '#director'
    organization_id = base + '#organization'
    graphs = jsonld_graphs(text)
    if not graphs:
        fail(f'{label}: no hay @graph JSON-LD')
    matches = []
    for graph in graphs:
        org = next((item for item in graph if isinstance(item, dict) and item.get('@id') == organization_id), None)
        person = next((item for item in graph if isinstance(item, dict) and item.get('@id') == director_id), None)
        if org and person:
            matches.append((org, person))
    if len(matches) != 1:
        fail(f'{label}: debe existir exactamente un grafo Organization ↔ Person')
    org, person = matches[0]
    if org.get('founder') != {'@id': director_id}:
        fail(f'{label}: Organization.founder no enlaza al director')
    if person.get('name') != data['director']['name'] or person.get('jobTitle') != data['director']['role']:
        fail(f'{label}: identidad Person desalineada')
    alumni = person.get('alumniOf') or {}
    if alumni.get('name') != 'Universidad EAFIT':
        fail(f'{label}: Person.alumniOf debe conservar Universidad EAFIT')
    if len(person.get('knowsAbout') or []) != 4:
        fail(f'{label}: Person.knowsAbout debe derivar de cuatro asuntos representativos')


def validate_materialized(data: dict | None = None) -> None:
    data = data or json.loads(SOURCE.read_text(encoding='utf-8'))
    validate_source(data)
    home = HOME.read_text(encoding='utf-8')
    firm = FIRM.read_text(encoding='utf-8')
    demo = DEMO.read_text(encoding='utf-8')

    if home.count(HOME_START) != 1 or home.count(HOME_END) != 1:
        fail('index.html: bloque home v5.25 duplicado o ausente')
    if firm.count(FIRM_START) != 1 or firm.count(FIRM_END) != 1:
        fail('firma.html: bloque firm v5.25 duplicado o ausente')
    if home.count('<link rel="stylesheet" href="professional-authority-v525.css">') != 1:
        fail('index.html: CSS v5.25 debe cargarse una vez')
    if firm.count('<link rel="stylesheet" href="professional-authority-v525.css">') != 1:
        fail('firma.html: CSS v5.25 debe cargarse una vez')

    home_block = extract(home, HOME_START, HOME_END)
    firm_block = extract(firm, FIRM_START, FIRM_END)
    for required in ('Universidad EAFIT', '2018', 'Greenatics S.A.S.', 'firma.html#trayectoria'):
        if required not in home_block:
            fail(f'index.html: falta prueba profesional {required!r}')
    if 'no corresponde a una lista de clientes' not in home_block.lower():
        fail('index.html: falta frontera explícita de no-client-list')
    if 'id="trayectoria"' not in firm_block:
        fail('firma.html: falta #trayectoria')
    if 'href="#trayectoria">Ver trayectoria profesional</a>' not in firm:
        fail('firma.html: hero debe priorizar trayectoria profesional')
    if 'href="#trayectoria">Trayectoria</a>' not in firm:
        fail('firma.html: navegación debe incluir trayectoria')

    for period, organization, role in EXPECTED_ROLES:
        for token in (period, organization, role):
            if token not in firm_block:
                fail(f'firma.html: falta dato documentado {token!r}')
    for matter in data['representative_matters']:
        if matter['title'] not in firm_block:
            fail(f'firma.html: falta asunto representativo {matter["title"]!r}')
    if data['boundaries']['copy'] not in re.sub(r'&amp;', '&', firm_block):
        fail('firma.html: falta boundary de trayectoria')
    if '<img' in firm_block.lower() or '<blockquote' in firm_block.lower():
        fail('firma.html: v5.25 no debe simular logos, retratos de terceros o testimonios')

    combined = (home_block + firm_block).lower()
    for phrase in FORBIDDEN:
        if phrase in combined:
            fail(f'claim prohibido materializado: {phrase}')

    if '<meta name="robots" content="noindex,follow">' not in demo or 'Todos los escenarios, nombres, cifras y resultados son ficticios.' not in demo:
        fail('experiencia.html: la demostración debe conservar noindex y frontera ficticia')

    validate_schema(home, data, 'index.html')
    validate_schema(firm, data, 'firma.html')


def main() -> int:
    validate_materialized()
    print('PROFESSIONAL AUTHORITY V5.25 OK: trayectoria documentada, schema Person coherente y cero social proof ficticio.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Aplica la capa editorial y demostrativa UX/UI v4.7 de forma idempotente."""

from pathlib import Path
from urllib.parse import quote_plus
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'version.json').read_text(encoding='utf-8'))['version']
PERSPECTIVE_DIR = ROOT / 'perspectivas'
SECTOR_DIR = ROOT / 'sectores'
PERSPECTIVES = sorted(PERSPECTIVE_DIR.glob('*.html'))
SECTORS = sorted(SECTOR_DIR.glob('*.html'))
ROOT_PAGES = [ROOT / 'firma.html', ROOT / 'perspectivas.html', ROOT / 'experiencia.html', ROOT / 'demo.html']
TARGETS = ROOT_PAGES + PERSPECTIVES + SECTORS

MENU_START = '<!-- EDITORIAL-V47-MENU:START -->'
MENU_END = '<!-- EDITORIAL-V47-MENU:END -->'
MOBILE_START = '<!-- EDITORIAL-V47-MOBILE:START -->'
MOBILE_END = '<!-- EDITORIAL-V47-MOBILE:END -->'
SECTOR_NAV_START = '<!-- EDITORIAL-V47-SECTOR-NAV:START -->'
SECTOR_NAV_END = '<!-- EDITORIAL-V47-SECTOR-NAV:END -->'
CONVERSION_START = '<!-- EDITORIAL-V47-CONVERSION:START -->'
CONVERSION_END = '<!-- EDITORIAL-V47-CONVERSION:END -->'
TRUST_START = '<!-- EDITORIAL-V47-TRUST:START -->'
TRUST_END = '<!-- EDITORIAL-V47-TRUST:END -->'
DEMO_GUIDE_START = '<!-- EDITORIAL-V47-DEMO-GUIDE:START -->'
DEMO_GUIDE_END = '<!-- EDITORIAL-V47-DEMO-GUIDE:END -->'

FIRM_SECTORS = {
    'Tecnología, software e IA': 'sectores/tecnologia-software-ia.html',
    'Servicios públicos, aseo y economía circular': 'sectores/servicios-publicos-aseo-economia-circular.html',
    'Agroindustria, fertilizantes y sostenibilidad': 'sectores/agroindustria-fertilizantes-sostenibilidad.html',
    'Salud y negocios regulados': 'sectores/salud-negocios-regulados.html',
    'Comercio y distribución': 'sectores/comercio-distribucion.html',
    'Startups e inversión': 'sectores/startups-inversion.html',
    'Proyectos públicos y territoriales': 'sectores/proyectos-publicos-territoriales.html',
    'Legal Operations': 'sectores/operaciones-juridicas.html',
}

PERSPECTIVE_SLUGS = [
    'gobierno-juridico-inteligencia-artificial.html',
    'contratos-administrables.html',
    'proyectos-regulados-secuencia-viabilidad.html',
    'propiedad-intelectual-cadena-titularidad.html',
    'socios-inversion-gobierno.html',
    'legal-operations-modelo-operativo.html',
]
DUPLICATE_LIBRARY_SLUGS = PERSPECTIVE_SLUGS[:3]


def remove_block(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r'[\s\S]*?' + re.escape(end), '', text, count=1)


def strip_managed_line(text: str, pattern: str) -> str:
    return re.sub(r'(?m)^[ \t]*' + pattern + r'[ \t]*\n?', '', text)


def root_prefix(path: Path) -> str:
    return '../' if path.parent != ROOT else ''


def ensure_body_metadata(text: str, path: Path) -> str:
    text = re.sub(r'\sdata-editorial-v47="true"', '', text, count=1)
    if path.name == 'perspectivas.html' and path.parent == ROOT:
        text = text.replace('<body>', '<body data-page-type="Perspectivas" data-page-title="Biblioteca de perspectivas" data-page-need="Otra necesidad">', 1)
    elif path.name == 'experiencia.html':
        text = text.replace('<body class="experience-body">', '<body class="experience-body" data-page-type="Centro demo" data-page-title="Centro de demostración" data-page-need="Otra necesidad">', 1)
    elif path.name == 'demo.html':
        text = text.replace('<body class="demo-page">', '<body class="demo-page" data-page-type="Demo" data-page-title="Meridiano Empresas" data-page-need="Otra necesidad">', 1)
    text = re.sub(r'<body([^>]*)>', lambda m: '<body' + m.group(1) + ' data-editorial-v47="true">', text, count=1)
    return text


def page_context(text: str) -> tuple[str, str, str]:
    def attr(name: str, fallback: str) -> str:
        match = re.search(fr'{name}="([^"]+)"', text)
        return html.unescape(match.group(1)) if match else fallback
    return attr('data-page-type', 'Página'), attr('data-page-title', 'Meridiano Legal'), attr('data-page-need', 'Otra necesidad')


def contact_href(path: Path, text: str) -> str:
    page_type, title, need = page_context(text)
    context = quote_plus(f'{page_type}: {title}')
    return f'{root_prefix(path)}index.html?context={context}&need={quote_plus(need)}#contacto'


def add_assets(text: str, path: Path) -> str:
    prefix = root_prefix(path)
    text = strip_managed_line(text, r'<link rel="stylesheet" href="(?:\.\./)?editorial-v47\.css">')
    text = strip_managed_line(text, r'<script defer src="(?:\.\./)?editorial-v47\.js"></script>')
    if '</head>' not in text or '</body>' not in text:
        raise RuntimeError(f'{path}: HTML incompleto')
    text = text.replace('</head>', f'  <link rel="stylesheet" href="{prefix}editorial-v47.css">\n</head>', 1)
    text = text.replace('</body>', f'  <script defer src="{prefix}editorial-v47.js"></script>\n</body>', 1)
    return text


def add_menu(text: str, path: Path) -> str:
    if path.name == 'demo.html':
        return text
    text = remove_block(text, MENU_START, MENU_END)
    text = text.replace(' editorial-nav-v47', '').replace(' id="editorial-nav-v47"', '')
    nav_match = re.search(r'<nav class="(firm-nav|insight-nav|sector-nav|experience-nav)"', text)
    if not nav_match:
        raise RuntimeError(f'{path}: no se encontró navegación para v4.7')
    nav_class = nav_match.group(1)
    old = f'<nav class="{nav_class}"'
    menu = f'{MENU_START}\n<button class="editorial-menu-toggle-v47" type="button" aria-expanded="false" aria-controls="editorial-nav-v47" aria-label="Abrir menú"><span></span><span></span><span></span><span class="sr-only">Abrir menú</span></button>\n{MENU_END}\n'
    new = menu + f'<nav class="{nav_class} editorial-nav-v47" id="editorial-nav-v47"'
    return text.replace(old, new, 1)


def add_mobile_cta(text: str, path: Path) -> str:
    text = remove_block(text, MOBILE_START, MOBILE_END)
    prefix = root_prefix(path)
    if path.name == 'demo.html':
        primary_href, primary_label = 'experiencia.html', 'Centro demo'
        secondary_href, secondary_label = 'index.html', 'Volver a la web'
    elif path.name == 'experiencia.html':
        primary_href, primary_label = contact_href(path, text), 'Presentar necesidad'
        secondary_href, secondary_label = 'demo.html', 'Abrir Empresas'
    elif path.name == 'firma.html':
        primary_href, primary_label = contact_href(path, text), 'Presentar necesidad'
        secondary_href, secondary_label = 'experiencia.html', 'Centro demo'
    elif path.name == 'perspectivas.html' and path.parent == ROOT:
        primary_href, primary_label = contact_href(path, text), 'Presentar necesidad'
        secondary_href, secondary_label = 'index.html#servicios', 'Ver servicios'
    elif path.parent == PERSPECTIVE_DIR:
        primary_href, primary_label = contact_href(path, text), 'Presentar necesidad'
        secondary_href, secondary_label = '../perspectivas.html', 'Más perspectivas'
    elif path.parent == SECTOR_DIR:
        primary_href, primary_label = contact_href(path, text), 'Presentar necesidad'
        secondary_href, secondary_label = '../index.html#sectores', 'Otros sectores'
    else:
        primary_href, primary_label = f'{prefix}index.html#contacto', 'Presentar necesidad'
        secondary_href, secondary_label = f'{prefix}index.html', 'Inicio'
    block = f'''{MOBILE_START}\n<div class="editorial-mobile-cta-v47" aria-label="Acciones rápidas"><a href="{primary_href}">{primary_label}</a><a href="{secondary_href}">{secondary_label}</a></div>\n{MOBILE_END}\n'''
    return text.replace('</body>', block + '</body>', 1)


def patch_firm(text: str) -> str:
    text = re.sub(r'<div class="director-mark(?: v47-mark)?"[^>]*>[\s\S]*?</div>', '<div class="director-mark v47-mark" aria-hidden="true"><img src="assets/brand/meridiano-monogram.svg" alt=""></div>', text, count=1)
    text = re.sub(r'<a class="firm-sector-link-v47"[^>]*>[^<]*</a>', '', text)
    for title, href in FIRM_SECTORS.items():
        pattern = r'(<article><strong>' + re.escape(title) + r'</strong><p>[\s\S]*?</p>)(</article>)'
        replacement = r'\1<a class="firm-sector-link-v47" href="' + href + r'">Ver enfoque sectorial</a>\2'
        text, count = re.subn(pattern, replacement, text, count=1)
        if count != 1:
            raise RuntimeError(f'firma.html: no se pudo enlazar el sector {title}')
    return text


def patch_perspectives_index(text: str, path: Path) -> str:
    text = text.replace('href="index.html#contacto"', f'href="{contact_href(path, text)}"')
    marker = '<div class="insights-grid">'
    start = text.find(marker)
    if start < 0:
        raise RuntimeError('perspectivas.html: falta insights-grid')
    end = text.find('</div>', start)
    if end < 0:
        raise RuntimeError('perspectivas.html: cierre de insights-grid no encontrado')
    fragment = text[start:end]
    for slug in DUPLICATE_LIBRARY_SLUGS:
        fragment = re.sub(r'<a class="insight-card"[^>]*href="perspectivas/' + re.escape(slug) + r'"[\s\S]*?</a>', '', fragment, count=1)
    return text[:start] + fragment + text[end:]


def patch_perspective_article(text: str, path: Path) -> str:
    text = remove_block(text, CONVERSION_START, CONVERSION_END)
    marker = '<!-- EDITORIAL-SEQUENCE:START -->'
    if marker not in text:
        raise RuntimeError(f'{path}: falta secuencia editorial')
    href = contact_href(path, text)
    title = page_context(text)[1]
    block = f'''{CONVERSION_START}\n<section class="editorial-conversion-v47" aria-label="Siguiente paso"><div class="container editorial-conversion-grid-v47"><div><h2>¿Esta perspectiva coincide con una decisión abierta en su empresa?</h2><p>Use la lectura para formular la pregunta inicial. El alcance profesional se define con hechos, plazo, actores, evidencia disponible y resultado esperado.</p></div><div class="editorial-conversion-actions-v47"><a href="{href}">Presentar necesidad</a><a href="../perspectivas.html">Volver a la biblioteca</a></div></div></section>\n{CONVERSION_END}\n'''
    text = text.replace(marker, block + marker, 1)
    return text


def patch_sector(text: str, path: Path) -> str:
    text = remove_block(text, SECTOR_NAV_START, SECTOR_NAV_END)
    quicknav = f'''{SECTOR_NAV_START}\n<nav class="sector-quicknav-v47" aria-label="Recorrido sectorial"><div class="container"><span>RECORRIDO SECTORIAL</span><a href="#sector-enfoque">Enfoque</a><a href="#sector-decisiones">Decisiones</a><a href="#sector-riesgos">Riesgos</a><a href="#sector-contacto">Siguiente paso</a></div></nav>\n{SECTOR_NAV_END}'''
    text, count = re.subn(r'</section>\s*<section class="section"(?: id="sector-enfoque")?>', '</section>\n' + quicknav + '\n<section class="section" id="sector-enfoque">', text, count=1)
    if count != 1:
        raise RuntimeError(f'{path}: no se pudo insertar recorrido sectorial')
    text = re.sub(r'<section class="section soft"(?: id="sector-decisiones")?>', '<section class="section soft" id="sector-decisiones">', text, count=1)
    text = re.sub(r'<section class="section ivory"(?: id="sector-riesgos")?>', '<section class="section ivory" id="sector-riesgos">', text, count=1)
    text = re.sub(r'<section class="sector-closing"(?: id="sector-contacto")?>', '<section class="sector-closing" id="sector-contacto">', text, count=1)
    for required in ('id="sector-enfoque"', 'id="sector-decisiones"', 'id="sector-riesgos"', 'id="sector-contacto"'):
        if required not in text:
            raise RuntimeError(f'{path}: falta {required}')
    return text


def patch_experience(text: str, path: Path) -> str:
    text = remove_block(text, TRUST_START, TRUST_END)
    text = remove_block(text, CONVERSION_START, CONVERSION_END)
    trust = f'''{TRUST_START}\n<section class="experience-trust-v47" aria-label="Condiciones de la demostración"><div class="container experience-trust-grid-v47"><article><strong>Datos ficticios</strong><span>Nombres, cifras, expedientes y resultados son exclusivamente demostrativos.</span></article><article><strong>Procesamiento local</strong><span>El simulador opera en el navegador y no envía la hipótesis a un servidor.</span></article><article><strong>Sin carga de información sensible</strong><span>El recorrido no requiere documentos, bases de datos ni expedientes reales.</span></article></div></section>\n{TRUST_END}'''
    text, count = re.subn(r'</section>\s*<section class="experience-index">', '</section>\n' + trust + '\n<section class="experience-index">', text, count=1)
    if count != 1:
        raise RuntimeError('experiencia.html: no se pudo insertar franja de confianza')
    conversion = f'''{CONVERSION_START}\n<section class="experience-conversion-v47"><div class="container experience-conversion-grid-v47"><div><h2>Del recorrido demostrativo a un alcance profesional verificable.</h2><p>Si la lógica de trabajo coincide con su necesidad, presente únicamente el contexto inicial. La revisión de información sensible comienza después de validar alcance, conflicto y canal.</p></div><div class="experience-conversion-actions-v47"><a href="{contact_href(path, text)}">Presentar necesidad</a><a href="demo.html">Abrir Meridiano Empresas</a></div></div></section>\n{CONVERSION_END}\n'''
    if '<footer class="experience-footer">' not in text:
        raise RuntimeError('experiencia.html: falta footer')
    return text.replace('<footer class="experience-footer">', conversion + '<footer class="experience-footer">', 1)


def patch_demo(text: str) -> str:
    text = remove_block(text, DEMO_GUIDE_START, DEMO_GUIDE_END)
    guide = f'''{DEMO_GUIDE_START}\n<section class="demo-guide-v47" aria-label="Cómo usar la demostración"><div class="demo-guide-grid-v47"><strong>RECORRIDO RECOMENDADO</strong><article><strong>1 · Elija un perfil</strong><span>Cliente, abogada o socio director.</span></article><article><strong>2 · Explore módulos</strong><span>Solicitudes, expedientes, documentos, riesgos y analítica.</span></article><article><strong>3 · Regrese al centro demo</strong><span>Compare el portal con entregables y método.</span></article></div></section>\n{DEMO_GUIDE_END}\n'''
    if '</header>' not in text:
        raise RuntimeError('demo.html: falta topbar')
    return text.replace('</header>', '</header>\n' + guide, 1)


def patch(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    text = ensure_body_metadata(text, path)
    text = add_menu(text, path)
    if path.name == 'firma.html' and path.parent == ROOT:
        text = patch_firm(text)
    elif path.name == 'perspectivas.html' and path.parent == ROOT:
        text = patch_perspectives_index(text, path)
    elif path.parent == PERSPECTIVE_DIR:
        text = patch_perspective_article(text, path)
    elif path.parent == SECTOR_DIR:
        text = patch_sector(text, path)
    elif path.name == 'experiencia.html':
        text = patch_experience(text, path)
    elif path.name == 'demo.html':
        text = patch_demo(text)
    text = add_mobile_cta(text, path)
    text = add_assets(text, path)
    path.write_text(text, encoding='utf-8')


def main() -> int:
    if len(PERSPECTIVES) != 6:
        raise RuntimeError(f'Se esperaban 6 perspectivas y se encontraron {len(PERSPECTIVES)}')
    if len(SECTORS) != 8:
        raise RuntimeError(f'Se esperaban 8 sectores y se encontraron {len(SECTORS)}')
    if len(TARGETS) != 18:
        raise RuntimeError(f'Se esperaban 18 páginas v4.7 y se encontraron {len(TARGETS)}')
    for path in TARGETS:
        patch(path)
    print(f'UX/UI editorial y demostrativa v{VERSION} aplicada en {len(TARGETS)} páginas.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

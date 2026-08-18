#!/usr/bin/env python3
"""Meridiano Legal v6: materializa Home y las 16 fichas profundas desde fuentes canónicas.

Wave 2 mantiene íntegro el contenido v5.31 como profundidad accesible. Los catálogos
v4.1/v4.2 siguen siendo la verdad de alcance, entregables, método y límites; el JSON v6
solo aporta Home y overrides editoriales explícitos para superficies piloto.
"""
from __future__ import annotations

from html import escape, unescape
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "experience-system-v60.json"
CONTENT = ROOT / "experience-content-v60.json"
HOME = ROOT / "index.html"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")

HOME_START = "<!-- EXPERIENCE-V60-HOME:START -->"
HOME_END = "<!-- EXPERIENCE-V60-HOME:END -->"
DETAIL_START = "<!-- EXPERIENCE-V60-DETAIL:START -->"
DETAIL_END = "<!-- EXPERIENCE-V60-DETAIL:END -->"
LEGACY_START = "<!-- EXPERIENCE-V60-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-LEGACY:END -->"
COMMERCIAL_START = "<!-- COMMERCIAL-V43:START -->"
COMMERCIAL_END = "<!-- COMMERCIAL-V43:END -->"
FORM_MOVED = '<div class="v6-form-moved-note">El formulario canónico se muestra en el cierre principal v6 de esta página.</div>'

SOLUTION_HREFS = [
    "soluciones/ordenar-riesgo-juridico-empresa.html",
    "soluciones/direccion-juridica-externa-empresa.html",
    "soluciones/gobernar-inteligencia-artificial-empresa.html",
    "soluciones/preparar-empresa-para-inversion.html",
    "soluciones/estructurar-proyecto-regulado.html",
    "soluciones/ordenar-operacion-juridica.html",
]


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


def load_catalog_sources() -> dict[str, dict]:
    sources: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            raise RuntimeError(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            payload = load_json(path)
            if len(payload) != 1:
                raise RuntimeError(f"{path.name}: cada fuente debe declarar exactamente un catalog_id")
            catalog_id, data = next(iter(payload.items()))
            if catalog_id in sources:
                raise RuntimeError(f"catalog_id duplicado: {catalog_id}")
            sources[catalog_id] = data
    if len(sources) != 16:
        raise RuntimeError(f"se esperaban 16 fuentes profundas y hay {len(sources)}")
    return sources


def discover_detail_paths() -> dict[str, Path]:
    result: dict[str, Path] = {}
    paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(paths) != 16:
        raise RuntimeError(f"se esperaban 16 fichas HTML y hay {len(paths)}")
    for path in paths:
        value = path.read_text(encoding="utf-8")
        catalog_id = body_attr(value, "data-catalog-id")
        if not catalog_id:
            raise RuntimeError(f"{path.relative_to(ROOT)}: falta data-catalog-id")
        if catalog_id in result:
            raise RuntimeError(f"data-catalog-id duplicado en HTML: {catalog_id}")
        result[catalog_id] = path
    return result


def numbered(items: list[list[str]]) -> list[list[str]]:
    return [[f"{idx:02d}", title, copy] for idx, (title, copy) in enumerate(items, 1)]


def normalize_detail(catalog_id: str, source: dict, override: dict | None) -> dict:
    kind = "product" if source.get("type") == "Producto jurídico" else "service"
    acceptance = source.get("acceptance", [])
    supplements = source.get("supplements", [])
    verification = [f"{title}. {copy}" for title, copy in acceptance]
    close = "Cierre verificable: " + "; ".join(title for title, _ in acceptance) + "." if acceptance else "El cierre se verifica contra los entregables y el perímetro acordados."
    scope_change = (
        "Suplementos previstos: " + "; ".join(title for title, _ in supplements) + "."
        if supplements
        else "Cualquier ampliación del perímetro requiere alcance expreso."
    )
    data = {
        "catalog_id": catalog_id,
        "kind": kind,
        "eyebrow": f"{source['type'].upper()} · {source['modality'].upper()}",
        "title": source["title"],
        "lead": source["summary"],
        "meta": [["Horizonte", source["duration"]], ["Modalidad", source["modality"]], ["Dirigido a", source["audience"]]],
        "question": source["question"],
        "result_text": source["result"],
        "result_title": "Qué cambia al terminar el trabajo.",
        "result_points": verification,
        "deliverables_title": "Qué recibe la empresa y para qué sirve cada salida.",
        "deliverables": numbered(source.get("deliverables", [])),
        "perimeter": source.get("perimeter", []),
        "method": numbered(source.get("method", [])),
        "limits": source.get("limits", []),
        "close": close,
        "scope_change": scope_change,
        "primary_cta": "Presentar esta necesidad",
    }
    if override:
        data.update(override)
    data["catalog_id"] = catalog_id
    data["kind"] = kind
    data["result_text"] = source["result"]
    return data


def mark_body(text: str, surface: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        for attr in ("data-experience-system", "data-experience-wave", "data-experience-surface"):
            tag = re.sub(rf'\s{attr}="[^"]*"', "", tag)
        return tag[:-1] + f' data-experience-system="v6" data-experience-wave="deep-offers" data-experience-surface="{e(surface)}">'
    return re.sub(r"<body\b[^>]*>", repl, text, count=1)


def ensure_styles(text: str, prefix: str) -> str:
    hrefs = [
        f"{prefix}assets/css/v6/tokens.css",
        f"{prefix}assets/css/v6/base.css",
        f"{prefix}assets/css/v6/components.css",
        f"{prefix}assets/css/v6/surfaces.css",
    ]
    for href in hrefs:
        text = re.sub(rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(href)}">\s*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("página sin </head> para cargar Experience System v6")
    links = "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in hrefs)
    return text.replace("</head>", f"{links}\n</head>", 1)


def home_header(text: str) -> str:
    nav = (
        '<nav id="main-nav" class="main-nav" aria-label="Navegación principal">'
        '<a href="#v6-situations">Cómo podemos ayudar</a><a href="soluciones/index.html">Soluciones</a>'
        '<a href="#v6-commercial-depth">Oferta completa</a><a href="perspectivas.html">Perspectivas</a><a href="firma.html">Firma</a>'
        '<span class="mobile-nav-actions"><a href="experiencia.html">Cómo trabajamos · demo</a><a href="#contacto">Presentar necesidad</a></span></nav>'
    )
    text, count = re.subn(r'<nav id="main-nav" class="main-nav" aria-label="Navegación principal">.*?</nav>', nav, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Home v6: no se localizó main-nav")
    actions = '<div class="header-actions"><a class="btn btn-navy" href="#contacto">Presentar necesidad</a></div>'
    text, count = re.subn(r'<div class="header-actions">.*?</div>', actions, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Home v6: no se localizaron header-actions")
    return text


def detail_header(text: str, contact_href: str) -> str:
    nav = (
        '<nav class="detail-nav" id="detail-nav" aria-label="Navegación principal">'
        '<a href="../index.html#v6-situations">Cómo podemos ayudar</a><a href="../soluciones/index.html">Soluciones</a>'
        '<a href="../index.html#v6-commercial-depth">Oferta completa</a><a href="../perspectivas.html">Perspectivas</a><a href="../firma.html">Firma</a></nav>'
    )
    text, count = re.subn(r'<nav class="detail-nav" id="detail-nav" aria-label="Navegación principal">.*?</nav>', nav, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Ficha v6: no se localizó detail-nav")
    actions = f'<div class="detail-header-actions"><a class="btn btn-navy" data-experience-v60-cta="header" href="{e(contact_href)}">Presentar necesidad</a></div>'
    text, count = re.subn(r'<div class="detail-header-actions">.*?</div>', actions, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Ficha v6: no se localizaron detail-header-actions")
    return text


def detail_journey(text: str, contact_href: str) -> str:
    journey = re.search(r'<div class="journey-bar"[^>]*>.*?</div>', text, flags=re.S)
    if not journey:
        raise RuntimeError("Ficha v6: no se localizó journey-bar")
    fragment = journey.group(0)
    anchor = re.search(r'<a\b([^>]*)>Presentar esta necesidad →</a>', fragment, flags=re.S)
    if not anchor:
        raise RuntimeError("Ficha v6: no se localizó CTA de journey-bar")
    attrs = anchor.group(1)
    attrs = re.sub(r'\s+href="[^"]*"', "", attrs)
    attrs = re.sub(r'\s+data-experience-v60-cta="[^"]*"', "", attrs)
    replacement = f'<a{attrs} data-experience-v60-cta="journey" href="{e(contact_href)}">Presentar esta necesidad →</a>'
    fragment = fragment[:anchor.start()] + replacement + fragment[anchor.end():]
    return text[:journey.start()] + fragment + text[journey.end():]


def render_method_artifact(method: list[list[str]]) -> str:
    rows = "".join(f'<div class="v6-artifact-step"><span>{e(num)}</span><strong>{e(title)}</strong></div>' for num, title, _ in method)
    return '<aside class="v6-artifact" aria-label="Método de trabajo"><div class="v6-artifact-inner"><p class="v6-eyebrow">DE PROBLEMA A EJECUCIÓN</p><h2 class="v6-artifact-title">El criterio jurídico debe dejar una ruta que pueda administrarse.</h2><div class="v6-artifact-steps">' + rows + '</div></div></aside>'


def render_home(data: dict, form_html: str, commercial: str, legacy: str) -> str:
    situations = []
    for idx, (num, title, action) in enumerate(data["situations"]):
        situations.append(f'<a class="v6-index-row" href="{e(SOLUTION_HREFS[idx])}"><span class="v6-index-num">{e(num)}</span><strong class="v6-index-title">{e(title)}</strong><span class="v6-index-action">{e(action)} →</span></a>')
    outcomes = "".join(f'<article class="v6-outcome"><b>{e(num)}</b><h3>{e(title)}</h3><p>{e(copy)}</p></article>' for num, title, copy in data["outcomes"])
    timeline = "".join(f'<article class="v6-timeline-row"><span class="v6-timeline-num">{e(num)}</span><strong class="v6-timeline-title">{e(title)}</strong><p class="v6-timeline-copy">{e(copy)}</p></article>' for num, title, copy in data["method"])
    evidence = "".join(f'<div class="v6-evidence-row"><b>{idx:02d}</b><span>{e(copy)}</span></div>' for idx, copy in enumerate(data["evidence"], 1))
    families = "".join(f'<article class="v6-family"><h3>{e(title)}</h3><p>{e(copy)}</p><a class="v6-text-link" href="#v6-commercial-depth">Explorar oferta y condiciones →</a></article>' for title, copy in data["offer_families"])
    assurance = "".join(f'<span>{e(item)}</span>' for item in data["assurance"])
    return f'''{HOME_START}
<section class="v6-hero" aria-labelledby="v6-home-title"><div class="v6-container v6-hero-grid"><div class="v6-hero-copy"><p class="v6-eyebrow">{e(data['eyebrow'])}</p><h1 class="v6-display" id="v6-home-title">{e(data['title'])}</h1><p class="v6-lead">{e(data['lead'])}</p><div class="v6-actions"><a class="v6-btn" href="#contacto">{e(data['primary_cta'])} →</a><a class="v6-btn v6-btn-secondary" href="#v6-situations">{e(data['secondary_cta'])}</a></div><div class="v6-assurance">{assurance}</div></div>{render_method_artifact(data['method'])}</div></section>
<section class="v6-section v6-home-situations" id="v6-situations" aria-labelledby="v6-situations-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">EMPIECE POR LO QUE ESTÁ PASANDO</p><h2 class="v6-heading" id="v6-situations-title">No necesita saber el nombre del servicio. Empiece por la decisión que debe resolver.</h2><p class="v6-lead">Seis rutas conectan una situación empresarial reconocible con una decisión jurídica y una forma proporcional de intervenir.</p></div><div class="v6-index">{''.join(situations)}</div></div></section>
<section class="v6-section v6-outcomes" aria-labelledby="v6-outcomes-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">RESULTADOS JURÍDICOS ADMINISTRABLES</p><h2 class="v6-heading" id="v6-outcomes-title">El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.</h2></div><div class="v6-outcome-grid">{outcomes}</div></div></section>
<section class="v6-section v6-home-method" aria-labelledby="v6-method-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">DE PROBLEMA A EJECUCIÓN</p><h2 class="v6-heading" id="v6-method-title">Primero entendemos la decisión. Después definimos el instrumento.</h2></div><div class="v6-method-line"></div><div class="v6-timeline">{timeline}</div></div></section>
<section class="v6-section v6-evidence" aria-labelledby="v6-evidence-title"><div class="v6-container v6-evidence-grid"><div class="v6-section-head"><p class="v6-eyebrow">CRITERIO QUE PUEDE VERIFICARSE</p><h2 class="v6-heading" id="v6-evidence-title">La experiencia debe leerse en cómo se estructura el trabajo.</h2><p class="v6-lead">La confianza depende de poder entender alcance, método, evidencia, límites y trayectoria.</p><div class="v6-actions"><a class="v6-btn" href="firma.html#trayectoria">Ver trayectoria y método →</a><a class="v6-btn v6-btn-secondary" href="experiencia.html">Ver experiencia demo</a></div></div><div class="v6-evidence-list">{evidence}</div></div></section>
<section class="v6-section v6-home-offer" id="v6-offer" aria-labelledby="v6-offer-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">OFERTA COMPLETA</p><h2 class="v6-heading" id="v6-offer-title">Cuando ya reconoce la necesidad, compare la forma de intervenir.</h2></div><div class="v6-family-grid">{families}</div></div></section>
<details class="v6-depth v6-commercial-depth" id="v6-commercial-depth"><summary><span>PLANES, HONORARIOS Y CONTRATACIÓN</span><strong>Comparar referencias económicas, modalidades y condiciones antes de presentar la necesidad</strong></summary><div class="v6-depth-inner">{commercial}</div></details>
<section class="v6-section v6-contact" id="contacto" data-conversion-path-v528="true" aria-labelledby="v6-contact-title"><div class="v6-container v6-contact-grid"><div class="v6-contact-copy"><p class="v6-eyebrow">SIGUIENTE PASO</p><h2 class="v6-heading" id="v6-contact-title">Cuéntenos qué decisión necesita resolver.</h2><p class="v6-lead">No necesita escoger primero un servicio. Comparta el contexto general, el horizonte y el resultado esperado. No envíe información confidencial ni documentos sensibles.</p><p class="v6-lead"><strong>Este formulario no crea una relación profesional, no envía archivos y no registra una conversión.</strong> Prepara un handoff manual a WhatsApp conforme al contrato vigente.</p></div><div class="v6-contact-form">{form_html}</div></div></section>
<details class="v6-depth v6-legacy-home" id="v6-depth"><summary><span>PROFUNDIDAD COMPLETA</span><strong>Explorar sectores, perspectivas, firma, preguntas y condiciones del sitio v5.31</strong></summary><div class="v6-depth-inner">{LEGACY_START}{legacy}{LEGACY_END}</div></details>
{HOME_END}'''


def render_detail_hero(data: dict, contact_href: str) -> str:
    meta = "".join(f'<div><span>{e(label)}</span><strong>{e(value)}</strong></div>' for label, value in data["meta"])
    secondary_target = "#v6-boundary" if data["kind"] == "service" else "#v6-perimeter"
    secondary = "Ver qué cubre y qué no cubre" if data["kind"] == "service" else "Ver perímetro exacto"
    return f'<section class="v6-hero v6-detail-hero" aria-labelledby="v6-detail-title"><div class="v6-container v6-hero-grid"><div class="v6-hero-copy"><p class="v6-eyebrow">{e(data["eyebrow"])}</p><h1 class="v6-display" id="v6-detail-title">{e(data["title"])}</h1><p class="v6-lead">{e(data["lead"])}</p><div class="v6-actions"><a class="v6-btn" data-experience-v60-cta="primary" href="{e(contact_href)}">{e(data["primary_cta"])} →</a><a class="v6-btn v6-btn-secondary" href="{secondary_target}">{secondary}</a></div><div class="v6-detail-meta">{meta}</div></div></div></section>'


def render_detail_nav(data: dict) -> str:
    first = '<a href="#v6-result">Resultado</a>' if data["kind"] == "product" else '<a href="#v6-question">Decisión</a>'
    return '<nav class="v6-detail-nav" aria-label="Navegación de la ficha v6"><div class="v6-container v6-detail-nav-inner">' + first + '<a href="#v6-deliverables">Entregables</a><a href="#v6-perimeter">Perímetro</a><a href="#v6-process">Proceso</a><a href="#v6-boundary">Límites</a><a href="#v6-detail-depth">Profundidad</a></div></nav>'


def render_result(data: dict) -> str:
    points = data.get("result_points", [])
    items = "".join(f'<div class="v6-result-item"><b>{idx:02d}</b><span>{e(item)}</span></div>' for idx, item in enumerate(points, 1))
    return f'<section class="v6-section v6-result" id="v6-result" aria-labelledby="v6-result-title"><div class="v6-container v6-result-grid"><div class="v6-section-head"><p class="v6-eyebrow">RESULTADO</p><h2 class="v6-heading" id="v6-result-title">{e(data["result_title"])}</h2><p class="v6-lead">{e(data["result_text"])}</p></div><div class="v6-result-list">{items}</div></div></section>'


def render_deliverables(data: dict) -> str:
    rows = "".join(f'<article class="v6-ledger-row"><span class="v6-ledger-num">{e(num)}</span><div><h3 class="v6-ledger-title">{e(title)}</h3><p class="v6-ledger-copy">{e(copy)}</p></div><span class="v6-ledger-meta">Salida verificable</span></article>' for num, title, copy in data["deliverables"])
    eyebrow = "EXPEDIENTE DE SALIDA" if data["kind"] == "product" else "LO QUE RECIBE"
    return f'<section class="v6-section v6-deliverables" id="v6-deliverables" aria-labelledby="v6-deliverables-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">{eyebrow}</p><h2 class="v6-heading" id="v6-deliverables-title">{e(data["deliverables_title"])}</h2><p class="v6-lead">Cada salida conserva la función y el perímetro definidos en la fuente canónica.</p></div><div class="v6-ledger">{rows}</div></div></section>'


def render_perimeter(data: dict) -> str:
    rows = "".join(f'<div class="v6-matrix-row"><dt>{e(label)}</dt><dd>{e(value)}</dd></div>' for label, value in data["perimeter"])
    intro = "Un producto cerrado debe poder medirse antes de contratarse." if data["kind"] == "product" else "El alcance debe identificar qué universo entra al análisis."
    eyebrow = "PERÍMETRO ESTÁNDAR" if data["kind"] == "product" else "PERÍMETRO DE REFERENCIA"
    return f'<section class="v6-section v6-perimeter" id="v6-perimeter" aria-labelledby="v6-perimeter-title"><div class="v6-container v6-matrix-shell"><div class="v6-section-head"><p class="v6-eyebrow">{eyebrow}</p><h2 class="v6-heading" id="v6-perimeter-title">{intro}</h2><p class="v6-lead">{e(data["scope_change"])}</p></div><dl class="v6-matrix">{rows}</dl></div></section>'


def render_process(data: dict) -> str:
    rows = "".join(f'<article class="v6-timeline-row"><span class="v6-timeline-num">{e(num)}</span><strong class="v6-timeline-title">{e(title)}</strong><p class="v6-timeline-copy">{e(copy)}</p></article>' for num, title, copy in data["method"])
    return f'<section class="v6-section v6-process" id="v6-process" aria-labelledby="v6-process-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">CÓMO OCURRE</p><h2 class="v6-heading" id="v6-process-title">Una secuencia de trabajo con decisiones y cierre verificable.</h2></div><div class="v6-method-line"></div><div class="v6-timeline">{rows}</div></div></section>'


def render_boundary(data: dict) -> str:
    limits = "".join(f'<li>{e(item)}</li>' for item in data["limits"])
    title = "Precisión sin promesa de certificación." if data["kind"] == "product" else "El servicio no sustituye especialidades o decisiones fuera de su perímetro."
    return f'<section class="v6-section v6-boundary" id="v6-boundary" aria-labelledby="v6-boundary-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">LÍMITES PRINCIPALES</p><h2 class="v6-heading" id="v6-boundary-title">{title}</h2></div><ul class="v6-boundary-list">{limits}</ul></div></section>'


def render_close(data: dict, contact_href: str) -> str:
    return f'<section class="v6-section v6-detail-close"><div class="v6-container"><div class="v6-close"><div><strong>{e(data["close"])}</strong><p>{e(data["scope_change"])}</p></div><a class="v6-btn" data-experience-v60-cta="close" href="{e(contact_href)}">{e(data["primary_cta"])} →</a></div></div></section>'


def render_detail(data: dict, legacy: str, contact_href: str) -> str:
    question = ""
    if data["kind"] == "service":
        question = f'<section class="v6-section v6-question" id="v6-question" aria-labelledby="v6-question-title"><div class="v6-container"><p class="v6-eyebrow">PREGUNTA DE GOBIERNO</p><blockquote id="v6-question-title">{e(data["question"])}</blockquote></div></section>'
    return f'''{DETAIL_START}
{question}
{render_result(data)}
{render_deliverables(data)}
{render_perimeter(data)}
{render_process(data)}
{render_boundary(data)}
{render_close(data, contact_href)}
<details class="v6-depth v6-detail-depth" id="v6-detail-depth"><summary><span>PROFUNDIDAD JURÍDICA Y CONTRACTUAL</span><strong>Ver ficha completa: encaje, frentes, formatos, cronograma, responsabilidades, aceptación, alternativas, prueba y contratación</strong></summary><div class="v6-depth-inner">{LEGACY_START}{legacy}{LEGACY_END}</div></details>
{DETAIL_END}'''


def extract_main(text: str) -> tuple[re.Match[str], str]:
    match = re.search(r'<main id="contenido"[^>]*>(.*?)</main>', text, flags=re.S)
    if not match:
        raise RuntimeError("no se localizó <main id=contenido>")
    return match, match.group(1)


def extract_legacy(current_main: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r'(.*?)' + re.escape(LEGACY_END), current_main, flags=re.S)
    return match.group(1) if match else current_main


def extract_commercial(current_main: str) -> str:
    match = re.search(re.escape(COMMERCIAL_START) + r'.*?' + re.escape(COMMERCIAL_END), current_main, flags=re.S)
    if not match:
        raise RuntimeError("Home v6: no se localizó bloque comercial v4.3")
    return match.group(0)


def patch_home(data: dict) -> None:
    text = HOME.read_text(encoding="utf-8")
    text = ensure_styles(text, "")
    text = mark_body(text, "home")
    text = home_header(text)
    main_match, current_main = extract_main(text)
    form_matches = list(re.finditer(r'<form\b[^>]*>.*?</form>', current_main, flags=re.S))
    if len(form_matches) != 1:
        raise RuntimeError(f"Home v6 esperaba un único formulario; encontró {len(form_matches)}")
    form_html = form_matches[0].group(0)
    commercial = extract_commercial(current_main)
    legacy = extract_legacy(current_main)
    if commercial in legacy:
        legacy = legacy.replace(commercial, "", 1)
    if re.search(r'<form\b[^>]*>.*?</form>', legacy, flags=re.S):
        legacy = re.sub(r'<form\b[^>]*>.*?</form>', FORM_MOVED, legacy, count=1, flags=re.S)
    legacy = legacy.replace('id="contacto"', 'id="contacto-v531-legacy"')
    legacy = legacy.replace(' data-conversion-path-v528="true"', '', 1)
    new_main = f'<main id="contenido" data-experience-v60="home">\n{render_home(data, form_html, commercial, legacy)}\n</main>'
    text = text[:main_match.start()] + new_main + text[main_match.end():]
    HOME.write_text(text, encoding="utf-8")


def canonical_contact_href(text: str) -> str:
    candidates = [tag for tag in re.findall(r'<a\b[^>]*>', text, flags=re.S) if 'data-decision-v58-cta="true"' in tag]
    if len(candidates) != 1:
        raise RuntimeError(f"Ficha v6: esperaba una CTA comercial canónica v5.8; encontró {len(candidates)}")
    href_match = re.search(r'href="([^"]+)"', candidates[0])
    if not href_match:
        raise RuntimeError("Ficha v6: CTA comercial canónica sin href")
    href = unescape(href_match.group(1))
    parts = urlsplit(href)
    pairs = [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if key != "experience"]
    pairs.append(("experience", "v6"))
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(pairs), parts.fragment or "contacto"))


def contact_href_for(text: str, data: dict) -> str:
    # La CTA visible v6 hereda la ruta comercial canónica ya materializada por v5.8/v5.10.
    # v6 solo añade contexto de experiencia; no reconstruye modalidad, intención ni estándar.
    return canonical_contact_href(text)


def replace_detail_hero(text: str, new_hero: str, path: Path) -> str:
    for pattern in (r'<section class="v6-hero v6-detail-hero"[^>]*>.*?</section>', r'<section class="detail-hero">.*?</section>'):
        text, count = re.subn(pattern, new_hero, text, count=1, flags=re.S)
        if count == 1:
            return text
    raise RuntimeError(f"{path.name}: no se localizó hero v5 ni v6")


def replace_detail_nav(text: str, new_toc: str, path: Path) -> str:
    text, count = re.subn(r'<nav class="v6-detail-nav"[^>]*>.*?</nav>', new_toc, text, count=1, flags=re.S)
    if count == 1:
        return text
    text, count = re.subn(r'<!-- DETAIL-V46-NAV:START -->.*?<!-- DETAIL-V46-NAV:END -->', new_toc, text, count=1, flags=re.S)
    if count == 1:
        return text
    raise RuntimeError(f"{path.name}: no se localizó navegación detail v4.6 ni v6")


def patch_detail(catalog_id: str, path: Path, data: dict) -> None:
    text = path.read_text(encoding="utf-8")
    contact_href = contact_href_for(text, data)
    text = ensure_styles(text, "../")
    text = mark_body(text, catalog_id)
    text = detail_header(text, contact_href)
    text = detail_journey(text, contact_href)
    text = replace_detail_hero(text, render_detail_hero(data, contact_href), path)
    text = replace_detail_nav(text, render_detail_nav(data), path)
    main_match, current_main = extract_main(text)
    legacy = extract_legacy(current_main)
    new_main = f'<main id="contenido" data-experience-v60="{e(catalog_id)}">\n{render_detail(data, legacy, contact_href)}\n</main>'
    text = text[:main_match.start()] + new_main + text[main_match.end():]
    path.write_text(text, encoding="utf-8")


def validate() -> None:
    validator = ROOT / "scripts/validate_experience_v60.py"
    if not validator.exists():
        return
    result = subprocess.run([sys.executable, str(validator)], cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError((result.stderr or result.stdout).strip())
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    version = load_json(VERSION).get("version", "0.0.0")
    if semver(version) < (6, 0, 0):
        return 0
    contract = load_json(CONTRACT)
    content = load_json(CONTENT)
    if contract.get("version") != "6.0.0" or content.get("version") != "6.0.0":
        raise RuntimeError("contratos v6 deben declarar 6.0.0")

    sources = load_catalog_sources()
    paths = discover_detail_paths()
    if set(sources) != set(paths):
        missing_html = sorted(set(sources) - set(paths))
        missing_source = sorted(set(paths) - set(sources))
        raise RuntimeError(f"desalineación fuentes/HTML; sin HTML={missing_html}; sin fuente={missing_source}")

    overrides = content.get("pilots", {})
    unknown_overrides = sorted(set(overrides) - set(sources))
    if unknown_overrides:
        raise RuntimeError(f"overrides v6 sin fuente canónica: {unknown_overrides}")

    patch_home(content["home"])
    for catalog_id in sorted(sources):
        data = normalize_detail(catalog_id, sources[catalog_id], overrides.get(catalog_id))
        patch_detail(catalog_id, paths[catalog_id], data)

    validate()
    print("EXPERIENCE V6 WAVE 2 OK: Home + 16/16 fichas materializadas desde catálogos canónicos; v5.31 preservado; formulario único.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

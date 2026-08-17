#!/usr/bin/env python3
"""Meridiano Legal v6: materializa la primera capa semántica de experiencia en superficies piloto.

Wave 1 mantiene íntegro el contenido v5.31 como profundidad accesible mientras prueba
Home + producto diagnóstico + servicio IA. No crea capabilities nuevas ni duplica el
formulario físico.
"""
from __future__ import annotations

from html import escape
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "experience-system-v60.json"
CONTENT = ROOT / "experience-content-v60.json"
HOME = ROOT / "index.html"
PILOTS = {
    "product-diagnostic": ROOT / "productos/diagnostico-juridico-empresarial.html",
    "service-ai": ROOT / "servicios/tecnologia-inteligencia-artificial.html",
}

HOME_START = "<!-- EXPERIENCE-V60-HOME:START -->"
HOME_END = "<!-- EXPERIENCE-V60-HOME:END -->"
DETAIL_START = "<!-- EXPERIENCE-V60-DETAIL:START -->"
DETAIL_END = "<!-- EXPERIENCE-V60-DETAIL:END -->"
LEGACY_START = "<!-- EXPERIENCE-V60-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-LEGACY:END -->"
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


def mark_body(text: str, surface: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        tag = re.sub(r'\sdata-experience-system="[^"]*"', "", tag)
        tag = re.sub(r'\sdata-experience-wave="[^"]*"', "", tag)
        tag = re.sub(r'\sdata-experience-surface="[^"]*"', "", tag)
        return tag[:-1] + f' data-experience-system="v6" data-experience-wave="pilots" data-experience-surface="{e(surface)}">'

    return re.sub(r"<body\b[^>]*>", repl, text, count=1)


def ensure_styles(text: str, prefix: str) -> str:
    hrefs = [
        f"{prefix}assets/css/v6/tokens.css",
        f"{prefix}assets/css/v6/base.css",
        f"{prefix}assets/css/v6/components.css",
        f"{prefix}assets/css/v6/surfaces.css",
    ]
    for href in hrefs:
        text = re.sub(
            rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(href)}">\s*(?:\r?\n)?',
            "",
            text,
        )
    if "</head>" not in text:
        raise RuntimeError("página sin </head> para cargar Experience System v6")
    links = "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in hrefs)
    return text.replace("</head>", f"{links}\n</head>", 1)


def home_header(text: str) -> str:
    nav = (
        '<nav id="main-nav" class="main-nav" aria-label="Navegación principal">'
        '<a href="#v6-situations">Cómo podemos ayudar</a>'
        '<a href="soluciones/index.html">Soluciones</a>'
        '<a href="#v6-depth">Oferta completa</a>'
        '<a href="perspectivas.html">Perspectivas</a>'
        '<a href="firma.html">Firma</a>'
        '<span class="mobile-nav-actions">'
        '<a href="experiencia.html">Cómo trabajamos · demo</a>'
        '<a href="#contacto">Presentar necesidad</a>'
        '</span></nav>'
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
        '<a href="../index.html#v6-situations">Cómo podemos ayudar</a>'
        '<a href="../soluciones/index.html">Soluciones</a>'
        '<a href="../index.html#v6-depth">Oferta completa</a>'
        '<a href="../perspectivas.html">Perspectivas</a>'
        '<a href="../firma.html">Firma</a>'
        '</nav>'
    )
    text, count = re.subn(r'<nav class="detail-nav" id="detail-nav" aria-label="Navegación principal">.*?</nav>', nav, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Ficha v6: no se localizó detail-nav")
    actions = f'<div class="detail-header-actions"><a class="btn btn-navy" href="{e(contact_href)}">Presentar necesidad</a></div>'
    text, count = re.subn(r'<div class="detail-header-actions">.*?</div>', actions, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Ficha v6: no se localizaron detail-header-actions")
    return text


def render_method_artifact(method: list[list[str]]) -> str:
    rows = []
    for num, title, _copy in method:
        rows.append(f'<div class="v6-artifact-step"><span>{e(num)}</span><strong>{e(title)}</strong></div>')
    return (
        '<aside class="v6-artifact" aria-label="Método de trabajo">'
        '<div class="v6-artifact-inner">'
        '<p class="v6-eyebrow">DE PROBLEMA A EJECUCIÓN</p>'
        '<h2 class="v6-artifact-title">El criterio jurídico debe dejar una ruta que pueda administrarse.</h2>'
        '<div class="v6-artifact-steps">' + "".join(rows) + '</div>'
        '</div></aside>'
    )


def render_home(data: dict, form_html: str, legacy: str) -> str:
    situations = []
    for idx, item in enumerate(data["situations"]):
        num, title, action = item
        href = SOLUTION_HREFS[idx]
        situations.append(
            '<a class="v6-index-row" href="%s">'
            '<span class="v6-index-num">%s</span>'
            '<strong class="v6-index-title">%s</strong>'
            '<span class="v6-index-action">%s →</span>'
            '</a>' % (e(href), e(num), e(title), e(action))
        )

    outcomes = []
    for num, title, copy in data["outcomes"]:
        outcomes.append(
            f'<article class="v6-outcome"><b>{e(num)}</b><h3>{e(title)}</h3><p>{e(copy)}</p></article>'
        )

    timeline = []
    for num, title, copy in data["method"]:
        timeline.append(
            f'<article class="v6-timeline-row"><span class="v6-timeline-num">{e(num)}</span>'
            f'<strong class="v6-timeline-title">{e(title)}</strong><p class="v6-timeline-copy">{e(copy)}</p></article>'
        )

    evidence = []
    for idx, copy in enumerate(data["evidence"], 1):
        evidence.append(
            f'<div class="v6-evidence-row"><b>{idx:02d}</b><span>{e(copy)}</span></div>'
        )

    families = []
    for title, copy in data["offer_families"]:
        families.append(
            f'<article class="v6-family"><h3>{e(title)}</h3><p>{e(copy)}</p>'
            '<a class="v6-text-link" href="#v6-depth">Explorar oferta y condiciones →</a></article>'
        )

    assurance = "".join(f'<span>{e(item)}</span>' for item in data["assurance"])

    return f'''{HOME_START}
<section class="v6-hero" aria-labelledby="v6-home-title">
  <div class="v6-container v6-hero-grid">
    <div class="v6-hero-copy">
      <p class="v6-eyebrow">{e(data['eyebrow'])}</p>
      <h1 class="v6-display" id="v6-home-title">{e(data['title'])}</h1>
      <p class="v6-lead">{e(data['lead'])}</p>
      <div class="v6-actions"><a class="v6-btn" href="#contacto">{e(data['primary_cta'])} →</a><a class="v6-btn v6-btn-secondary" href="#v6-situations">{e(data['secondary_cta'])}</a></div>
      <div class="v6-assurance">{assurance}</div>
    </div>
    {render_method_artifact(data['method'])}
  </div>
</section>
<section class="v6-section v6-home-situations" id="v6-situations" aria-labelledby="v6-situations-title">
  <div class="v6-container">
    <div class="v6-section-head"><p class="v6-eyebrow">EMPIECE POR LO QUE ESTÁ PASANDO</p><h2 class="v6-heading" id="v6-situations-title">No necesita saber el nombre del servicio. Empiece por la decisión que debe resolver.</h2><p class="v6-lead">Seis rutas conectan una situación empresarial reconocible con una decisión jurídica y una forma proporcional de intervenir.</p></div>
    <div class="v6-index">{''.join(situations)}</div>
  </div>
</section>
<section class="v6-section v6-outcomes" aria-labelledby="v6-outcomes-title">
  <div class="v6-container">
    <div class="v6-section-head"><p class="v6-eyebrow">RESULTADOS JURÍDICOS ADMINISTRABLES</p><h2 class="v6-heading" id="v6-outcomes-title">El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.</h2></div>
    <div class="v6-outcome-grid">{''.join(outcomes)}</div>
  </div>
</section>
<section class="v6-section v6-home-method" aria-labelledby="v6-method-title">
  <div class="v6-container">
    <div class="v6-section-head"><p class="v6-eyebrow">DE PROBLEMA A EJECUCIÓN</p><h2 class="v6-heading" id="v6-method-title">Primero entendemos la decisión. Después definimos el instrumento.</h2></div>
    <div class="v6-method-line"></div><div class="v6-timeline">{''.join(timeline)}</div>
  </div>
</section>
<section class="v6-section v6-evidence" aria-labelledby="v6-evidence-title">
  <div class="v6-container v6-evidence-grid">
    <div class="v6-section-head"><p class="v6-eyebrow">CRITERIO QUE PUEDE VERIFICARSE</p><h2 class="v6-heading" id="v6-evidence-title">La experiencia debe leerse en cómo se estructura el trabajo.</h2><p class="v6-lead">La confianza no depende de slogans ni de una lista de clientes inventada: depende de poder entender alcance, método, evidencia, límites y trayectoria.</p><div class="v6-actions"><a class="v6-btn" href="firma.html#trayectoria">Ver trayectoria y método →</a><a class="v6-btn v6-btn-secondary" href="experiencia.html">Ver experiencia demo</a></div></div>
    <div class="v6-evidence-list">{''.join(evidence)}</div>
  </div>
</section>
<section class="v6-section v6-home-offer" id="v6-offer" aria-labelledby="v6-offer-title">
  <div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">OFERTA COMPLETA</p><h2 class="v6-heading" id="v6-offer-title">Cuando ya reconoce la necesidad, compare la forma de intervenir.</h2></div><div class="v6-family-grid">{''.join(families)}</div></div>
</section>
<section class="v6-section v6-contact" id="contacto" aria-labelledby="v6-contact-title">
  <div class="v6-container v6-contact-grid">
    <div class="v6-contact-copy"><p class="v6-eyebrow">SIGUIENTE PASO</p><h2 class="v6-heading" id="v6-contact-title">Cuéntenos qué decisión necesita resolver.</h2><p class="v6-lead">No necesita escoger primero un servicio. Comparta el contexto general, el horizonte y el resultado esperado. No envíe información confidencial ni documentos sensibles.</p><p class="v6-lead"><strong>Este formulario no crea una relación profesional, no envía archivos y no registra una conversión.</strong> Prepara un handoff manual a WhatsApp conforme al contrato vigente.</p></div>
    <div class="v6-contact-form">{form_html}</div>
  </div>
</section>
<details class="v6-depth v6-legacy-home" id="v6-depth">
  <summary><span>PROFUNDIDAD COMPLETA</span><strong>Explorar oferta, planes, sectores, perspectivas, firma, preguntas y condiciones del sitio v5.31</strong></summary>
  <div class="v6-depth-inner">{LEGACY_START}{legacy}{LEGACY_END}</div>
</details>
{HOME_END}'''


def render_detail_hero(data: dict, contact_href: str) -> str:
    meta = "".join(
        f'<div><span>{e(label)}</span><strong>{e(value)}</strong></div>' for label, value in data["meta"]
    )
    secondary_target = "#v6-boundary" if data["kind"] == "service" else "#v6-perimeter"
    return f'''<section class="v6-hero v6-detail-hero" aria-labelledby="v6-detail-title">
  <div class="v6-container v6-hero-grid"><div class="v6-hero-copy">
    <p class="v6-eyebrow">{e(data['eyebrow'])}</p>
    <h1 class="v6-display" id="v6-detail-title">{e(data['title'])}</h1>
    <p class="v6-lead">{e(data['lead'])}</p>
    <div class="v6-actions"><a class="v6-btn" href="{e(contact_href)}">{e(data['primary_cta'])} →</a><a class="v6-btn v6-btn-secondary" href="{secondary_target}">{'Ver qué cubre y qué no cubre' if data['kind']=='service' else 'Ver perímetro exacto'}</a></div>
    <div class="v6-detail-meta">{meta}</div>
  </div></div>
</section>'''


def render_detail_nav(data: dict) -> str:
    first = '<a href="#v6-result">Resultado</a>' if data["kind"] == "product" else '<a href="#v6-question">Decisión</a>'
    return (
        '<nav class="v6-detail-nav" aria-label="Navegación de la ficha v6"><div class="v6-container v6-detail-nav-inner">'
        f'{first}<a href="#v6-deliverables">Entregables</a><a href="#v6-perimeter">Perímetro</a>'
        '<a href="#v6-process">Proceso</a><a href="#v6-boundary">Límites</a><a href="#v6-detail-depth">Profundidad</a>'
        '</div></nav>'
    )


def render_result(data: dict) -> str:
    if data["kind"] == "product":
        title = data["result_title"]
        points = data["result_points"]
    else:
        title = "El alcance debe terminar en gobierno operable, no en un diagnóstico abstracto."
        points = data["close_points"]
    items = "".join(
        f'<div class="v6-result-item"><b>{idx:02d}</b><span>{e(item)}</span></div>'
        for idx, item in enumerate(points, 1)
    )
    return f'''<section class="v6-section v6-result" id="v6-result" aria-labelledby="v6-result-title"><div class="v6-container v6-result-grid"><div class="v6-section-head"><p class="v6-eyebrow">RESULTADO</p><h2 class="v6-heading" id="v6-result-title">{e(title)}</h2></div><div class="v6-result-list">{items}</div></div></section>'''


def render_deliverables(data: dict) -> str:
    rows = []
    for num, title, copy in data["deliverables"]:
        rows.append(
            f'<article class="v6-ledger-row"><span class="v6-ledger-num">{e(num)}</span><div><h3 class="v6-ledger-title">{e(title)}</h3><p class="v6-ledger-copy">{e(copy)}</p></div><span class="v6-ledger-meta">Salida verificable</span></article>'
        )
    return f'''<section class="v6-section v6-deliverables" id="v6-deliverables" aria-labelledby="v6-deliverables-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">{'EXPEDIENTE DE SALIDA' if data['kind']=='product' else 'LO QUE RECIBE'}</p><h2 class="v6-heading" id="v6-deliverables-title">{e(data['deliverables_title'])}</h2><p class="v6-lead">La profundidad completa conserva los demás documentos, formatos, criterios de aceptación y condiciones definidos en la ficha canónica.</p></div><div class="v6-ledger">{''.join(rows)}</div></div></section>'''


def render_perimeter(data: dict) -> str:
    rows = "".join(
        f'<div class="v6-matrix-row"><dt>{e(label)}</dt><dd>{e(value)}</dd></div>' for label, value in data["perimeter"]
    )
    intro = (
        "Un producto cerrado debe poder medirse antes de contratarse."
        if data["kind"] == "product"
        else "Gobernar exige saber qué universo de casos y terceros entra al análisis."
    )
    return f'''<section class="v6-section v6-perimeter" id="v6-perimeter" aria-labelledby="v6-perimeter-title"><div class="v6-container v6-matrix-shell"><div class="v6-section-head"><p class="v6-eyebrow">{'PERÍMETRO ESTÁNDAR' if data['kind']=='product' else 'PERÍMETRO DE REFERENCIA'}</p><h2 class="v6-heading" id="v6-perimeter-title">{e(intro)}</h2><p class="v6-lead">{e(data['scope_change'])}</p></div><dl class="v6-matrix">{rows}</dl></div></section>'''


def render_process(data: dict) -> str:
    rows = []
    for num, title, copy in data["method"]:
        rows.append(
            f'<article class="v6-timeline-row"><span class="v6-timeline-num">{e(num)}</span><strong class="v6-timeline-title">{e(title)}</strong><p class="v6-timeline-copy">{e(copy)}</p></article>'
        )
    return f'''<section class="v6-section v6-process" id="v6-process" aria-labelledby="v6-process-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">CÓMO OCURRE</p><h2 class="v6-heading" id="v6-process-title">Una secuencia de trabajo con decisiones y cierre verificable.</h2></div><div class="v6-method-line"></div><div class="v6-timeline">{''.join(rows)}</div></div></section>'''


def render_boundary(data: dict) -> str:
    limits = "".join(f'<li>{e(item)}</li>' for item in data["limits"])
    title = (
        "Precisión sin promesa de certificación."
        if data["kind"] == "product"
        else "La gobernanza jurídica no sustituye validación técnica."
    )
    return f'''<section class="v6-section v6-boundary" id="v6-boundary" aria-labelledby="v6-boundary-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">LÍMITES PRINCIPALES</p><h2 class="v6-heading" id="v6-boundary-title">{e(title)}</h2></div><ul class="v6-boundary-list">{limits}</ul></div></section>'''


def render_close(data: dict, contact_href: str) -> str:
    return f'''<section class="v6-section v6-detail-close"><div class="v6-container"><div class="v6-close"><div><strong>{e(data['close'])}</strong><p>{e(data['scope_change'])}</p></div><a class="v6-btn" href="{e(contact_href)}">{e(data['primary_cta'])} →</a></div></div></section>'''


def render_detail(data: dict, legacy: str, contact_href: str) -> str:
    question = ""
    if data["kind"] == "service":
        question = f'''<section class="v6-section v6-question" id="v6-question" aria-labelledby="v6-question-title"><div class="v6-container"><p class="v6-eyebrow">PREGUNTA DE GOBIERNO</p><blockquote id="v6-question-title">{e(data['question'])}</blockquote></div></section>'''
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
    legacy = extract_legacy(current_main)
    if re.search(r'<form\b[^>]*>.*?</form>', legacy, flags=re.S):
        legacy = re.sub(r'<form\b[^>]*>.*?</form>', FORM_MOVED, legacy, count=1, flags=re.S)
    legacy = legacy.replace('id="contacto"', 'id="contacto-v531-legacy"')
    new_inner = render_home(data, form_html, legacy)
    new_main = f'<main id="contenido" data-experience-v60="home">\n{new_inner}\n</main>'
    text = text[:main_match.start()] + new_main + text[main_match.end():]
    HOME.write_text(text, encoding="utf-8")


def contact_href_for(text: str, data: dict) -> str:
    page_title = body_attr(text, "data-page-title") or data["title"]
    need = body_attr(text, "data-page-need") or page_title
    label = "Producto jurídico" if data["kind"] == "product" else "Servicio profesional"
    query = urlencode({"context": f"{label}: {page_title}", "need": need, "experience": "v6"})
    return f"../index.html?{query}#contacto"


def patch_detail(catalog_id: str, data: dict) -> None:
    path = PILOTS[catalog_id]
    text = path.read_text(encoding="utf-8")
    contact_href = contact_href_for(text, data)
    text = ensure_styles(text, "../")
    text = mark_body(text, catalog_id)
    text = detail_header(text, contact_href)

    new_hero = render_detail_hero(data, contact_href)
    text, count = re.subn(r'<section class="detail-hero">.*?</section>', new_hero, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{path.name}: no se localizó detail-hero")

    new_toc = render_detail_nav(data)
    marker_pattern = r'<!-- DETAIL-V46-NAV:START -->.*?<!-- DETAIL-V46-NAV:END -->'
    text, count = re.subn(marker_pattern, new_toc, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{path.name}: no se localizó navegación detail v4.6")

    main_match, current_main = extract_main(text)
    legacy = extract_legacy(current_main)
    new_inner = render_detail(data, legacy, contact_href)
    new_main = f'<main id="contenido" data-experience-v60="{e(catalog_id)}">\n{new_inner}\n</main>'
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
    patch_home(content["home"])
    for catalog_id, data in content["pilots"].items():
        patch_detail(catalog_id, data)
    validate()
    print("EXPERIENCE V6 WAVE 1 OK: Home + Auditoría + IA materializados; v5.31 preservado como profundidad; formulario único.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

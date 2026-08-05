#!/usr/bin/env python3
"""Enriquece firma, perspectivas y sectores sin reescribir su contenido editorial."""

from __future__ import annotations

from html import escape
from pathlib import Path
from urllib.parse import urlencode
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://arendon7.github.io/MERDIANOLEGAL/"
RELEASE_DATE = "2026-08-05"

PAGES = {
    "firma.html": {
        "kind": "firm",
        "type": "La firma",
        "title": "Meridiano Legal: dirección, método y principios profesionales",
        "description": "Conozca la dirección, metodología, principios profesionales y experiencia aplicada de Meridiano Legal.",
        "need": "Otra necesidad",
        "back_label": "Volver al inicio",
        "back_href": "index.html",
    },
    "perspectivas/gobierno-juridico-inteligencia-artificial.html": {
        "kind": "article", "type": "Perspectiva", "title": "Gobierno jurídico de inteligencia artificial",
        "description": "Marco jurídico empresarial para inventariar, clasificar y gobernar casos de uso de inteligencia artificial.",
        "need": "Gobernanza de IA", "back_label": "Biblioteca", "back_href": "../perspectivas.html",
        "keywords": ["inteligencia artificial", "gobernanza", "datos", "proveedores"],
    },
    "perspectivas/contratos-administrables.html": {
        "kind": "article", "type": "Perspectiva", "title": "Contratos administrables después de la firma",
        "description": "Cómo convertir un contrato en obligaciones, responsables, evidencias, cambios, preavisos y alternativas de salida.",
        "need": "Contratos y negociaciones", "back_label": "Biblioteca", "back_href": "../perspectivas.html",
        "keywords": ["contratos", "obligaciones", "gestión contractual", "evidencia"],
    },
    "perspectivas/propiedad-intelectual-cadena-titularidad.html": {
        "kind": "article", "type": "Perspectiva", "title": "Propiedad intelectual y cadena de titularidad",
        "description": "Cómo probar creación, cesión, licencia y explotación de marcas, software, contenidos y conocimiento empresarial.",
        "need": "Marca, software o intangibles", "back_label": "Biblioteca", "back_href": "../perspectivas.html",
        "keywords": ["propiedad intelectual", "software", "marcas", "titularidad"],
    },
    "perspectivas/socios-inversion-gobierno.html": {
        "kind": "article", "type": "Perspectiva", "title": "Socios, inversión y gobierno corporativo",
        "description": "Reglas sobre capital, autoridad, información, conflictos, permanencia, transferencia e inversión.",
        "need": "Socios, gobierno o inversión", "back_label": "Biblioteca", "back_href": "../perspectivas.html",
        "keywords": ["socios", "inversión", "gobierno corporativo", "capital"],
    },
    "perspectivas/proyectos-regulados-secuencia-viabilidad.html": {
        "kind": "article", "type": "Perspectiva", "title": "Secuencia de viabilidad para proyectos regulados",
        "description": "Actividad, territorio, autoridades, permisos, actores, contratos y condiciones precedentes para estructurar un proyecto regulado.",
        "need": "Proyecto regulado", "back_label": "Biblioteca", "back_href": "../perspectivas.html",
        "keywords": ["proyectos regulados", "permisos", "viabilidad", "autoridades"],
    },
    "perspectivas/legal-operations-modelo-operativo.html": {
        "kind": "article", "type": "Perspectiva", "title": "Legal Operations y modelo operativo jurídico",
        "description": "Cómo ordenar demanda, canales, triage, roles, documentos, métricas, tecnología y gestión del cambio jurídico.",
        "need": "Legal Operations", "back_label": "Biblioteca", "back_href": "../perspectivas.html",
        "keywords": ["Legal Operations", "procesos jurídicos", "métricas", "automatización"],
    },
    "sectores/tecnologia-software-ia.html": {
        "kind": "sector", "type": "Sector", "title": "Tecnología, software e inteligencia artificial",
        "description": "Enfoque jurídico para desarrollo, licenciamiento, datos, proveedores, titularidad y gobernanza de inteligencia artificial.",
        "need": "Gobernanza de IA", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/servicios-publicos-aseo-economia-circular.html": {
        "kind": "sector", "type": "Sector", "title": "Servicios públicos, aseo y economía circular",
        "description": "Enfoque jurídico para modelos operativos, actores territoriales, habilitaciones, contratos, obligaciones y aprovechamiento.",
        "need": "Proyecto regulado", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/agroindustria-fertilizantes-sostenibilidad.html": {
        "kind": "sector", "type": "Sector", "title": "Agroindustria, fertilizantes y sostenibilidad",
        "description": "Enfoque jurídico para producción, comercialización, alianzas, activos, regulación y proyectos agroindustriales sostenibles.",
        "need": "Proyecto regulado", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/salud-negocios-regulados.html": {
        "kind": "sector", "type": "Sector", "title": "Salud y negocios regulados",
        "description": "Enfoque jurídico para prestación, alianzas, experiencia del usuario, datos, responsabilidad y riesgo regulatorio en salud.",
        "need": "Proyecto regulado", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/comercio-distribucion.html": {
        "kind": "sector", "type": "Sector", "title": "Comercio y distribución",
        "description": "Enfoque jurídico para canales, consumidor, garantías, marcas, territorio, metas, distribución y terminación.",
        "need": "Contratos y negociaciones", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/startups-inversion.html": {
        "kind": "sector", "type": "Sector", "title": "Startups e inversión",
        "description": "Enfoque jurídico para fundadores, capital, gobierno, activos, contratos y preparación para inversión.",
        "need": "Socios, gobierno o inversión", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/proyectos-publicos-territoriales.html": {
        "kind": "sector", "type": "Sector", "title": "Proyectos públicos y territoriales",
        "description": "Enfoque jurídico para competencias, convenios, actores, cronogramas, obligaciones y articulación público-privada.",
        "need": "Proyecto regulado", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
    "sectores/operaciones-juridicas.html": {
        "kind": "sector", "type": "Sector", "title": "Transformación de operaciones jurídicas",
        "description": "Enfoque para solicitudes, procesos, documentos, obligaciones, indicadores, automatización y gestión del cambio jurídico.",
        "need": "Legal Operations", "back_label": "Todos los sectores", "back_href": "../index.html#sectores",
    },
}

ARTICLE_ORDER = [path for path, meta in PAGES.items() if meta["kind"] == "article"]
SECTOR_ORDER = [path for path, meta in PAGES.items() if meta["kind"] == "sector"]

HEAD_START = "<!-- EDITORIAL-SEO:START -->"
HEAD_END = "<!-- EDITORIAL-SEO:END -->"
JOURNEY_START = "<!-- EDITORIAL-JOURNEY:START -->"
JOURNEY_END = "<!-- EDITORIAL-JOURNEY:END -->"
SEQUENCE_START = "<!-- EDITORIAL-SEQUENCE:START -->"
SEQUENCE_END = "<!-- EDITORIAL-SEQUENCE:END -->"
SCRIPT_START = "<!-- EDITORIAL-SCRIPT:START -->"
SCRIPT_END = "<!-- EDITORIAL-SCRIPT:END -->"


def managed_pattern(start: str, end: str) -> re.Pattern[str]:
    return re.compile(rf"\s*{re.escape(start)}.*?{re.escape(end)}\s*", re.DOTALL)


def prefix_for(path: str) -> str:
    return "../" if "/" in path else ""


def absolute_url(path: str) -> str:
    return BASE_URL + path


def contact_url(path: str, meta: dict[str, object]) -> str:
    prefix = prefix_for(path)
    query = urlencode({"context": f'{meta["type"]}: {meta["title"]}', "need": str(meta["need"])})
    return f"{prefix}index.html?{query}#contacto"


def breadcrumb_schema(path: str, meta: dict[str, object]) -> dict[str, object]:
    if meta["kind"] == "article":
        middle_name, middle_url = "Perspectivas", BASE_URL + "perspectivas.html"
    elif meta["kind"] == "sector":
        middle_name, middle_url = "Sectores", BASE_URL + "#sectores"
    else:
        middle_name, middle_url = "La firma", absolute_url(path)
    elements = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE_URL}]
    if meta["kind"] != "firm":
        elements.append({"@type": "ListItem", "position": 2, "name": middle_name, "item": middle_url})
        position = 3
    else:
        position = 2
    elements.append({"@type": "ListItem", "position": position, "name": meta["title"], "item": absolute_url(path)})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elements}


def primary_schema(path: str, meta: dict[str, object]) -> dict[str, object]:
    common = {
        "@context": "https://schema.org",
        "url": absolute_url(path),
        "name": meta["title"],
        "description": meta["description"],
        "inLanguage": "es-CO",
    }
    if meta["kind"] == "article":
        return {
            **common,
            "@type": "Article",
            "headline": meta["title"],
            "datePublished": RELEASE_DATE,
            "dateModified": RELEASE_DATE,
            "keywords": meta.get("keywords", []),
            "author": {"@type": "Person", "name": "Agustín Rendón Calle"},
            "publisher": {"@type": "Organization", "name": "Meridiano Legal", "url": BASE_URL},
            "mainEntityOfPage": {"@type": "WebPage", "@id": absolute_url(path)},
        }
    if meta["kind"] == "sector":
        return {
            **common,
            "@type": "WebPage",
            "about": {"@type": "Thing", "name": meta["title"]},
            "publisher": {"@type": "Organization", "name": "Meridiano Legal", "url": BASE_URL},
        }
    return {
        "@context": "https://schema.org",
        "@graph": [
            {**common, "@type": "AboutPage", "mainEntity": {"@id": BASE_URL + "#organization"}},
            {
                "@type": "LegalService", "@id": BASE_URL + "#organization", "name": "Meridiano Legal",
                "url": BASE_URL, "areaServed": "Colombia", "founder": {"@id": BASE_URL + "#director"},
            },
            {
                "@type": "Person", "@id": BASE_URL + "#director", "name": "Agustín Rendón Calle",
                "jobTitle": "Fundador y director", "worksFor": {"@id": BASE_URL + "#organization"},
                "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidad EAFIT"},
            },
        ],
    }


def head_block(path: str, meta: dict[str, object]) -> str:
    prefix = prefix_for(path)
    title = escape(str(meta["title"]), quote=True)
    description = escape(str(meta["description"]), quote=True)
    extra = ""
    if meta["kind"] == "article":
        extra = (
            f'  <meta name="author" content="Agustín Rendón Calle">\n'
            f'  <meta property="article:published_time" content="{RELEASE_DATE}">\n'
            f'  <meta property="article:modified_time" content="{RELEASE_DATE}">\n'
        )
    schemas = "\n".join(
        f'  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(",", ":"))}</script>'
        for schema in (primary_schema(path, meta), breadcrumb_schema(path, meta))
    )
    return (
        f"\n  {HEAD_START}\n"
        f'  <meta property="og:url" content="{absolute_url(path)}">\n'
        f'  <meta property="og:site_name" content="Meridiano Legal">\n'
        f'  <meta name="twitter:card" content="summary_large_image">\n'
        f'  <meta name="twitter:title" content="{title}">\n'
        f'  <meta name="twitter:description" content="{description}">\n'
        f'  <meta name="twitter:image" content="{prefix}assets/hero-meridiano-v3.svg">\n'
        f"{extra}"
        f'  <link rel="stylesheet" href="{prefix}page-context.css">\n'
        f"{schemas}\n"
        f"  {HEAD_END}\n"
    )


def set_body_attributes(text: str, meta: dict[str, object]) -> str:
    attributes = {
        "data-page-type": str(meta["type"]),
        "data-page-title": str(meta["title"]),
        "data-page-need": str(meta["need"]),
    }
    match = re.search(r"<body(?P<attrs>[^>]*)>", text, flags=re.IGNORECASE)
    if not match:
        raise ValueError("No se encontró <body>")
    raw_attrs = match.group("attrs")
    for name in attributes:
        raw_attrs = re.sub(rf"\s+{re.escape(name)}=(?:\"[^\"]*\"|'[^']*')", "", raw_attrs, flags=re.IGNORECASE)
    additions = "".join(f' {name}="{escape(value, quote=True)}"' for name, value in attributes.items())
    return text[: match.start()] + f"<body{raw_attrs}{additions}>" + text[match.end() :]


def sequence_link(path: str, target: str, label: str) -> str:
    current = Path(path).parent
    target_path = Path(target)
    if current == Path("."):
        href = target
    else:
        href = target_path.name if target_path.parent == current else "../" + target
    return f'<a href="{href}"><span>{label}</span><strong>{escape(str(PAGES[target]["title"]))}</strong></a>'


def sequence_block(path: str, meta: dict[str, object]) -> str:
    if meta["kind"] == "article":
        order = ARTICLE_ORDER
        index = order.index(path)
        previous = order[index - 1] if index > 0 else order[-1]
        following = order[(index + 1) % len(order)]
        links = sequence_link(path, previous, "Perspectiva anterior") + sequence_link(path, following, "Siguiente perspectiva")
    elif meta["kind"] == "sector":
        order = SECTOR_ORDER
        index = order.index(path)
        previous = order[index - 1] if index > 0 else order[-1]
        following = order[(index + 1) % len(order)]
        links = sequence_link(path, previous, "Sector anterior") + sequence_link(path, following, "Siguiente sector")
    else:
        links = (
            '<a href="index.html#servicios"><span>Portafolio</span><strong>Explorar servicios profesionales</strong></a>'
            '<a href="perspectivas.html"><span>Biblioteca</span><strong>Leer perspectivas jurídicas</strong></a>'
        )
    return (
        f"\n{SEQUENCE_START}\n"
        f'<nav class="editorial-sequence" aria-label="Navegación relacionada"><div class="container">{links}</div></nav>\n'
        f"{SEQUENCE_END}\n"
    )


def enrich(path: str, meta: dict[str, object]) -> bool:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    original = text

    for start, end in ((HEAD_START, HEAD_END), (JOURNEY_START, JOURNEY_END), (SEQUENCE_START, SEQUENCE_END), (SCRIPT_START, SCRIPT_END)):
        text = managed_pattern(start, end).sub("\n", text)

    prefix = prefix_for(path)
    text = re.sub(r'\s*<link rel="stylesheet" href="(?:\.\./)?page-context\.css">', "", text)
    text = re.sub(r'\s*<script src="(?:\.\./)?page-context\.js"></script>', "", text)
    text = text.replace("</head>", head_block(path, meta) + "</head>", 1)
    text = set_body_attributes(text, meta)

    explicit_contact = contact_url(path, meta)
    text = re.sub(
        r'href="(?:\.\./)?index\.html(?:\?[^\"]*)?#contacto"',
        f'href="{escape(explicit_contact, quote=True)}"',
        text,
    )

    journey = (
        f"\n{JOURNEY_START}\n"
        f'<div class="journey-bar editorial-journey"><div class="container"><span>{escape(str(meta["type"]))}</span>'
        f'<strong>{escape(str(meta["title"]))}</strong><div><a href="{escape(str(meta["back_href"]), quote=True)}">{escape(str(meta["back_label"]))}</a>'
        f'<a href="{escape(explicit_contact, quote=True)}">Presentar esta necesidad →</a></div></div></div>\n'
        f"{JOURNEY_END}\n"
    )
    text = text.replace("</header>", "</header>" + journey, 1)
    text = text.replace("<footer", sequence_block(path, meta) + "<footer", 1)
    script = f'\n{SCRIPT_START}\n<script src="{prefix}page-context.js"></script>\n{SCRIPT_END}\n'
    text = text.replace("</body>", script + "</body>", 1)

    # Mejora atributos básicos sin alterar el contenido.
    text = re.sub(r'<nav class="(firm-nav|insight-nav|sector-nav)"(?![^>]*aria-label)', r'<nav class="\1" aria-label="Navegación principal"', text)
    text = re.sub(r'<a class="(insight-brand|sector-brand)" href="([^"]+)"(?![^>]*aria-label)', r'<a class="\1" href="\2" aria-label="Meridiano Legal, inicio"', text)

    if text != original:
        file_path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = []
    for path, meta in PAGES.items():
        if not (ROOT / path).exists():
            raise FileNotFoundError(path)
        if enrich(path, meta):
            changed.append(path)
    print(f"Páginas editoriales actualizadas: {len(changed)}")
    for path in changed:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

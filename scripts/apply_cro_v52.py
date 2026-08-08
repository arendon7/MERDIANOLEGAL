#!/usr/bin/env python3
"""v5.2: refuerza CRO, SEO de intención y FAQ estructurado en soluciones/ sin duplicar el catálogo."""
from __future__ import annotations

from html import escape
from pathlib import Path
import json
import re

R = Path(__file__).resolve().parents[1]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8"))["version"]
DATA = json.loads((R / "cro-solutions-v52.json").read_text(encoding="utf-8"))
V51 = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
V51_BY_SLUG = {item["slug"]: item for item in V51["solutions"]}


def semver(value: str) -> tuple[int, int, int]:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, m.groups())) if m else (0, 0, 0)


def strip_managed(text: str) -> str:
    return re.sub(r"\n?<!-- CRO-V52-[A-Z-]+:START -->[\s\S]*?<!-- CRO-V52-[A-Z-]+:END -->\n?", "\n", text)


def replace_meta(text: str, attr: str, value: str) -> str:
    escaped = escape(value, quote=True)
    pattern = rf'(<meta {re.escape(attr)} content=")[^"]*(">)'
    updated, count = re.subn(pattern, rf'\g<1>{escaped}\g<2>', text, count=1)
    if count != 1:
        raise RuntimeError(f"No se pudo reemplazar meta {attr}")
    return updated


def css_block(prefix: str) -> str:
    return f'<!-- CRO-V52-CSS:START -->\n  <link rel="stylesheet" href="{prefix}cro-v52.css">\n<!-- CRO-V52-CSS:END -->'


def faq_schema(item: dict) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}}
            for question, answer in item["faq"]
        ],
    }
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return f'<!-- CRO-V52-FAQ-SCHEMA:START -->\n  <script type="application/ld+json" data-cro-v52="faq">{raw}</script>\n<!-- CRO-V52-FAQ-SCHEMA:END -->'


def render_fit(item: dict) -> str:
    yes = "".join(f"<li>{escape(value)}</li>" for value in item["fit"])
    no = "".join(f"<li>{escape(value)}</li>" for value in item["not_fit"])
    return (
        '<!-- CRO-V52-FIT:START -->\n<section class="growth-section-v51 cro-fit-v52"><div class="container">'
        '<div class="growth-heading-v51"><p class="eyebrow dark">ENCAJE</p><h2>Antes de escoger modalidad, confirme si este es realmente el problema.</h2>'
        '<p>Una buena conversión no consiste en empujar un servicio: consiste en delimitar cuándo una intervención tiene sentido y cuándo conviene otra ruta.</p></div>'
        f'<div class="cro-fit-grid-v52"><article class="cro-fit-card-v52 is-fit"><h3>Conviene explorar esta ruta cuando…</h3><ul>{yes}</ul></article>'
        f'<article class="cro-fit-card-v52 is-not"><h3>No necesariamente es la ruta correcta cuando…</h3><ul>{no}</ul></article></div></div></section>\n<!-- CRO-V52-FIT:END -->'
    )


def render_objections(item: dict) -> str:
    cards = "".join(
        f'<article class="cro-objection-v52"><h3>{escape(question)}</h3><p>{escape(answer)}</p></article>'
        for question, answer in item["objections"]
    )
    return (
        '<!-- CRO-V52-OBJECTIONS:START -->\n<section class="growth-section-v51 cro-objections-v52"><div class="container">'
        '<div class="growth-heading-v51"><p class="eyebrow dark">OBJECIONES FRECUENTES</p><h2>Lo que conviene aclarar antes de contratar.</h2>'
        '<p>Estas respuestas delimitan mejor el alcance y evitan contratar por una expectativa que la intervención no está diseñada para cumplir.</p></div>'
        f'<div class="cro-objections-grid-v52">{cards}</div></div></section>\n<!-- CRO-V52-OBJECTIONS:END -->'
    )


def render_pricing(item: dict) -> str:
    pricing = item["pricing"]
    return (
        '<!-- CRO-V52-PRICING:START -->\n<section class="growth-section-v51"><div class="container">'
        f'<div class="cro-pricing-v52"><p class="eyebrow dark">ALCANCE Y HONORARIOS</p><h3>{escape(pricing["title"])}</h3>'
        f'<p>{escape(pricing["copy"])}</p><a href="{pricing["href"]}">Revisar referencias públicas de honorarios →</a></div></div></section>\n<!-- CRO-V52-PRICING:END -->'
    )


def render_faq(item: dict) -> str:
    details = "".join(
        f'<details><summary>{escape(question)}</summary><p>{escape(answer)}</p></details>'
        for question, answer in item["faq"]
    )
    return (
        '<!-- CRO-V52-FAQ:START -->\n<section class="growth-section-v51"><div class="container">'
        '<div class="growth-heading-v51"><p class="eyebrow dark">PREGUNTAS FRECUENTES</p><h2>Preguntas que suelen aparecer antes de definir alcance.</h2>'
        '<p>Las respuestas son generales y no sustituyen la revisión del caso concreto, pero ayudan a llegar a la primera conversación con expectativas más precisas.</p></div>'
        f'<div class="cro-faq-v52">{details}</div></div></section>\n<!-- CRO-V52-FAQ:END -->'
    )


def render_related(item: dict) -> str:
    links = []
    for slug in item["related"]:
        related = V51_BY_SLUG[slug]
        links.append(f'<a href="{slug}.html"><strong>{escape(related["short"])}</strong><span>Explorar ruta →</span></a>')
    return (
        '<!-- CRO-V52-RELATED:START -->\n<section class="growth-section-v51 cro-related-v52"><div class="container">'
        '<div class="growth-heading-v51"><p class="eyebrow">RUTAS RELACIONADAS</p><h2>Si el problema cambia al profundizar, estas rutas suelen conectarse.</h2>'
        '<p>La calificación inicial puede mover la necesidad hacia otra modalidad sin obligar a empezar de cero.</p></div>'
        f'<div class="cro-related-grid-v52">{"".join(links)}</div></div></section>\n<!-- CRO-V52-RELATED:END -->'
    )


def patch_solution(item: dict) -> None:
    path = R / "soluciones" / f'{item["slug"]}.html'
    if not path.exists():
        raise RuntimeError(f"Falta {path.relative_to(R)}")
    text = strip_managed(path.read_text(encoding="utf-8")).replace(' data-cro-v52="solution"', '')
    text = re.sub(r"<title>[\s\S]*?</title>", f'<title>{escape(item["seo_title"])}</title>', text, count=1)
    text = replace_meta(text, 'name="description"', item["seo_description"])
    text = replace_meta(text, 'property="og:title"', item["seo_title"])
    text = replace_meta(text, 'property="og:description"', item["seo_description"])
    text = text.replace("</head>", css_block("../") + "\n" + faq_schema(item) + "\n</head>", 1)
    text = text.replace('data-growth-v51="solution"', 'data-growth-v51="solution" data-cro-v52="solution"', 1)

    intent = '<!-- CRO-V52-INTENT:START -->\n' + f'<div class="cro-intent-v52"><strong>{escape(item["decision_label"])}</strong><p>{escape(item["decision_copy"])}</p></div>\n' + '<!-- CRO-V52-INTENT:END -->'
    text, count = re.subn(r'(<p class="growth-intent-v51">[\s\S]*?</p>)', lambda m: m.group(1) + intent, text, count=1)
    if count != 1:
        raise RuntimeError(f"{path.name}: no se encontró growth-intent-v51")

    marker = '<section class="growth-section-v51 growth-dark-v51">'
    if marker not in text:
        raise RuntimeError(f"{path.name}: falta bloque de decisiones")
    text = text.replace(marker, render_fit(item) + "\n" + marker, 1)

    result_marker = '<section class="growth-section-v51 growth-soft-v51">'
    if result_marker not in text:
        raise RuntimeError(f"{path.name}: falta bloque de resultado")
    text = text.replace(result_marker, render_objections(item) + "\n" + render_pricing(item) + "\n" + result_marker, 1)

    proof_marker = '<section class="growth-section-v51 growth-proof-page-v51">'
    if proof_marker not in text:
        raise RuntimeError(f"{path.name}: falta bloque de prueba")
    text = text.replace(proof_marker, render_faq(item) + "\n" + render_related(item) + "\n" + proof_marker, 1)

    generic_title = "No necesita identificar el servicio correcto antes de escribir."
    generic_copy = "Describa la decisión, plazo, actores y resultado esperado. La primera revisión busca definir punto de entrada, disponibilidad y alcance; no requiere enviar documentos confidenciales."
    if generic_title not in text or generic_copy not in text:
        raise RuntimeError(f"{path.name}: CTA genérico v5.1 no encontrado")
    text = text.replace(generic_title, escape(item["cta_title"]), 1).replace(generic_copy, escape(item["cta_copy"]), 1)
    path.write_text(text, encoding="utf-8")


def patch_hub() -> None:
    item = DATA["hub"]
    path = R / "soluciones" / "index.html"
    text = strip_managed(path.read_text(encoding="utf-8")).replace(' data-cro-v52="hub"', '')
    text = re.sub(r"<title>[\s\S]*?</title>", f'<title>{escape(item["seo_title"])}</title>', text, count=1)
    text = replace_meta(text, 'name="description"', item["seo_description"])
    text = replace_meta(text, 'property="og:title"', item["seo_title"])
    text = replace_meta(text, 'property="og:description"', item["seo_description"])
    text = text.replace("</head>", css_block("../") + "\n</head>", 1)
    text = text.replace('data-growth-v51="hub"', 'data-growth-v51="hub" data-cro-v52="hub"', 1)
    cards = "".join(
        f'<a href="{guide["href"]}"><strong>{escape(guide["title"])}</strong><p>{escape(guide["copy"])}</p><span>Ver punto de entrada →</span></a>'
        for guide in item["guides"]
    )
    guide = (
        '<!-- CRO-V52-HUB-GUIDE:START -->\n<section class="cro-hub-guide-v52" aria-label="Guía rápida para escoger ruta">'
        f'<div class="container"><div class="growth-heading-v51"><p class="eyebrow dark">GUÍA RÁPIDA</p><h2>{escape(item["headline"])}</h2><p>{escape(item["intro"])}</p></div></div>'
        f'<div class="container">{cards}</div></section>\n<!-- CRO-V52-HUB-GUIDE:END -->'
    )
    route_marker = '<section class="growth-section-v51"><div class="container"><div class="growth-route-grid-v51">'
    if route_marker not in text:
        raise RuntimeError("soluciones/index.html: grid de rutas no encontrado")
    text = text.replace(route_marker, guide + "\n" + route_marker, 1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if semver(VERSION) < (5, 2, 0):
        raise SystemExit("v5.2 requiere version.json >= 5.2.0")
    if DATA.get("version") != "5.2.0" or len(DATA.get("solutions", [])) != 6:
        raise SystemExit("cro-solutions-v52.json debe declarar 6 rutas v5.2.0")
    expected = set(V51_BY_SLUG)
    actual = {item["slug"] for item in DATA["solutions"]}
    if expected != actual:
        raise SystemExit(f"v5.2 debe cubrir exactamente las rutas v5.1: {sorted(expected ^ actual)}")
    patch_hub()
    for item in DATA["solutions"]:
        patch_solution(item)
    print(f"CRO/SEO v{VERSION} aplicado: encaje, objeciones, honorarios, FAQ schema y rutas relacionadas en 6 soluciones.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

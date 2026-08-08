#!/usr/bin/env python3
"""v5.1: genera rutas comerciales por situación empresarial y prueba pública verificable."""
from __future__ import annotations

from pathlib import Path
from html import escape
from urllib.parse import quote_plus
import json
import re

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
BASE_URL = CONFIG["base_url"]
VERSION_DATA = json.loads((R / "version.json").read_text(encoding="utf-8"))
VERSION = VERSION_DATA["version"]
RELEASE_DATE = VERSION_DATA["release_date"]
DATA = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
SOLUTIONS = DATA["solutions"]

CSS_A = "<!-- GROWTH-V51-CSS:START -->"
CSS_B = "<!-- GROWTH-V51-CSS:END -->"
PROOF_A = "<!-- GROWTH-V51-PROOF:START -->"
PROOF_B = "<!-- GROWTH-V51-PROOF:END -->"
SITEMAP_A = "<!-- GROWTH-V51-SITEMAP:START -->"
SITEMAP_B = "<!-- GROWTH-V51-SITEMAP:END -->"


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def managed_remove(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r"[\s\S]*?" + re.escape(end) + r"\n?", "", text, count=1)


def contact_href(item: dict) -> str:
    context = quote_plus(item["title"])
    need = quote_plus(item["need"])
    return f"../index.html?context={context}&amp;need={need}#contacto"


def route_cards(prefix: str = "") -> str:
    cards = []
    for index, item in enumerate(SOLUTIONS, 1):
        cards.append(
            f'<a class="growth-route-card-v51" href="{prefix}{item["slug"]}.html">'
            f'<span>{index:02d}</span><strong>{escape(item["short"])}</strong>'
            f'<p>{escape(item["intent"])}</p><b>Ver ruta de decisión →</b></a>'
        )
    return "".join(cards)


def render_solution(item: dict) -> str:
    relative = f'soluciones/{item["slug"]}.html'
    canonical = BASE_URL + relative
    page_title = f'{item["title"]} | Meridiano Legal'
    description = item["description"]
    signals = "".join(f'<li>{escape(value)}</li>' for value in item["signals"])
    questions = "".join(f'<li>{escape(value)}</li>' for value in item["questions"])
    deliverables = "".join(f'<li>{escape(value)}</li>' for value in item["deliverables"])
    offers = "".join(
        f'<article><h3>{escape(route["name"])}</h3><p>{escape(route["summary"])}</p>'
        f'<a href="{route["href"]}">Revisar alcance →</a></article>'
        for route in item["routes"]
    )
    schema = json.dumps(
        {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebPage",
                    "@id": canonical + "#webpage",
                    "url": canonical,
                    "name": item["title"],
                    "description": description,
                    "inLanguage": "es-CO",
                    "isPartOf": {"@id": BASE_URL + "#website"},
                    "about": {"@id": BASE_URL + "#organization"},
                },
                {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE_URL},
                        {"@type": "ListItem", "position": 2, "name": "Soluciones", "item": BASE_URL + "soluciones/"},
                        {"@type": "ListItem", "position": 3, "name": item["short"], "item": canonical},
                    ],
                },
            ],
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return f'''<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta property="og:title" content="{escape(page_title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website"><meta property="og:image" content="../assets/images/global/home-hero.webp">
  <title>{escape(page_title)}</title>
  <link rel="icon" href="../assets/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../site-v3.css"><link rel="stylesheet" href="../visual-v39.css"><link rel="stylesheet" href="../page-context.css"><link rel="stylesheet" href="../growth-v51.css">
  <script type="application/ld+json">{schema}</script>
</head>
<body class="growth-page-v51" data-growth-v51="solution">
<a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="growth-header-v51"><div class="container"><a class="growth-brand-v51" href="../index.html"><img src="../assets/brand/meridiano-logo-horizontal-dark.svg" alt="Meridiano Legal"></a><nav aria-label="Navegación de solución"><a href="../index.html#servicios">Servicios</a><a href="../index.html#productos">Productos</a><a href="../index.html#sectores">Sectores</a><a href="../firma.html">Firma</a></nav><a class="btn btn-navy" href="{contact_href(item)}">Presentar necesidad</a></div></header>
<main id="contenido">
<section class="growth-hero-v51"><div class="container growth-hero-grid-v51"><div><p class="eyebrow dark">{escape(item["eyebrow"])}</p><h1>{escape(item["title"])}</h1><p class="growth-lead-v51">{escape(description)}</p><p class="growth-intent-v51">{escape(item["intent"])}</p><div class="growth-actions-v51"><a class="btn btn-gold btn-lg" href="{contact_href(item)}">Presentar esta situación →</a><a class="btn btn-outline-dark btn-lg" href="#ruta">Ver cómo se estructura</a></div></div><aside><span>RUTA DE DECISIÓN</span><ol><li>Comprender contexto y resultado.</li><li>Delimitar riesgo y dependencias.</li><li>Elegir modalidad y alcance.</li><li>Definir entregables y cierre.</li></ol></aside></div></section>
<section class="growth-section-v51" id="senales"><div class="container growth-two-v51"><div><p class="eyebrow dark">CUÁNDO CONVIENE ACTUAR</p><h2>Señales de que esta necesidad ya está abierta.</h2></div><ul class="growth-checklist-v51">{signals}</ul></div></section>
<section class="growth-section-v51 growth-dark-v51"><div class="container growth-two-v51"><div><p class="eyebrow">DECISIONES</p><h2>Las preguntas que deben quedar resueltas.</h2></div><ol class="growth-numbered-v51">{questions}</ol></div></section>
<section class="growth-section-v51" id="ruta"><div class="container"><div class="growth-heading-v51"><p class="eyebrow dark">MODALIDAD ADECUADA</p><h2>La misma situación puede exigir un producto cerrado, un servicio adaptable o capacidad recurrente.</h2><p>La modalidad se define por resultado, perímetro, urgencia, volumen, necesidad de negociación y nivel de seguimiento.</p></div><div class="growth-offer-grid-v51">{offers}</div></div></section>
<section class="growth-section-v51 growth-soft-v51"><div class="container growth-two-v51"><div><p class="eyebrow dark">RESULTADO ESPERADO</p><h2>Qué puede recibir la empresa.</h2></div><ul class="growth-deliverables-v51">{deliverables}</ul></div></section>
<section class="growth-section-v51"><div class="container growth-boundary-v51"><div><p class="eyebrow dark">LÍMITES</p><h2>Qué no debe asumirse dentro del alcance.</h2></div><p>{escape(item["limits"])}</p></div></section>
<section class="growth-section-v51 growth-proof-page-v51"><div class="container"><div class="growth-heading-v51"><p class="eyebrow dark">REVISAR ANTES DE CONTACTAR</p><h2>Puede validar criterio, sector y método antes de presentar la necesidad.</h2></div><div class="growth-proof-links-v51"><a href="{item["perspective"]["href"]}"><strong>{escape(item["perspective"]["name"])}</strong><span>Perspectiva jurídica desarrollada →</span></a><a href="{item["sector"]["href"]}"><strong>{escape(item["sector"]["name"])}</strong><span>Lectura sectorial →</span></a><a href="../experiencia.html"><strong>Centro Demo</strong><span>Recorrido con datos ficticios →</span></a><a href="../firma.html"><strong>Firma y método</strong><span>Cómo se estructura el trabajo →</span></a></div></div></section>
<section class="growth-cta-v51"><div class="container"><div><p class="eyebrow">SIGUIENTE PASO</p><h2>No necesita identificar el servicio correcto antes de escribir.</h2><p>Describa la decisión, plazo, actores y resultado esperado. La primera revisión busca definir punto de entrada, disponibilidad y alcance; no requiere enviar documentos confidenciales.</p></div><a class="btn btn-gold btn-lg" href="{contact_href(item)}">Presentar necesidad →</a></div></section>
</main>
<footer class="growth-footer-v51"><div class="container"><span>Meridiano Legal · Medellín, Colombia · Web pública v{escape(VERSION)}</span><nav aria-label="Legal"><a href="../aviso-legal.html">Aviso legal</a><a href="../privacidad.html">Privacidad</a><a href="../terminos.html">Términos</a></nav></div></footer>
</body></html>'''


def render_hub() -> str:
    canonical = BASE_URL + "soluciones/"
    description = "Rutas de entrada para ordenar riesgo jurídico, dirección externa, IA, inversión, proyectos regulados y operaciones jurídicas."
    schema = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "CollectionPage",
            "@id": canonical + "#webpage",
            "url": canonical,
            "name": "Soluciones por situación empresarial | Meridiano Legal",
            "description": description,
            "inLanguage": "es-CO",
            "isPartOf": {"@id": BASE_URL + "#website"},
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return f'''<!doctype html>
<html lang="es-CO"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow,max-image-preview:large"><meta name="description" content="{description}"><meta property="og:title" content="Soluciones por situación empresarial | Meridiano Legal"><meta property="og:description" content="Empiece por la decisión empresarial y revise después la modalidad jurídica adecuada."><meta property="og:type" content="website"><meta property="og:image" content="../assets/images/global/home-hero.webp"><title>Soluciones por situación empresarial | Meridiano Legal</title><link rel="icon" href="../assets/brand/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="../site-v3.css"><link rel="stylesheet" href="../visual-v39.css"><link rel="stylesheet" href="../growth-v51.css"><script type="application/ld+json">{schema}</script></head>
<body class="growth-page-v51" data-growth-v51="hub"><a class="skip-link" href="#contenido">Saltar al contenido</a><header class="growth-header-v51"><div class="container"><a class="growth-brand-v51" href="../index.html"><img src="../assets/brand/meridiano-logo-horizontal-dark.svg" alt="Meridiano Legal"></a><nav aria-label="Navegación de soluciones"><a href="../index.html#servicios">Servicios</a><a href="../index.html#productos">Productos</a><a href="../index.html#sectores">Sectores</a><a href="../firma.html">Firma</a></nav><a class="btn btn-navy" href="../index.html#contacto">Presentar necesidad</a></div></header>
<main id="contenido"><section class="growth-hub-hero-v51"><div class="container"><p class="eyebrow dark">SOLUCIONES POR SITUACIÓN EMPRESARIAL</p><h1>Empiece por la decisión. La modalidad jurídica viene después.</h1><p>Estas rutas conectan problemas frecuentes con productos cerrados, servicios especializados, planes recurrentes, perspectivas y experiencia sectorial. No sustituyen la calificación profesional del caso.</p></div></section><section class="growth-section-v51"><div class="container"><div class="growth-route-grid-v51">{route_cards()}</div></div></section><section class="growth-cta-v51"><div class="container"><div><p class="eyebrow">SI SU SITUACIÓN NO ENCAJA</p><h2>Puede presentar el resultado esperado directamente.</h2><p>Meridiano calificará si corresponde orientación, diagnóstico, producto cerrado, servicio, plan recurrente o coordinación con otra especialidad.</p></div><a class="btn btn-gold btn-lg" href="../index.html#contacto">Presentar necesidad →</a></div></section></main><footer class="growth-footer-v51"><div class="container"><span>Meridiano Legal · Medellín, Colombia · Web pública v{escape(VERSION)}</span><nav aria-label="Legal"><a href="../aviso-legal.html">Aviso legal</a><a href="../privacidad.html">Privacidad</a><a href="../terminos.html">Términos</a></nav></div></footer></body></html>'''


def write_solutions() -> None:
    folder = R / "soluciones"
    folder.mkdir(exist_ok=True)
    expected = {"index.html", *(f'{item["slug"]}.html' for item in SOLUTIONS)}
    for path in folder.glob("*.html"):
        if path.name not in expected:
            path.unlink()
    (folder / "index.html").write_text(render_hub(), encoding="utf-8")
    for item in SOLUTIONS:
        (folder / f'{item["slug"]}.html').write_text(render_solution(item), encoding="utf-8")


def patch_index() -> None:
    path = R / "index.html"
    text = path.read_text(encoding="utf-8")
    text = managed_remove(text, CSS_A, CSS_B)
    css = f'{CSS_A}\n  <link rel="stylesheet" href="growth-v51.css">\n{CSS_B}'
    text = text.replace("</head>", css + "\n</head>", 1)
    needs = (
        '<section class="section needs-section" id="necesidades"><div class="container">'
        '<div class="section-heading centered"><p class="eyebrow dark">PUNTO DE ENTRADA POR NECESIDAD</p>'
        '<h2>Empiece por la situación empresarial, no por el nombre del servicio.</h2>'
        '<p>Estas seis rutas explican qué señales observar, qué decisiones deben resolverse y qué modalidad jurídica puede encajar antes de solicitar una propuesta.</p></div>'
        f'<div class="needs-grid growth-needs-v51">{route_cards("soluciones/")}</div>'
        '<div class="growth-needs-action-v51"><a href="soluciones/">Ver las seis rutas completas →</a>'
        '<span>Producto cerrado · servicio especializado · plan recurrente</span></div></div></section>'
    )
    text, count = re.subn(r'<section class="section needs-section" id="necesidades">[\s\S]*?</section>', needs, text, count=1)
    if count != 1:
        raise RuntimeError("index.html: no se pudo reemplazar necesidades")
    text = managed_remove(text, PROOF_A, PROOF_B)
    proof = (
        f'{PROOF_A}\n<section class="growth-proof-v51" aria-label="Evidencia pública verificable"><div class="container">'
        '<div class="growth-proof-intro-v51"><p class="eyebrow dark">ANTES DE CONTRATAR</p><h2>La prueba pública debe poder revisarse, no solo prometerse.</h2>'
        '<p>Por eso la web expone alcance, método, límites, conocimiento sectorial y una demostración ficticia antes de pedir información confidencial.</p></div>'
        '<div class="growth-proof-grid-v51"><a href="#servicios"><strong>16 fichas profundas</strong><span>Servicios y productos con alcance, entregables, responsabilidades y límites.</span></a>'
        '<a href="#sectores"><strong>8 lecturas sectoriales</strong><span>Decisiones, dependencias y riesgos conectados con la operación.</span></a>'
        '<a href="perspectivas.html"><strong>6 perspectivas desarrolladas</strong><span>Criterio jurídico explicado antes de una conversación comercial.</span></a>'
        '<a href="experiencia.html"><strong>Centro Demo</strong><span>Recorrido con información ficticia para visualizar método, entregables y seguimiento.</span></a></div>'
        '<div class="growth-proof-actions-v51"><a href="firma.html">Conocer la firma y su método →</a><a href="#contacto">Presentar una necesidad →</a></div></div></section>\n'
        f'{PROOF_B}'
    )
    if needs not in text:
        raise RuntimeError("index.html: bloque necesidades generado no encontrado")
    text = text.replace(needs, needs + "\n" + proof, 1)
    path.write_text(text, encoding="utf-8")


def patch_sitemap() -> None:
    path = R / "sitemap.xml"
    text = managed_remove(path.read_text(encoding="utf-8"), SITEMAP_A, SITEMAP_B)
    entries = [("soluciones/", "0.9"), *((f'soluciones/{item["slug"]}.html', "0.8") for item in SOLUTIONS)]
    urls = "".join(
        f'  <url><loc>{BASE_URL}{relative}</loc><lastmod>{RELEASE_DATE}</lastmod><changefreq>monthly</changefreq><priority>{priority}</priority></url>\n'
        for relative, priority in entries
    )
    if "</urlset>" not in text:
        raise RuntimeError("sitemap.xml: falta cierre urlset")
    text = text.replace("</urlset>", f'{SITEMAP_A}\n{urls}{SITEMAP_B}\n</urlset>', 1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if semver(VERSION) < (5, 1, 0):
        raise SystemExit("v5.1 requiere version.json >= 5.1.0")
    if DATA.get("version") != "5.1.0" or len(SOLUTIONS) != 6:
        raise SystemExit("growth-solutions-v51.json debe contener exactamente 6 rutas v5.1.0")
    write_solutions()
    patch_index()
    patch_sitemap()
    print(f"Crecimiento v{VERSION} aplicado: 6 rutas por situación, hub indexable y prueba verificable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

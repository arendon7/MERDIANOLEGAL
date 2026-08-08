#!/usr/bin/env python3
"""Valida el cierre de calidad visual, comercial, SEO y accesibilidad v4.8."""

from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
CATALOG_HOME = ROOT / "catalog-home-v32.js"
DEMO = ROOT / "demo.html"
SITEMAP = ROOT / "sitemap.xml"
VERSION_DATA = json.loads((ROOT / "version.json").read_text(encoding="utf-8"))
VERSION = VERSION_DATA.get("version", "")
RELEASE_DATE = VERSION_DATA.get("release_date", "")
errors: list[str] = []


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


if semver(VERSION) < (4, 8, 0):
    errors.append(f"version.json debe ser 4.8.0 o superior y registra {VERSION!r}")

for relative in ("quality-v48.css", "scripts/apply_quality_v48.py", "scripts/validate_quality_v48.py"):
    path = ROOT / relative
    if not path.exists() or path.stat().st_size < 400:
        errors.append(f"Falta recurso sustantivo {relative}")

text = INDEX.read_text(encoding="utf-8")
required_index = [
    '<html lang="es-CO">',
    'href="quality-v48.css"',
    'href="page-context.css"',
    'QUALITY-V48-SEO:START',
    'meta name="robots" content="index,follow,max-image-preview:large"',
    'property="og:locale" content="es_CO"',
    'property="og:url" content="https://arendon7.github.io/MERDIANOLEGAL/"',
    'name="twitter:card" content="summary_large_image"',
    'rel="preload" as="image" href="assets/images/global/home-hero.webp"',
    '"@type":["Organization","LegalService"]',
    '<img src="assets/images/global/home-hero.webp"',
    'width="800" height="450"',
    'fetchpriority="high"',
    '<span id="year">2026</span>',
    'class="product-tabs" role="group" aria-label="Filtrar productos"',
]
for marker in required_index:
    if marker not in text:
        errors.append(f"index.html: falta {marker!r}")

for forbidden in ('assets/hero-meridiano-v3.svg', 'role="tablist"', 'data-route=', ' aria-selected='):
    if forbidden in text:
        errors.append(f"index.html conserva estado legado {forbidden!r}")

if text.count('<a class="need-card"') != 6:
    errors.append("La portada debe tener exactamente 6 rutas por necesidad navegables sin JavaScript")
if 'class="need-card" href="servicios/legal-operations.html"' not in text:
    errors.append("Mi operación jurídica debe llevar a Legal Operations")

canonical_products = [
    "Auditoría Jurídica Empresarial Integral",
    "Empresa Jurídicamente Organizada",
    "Marca, Software y Activos Intangibles Protegidos",
    "Empresa Lista para Inversión",
    "Programa de Gobernanza Jurídica y Uso Responsable de IA",
    "Proyecto Regulado Jurídicamente Estructurado",
    "Sistema Contractual Empresarial",
    "Programa de Datos, Consumidor y Canales Digitales",
]
for title in canonical_products:
    if title not in text:
        errors.append(f"index.html: falta nombre canónico de producto {title}")
if text.count('class="full-detail-link"') != 16:
    errors.append("La portada debe publicar 8 enlaces profundos de servicio y 8 de producto en HTML estático")

canonical_sectors = [
    "Tecnología, software e IA",
    "Servicios públicos, aseo y economía circular",
    "Agroindustria y fertilizantes",
    "Salud y negocios regulados",
    "Comercio y distribución",
    "Startups e inversión",
    "Proyectos públicos",
    "Transformación de operaciones jurídicas",
]
for title in canonical_sectors:
    if title not in text:
        errors.append(f"index.html: falta sector canónico {title}")
if text.count('class="sector-deep-link"') != 8:
    errors.append("Los 8 sectores deben ser navegables desde HTML estático")
if "Economía circular y aseo</strong>" in text or "<strong>Servicios públicos</strong>" in text:
    errors.append("La portada conserva la división sectorial previa en vez del catálogo canónico")

if text.count('class="perspective-read-link"') != 3:
    errors.append("Las tres perspectivas destacadas deben enlazar su artículo completo")
if text.count('class="library-deep-link"') != 1:
    errors.append("La portada debe enlazar una sola vez la biblioteca de perspectivas")
if text.count('class="firm-deep-link"') != 1:
    errors.append("La portada debe enlazar la página institucional de la firma")

site = SITE_JS.read_text(encoding="utf-8")
for forbidden in ("const routeMap", "querySelectorAll('[data-route]')", "aria-selected"):
    if forbidden in site:
        errors.append(f"site-v3.js conserva lógica legada {forbidden!r}")
for marker in ("aria-pressed", "Cerrar menú", "menu-open", "prefers-reduced-motion: reduce"):
    if marker not in site:
        errors.append(f"site-v3.js: falta mejora de accesibilidad {marker!r}")

CATALOG_HOME.read_text(encoding="utf-8")

portal = DEMO.read_text(encoding="utf-8")
if '<html lang="es-CO">' not in portal or 'meta name="robots" content="noindex,nofollow"' not in portal:
    errors.append("demo.html debe declarar es-CO y noindex,nofollow")

sitemap = SITEMAP.read_text(encoding="utf-8")
lastmods = re.findall(r"<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>", sitemap)
if not lastmods or any(value != RELEASE_DATE for value in lastmods):
    errors.append("sitemap.xml debe usar release_date como lastmod de las páginas vigentes")
if "demo.html" in sitemap:
    errors.append("demo.html no debe estar en sitemap.xml")

html_targets = list(ROOT.glob("*.html"))
for folder in ("servicios", "productos", "sectores", "perspectivas"):
    html_targets.extend((ROOT / folder).glob("*.html"))
for path in html_targets:
    page = path.read_text(encoding="utf-8")
    if '<html lang="es">' in page:
        errors.append(f"{path.relative_to(ROOT)} conserva lang=es en vez de es-CO")

css = (ROOT / "quality-v48.css").read_text(encoding="utf-8") if (ROOT / "quality-v48.css").exists() else ""
for marker in ("a.need-card", "body.menu-open", "prefers-reduced-motion", "focus-visible"):
    if marker not in css:
        errors.append(f"quality-v48.css: falta {marker!r}")

result = subprocess.run(["node", "--check", str(SITE_JS)], capture_output=True, text=True)
if result.returncode != 0:
    errors.append("site-v3.js no supera node --check: " + result.stderr.strip())
result = subprocess.run(["node", "--check", str(CATALOG_HOME)], capture_output=True, text=True)
if result.returncode != 0:
    errors.append("catalog-home-v32.js no supera node --check: " + result.stderr.strip())

if errors:
    print("VALIDACIÓN DE CALIDAD V4.8 FALLIDA", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"OK: calidad v{VERSION} validada — HTML estático, rutas, accesibilidad, SEO, sitemap y performance.")

#!/usr/bin/env python3
"""Valida rutas de crecimiento, evidencia pública y SEO de v5.1."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
BASE_URL = CONFIG["base_url"]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "")
DATA_PATH = R / "growth-solutions-v51.json"
CSS_PATH = R / "growth-v51.css"
INDEX = R / "index.html"
DISCOVERY_V62 = R / "assets/data/v6/search-discovery-readiness-v62.json"
errors: list[str] = []


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


if semver(VERSION) < (5, 1, 0):
    errors.append(f"version.json debe ser >= 5.1.0 y registra {VERSION!r}")

for relative in (
    "growth-solutions-v51.json",
    "growth-v51.css",
    "scripts/apply_growth_v51.py",
    "scripts/normalize_growth_compat_v51.py",
    "scripts/finalize_growth_v51.py",
    "scripts/validate_growth_v51.py",
    "scripts/validate_live_v51.py",
):
    path = R / relative
    if not path.exists() or path.stat().st_size < 80:
        errors.append(f"Falta recurso v5.1 {relative}")

if DATA_PATH.exists():
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    solutions = data.get("solutions") or []
else:
    data = {}
    solutions = []

if data.get("version") != "5.1.0":
    errors.append("growth-solutions-v51.json debe declarar version 5.1.0")
if len(solutions) != 6:
    errors.append(f"Se esperaban 6 rutas de decisión y se encontraron {len(solutions)}")
slugs = [str(item.get("slug", "")) for item in solutions]
if len(set(slugs)) != len(slugs) or any(not re.fullmatch(r"[a-z0-9-]+", slug) for slug in slugs):
    errors.append("Los slugs v5.1 deben ser únicos y URL-safe")

css = CSS_PATH.read_text(encoding="utf-8") if CSS_PATH.exists() else ""
for marker in (
    ".growth-route-card-v51",
    ".growth-proof-v51",
    ".growth-hero-v51",
    ".growth-offer-grid-v51",
    ".growth-cta-v51",
    "@media(max-width:680px)",
    "@media(prefers-reduced-motion:reduce)",
):
    if marker not in css:
        errors.append(f"growth-v51.css: falta {marker!r}")

index = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
index_markers = [
    'href="growth-v51.css"',
    "GROWTH-V51-CSS:START",
    "GROWTH-V51-PROOF:START",
    "Empiece por la situación empresarial, no por el nombre del servicio.",
    'href="soluciones/"',
    "16 fichas profundas",
    "8 lecturas sectoriales",
    "6 perspectivas desarrolladas",
    "Centro Demo",
]
if semver(VERSION) < (5, 22, 0):
    index_markers.append("La prueba pública debe poder revisarse, no solo prometerse.")
else:
    index_markers.extend((
        "CÓMO SE VE EL CRITERIO SENIOR",
        "La experiencia se demuestra en las preguntas, el alcance y la capacidad de ejecutar.",
        "Antes de contratar, revise si la propuesta identifica régimen, fuentes, supuestos, responsables, límites, entregables y cierre.",
    ))

for marker in index_markers:
    if marker not in index:
        errors.append(f"index.html: falta {marker!r}")
if index.count("GROWTH-V51-PROOF:START") != 1 or index.count("GROWTH-V51-CSS:START") != 1:
    errors.append("index.html debe contener una sola capa gestionada v5.1")
if index.count('class="need-card" href="soluciones/') != 6:
    errors.append("index.html debe exponer exactamente 6 rutas v5.1 con class=need-card exacta")
if index.count('class="growth-proof-grid-v51"') != 1:
    errors.append("index.html debe contener un único bloque de evidencia pública")
for slug in slugs:
    if f'href="soluciones/{slug}.html"' not in index:
        errors.append(f"index.html no enlaza soluciones/{slug}.html")

folder = R / "soluciones"
expected_names = {"index.html", *(f"{slug}.html" for slug in slugs)}
actual_names = {path.name for path in folder.glob("*.html")} if folder.exists() else set()
if actual_names != expected_names:
    errors.append(f"soluciones/: se esperaban {sorted(expected_names)} y existen {sorted(actual_names)}")

hub = folder / "index.html"
if hub.exists():
    hub_text = hub.read_text(encoding="utf-8")
    for marker in (
        'data-growth-v51="hub"',
        "SOLUCIONES POR SITUACIÓN EMPRESARIAL",
        "Empiece por la decisión. La modalidad jurídica viene después.",
        f'<link rel="canonical" href="{BASE_URL}soluciones/">',
        f'<meta property="og:url" content="{BASE_URL}soluciones/">',
        "../telemetry-v50.js",
    ):
        if marker not in hub_text:
            errors.append(f"soluciones/index.html: falta {marker!r}")
    if hub_text.count('class="growth-route-card-v51"') != 6:
        errors.append("soluciones/index.html debe mostrar las 6 rutas")

required_page_markers = [
    'data-growth-v51="solution"',
    "CUÁNDO CONVIENE ACTUAR",
    "Las preguntas que deben quedar resueltas.",
    "MODALIDAD ADECUADA",
    "Qué puede recibir la empresa.",
    "Qué no debe asumirse dentro del alcance.",
    "REVISAR ANTES DE CONTACTAR",
    "../runtime-config.js",
    "../telemetry-v50.js",
]
if semver(VERSION) < (5, 2, 0):
    required_page_markers.append("No necesita identificar el servicio correcto antes de escribir.")
else:
    required_page_markers.append("SIGUIENTE PASO")

for item in solutions:
    slug = item["slug"]
    path = folder / f"{slug}.html"
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    for marker in required_page_markers:
        if marker not in text:
            errors.append(f"soluciones/{slug}.html: falta {marker!r}")
    canonical = BASE_URL + f"soluciones/{slug}.html"
    if f'<link rel="canonical" href="{canonical}">' not in text:
        errors.append(f"soluciones/{slug}.html: canonical incorrecto")
    if f'<meta property="og:url" content="{canonical}">' not in text:
        errors.append(f"soluciones/{slug}.html: og:url incorrecto")
    if text.count('class="growth-offer-grid-v51"') != 1 or text.count("<article><h3>") < 3:
        errors.append(f"soluciones/{slug}.html: debe comparar al menos tres modalidades o rutas")
    if text.count("<li>") < 12:
        errors.append(f"soluciones/{slug}.html: profundidad insuficiente en señales, decisiones y recorrido")
    for route in item.get("routes", []):
        if route.get("href") not in text:
            errors.append(f"soluciones/{slug}.html no enlaza {route.get('href')}")
    for key in ("perspective", "sector"):
        href = (item.get(key) or {}).get("href")
        if href and href not in text:
            errors.append(f"soluciones/{slug}.html no enlaza evidencia {href}")

sitemap = (R / "sitemap.xml").read_text(encoding="utf-8")
for relative in ["soluciones/", *(f"soluciones/{slug}.html" for slug in slugs)]:
    if f"<loc>{BASE_URL}{relative}</loc>" not in sitemap:
        errors.append(f"sitemap.xml no incluye {relative}")
# El marcador físico v5.1 solo es obligatorio en baselines legacy. En una fuente
# v6.2 aún no materializada puede existir transitoriamente; el normalizador y el
# validator Search Discovery son quienes exigen eliminarlo del output canónico.
if not DISCOVERY_V62.exists() and sitemap.count("GROWTH-V51-SITEMAP:START") != 1:
    errors.append("sitemap.xml legacy debe contener un único bloque v5.1")

combined = index + "\n" + "\n".join(path.read_text(encoding="utf-8") for path in folder.glob("*.html")) if folder.exists() else index
for forbidden in ("casos de éxito", "nuestros clientes confían", "tasa de éxito", "testimonio de cliente"):
    if forbidden.lower() in combined.lower():
        errors.append(f"v5.1 no debe publicar prueba social no sustentada: {forbidden!r}")

if errors:
    print("VALIDACIÓN DE CRECIMIENTO V5.1 FALLIDA", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("VALIDACIÓN DE CRECIMIENTO V5.1 OK: 6 rutas, hub, evidencia verificable, SEO e interlinking íntegros; narrativa v5.22 compatible cuando aplica.")

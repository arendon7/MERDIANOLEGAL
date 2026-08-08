#!/usr/bin/env python3
"""Valida arquitectura, jerarquía y responsive UX/UI v4.5 de la portada."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CSS = ROOT / "ux-v45.css"
CATALOG_HOME = ROOT / "catalog-home-v32.js"
DECISION_FLOW = ROOT / "decision-flow.js"
errors: list[str] = []

for relative in ("ux-v45.css", "scripts/apply_ux_v45.py", "scripts/validate_ux_v45.py"):
    if not (ROOT / relative).exists():
        errors.append(f"Falta {relative}")

version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "")
match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(version))
if not match or tuple(map(int, match.groups())) < (4, 5, 0):
    errors.append(f"version.json debe ser 4.5.0 o superior y registra {version!r}")

text = INDEX.read_text(encoding="utf-8")
required = [
    'href="ux-v45.css"',
    '<a href="#necesidades">Necesidades</a>',
    '<a href="#planes">Planes y precios</a>',
    '<a class="btn btn-navy" href="#contacto">Presentar necesidad</a>',
    'class="mobile-nav-actions"',
    'class="mobile-conversion-v45"',
    '8 servicios', '8 productos', '5 planes', '8 sectores', 'Centro demo',
    'id="necesidades"', 'id="elegir"', 'id="servicios"', 'id="productos"',
    'id="entregables"', 'id="experiencia"', 'class="platform-mockup-v45"',
    'Interfaz ilustrativa y datos ficticios', 'id="planes"', 'id="honorarios"',
    'id="contratacion"', 'class="contracting-route-v45"', 'assets/route-meridiano-v3.svg',
    'id="sectores"', 'id="perspectivas"', 'id="firma"', 'id="preguntas"', 'id="contacto"',
    'Planes y honorarios', 'demo.html#documentos', 'Área de clientes',
]
for marker in required:
    if marker not in text:
        errors.append(f"index.html: falta {marker!r}")

for removed in ('id="modalidades"', 'id="documentos"', 'id="ruta"', 'class="section strategic-band"', 'class="section fit-section"'):
    if removed in text:
        errors.append(f"index.html conserva bloque redundante {removed!r}")

if text.count('class="outcome-card"') != 4:
    errors.append("La portada v4.5 debe resumir QUÉ RECIBE LA EMPRESA en exactamente 4 tarjetas")
if text.count('class="platform-mockup-v45"') != 1:
    errors.append("Debe existir un único mockup demostrativo v4.5")
if text.count('class="mobile-conversion-v45"') != 1:
    errors.append("Debe existir un único CTA móvil persistente")
if 'href="#ruta"' in text or 'href="#documentos"' in text:
    errors.append("La navegación pública conserva anclas eliminadas de la portada")

order = [
    'id="necesidades"', 'id="elegir"', 'id="servicios"', 'id="productos"',
    'id="entregables"', 'id="experiencia"', 'id="planes"', 'id="honorarios"',
    'id="contratacion"', 'id="sectores"', 'id="perspectivas"', 'id="firma"',
    'id="preguntas"', 'id="contacto"',
]
positions = [text.find(marker) for marker in order]
if any(position < 0 for position in positions) or positions != sorted(positions):
    errors.append("El orden narrativo v4.5 de la portada no es canónico")

nav_match = re.search(r'<nav id="main-nav" class="main-nav"[^>]*>([\s\S]*?)</nav>', text)
if not nav_match:
    errors.append("No se encontró main-nav")
else:
    nav = nav_match.group(1)
    for legacy in ('href="#elegir"', 'href="#ruta"', 'href="#contacto">Contacto'):
        if legacy in nav:
            errors.append(f"main-nav conserva navegación legada {legacy!r}")

catalog = CATALOG_HOME.read_text(encoding="utf-8") if CATALOG_HOME.exists() else ""
if "nav-perspectives" in catalog:
    errors.append("catalog-home-v32.js todavía inyecta Perspectivas en el menú principal")
flow = DECISION_FLOW.read_text(encoding="utf-8") if DECISION_FLOW.exists() else ""
for legacy in ("nav-selector", "nav-mobile-utility"):
    if legacy in flow:
        errors.append(f"decision-flow.js todavía inyecta navegación legada: {legacy}")

css = CSS.read_text(encoding="utf-8") if CSS.exists() else ""
for marker in (
    ".mobile-conversion-v45", ".platform-mockup-v45", ".commercial-plans", ".contracting-route-v45",
    ":focus-visible", "@media(max-width:700px)", "grid-template-columns:repeat(12,1fr)",
):
    if marker not in css:
        errors.append(f"ux-v45.css: falta {marker!r}")

if errors:
    print("VALIDACIÓN UX/UI V4.5 FALLIDA")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDACIÓN UX/UI V4.5 OK: narrativa, densidad, navegación, mockup, accesibilidad y móvil íntegros.")

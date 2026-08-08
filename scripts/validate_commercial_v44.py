#!/usr/bin/env python3
"""Valida la capa comercial pública y el flujo de conversión v4.4."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
errors: list[str] = []

required_files = [
    "commercial-v43.css",
    "commercial-conversion-v44.js",
    "scripts/apply_commercial_v43.py",
]
for relative in required_files:
    if not (ROOT / relative).exists():
        errors.append(f"Falta {relative}")

version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "")
match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(version))
if not match or tuple(map(int, match.groups())) < (4, 4, 0):
    errors.append(f"version.json debe ser 4.4.0 o superior y registra {version!r}")

text = INDEX.read_text(encoding="utf-8")
markers = [
    "COMMERCIAL-V43:START",
    "COMMERCIAL-V43:END",
    'id="planes"',
    'id="honorarios"',
    'id="contratacion"',
    'href="commercial-v43.css"',
    '<script src="commercial-conversion-v44.js"></script>',
    "PLANES RECURRENTES",
    "REFERENCIAS DE HONORARIOS",
    "CÓMO SE CONTRATA",
    "Plan Esencial",
    "Plan Empresarial",
    "Plan Dirección",
    "Plan Regulado",
    "Banco Documental y Legal Operations",
    "$ 2.800.000 COP",
    "$ 5.200.000 COP",
    "$ 8.500.000 COP",
    "Desde $ 12.000.000 COP",
    "6 horas / mes",
    "14 horas / mes",
    "25 horas / mes",
    "35 horas / mes de referencia",
    "$ 3.500.000",
    "$ 4.500.000",
    "$ 12–25 millones",
    "$ 1.200.000 + tasas",
    "$ 2.500.000 + tasas",
    "$ 4–8 millones",
    "$ 600.000",
    "$ 900.000",
    "$ 1.500.000",
    "$ 1.800.000",
    "$ 2.000.000",
    "horas adicionales se cotizan en $350.000, $450.000 o $550.000 COP",
    "sujetos al alcance definitivo y al IVA cuando corresponda",
    "<option>Plan recurrente</option>",
    'data-commercial-contact="Plan Esencial"',
    'data-commercial-contact="Plan Empresarial"',
    'data-commercial-contact="Plan Dirección"',
    'data-commercial-contact="Plan Regulado"',
    'data-commercial-context="Honorarios: Diagnóstico jurídico"',
    'data-commercial-context="Honorarios: Gobernanza de IA"',
    "La ejecución comienza con aceptación expresa.",
]
for marker in markers:
    if marker not in text:
        errors.append(f"index.html: falta {marker!r}")

if text.count('class="plan-card-v43') != 5:
    errors.append("index.html debe contener exactamente 5 planes")
if text.count('class="contracting-grid-v44') != 1 or text.count('class="contracting-grid-v44"><article>') != 1:
    errors.append("index.html debe contener un único flujo de contratación v4.4")
if text.count("COMMERCIAL-V43:START") != 1 or text.count("COMMERCIAL-V43:END") != 1:
    errors.append("La capa comercial debe existir una sola vez")
if "disponibilidad ilimitada" not in text:
    errors.append("Debe conservarse la aclaración de que los planes no implican disponibilidad ilimitada")
if "Publicamos referencias de honorarios" not in text:
    errors.append("La FAQ de precios no refleja la política de transparencia")
if '<script src="catalog-home-v32.js"></script>' in text:
    errors.append("index.html no debe cargar catalog-home-v32.js directamente; site-v3.js ya lo carga")
if text.count("data-commercial-contact=") < 6:
    errors.append("Faltan CTA comerciales contextualizados")
if text.count("data-commercial-context=") < 4:
    errors.append("Faltan enlaces profundos con contexto comercial")

conversion = (ROOT / "commercial-conversion-v44.js").read_text(encoding="utf-8") if (ROOT / "commercial-conversion-v44.js").exists() else ""
for marker in ["data-commercial-contact", "Plan recurrente", "scrollIntoView", "data-commercial-context"]:
    if marker not in conversion:
        errors.append(f"commercial-conversion-v44.js: falta {marker!r}")

if errors:
    print("VALIDACIÓN COMERCIAL V4.4 FALLIDA")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDACIÓN COMERCIAL V4.4 OK: planes, honorarios, contratación, contexto y CTA íntegros sin doble carga del catálogo.")

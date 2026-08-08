#!/usr/bin/env python3
"""Valida la capa comercial pública v4.3 y evita regresiones de precios/planes."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
errors: list[str] = []

required_files = [
    "commercial-v43.css",
    "scripts/apply_commercial_v43.py",
]
for relative in required_files:
    if not (ROOT / relative).exists():
        errors.append(f"Falta {relative}")

version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "")
match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(version))
if not match or tuple(map(int, match.groups())) < (4, 3, 0):
    errors.append(f"version.json debe ser 4.3.0 o superior y registra {version!r}")

text = INDEX.read_text(encoding="utf-8")
markers = [
    "COMMERCIAL-V43:START",
    "COMMERCIAL-V43:END",
    'id="planes"',
    'id="honorarios"',
    'href="commercial-v43.css"',
    '<script src="catalog-home-v32.js"></script>',
    "PLANES RECURRENTES",
    "REFERENCIAS DE HONORARIOS",
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
]
for marker in markers:
    if marker not in text:
        errors.append(f"index.html: falta {marker!r}")

if text.count('class="plan-card-v43') != 5:
    errors.append("index.html debe contener exactamente 5 planes v4.3")
if text.count("COMMERCIAL-V43:START") != 1 or text.count("COMMERCIAL-V43:END") != 1:
    errors.append("La capa comercial v4.3 debe existir una sola vez")
if "disponibilidad ilimitada" not in text:
    errors.append("Debe conservarse la aclaración de que los planes no implican disponibilidad ilimitada")
if "Publicamos referencias de honorarios" not in text:
    errors.append("La FAQ de precios no refleja la política de transparencia v4.3")

if errors:
    print("VALIDACIÓN COMERCIAL V4.3 FALLIDA")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("VALIDACIÓN COMERCIAL V4.3 OK: 5 planes, precios orientativos, reglas de contratación y enlaces canónicos íntegros.")

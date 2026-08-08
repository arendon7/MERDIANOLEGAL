#!/usr/bin/env python3
"""Valida CRO, SEO de intención, FAQ y continuidad jurídica de v5.2."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

R = Path(__file__).resolve().parents[1]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "")
DATA = json.loads((R / "cro-solutions-v52.json").read_text(encoding="utf-8"))
V51 = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
V51_BY_SLUG = {item["slug"]: item for item in V51["solutions"]}
errors: list[str] = []


def semver(value: str) -> tuple[int, int, int]:
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, m.groups())) if m else (0, 0, 0)


if semver(VERSION) < (5, 2, 0):
    errors.append(f"version.json debe ser >=5.2.0 y registra {VERSION!r}")
if DATA.get("version") != "5.2.0":
    errors.append("cro-solutions-v52.json debe declarar version 5.2.0")
solutions = DATA.get("solutions") or []
if len(solutions) != 6:
    errors.append(f"Se esperaban 6 rutas v5.2 y existen {len(solutions)}")
if {item.get("slug") for item in solutions} != set(V51_BY_SLUG):
    errors.append("v5.2 debe cubrir exactamente las seis rutas v5.1")

for relative in ("cro-solutions-v52.json", "cro-v52.css", "scripts/apply_cro_v52.py", "scripts/validate_cro_v52.py", "scripts/validate_live_v52.py"):
    path = R / relative
    if not path.exists() or path.stat().st_size < 100:
        errors.append(f"Falta recurso sustantivo v5.2: {relative}")

css = (R / "cro-v52.css").read_text(encoding="utf-8") if (R / "cro-v52.css").exists() else ""
for marker in (".cro-fit-v52", ".cro-objections-v52", ".cro-pricing-v52", ".cro-faq-v52", ".cro-related-v52", ".cro-hub-guide-v52", "@media(max-width:680px)", "@media(prefers-reduced-motion:reduce)"):
    if marker not in css:
        errors.append(f"cro-v52.css: falta {marker!r}")

hub = R / "soluciones" / "index.html"
if hub.exists():
    text = hub.read_text(encoding="utf-8")
    for marker in ('data-cro-v52="hub"', 'href="../cro-v52.css"', "Identifique la decisión jurídica antes de escoger el servicio.", "CRO-V52-HUB-GUIDE:START"):
        if marker not in text:
            errors.append(f"soluciones/index.html: falta {marker!r}")
    if text.count("CRO-V52-HUB-GUIDE:START") != 1 or text.count("cro-hub-guide-v52") != 1:
        errors.append("soluciones/index.html debe contener una sola guía CRO v5.2")
else:
    errors.append("Falta soluciones/index.html")

for item in solutions:
    slug = item["slug"]
    path = R / "soluciones" / f"{slug}.html"
    if not path.exists():
        errors.append(f"Falta soluciones/{slug}.html")
        continue
    text = path.read_text(encoding="utf-8")
    required = (
        'data-cro-v52="solution"',
        'href="../cro-v52.css"',
        "CRO-V52-INTENT:START",
        "CRO-V52-FIT:START",
        "CRO-V52-OBJECTIONS:START",
        "CRO-V52-PRICING:START",
        "CRO-V52-FAQ:START",
        "CRO-V52-FAQ-SCHEMA:START",
        "CRO-V52-RELATED:START",
        "OBJECIONES FRECUENTES",
        "ALCANCE Y HONORARIOS",
        "PREGUNTAS FRECUENTES",
        item["cta_title"],
    )
    for marker in required:
        if marker not in text:
            errors.append(f"soluciones/{slug}.html: falta {marker!r}")
    for managed in ("INTENT", "FIT", "OBJECTIONS", "PRICING", "FAQ", "FAQ-SCHEMA", "RELATED", "CSS"):
        if text.count(f"CRO-V52-{managed}:START") != 1:
            errors.append(f"soluciones/{slug}.html: bloque {managed} debe existir exactamente una vez")
    if f"<title>{item['seo_title']}</title>" not in text:
        errors.append(f"soluciones/{slug}.html: title SEO v5.2 incorrecto")
    if item["seo_description"] not in text:
        errors.append(f"soluciones/{slug}.html: description SEO v5.2 ausente")
    if not 35 <= len(item["seo_title"]) <= 75:
        errors.append(f"{slug}: seo_title fuera de rango razonable")
    if not 115 <= len(item["seo_description"]) <= 180:
        errors.append(f"{slug}: seo_description fuera de rango razonable")
    if len(item.get("fit", [])) < 3 or len(item.get("not_fit", [])) < 2:
        errors.append(f"{slug}: encaje/no encaje insuficiente")
    if len(item.get("objections", [])) != 3:
        errors.append(f"{slug}: deben existir 3 objeciones")
    if len(item.get("faq", [])) != 3:
        errors.append(f"{slug}: deben existir 3 FAQ")
    if text.count("<details>") != 3:
        errors.append(f"soluciones/{slug}.html: debe renderizar 3 preguntas FAQ")
    match = re.search(r'<script type="application/ld\+json" data-cro-v52="faq">([\s\S]*?)</script>', text)
    if not match:
        errors.append(f"soluciones/{slug}.html: FAQPage schema no encontrado")
    else:
        try:
            schema = json.loads(match.group(1))
            if schema.get("@type") != "FAQPage" or len(schema.get("mainEntity", [])) != 3:
                errors.append(f"soluciones/{slug}.html: FAQPage schema incompleto")
        except json.JSONDecodeError:
            errors.append(f"soluciones/{slug}.html: FAQPage schema inválido")
    for related in item.get("related", []):
        if related not in V51_BY_SLUG or f'href="{related}.html"' not in text:
            errors.append(f"soluciones/{slug}.html: ruta relacionada inválida {related!r}")
    href = (item.get("pricing") or {}).get("href", "")
    if href not in ("../index.html#honorarios", "../index.html#planes") or href not in text:
        errors.append(f"soluciones/{slug}.html: referencia de honorarios inválida")

raw = json.dumps(DATA, ensure_ascii=False).lower()
for forbidden in ("casos de éxito", "testimonio", "tasa de éxito", "clientes confían", "$", " cop "):
    if forbidden in raw:
        errors.append(f"v5.2 no debe inventar prueba social ni duplicar precios: {forbidden!r}")

if errors:
    print("VALIDACIÓN CRO/SEO V5.2 FALLIDA", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("VALIDACIÓN CRO/SEO V5.2 OK: 6 landings con encaje, objeciones, honorarios, FAQ schema, SEO e interlinking íntegros.")

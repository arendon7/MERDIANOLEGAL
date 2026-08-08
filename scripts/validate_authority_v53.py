#!/usr/bin/env python3
"""Valida autoridad, descubrimiento, schema y contrato de medición v5.3."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
BASE_URL = CONFIG["base_url"]
VERSION_DATA = json.loads((R / "version.json").read_text(encoding="utf-8"))
VERSION = VERSION_DATA.get("version", "")
RELEASE_DATE = VERSION_DATA.get("release_date", "")
AUTH = json.loads((R / "authority-v53.json").read_text(encoding="utf-8"))
CONTRACT = json.loads((R / "measurement-contract-v53.json").read_text(encoding="utf-8"))
V51 = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
SOLUTIONS = {item["slug"]: item for item in V51["solutions"]}
errors: list[str] = []


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


if semver(VERSION) < (5, 3, 0):
    errors.append(f"version.json debe ser >= 5.3.0 y registra {VERSION!r}")

for relative in (
    "authority-v53.json",
    "measurement-contract-v53.json",
    "measurement-v53.js",
    "scripts/apply_authority_v53.py",
    "scripts/validate_authority_v53.py",
    "scripts/validate_live_v53.py",
):
    path = R / relative
    if not path.exists() or path.stat().st_size < 80:
        errors.append(f"Falta recurso v5.3 {relative}")

if AUTH.get("version") != "5.3.0":
    errors.append("authority-v53.json debe declarar 5.3.0")
if len(AUTH.get("perspectives", [])) != 6:
    errors.append("authority-v53.json debe mapear 6 perspectivas")
if len(AUTH.get("sectors", [])) != 8:
    errors.append("authority-v53.json debe mapear 8 sectores")

known_slugs = set(SOLUTIONS)
mapped_slugs: set[str] = set()
for group in ("perspectives", "sectors"):
    seen_paths: set[str] = set()
    for entry in AUTH.get(group, []):
        path = entry.get("path", "")
        if path in seen_paths:
            errors.append(f"{group}: ruta duplicada {path}")
        seen_paths.add(path)
        if not (R / path).exists():
            errors.append(f"{group}: no existe {path}")
        for related in entry.get("solutions", []):
            slug = related.get("slug", "")
            mapped_slugs.add(slug)
            if slug not in known_slugs:
                errors.append(f"{group}: slug desconocido {slug}")
            if len(str(related.get("reason", ""))) < 80:
                errors.append(f"{group}/{path}: razón demasiado corta para {slug}")

if mapped_slugs != known_slugs:
    errors.append(f"v5.3 debe descubrir las 6 soluciones; diferencia: {sorted(mapped_slugs ^ known_slugs)}")

knows = AUTH.get("organization_knows_about") or []
if len(knows) != 8 or len(set(knows)) != 8:
    errors.append("organization_knows_about debe contener 8 materias únicas")

home = (R / "index.html").read_text(encoding="utf-8")
if '"logo":{"@type":"ImageObject","url":"' + BASE_URL + 'assets/brand/meridiano-logo-horizontal-dark.svg"}' not in home:
    errors.append("index.html: Organization debe publicar logo canónico")
for topic in knows:
    if topic not in home:
        errors.append(f"index.html: Organization.knowsAbout no contiene {topic!r}")

hub = (R / "soluciones" / "index.html").read_text(encoding="utf-8")
if 'data-authority-v53="item-list"' not in hub:
    errors.append("soluciones/index.html: falta ItemList v5.3")
for slug in SOLUTIONS:
    if f'"url":"{BASE_URL}soluciones/{slug}.html"' not in hub:
        errors.append(f"soluciones/index.html: ItemList no incluye {slug}")

for slug, item in SOLUTIONS.items():
    path = R / "soluciones" / f"{slug}.html"
    text = path.read_text(encoding="utf-8")
    for marker in (
        f'data-solution-slug="{slug}"',
        f'data-page-need="{item["need"]}"',
        'data-authority-v53="item-list"',
        "../measurement-v53.js",
        "../telemetry-v50.js",
        'data-cro-v52="solution"',
    ):
        if marker not in text:
            errors.append(f"{path.relative_to(R)}: falta {marker!r}")
    if text.count("AUTHORITY-V53-SCHEMA:START") != 1 or text.count("MEASUREMENT-V53:START") != 1:
        errors.append(f"{path.relative_to(R)}: bloques v5.3 duplicados o ausentes")
    for route in item.get("routes", []):
        if route["name"] not in text:
            errors.append(f"{path.relative_to(R)}: ItemList/oferta no conserva {route['name']!r}")

for entry in AUTH.get("perspectives", []):
    path = R / entry["path"]
    text = path.read_text(encoding="utf-8")
    for marker in (
        "DE LA LECTURA A LA DECISIÓN",
        "AUTHORITY-V53-PERSPECTIVE:START",
        'data-authority-v53="item-list"',
        "../measurement-v53.js",
        "../telemetry-v50.js",
        f'<meta property="article:modified_time" content="{RELEASE_DATE}">',
        f'"dateModified":"{RELEASE_DATE}"',
    ):
        if marker not in text:
            errors.append(f"{entry['path']}: falta {marker!r}")
    if text.count("AUTHORITY-V53-PERSPECTIVE:START") != 1:
        errors.append(f"{entry['path']}: bloque de autoridad duplicado")
    for related in entry["solutions"]:
        slug = related["slug"]
        if f'data-authority-solution="{slug}"' not in text or f'../soluciones/{slug}.html' not in text:
            errors.append(f"{entry['path']}: no enlaza ruta {slug}")

for entry in AUTH.get("sectors", []):
    path = R / entry["path"]
    text = path.read_text(encoding="utf-8")
    for marker in (
        "RUTAS POR SITUACIÓN",
        "AUTHORITY-V53-SECTOR:START",
        'data-authority-v53="item-list"',
        "../measurement-v53.js",
        "../telemetry-v50.js",
    ):
        if marker not in text:
            errors.append(f"{entry['path']}: falta {marker!r}")
    if text.count("AUTHORITY-V53-SECTOR:START") != 1:
        errors.append(f"{entry['path']}: bloque de autoridad duplicado")
    for related in entry["solutions"]:
        slug = related["slug"]
        if f'data-authority-solution="{slug}"' not in text or f'../soluciones/{slug}.html' not in text:
            errors.append(f"{entry['path']}: no enlaza ruta {slug}")

if CONTRACT.get("version") != "5.3.0":
    errors.append("measurement-contract-v53.json debe declarar 5.3.0")
privacy = CONTRACT.get("privacy") or {}
if privacy.get("pii_allowed") is not False or privacy.get("network_transport") is not False or privacy.get("persistent_storage") is not False:
    errors.append("Contrato v5.3 debe prohibir PII, transporte de red y almacenamiento persistente")

event_names = [event.get("name") for event in CONTRACT.get("events", [])]
expected_events = {"solution_view", "authority_open", "evidence_open", "route_open", "faq_open", "contact_intent"}
if set(event_names) != expected_events or len(event_names) != len(expected_events):
    errors.append("Contrato v5.3 debe declarar exactamente los 6 eventos CRO aprobados")

js = (R / "measurement-v53.js").read_text(encoding="utf-8")
for event_name in expected_events:
    if f"'{event_name}'" not in js:
        errors.append(f"measurement-v53.js: falta evento {event_name}")
for forbidden in ("fetch(", "XMLHttpRequest", "sendBeacon", "document.cookie", "localStorage", "sessionStorage", "email", "company", "message:"):
    if forbidden in js:
        errors.append(f"measurement-v53.js: uso prohibido {forbidden!r}")
for marker in ("piiAllowed: false", "networkTransport: false", "persistentStorage: false"):
    if marker not in js:
        errors.append(f"measurement-v53.js: falta {marker!r}")

analytics = CONFIG.get("analytics") or {}
if analytics.get("enabled") is not False or analytics.get("provider") != "none":
    errors.append("v5.3 no debe activar analítica externa")
if CONFIG.get("search_console_verification"):
    errors.append("v5.3 no debe inventar ni activar Search Console sin token real")

if errors:
    print("VALIDACIÓN DE AUTORIDAD Y MEDICIÓN V5.3 FALLIDA", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("VALIDACIÓN V5.3 OK: autoridad bidireccional, Organization/ItemList, dateModified y contrato CRO sin PII íntegros.")

#!/usr/bin/env python3
"""Valida v5.31: compresión decisional sin pérdida de verdad jurídica/comercial."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "decision-compression-v531.json"
CSS = ROOT / "decision-compression-v531.css"
DETAILS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
SOLUTIONS = sorted(path for path in (ROOT / "soluciones").glob("*.html") if path.name != "index.html")
STYLE = '<link rel="stylesheet" href="../decision-compression-v531.css">'


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def fail(message: str) -> None:
    raise AssertionError(message)


def validate_contract() -> None:
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if payload.get("version") != "5.31.0":
        fail("contrato debe declarar 5.31.0")
    baseline = payload.get("baseline") or {}
    targets = payload.get("targets") or {}
    preserve = payload.get("preservation") or {}
    if baseline.get("deep_pages") != 16 or baseline.get("solution_routes") != 6:
        fail("baseline debe fijar 16 fichas y 6 rutas")
    if targets.get("deep_always_open_decision_groups_max") != 2:
        fail("target debe limitar a 2 grupos decisionales abiertos antes del núcleo")
    if not targets.get("deep_offer_narrative_progressive") or not targets.get("solution_secondary_progressive"):
        fail("la divulgación progresiva debe ser explícita")
    forbidden_true = [key for key, value in preserve.items() if value is True]
    if forbidden_true:
        fail(f"preservation contiene permisos incompatibles: {forbidden_true}")
    css = CSS.read_text(encoding="utf-8").lower()
    if "display:none" in css.replace(" ", "") or "visibility:hidden" in css.replace(" ", ""):
        fail("v5.31 no puede simular compresión ocultando con CSS")


def details_opening(text: str, value: str) -> str:
    match = re.search(rf'<details[^>]*data-decision-compression-v531="{re.escape(value)}"[^>]*>', text)
    if not match:
        fail(f"falta details {value}")
    return match.group(0)


def validate_deep() -> None:
    if len(DETAILS) != 16:
        fail(f"se esperaban 16 fichas y hay {len(DETAILS)}")
    for path in DETAILS:
        text = path.read_text(encoding="utf-8")
        if text.count(STYLE) != 1:
            fail(f"{path.name}: CSS v5.31 no es único")
        if text.count('data-decision-compression-v531="decision-result"') != 1:
            fail(f"{path.name}: pareja decisión/resultado no es única")
        if text.count('data-decision-compression-v531="offer-narrative"') != 1:
            fail(f"{path.name}: narrativa progresiva no es única")
        opening = details_opening(text, "offer-narrative")
        if re.search(r'\b(open|hidden)\b', opening):
            fail(f"{path.name}: narrativa secundaria debe iniciar cerrada y sin hidden")
        deep_start = text.find('data-decision-compression-v531="offer-narrative"')
        offer_marker = text.find("<!-- OFFER-NARRATIVE-V522:START -->")
        offer_end = text.find("<!-- OFFER-NARRATIVE-V522:END -->")
        if not (deep_start < offer_marker < offer_end):
            fail(f"{path.name}: v5.22 debe conservarse dentro de details v5.31")
        pair_start = text.find('data-decision-compression-v531="decision-result"')
        question = text.find('aria-labelledby="pregunta-title"')
        result = text.find('aria-labelledby="resultado-title"')
        if not (pair_start < question < result < offer_marker):
            fail(f"{path.name}: pregunta + resultado deben formar el segundo grupo abierto")
        v58 = text.find("<!-- DECISION-V58-DETAIL:START -->")
        v530 = text.find("<!-- OFFER-COMMERCIAL-V530:START -->")
        if not (v58 < v530 < pair_start):
            fail(f"{path.name}: v5.8/v5.30 deben seguir siendo el primer grupo abierto")
        for required in ("CRITERIO DE CONTRATACIÓN", "ALTERNATIVA CERCANA", "LENTE JURÍDICA"):
            if required not in text[offer_marker:offer_end]:
                fail(f"{path.name}: se perdió contenido v5.22: {required}")
        if text.count('id="contacto"') != 1 or 'id="alcance-title"' not in text:
            fail(f"{path.name}: contacto o alcance canónico alterado")


def validate_solutions() -> None:
    if len(SOLUTIONS) != 6:
        fail(f"se esperaban 6 rutas de necesidad y hay {len(SOLUTIONS)}")
    for path in SOLUTIONS:
        text = path.read_text(encoding="utf-8")
        if text.count(STYLE) != 1:
            fail(f"{path.name}: CSS v5.31 no es único")
        for key in ("objections", "faq", "related", "proof"):
            value = f"solution-{key}"
            if text.count(f'data-decision-compression-v531="{value}"') != 1:
                fail(f"{path.name}: details {key} no es único")
            opening = details_opening(text, value)
            if re.search(r'\b(open|hidden)\b', opening):
                fail(f"{path.name}: {key} debe iniciar cerrado y sin hidden")
        if text.find('id="ruta"') > text.find('data-decision-compression-v531="solution-objections"'):
            fail(f"{path.name}: la modalidad principal debe permanecer antes de contenido secundario")
        pricing = text.find("<!-- CRO-V52-PRICING:START -->")
        result = text.find("RESULTADO ESPERADO")
        limits = text.find("LÍMITES")
        final_cta = text.find('class="growth-cta-v51"')
        if -1 in (pricing, result, limits, final_cta):
            fail(f"{path.name}: falta una capa primaria que debe permanecer abierta")
        objection_end = text.find("DECISION-COMPRESSION-V531:SOLUTION-OBJECTIONS-END")
        faq_start = text.find('data-decision-compression-v531="solution-faq"')
        if not (objection_end < pricing < result < limits < faq_start < final_cta):
            fail(f"{path.name}: la ruta primaria/ secundaria perdió su jerarquía")
        for marker in ("CRO-V52-OBJECTIONS:START", "CRO-V52-FAQ:START", "CRO-V52-RELATED:START", "growth-proof-page-v51"):
            if marker not in text:
                fail(f"{path.name}: se perdió contenido secundario {marker}")


def main() -> int:
    version = json.loads(VERSION.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 31, 0):
        return 0
    try:
        validate_contract()
        validate_deep()
        validate_solutions()
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"DECISION COMPRESSION V5.31 FAIL: {exc}", file=sys.stderr)
        return 1
    print("DECISION COMPRESSION V5.31 PASS: 16 fichas + 6 rutas, 2 grupos abiertos en fichas y profundidad secundaria accesible por details.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

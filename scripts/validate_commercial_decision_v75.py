#!/usr/bin/env python3
"""Valida Commercial Decision System v7.5 y su frontera con v7.4."""
from __future__ import annotations

from html import escape
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/commercial-decision-system-v75.json"
ATTRIBUTION = ROOT / "assets/data/v7/commercial-evidence-v74.json"
TARGET = ROOT / "index.html"
STYLE = "assets/css/v7/commercial-decision-v75.css"
START = "<!-- COMMERCIAL-DECISION-V75:START -->"
END = "<!-- COMMERCIAL-DECISION-V75:END -->"
EXPECTED = [
    "legal-ai-transformation",
    "contract-control",
    "ai-governance-360",
    "regulatory-control",
    "legal-desk",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str) -> None:
    raise RuntimeError(message)


def managed_block(text: str) -> str:
    if text.count(START) != 1 or text.count(END) != 1:
        fail("v7.5 debe tener un único bloque gestionado en Home")
    match = re.search(re.escape(START) + r".*?" + re.escape(END), text, flags=re.S)
    if not match:
        fail("v7.5 no pudo aislar el bloque gestionado")
    return match.group(0)


def validate_contract(data: dict, attr: dict) -> None:
    lifecycle = data.get("lifecycle")
    version = str(data.get("version", ""))
    if lifecycle not in {"prototype", "release-candidate", "certified"}:
        fail("lifecycle v7.5 inválido")
    if lifecycle == "prototype" and not version.startswith("7.5.0-prototype"):
        fail("prototype v7.5 debe usar versión 7.5.0-prototype*")
    if lifecycle in {"release-candidate", "certified"} and version != "7.5.0":
        fail("candidate/certified v7.5 debe usar versión 7.5.0")
    if data.get("baseline") != "7.4.0":
        fail("baseline v7.5 debe ser 7.4.0")

    rules = data.get("rules", {})
    required_false = ("no_new_pricing", "no_new_capabilities", "no_software_claims", "no_external_analytics", "no_new_javascript")
    for key in required_false:
        if rules.get(key) is not True:
            fail(f"v7.5 debe preservar regla {key}")
    if rules.get("deliverables_per_offer") != 3:
        fail("v7.5 debe limitar la comparación a tres entregables/componentes")

    if attr.get("version") != "7.4.0" or attr.get("lifecycle") != "certified":
        fail("v7.5 requiere v7.4 certified")
    if attr.get("status") != "readiness-disabled":
        fail("v7.5 no puede activar Commercial Evidence")
    activation = attr.get("activation", {})
    if activation.get("external_analytics") is not False or activation.get("provider") != "none":
        fail("v7.5 requiere analytics externo deshabilitado")

    offers = data.get("offers", [])
    ids = [item.get("id") for item in offers]
    if ids != EXPECTED:
        fail(f"v7.5 debe conservar orden exacto de sujetos: {EXPECTED}")
    allowlist = {item["id"]: item["source"] for item in attr.get("subjects", [])}
    for offer in offers:
        if allowlist.get(offer["id"]) != offer.get("source_token"):
            fail(f"{offer['id']}: source_token fuera del allowlist v7.4")
        if not str(offer.get("route", "")).endswith(tuple(["#v7-legal-ai-transformation", "#v7-contract-control", "#v7-ai-governance-360", "#v7-regulatory-control", "#v7-legal-intelligence"])):
            fail(f"{offer['id']}: ruta profunda no declarada")


def validate_sources(data: dict) -> None:
    for offer in data["offers"]:
        path = ROOT / offer["source"]
        if not path.exists():
            fail(f"{offer['id']}: fuente inexistente")
        if offer["id"] == "legal-desk":
            source = load(path)
            items = source.get("home", {}).get("installed", {}).get("items", [])
            matches = [item for item in items if item.get("name") == "Meridiano Legal Desk"]
            if len(matches) != 1:
                fail("legal-desk: fuente v7.1 no es única")
            if len(offer.get("deliverables", [])) != 3:
                fail("legal-desk: comparación debe contener tres componentes")
            continue
        payload = load(path)
        if len(payload) != 1:
            fail(f"{offer['id']}: JSON canónico debe contener una sola oferta")
        catalog_id, source = next(iter(payload.items()))
        if catalog_id != offer.get("catalog_id"):
            fail(f"{offer['id']}: catalog_id no coincide")
        for field in ("modality", "duration", "audience", "question", "result", "deliverables", "limits"):
            if not source.get(field):
                fail(f"{offer['id']}: falta {field} en fuente")
        indices = offer.get("deliverable_indices", [])
        if len(indices) != 3 or len(set(indices)) != 3:
            fail(f"{offer['id']}: deben seleccionarse tres entregables distintos")
        for index in indices:
            if not isinstance(index, int) or not 0 <= index < len(source["deliverables"]):
                fail(f"{offer['id']}: índice de entregable inválido")
        limit_index = offer.get("limit_index")
        if not isinstance(limit_index, int) or not 0 <= limit_index < len(source["limits"]):
            fail(f"{offer['id']}: índice de límite inválido")


def validate_markup(data: dict) -> None:
    text = TARGET.read_text(encoding="utf-8")
    block = managed_block(text)
    if text.count(STYLE) != 1:
        fail("v7.5 stylesheet debe aparecer exactamente una vez")
    if text.find(data["insert_after_marker"]) > text.find(START):
        fail("v7.5 debe insertarse después de Legal Intelligence v7.1")
    evidence = text.find('<section class="v6-section v6-evidence"')
    if evidence < 0 or text.find(END) > evidence:
        fail("v7.5 debe preceder la sección de evidencia v6")
    if block.count('class="v75-decision-offer"') != 5:
        fail("v7.5 debe renderizar cinco ofertas comparables")
    for offer in data["offers"]:
        offer_id = offer["id"]
        token = offer["source_token"]
        if block.count(f'data-v75-offer="{offer_id}"') != 1:
            fail(f"{offer_id}: detalle comparativo faltante o duplicado")
        if f"source={token}" not in block:
            fail(f"{offer_id}: atribución de contacto/ficha ausente")
        if escape(offer["display_name"], quote=True) not in block:
            fail(f"{offer_id}: nombre público ausente")
    forbidden = [
        r"<script\b",
        r"plausible\.io",
        r"google-analytics",
        r"googletagmanager",
        r"localStorage",
        r"sessionStorage",
        r"indexedDB",
        r"\bCOP\b",
        r"\$\s*[0-9]",
    ]
    for pattern in forbidden:
        if re.search(pattern, block, flags=re.I):
            fail(f"v7.5 contiene contenido prohibido en Home: {pattern}")
    if "La ficha completa y la propuesta gobiernan" not in block:
        fail("v7.5 debe preservar la frontera comercial de la comparación")


def validate_idempotence() -> None:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/apply_commercial_decision_v75.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if completed.returncode:
        fail(completed.stderr.strip() or "materializador v7.5 presenta drift")


def main() -> int:
    if not CONTRACT.exists():
        return 0
    data = load(CONTRACT)
    attr = load(ATTRIBUTION)
    validate_contract(data, attr)
    validate_sources(data)
    validate_markup(data)
    validate_idempotence()
    print("COMMERCIAL DECISION V7.5 VALIDATION OK: 5 ofertas, fuente canónica, sin pricing/capabilities/analytics nuevos.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"COMMERCIAL DECISION V7.5 VALIDATION FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Valida v5.9: intake comercial privacy-first y handoff preparado para propuesta."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
RUNTIME = ROOT / "commercial-intake-v59.js"
CONTRACT = ROOT / "commercial-intake-v59.json"


def main() -> int:
    errors: list[str] = []
    required_files = [
        "commercial-intake-v59.json",
        "commercial-intake-v59.js",
        "commercial-intake-v59.css",
        "scripts/apply_commercial_v59.py",
        "scripts/validate_commercial_v59.py",
    ]
    for relative in required_files:
        if not (ROOT / relative).is_file():
            errors.append(f"falta {relative}")
    if errors:
        return fail(errors)

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    privacy = contract.get("privacy", {})
    expected_privacy = {
        "pii_in_telemetry": False,
        "network_transport": False,
        "persistent_storage": False,
        "form_storage": False,
    }
    for key, expected in expected_privacy.items():
        if privacy.get(key) is not expected:
            errors.append(f"commercial-intake-v59.json: privacy.{key} debe ser false")

    index = INDEX.read_text(encoding="utf-8")
    site = SITE_JS.read_text(encoding="utf-8")
    runtime = RUNTIME.read_text(encoding="utf-8")
    css = (ROOT / "commercial-intake-v59.css").read_text(encoding="utf-8")
    apply = (ROOT / "scripts/apply_commercial_v59.py").read_text(encoding="utf-8")
    authority = (ROOT / "scripts/apply_authority_v53.py").read_text(encoding="utf-8")

    required_index = (
        'data-commercial-intake-v59="true"',
        'data-qualification-v59="true"',
        'name="decision_stage" required',
        'name="urgency" required',
        'name="budget"',
        'data-qualification-summary-v59="true"',
        'data-qualification-next-step-v59',
        'commercial-intake-v59.css',
        'commercial-intake-v59.js',
        'La clasificación orienta el proceso comercial.',
    )
    for marker in required_index:
        if marker not in index:
            errors.append(f"index.html: falta {marker!r}")

    if index.count('data-qualification-v59="true"') != 1:
        errors.append("index.html debe contener exactamente un intake v5.9")
    if index.count('commercial-intake-v59.css') != 1:
        errors.append("index.html debe cargar commercial-intake-v59.css exactamente una vez")
    if index.count('commercial-intake-v59.js') != 1:
        errors.append("index.html debe cargar commercial-intake-v59.js exactamente una vez")
    if index.find('decision-v58.css') > index.find('commercial-intake-v59.css'):
        errors.append("commercial-intake-v59.css debe cargar después de decision-v58.css")
    if index.find('commercial-conversion-v44.js') > index.find('commercial-intake-v59.js'):
        errors.append("commercial-intake-v59.js debe cargar después de commercial-conversion-v44.js")

    for field_name, field in contract.get("fields", {}).items():
        if f'name="{field_name}"' not in index:
            errors.append(f"index.html: falta campo {field_name}")
        for option in field.get("options", []):
            if option not in index:
                errors.append(f"index.html: falta opción v5.9 {option!r}")

    for marker in (
        "Etapa de decisión:",
        "Horizonte comercial:",
        "Presupuesto orientativo:",
        "Siguiente paso sugerido:",
        "readiness: cleanContactValue(form.dataset.proposalReadiness, 32)",
    ):
        if marker not in site:
            errors.append(f"site-v3.js: falta {marker!r}")

    prohibited_runtime = (
        "localStorage",
        "sessionStorage",
        "fetch(",
        "XMLHttpRequest",
        "sendBeacon",
        "MeridianoAnalyticsAdapter",
        "document.cookie",
    )
    for marker in prohibited_runtime:
        if marker in runtime:
            errors.append(f"commercial-intake-v59.js no debe usar {marker}")

    for marker in (
        "proposal_ready",
        "scope_first",
        "orientation_first",
        "meridiano:qualification-updated",
        "networkTransport: false",
        "persistentStorage: false",
        "piiInTelemetry: false",
    ):
        if marker not in runtime:
            errors.append(f"commercial-intake-v59.js: falta {marker!r}")

    for pii_marker in ("data.get('name')", "data.get('email')", "data.get('company')", "data.get('message')"):
        if pii_marker in runtime:
            errors.append(f"commercial-intake-v59.js no debe leer PII del formulario: {pii_marker}")

    if "apply_commercial_v59" not in authority:
        errors.append("apply_authority_v53.py debe encadenar apply_commercial_v59")
    if authority.find("apply_decision_v58()") > authority.find("apply_commercial_v59()"):
        errors.append("apply_commercial_v59 debe ejecutarse después de apply_decision_v58")
    if "COMMERCIAL-V59-QUALIFICATION:START" not in apply or "patch_site_js" not in apply:
        errors.append("apply_commercial_v59.py no protege markup + handoff")

    if ".qualification-v59" not in css or "@media(max-width:760px)" not in css:
        errors.append("commercial-intake-v59.css debe incluir layout y adaptación móvil")

    if errors:
        return fail(errors)
    print("COMMERCIAL V5.9 VALIDATION OK: intake estructurado, siguiente paso no numérico, WhatsApp enriquecido y privacidad sin persistencia.")
    return 0


def fail(errors: list[str]) -> int:
    print("VALIDACIÓN COMMERCIAL V5.9 FALLIDA")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

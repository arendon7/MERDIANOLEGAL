#!/usr/bin/env python3
"""Valida v5.10: continuidad de intención, ruta de cierre y telemetría sin PII."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CONTRACT = ROOT / "conversion-close-v510.json"
RUNTIME = ROOT / "conversion-close-v510.js"
TEST = ROOT / "tests/e2e/public-site.spec.mjs"
PRODUCTS = sorted((ROOT / "productos").glob("*.html"))
SERVICES = sorted((ROOT / "servicios").glob("*.html"))


def fail(message: str) -> None:
    raise SystemExit(f"CONVERSION V5.10 FAIL: {message}")


def validate_contract() -> None:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if data.get("version") != "5.10.0":
        fail("conversion-close-v510.json debe declarar 5.10.0")
    privacy = data.get("privacy", {})
    for key in ("pii_in_telemetry", "network_transport", "persistent_storage", "form_storage"):
        if privacy.get(key) is not False:
            fail(f"privacy.{key} debe permanecer en false")
    if privacy.get("handoff") != "whatsapp-user-confirmed":
        fail("el handoff debe seguir requiriendo confirmación del usuario en WhatsApp")
    allowed = set(data.get("telemetry", {}).get("allowed_fields", []))
    if allowed != {"stage", "target", "need"}:
        fail("la telemetría v5.10 solo puede usar stage, target y need")
    events = set(data.get("telemetry", {}).get("events", []))
    expected_events = {"close_intent_applied", "close_route_view", "close_handoff_prepared"}
    if events != expected_events:
        fail("eventos v5.10 incompletos o inesperados")
    if len(data.get("proposal_contents", [])) < 7 or len(data.get("close_path", [])) != 4:
        fail("el contrato debe conservar anatomía de propuesta y ruta de cierre")


def validate_home() -> None:
    text = INDEX.read_text(encoding="utf-8")
    if text.count("<!-- CLOSE-V510:START -->") != 1 or text.count("<!-- CLOSE-V510:END -->") != 1:
        fail("index.html debe contener exactamente un bloque de cierre v5.10")
    if 'data-commercial-close-v510="true"' not in text or 'data-close-path-v510="true"' not in text:
        fail("faltan selectores estables v5.10 en el formulario")
    if text.count('data-close-step-v510=') != 4:
        fail("la ruta comercial v5.10 debe tener exactamente 4 pasos")
    for item in ("Objetivo", "Perímetro", "Entregables", "Cronograma", "Honorarios", "Responsabilidades", "Supuestos y exclusiones"):
        if f">{item}<" not in text:
            fail(f"falta componente de propuesta: {item}")

    v59_end = text.find("<!-- COMMERCIAL-V59-QUALIFICATION:END -->")
    v510_start = text.find("<!-- CLOSE-V510:START -->")
    form_start = text.find('<form class="contact-form"')
    form_end = text.find("</form>", form_start)
    if not (0 <= form_start < v59_end < v510_start < form_end):
        fail("v5.10 debe estar dentro del formulario y después de v5.9")

    style59 = text.find('<link rel="stylesheet" href="commercial-intake-v59.css">')
    style510 = text.find('<link rel="stylesheet" href="conversion-close-v510.css">')
    telemetry = text.find('<script defer src="telemetry-v50.js"></script>')
    runtime510 = text.find('<script defer src="conversion-close-v510.js"></script>')
    if not (0 <= style59 < style510):
        fail("conversion-close-v510.css debe cargarse después de v5.9")
    if not (0 <= telemetry < runtime510):
        fail("runtime v5.10 debe ejecutarse después de la telemetría local")


def validate_runtime() -> None:
    text = RUNTIME.read_text(encoding="utf-8")
    for event in ("close_intent_applied", "close_route_view", "close_handoff_prepared"):
        if event not in text:
            fail(f"runtime sin evento {event}")
    for forbidden_field in ("[name=\"name\"]", "[name=\"email\"]", "[name=\"company\"]", "[name=\"message\"]"):
        if forbidden_field in text:
            fail(f"runtime v5.10 no debe leer PII/texto libre: {forbidden_field}")
    if "MeridianoTelemetry.track" not in text:
        fail("runtime v5.10 debe usar la cola first-party existente")
    if "networkTransport: false" not in text or "persistentStorage: false" not in text or "piiInTelemetry: false" not in text:
        fail("runtime v5.10 debe publicar sus guardrails de privacidad")


def validate_detail(path: Path, intent: str, expected_label: str) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        r'<a class="buying-clarity-cta-v58" data-decision-v58-cta="true" data-close-intent-v510="([^"]+)" href="([^"]+)">([^<]+)</a>',
        text,
    )
    if not match:
        fail(f"{path}: falta CTA v5.10")
    if match.group(1) != intent:
        fail(f"{path}: intención esperada {intent} y encontrada {match.group(1)}")
    if f"commercial_intent={intent}" not in match.group(2) or not match.group(2).endswith("#contacto"):
        fail(f"{path}: el CTA no preserva la intención hasta #contacto")
    if match.group(3).strip() != expected_label:
        fail(f"{path}: etiqueta CTA incorrecta")


def validate_e2e() -> None:
    text = TEST.read_text(encoding="utf-8")
    required = [
        'data-close-intent-v510="proposal"',
        'data-commercial-close-v510',
        'data-close-route-v510',
        "close_intent_applied",
        "close_handoff_prepared",
    ]
    for token in required:
        if token not in text:
            fail(f"E2E no cubre {token}")


def main() -> int:
    for path in (CONTRACT, RUNTIME, ROOT / "conversion-close-v510.css"):
        if not path.exists():
            fail(f"falta {path.name}")
    if len(PRODUCTS) != 8 or len(SERVICES) != 8:
        fail(f"se esperaban 8 productos y 8 servicios; hay {len(PRODUCTS)} y {len(SERVICES)}")
    validate_contract()
    validate_home()
    validate_runtime()
    for path in PRODUCTS:
        validate_detail(path, "proposal", "Solicitar propuesta con este alcance →")
    for path in SERVICES:
        validate_detail(path, "scope", "Definir alcance y propuesta →")
    validate_e2e()
    print("CONVERSION V5.10 OK: 16 CTA conservan intención, ruta de cierre visible y telemetría sin PII.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

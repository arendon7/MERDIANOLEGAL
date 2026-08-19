#!/usr/bin/env python3
"""Valida Commercial Evidence Readiness v7.4 fail-closed.

La release debe seguir sin analytics externo. Solo se permiten sujetos/interacciones
allowlisted, propagación por `source=li-*` y memoria efímera en la pestaña.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets" / "data" / "v7" / "commercial-evidence-v74.json"
RUNTIME = ROOT / "assets" / "js" / "v7" / "commercial-evidence-v74.js"
SITE_CONFIG = ROOT / "site-config.json"
MEASUREMENT = ROOT / "assets" / "data" / "v6" / "measurement-readiness-v61.json"
APPLY = ROOT / "scripts" / "apply_commercial_evidence_v74.py"
START = "<!-- COMMERCIAL-EVIDENCE-V74:START -->"
END = "<!-- COMMERCIAL-EVIDENCE-V74:END -->"
EXPECTED_SUBJECTS = {
    "legal-ai-transformation": "li-legal-ai-transformation",
    "contract-control": "li-contract-control",
    "ai-governance-360": "li-ai-governance-360",
    "regulatory-control": "li-regulatory-control",
    "legal-desk": "li-legal-desk",
}
EXPECTED_INTERACTIONS = {"offer_view", "demo_offer_open", "contact_intent", "handoff_prepared"}
EXPECTED_SURFACES = {
    "index.html",
    "experiencia.html",
    "servicios/legal-operations.html",
    "productos/sistema-contractual-empresarial.html",
    "productos/programa-gobernanza-ia.html",
    "productos/proyecto-regulado-estructurado.html",
    "soluciones/ordenar-operacion-juridica.html",
}
FORBIDDEN_RUNTIME = (
    r"\bfetch\s*\(",
    r"\bXMLHttpRequest\b",
    r"\bsendBeacon\b",
    r"\blocalStorage\b",
    r"\bsessionStorage\b",
    r"\bdocument\.cookie\b",
    r"\bindexedDB\b",
    r"\bWebSocket\b",
    r"\bEventSource\b",
)


def fail(message: str) -> None:
    raise SystemExit("Commercial Evidence v7.4 FAIL: " + message)


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if not str(data.get("version", "")).startswith("7.4.0-prototype"):
        fail("la versión debe permanecer prototype")
    if data.get("status") != "readiness-disabled" or data.get("baseline") != "7.3.0":
        fail("status/baseline inválidos")
    activation = data.get("activation") or {}
    if activation.get("external_analytics") is not False or activation.get("network_transport") is not False:
        fail("analytics/transporte externo deben permanecer deshabilitados")
    if activation.get("provider") != "none" or activation.get("requires_separate_release_decision") is not True:
        fail("la activación futura debe requerir decisión separada")

    subjects = data.get("subjects") or []
    actual_subjects = {item.get("id"): item.get("source") for item in subjects}
    if actual_subjects != EXPECTED_SUBJECTS:
        fail(f"subjects allowlist inesperada: {actual_subjects}")
    if any(not str(source).startswith("li-") for source in actual_subjects.values()):
        fail("todo source comercial debe usar prefijo li-")
    if set(data.get("interactions") or []) != EXPECTED_INTERACTIONS:
        fail("interacciones fuera del allowlist")
    if set(data.get("surfaces") or []) != EXPECTED_SURFACES:
        fail("boundary de superficies inesperado")

    privacy = data.get("privacy") or {}
    required_false = (
        "pii_allowed", "free_text_allowed", "form_content_allowed", "full_url_in_event_allowed",
        "persistent_storage", "cookies", "cross_session_identifier", "fingerprinting",
        "network_transport", "exportable_event_properties",
    )
    if any(privacy.get(key) is not False for key in required_false):
        fail("privacy contract permite un dato/transporte prohibido")
    if privacy.get("max_in_memory_events") != 24:
        fail("el buffer efímero debe permanecer limitado a 24 eventos")

    site = json.loads(SITE_CONFIG.read_text(encoding="utf-8"))
    analytics = site.get("analytics") or {}
    if analytics.get("enabled") is not False or analytics.get("provider") != "none" or analytics.get("site_id") != "":
        fail("site-config no puede activar analytics en readiness v7.4")
    measurement = json.loads(MEASUREMENT.read_text(encoding="utf-8"))
    if (measurement.get("production") or {}).get("analytics_enabled") is not False:
        fail("measurement v6.1 debe permanecer production-disabled")

    runtime = RUNTIME.read_text(encoding="utf-8")
    for pattern in FORBIDDEN_RUNTIME:
        if re.search(pattern, runtime):
            fail(f"runtime contiene capacidad prohibida: {pattern}")
    for subject, source in EXPECTED_SUBJECTS.items():
        if subject not in runtime or source not in runtime:
            fail(f"runtime no contiene mapping cerrado {subject}/{source}")
    for interaction in EXPECTED_INTERACTIONS:
        if interaction not in runtime:
            fail(f"runtime no contiene interacción {interaction}")
    if "new CustomEvent('meridiano:commercial-evidence-v74'" not in runtime:
        fail("falta evento local v7.4")
    if "detail: Object.freeze({ subject, interaction })" not in runtime:
        fail("el detail exportable local debe limitarse a subject + interaction")
    if "externalAnalyticsEnabled: false" not in runtime or "networkTransport: false" not in runtime:
        fail("snapshot runtime no declara límites de transporte")

    for relative in EXPECTED_SURFACES:
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        if text.count(START) != 1 or text.count(END) != 1:
            fail(f"{relative}: bloque v7.4 debe existir exactamente una vez")
        if text.count("commercial-evidence-v74.js") != 1:
            fail(f"{relative}: runtime v7.4 debe cargarse exactamente una vez")

    demo = (ROOT / "experiencia.html").read_text(encoding="utf-8")
    for subject in EXPECTED_SUBJECTS:
        if f'data-li-demo-scenario="{subject}"' not in demo:
            fail(f"Centro Demo no contiene escenario {subject}")

    site_js = (ROOT / "site-v3.js").read_text(encoding="utf-8")
    if "const source = `${current.pathname}${current.search}`;" not in site_js or "`Origen: ${source}`" not in site_js:
        fail("handoff debe conservar origen pathname+search visible en el resumen de WhatsApp")

    if not APPLY.exists():
        fail("falta materializador v7.4")
    print("Commercial Evidence v7.4: PASS (readiness-disabled, allowlist comercial, sin red/PII/persistencia)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

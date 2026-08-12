#!/usr/bin/env python3
"""Valida v5.18: observabilidad del handoff manual sin PII, storage ni inferencias falsas."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
EXPECTED = {
    "handoff_prepared": ("prepared", "whatsapp-draft"),
    "handoff_reopen_requested": ("reopen_requested", "whatsapp"),
    "handoff_copy_succeeded": ("copy_succeeded", "clipboard"),
    "handoff_copy_failed": ("copy_failed", "clipboard"),
    "handoff_edit_requested": ("edit_requested", "contact-form"),
    "handoff_draft_stale": ("draft_stale", "draft"),
}
FORBIDDEN_EVENTS = {
    "handoff_sent",
    "handoff_delivered",
    "handoff_read",
    "proposal_accepted",
    "engagement_started",
    "conversion_completed",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"HANDOFF OBSERVABILITY V5.18 FAIL: {message}")


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def main() -> int:
    version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "")
    require(semver(version) >= (5, 17, 0), "release base debe ser >=5.17.0")

    config = json.loads((ROOT / "site-config.json").read_text(encoding="utf-8"))
    analytics = config.get("analytics") or {}
    require(analytics.get("enabled") is False, "site-config debe mantener analytics.enabled=false")
    require(analytics.get("provider") == "none", "site-config debe mantener analytics.provider=none")
    require(not analytics.get("site_id"), "site-config no debe declarar site_id analítico sin proveedor real")

    contract = json.loads((ROOT / "handoff-observability-v518.json").read_text(encoding="utf-8"))
    require(contract.get("version") == "5.18.0", "contrato debe declarar 5.18.0")
    require(contract.get("scope") == "manual_handoff_observability", "scope canónico incorrecto")
    privacy = contract.get("privacy") or {}
    for key in ("pii_allowed", "network_transport_introduced", "persistent_storage", "cross_session_identifier", "form_content_allowed"):
        require(privacy.get(key) is False, f"privacy.{key} debe ser false")

    events = contract.get("events") or []
    names = [item.get("name") for item in events]
    require(set(names) == set(EXPECTED) and len(names) == len(EXPECTED), "contrato debe declarar exactamente los 6 eventos v5.18")
    signals = []
    for item in events:
        name = item.get("name")
        signal, target = EXPECTED[name]
        require(item.get("signal") == signal, f"{name}: signal incorrecta")
        require(item.get("stage") == "handoff", f"{name}: stage debe ser handoff")
        require(item.get("target") == target, f"{name}: target incorrecto")
        require(len(str(item.get("meaning", ""))) >= 45, f"{name}: meaning insuficiente")
        signals.append(item.get("signal"))
    require(len(signals) == len(set(signals)), "signals v5.18 deben ser únicas")
    require(set(contract.get("forbidden_events") or []) == FORBIDDEN_EVENTS, "lista de eventos prohibidos debe permanecer completa")

    runtime = (ROOT / "handoff-observability-v518.js").read_text(encoding="utf-8")
    for name, (signal, target) in EXPECTED.items():
        require(f"{signal}: Object.freeze({{ name: '{name}', stage: 'handoff', target: '{target}' }})" in runtime,
                f"runtime no mapea {signal}→{name}")
    for marker in (
        "meridiano:handoff-observation-v518",
        "meridiano:handoff-measurement-v518",
        "window.MeridianoTelemetry.track(mapped.name, payload)",
        "version: '5.18.0'",
        "piiAllowed: false",
        "networkTransportIntroduced: false",
        "persistentStorage: false",
        "crossSessionIdentifier: false",
        "formContentAllowed: false",
        "sentKnown: false",
        "deliveredKnown: false",
        "readKnown: false",
        "acceptedKnown: false",
        "engagementStartedKnown: false",
        "conversionKnown: false",
    ):
        require(marker in runtime, f"runtime v5.18 no contiene {marker}")
    for forbidden in (
        "fetch(", "XMLHttpRequest", "sendBeacon", "localStorage", "sessionStorage", "document.cookie",
        "reference", "summary", "company", "email", "phone", "message", "wa.me/",
    ):
        require(forbidden not in runtime, f"runtime v5.18 no debe contener {forbidden!r}")
    for forbidden_event in FORBIDDEN_EVENTS:
        require(forbidden_event not in runtime, f"runtime v5.18 no debe emitir evento falso {forbidden_event}")

    handoff = (ROOT / "handoff-continuity-v517.js").read_text(encoding="utf-8")
    require("meridiano:handoff-observation-v518" in handoff, "v5.17 debe exponer señales internas a v5.18")
    require("detail: Object.freeze({ action:" in handoff, "señal v5.18 debe transportar únicamente action")
    for signal in ("prepared", "reopen_requested", "copy_succeeded", "copy_failed", "edit_requested", "draft_stale"):
        require(f"observe('{signal}')" in handoff, f"handoff v5.17 no emite {signal}")
    require("observe('copy_succeeded')" in handoff.split("try {", 1)[1].split("} catch {", 1)[0],
            "copy_succeeded debe emitirse solo en rama exitosa del portapapeles")
    require("observe('copy_failed')" in handoff.split("} catch {", 1)[1],
            "copy_failed debe emitirse en rama de fallo")

    home = HOME.read_text(encoding="utf-8")
    script = '<script defer src="handoff-observability-v518.js"></script>'
    telemetry = '<script defer src="telemetry-v50.js"></script>'
    require(home.count(script) == 1, "portada debe cargar una sola vez runtime v5.18")
    require(telemetry in home and home.find(telemetry) < home.find(script), "runtime v5.18 debe cargar después de telemetry-v50.js")

    applicator = (ROOT / "scripts/apply_handoff_observability_v518.py").read_text(encoding="utf-8")
    for marker in ("SCRIPT", "ANCHOR", "text.replace(ANCHOR, ANCHOR +", "text.count(SCRIPT) != 1"):
        require(marker in applicator, f"applicator v5.18 no contiene {marker}")

    public_spec = (ROOT / "tests/e2e/public-site.spec.mjs").read_text(encoding="utf-8")
    helpers = (ROOT / "tests/e2e/helpers.mjs").read_text(encoding="utf-8")
    require("formulario prepara WhatsApp sin enviar ni salir de la web" in public_spec,
            "debe preservarse el test histórico de handoff")
    for marker in (
        "MeridianoHandoffObservabilityV518",
        "handoff_prepared",
        "handoff_reopen_requested",
        "handoff_copy_succeeded",
        "handoff_edit_requested",
        "handoff_draft_stale",
        "__meridianoClipboard",
        "telemetryBeforeChange",
        "networkEnabled",
        "provider: 'none'",
    ):
        require(marker in helpers, f"fixture E2E no cubre {marker}")
    for forbidden_event in FORBIDDEN_EVENTS:
        require(forbidden_event not in public_spec and forbidden_event not in helpers,
                f"tests no deben normalizar evento semánticamente falso {forbidden_event}")

    build = (ROOT / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    governance = (ROOT / ".github/workflows/release-governance.yml").read_text(encoding="utf-8")
    for marker in (
        "handoff-observability-v518.json",
        "handoff-observability-v518.js",
        "scripts/apply_handoff_observability_v518.py",
        "scripts/validate_handoff_observability_v518.py",
        "Apply handoff observability v5.18",
    ):
        require(marker in build, f"builder no gobierna {marker}")
    require("python3 scripts/apply_handoff_v517.py\n          python3 scripts/apply_handoff_observability_v518.py\n          git diff --exit-code" in pages,
            "Pages debe terminar idempotencia en v5.18")
    require("Validate handoff observability v5.18" in pages and "node --check handoff-observability-v518.js" in pages,
            "Pages debe validar contrato y sintaxis v5.18")
    require(pages.count("python3 scripts/validate_handoff_observability_v518.py") >= 2,
            "Pages debe validar v5.18 en quality y release-health")
    require("Validate handoff observability v5.18" in governance,
            "Governance debe ejecutar validator v5.18")

    print("HANDOFF OBSERVABILITY V5.18 OK: 6 hechos observables, analítica externa apagada, cero PII/storage/red nueva y cero inferencias de envío/conversión.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

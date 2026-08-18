#!/usr/bin/env python3
"""Valida readiness de medición v6.1 sin activar analítica de terceros."""
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "assets" / "data" / "v6" / "measurement-readiness-v61.json"
ADAPTER_PATH = ROOT / "assets" / "js" / "v6" / "analytics-adapter-v61.js"
ADAPTER_PUBLIC_PATH = "assets/js/v6/analytics-adapter-v61.js"
CONFIG_PATH = ROOT / "site-config.json"
RUNTIME_PATH = ROOT / "runtime-config.js"
PRIVACY_PATH = ROOT / "privacidad.html"
TELEMETRY_PATH = ROOT / "telemetry-v50.js"
BUILD_WORKFLOW = ROOT / ".github" / "workflows" / "build-canonical.yml"
EQUIV_WORKFLOW = ROOT / ".github" / "workflows" / "v6-canonical-equivalence.yml"
READINESS_WORKFLOW = ROOT / ".github" / "workflows" / "v61-measurement-readiness.yml"
PUBLIC_DIRS = ("servicios", "productos", "soluciones", "sectores", "perspectivas")
EXPECTED_STAGES = ["need", "offer", "evidence", "decision", "contact", "handoff"]
EXPECTED_EVENTS = [f"meridiano_funnel_{stage}" for stage in EXPECTED_STAGES]
EXPECTED_WITHOUT_TELEMETRY = {"404.html", "demo.html", "experiencia.html"}
EXPECTED_INSTRUMENTED = 43
errors: list[str] = []


def html_targets() -> list[Path]:
    targets = list(ROOT.glob("*.html"))
    for folder in PUBLIC_DIRS:
        targets.extend((ROOT / folder).glob("*.html"))
    return sorted(set(targets))


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


for path in (
    CONTRACT_PATH, ADAPTER_PATH, CONFIG_PATH, RUNTIME_PATH, PRIVACY_PATH, TELEMETRY_PATH,
    BUILD_WORKFLOW, EQUIV_WORKFLOW, READINESS_WORKFLOW,
):
    require(path.exists() and path.stat().st_size > 20, f"Falta recurso de measurement readiness: {path.as_posix()}")

contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8")) if CONTRACT_PATH.exists() else {}
require(contract.get("version") == "6.1.0", "measurement readiness debe declarar 6.1.0")
require(contract.get("state") == "readiness-disabled", "measurement readiness debe permanecer readiness-disabled")
activation = contract.get("activation", {})
require(activation.get("production_enabled") is False, "measurement readiness no puede activar producción")
require(activation.get("requires_explicit_provider") is True, "activación debe exigir proveedor explícito")
require(activation.get("requires_real_site_id") is True, "activación debe exigir site id real")
require(activation.get("requires_privacy_policy_update_before_enable") is True, "activación debe exigir actualización previa de privacidad")
require(activation.get("requires_provider_metadata_review_before_enable") is True, "activación debe exigir revisión previa de metadata estándar del proveedor")
require(contract.get("external_events") == EXPECTED_EVENTS, "eventos externos v6.1 deben ser seis etapas allowlisted")
require(contract.get("stage_map") == {stage: f"meridiano_funnel_{stage}" for stage in EXPECTED_STAGES}, "stage_map v6.1 no coincide con allowlist")
require(contract.get("source") == {
    "event": "meridiano:funnel-v529",
    "accepted_field": "stage",
    "ignored_fields": ["event", "target"],
    "raw_telemetry_adapter_track": "no-op",
    "deduplication": "first-event-per-stage-per-page-lifetime",
}, "measurement readiness debe consumir solo la etapa saneada del funnel y deduplicarla por página")
privacy_contract = contract.get("privacy", {})
for key in (
    "pii_allowed_in_meridiano_custom_payload",
    "form_content_allowed",
    "handoff_reference_allowed",
    "custom_event_properties_allowed",
    "automatic_pageviews_allowed",
    "persistent_storage_introduced",
    "cross_session_identifier_introduced",
    "fingerprinting_introduced",
    "cookies_introduced_by_meridiano_adapter",
):
    require(privacy_contract.get(key) is False, f"privacy.{key} debe ser false")
require(
    privacy_contract.get("provider_standard_request_metadata_possible_after_activation") is True,
    "El contrato debe reconocer metadata estándar posible del proveedor después de activar",
)
plausible = contract.get("providers", {}).get("plausible", {})
require(plausible.get("status") == "adapter-ready-disabled", "Plausible debe permanecer adapter-ready-disabled")
require(plausible.get("automatic_pageviews") is False, "Plausible debe mantener pageviews automáticos deshabilitados")
require(plausible.get("meridiano_custom_payload") == "event-name-only-no-properties", "Payload custom de Meridiano debe ser event-name-only-no-properties")
require(plausible.get("provider_standard_context") == "subject-to-pre-activation-review-and-policy-update", "Metadata estándar de proveedor debe quedar sujeta a revisión/política previa")

config = json.loads(CONFIG_PATH.read_text(encoding="utf-8")) if CONFIG_PATH.exists() else {}
analytics = config.get("analytics", {})
require(analytics.get("enabled") is False, "site-config.json debe mantener analytics.enabled=false durante readiness")
require(analytics.get("provider") == "none", "site-config.json debe mantener analytics.provider=none durante readiness")
require(str(analytics.get("site_id", "")) == "", "site-config.json no debe contener site_id real durante readiness")

runtime = RUNTIME_PATH.read_text(encoding="utf-8") if RUNTIME_PATH.exists() else ""
require('"analytics":{"enabled":false,"provider":"none","site_id":""}' in runtime, "runtime-config.js debe exponer analytics deshabilitada")

adapter = ADAPTER_PATH.read_text(encoding="utf-8") if ADAPTER_PATH.exists() else ""
for marker in (
    "window.MeridianoAnalyticsAdapter",
    "meridiano_funnel_",
    "invalid-plausible-site-id",
    "unsupported-provider",
    "https://plausible.io/js/",
    "window.addEventListener('meridiano:funnel-v529'",
    "const track = () => false;",
    "state.seenStages.has(stage)",
    "state.seenStages.add(stage)",
    "autoCapturePageviews: false",
    "automaticPageviewsAllowed: false",
    "eventPropertiesAllowed: false",
    "handoffReferenceAllowed: false",
):
    require(marker in adapter, f"analytics-adapter-v61.js: falta {marker!r}")
for forbidden in (
    "fetch(",
    "XMLHttpRequest",
    "sendBeacon",
    "localStorage",
    "sessionStorage",
    "document.cookie",
    "email",
    "company",
    "phone",
    "message",
    "reference",
    "budget",
    "urgency",
    "lead_prepared",
    "solution_view",
    "cta_click",
    "detail?.event",
    "detail?.target",
    "plausible('pageview'",
    'plausible("pageview"',
):
    require(forbidden not in adapter, f"analytics-adapter-v61.js no debe contener ni consumir {forbidden!r}")
require("window.plausible(safeEvent.name)" in adapter, "Plausible debe recibir solo el nombre custom saneado de Meridiano")
require("window.plausible(name)" in adapter, "La cola Plausible debe contener solo nombres custom")

telemetry = TELEMETRY_PATH.read_text(encoding="utf-8") if TELEMETRY_PATH.exists() else ""
require("MeridianoAnalyticsAdapter" in telemetry and "adapter.track(event.name, event)" in telemetry, "telemetry-v50.js debe conservar el punto de extensión histórico, aunque v6.1 lo trate como no-op")

privacy = PRIVACY_PATH.read_text(encoding="utf-8") if PRIVACY_PATH.exists() else ""
for marker in (
    "La analítica de terceros se encuentra actualmente desactivada",
    "No utiliza cookies",
    "ni transmite esos eventos a un proveedor externo",
    "Cualquier activación futura deberá reflejarse previamente en la configuración pública y en esta política",
):
    require(marker in privacy, f"privacidad.html debe conservar la promesa vigente: {marker!r}")

builder = BUILD_WORKFLOW.read_text(encoding="utf-8") if BUILD_WORKFLOW.exists() else ""
equivalence = EQUIV_WORKFLOW.read_text(encoding="utf-8") if EQUIV_WORKFLOW.exists() else ""
readiness_workflow = READINESS_WORKFLOW.read_text(encoding="utf-8") if READINESS_WORKFLOW.exists() else ""
require("- assets/**" in builder, "Build canonical debe seguir reaccionando a cambios en assets/**")
require("- assets/**" in equivalence, "Canonical Equivalence debe seguir reaccionando a cambios en assets/**")
for marker in (
    "assets/js/v6/analytics-adapter-v61.js",
    "assets/data/v6/measurement-readiness-v61.json",
    "scripts/normalize_experience_compat_v60.py",
    "scripts/validate_measurement_readiness_v61.py",
    "tests/e2e/measurement-readiness-v61.spec.mjs",
    "python3 scripts/validate_release_governance_v57.py",
    "python3 scripts/validate_pages_trigger_v511.py",
    "npm run test:e2e",
):
    require(marker in readiness_workflow, f"Gate v6.1 debe preservar cobertura: {marker}")

instrumented_paths: set[str] = set()
without_telemetry_paths: set[str] = set()
for path in html_targets():
    text = path.read_text(encoding="utf-8")
    telemetry_count = text.count("telemetry-v50.js")
    adapter_count = text.count(ADAPTER_PUBLIC_PATH)
    relative = path.relative_to(ROOT).as_posix()
    if telemetry_count:
        require(telemetry_count == 1, f"{relative}: telemetría v5.0 debe ser única")
        require(adapter_count == 1, f"{relative}: adapter v6.1 debe ser único donde existe telemetría")
        if telemetry_count == 1 and adapter_count == 1:
            require(text.find(ADAPTER_PUBLIC_PATH) < text.find("telemetry-v50.js"), f"{relative}: adapter debe cargar antes de telemetría")
        instrumented_paths.add(relative)
    else:
        require(adapter_count == 0, f"{relative}: no debe añadirse adapter sin telemetría previa")
        without_telemetry_paths.add(relative)

require(len(instrumented_paths) == EXPECTED_INSTRUMENTED, f"Measurement v6.1 debe instrumentar exactamente {EXPECTED_INSTRUMENTED} superficies; encontró {len(instrumented_paths)}")
require(without_telemetry_paths == EXPECTED_WITHOUT_TELEMETRY, f"Superficies sin telemetría cambiaron: {sorted(without_telemetry_paths)}")
require(len(instrumented_paths | without_telemetry_paths) == 46, "Measurement v6.1 debe clasificar exactamente las 46 superficies públicas")

node = subprocess.run(["node", "--check", str(ADAPTER_PATH)], capture_output=True, text=True)
require(node.returncode == 0, f"analytics-adapter-v61.js no supera node --check: {node.stderr.strip()}")

if errors:
    print("MEASUREMENT READINESS V6.1 FALLÓ", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(
    "MEASUREMENT READINESS V6.1 OK: "
    f"{len(instrumented_paths)} superficies instrumentadas, {len(without_telemetry_paths)} sin telemetría previa "
    f"({', '.join(sorted(without_telemetry_paths))}), 6 etapas allowlisted desde funnel saneado, "
    "deduplicación por etapa/página, pageviews automáticos deshabilitados, analítica externa deshabilitada, "
    "cero PII/propiedades en el payload custom de Meridiano y topología CI cubierta."
)

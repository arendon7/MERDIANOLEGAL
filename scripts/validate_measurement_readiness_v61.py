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


for path in (CONTRACT_PATH, ADAPTER_PATH, CONFIG_PATH, RUNTIME_PATH, PRIVACY_PATH, TELEMETRY_PATH):
    require(path.exists() and path.stat().st_size > 20, f"Falta recurso de measurement readiness: {path.as_posix()}")

contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8")) if CONTRACT_PATH.exists() else {}
require(contract.get("version") == "6.1.0", "measurement readiness debe declarar 6.1.0")
require(contract.get("state") == "readiness-disabled", "measurement readiness debe permanecer readiness-disabled")
require(contract.get("activation", {}).get("production_enabled") is False, "measurement readiness no puede activar producción")
require(contract.get("external_events") == EXPECTED_EVENTS, "eventos externos v6.1 deben ser seis etapas allowlisted")
require(contract.get("stage_map") == {stage: f"meridiano_funnel_{stage}" for stage in EXPECTED_STAGES}, "stage_map v6.1 no coincide con allowlist")
privacy_contract = contract.get("privacy", {})
for key in (
    "pii_allowed",
    "form_content_allowed",
    "handoff_reference_allowed",
    "event_properties_allowed",
    "persistent_storage_introduced",
    "cross_session_identifier_introduced",
    "fingerprinting_introduced",
    "cookies_introduced_by_meridiano_adapter",
):
    require(privacy_contract.get(key) is False, f"privacy.{key} debe ser false")

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
    "https://plausible.io/js/",
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
):
    require(forbidden not in adapter, f"analytics-adapter-v61.js no debe contener {forbidden!r}")
require("window.plausible(safeEvent.name)" in adapter, "Plausible debe recibir solo el nombre externo saneado")
require("window.plausible(name)" in adapter, "La cola Plausible debe contener solo nombres externos")

telemetry = TELEMETRY_PATH.read_text(encoding="utf-8") if TELEMETRY_PATH.exists() else ""
require("MeridianoAnalyticsAdapter" in telemetry and "adapter.track(event.name, event)" in telemetry, "telemetry-v50.js debe conservar el punto de extensión gobernado")

privacy = PRIVACY_PATH.read_text(encoding="utf-8") if PRIVACY_PATH.exists() else ""
for marker in (
    "La analítica de terceros se encuentra actualmente desactivada",
    "No utiliza cookies",
    "ni transmite esos eventos a un proveedor externo",
    "Cualquier activación futura deberá reflejarse previamente en la configuración pública y en esta política",
):
    require(marker in privacy, f"privacidad.html debe conservar la promesa vigente: {marker!r}")

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
    f"({', '.join(sorted(without_telemetry_paths))}), 6 etapas allowlisted, analítica externa deshabilitada y "
    "cero PII/propiedades/persistencia propias."
)

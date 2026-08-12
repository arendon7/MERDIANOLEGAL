#!/usr/bin/env python3
"""Valida v5.16 fase 1: Lighthouse conserva diagnóstico accesible sin alterar gates."""
from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts/run_quality_v55.mjs"
PAGES = ROOT / ".github/workflows/pages.yml"
GOVERNANCE = ROOT / ".github/workflows/release-governance.yml"
BUILD = ROOT / ".github/workflows/build-canonical.yml"
BASELINE = ROOT / "ci-baseline-v56.json"
BUDGETS = ROOT / "quality-budgets-v55.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"ACCESSIBILITY V5.16 FAIL: {message}")


def main() -> int:
    runner = RUNNER.read_text(encoding="utf-8")
    for marker in (
        "function compactDetail",
        "function accessibilityDiagnostics",
        "lhr.categories?.accessibility?.auditRefs",
        "audit.score < 1",
        "accessibilityAuditGaps",
        "Diagnóstico de accesibilidad Lighthouse",
        "Auditorías con score < 1",
        ".slice(0, 8)",
    ):
        require(marker in runner, f"runner carece de {marker}")

    require("accessibilityAuditGaps," in runner, "summary.json debe persistir gaps de accesibilidad")
    require("budgetsRelaxed: false" in runner, "runner debe conservar budgetsRelaxed=false")
    require("nonRetryableMetrics" in runner and "hasNonRetryableFailure" in runner, "runner debe conservar política de métricas no reintentables")
    require("--only-categories=performance,accessibility" in runner, "runner debe seguir midiendo performance+accessibility")
    require("timeout: 120_000" in runner, "runner debe conservar timeout por auditoría")

    baseline = json.loads(BASELINE.read_text(encoding="utf-8")).get("policy", {})
    require("accessibilityScore" in baseline.get("lighthouseNonRetryableMetrics", []), "accessibilityScore debe seguir siendo no reintentable")
    require(baseline.get("lighthouseVerificationRunsOnFailure") == 2, "política de verificación Lighthouse no debe cambiar")
    require(baseline.get("lighthouseMaxSamplesPerSurface") == 3, "máximo de muestras Lighthouse no debe cambiar")

    budgets = json.loads(BUDGETS.read_text(encoding="utf-8"))
    require(budgets.get("version") == "5.5.0", "contrato de budgets debe seguir en v5.5.0")
    require(budgets.get("budgets", {}).get("accessibilityScoreMin") == 0.9, "v5.16 no debe relajar ni alterar accessibilityScoreMin")
    require(len(budgets.get("surfaces", [])) == 6, "deben conservarse seis superficies Lighthouse")

    build = BUILD.read_text(encoding="utf-8")
    pages = PAGES.read_text(encoding="utf-8")
    governance = GOVERNANCE.read_text(encoding="utf-8")
    require("scripts/validate_accessibility_v516.py" in build, "builder debe gobernar cambios del validator v5.16")
    require("Validate accessibility observability v5.16" in pages, "Pages debe ejecutar validator v5.16")
    require("python3 scripts/validate_accessibility_v516.py" in pages, "Pages no ejecuta validator v5.16")
    require("scripts/validate_accessibility_v516.py" in governance, "Governance debe reaccionar al validator v5.16")
    require("Validate accessibility observability v5.16" in governance, "Governance debe ejecutar validator v5.16")

    require("summary.json" in pages and "summary.md" in pages, "artifact Lighthouse debe conservar resumen JSON/Markdown")
    require("quality-artifacts/v5.5" in pages, "artifact Lighthouse debe conservar ruta canónica")

    print("ACCESSIBILITY V5.16 OK: diagnósticos Lighthouse score<1 persistentes, acotados y sin cambios de budgets/retries/superficies.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

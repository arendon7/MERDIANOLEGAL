#!/usr/bin/env python3
"""Valida eficiencia, paralelismo y observabilidad CI incorporados en v5.6."""
from pathlib import Path
import json
import re

R = Path(__file__).resolve().parents[1]
V = json.loads((R / "version.json").read_text(encoding="utf-8"))


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"VALIDACIÓN CI V5.6 FALLÓ: {message}")


def section(text: str, start: str, end: str) -> str:
    require(start in text, f"falta sección {start.strip()}")
    tail = text.split(start, 1)[1]
    require(end in tail, f"falta delimitador {end.strip()} después de {start.strip()}")
    return tail.split(end, 1)[0]


def main() -> int:
    require(semver(V.get("version", "")) >= (5, 6, 0), "version.json debe ser >= 5.6.0")
    require(V.get("channel") == "github-pages-public-ci-observability-ready", "canal v5.6 incorrecto")

    baseline = json.loads((R / "ci-baseline-v56.json").read_text(encoding="utf-8"))
    require(baseline.get("version") == "5.6.0", "baseline debe declarar 5.6.0")
    base = baseline.get("baseline", {})
    require(base.get("runId") == 31433199058, "run baseline v5.5 inesperado")
    require(base.get("headSha") == "440c09c235c3826c7b0031fd5ac9ddaed9748379", "SHA baseline v5.5 inesperado")
    require(base.get("measurement") == "quality-start-to-snapshot-start", "medición baseline debe ser comparable")
    require(base.get("criticalPathSeconds") == 279, "baseline crítico debe conservar 279 s")
    require(base.get("browserQualityJobSeconds") == 215, "baseline Browser Quality debe conservar 215 s")
    policy = baseline.get("policy", {})
    require(policy.get("coverageReductionAllowed") is False, "v5.6 no puede autorizar reducción de cobertura")
    require(policy.get("budgetRelaxationAllowed") is False, "v5.6 no puede autorizar relajación de budgets")
    require(policy.get("browserBinaryCache") is False, "v5.6 no debe cachear binarios Playwright")
    require(policy.get("qualityJobsParallelAfterSmoke") is True, "gates de calidad deben paralelizarse tras smoke")
    require(policy.get("stableRequiresAllQualityJobs") is True, "stable debe exigir ambos gates")

    budgets = json.loads((R / "quality-budgets-v55.json").read_text(encoding="utf-8"))
    require(budgets.get("version") == "5.5.0", "v5.6 debe preservar el contrato de budgets v5.5")
    require(budgets.get("budgets") == {
        "performanceScoreMin": 0.7,
        "accessibilityScoreMin": 0.9,
        "largestContentfulPaintMsMax": 4000,
        "cumulativeLayoutShiftMax": 0.15,
        "totalBlockingTimeMsMax": 350,
        "totalByteWeightMax": 1500000,
    }, "v5.6 no puede modificar los presupuestos v5.5")
    require(len(budgets.get("surfaces", [])) == 6, "deben conservarse seis superficies Lighthouse")

    config = (R / "playwright.config.mjs").read_text(encoding="utf-8")
    require("['github']" in config, "Playwright CI debe publicar anotaciones GitHub")
    require("./tests/e2e/ci-summary-reporter.mjs" in config, "falta reporter de resumen CI")
    require("workers: process.env.CI ? 1 : undefined" in config, "v5.6 no debe aumentar workers de Playwright")
    for project in ("chromium-desktop", "chromium-mobile", "webkit-desktop", "accessibility-chromium"):
        require(project in config, f"se perdió proyecto Playwright {project}")

    reporter = (R / "tests/e2e/ci-summary-reporter.mjs").read_text(encoding="utf-8")
    for marker in ("GITHUB_STEP_SUMMARY", "Tests observados", "Aprobados", "Omitidos", "Fallidos", "reintento"):
        require(marker in reporter, f"reporter CI no contiene {marker}")

    runner = (R / "scripts/run_quality_v55.mjs").read_text(encoding="utf-8")
    for marker in ("summary.json", "summary.md", "GITHUB_STEP_SUMMARY", "Presupuestos:"):
        require(marker in runner, f"runner Lighthouse no publica {marker}")

    summarizer = (R / "scripts/summarize_ci_v56.py").read_text(encoding="utf-8")
    for marker in ("quality-start-to-snapshot-start", "criticalPathSeconds", "baselineCriticalPathSeconds", "improvementPercent", "coverageReduced", "budgetsRelaxed"):
        require(marker in summarizer, f"summarizer CI no contiene {marker}")

    pages = (R / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    require("Validate CI efficiency and observability v5.6" in pages, "quality job no ejecuta validador v5.6")
    browser = section(pages, "  browser_e2e:\n", "  lighthouse_quality:\n")
    lighthouse = section(pages, "  lighthouse_quality:\n", "  snapshot:\n")
    snapshot = pages.split("  snapshot:\n", 1)[1]

    require("needs: [deploy, live_smoke]" in browser, "Browser E2E debe iniciar después de deploy + smoke")
    require("npx playwright install --with-deps chromium webkit" in browser, "Browser E2E debe instalar Chromium y WebKit fijados")
    require("npm run test:e2e" in browser, "Browser E2E debe ejecutar la suite completa")
    require("npm run audit:quality" not in browser, "Lighthouse no debe serializarse dentro del job E2E")
    require("cache: 'npm'" in browser and "cache-dependency-path: package-lock.json" in browser, "Browser E2E debe reutilizar caché npm segura")

    require("needs: [deploy, live_smoke]" in lighthouse, "Lighthouse debe iniciar en paralelo después de deploy + smoke")
    require("npm run audit:quality" in lighthouse, "job Lighthouse debe ejecutar audit:quality")
    require("command -v google-chrome" in lighthouse, "Lighthouse debe usar Chrome del runner")
    require("npx playwright install" not in lighthouse, "Lighthouse no debe descargar binarios Playwright")
    require("cache: 'npm'" in lighthouse and "cache-dependency-path: package-lock.json" in lighthouse, "Lighthouse debe reutilizar caché npm segura")
    require("quality-artifacts/v5.5/summary.json" in lighthouse and "quality-artifacts/v5.5/summary.md" in lighthouse, "Lighthouse debe publicar resumen compacto")

    require("needs: [browser_e2e, lighthouse_quality]" in snapshot, "stable debe depender de E2E y Lighthouse")
    require("actions: read" in snapshot, "snapshot necesita actions:read para observabilidad")
    require("scripts/summarize_ci_v56.py" in snapshot, "snapshot debe construir resumen CI")
    require("ci-certification-summary-v56" in snapshot, "snapshot debe publicar artefacto de certificación")
    require("Move stable to deployed commit" in snapshot, "snapshot debe conservar promoción de stable")

    require("github.event.workflow_run.head_commit.message" in pages, "workflow_run debe filtrar commits canónicos generados")
    require(pages.count("build: sincroniza sitio público canónico") >= 2, "deben filtrarse commits generados en push y workflow_run")
    require("~/.cache/ms-playwright" not in pages and "actions/cache@" not in pages, "v5.6 no debe cachear binarios Playwright")

    build = (R / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    require("if: ${{ !startsWith(github.event.head_commit.message, 'build') }}" in build, "builder debe omitir commits canónicos generados con condición YAML segura")
    for marker in (
        "ci-baseline-v56.json",
        "tests/e2e/**",
        "scripts/summarize_ci_v56.py",
        "scripts/validate_ci_v56.py",
    ):
        require(marker in build, f"builder no vigila {marker}")

    print("VALIDACIÓN CI V5.6 OK: gates paralelos, Chrome del runner, caché npm, observabilidad y stable dual preservados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

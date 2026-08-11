#!/usr/bin/env python3
"""Valida la infraestructura de performance y accesibilidad incorporada en v5.5 y preservada en releases posteriores."""
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
        raise SystemExit(f"VALIDACIÓN QUALITY V5.5 FALLÓ: {message}")


def main() -> int:
    site_version = semver(V.get("version", ""))
    require(site_version >= (5, 5, 0), "version.json debe ser >= 5.5.0")

    package = json.loads((R / "package.json").read_text(encoding="utf-8"))
    deps = package.get("devDependencies", {})
    package_version = semver(package.get("version", ""))
    require(package_version >= (5, 5, 0), "package.json debe declarar versión QA >= 5.5.0")
    require(package.get("engines", {}).get("node") == ">=22", "Node debe ser >=22")
    require(deps.get("@playwright/test") == "1.62.0", "Playwright debe estar fijado en 1.62.0")
    require(deps.get("@axe-core/playwright") == "4.12.1", "axe Playwright debe estar fijado en 4.12.1")
    require(deps.get("lighthouse") == "13.4.1", "Lighthouse debe estar fijado en 13.4.1")
    require(package.get("scripts", {}).get("audit:quality") == "node scripts/run_quality_v55.mjs", "falta script audit:quality")

    lock = R / "package-lock.json"
    require(lock.exists(), "package-lock.json debe existir")
    lock_data = json.loads(lock.read_text(encoding="utf-8"))
    root_pkg = lock_data.get("packages", {}).get("", {})
    require(root_pkg.get("version") == package.get("version"), "lockfile no está sincronizado con package.json")
    for name, expected in (("@playwright/test", "1.62.0"), ("@axe-core/playwright", "4.12.1"), ("lighthouse", "13.4.1")):
        require(root_pkg.get("devDependencies", {}).get(name) == expected, f"lockfile no fija {name}={expected}")

    config = (R / "playwright.config.mjs").read_text(encoding="utf-8")
    require("accessibility-chromium" in config, "falta proyecto accessibility-chromium")
    require("testIgnore: a11ySpec" in config and "testMatch: a11ySpec" in config, "la suite axe debe ejecutarse una sola vez")

    axe = (R / "tests/e2e/accessibility.spec.mjs").read_text(encoding="utf-8")
    for marker in ("AxeBuilder", "wcag21aa", "serious", "critical", "#ticket-modal", "cliente@empresa-demo.com"):
        require(marker in axe, f"suite axe no contiene {marker}")
    require(axe.count("['") >= 6, "suite axe debe cubrir superficies públicas representativas")

    budgets = json.loads((R / "quality-budgets-v55.json").read_text(encoding="utf-8"))
    require(budgets.get("version") == "5.5.0", "budgets debe conservar contrato 5.5.0")
    require(budgets.get("mode") == "mobile-lab", "Lighthouse debe usar contrato mobile-lab")
    b = budgets.get("budgets", {})
    require(b.get("performanceScoreMin", 0) >= 0.70, "performanceScoreMin no puede ser < 0.70")
    require(b.get("accessibilityScoreMin", 0) >= 0.90, "accessibilityScoreMin no puede ser < 0.90")
    require(b.get("largestContentfulPaintMsMax", 999999) <= 4000, "LCP no puede exceder 4000 ms")
    require(b.get("cumulativeLayoutShiftMax", 999) <= 0.15, "CLS no puede exceder 0.15")
    require(b.get("totalBlockingTimeMsMax", 999999) <= 350, "TBT no puede exceder 350 ms")
    require(b.get("totalByteWeightMax", 999999999) <= 1500000, "transferencia no puede exceder 1.5 MB")
    surfaces = budgets.get("surfaces", [])
    require(len(surfaces) == 6, "deben existir exactamente seis superficies Lighthouse")
    ids = {item.get("id") for item in surfaces}
    require(len(ids) == 6, "ids Lighthouse deben ser únicos")
    required_paths = {
        "",
        "soluciones/gobernar-inteligencia-artificial-empresa.html",
        "productos/programa-gobernanza-ia.html",
        "sectores/tecnologia-software-ia.html",
        "perspectivas/gobierno-juridico-inteligencia-artificial.html",
        "demo.html",
    }
    require({item.get("path") for item in surfaces} == required_paths, "superficies Lighthouse no coinciden con el contrato v5.5")
    for path in required_paths - {""}:
        require((R / path).exists(), f"superficie Lighthouse inexistente: {path}")

    runner = (R / "scripts/run_quality_v55.mjs").read_text(encoding="utf-8")
    for marker in ("largest-contentful-paint", "cumulative-layout-shift", "total-blocking-time", "total-byte-weight", "quality-artifacts"):
        require(marker in runner, f"runner Lighthouse no contiene {marker}")
    require("--only-categories=performance,accessibility" in runner, "Lighthouse debe limitarse a performance/accessibility")
    require("timeout: 120_000" in runner, "cada auditoría Lighthouse debe tener timeout")

    pages = (R / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    for marker in (
        "Validate performance and accessibility QA v5.5",
        "actions/setup-node@v6",
        "node-version: '22'",
        "npm ci --ignore-scripts --no-audit --no-fund",
        "npm run audit:quality",
        "quality-artifacts",
    ):
        require(marker in pages, f"pages.yml no contiene {marker}")
    if site_version >= (5, 6, 0):
        require("lighthouse_quality:" in pages, "v5.6+ debe preservar Lighthouse como gate independiente")
        require("needs: [browser_e2e, lighthouse_quality]" in pages, "stable debe depender de browser_e2e y lighthouse_quality")
    else:
        require("needs: browser_e2e" in pages, "stable debe depender del Browser QA v5.5")
    require("npm install --no-audit --no-fund" not in pages, "Browser QA debe usar npm ci, no npm install")

    build = (R / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    for marker in (
        "quality-budgets-v55.json",
        "tests/e2e/**",
        "scripts/run_quality_v55.mjs",
        "scripts/validate_quality_v55.py",
        "npm install --package-lock-only --ignore-scripts --no-audit --no-fund",
        "package-lock.json",
    ):
        require(marker in build, f"build-canonical no contiene {marker}")

    print("VALIDACIÓN QUALITY V5.5 OK: axe, Lighthouse, budgets, Node 22+, lockfile y gate previo a stable íntegros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

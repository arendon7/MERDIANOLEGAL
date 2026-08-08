#!/usr/bin/env python3
"""Valida la infraestructura Playwright y el gate browser E2E de la release v5.4."""
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
        raise SystemExit(f"VALIDACIÓN BROWSER V5.4 FALLÓ: {message}")


def main() -> int:
    require(semver(V.get("version", "")) >= (5, 4, 0), "version.json debe ser >= 5.4.0")

    package = json.loads((R / "package.json").read_text(encoding="utf-8"))
    require(package.get("private") is True, "package.json debe ser privado")
    require(package.get("devDependencies", {}).get("@playwright/test") == "1.55.0", "Playwright debe estar fijado en 1.55.0")
    require(package.get("scripts", {}).get("test:e2e") == "playwright test", "falta script test:e2e")

    config = (R / "playwright.config.mjs").read_text(encoding="utf-8")
    for marker in ("chromium-desktop", "chromium-mobile", "webkit-desktop", "MERIDIANO_BASE_URL", "retain-on-failure"):
        require(marker in config, f"playwright.config.mjs no contiene {marker}")

    public = (R / "tests/e2e/public-site.spec.mjs").read_text(encoding="utf-8")
    demo = (R / "tests/e2e/demo.spec.mjs").read_text(encoding="utf-8")
    helpers = (R / "tests/e2e/helpers.mjs").read_text(encoding="utf-8")
    for marker in (
        ".need-card",
        "solution_view",
        "faq_open",
        "authority_open",
        "data-contact-v49",
        "573008507813",
        "honeypot bloquea",
        "menú móvil",
    ):
        require(marker in public, f"suite pública no cubre {marker}")
    for marker in ("cliente@empresa-demo.com", ".portal-nav", "#documentos", "Solicitud E2E"):
        require(marker in demo, f"suite demo no cubre {marker}")
    require("pageerror" in helpers and "console.error" in helpers, "helpers debe capturar errores runtime")
    require("scrollWidth" in helpers and "clientWidth" in helpers, "helpers debe controlar overflow horizontal")

    pages = (R / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    require("Validate browser E2E infrastructure v5.4" in pages, "quality no valida infraestructura v5.4")
    require("name: Browser E2E on deployed Pages" in pages, "falta job Browser E2E")
    require("needs: [deploy, live_smoke]" in pages, "Browser E2E debe depender de deploy y smoke HTTP")
    require("timeout 360s npx playwright install --with-deps chromium webkit" in pages, "instalación de navegadores debe tener timeout explícito")
    require("npm run test:e2e" in pages, "job Browser E2E no ejecuta la suite")
    require("needs: browser_e2e" in pages, "stable debe depender del gate Browser E2E")
    require("playwright-report" in pages and "test-results" in pages, "deben conservarse artefactos de fallo")

    build = (R / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    for marker in ("package.json", "playwright.config.mjs", "tests/e2e/**", "scripts/validate_browser_v54.py"):
        require(marker in build, f"build-canonical no vigila {marker}")

    print("VALIDACIÓN BROWSER V5.4 OK: Playwright multi-browser, QA responsive y gate previo a stable configurados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

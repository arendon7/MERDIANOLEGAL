#!/usr/bin/env python3
"""Valida v5.17: continuidad del handoff manual a WhatsApp sin persistencia ni automatismos."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
START = "<!-- HANDOFF-V517:START -->"
END = "<!-- HANDOFF-V517:END -->"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"HANDOFF V5.17 FAIL: {message}")


def public_html() -> list[Path]:
    paths = list(ROOT.glob("*.html"))
    for folder in ("servicios", "productos", "soluciones", "sectores", "perspectivas"):
        paths.extend((ROOT / folder).glob("*.html"))
    return sorted(set(paths))


def contact_pages() -> list[Path]:
    result = []
    for path in public_html():
        text = path.read_text(encoding="utf-8")
        if 'id="contact-form"' in text and 'data-contact-v49="true"' in text:
            result.append(path)
    return result


def main() -> int:
    version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "")
    require(tuple(map(int, version.split("."))) >= (5, 16, 0), "version base debe ser >=5.16.0")

    targets = contact_pages()
    require(targets == [HOME], f"debe existir un único formulario canónico en index.html; detectados {len(targets)}")

    home = HOME.read_text(encoding="utf-8")
    require(home.count(START) == 1 and home.count(END) == 1, "bloque v5.17 de portada no es único")
    require('href="handoff-continuity-v517.css"' in home, "portada no carga CSS v5.17")
    require('src="handoff-continuity-v517.js"' in home, "portada no carga runtime v5.17")
    for marker in (
        'data-handoff-v517="true"',
        'data-handoff-state="idle"',
        'data-handoff-reference-v517',
        'data-handoff-reopen-v517',
        'data-handoff-copy-v517',
        'data-handoff-edit-v517',
        'data-handoff-live-v517',
        'hidden aria-labelledby="handoff-v517-title"',
        'Esta web no recibe confirmación de entrega, lectura, aceptación ni inicio del encargo.',
        'Este formulario público no registra entrega, aceptación contractual ni apertura de expediente.',
    ):
        require(marker in home, f"portada: falta contrato {marker}")
    require(home.count('type="button" data-handoff-') == 3, "deben existir tres acciones manuales type=button")

    deep_pages = sorted((ROOT / "productos").glob("*.html")) + sorted((ROOT / "servicios").glob("*.html"))
    require(len(deep_pages) == 16, f"se esperaban 16 fichas profundas y hay {len(deep_pages)}")
    for path in deep_pages:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        require('id="contact-form"' not in text, f"{rel}: no debe duplicar el formulario canónico")
        links = re.findall(r'href="([^"]*index\.html\?[^"]*#contacto)"', text)
        contextual = [href for href in links if "commercial_intent=" in href and "modality=" in href and "proof_standard=" in href]
        require(contextual, f"{rel}: falta handoff contextual hacia index.html#contacto")

    runtime = (ROOT / "handoff-continuity-v517.js").read_text(encoding="utf-8")
    for marker in (
        "meridiano:handoff-draft-v517",
        "manualSend: true",
        "automaticClipboard: false",
        "staleDraftProtection: true",
        "persistentStorage: false",
        "piiInTelemetry: false",
        "piiInDomSummary: false",
        "panel.dataset.handoffState = 'changed'",
        "setButtonsDisabled(true)",
        "navigator.clipboard.writeText(draft.summary)",
        "window.open(draft.url",
        "Esta web estática no recibe confirmación de entrega, lectura, aceptación ni inicio del encargo.",
    ):
        require(marker in runtime, f"runtime v5.17 no contiene {marker}")
    for forbidden in ("localStorage", "sessionStorage", "fetch(", "XMLHttpRequest", "sendBeacon", "dataset.handoffSummary", "dataset.handoffUrl"):
        require(forbidden not in runtime, f"runtime v5.17 no debe contener {forbidden}")

    css = (ROOT / "handoff-continuity-v517.css").read_text(encoding="utf-8")
    for marker in ("min-height:44px", "[data-handoff-state=\"changed\"]", "@media(max-width:760px)", ".handoff-actions-v517 button:disabled"):
        require(marker in css, f"CSS v5.17 no contiene {marker}")

    site = (ROOT / "site-v3.js").read_text(encoding="utf-8")
    require("meridiano:handoff-draft-v517" in site, "site-v3.js no entrega borrador efímero a v5.17")
    require("detail: { reference, summary, url }" in site, "evento v5.17 debe usar solo memoria efímera")
    require("navigator.clipboard?.writeText(summary)" not in site, "la copia automática histórica debe estar eliminada")
    require("meridiano:lead-prepared" in site, "se debe conservar lead-prepared histórico")
    require("window.open(url, '_blank', 'noopener,noreferrer')" in site, "se debe conservar apertura manual de WhatsApp")
    require("La solicitud solo queda enviada cuando confirme el envío allí." in site, "se debe conservar aclaración de envío manual")

    applicator = (ROOT / "scripts/apply_handoff_v517.py").read_text(encoding="utf-8")
    for marker in ("contact_pages()", "patch_home()", "patch_site_runtime()", "AUTO_CLIPBOARD", "DRAFT_EVENT", "targets != [HOME]"):
        require(marker in applicator, f"applicator v5.17 no contiene {marker}")

    helpers = (ROOT / "tests/e2e/helpers.mjs").read_text(encoding="utf-8")
    for marker in (
        "__meridianoHandoffGuardV517",
        "meridiano:handoff-draft-v517",
        "handoff.references).toHaveLength(1)",
        "handoff.panelText).not.toContain(value)",
        "data-handoff-state', 'changed",
        "data-handoff-reopen-v517",
        "data-handoff-copy-v517",
    ):
        require(marker in helpers, f"cobertura E2E v5.17 no contiene {marker}")

    public_spec = (ROOT / "tests/e2e/public-site.spec.mjs").read_text(encoding="utf-8")
    require("formulario prepara WhatsApp sin enviar ni salir de la web" in public_spec, "debe conservarse el test histórico de handoff")
    require("window.__meridianoOpenedUrls" in public_spec, "test histórico debe seguir verificando la apertura de WhatsApp")

    build = (ROOT / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    for marker in (
        "handoff-continuity-v517.css",
        "handoff-continuity-v517.js",
        "scripts/apply_handoff_v517.py",
        "scripts/validate_handoff_v517.py",
        "Apply manual handoff continuity v5.17",
    ):
        require(marker in build, f"builder no gobierna {marker}")

    print("HANDOFF V5.17 OK: 1 formulario canónico + 16 rutas profundas, borrador efímero, stale protection y cobertura E2E sin nueva entrada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Valida v5.17: continuidad del handoff manual a WhatsApp sin persistencia ni automatismos."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
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
    return [
        path for path in public_html()
        if 'id="contact-form"' in path.read_text(encoding="utf-8")
        and 'data-contact-v49="true"' in path.read_text(encoding="utf-8")
    ]


def prefix_for(path: Path) -> str:
    return "" if path.parent == ROOT else "../"


def main() -> int:
    version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "")
    require(tuple(map(int, version.split("."))) >= (5, 16, 0), "version base debe ser >=5.16.0")

    targets = contact_pages()
    require(len(targets) >= 17, f"se esperaban al menos 17 contact-form; hay {len(targets)}")
    required = {ROOT / "index.html"}
    required.update((ROOT / "productos").glob("*.html"))
    required.update((ROOT / "servicios").glob("*.html"))
    require(required.issubset(set(targets)), "portada + 16 fichas profundas deben conservar contact-form")

    for path in targets:
        text = path.read_text(encoding="utf-8")
        prefix = prefix_for(path)
        rel = path.relative_to(ROOT)
        require(text.count(START) == 1 and text.count(END) == 1, f"{rel}: bloque v5.17 no es único")
        require(f'href="{prefix}handoff-continuity-v517.css"' in text, f"{rel}: falta CSS v5.17")
        require(f'src="{prefix}handoff-continuity-v517.js"' in text, f"{rel}: falta runtime v5.17")
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
            require(marker in text, f"{rel}: falta contrato {marker}")
        require(text.count('type="button" data-handoff-') == 3, f"{rel}: deben existir tres acciones manuales type=button")

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
    for marker in ("contact_pages()", "patch_site_runtime()", "AUTO_CLIPBOARD", "DRAFT_EVENT", "len(targets) < 17"):
        require(marker in applicator, f"applicator v5.17 no contiene {marker}")

    print(f"HANDOFF V5.17 OK: {len(targets)} formularios con continuidad manual, borrador efímero, protección stale y sin copia automática/persistencia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

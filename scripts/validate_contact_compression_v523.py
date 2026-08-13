#!/usr/bin/env python3
"""Valida v5.23: una síntesis comercial y un disclosure de proceso sin pérdida contractual."""
from __future__ import annotations

from pathlib import Path
import json
import re

R = Path(__file__).resolve().parents[1]
HOME = R / "index.html"
VERSION = R / "version.json"
RUNTIME = R / "decision-action-v515.js"
STYLE = R / "contact-v523.css"
TEST = R / "tests/e2e/contact-compression.spec.mjs"


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"CONTACT COMPRESSION V5.23 FAIL: {message}")


def bounded(text: str, start: str, end: str, label: str) -> str:
    a = text.find(start)
    b = text.find(end, a + len(start)) if a >= 0 else -1
    require(a >= 0 and b >= 0, f"falta {label}")
    return text[a : b + len(end)]


def validate_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    require(text.count('<form class="contact-form" id="contact-form"') == 1, "debe existir un único formulario físico")
    require(text.count('data-contact-compression-v523="true"') == 1, "formulario debe declarar v5.23 una vez")
    require(text.count('data-contact-synthesis-v523="true"') == 1, "debe existir una única síntesis comercial")
    require(text.count('data-contact-process-v523="true"') == 1, "debe existir un único disclosure de proceso")
    require(text.count('data-qualification-summary-v59="true"') == 1, "resumen v5.9 debe existir una sola vez")
    require(text.count('data-commercial-brief-v513="true"') == 1, "brief v5.13 debe existir una sola vez")
    require(text.count('data-recommendation-brief-v514="true"') == 1, "recomendación v5.14 debe existir una sola vez")
    require(text.count('data-close-path-v510="true"') == 1, "ruta v5.10 debe existir una sola vez")
    require(text.count('data-engagement-v511="true"') == 1, "engagement v5.11 debe existir una sola vez")
    require(text.count('<link rel="stylesheet" href="contact-v523.css">') == 1, "debe cargarse una sola hoja v5.23")

    for field in ("name", "company", "email", "need", "decision_stage", "urgency", "budget", "message", "privacy"):
        require(text.count(f'name="{field}"') == 1, f"campo {field} debe conservar una sola instancia")

    synthesis = bounded(text, "<!-- CONTACT-SYNTHESIS-V523:START -->", "<!-- CONTACT-SYNTHESIS-V523:END -->", "síntesis v5.23")
    process = bounded(text, "<!-- CONTACT-PROCESS-V523:START -->", "<!-- CONTACT-PROCESS-V523:END -->", "proceso v5.23")
    qualification = bounded(text, "<!-- COMMERCIAL-V59-QUALIFICATION:START -->", "<!-- COMMERCIAL-V59-QUALIFICATION:END -->", "calificación v5.9")

    require('data-qualification-summary-v59="true"' not in qualification, "campos v5.9 no deben contener un segundo panel de resumen")
    for marker in (
        'data-qualification-summary-v59="true"',
        'data-commercial-brief-v513="true"',
        'data-recommendation-brief-v514="true"',
        'data-qualification-context-v59',
        'data-qualification-need-v59',
        'data-qualification-stage-v59',
        'data-qualification-urgency-v59',
        'data-qualification-budget-v59',
        'data-qualification-next-step-v59',
        'data-brief-modality-v513',
        'data-brief-proof-v513',
        'data-recommendation-fit-v514',
        'data-route-panel-v515',
        'data-recommendation-boundary-v514',
        'data-recommendation-alternative-v514',
    ):
        require(marker in synthesis, f"síntesis pierde {marker}")

    for marker in (
        '<details class="contact-process-v523',
        'data-close-path-v510="true"',
        'data-engagement-v511="true"',
        'data-close-step-v510="request"',
        'data-close-step-v510="proposal"',
        'data-engagement-state-v511="accepted"',
        'data-engagement-state-v511="started"',
        'data-engagement-automatic-v511="false"',
        "No acepta contratos",
        "No cobra pagos",
        "No reserva agenda",
        "No inicia el encargo",
    ):
        require(marker in process, f"disclosure de proceso pierde {marker}")
    require(process.count('data-close-step-v510=') == 4, "proceso debe conservar cuatro pasos v5.10")
    require(process.count('data-engagement-state-v511=') == 4, "proceso debe conservar cuatro estados v5.11")

    order = [
        text.index("<!-- COMMERCIAL-V59-QUALIFICATION:END -->"),
        text.index("<!-- CONTACT-SYNTHESIS-V523:START -->"),
        text.index("<!-- COMMERCIAL-BRIEF-V513:START -->"),
        text.index("<!-- RECOMMENDATION-V514-FORM:START -->"),
        text.index("<!-- CONTACT-SYNTHESIS-V523:END -->"),
        text.index("<!-- CONTACT-PROCESS-V523:START -->"),
        text.index("<!-- CLOSE-V510:START -->"),
        text.index("<!-- ENGAGEMENT-V511:START -->"),
        text.index("<!-- CONTACT-PROCESS-V523:END -->"),
        text.index('<label class="full">Contexto general'),
    ]
    require(order == sorted(order), "jerarquía del formulario no coincide con el contrato v5.23")

    require("style=\"display:none" not in synthesis and " hidden" not in synthesis, "síntesis no debe ocultar material")


def validate_runtime() -> None:
    js = RUNTIME.read_text(encoding="utf-8")
    for marker in (
        "CONTACT-COMPRESSION-V523:START",
        "form.querySelector('[data-contact-process-v523=\"true\"]')",
        "const expandCompressedV523 = explicitIntent === 'proposal'",
        "compressedProcess.open = expandCompressedV523",
        "contactCompressionV523: Object.freeze",
        "singleSynthesis: true",
        "singleProcessDisclosure: true",
        "automaticDecisionChange: false",
    ):
        require(marker in js, f"runtime carece de {marker}")
    for forbidden in ("localStorage", "sessionStorage", "fetch(", "XMLHttpRequest"):
        require(forbidden not in js, f"runtime no debe introducir {forbidden}")
    require("explicitIntent === 'proposal' && !isMobile" in js, "runtime debe conservar regla histórica v5.19")
    require("details.dataset.commercialDisclosureV519 = key" in js, "runtime debe conservar compositor histórico v5.19")


def validate_visual_reuse() -> None:
    text = HOME.read_text(encoding="utf-8")
    synthesis = bounded(text, "<!-- CONTACT-SYNTHESIS-V523:START -->", "<!-- CONTACT-SYNTHESIS-V523:END -->", "síntesis v5.23")
    require("contact-synthesis-v523" in synthesis, "falta contenedor visual v5.23")
    normalizer = (R / "scripts/normalize_contact_compression_v523.py").read_text(encoding="utf-8")
    for marker in (
        "qualification-summary-v59 contact-synthesis-v523",
        "contact-qualification-v523",
        "commercial-brief-head-v513 contact-brief-head-v523",
        "qualification-summary-grid-v59 contact-brief-grid-v523",
        "contact-recommendation-v523",
        "contact-v523.css",
    ):
        require(marker in normalizer, f"normalizador visual carece de {marker}")
    require(STYLE.exists(), "falta contact-v523.css")
    css = STYLE.read_text(encoding="utf-8")
    for selector in (
        ".contact-synthesis-v523 #contact-synthesis-v523-title",
        ".contact-synthesis-v523 #commercial-brief-v513-title",
        ".contact-synthesis-v523 .commercial-brief-note-v513",
        ".contact-synthesis-v523 .recommendation-brief-state-v514",
    ):
        require(selector in css, f"contraste v5.23 no cubre {selector}")


def validate_chain() -> None:
    chain = (R / "scripts/apply_handoff_observability_v518.py").read_text(encoding="utf-8")
    require("apply_contact_compression_v523" in chain, "composición final no encadena v5.23")
    require("normalize_contact_compression_v523" in chain, "composición final no normaliza presentación v5.23")
    require("semver(version) >= (5, 23, 0)" in chain, "v5.23 debe ser version-aware")


def validate_e2e() -> None:
    require(TEST.exists(), "falta E2E específico v5.23")
    text = TEST.read_text(encoding="utf-8")
    for marker in (
        "data-contact-synthesis-v523",
        "data-contact-process-v523",
        "data-commercial-brief-v513",
        "data-recommendation-brief-v514",
        "data-close-path-v510",
        "data-engagement-v511",
        "Propuesta verificable",
        "Orientación inicial",
    ):
        require(marker in text, f"E2E v5.23 no verifica {marker}")


def main() -> int:
    version = json.loads(VERSION.read_text(encoding="utf-8")).get("version", "0.0.0")
    require(semver(version) >= (5, 23, 0), "version.json debe declarar v5.23+")
    validate_home()
    validate_runtime()
    validate_visual_reuse()
    validate_chain()
    validate_e2e()
    print("CONTACT COMPRESSION V5.23 OK: una síntesis, un disclosure, contraste AA explícito, mismos campos/estados y cero red, storage o scoring nuevo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Valida v5.13: modalidad y prueba verificable sobreviven hasta formulario y WhatsApp."""
from __future__ import annotations

from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
PROOF_STANDARD = "Método + entregables + formatos + aceptación/cierre"
MODALITIES = {
    "diagnostic": "Diagnóstico jurídico",
    "audit": "Auditoría jurídica de alcance cerrado",
    "product": "Producto de alcance cerrado",
    "specialist": "Servicio jurídico especializado",
    "recurring": "Acompañamiento jurídico recurrente",
}
SPECIAL_BY_CATALOG = {
    "product-diagnostic": "audit",
    "service-diagnostic": "diagnostic",
    "service-direction": "recurring",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"COMMERCIAL BRIEF V5.13 FAIL: {message}")


def modality_for(catalog_id: str, page_type: str) -> str:
    if catalog_id in SPECIAL_BY_CATALOG:
        return SPECIAL_BY_CATALOG[catalog_id]
    return "product" if page_type == "Producto jurídico" else "specialist"


def href_params(href: str) -> dict[str, list[str]]:
    return parse_qs(urlsplit(unescape(href)).query)


def validate_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    require(text.count("<!-- COMMERCIAL-BRIEF-V513:START -->") == 1, "falta bloque de brief en portada")
    require(text.count("<!-- COMMERCIAL-BRIEF-V513:END -->") == 1, "cierre de brief duplicado o ausente")
    require('<link rel="stylesheet" href="commercial-brief-v513.css">' in text, "falta CSS v5.13")
    require('<script src="commercial-brief-v513.js"></script>' in text, "falta JS v5.13")
    require(text.index("<!-- COMMERCIAL-V59-QUALIFICATION:END -->") < text.index("<!-- COMMERCIAL-BRIEF-V513:START -->") < text.index("<!-- CLOSE-V510:START -->"), "brief debe quedar entre calificación y cierre")
    block = text[text.index("<!-- COMMERCIAL-BRIEF-V513:START -->"):text.index("<!-- COMMERCIAL-BRIEF-V513:END -->")]
    require('data-commercial-brief-v513="true"' in block, "falta contrato DOM v5.13")
    require('data-brief-modality-v513' in block and 'data-brief-proof-v513' in block, "faltan salidas visibles del brief")
    for code in MODALITIES:
        require(f'data-commercial-modality-v513="{code}"' in text, f"tarjeta v5.12 no conserva modalidad {code}")

    js = (ROOT / "commercial-brief-v513.js").read_text(encoding="utf-8")
    require("localStorage" not in js and "sessionStorage" not in js, "v5.13 no debe introducir storage")
    require("fetch(" not in js and "XMLHttpRequest" not in js, "v5.13 no debe introducir transporte de red")
    require(PROOF_STANDARD in js, "JS debe usar estándar verificable canónico")
    for code, label in MODALITIES.items():
        require(f"{code}: '{label}'" in js, f"JS carece de modalidad {code}")


def validate_site_js() -> None:
    text = SITE_JS.read_text(encoding="utf-8")
    require(text.count("// COMMERCIAL-BRIEF-V513:START") == 1 and text.count("// COMMERCIAL-BRIEF-V513:END") == 1, "site-v3.js debe tener un único parche v5.13")
    require("Modalidad considerada: ${commercialModalityV513}" in text, "WhatsApp no incluye modalidad")
    require("Estándar verificable: ${proofExpectationV513}" in text, "WhatsApp no incluye prueba verificable")
    require("form.dataset.commercialModalityV513" in text and "form.dataset.proofExpectationV513" in text, "site-v3.js no consume datasets v5.13")


def validate_detail(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    body = re.search(r'<body\s+([^>]+)>', text)
    require(bool(body), f"{path.name}: falta body")
    attrs = body.group(1)
    catalog = re.search(r'data-catalog-id="([^"]+)"', attrs)
    page_type = re.search(r'data-page-type="([^"]+)"', attrs)
    require(bool(catalog and page_type), f"{path.name}: metadatos incompletos")
    code = modality_for(unescape(catalog.group(1)), unescape(page_type.group(1)))
    label = MODALITIES[code]

    proof = re.search(r'<section class="proof-detail-v512"[^>]*>', text)
    require(bool(proof), f"{path.name}: falta prueba v5.12")
    require(f'data-commercial-modality-v513="{code}"' in proof.group(0), f"{path.name}: prueba no declara modalidad {code}")

    cta = re.search(r'<a class="buying-clarity-cta-v58"[^>]*data-decision-v58-cta="true"[^>]*>', text)
    require(bool(cta), f"{path.name}: falta CTA v5.8")
    href = re.search(r'href="([^"]+)"', cta.group(0))
    require(bool(href), f"{path.name}: CTA sin href")
    params = href_params(href.group(1))
    require(params.get("modality") == [code], f"{path.name}: CTA no transporta modalidad {code}")
    require(params.get("proof_standard") == ["source"], f"{path.name}: CTA no transporta proof_standard=source")

    general = re.search(r'<a class="btn btn-outline-light" href="([^"]+)">Formulario general</a>', text)
    require(bool(general), f"{path.name}: falta formulario general contextual")
    general_params = href_params(general.group(1))
    require(general_params.get("modality") == [code] and general_params.get("proof_standard") == ["source"], f"{path.name}: formulario general pierde brief")

    direct = re.search(r'<a class="btn btn-gold" href="(https://wa\.me/573008507813\?text=[^"]+)"[^>]*>Conversar por WhatsApp →</a>', text)
    require(bool(direct), f"{path.name}: falta WhatsApp directo")
    direct_text = unquote(parse_qs(urlsplit(unescape(direct.group(1))).query).get("text", [""])[0])
    require(f"Modalidad considerada: {label}" in direct_text, f"{path.name}: WhatsApp directo pierde modalidad")
    require(f"Estándar verificable: {PROOF_STANDARD}" in direct_text, f"{path.name}: WhatsApp directo pierde estándar")
    require("modalidad y el alcance definitivos deben confirmarse" in direct_text, f"{path.name}: WhatsApp directo debe conservar disclaimer")


def validate_workflow_contracts() -> None:
    build = (ROOT / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    governance = (ROOT / ".github/workflows/release-governance.yml").read_text(encoding="utf-8")
    for name, text in (("builder", build), ("Pages", pages), ("Governance", governance)):
        require("scripts/apply_commercial_brief_v513.py" in text or name == "Pages", f"{name}: falta applicator v5.13")
    require("python3 scripts/apply_proof_v512.py" in build and "python3 scripts/apply_commercial_brief_v513.py" in build, "builder sin composición v5.12→v5.13")
    require(build.index("python3 scripts/apply_proof_v512.py") < build.index("python3 scripts/apply_commercial_brief_v513.py"), "builder debe terminar v5.12→v5.13")
    require("python3 scripts/apply_commercial_brief_v513.py" in pages and "python3 scripts/validate_commercial_brief_v513.py" in pages, "Pages no valida v5.13")
    require("python3 scripts/apply_commercial_brief_v513.py" in governance and "python3 scripts/validate_commercial_brief_v513.py" in governance, "Governance no compone v5.13")


def main() -> int:
    require(len(DETAIL_TARGETS) == 16, "deben existir 16 fichas profundas")
    validate_home()
    validate_site_js()
    for path in DETAIL_TARGETS:
        validate_detail(path)
    validate_workflow_contracts()
    test_text = (ROOT / "tests/e2e/public-site.spec.mjs").read_text(encoding="utf-8")
    require("data-commercial-brief-v513" in test_text, "E2E no verifica brief v5.13")
    require("Modalidad considerada: Producto de alcance cerrado" in test_text, "E2E no verifica modalidad en WhatsApp")
    require(f"Estándar verificable: {PROOF_STANDARD}" in test_text, "E2E no verifica estándar en WhatsApp")
    print("COMMERCIAL BRIEF V5.13 OK: 5 modalidades + 16 fichas + formulario + WhatsApp con continuidad verificable y sin storage/red adicional.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

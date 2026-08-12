#!/usr/bin/env python3
"""Valida v5.14: recomendación explicable sin scoring, storage ni backend."""
from __future__ import annotations

from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
CONTRACT = ROOT / "recommendation-v514.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
CODES = ("diagnostic", "audit", "product", "specialist", "recurring")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"RECOMMENDATION V5.14 FAIL: {message}")


def load_contract() -> dict:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    require(data.get("version") == "5.14.0", "versión contractual incorrecta")
    require(data.get("scoring") is False, "scoring debe permanecer desactivado")
    modalities = data.get("modalities") or {}
    require(tuple(modalities.keys()) == CODES, "deben existir cinco modalidades en orden canónico")
    for code, rule in modalities.items():
        for field in ("label", "fit", "boundary", "alternative", "href", "cta"):
            require(isinstance(rule.get(field), str) and rule[field].strip(), f"{code}: falta {field}")
        require(len(rule["fit"]) >= 70, f"{code}: explicación de encaje demasiado superficial")
        require(len(rule["boundary"]) >= 70, f"{code}: límite demasiado superficial")
        require(len(rule["alternative"]) >= 80, f"{code}: alternativa demasiado superficial")
    return data


def validate_home(contract: dict) -> None:
    text = HOME.read_text(encoding="utf-8")
    require(text.count("<!-- RECOMMENDATION-V514-HOME:START -->") == 1 and text.count("<!-- RECOMMENDATION-V514-HOME:END -->") == 1, "bloque home v5.14 inválido")
    require(text.count("<!-- RECOMMENDATION-V514-FORM:START -->") == 1 and text.count("<!-- RECOMMENDATION-V514-FORM:END -->") == 1, "bloque form v5.14 inválido")
    require('<link rel="stylesheet" href="recommendation-v514.css">' in text, "falta CSS v5.14")
    require('<script src="recommendation-v514.js"></script>' in text, "falta JS v5.14")
    require(text.index("<!-- PROOF-V512-HOME:END -->") < text.index("<!-- RECOMMENDATION-V514-HOME:START -->"), "v5.14 home debe seguir a prueba v5.12")
    require(text.index("<!-- COMMERCIAL-BRIEF-V513:END -->") < text.index("<!-- RECOMMENDATION-V514-FORM:START -->") < text.index("<!-- CLOSE-V510:START -->"), "v5.14 form debe seguir al brief v5.13")
    require(text.count('data-recommendation-model-v514=') == 5, "deben existir cinco tarjetas explicables")
    for code, rule in contract["modalities"].items():
        require(f'data-recommendation-model-v514="{code}"' in text, f"falta tarjeta {code}")
        require(rule["fit"] in text and rule["boundary"] in text and rule["alternative"] in text, f"home no refleja contrato {code}")
    require('id="recommendation-contract-v514"' in text, "falta contrato JSON embebido")
    require('data-recommendation-brief-v514="true"' in text, "falta brief explicable")
    for attr in ("data-recommendation-fit-v514", "data-recommendation-boundary-v514", "data-recommendation-alternative-v514", "data-recommendation-state-v514"):
        require(attr in text, f"falta salida {attr}")
    lower_block = text[text.index("<!-- RECOMMENDATION-V514-HOME:START -->"):text.index("<!-- RECOMMENDATION-V514-HOME:END -->")].lower()
    require("puntaje" in lower_block and "no asigna puntajes" in lower_block, "debe explicitar ausencia de scoring")


def validate_js(contract: dict) -> None:
    js = (ROOT / "recommendation-v514.js").read_text(encoding="utf-8")
    require("recommendation-contract-v514" in js and "JSON.parse" in js, "JS debe consumir contrato embebido")
    require("localStorage" not in js and "sessionStorage" not in js, "v5.14 no debe persistir datos")
    require("fetch(" not in js and "XMLHttpRequest" not in js, "v5.14 no debe introducir red")
    require("scoring: false" in js and "scoreUsed: false" in js, "JS debe declarar ausencia de scoring")
    require("data.recommendation" not in js.lower(), "no debe inventar API externa de recomendación")

    site = SITE_JS.read_text(encoding="utf-8")
    require(site.count("// RECOMMENDATION-V514:START") == 1 and site.count("// RECOMMENDATION-V514:END") == 1, "site-v3.js debe tener parche v5.14 único")
    for phrase in ("Por qué encaja la modalidad:", "Límite de la modalidad:", "Alternativa si cambia el alcance:"):
        require(phrase in site, f"WhatsApp preparado no incluye {phrase}")
    require("form.dataset.recommendationFitV514" in site, "site-v3.js no consume recomendación")


def whatsapp_text(href: str) -> str:
    query = parse_qs(urlsplit(unescape(href)).query)
    return unquote(query.get("text", [""])[0])


def validate_details(contract: dict) -> None:
    seen = {code: 0 for code in CODES}
    for path in DETAIL_TARGETS:
        text = path.read_text(encoding="utf-8")
        match = re.search(r'<section class="proof-detail-v512"[^>]*data-commercial-modality-v513="([^"]+)"[^>]*>', text)
        require(bool(match), f"{path.name}: falta modalidad heredada v5.13")
        code = match.group(1)
        require(code in contract["modalities"], f"{path.name}: modalidad desconocida {code}")
        seen[code] += 1
        rule = contract["modalities"][code]
        direct = re.search(r'<a class="btn btn-gold" href="(https://wa\.me/573008507813\?text=[^"]+)"[^>]*>Conversar por WhatsApp →</a>', text)
        require(bool(direct), f"{path.name}: falta WhatsApp directo")
        message = whatsapp_text(direct.group(1))
        require(f"Modalidad considerada: {rule['label']}" in message, f"{path.name}: modalidad no llega a WhatsApp")
        require(f"Por qué encaja la modalidad: {rule['fit']}" in message, f"{path.name}: encaje no llega a WhatsApp")
        require(f"Límite de la modalidad: {rule['boundary']}" in message, f"{path.name}: límite no llega a WhatsApp")
        require(f"Alternativa si cambia el alcance: {rule['alternative']}" in message, f"{path.name}: alternativa no llega a WhatsApp")
        require("modalidad y el alcance definitivos deben confirmarse" in message, f"{path.name}: falta disclaimer")
    require(all(count >= 1 for count in seen.values()), f"todas las modalidades deben estar representadas en fichas: {seen}")


def validate_workflows() -> None:
    build = (ROOT / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    governance = (ROOT / ".github/workflows/release-governance.yml").read_text(encoding="utf-8")
    for name, text in (("builder", build), ("Pages", pages), ("Governance", governance)):
        require("scripts/apply_recommendation_v514.py" in text, f"{name}: falta applicator v5.14")
        require("recommendation-v514" in text, f"{name}: paths v5.14 no gobernados")
    require(build.index("python3 scripts/apply_commercial_brief_v513.py") < build.index("python3 scripts/apply_recommendation_v514.py"), "builder debe terminar v5.13→v5.14")
    require("python3 scripts/validate_recommendation_v514.py" in pages, "Pages no valida v5.14")
    require("python3 scripts/validate_recommendation_v514.py" in governance, "Governance no valida v5.14")


def validate_e2e(contract: dict) -> None:
    text = (ROOT / "tests/e2e/public-site.spec.mjs").read_text(encoding="utf-8")
    require("data-recommendation-v514" in text, "E2E no verifica comparación v5.14")
    require("data-recommendation-brief-v514" in text, "E2E no verifica brief v5.14")
    product = contract["modalities"]["product"]
    require(product["fit"] in text, "E2E no verifica razón de producto")
    require(product["boundary"] in text, "E2E no verifica límite de producto")
    require(product["alternative"] in text, "E2E no verifica alternativa de producto")


def main() -> int:
    require(len(DETAIL_TARGETS) == 16, "deben existir 16 fichas profundas")
    contract = load_contract()
    validate_home(contract)
    validate_js(contract)
    validate_details(contract)
    validate_workflows()
    validate_e2e(contract)
    print("RECOMMENDATION V5.14 OK: 5 modalidades explicables + límites + alternativas + continuidad al brief/WhatsApp; scoring/storage/red desactivados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Valida v5.15: selector consolidado, comparación secundaria y ruta comercial controlada."""
from __future__ import annotations

from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
CONTRACT = ROOT / "recommendation-v514.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
CODES = ("diagnostic", "audit", "product", "specialist", "recurring")
ROUTE_BY_MODALITY = {
    "diagnostic": "scope",
    "audit": "proposal",
    "product": "proposal",
    "specialist": "scope",
    "recurring": "scope",
}
ROUTE_LABEL = {"proposal": "Propuesta verificable", "scope": "Definición de alcance", "orientation": "Orientación inicial"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"DECISION ACTION V5.15 FAIL: {message}")


def contract() -> dict:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    require(data.get("scoring") is False, "el contrato v5.14 debe mantener scoring=false")
    require(tuple((data.get("modalities") or {}).keys()) == CODES, "deben existir cinco modalidades canónicas")
    return data


def href_params(href: str) -> dict[str, list[str]]:
    return parse_qs(urlsplit(unescape(href)).query)


def whatsapp_text(href: str) -> str:
    return parse_qs(urlsplit(unescape(href)).query).get("text", [""])[0]


def validate_home(data: dict) -> None:
    text = HOME.read_text(encoding="utf-8")
    require('<link rel="stylesheet" href="decision-action-v515.css">' in text, "falta CSS v5.15")
    require('<script src="decision-action-v515.js"></script>' in text, "falta JS v5.15")
    require(text.count('data-decision-action-v515="true"') == 1, "debe existir una única superficie v5.15 en home")
    require(text.count('data-decision-action-source-v515=') == 5, "las cinco tarjetas v5.12 deben ser fuentes de acción")
    require(text.count('class="proof-fit-v515"') == 5, "cada modalidad debe mostrar encaje junto al CTA")
    for code, rule in data["modalities"].items():
        proof = re.search(r'<a class="proof-model-card-v512"[^>]*data-proof-model-v512="' + re.escape(code) + r'"[^>]*>.*?</a>', text, re.S)
        require(bool(proof), f"falta selector v5.12 {code}")
        require(f'data-decision-action-source-v515="{code}"' in proof.group(0), f"{code}: selector no participa en v5.15")
        require(rule["fit"] in proof.group(0), f"{code}: encaje no quedó junto al CTA")

    compare = re.search(r'<details class="recommendation-compare-v515"[^>]*>.*?</details>', text, re.S)
    require(bool(compare), "falta comparación secundaria desplegable")
    require(" open" not in compare.group(0).split(">", 1)[0], "comparación ampliada debe iniciar colapsada")
    require(compare.group(0).count('data-recommendation-model-v514=') == 5, "comparación debe conservar cinco modalidades v5.14")
    for code, rule in data["modalities"].items():
        require(rule["boundary"] in compare.group(0) and rule["alternative"] in compare.group(0), f"{code}: comparación pierde límite o alternativa")
    require('class="recommendation-fit-source-v515"' in compare.group(0), "la fuente de encaje v5.14 debe preservarse para compatibilidad")
    css = (ROOT / "decision-action-v515.css").read_text(encoding="utf-8")
    require(".recommendation-compare-v515 .recommendation-fit-source-v515{display:none}" in css, "encaje duplicado debe ocultarse en comparación ampliada")

    form = re.search(r'<!-- RECOMMENDATION-V514-FORM:START -->(.*?)<!-- RECOMMENDATION-V514-FORM:END -->', text, re.S)
    require(bool(form), "falta brief v5.14/v5.15 en formulario")
    block = form.group(1)
    for attr in ("data-decision-route-v515", "data-route-panel-v515", "data-route-label-v515", "data-route-copy-v515", "data-route-source-v515", "data-apply-route-v515"):
        require(attr in block, f"formulario carece de {attr}")
    require('data-recommendation-fit-v514' in block and 'data-recommendation-boundary-v514' in block and 'data-recommendation-alternative-v514' in block, "v5.15 debe conservar outputs explicables v5.14")
    require('<details class="recommendation-details-v515"' in block, "límite/alternativa deben quedar bajo detalle secundario")


def validate_runtime() -> None:
    js = (ROOT / "decision-action-v515.js").read_text(encoding="utf-8")
    require("localStorage" not in js and "sessionStorage" not in js, "v5.15 no debe persistir decisión")
    require("fetch(" not in js and "XMLHttpRequest" not in js, "v5.15 no debe introducir transporte de red")
    require("automaticChange: false" in js, "v5.15 debe declarar ausencia de cambio automático")
    require("scoring: false" in js, "v5.15 debe mantener scoring desactivado")
    for code, route in ROUTE_BY_MODALITY.items():
        require(f"{code}: '{route}'" in js, f"runtime carece de ruta {code}→{route}")
    require("preferred.explicit" in js and "routeButton.disabled = true" in js, "una intención explícita debe prevalecer y bloquear reaplicación")
    require("decisionStage.dispatchEvent(new Event('change'" in js, "aplicación manual debe reutilizar el flujo existente")


def modality(text: str) -> str:
    match = re.search(r'<section class="proof-detail-v512"[^>]*data-commercial-modality-v513="([^"]+)"[^>]*>', text)
    require(bool(match), "ficha sin modalidad v5.13")
    return match.group(1)


def validate_details() -> None:
    seen = {code: 0 for code in CODES}
    for path in DETAIL_TARGETS:
        text = path.read_text(encoding="utf-8")
        code = modality(text)
        require(code in ROUTE_BY_MODALITY, f"{path.name}: modalidad desconocida {code}")
        seen[code] += 1
        route = ROUTE_BY_MODALITY[code]

        cta = re.search(r'<a class="buying-clarity-cta-v58"[^>]*data-decision-v58-cta="true"[^>]*>', text)
        require(bool(cta), f"{path.name}: falta CTA principal")
        require(f'data-action-route-v515="{route}"' in cta.group(0), f"{path.name}: CTA no declara ruta {route}")
        href = re.search(r'href="([^"]+)"', cta.group(0))
        require(bool(href) and href_params(href.group(1)).get("commercial_intent") == [route], f"{path.name}: CTA principal pierde ruta {route}")
        params = href_params(href.group(1))
        require(params.get("modality") == [code] and params.get("proof_standard") == ["source"], f"{path.name}: CTA pierde modalidad/prueba")

        general = re.search(r'<a class="btn btn-outline-light" href="([^"]+)">Formulario general</a>', text)
        require(bool(general), f"{path.name}: falta formulario general")
        general_params = href_params(general.group(1))
        require(general_params.get("commercial_intent") == [route], f"{path.name}: formulario general debe usar {route}")
        require(general_params.get("modality") == [code] and general_params.get("proof_standard") == ["source"], f"{path.name}: formulario general pierde contexto v5.13")

        direct = re.search(r'<a class="btn btn-gold" href="(https://wa\.me/573008507813\?text=[^"]+)"[^>]*>Conversar por WhatsApp →</a>', text)
        require(bool(direct), f"{path.name}: falta WhatsApp directo")
        message = whatsapp_text(direct.group(1))
        require(f"Siguiente paso sugerido: {ROUTE_LABEL[route]}." in message, f"{path.name}: WhatsApp directo no explica siguiente paso")
        require("Por qué encaja la modalidad:" in message and "Límite de la modalidad:" in message and "Alternativa si cambia el alcance:" in message, f"{path.name}: v5.15 no debe perder explicación v5.14")
    require(all(count >= 1 for count in seen.values()), f"todas las modalidades deben estar representadas: {seen}")


def validate_workflows() -> None:
    build = (ROOT / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    governance = (ROOT / ".github/workflows/release-governance.yml").read_text(encoding="utf-8")
    for name, text in (("builder", build), ("Pages", pages), ("Governance", governance)):
        require("decision-action-v515" in text, f"{name}: paths v5.15 no gobernados")
        require("scripts/apply_decision_action_v515.py" in text, f"{name}: falta applicator v5.15")
        require("scripts/validate_decision_action_v515.py" in text, f"{name}: falta validator v5.15")
    require(build.index("python3 scripts/apply_recommendation_v514.py") < build.index("python3 scripts/apply_decision_action_v515.py"), "builder debe terminar v5.14→v5.15")
    require(pages.index("python3 scripts/apply_recommendation_v514.py") < pages.index("python3 scripts/apply_decision_action_v515.py"), "Pages debe componer v5.14→v5.15")
    require(governance.index("python3 scripts/apply_recommendation_v514.py") < governance.index("python3 scripts/apply_decision_action_v515.py"), "Governance debe componer v5.14→v5.15")


def validate_e2e(data: dict) -> None:
    text = (ROOT / "tests/e2e/public-site.spec.mjs").read_text(encoding="utf-8")
    for marker in ("data-decision-action-v515", "data-recommendation-compare-v515", "data-decision-route-v515", "data-route-panel-v515"):
        require(marker in text, f"E2E no verifica {marker}")
    require(data["modalities"]["product"]["fit"] in text, "E2E debe conservar encaje del producto")
    require("Siguiente paso sugerido: Definición de alcance" in text, "E2E debe verificar handoff de alcance en servicio")


def main() -> int:
    require(len(DETAIL_TARGETS) == 16, "deben existir 16 fichas profundas")
    data = contract()
    validate_home(data)
    validate_runtime()
    validate_details()
    validate_workflows()
    validate_e2e(data)
    print("DECISION ACTION V5.15 OK: 5 modalidades consolidadas + rutas proposal/scope/orientation controladas + 16 handoffs coherentes, sin scoring/storage/red.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

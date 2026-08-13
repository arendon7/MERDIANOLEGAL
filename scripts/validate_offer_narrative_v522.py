#!/usr/bin/env python3
"""Valida v5.22: narrativa de oferta, diferenciación y criterio jurídico sin claims ficticios."""
from __future__ import annotations

from pathlib import Path
import json
import re

R = Path(__file__).resolve().parents[1]
CONTRACT = R / "offer-narrative-v522.json"
HOME = R / "index.html"
CATALOG_RUNTIME = R / "catalog-page.js"
EXPECTED_IDS = {
    "service-diagnostic", "service-direction", "service-contracts", "service-corporate",
    "service-ip", "service-ai", "service-regulated", "service-ops",
    "product-diagnostic", "product-organized", "product-assets", "product-investment",
    "product-ai", "product-regulated", "product-contract-system", "product-data-consumer",
}
PAIRS = {
    "service-diagnostic": "product-diagnostic",
    "service-contracts": "product-contract-system",
    "service-ip": "product-assets",
    "service-ai": "product-ai",
    "service-regulated": "product-regulated",
}
FORBIDDEN_CLAIMS = (
    "garantizamos resultados",
    "garantía de resultado",
    "mejor firma",
    "líder del mercado",
    "años de experiencia",
    "clientes satisfechos",
    "portal productivo meridiano empresas",
    "ley general de ia vigente en colombia",
)
UNSAFE_PLATFORM_PHRASES = (
    "Meridiano Empresas o SharePoint/OneDrive",
    "Meridiano Empresas o Microsoft 365",
    "Meridiano Empresas o tablero acordado",
    "Meridiano Empresas o entorno disponible",
)
CATALOG_DIRS = (R / "catalog-services-v42", R / "catalog-products-v41")
DETAIL_STATIC_PATTERN = re.compile(r'<div\s+id="detail-page"\s+data-static-catalog="true">')


def fail(message: str) -> None:
    raise SystemExit(f"OFFER NARRATIVE V5.22 ERROR: {message}")


def safe_meridiano_reference(text: str) -> bool:
    if "Meridiano Empresas" not in text:
        return True
    conditional = re.search(
        r"Meridiano Empresas[^.\n]{0,120}(?:habilitad[oa]|habilitación productiva|opere productivamente|operación productiva)",
        text,
        re.I,
    )
    explicit_demo = "Demostración" in text and "demo.html" in text
    return bool(conditional or explicit_demo)


def load_contract() -> dict:
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if payload.get("version") != "5.22.0":
        fail("el contrato debe declarar version 5.22.0")
    offers = payload.get("offers") or {}
    if set(offers) != EXPECTED_IDS:
        fail(f"IDs de oferta desalineados: {sorted(set(offers) ^ EXPECTED_IDS)}")
    for catalog_id, entry in offers.items():
        for field in ("decision", "modality_reason", "installed", "alternative", "legal_lens"):
            if not entry.get(field):
                fail(f"{catalog_id}: falta {field}")
        alt = entry["alternative"]
        if not all(str(alt.get(key, "")).strip() for key in ("label", "href", "copy")):
            fail(f"{catalog_id}: alternativa incompleta")
        lens = entry["legal_lens"]
        if not isinstance(lens, list) or len(lens) != 3:
            fail(f"{catalog_id}: legal_lens debe contener exactamente 3 criterios")
        for item in lens:
            if not isinstance(item, list) or len(item) != 2 or not all(str(value).strip() for value in item):
                fail(f"{catalog_id}: lente jurídica inválida")
        corpus = json.dumps(entry, ensure_ascii=False).lower()
        for claim in FORBIDDEN_CLAIMS:
            if claim in corpus:
                fail(f"{catalog_id}: claim no verificable/prohibido: {claim}")
    return payload


def validate_catalog_capability_truth() -> None:
    files = [path for folder in CATALOG_DIRS for path in sorted(folder.glob("*.json"))]
    if len(files) != 16:
        fail(f"se esperaban 16 fuentes de catálogo y se encontraron {len(files)}")
    for path in files:
        text = path.read_text(encoding="utf-8")
        for phrase in UNSAFE_PLATFORM_PHRASES:
            if phrase in text:
                fail(f"{path.relative_to(R)}: referencia de plataforma ambigua: {phrase}")
        if not safe_meridiano_reference(text):
            fail(f"{path.relative_to(R)}: Meridiano Empresas debe estar condicionado a operación productiva o identificado como demo")


def page_map() -> dict[str, Path]:
    result: dict[str, Path] = {}
    for folder in ("servicios", "productos"):
        for path in sorted((R / folder).glob("*.html")):
            text = path.read_text(encoding="utf-8")
            match = re.search(r'data-catalog-id="([^"]+)"', text)
            if not match:
                fail(f"{path.relative_to(R)} sin data-catalog-id")
            catalog_id = match.group(1)
            if catalog_id in result:
                fail(f"catalog-id duplicado: {catalog_id}")
            result[catalog_id] = path
    if set(result) != EXPECTED_IDS:
        fail(f"las 16 fichas no corresponden al contrato: {sorted(set(result) ^ EXPECTED_IDS)}")
    return result


def validate_source_contract(payload: dict, pages: dict[str, Path]) -> None:
    offers = payload["offers"]
    for left, right in PAIRS.items():
        left_href = offers[left]["alternative"]["href"]
        right_href = offers[right]["alternative"]["href"]
        if pages[right].name not in left_href or pages[left].name not in right_href:
            fail(f"par {left} ↔ {right} no es recíproco")
        if offers[left]["modality_reason"] == offers[right]["modality_reason"]:
            fail(f"par {left} ↔ {right} no diferencia modalidad")

    ai_service = json.dumps(offers["service-ai"], ensure_ascii=False)
    ai_product = json.dumps(offers["product-ai"], ensure_ascii=False)
    if "CONPES 4144 de 2025" not in ai_service or "CONPES 4144 de 2025" not in ai_product:
        fail("IA debe distinguir la Política Nacional de IA mediante CONPES 4144 de 2025")
    service_policy_boundary = "ley general" in ai_service.lower() and "conpes" in ai_service.lower()
    product_policy_boundary = (
        "conpes" in ai_product.lower()
        and "política pública" in ai_product.lower()
        and "proyectos legislativos" in ai_product.lower()
        and "derecho vigente" in ai_product.lower()
    )
    if not service_policy_boundary or not product_policy_boundary:
        fail("IA debe diferenciar semánticamente política pública, proyectos legislativos y derecho vigente")

    data = json.dumps(offers["product-data-consumer"], ensure_ascii=False)
    if "Ley 1581 de 2012" not in data or "Ley 1480 de 2011" not in data:
        fail("datos/consumidor debe conservar las referencias legales verificadas")
    corporate = json.dumps(offers["service-corporate"], ensure_ascii=False)
    if "Ley 1258 de 2008" not in corporate:
        fail("societario debe conservar referencia SAS verificable cuando aplique")

    for catalog_id, entry in offers.items():
        href = str(entry["alternative"]["href"]).split("#", 1)[0].split("?", 1)[0]
        if href:
            target = (pages[catalog_id].parent / href).resolve()
            try:
                target.relative_to(R.resolve())
            except ValueError:
                fail(f"{catalog_id}: alternativa sale del repositorio")
            if not target.exists():
                fail(f"{catalog_id}: alternativa local inexistente: {href}")


def validate_static_first_runtime() -> None:
    text = CATALOG_RUNTIME.read_text(encoding="utf-8")
    required = (
        "STATIC-FIRST-V522",
        "const staticCatalog = document.getElementById('detail-page');",
        "if (staticCatalog?.dataset.staticCatalog === 'true') return;",
        "if (!productSources[id]) return;",
    )
    for marker in required:
        if marker not in text:
            fail(f"catalog-page.js: falta guard static-first {marker!r}")
    product_gate = text.index("if (!productSources[id]) return;")
    guard = text.index("if (staticCatalog?.dataset.staticCatalog === 'true') return;")
    renderer = text.index("const render = (entry) =>")
    fetcher = text.index("fetch(productSources[id]")
    if not (product_gate < guard < renderer < fetcher):
        fail("catalog-page.js: servicios deben salir por product gate y productos static-first antes del renderer/fetch legado")


def static_body(text: str, path: Path) -> str:
    match = re.search(r'<!-- STATIC-CATALOG-BODY:START -->(.*?)<!-- STATIC-CATALOG-BODY:END -->', text, re.S)
    if not match:
        fail(f"{path.relative_to(R)}: falta STATIC-CATALOG-BODY")
    return match.group(1)


def validate_materialized_pages(pages: dict[str, Path]) -> None:
    for catalog_id, path in pages.items():
        text = path.read_text(encoding="utf-8")
        if len(DETAIL_STATIC_PATTERN.findall(text)) != 1:
            fail(f"{path.relative_to(R)}: #detail-page debe declarar exactamente una vez data-static-catalog=true")

        marker = f'data-offer-narrative-v522="{catalog_id}"'
        if text.count(marker) != 1:
            fail(f"{path.relative_to(R)}: debe materializar exactamente una capa v5.22")
        if text.count('<link rel="stylesheet" href="../offer-v522.css">') != 1:
            fail(f"{path.relative_to(R)}: debe cargar offer-v522.css una vez")
        body = static_body(text, path)
        for required in (
            "CRITERIO DE CONTRATACIÓN",
            "DECISIÓN EMPRESARIAL",
            "POR QUÉ ESTA MODALIDAD",
            "CAPACIDAD QUE QUEDA INSTALADA",
            "ALTERNATIVA CERCANA",
            "LENTE JURÍDICA",
        ):
            if required not in body:
                fail(f"{path.relative_to(R)}: falta {required}")
        if body.count('class="offer-positioning-card-v522"') != 3:
            fail(f"{path.relative_to(R)}: la capa debe tener 3 bloques editoriales")
        if body.count('offer-legal-lens-grid-v522') != 1:
            fail(f"{path.relative_to(R)}: lente jurídica duplicada o ausente")
        for phrase in UNSAFE_PLATFORM_PHRASES:
            if phrase in body:
                fail(f"{path.relative_to(R)}: referencia de plataforma ambigua: {phrase}")
        if not safe_meridiano_reference(body):
            fail(f"{path.relative_to(R)}: mención de Meridiano Empresas sin condición productiva ni contexto demo")


def validate_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    required = (
        'data-home-narrative-v522="true"',
        "Dirección jurídica <em>para decisiones que deben avanzar.</em>",
        "No entregamos respuestas aisladas",
        "Primero defina qué necesita resolver; después elija cómo conviene contratarlo.",
        "CÓMO SE VE EL CRITERIO SENIOR",
        "Intervenciones para hechos, actores y negociaciones que exigen criterio adaptable.",
        "Resultados jurídicos con perímetro, entregables y cierre definidos desde el inicio.",
    )
    for item in required:
        if item not in text:
            fail(f"index.html: falta narrativa canónica: {item}")
    if text.count('data-home-decision-v520="true"') != 1:
        fail("index.html: v5.22 debe conservar exactamente una superficie de modalidad v5.20")
    if 'id="elegir"' in text or "DECISION-V58-HOME:START" in text:
        fail("index.html: no puede reaparecer la arquitectura de decisión redundante pre-v5.20")
    if text.count(CSS := '<link rel="stylesheet" href="offer-v522.css">') != 1:
        fail(f"index.html: {CSS} debe aparecer una sola vez")


def main() -> int:
    payload = load_contract()
    validate_catalog_capability_truth()
    pages = page_map()
    validate_source_contract(payload, pages)
    validate_static_first_runtime()
    validate_materialized_pages(pages)
    validate_home()
    print("OFFER NARRATIVE V5.22 OK: 16/16 ofertas, 5 pares diferenciados, lente jurídica x3, capability truth source-driven, #detail-page canónico y runtime sin rehidratación destructiva.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Valida contratos estructurales y truth-parity de Experience System v6 Wave 2."""
from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
STYLE_HOME = [
    "assets/css/v6/tokens.css",
    "assets/css/v6/base.css",
    "assets/css/v6/components.css",
    "assets/css/v6/surfaces.css",
]
STYLE_DETAIL = [f"../{href}" for href in STYLE_HOME]
DETAIL_START = "<!-- EXPERIENCE-V60-DETAIL:START -->"
DETAIL_END = "<!-- EXPERIENCE-V60-DETAIL:END -->"
LEGACY_START = "<!-- EXPERIENCE-V60-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-LEGACY:END -->"


def fail(message: str) -> None:
    raise AssertionError(message)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(text(path))


def body_attr(value: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', value)
    return match.group(1) if match else ""


def count_public_html() -> int:
    root_files = list(ROOT.glob("*.html"))
    nested = []
    for folder in ("productos", "servicios", "soluciones", "sectores", "perspectivas"):
        nested.extend((ROOT / folder).glob("*.html"))
    return len(root_files) + len(nested)


def load_sources() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            fail(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            payload = load_json(path)
            if len(payload) != 1:
                fail(f"{path.name}: debe declarar exactamente un catalog_id")
            catalog_id, data = next(iter(payload.items()))
            if catalog_id in result:
                fail(f"catalog_id duplicado en fuentes: {catalog_id}")
            result[catalog_id] = data
    if len(result) != 16:
        fail(f"se esperaban 16 fuentes profundas y hay {len(result)}")
    return result


def load_detail_paths() -> dict[str, Path]:
    paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(paths) != 16:
        fail(f"se esperaban 16 fichas profundas y hay {len(paths)}")
    result: dict[str, Path] = {}
    for path in paths:
        value = text(path)
        catalog_id = body_attr(value, "data-catalog-id")
        if not catalog_id:
            fail(f"{path.relative_to(ROOT)}: falta data-catalog-id")
        if catalog_id in result:
            fail(f"catalog_id duplicado en HTML: {catalog_id}")
        result[catalog_id] = path
    return result


def assert_once(value: str, needle: str, label: str) -> None:
    count = value.count(needle)
    if count != 1:
        fail(f"{label}: esperaba 1 ocurrencia de {needle!r}; encontró {count}")


def assert_contains(value: str, needles: list[str], label: str) -> None:
    missing = [needle for needle in needles if needle not in value]
    if missing:
        fail(f"{label}: faltan {missing[:8]}" + (f" (+{len(missing)-8})" if len(missing) > 8 else ""))


def legacy_block(value: str, label: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r"(.*?)" + re.escape(LEGACY_END), value, flags=re.S)
    if not match:
        fail(f"{label}: falta bloque legacy preservado")
    return match.group(1)


def first_layer(value: str, label: str) -> str:
    start = value.find(DETAIL_START)
    legacy = value.find(LEGACY_START, start + len(DETAIL_START)) if start >= 0 else -1
    if start < 0 or legacy < 0:
        fail(f"{label}: no se pudo aislar la primera capa v6")
    return unescape(value[start:legacy])


def validate_contracts() -> None:
    contract = load_json(ROOT / "experience-system-v60.json")
    content = load_json(ROOT / "experience-content-v60.json")
    if contract.get("version") != "6.0.0" or content.get("version") != "6.0.0":
        fail("contratos Experience v6 deben declarar 6.0.0")
    baseline = contract.get("baseline", {})
    if baseline.get("html_total") != 46 or baseline.get("builder_steps") != 30 or baseline.get("deep_offers") != 16:
        fail("baseline v6 debe preservar 46 HTML, 16 fichas y 30 pasos")
    invariants = contract.get("invariants", {})
    for key in (
        "static_first", "single_physical_form", "manual_whatsapp_handoff", "no_pii_persistence",
        "no_business_conversion_inference", "no_fake_backend_capability", "full_legal_depth_preserved",
        "stable_only_after_all_gates",
    ):
        if invariants.get(key) is not True:
            fail(f"invariante v6 no está fijada: {key}")
    overrides = content.get("pilots", {})
    if set(overrides) != {"product-diagnostic", "service-ai"}:
        fail("los overrides editoriales deben seguir limitados a los dos pilotos aprobados")


def validate_builder() -> None:
    workflow = text(ROOT / ".github/workflows/build-canonical.yml")
    names = re.findall(r"(?m)^      - name:", workflow)
    if len(names) != 30:
        fail(f"builder v6 debe conservar 30 pasos nombrados; encontró {len(names)}")
    assert_contains(workflow, [
        "scripts/apply_experience_v60.py", "scripts/validate_experience_v60.py",
        "experience-system-v60.json", "experience-content-v60.json", "assets/css/v6/**",
        "catalog-products-v41/**", "catalog-services-v42/**",
    ], "builder")


def validate_home() -> None:
    value = text(HOME)
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="deep-offers"', 'data-experience-v60="home"',
        "Decisiones empresariales complejas, convertidas en estructura jurídica ejecutable.",
        "No necesita saber el nombre del servicio. Empiece por la decisión que debe resolver.",
        "El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.",
        "Cuéntenos qué decisión necesita resolver.", *[
            "soluciones/ordenar-riesgo-juridico-empresa.html",
            "soluciones/direccion-juridica-externa-empresa.html",
            "soluciones/gobernar-inteligencia-artificial-empresa.html",
            "soluciones/preparar-empresa-para-inversion.html",
            "soluciones/estructurar-proyecto-regulado.html",
            "soluciones/ordenar-operacion-juridica.html",
        ]
    ], "Home v6")
    for href in STYLE_HOME:
        assert_once(value, f'href="{href}"', "Home v6 styles")
    if len(re.findall(r"<form\b", value)) != 1:
        fail("Home v6 debe contener exactamente un formulario físico")
    if value.count('id="contacto"') != 1 or value.count('id="contacto-v531-legacy"') != 1:
        fail("Home v6 debe tener contacto principal único y contacto legacy renombrado")
    for marker in (
        "<!-- ENGAGEMENT-V511:START -->", "<!-- ENGAGEMENT-V511:END -->",
        "<!-- HANDOFF-V517:START -->", "<!-- HANDOFF-V517:END -->",
        'data-engagement-v511="true"', 'data-handoff-v517="true"',
    ):
        assert_once(value, marker, "Home v6 form contracts")
    legacy = legacy_block(value, "Home v6")
    assert_contains(legacy, ["PROFESSIONAL-AUTHORITY-V525-HOME:START", "EXPERIENCIA SECTORIAL", "PERSPECTIVAS", "PREGUNTAS FRECUENTES"], "Home legacy")
    if re.search(r"<form\b", legacy):
        fail("Home legacy no puede conservar una segunda copia del formulario")
    if "ENGAGEMENT-V511:START" in legacy or "HANDOFF-V517:START" in legacy:
        fail("v5.11/v5.17 deben viajar con el formulario canónico, no duplicarse en legacy")


def source_truth_needles(source: dict, kind: str) -> list[str]:
    needles = [source["result"]]
    if kind == "service":
        needles.append(source["question"])
    for field in ("deliverables", "perimeter", "method", "acceptance"):
        for title, copy in source.get(field, []):
            needles.extend([title, copy])
    needles.extend(source.get("limits", []))
    return needles


def validate_detail(catalog_id: str, path: Path, source: dict) -> None:
    value = text(path)
    kind = "product" if source.get("type") == "Producto jurídico" else "service"
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="deep-offers"',
        f'data-experience-v60="{catalog_id}"', f'data-experience-surface="{catalog_id}"',
        source["duration"], source["modality"], source["audience"],
    ], catalog_id)
    for href in STYLE_DETAIL:
        assert_once(value, f'href="{href}"', f"{catalog_id} styles")
    if re.search(r"<form\b", value):
        fail(f"{catalog_id}: una ficha profunda no debe crear formulario físico")
    assert_once(value, DETAIL_START, f"{catalog_id} marker")
    assert_once(value, DETAIL_END, f"{catalog_id} marker")

    first = first_layer(value, catalog_id)
    assert_contains(first, source_truth_needles(source, kind), f"{catalog_id} primera capa/source truth")

    legacy = legacy_block(value, catalog_id)
    assert_contains(legacy, [
        "DECISION-V58-DETAIL:START", "DECISION-COMPRESSION-V531:PAIR-START",
        "OFFER-NARRATIVE-V522:START", "PROOF-V512-DETAIL:START", 'id="limites-title"',
    ], f"{catalog_id} legacy")

    # Los dos pilotos conservan su capa editorial aprobada por encima de la misma verdad fuente.
    if catalog_id == "product-diagnostic":
        assert_contains(value, ["Sepa qué riesgo jurídico existe, qué evidencia falta y qué debe corregirse primero.", "1 sociedad colombiana", "Hasta 60"], catalog_id)
    if catalog_id == "service-ai":
        assert_contains(value, ["Adopte inteligencia artificial con casos, datos, proveedores y responsabilidades gobernables.", "Hasta 20", "2 sesiones"], catalog_id)


def main() -> int:
    if count_public_html() != 46:
        fail(f"se esperaban 46 HTML públicos; se encontraron {count_public_html()}")
    validate_contracts()
    validate_builder()
    validate_home()
    sources = load_sources()
    paths = load_detail_paths()
    if set(sources) != set(paths):
        fail(f"fuentes y fichas no coinciden; solo fuente={sorted(set(sources)-set(paths))}; solo HTML={sorted(set(paths)-set(sources))}")
    for catalog_id in sorted(sources):
        validate_detail(catalog_id, paths[catalog_id], sources[catalog_id])
    print("VALIDATE EXPERIENCE V6 WAVE 2 OK: 46 HTML, 30 pasos, 1 formulario y 16/16 fichas con truth visible + profundidad v5.31 preservada.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE EXPERIENCE V6 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

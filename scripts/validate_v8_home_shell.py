#!/usr/bin/env python3
"""Fail-closed validator for W5.0 Home + navigation source model across pre/persisted states.

This gate validates the source-driven shell and preserves the historical W5.0A
contracts. Once W5.0E is persisted, index.html is accepted only when it is
byte-identical to the certified source renderer.
"""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys

from render_v8_home_persisted import render_document
from v8_legacy_projection import PERSISTED_MARKER

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "assets/data/v8/home-shell-v80.json"
ROUTES = ROOT / "assets/data/v8/route-contract-v80.json"
PILOTS = ROOT / "assets/data/v8/experience-model-v80.json"
INDEX = ROOT / "index.html"
SITEMAP = ROOT / "sitemap.xml"

PILOT_ROUTES = (
    "soluciones/sistema-contractual-empresarial.html",
    "practicas/corporativo-societario-gobierno.html",
    "servicios-continuos/direccion-juridica-externa.html",
)
HOME_ORDER = [f"H{i:02d}" for i in range(1, 13)]
MOBILE_ORDER = [f"H{i:02d}" for i in range(1, 13)]
PRIMARY_LABELS = ["Qué hacemos", "Sectores", "Firma", "Insights", "Contacto"]
ANALYTICS = ["cta_click", "solution_view", "practice_view", "diagnosis_start", "contact_submit", "portal_click"]


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    if not path.exists():
        fail(f"falta {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def physical(href: str) -> Path:
    clean = href.split("?", 1)[0].split("#", 1)[0]
    if not clean:
        return INDEX
    path = ROOT / clean.lstrip("/")
    if clean.endswith("/"):
        path = path / "index.html"
    return path


def route_targets(route_contract: dict) -> dict[str, str]:
    result: dict[str, str] = {}
    families = route_contract["target_families"]
    for family in ("practices", "solutions"):
        for code, route in families[family]:
            result[code] = route
    for code, route, _publishable in families["recurring"]:
        result[code] = route
    return result


def nav_items(model: dict) -> dict[str, list]:
    items: dict[str, list] = {}
    for rows in model["navigation"]["mega_groups"].values():
        for row in rows:
            if len(row) != 5:
                fail(f"mega item inválido: {row!r}")
            code = row[0]
            if code in items:
                fail(f"ID duplicado en mega menu: {code}")
            items[code] = row
    return items


def main() -> int:
    model = load(MODEL)
    routes = load(ROUTES)
    pilots = load(PILOTS)

    if model.get("schema_version") != "1.0.0" or model.get("contract") != "v8-w5-home-shell":
        fail("identidad/schema del Home shell inválida")
    if model.get("status") != "candidate":
        fail("W5 source model debe permanecer status=candidate")
    activation = model.get("activation") or {}
    if any(activation.get(key) for key in ("public", "indexing_change", "sitemap_change")):
        fail("W5 source model no puede activar publicación, indexación ni sitemap")
    if activation.get("legacy_routes_unchanged") is not True:
        fail("W5 debe preservar rutas legacy")

    for _name, rel in model.get("sources", {}).items():
        if not (ROOT / rel).exists():
            fail(f"source contract inexistente: {rel}")

    primary = model["navigation"]["primary"]
    if [row[1] for row in primary] != PRIMARY_LABELS:
        fail("navegación primaria no coincide con contrato W5.0")
    if len(primary) != 5 or primary[0][2:] != ["mega", None]:
        fail("Qué hacemos debe ser el único trigger mega de primer nivel")
    forbidden_top = {"Productos", "Planes", "Documentos", "LegalAIZ", "Oferta completa"}
    if forbidden_top & {row[1] for row in primary}:
        fail("taxonomía legacy/infraestructura apareció en navegación primaria")

    actions = {row[0]: row for row in model["navigation"]["actions"]}
    if actions["talk"][1:] != ["Hablar con Meridiano", "primary", "#contacto", True]:
        fail("CTA primario cambió")
    if actions["portal"][4] is not False or actions["portal"][3] is not None:
        fail("Portal clientes no puede hacerse visible sin destino verificado")

    groups = model["navigation"]["mega_groups"]
    if len(groups["practices"]) != 6 or len(groups["solutions"]) != 8 or len(groups["recurring"]) != 2:
        fail("mega menu debe contener 6 prácticas, 8 soluciones y 2 continuos")
    items = nav_items(model)
    targets = route_targets(routes)
    if set(items) != set(targets):
        fail(f"IDs Home/route-contract divergen: home={sorted(items)}, routes={sorted(targets)}")
    for code, row in items.items():
        _id, _label, target, fallback, availability = row
        if target != targets[code]:
            fail(f"{code}: target Home {target} != route-contract {targets[code]}")
        if availability in {"legacy_bridge", "v8_pilot"}:
            if not fallback or not physical(fallback).is_file():
                fail(f"{code}: candidate_href no resuelve: {fallback!r}")
        elif code == "RC02":
            if fallback is not None or availability != "owner_confirmed_not_materialized":
                fail("RC02 debe permanecer sin href físico en W5")
        else:
            fail(f"{code}: availability desconocida {availability!r}")

    home = model["home"]
    if home["section_order"] != HOME_ORDER:
        fail("orden desktop H01-H12 cambió")
    if model["mobile"]["section_order"] != MOBILE_ORDER:
        fail("orden mobile no coincide con contrato W5.0")
    if model["mobile"].get("minimum_target_px", 0) < 44:
        fail("targets mobile deben ser >=44px")
    if model["mobile"].get("horizontal_overflow_forbidden") is not True:
        fail("overflow horizontal debe estar prohibido")

    if home["hero"]["title"] != "Derecho empresarial para decisiones que necesitan avanzar.":
        fail("H01 headline canónico cambió")
    if len(home["situations"]["items"]) != 6:
        fail("H02 debe contener seis situaciones")
    if home["featured_solutions"]["route_ids"] != ["SO01", "SO07", "SO04", "SO06"]:
        fail("H03 featured solutions cambió")
    if home["practices"]["route_ids"] != ["PR01", "PR02", "PR03", "PR04", "PR05", "PR06"]:
        fail("H05 debe listar seis prácticas canónicas")
    if home["method"]["steps"] != ["Entender", "Estructurar", "Ejecutar", "Controlar"]:
        fail("H06 método canónico cambió")
    if len(home["sectors"]["items"]) != 6:
        fail("H09 debe mostrar seis clusters sectoriales")

    rc02 = home["meridiano_contracts"]
    if rc02.get("capability_id") != "RC02" or rc02.get("capability_status") != "owner_confirmed":
        fail("H04 debe gobernarse por RC02 owner_confirmed")
    if rc02.get("publication_status") != "candidate_only" or rc02.get("technical_claims_status") != "deferred":
        fail("RC02 no puede declararse publicable/técnicamente verificado")
    rc02_text = json.dumps(rc02, ensure_ascii=False).lower()
    for required in ("futuras generaciones", "no modifican automáticamente", "revisión jurídica humana"):
        if required not in rc02_text:
            fail(f"RC02 omite guardrail requerido: {required}")
    for forbidden in ("uptime garantizado", "firma electrónica incluida", "autenticación multifactor", "cifrado certificado"):
        if forbidden in rc02_text:
            fail(f"RC02 incluye claim técnico no verificado: {forbidden}")

    rc01 = home["external_legal_direction"]
    rc01_text = json.dumps(rc01, ensure_ascii=False).lower()
    for forbidden in ("bolsa de horas", "horas al mes", "hourly retainer"):
        if forbidden not in rc01_text:
            fail(f"RC01 guardrail no declara framing prohibido: {forbidden}")
    for dimension in ("Cobertura", "Complejidad", "Prioridad", "SLA / nivel de servicio", "Gobierno y reporting"):
        if dimension not in rc01["commercial_dimensions"]:
            fail(f"RC01 falta dimensión comercial: {dimension}")

    if model["analytics"]["events"] != ANALYTICS or model["analytics"].get("pii_forbidden") is not True:
        fail("contrato analytics W5 cambió o permite PII")
    a11y = model["accessibility"]
    if a11y.get("standard") != "WCAG 2.1 AA" or not all(a11y.get(k) for k in ("keyboard_navigation", "visible_focus", "reduced_motion", "semantic_landmarks", "mega_menu_accessible")):
        fail("contrato de accesibilidad incompleto")

    recurring = {row[0]: row for row in routes["target_families"]["recurring"]}
    if recurring["RC02"][2] is not False:
        fail("route-contract histórico RC02 debe seguir publishable=false")
    if pilots["pilot_policy"].get("rc02_meridiano_contratos_in_scope") is not False:
        fail("W4 pilot model no debe reescribirse para introducir RC02")

    sitemap = SITEMAP.read_text(encoding="utf-8")
    for rel in PILOT_ROUTES:
        page = ROOT / rel
        if not page.is_file():
            fail(f"piloto W4 inexistente: {rel}")
        text = page.read_text(encoding="utf-8")
        robots = re.search(r'<meta name="robots" content="([^"]+)">', text)
        if not robots or "noindex" not in robots.group(1).lower():
            fail(f"piloto W4 perdió noindex antes de activation gate: {rel}")
        if rel in sitemap:
            fail(f"piloto W4 entró prematuramente al sitemap: {rel}")

    index = INDEX.read_text(encoding="utf-8")
    persisted = PERSISTED_MARKER in index
    if persisted:
        expected = render_document(model)
        if index != expected:
            fail("persisted W5 Home differs from source-driven E2 renderer")
        if home["hero"]["title"] not in index or 'data-v8-home-shell="persisted-candidate"' not in index:
            fail("persisted W5 Home lost canonical source markers")
    elif "data-v8-home-shell" in index or home["hero"]["title"] in index:
        fail("partial W5 Home detected before persisted marker")

    html_count = len(list(ROOT.rglob("*.html")))
    if html_count != 49:
        fail(f"W5 expects physical 49 HTML topology; found {html_count}")

    state = "persisted" if persisted else "pre-persist"
    print(f"VALIDATE V8 W5 HOME SHELL OK: 6 practices, 8 solutions, 2 recurring; H01-H12; 49 HTML; RC02 candidate-only; state={state}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 W5 HOME SHELL FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

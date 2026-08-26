#!/usr/bin/env python3
"""Renderer v8 para los tres pilotos W4.3.

En W4.3 este script es deliberadamente no-destructivo:
- `--check` valida modelo, fuentes, links target y truth parity en memoria;
- `--preview PILOT_ID` imprime el HTML candidato en stdout;
- no existe modo que escriba sobre superficies públicas.

La materialización física se habilitará en una wave posterior, después de que este
contrato y sus gates estén certificados.
"""
from __future__ import annotations

from argparse import ArgumentParser
from copy import deepcopy
from html import escape
from pathlib import Path, PurePosixPath
from urllib.parse import urlencode
import json
import posixpath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "assets/data/v8/experience-model-v80.json"
ROUTES_PATH = ROOT / "assets/data/v8/route-contract-v80.json"
SITE_CONFIG = ROOT / "site-config.json"

REQUIRED_SOURCE_FIELDS = {
    "summary", "duration", "modality", "audience", "question", "result",
    "situations", "scope", "perimeter", "method", "deliverables", "formats",
    "timeline", "requirements", "responsibilities", "acceptance", "limits",
    "supplements", "related",
}

PRESENTATION_OVERRIDE_FIELDS = {
    "scope", "perimeter", "method", "deliverables", "requirements", "limits", "supplements",
}

FAMILY_LABELS = {
    "solution": "Solución Meridiano",
    "practice": "Práctica",
    "recurring": "Servicio continuo",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def e(value: object) -> str:
    return escape(str(value), quote=True)


def fail(message: str) -> None:
    raise AssertionError(message)


def route_rows(contract: dict) -> list[dict]:
    fields = contract["legacy_route_fields"]
    return [dict(zip(fields, row)) for row in contract["legacy_routes"]]


def load_source(pilot: dict) -> dict:
    path = ROOT / pilot["source"]
    if not path.exists():
        fail(f"{pilot['id']}: fuente inexistente {pilot['source']}")
    payload = load_json(path)
    if list(payload) != [pilot["catalog_id"]]:
        fail(f"{pilot['id']}: catalog_id no coincide con la única entrada de {pilot['source']}")
    entry = payload[pilot["catalog_id"]]
    missing = sorted(REQUIRED_SOURCE_FIELDS - set(entry))
    if missing:
        fail(f"{pilot['id']}: fuente incompleta, faltan {missing}")
    if pilot["family"] == "solution" and not entry.get("productV41"):
        fail(f"{pilot['id']}: solución piloto debe provenir de producto v4.1")
    if pilot["family"] in {"practice", "recurring"} and not entry.get("serviceV42"):
        fail(f"{pilot['id']}: práctica/recurrente piloto debe provenir de servicio v4.2")
    return entry


def _resolve_override_parent(container: object, path: list[object], pilot_id: str) -> tuple[object, object]:
    if not path:
        fail(f"{pilot_id}: presentation override sin path")
    cursor = container
    for part in path[:-1]:
        if isinstance(part, str):
            if not isinstance(cursor, dict) or part not in cursor:
                fail(f"{pilot_id}: path de presentation override inválido en {part!r}")
            cursor = cursor[part]
        elif isinstance(part, int):
            if not isinstance(cursor, list) or part < 0 or part >= len(cursor):
                fail(f"{pilot_id}: índice de presentation override inválido en {part}")
            cursor = cursor[part]
        else:
            fail(f"{pilot_id}: segmento de presentation override inválido {part!r}")
    return cursor, path[-1]


def apply_presentation_overrides(pilot: dict, source: dict) -> dict:
    """Aplica únicamente overrides v8 explícitos y auditables sobre una copia de truth legacy.

    Cada reemplazo debe declarar path exacto, valor histórico esperado (`from`) y
    framing v8 (`to`). Si la truth histórica cambia, el renderer falla cerrado en
    lugar de aplicar una sustitución silenciosa sobre contenido nuevo.
    """
    effective = deepcopy(source)
    contract = pilot.get("presentation_overrides")
    if contract is None:
        return effective

    if pilot.get("id") != "RC01" or pilot.get("family") != "recurring":
        fail(f"{pilot['id']}: presentation_overrides solo están autorizados para RC01 en W4.12")
    if contract.get("policy") != "commercial-framing-only":
        fail(f"{pilot['id']}: presentation override policy inválida")
    replacements = contract.get("replacements")
    if not isinstance(replacements, list) or not replacements:
        fail(f"{pilot['id']}: presentation_overrides requiere replacements")

    seen_paths: set[tuple[object, ...]] = set()
    for replacement in replacements:
        if not isinstance(replacement, dict):
            fail(f"{pilot['id']}: replacement inválido")
        path = replacement.get("path")
        expected = replacement.get("from")
        target = replacement.get("to")
        if not isinstance(path, list) or not path or not isinstance(path[0], str):
            fail(f"{pilot['id']}: replacement path inválido")
        if path[0] not in PRESENTATION_OVERRIDE_FIELDS:
            fail(f"{pilot['id']}: override fuera de campos permitidos: {path[0]}")
        path_key = tuple(path)
        if path_key in seen_paths:
            fail(f"{pilot['id']}: override duplicado en {path}")
        seen_paths.add(path_key)
        if not isinstance(expected, str) or not isinstance(target, str) or not target.strip():
            fail(f"{pilot['id']}: from/to deben ser strings no vacíos")

        parent, leaf = _resolve_override_parent(effective, path, pilot["id"])
        if isinstance(leaf, str):
            if not isinstance(parent, dict) or leaf not in parent:
                fail(f"{pilot['id']}: leaf inválido en {path}")
            current = parent[leaf]
            if current != expected:
                fail(f"{pilot['id']}: truth source cambió en {path}; esperado {expected!r}, encontró {current!r}")
            parent[leaf] = target
        elif isinstance(leaf, int):
            if not isinstance(parent, list) or leaf < 0 or leaf >= len(parent):
                fail(f"{pilot['id']}: leaf index inválido en {path}")
            current = parent[leaf]
            if current != expected:
                fail(f"{pilot['id']}: truth source cambió en {path}; esperado {expected!r}, encontró {current!r}")
            parent[leaf] = target
        else:
            fail(f"{pilot['id']}: leaf de override inválido en {path}")

    effective_text = json.dumps(effective, ensure_ascii=False).lower()
    for forbidden in ("bolsa mensual", "atención dentro de la bolsa", "bolsa adicional"):
        if forbidden in effective_text:
            fail(f"{pilot['id']}: framing por bolsa persiste después del override: {forbidden!r}")
    if re.search(r"\bhoras?\b", effective_text):
        fail(f"{pilot['id']}: framing público por horas persiste después del override")
    return effective


def resolve_related_href(pilot: dict, href: str, route_map: dict[str, str]) -> str:
    if re.match(r"^[a-z]+://", href, flags=re.I) or href.startswith(("#", "mailto:", "tel:")):
        return href
    legacy = pilot["legacy_route"]
    parent = posixpath.dirname(legacy)
    current = posixpath.normpath(posixpath.join(parent, href))
    if not current.startswith("/"):
        current = "/" + current
    target = route_map.get(current, current)
    target_path = PurePosixPath(target)
    # Los tres target pilots viven a una carpeta de profundidad. Generamos href
    # relativo a su carpeta para conservar hosting GitHub Pages de proyecto.
    from_dir = PurePosixPath(pilot["target_route"]).parent
    relative = posixpath.relpath(str(target_path), str(from_dir))
    return relative


def indexed_rows(items: list[list[str]], prefix: str = "") -> str:
    rows = []
    for index, item in enumerate(items, 1):
        title, description = item[0], item[1]
        marker = f"{prefix}{index:02d}" if prefix else f"{index:02d}"
        rows.append(
            f'<div class="ml-index-row"><b>{e(marker)}</b><strong>{e(title)}</strong><p>{e(description)}</p></div>'
        )
    return "".join(rows)


def ledger(items: list[list[str]]) -> str:
    return '<div class="ml-ledger">' + "".join(
        f'<div class="ml-ledger-item"><span>{index:02d}</span><strong>{e(item[0])}</strong><p>{e(item[1])}</p></div>'
        for index, item in enumerate(items, 1)
    ) + "</div>"


def timeline(items: list[list[str]]) -> str:
    return '<ol class="ml-timeline">' + "".join(
        f'<li><strong>{e(item[0])}</strong><span>{e(item[1])}</span></li>' for item in items
    ) + "</ol>"


def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{e(item)}</li>" for item in items) + "</ul>"


def related(pilot: dict, items: list[list[str]], route_map: dict[str, str]) -> str:
    cards = []
    for label, title, description, href in items:
        resolved = resolve_related_href(pilot, href, route_map)
        cards.append(
            f'<a href="{e(resolved)}"><span class="ml-eyebrow">{e(label)}</span>'
            f'<strong>{e(title)}</strong><p>{e(description)}</p><span>Explorar →</span></a>'
        )
    return '<div class="ml-related">' + "".join(cards) + "</div>"


def contact_href(pilot: dict, source: dict) -> str:
    commercial = pilot["legacy_commercial_contract"]
    query = urlencode({
        "context": f"{FAMILY_LABELS[pilot['family']]}: {pilot['public_title']}",
        "need": source.get("question", pilot["public_title"]),
        "commercial_intent": commercial["intent"],
        "modality": commercial["modality"],
        "proof_standard": "source",
        "experience": "v8-pilot",
    })
    return f"../index.html?{query}#contacto"


def head(pilot: dict, source: dict, base_url: str) -> str:
    target = base_url + pilot["target_route"].lstrip("/")
    description = source["summary"]
    title = pilot["public_title"]
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": title,
        "description": description,
        "url": target,
        "isPartOf": {"@type": "WebSite", "name": "Meridiano Legal", "url": base_url},
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": base_url},
            {"@type": "ListItem", "position": 2, "name": FAMILY_LABELS[pilot["family"]], "item": target},
            {"@type": "ListItem", "position": 3, "name": title, "item": target},
        ],
    }
    return f'''<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="description" content="{e(description)}">
  <meta name="robots" content="noindex,follow">
  <meta name="theme-color" content="#13263a">
  <meta property="og:title" content="{e(title)} | Meridiano Legal">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{e(target)}">
  <title>{e(title)} | Meridiano Legal — piloto v8</title>
  <link rel="canonical" href="{e(target)}">
  <link rel="icon" href="../assets/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../assets/css/v8/tokens.css">
  <link rel="stylesheet" href="../assets/css/v8/base.css">
  <link rel="stylesheet" href="../assets/css/v8/components.css">
  <link rel="stylesheet" href="../assets/css/v8/surfaces.css">
  <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(',', ':'))}</script>
  <script type="application/ld+json">{json.dumps(breadcrumb, ensure_ascii=False, separators=(',', ':'))}</script>
</head>'''


def hero(pilot: dict, source: dict) -> str:
    href = contact_href(pilot, source)
    return f'''<section class="ml-hero" aria-labelledby="ml-title">
  <div class="ml-container ml-hero-grid">
    <div class="ml-hero-copy">
      <span class="ml-family-marker">{e(FAMILY_LABELS[pilot['family']])}</span>
      <h1 id="ml-title">{e(pilot['public_title'])}</h1>
      <p class="ml-lead">{e(source['summary'])}</p>
      <div class="ml-actions"><a class="ml-btn" href="{e(href)}">Presentar esta necesidad →</a><a class="ml-btn ml-btn--secondary" href="#ml-result">Ver qué obtiene la empresa</a></div>
      <div class="ml-meta-ledger"><div><span>Horizonte</span><strong>{e(source['duration'])}</strong></div><div><span>Modalidad</span><strong>{e(source['modality'])}</strong></div><div><span>Dirigido a</span><strong>{e(source['audience'])}</strong></div></div>
    </div>
    <aside class="ml-hero-aside"><p class="ml-eyebrow">DECISIÓN CENTRAL</p><strong>{e(source['question'])}</strong><p>El alcance definitivo se confirma en propuesta. Este piloto no altera el contrato comercial vigente.</p></aside>
  </div>
</section>'''


def section(section_id: str, eyebrow: str, title: str, body: str, modifier: str = "") -> str:
    cls = f"ml-section{(' ' + modifier) if modifier else ''}"
    return f'''<section class="{cls}" id="{e(section_id)}" aria-labelledby="{e(section_id)}-title"><div class="ml-container"><div class="ml-section-head"><p class="ml-eyebrow">{e(eyebrow)}</p><h2 id="{e(section_id)}-title">{e(title)}</h2></div>{body}</div></section>'''


def governance(source: dict) -> str:
    # No inventa un SLA concreto: usa únicamente categorías presentes en source/override gobernado.
    items = [
        ("Perímetro", source["perimeter"][0][0]),
        ("Usuarios / capacidad", source["perimeter"][1][0]),
        ("Cobertura", source["perimeter"][2][0]),
        ("Cadencia", source["timeline"][2][0] if len(source["timeline"]) > 2 else source["duration"]),
    ]
    return '<div class="ml-recurring-governance">' + "".join(
        f'<div><span>{e(label)}</span><strong>{e(value)}</strong></div>' for label, value in items
    ) + "</div>"


def deep_layer(pilot: dict, source: dict, route_map: dict[str, str]) -> str:
    parts = [
        section("ml-scope", "ALCANCE DETALLADO", "Frentes que puede comprender la intervención.", ledger(source["scope"])),
        section("ml-formats", "FORMATOS Y TRAZABILIDAD", "Cómo quedan disponibles las salidas del trabajo.", ledger(source["formats"]), "ml-section--soft"),
        section("ml-responsibilities", "RESPONSABILIDADES", "La intervención funciona cuando cada decisión tiene dueño.", ledger(source["responsibilities"])),
        section("ml-supplements", "EXTENSIONES", "Qué exige ampliar expresamente el alcance.", ledger(source["supplements"]), "ml-section--ivory"),
        section("ml-related", "RELACIONADOS", "Continuidad y capacidades relacionadas.", related(pilot, source["related"], route_map)),
    ]
    return '<details class="ml-disclosure"><summary><span>Profundidad jurídica y operativa</span><span>Ver alcance completo</span></summary><div class="ml-disclosure-body">' + "".join(parts) + "</div></details>"


def body(pilot: dict, source: dict, route_map: dict[str, str]) -> str:
    family = pilot["family"]
    blocks = [
        section("ml-fit", "CUÁNDO ENCAJA", "Situaciones que justifican revisar esta intervención.", '<div class="ml-index">' + indexed_rows(source["situations"]) + "</div>"),
        section("ml-result", "RESULTADO", "Qué cambia para la empresa.", f'<div class="ml-outcome"><p>{e(source["result"])}</p></div>', "ml-section--ivory"),
    ]

    if family == "practice":
        blocks.append(section("ml-scope-primary", "CAMPO DE INTERVENCIÓN", "Decisiones y frentes que puede cubrir la práctica.", ledger(source["scope"])))
    elif family == "recurring":
        blocks.append(section("ml-governance", "GOBIERNO DEL SERVICIO", "Capacidad recurrente significa reglas de operación, no disponibilidad ilimitada.", governance(source)))

    blocks.extend([
        section("ml-deliverables", "ENTREGABLES", "Qué recibe la empresa dentro del perímetro acordado.", ledger(source["deliverables"]), "ml-section--soft"),
        section("ml-perimeter", "PERÍMETRO", "Unidades que hacen administrable la contratación.", ledger(source["perimeter"])),
        section("ml-method", "MÉTODO", "Secuencia de trabajo y puntos de decisión.", timeline(source["method"]), "ml-section--ivory"),
        section("ml-requirements", "PARTICIPACIÓN DEL CLIENTE", "Información y decisiones necesarias para ejecutar bien el alcance.", ledger(source["requirements"])),
        section("ml-timeline", "CADENCIA Y TIEMPOS", "Hitos sujetos a información, decisiones y terceros aplicables.", timeline(source["timeline"]), "ml-section--soft"),
        section("ml-acceptance", "ACEPTACIÓN", "Cómo se verifica el cierre o la operación del alcance.", ledger(source["acceptance"])),
        section("ml-boundaries", "LÍMITES", "Lo que esta intervención no incluye ni puede garantizar.", f'<div class="ml-boundary"><h2>Perímetro y límites materiales</h2>{bullets(source["limits"])}</div>'),
    ])

    blocks.append(deep_layer(pilot, source, route_map))
    href = contact_href(pilot, source)
    blocks.append(
        f'<section class="ml-container ml-next-step" aria-labelledby="ml-next-title"><div><p class="ml-eyebrow">SIGUIENTE PASO</p><h2 id="ml-next-title">Convirtamos la necesidad en un alcance verificable.</h2><p>La propuesta final confirma perímetro, entregables, responsables, tiempos, honorarios y exclusiones.</p></div><a class="ml-btn" href="{e(href)}">Presentar necesidad →</a></section>'
    )
    return "".join(blocks)


def render(pilot: dict, source: dict, route_map: dict[str, str], base_url: str) -> str:
    family = pilot["family"]
    return f'''<!doctype html>
<html lang="es-CO">
{head(pilot, source, base_url)}
<body class="ml-surface ml-surface--{e(family)}" data-v8-pilot="{e(pilot['id'])}" data-source-catalog-id="{e(pilot['catalog_id'])}" data-source-title="{e(source.get('title', ''))}">
  <a class="ml-skip-link" href="#contenido">Saltar al contenido</a>
  <div class="ml-pilot-banner"><div class="ml-container"><strong>Piloto v8 no indexable.</strong> Esta superficie se genera en memoria y no sustituye la versión certificada v7.4.</div></div>
  <main id="contenido">
    {hero(pilot, source)}
    {body(pilot, source, route_map)}
  </main>
</body>
</html>
'''


def truth_strings(source: dict, preserve: list[str]) -> list[str]:
    values: list[str] = []
    for field in preserve:
        value = source[field]
        if isinstance(value, str):
            values.append(value)
            continue
        if not isinstance(value, list):
            continue
        if field == "related":
            for item in value:
                values.extend(str(part) for part in item[:3])
            continue
        for item in value:
            if isinstance(item, str):
                values.append(item)
            elif isinstance(item, list):
                values.extend(str(part) for part in item)
    return values


def validate_model(model: dict, route_contract: dict) -> tuple[list[dict], dict[str, str]]:
    if model.get("schema_version") != "1.0.0" or model.get("contract") != "v8-experience-model":
        fail("experience model inválido")
    if model.get("status") != "infrastructure":
        fail("W4.3 espera experience model status=infrastructure")
    truth_policy = model.get("truth_policy") or {}
    if truth_policy.get("presentation_overrides") != "explicit-exact-source-replacement":
        fail("W4.12 requiere presentation_overrides fail-closed")
    policy = model.get("pilot_policy") or {}
    required_policy = {
        "commit_target_html": False,
        "candidate_indexing": "noindex",
        "legacy_routes_unchanged": True,
        "new_portal_claims": False,
        "new_pricing_claims": False,
        "runtime_required": False,
        "rc02_meridiano_contratos_in_scope": False,
    }
    for key, expected in required_policy.items():
        if policy.get(key) != expected:
            fail(f"pilot_policy {key} debe ser {expected!r}")

    pilots = model.get("pilots") or []
    if [pilot.get("id") for pilot in pilots] != ["SO07", "PR02", "RC01"]:
        fail("W4.3 debe limitarse a SO07, PR02 y RC01")
    if {pilot.get("family") for pilot in pilots} != set(FAMILY_LABELS):
        fail("W4.3 debe probar exactamente solution, practice y recurring")

    rows = route_rows(route_contract)
    route_map = {item["current"]: item["target"] for item in rows}
    for pilot in pilots:
        if route_map.get(pilot["legacy_route"]) != pilot["target_route"]:
            fail(f"{pilot['id']}: experience model diverge de route contract")
    return pilots, route_map


def check() -> int:
    model = load_json(MODEL_PATH)
    route_contract = load_json(ROUTES_PATH)
    site = load_json(SITE_CONFIG)
    pilots, route_map = validate_model(model, route_contract)
    base_url = site["base_url"]
    preserve = model["truth_policy"]["preserve_material_fields"]
    if set(preserve) != REQUIRED_SOURCE_FIELDS:
        fail("preserve_material_fields debe coincidir con el contrato material W4.3")

    for pilot in pilots:
        raw_source = load_source(pilot)
        source = apply_presentation_overrides(pilot, raw_source)
        first = render(pilot, source, route_map, base_url)
        second = render(pilot, source, route_map, base_url)
        if first != second:
            fail(f"{pilot['id']}: render no determinista")
        if '<meta name="robots" content="noindex,follow">' not in first:
            fail(f"{pilot['id']}: piloto debe permanecer noindex")
        if "<form" in first.lower():
            fail(f"{pilot['id']}: piloto no puede crear segundo formulario")
        for forbidden in ("portal productivo", "firma electrónica incluida", "pago en línea", "decisión jurídica autónoma"):
            if forbidden in first.lower():
                fail(f"{pilot['id']}: claim prohibido {forbidden!r}")
        missing_truth = [value for value in truth_strings(source, preserve) if e(value) not in first]
        if missing_truth:
            fail(f"{pilot['id']}: truth parity efectiva incompleta; faltan {missing_truth[:5]}")
        if pilot["target_route"] not in first:
            fail(f"{pilot['id']}: canonical target ausente del render")
        # Todos los relacionados legacy conocidos deben traducirse al target v8.
        for item in source["related"]:
            resolved = resolve_related_href(pilot, item[3], route_map)
            if f'href="{e(resolved)}"' not in first:
                fail(f"{pilot['id']}: relacionado no resuelto {item[3]} -> {resolved}")

    print("RENDER V8 PILOT CHECK OK: SO07 + PR02 + RC01 source-driven, overrides explícitos fail-closed, deterministas, noindex y con truth parity efectiva completa en memoria.")
    return 0


def preview(pilot_id: str) -> int:
    model = load_json(MODEL_PATH)
    route_contract = load_json(ROUTES_PATH)
    site = load_json(SITE_CONFIG)
    pilots, route_map = validate_model(model, route_contract)
    pilot = next((item for item in pilots if item["id"] == pilot_id), None)
    if pilot is None:
        fail(f"piloto desconocido {pilot_id!r}")
    raw_source = load_source(pilot)
    source = apply_presentation_overrides(pilot, raw_source)
    print(render(pilot, source, route_map, site["base_url"]))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--preview", choices=["SO07", "PR02", "RC01"])
    args = parser.parse_args(argv)
    if args.check:
        return check()
    return preview(args.preview)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"RENDER V8 PILOT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

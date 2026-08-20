#!/usr/bin/env python3
"""Materializa Commercial Decision System v7.5 en la Home.

La capa compara cinco ofertas Legal Intelligence usando fuentes canónicas existentes.
No crea precios, capacidades, analytics ni JavaScript nuevo.
"""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/commercial-decision-system-v75.json"
ATTRIBUTION = ROOT / "assets/data/v7/commercial-evidence-v74.json"
TARGET = ROOT / "index.html"
STYLE = "assets/css/v7/commercial-decision-v75.css"
START = "<!-- COMMERCIAL-DECISION-V75:START -->"
END = "<!-- COMMERCIAL-DECISION-V75:END -->"
VALID_LIFECYCLE = {
    "prototype": {"version_prefix": "7.5.0-prototype"},
    "release-candidate": {"version_exact": "7.5.0"},
    "certified": {"version_exact": "7.5.0"},
}


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_lifecycle(data: dict) -> str:
    lifecycle = str(data.get("lifecycle", ""))
    version = str(data.get("version", ""))
    if lifecycle not in VALID_LIFECYCLE:
        raise RuntimeError(f"lifecycle v7.5 inválido: {lifecycle}")
    rule = VALID_LIFECYCLE[lifecycle]
    if "version_exact" in rule and version != rule["version_exact"]:
        raise RuntimeError(f"{lifecycle} debe declarar version {rule['version_exact']}")
    if "version_prefix" in rule and not version.startswith(rule["version_prefix"]):
        raise RuntimeError(f"{lifecycle} debe declarar versión con prefijo {rule['version_prefix']}")
    if data.get("baseline") != "7.4.0":
        raise RuntimeError("baseline v7.5 debe ser 7.4.0")
    return lifecycle


def attribution_map() -> dict[str, str]:
    data = load_json(ATTRIBUTION)
    if data.get("version") != "7.4.0" or data.get("status") != "readiness-disabled":
        raise RuntimeError("v7.5 requiere Commercial Evidence v7.4 certificado y readiness-disabled")
    if data.get("activation", {}).get("external_analytics") is not False:
        raise RuntimeError("v7.5 no puede operar sobre analytics externo activo")
    return {item["id"]: item["source"] for item in data.get("subjects", [])}


def load_catalog_offer(offer: dict) -> dict:
    path = ROOT / offer["source"]
    payload = load_json(path)
    if len(payload) != 1:
        raise RuntimeError(f"{offer['id']}: fuente canónica inválida")
    catalog_id, source = next(iter(payload.items()))
    if catalog_id != offer.get("catalog_id"):
        raise RuntimeError(f"{offer['id']}: catalog_id no coincide con la fuente")
    for field in ("modality", "duration", "audience", "question", "result", "deliverables", "limits"):
        if not source.get(field):
            raise RuntimeError(f"{offer['id']}: fuente sin {field}")
    deliverables = []
    for index in offer.get("deliverable_indices", []):
        if not isinstance(index, int) or index < 0 or index >= len(source["deliverables"]):
            raise RuntimeError(f"{offer['id']}: deliverable index inválido {index}")
        title, copy = source["deliverables"][index]
        deliverables.append((title, copy))
    limit_index = offer.get("limit_index")
    if not isinstance(limit_index, int) or limit_index < 0 or limit_index >= len(source["limits"]):
        raise RuntimeError(f"{offer['id']}: limit index inválido")
    return {
        "fit": source["question"],
        "result": source["result"],
        "modality": source["modality"],
        "duration": source["duration"],
        "audience": source["audience"],
        "deliverables": deliverables,
        "boundary": source["limits"][limit_index],
    }


def legal_desk_item() -> dict:
    source = load_json(ROOT / "assets/data/v7/home-commercial-clarity-v71.json")
    items = source.get("home", {}).get("installed", {}).get("items", [])
    matches = [item for item in items if item.get("name") == "Meridiano Legal Desk"]
    if len(matches) != 1:
        raise RuntimeError("v7.5: no se encontró una única fuente Meridiano Legal Desk en v7.1")
    return matches[0]


def load_legal_desk_offer(offer: dict) -> dict:
    item = legal_desk_item()
    meta = offer.get("meta", {})
    deliverables = offer.get("deliverables", [])
    if len(deliverables) != 3:
        raise RuntimeError("legal-desk: se requieren exactamente tres descriptores de operación")
    return {
        "fit": item["title"] + ". " + item["body"],
        "result": item["body"],
        "modality": meta["modality"],
        "duration": meta["duration"],
        "audience": meta["audience"],
        "deliverables": [(value, "") for value in deliverables],
        "boundary": item["outcome"],
    }


def load_offer(offer: dict) -> dict:
    return load_legal_desk_offer(offer) if offer["id"] == "legal-desk" else load_catalog_offer(offer)


def href_with_source(route: str, token: str) -> str:
    if "#" in route:
        base, fragment = route.split("#", 1)
        return f"{base}?source={token}#{fragment}"
    return f"{route}?source={token}"


def render_deliverables(items: list[tuple[str, str]]) -> str:
    rendered = []
    for title, copy in items:
        detail = f" — {e(copy)}" if copy else ""
        rendered.append(f"<li><b>{e(title)}</b>{detail}</li>")
    return "".join(rendered)


def render_offer(offer: dict, source: dict) -> str:
    token = offer["source_token"]
    route = href_with_source(offer["route"], token)
    contact = f"index.html?source={token}#contacto"
    return (
        f'<details class="v75-decision-offer" data-v75-offer="{e(offer["id"])}">'
        '<summary>'
        f'<span class="v75-decision-number">{e(offer["number"])}</span>'
        '<span class="v75-decision-name">'
        f'<small>{e(offer["intent"])}</small><strong>{e(offer["display_name"])}</strong></span>'
        f'<p class="v75-decision-fit">{e(source["fit"])}</p>'
        '<span class="v75-decision-meta">'
        f'<span><b>Modalidad:</b> {e(source["modality"])}</span>'
        f'<span><b>Horizonte:</b> {e(source["duration"])}</span>'
        f'<span><b>Dirigido a:</b> {e(source["audience"])}</span>'
        '</span><span class="v75-decision-toggle" aria-hidden="true"></span>'
        '</summary>'
        '<div class="v75-decision-body">'
        '<div class="v75-decision-result"><strong>Resultado esperado</strong>'
        f'<p>{e(source["result"])}</p></div>'
        '<div class="v75-decision-deliverables"><strong>Tres entregables o componentes para dimensionar</strong>'
        f'<ul>{render_deliverables(source["deliverables"])}</ul></div>'
        '<div class="v75-decision-boundary"><strong>Frontera material</strong>'
        f'<p>{e(source["boundary"])}</p></div>'
        '<div class="v75-decision-actions">'
        f'<a data-v75-primary href="{e(route)}">Ver ficha completa →</a>'
        '<a href="experiencia.html#intelligence">Ver escenario demo</a>'
        f'<a href="{e(contact)}">Presentar esta necesidad</a>'
        '</div></div></details>'
    )


def render_section(data: dict) -> str:
    allowed = attribution_map()
    offers = data.get("offers", [])
    if len(offers) != 5:
        raise RuntimeError("v7.5 debe comparar exactamente cinco ofertas")
    rendered = []
    for offer in offers:
        if allowed.get(offer["id"]) != offer.get("source_token"):
            raise RuntimeError(f"{offer['id']}: token no coincide con allowlist v7.4")
        rendered.append(render_offer(offer, load_offer(offer)))
    section = data["section"]
    return (
        f'{START}\n'
        '<section class="v6-section commercial-decision-v75" id="v75-commercial-decision" '
        'aria-labelledby="v75-commercial-decision-title" data-v75-commercial-decision="true">'
        '<div class="v6-container">'
        '<div class="v75-decision-intro"><div class="v6-section-head">'
        f'<p class="v6-eyebrow">{e(section["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v75-commercial-decision-title">{e(section["title"])}</h2>'
        f'<p class="v6-lead">{e(section["lead"])}</p></div>'
        f'<p class="v75-decision-guide">{e(section["guide"])}</p></div>'
        f'<div class="v75-decision-list">{"".join(rendered)}</div>'
        '<p class="v75-decision-footnote">La comparación resume fuentes canónicas existentes. La ficha completa y la propuesta gobiernan cantidades, perímetro, responsabilidades, exclusiones y cualquier componente adicional.</p>'
        '</div></section>\n'
        f'{END}'
    )


def strip_managed(text: str) -> str:
    if START not in text and END not in text:
        return text
    if text.count(START) != 1 or text.count(END) != 1:
        raise RuntimeError("v7.5: marcadores parciales o duplicados")
    pattern = re.compile(r"(?m)^[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"[ \t]*(?:\r?\n)?", re.S)
    return pattern.sub("", text, count=1)


def ensure_style(text: str) -> str:
    pattern = re.compile(rf'(?m)^[ \t]*<link rel="stylesheet" href="{re.escape(STYLE)}">[ \t]*(?:\r?\n)?')
    text = pattern.sub("", text)
    if "</head>" not in text:
        raise RuntimeError("index.html no contiene </head>")
    return text.replace("</head>", f'  <link rel="stylesheet" href="{STYLE}">\n</head>', 1)


def expected_content(data: dict) -> str:
    text = TARGET.read_text(encoding="utf-8")
    text = strip_managed(text)
    text = ensure_style(text)
    marker = data["insert_after_marker"]
    if text.count(marker) != 1:
        raise RuntimeError("v7.5: marker de inserción v7.1 no es único")
    return text.replace(marker, marker + "\n" + render_section(data), 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not CONTRACT.exists():
        return 0
    data = load_json(CONTRACT)
    lifecycle = validate_lifecycle(data)
    before = TARGET.read_text(encoding="utf-8")
    after = expected_content(data)
    if args.check:
        if before != after:
            raise RuntimeError("Commercial Decision System v7.5 presenta drift en index.html")
        print(f"COMMERCIAL DECISION V7.5 CHECK OK: Home sin drift ({lifecycle}).")
        return 0
    if before != after:
        TARGET.write_text(after, encoding="utf-8")
        print(f"COMMERCIAL DECISION V7.5 OK: Home materializada ({lifecycle}).")
    else:
        print(f"COMMERCIAL DECISION V7.5 OK: Home ya materializada ({lifecycle}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"COMMERCIAL DECISION V7.5 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

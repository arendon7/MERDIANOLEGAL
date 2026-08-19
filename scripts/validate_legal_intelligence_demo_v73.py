#!/usr/bin/env python3
"""Valida el Centro Demo Legal Intelligence v7.3 contra fuentes canónicas, boundaries y lifecycle."""
from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-demo-v73.json"
TARGET = ROOT / "experiencia.html"
STYLE = "assets/css/v7/legal-intelligence-demo-v73.css"
TAB_START = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-TAB:START -->"
TAB_END = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-TAB:END -->"
PANEL_START = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-PANEL:START -->"
PANEL_END = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-PANEL:END -->"
VALID_LIFECYCLE = {
    "demo-prototype": {"version_prefix": "7.3.0-prototype"},
    "release-candidate": {"version_exact": "7.3.0"},
    "certified": {"version_exact": "7.3.0"},
}


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def source_for(scenario: dict) -> dict:
    path = ROOT / scenario["source"]
    if not path.exists():
        fail(f"fuente inexistente: {scenario['source']}")
    payload = load_json(path)
    if len(payload) != 1:
        fail(f"fuente inválida: {scenario['source']}")
    catalog_id, source = next(iter(payload.items()))
    if catalog_id != scenario["catalog_id"]:
        fail(f"{scenario['id']}: catalog_id no coincide")
    return source


def link_exists(href: str) -> None:
    path_part, _, fragment = href.partition("#")
    path = ROOT / path_part
    if not path.exists():
        fail(f"link demo inexistente: {href}")
    if fragment and f'id="{fragment}"' not in path.read_text(encoding="utf-8"):
        fail(f"fragmento demo inexistente: {href}")


def validate_lifecycle(data: dict) -> str:
    status = str(data.get("status", ""))
    version = str(data.get("version", ""))
    if status not in VALID_LIFECYCLE:
        fail(f"status demo v7.3 inválido: {status}")
    lifecycle = VALID_LIFECYCLE[status]
    if "version_exact" in lifecycle and version != lifecycle["version_exact"]:
        fail(f"{status} debe declarar version {lifecycle['version_exact']}")
    if "version_prefix" in lifecycle and not version.startswith(lifecycle["version_prefix"]):
        fail(f"{status} debe declarar versión con prefijo {lifecycle['version_prefix']}")
    if data.get("baseline") != "7.2.0":
        fail("baseline demo v7.3 debe ser 7.2.0")
    return status


def main() -> int:
    if not CONTRACT.exists() or not TARGET.exists():
        fail("faltan contrato o experiencia.html")
    data = load_json(CONTRACT)
    status = validate_lifecycle(data)
    scenarios = data.get("scenarios", [])
    if len(scenarios) != 5:
        fail("deben existir exactamente cinco escenarios")
    if len({item["id"] for item in scenarios}) != 5:
        fail("ids de escenarios deben ser únicos")

    text = TARGET.read_text(encoding="utf-8")
    if text.count(f'href="{STYLE}"') != 1:
        fail("CSS demo v7.3 debe cargarse exactamente una vez")
    for start, end in ((TAB_START, TAB_END), (PANEL_START, PANEL_END)):
        if text.count(start) != 1 or text.count(end) != 1:
            fail(f"markers deben existir exactamente una vez: {start}")
    if text.count('data-target="intelligence"') != 1:
        fail("debe existir exactamente una pestaña Legal Intelligence")
    if text.count('data-panel="intelligence"') != 1:
        fail("debe existir exactamente un panel Legal Intelligence")
    if text.find(PANEL_START) > text.find("</main>"):
        fail("panel demo debe vivir dentro de main")

    match = re.search(re.escape(PANEL_START) + r"(.*?)" + re.escape(PANEL_END), text, flags=re.S)
    if not match:
        fail("no se pudo aislar panel demo")
    panel = unescape(match.group(1))

    for value in (data["title"], data["lead"]):
        if value not in panel:
            fail(f"texto contractual ausente: {value[:70]}")
    for piece in [item.strip() for item in data["boundary"].split("·") if item.strip()]:
        if piece not in panel:
            fail(f"boundary demo ausente: {piece}")

    if panel.count('data-li-demo-scenario="') != 5:
        fail("panel debe contener exactamente cinco cards")
    if panel.count('class="li-demo-badge-v73">DEMO</span>') != 5:
        fail("cada escenario debe mostrar badge DEMO")

    for scenario in scenarios:
        source = source_for(scenario)
        card_match = re.search(
            rf'<article class="li-demo-card-v73" data-li-demo-scenario="{re.escape(scenario["id"])}">(.*?)</article>',
            panel,
            flags=re.S,
        )
        if not card_match:
            fail(f"falta escenario: {scenario['id']}")
        card = card_match.group(1)
        required = [scenario["name"], scenario["problem"], scenario["artifact"], scenario["result"], scenario["boundary"]]
        required.extend(scenario["flow"])
        for section, index in scenario.get("metrics", []):
            items = source.get(section, [])
            if not isinstance(index, int) or index < 0 or index >= len(items):
                fail(f"índice canónico inválido: {scenario['id']} {section}[{index}]")
            required.extend(items[index])
        for value in required:
            if str(value) not in card:
                fail(f"{scenario['id']}: truth demo ausente: {str(value)[:70]}")
        if 'class="li-demo-badge-v73">DEMO</span>' not in card:
            fail(f"{scenario['id']}: falta badge DEMO")
        if scenario["href"] not in card:
            fail(f"{scenario['id']}: href contractual ausente")
        link_exists(scenario["href"])

    forbidden_panel = ["<form", "type=\"file\"", "type='file'", "Meridiano Counsel"] + data.get("forbidden", [])
    for forbidden in forbidden_panel:
        if forbidden.lower() in panel.lower():
            fail(f"claim/capability prohibida dentro del panel: {forbidden}")

    desk = re.search(r'data-li-demo-scenario="legal-desk">(.*?)</article>', panel, flags=re.S)
    if not desk:
        fail("falta card Legal Desk")
    desk_text = desk.group(1)
    for pattern in (
        r"\d+\s+LU\b",
        r"\bLU\s*(?:incluidas?|mensuales?|por\s+mes)\b",
        r"SLA\s*(?:de\s*)?\d+",
        r"\d+\s+horas\s+incluidas",
        r"\d+\s+solicitudes\s+incluidas",
        r"capacidad\s+incluida\s*:\s*\d+",
    ):
        if re.search(pattern, desk_text, flags=re.I):
            fail(f"Legal Desk demo inventa capacidad no aprobada: {pattern}")
    if "no fija volumen, canales, Legal Units, SLA o capacidad incluida" not in desk_text:
        fail("Legal Desk debe declarar explícitamente su boundary de capacidad")

    print(f"VALIDATE LEGAL INTELLIGENCE DEMO V7.3 OK: 5/5 escenarios source-driven, ficticios y capability-safe ({status}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE LEGAL INTELLIGENCE DEMO V7.3 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

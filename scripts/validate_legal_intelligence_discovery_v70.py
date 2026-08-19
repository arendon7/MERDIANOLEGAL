#!/usr/bin/env python3
"""Validate the Legal Intelligence public discovery layer without creating a parallel catalog."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_V70 = ROOT / "assets/data/v7/legal-intelligence-discovery-v70.json"
CONTRACT_V71 = ROOT / "assets/data/v7/home-commercial-clarity-v71.json"
ARCHITECTURE = ROOT / "assets/data/v7/legal-intelligence-architecture-v70.json"
HOME_START = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HOME:START -->"
HOME_END = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HOME:END -->"
HUB_START = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HUB:START -->"
HUB_END = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HUB:END -->"
SIX_ROUTE_HREFS = [
    "ordenar-riesgo-juridico-empresa.html",
    "direccion-juridica-externa-empresa.html",
    "gobernar-inteligencia-artificial-empresa.html",
    "preparar-empresa-para-inversion.html",
    "estructurar-proyecto-regulado.html",
    "ordenar-operacion-juridica.html",
]


def fail(message: str) -> None:
    raise SystemExit(f"Legal Intelligence discovery validation failed: {message}")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def validate_link(target: Path, href: str) -> None:
    path_part, _, fragment = href.partition("#")
    resolved = (target.parent / path_part).resolve()
    if not resolved.exists():
        fail(f"{target.relative_to(ROOT)}: link target does not exist: {href}")
    if fragment:
        target_text = resolved.read_text(encoding="utf-8")
        if f'id="{fragment}"' not in target_text:
            fail(f"{target.relative_to(ROOT)}: link fragment does not exist: {href}")


def architecture_labels() -> dict[str, dict]:
    data = json.loads(ARCHITECTURE.read_text(encoding="utf-8"))
    return {item["label"]: item for item in data.get("solutions", [])}


def surface_block(surface: dict, start: str, end: str) -> tuple[Path, str, str]:
    target = ROOT / surface["target"]
    if not target.exists():
        fail(f"missing target {surface['target']}")
    content = target.read_text(encoding="utf-8")
    if content.count(start) != 1 or content.count(end) != 1:
        fail(f"{surface['target']}: discovery markers must exist exactly once")
    if content.index(start) > content.index(surface["insert_before"]):
        fail(f"{surface['target']}: discovery block is after its insertion boundary")
    block = content.split(start, 1)[1].split(end, 1)[0]
    return target, block, content


def require_values(block: str, values: list[str], target: Path) -> None:
    for value in values:
        if esc(value) not in block:
            fail(f"{target.relative_to(ROOT)}: contract text drift: {value[:80]}")


def validate_v70_surface(surface: dict, start: str, end: str, expected_count: int) -> str:
    target, block, _ = surface_block(surface, start, end)
    required = [surface["eyebrow"], surface["title"], surface["lead"], surface["boundary"]]
    items = surface.get("paths", surface.get("areas", []))
    if len(items) != expected_count:
        fail(f"{surface['target']}: contract expects {expected_count} discovery items")
    for item in items:
        required.extend([item["title"], item["body"], item["href"], item["action"]])
        if "number" in item:
            required.extend([item["number"], item["label"]])
        validate_link(target, item["href"])
    require_values(block, required, target)
    return block


def validate_v71_home(surface: dict) -> str:
    target, block, content = surface_block(surface, HOME_START, HOME_END)
    if 'data-v71-commercial-clarity="home"' not in block:
        fail("home must expose the v7.1 commercial-clarity marker")
    if 'data-v7-legal-intelligence-discovery="home"' not in block:
        fail("v7 public discovery selector must remain backward compatible")

    required = [surface["eyebrow"], surface["title"], surface["lead"], surface["boundary"]]

    if "interventions" in surface:
        interventions = surface.get("interventions", [])
        if len(interventions) != 4:
            fail("v7.1 consolidated Home must expose exactly four intervention paths")
        for item in interventions:
            required.extend([
                item["number"], item["label"], item["title"], item["capabilities"],
                item["body"], item["result"], item["href"], item["action"]
            ])
            validate_link(target, item["href"])
        if block.count("data-v7-li-discovery=") != 4:
            fail("v7 backward-compatible discovery must still expose four child paths")
    else:
        modes = surface.get("modes", [])
        if len(modes) != 5:
            fail("legacy v7.1 Home must expose exactly five intervention modes")
        for item in modes:
            required.extend([item["number"], item["label"], item["title"], item["body"], item["result"]])
        intelligence = surface.get("intelligence") or {}
        required.extend([intelligence.get("eyebrow", ""), intelligence.get("title", ""), intelligence.get("lead", "")])
        paths = intelligence.get("paths", [])
        if len(paths) != 4:
            fail("legacy v7.1 Legal Intelligence must preserve four comprehension stages")
        for item in paths:
            required.extend([item["number"], item["label"], item["title"], item["body"], item["href"], item["action"]])
            validate_link(target, item["href"])

    installed = surface.get("installed") or {}
    required.extend([installed.get("eyebrow", ""), installed.get("title", ""), installed.get("lead", "")])
    installed_items = installed.get("items", [])
    expected_installed = 4 if "interventions" in surface else 5
    if len(installed_items) != expected_installed:
        fail(f"v7.1 Home must expose exactly {expected_installed} installed-capability explanations")
    for item in installed_items:
        required.extend([
            item["number"], item["name"], item["title"], item["body"], item["outcome"], item["href"], item["action"]
        ])
        validate_link(target, item["href"])

    for class_name in surface.get("suppress_redundant_sections", []):
        if f'class="v6-section {class_name}"' in content:
            fail(f"Home still contains redundant section after v7.1 consolidation: {class_name}")

    require_values(block, [value for value in required if value], target)
    return block


def validate_v71_hub(surface: dict) -> str:
    target, block, _ = surface_block(surface, HUB_START, HUB_END)
    if 'id="v71-commercial-clarity-hub"' not in block:
        fail("solutions hub must expose the v7.1 commercial-clarity anchor")
    required = [surface["eyebrow"], surface["title"], surface["lead"], surface["boundary"]]
    areas = surface.get("areas", [])
    if len(areas) != 3:
        fail("v7.1 hub must preserve exactly three Legal Intelligence capability areas")
    for item in areas:
        required.extend([item["title"], item["body"], item["href"], item["action"]])
        validate_link(target, item["href"])
    require_values(block, required, target)
    return block


def validate_common(data: dict, home_block: str, hub_block: str) -> None:
    labels = architecture_labels()
    allowed = {
        "Legal AI Diagnostic",
        "Legal AI Transformation",
        "Meridiano Legal Desk",
        "Contract Control",
        "Regulatory Control",
        "AI Governance 360",
        "Legal Engineering Studio",
    }
    for label in allowed:
        if label not in labels:
            fail(f"architecture no longer contains discovery label: {label}")
        if labels[label].get("status") == "not-public-product":
            fail(f"public discovery cannot expose not-public product: {label}")

    joined = home_block + "\n" + hub_block
    if "Meridiano Counsel" in joined:
        fail("future Meridiano Counsel must not appear in public discovery")

    hub_text = (ROOT / data["hub"]["target"]).read_text(encoding="utf-8")
    routes_start = hub_text.find('id="v6-solutions-routes"')
    if routes_start < 0:
        fail("solutions hub lost the canonical six-route section")
    route_tail = hub_text[routes_start:]
    for href in SIX_ROUTE_HREFS:
        if f'href="{href}"' not in route_tail:
            fail(f"solutions hub lost canonical route: {href}")

    if "séptima ruta" not in hub_block:
        fail("hub must explicitly preserve the six-route architecture")
    if "catálogo" not in hub_block:
        fail("hub must explicitly reject a parallel catalog")

    forbidden = [
        r"(?:saas|portal)\s+(?:incluido|disponible|productivo)",
        r"producto\s+tecnol[oó]gico\s+aut[oó]nomo",
        r"monitoreo\s+autom[aá]tico\s+universal",
    ]
    for pattern in forbidden:
        match = re.search(pattern, joined, flags=re.I)
        if match:
            prefix = joined[max(0, match.start() - 64):match.start()].lower()
            if "no " not in prefix and "sin " not in prefix and "no implica " not in prefix:
                fail(f"unsupported public discovery capability claim: {pattern}")


def main() -> None:
    if not ARCHITECTURE.exists():
        fail("missing Legal Intelligence architecture contract")

    contract = CONTRACT_V71 if CONTRACT_V71.exists() else CONTRACT_V70
    if not contract.exists():
        fail("missing discovery contract")
    data = json.loads(contract.read_text(encoding="utf-8"))

    if contract == CONTRACT_V71:
        if data.get("status") != "commercial-clarity-prototype":
            fail("v7.1 commercial clarity must remain prototype-only")
        principle = data.get("principle", "")
        if "seis rutas" not in principle or "catálogo paralelo" not in principle:
            fail("v7.1 principle must preserve six routes and reject a parallel catalog")
        home_block = validate_v71_home(data["home"])
        hub_block = validate_v71_hub(data["hub"])
    else:
        if data.get("status") != "public-discovery-prototype":
            fail("v7 discovery contract must remain prototype-only")
        if "no como un catálogo" not in data.get("principle", ""):
            fail("discovery principle must explicitly reject a parallel catalog")
        home_block = validate_v70_surface(data["home"], HOME_START, HOME_END, 4)
        hub_block = validate_v70_surface(data["hub"], HUB_START, HUB_END, 3)

    validate_common(data, home_block, hub_block)
    print(f"Legal Intelligence public discovery: PASS ({contract.name}, six routes preserved, capability truth protected)")


if __name__ == "__main__":
    main()

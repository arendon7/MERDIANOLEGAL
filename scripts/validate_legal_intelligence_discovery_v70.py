#!/usr/bin/env python3
"""Validate the v7 Legal Intelligence public discovery layer without creating a parallel catalog."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-discovery-v70.json"
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
    raise SystemExit(f"Legal Intelligence discovery v7 validation failed: {message}")


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


def validate_surface(surface: dict, start: str, end: str, expected_count: int) -> str:
    target = ROOT / surface["target"]
    if not target.exists():
        fail(f"missing target {surface['target']}")
    content = target.read_text(encoding="utf-8")
    if content.count(start) != 1 or content.count(end) != 1:
        fail(f"{surface['target']}: discovery markers must exist exactly once")
    if content.index(start) > content.index(surface["insert_before"]):
        fail(f"{surface['target']}: discovery block is after its insertion boundary")
    block = content.split(start, 1)[1].split(end, 1)[0]
    required = [surface["eyebrow"], surface["title"], surface["lead"], surface["boundary"]]
    items = surface.get("paths", surface.get("areas", []))
    if len(items) != expected_count:
        fail(f"{surface['target']}: contract expects {expected_count} discovery items")
    for item in items:
        required.extend([item["title"], item["body"], item["href"], item["action"]])
        if "number" in item:
            required.extend([item["number"], item["label"]])
        validate_link(target, item["href"])
    for value in required:
        if esc(value) not in block:
            fail(f"{surface['target']}: contract text drift: {value[:80]}")
    return block


def main() -> None:
    if not CONTRACT.exists() or not ARCHITECTURE.exists():
        fail("missing discovery or architecture contract")
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if data.get("status") != "public-discovery-prototype":
        fail("discovery contract must remain prototype-only")
    if "no como un catálogo" not in data.get("principle", ""):
        fail("discovery principle must explicitly reject a parallel catalog")

    home_block = validate_surface(data["home"], HOME_START, HOME_END, 4)
    hub_block = validate_surface(data["hub"], HUB_START, HUB_END, 3)

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
    if "no añade una séptima" not in hub_block:
        fail("hub must explicitly preserve the six-route architecture")

    forbidden = [
        r"(?:saas|portal)\s+(?:incluido|disponible|productivo)",
        r"producto\s+tecnol[oó]gico\s+aut[oó]nomo",
        r"monitoreo\s+autom[aá]tico\s+universal",
    ]
    for pattern in forbidden:
        match = re.search(pattern, joined, flags=re.I)
        if match:
            prefix = joined[max(0, match.start() - 32):match.start()].lower()
            if "no " not in prefix and "sin " not in prefix:
                fail(f"unsupported public discovery capability claim: {pattern}")

    print("Legal Intelligence public discovery v7: PASS (home + hub, six routes preserved, no parallel catalog or future product exposure)")


if __name__ == "__main__":
    main()

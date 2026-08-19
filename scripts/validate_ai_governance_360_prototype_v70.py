#!/usr/bin/env python3
"""Fail-closed validation for the AI Governance 360 v7 prototype."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/ai-governance-360-prototype-v70.json"
ROUTE_START = "<!-- AI-GOVERNANCE-360-V70:START -->"
ROUTE_END = "<!-- AI-GOVERNANCE-360-V70:END -->"
EXPECTED_DEEP_IDS = ["ai-governance-implementation", "ai-governance-readiness-managed"]


def fail(message: str) -> None:
    raise SystemExit(f"AI Governance 360 v7 validation failed: {message}")


def deep_markers(item: dict) -> tuple[str, str]:
    key = item["id"].upper().replace("-", "_")
    return f"<!-- AI-GOVERNANCE-360-V70-{key}:START -->", f"<!-- AI-GOVERNANCE-360-V70-{key}:END -->"


def escaped(value: str) -> str:
    return html.escape(value, quote=True)


def validate_links(target: Path, hrefs: list[str]) -> None:
    for href in hrefs:
        if href.startswith("../index.html?") or href.startswith("../index.html#"):
            continue
        path = href.split("#", 1)[0].split("?", 1)[0]
        if not (target.parent / path).resolve().exists():
            fail(f"{target.relative_to(ROOT)}: link target does not exist: {href}")


def validate_route(route: dict) -> None:
    target = ROOT / route["target"]
    if not target.exists():
        fail(f"missing route target {route['target']}")
    content = target.read_text(encoding="utf-8")
    if content.count(ROUTE_START) != 1 or content.count(ROUTE_END) != 1:
        fail("route markers must exist exactly once")
    if content.index(ROUTE_START) > content.index(route["insert_before"]):
        fail("AI Governance route block must appear before existing intervention routes")
    if content.count('data-v7-ai-governance-stage=') != 3:
        fail("AI Governance route must expose exactly three stages")
    preserved = ['data-experience-system="v6"', 'id="v6-solution-fit"', 'id="v6-solution-routes"', 'id="v6-solution-boundary"']
    for token in preserved:
        if token not in content:
            fail(f"route damaged preserved v6 contract: {token}")
    required = [route["eyebrow"], route["title"], route["lead"], route["boundary"]]
    hrefs = []
    for stage in route["stages"]:
        required.extend([stage["number"], stage["label"], stage["title"], stage["body"], stage["action"], stage["href"]])
        hrefs.append(stage["href"])
    block = content.split(ROUTE_START, 1)[1].split(ROUTE_END, 1)[0]
    for value in required:
        if escaped(value) not in block:
            fail(f"route contract drift: {value[:70]}")
    validate_links(target, hrefs)


def validate_source_support(item: dict) -> None:
    source_path = ROOT / item["catalog_source"]
    if not source_path.exists():
        fail(f"missing canonical source {item['catalog_source']}")
    source = source_path.read_text(encoding="utf-8").lower()
    if item["id"] == "ai-governance-implementation":
        terms = ["gobierno recurrente", "plan de implementación", "90 días", "protocolo de incidentes"]
    else:
        terms = ["diagnóstico, implementación o gobierno continuo", "gobierno recurrente", "proveedor", "incidentes"]
    missing = [term for term in terms if term.lower() not in source]
    if missing:
        fail(f"{item['id']}: canonical source no longer supports {missing}")


def validate_deep(item: dict) -> None:
    validate_source_support(item)
    target = ROOT / item["target"]
    if not target.exists():
        fail(f"missing deep target {item['target']}")
    content = target.read_text(encoding="utf-8")
    start, end = deep_markers(item)
    if content.count(start) != 1 or content.count(end) != 1:
        fail(f"{item['target']}: expected one complete AI Governance deep block")
    if content.index(start) > content.index(item["insert_before"]):
        fail(f"{item['target']}: deep block must appear before canonical deliverables")
    if content.index(start) < content.index('id="v6-result"'):
        fail(f"{item['target']}: deep block must follow canonical result")
    block = content.split(start, 1)[1].split(end, 1)[0]
    required = [item["eyebrow"], item["title"], item["lead"], item["boundary"]]
    hrefs = []
    for row in item["items"]:
        required.extend([row["number"], row["title"], row["body"]])
    continuity = item["continuity"]
    required.extend([continuity["title"], continuity["body"], continuity["action"], continuity["href"]])
    hrefs.append(continuity["href"])
    for value in required:
        if escaped(value) not in block:
            fail(f"{item['target']}: contract drift: {value[:70]}")
    validate_links(target, hrefs)


def validate_capability_boundaries(blocks: list[str]) -> None:
    forbidden = [
        r"auditor[ií]a\s+t[eé]cnica\s+(?:incluida|autom[aá]tica)",
        r"(?<!no )(?<!ni )certifica(?:mos|ci[oó]n)?\s+(?:el\s+)?cumplimiento",
        r"monitoreo\s+autom[aá]tico\s+universal",
        r"plataforma\s+(?:saas\s+)?(?:incluida|disponible)",
        r"garantiza(?:mos)?\s+ausencia\s+de\s+sesgos",
    ]
    joined = "\n".join(blocks)
    for pattern in forbidden:
        if re.search(pattern, joined, flags=re.I):
            fail(f"unsupported capability claim: {pattern}")


def main() -> None:
    if not CONTRACT.exists():
        fail("missing AI Governance 360 contract")
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if data.get("status") != "ai-governance-360-prototype":
        fail("contract must remain prototype-only")
    route = data.get("route") or {}
    deep = data.get("deep_offers") or []
    if [item.get("id") for item in deep] != EXPECTED_DEEP_IDS:
        fail("contract must contain exactly the approved implementation and readiness/managed deep offers")

    validate_route(route)
    for item in deep:
        validate_deep(item)

    blocks = []
    route_content = (ROOT / route["target"]).read_text(encoding="utf-8")
    blocks.append(route_content.split(ROUTE_START, 1)[1].split(ROUTE_END, 1)[0])
    for item in deep:
        content = (ROOT / item["target"]).read_text(encoding="utf-8")
        start, end = deep_markers(item)
        blocks.append(content.split(start, 1)[1].split(end, 1)[0])
    validate_capability_boundaries(blocks)
    print("AI Governance 360 v7 prototype: PASS (route + 2 deep offers, canonical support and capability boundaries preserved)")


if __name__ == "__main__":
    main()

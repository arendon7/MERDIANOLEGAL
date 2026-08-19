#!/usr/bin/env python3
"""Fail-closed validation for the Regulatory Control v7 prototype."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/regulatory-control-prototype-v70.json"
ROUTE_START = "<!-- REGULATORY-CONTROL-V70:START -->"
ROUTE_END = "<!-- REGULATORY-CONTROL-V70:END -->"
EXPECTED_DEEP_IDS = ["regulatory-control-implementation", "regulatory-control-managed"]


def fail(message: str) -> None:
    raise SystemExit(f"Regulatory Control v7 validation failed: {message}")


def deep_markers(item: dict) -> tuple[str, str]:
    key = item["id"].upper().replace("-", "_")
    return f"<!-- REGULATORY-CONTROL-V70-{key}:START -->", f"<!-- REGULATORY-CONTROL-V70-{key}:END -->"


def escaped(value: str) -> str:
    return html.escape(value, quote=True)


def validate_links(target: Path, hrefs: list[str]) -> None:
    for href in hrefs:
        if href.startswith("../index.html?") or href.startswith("../index.html#"):
            continue
        path = href.split("#", 1)[0].split("?", 1)[0]
        if not (target.parent / path).resolve().exists():
            fail(f"{target.relative_to(ROOT)}: link target does not exist: {href}")


def validate_route(route: dict) -> str:
    target = ROOT / route["target"]
    if not target.exists():
        fail(f"missing route target {route['target']}")
    content = target.read_text(encoding="utf-8")
    if content.count(ROUTE_START) != 1 or content.count(ROUTE_END) != 1:
        fail("route markers must exist exactly once")
    if content.index(ROUTE_START) > content.index(route["insert_before"]):
        fail("Regulatory Control route must appear before existing intervention routes")
    if content.count('data-v7-regulatory-stage=') != 3:
        fail("Regulatory Control route must expose exactly three stages")
    for token in ['data-experience-system="v6"', 'id="v6-solution-fit"', 'id="v6-solution-routes"', 'id="v6-solution-boundary"']:
        if token not in content:
            fail(f"route damaged preserved v6 contract: {token}")
    block = content.split(ROUTE_START, 1)[1].split(ROUTE_END, 1)[0]
    required = [route["eyebrow"], route["title"], route["lead"], route["boundary"]]
    hrefs = []
    for stage in route["stages"]:
        required.extend([stage["number"], stage["label"], stage["title"], stage["body"], stage["action"], stage["href"]])
        hrefs.append(stage["href"])
    for value in required:
        if escaped(value) not in block:
            fail(f"route contract drift: {value[:70]}")
    validate_links(target, hrefs)
    return block


def validate_source_support(item: dict) -> None:
    source_path = ROOT / item["catalog_source"]
    if not source_path.exists():
        fail(f"missing canonical source {item['catalog_source']}")
    source = source_path.read_text(encoding="utf-8").lower()
    if item["id"] == "regulatory-control-implementation":
        terms = ["matriz maestra de permisos", "ruta habilitante", "calendario regulatorio", "seguimiento mensual"]
    else:
        terms = ["responsable, secuencia, evidencia y vigencia", "acompañamiento de implementación", "hitos, permisos y obligaciones", "cambios regulatorios"]
    missing = [term for term in terms if term.lower() not in source]
    if missing:
        fail(f"{item['id']}: canonical source no longer supports {missing}")


def validate_deep(item: dict) -> str:
    validate_source_support(item)
    target = ROOT / item["target"]
    if not target.exists():
        fail(f"missing deep target {item['target']}")
    content = target.read_text(encoding="utf-8")
    start, end = deep_markers(item)
    if content.count(start) != 1 or content.count(end) != 1:
        fail(f"{item['target']}: expected one complete Regulatory Control block")
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
    return block


def validate_boundaries(blocks: list[str]) -> None:
    forbidden = [
        r"(?<!no )(?<!ni )garantiza(?:mos)?\s+(?:la\s+)?(?:licencia|licencias|permiso|permisos|decisi[oó]n|decisiones)",
        r"(?:incluye|ofrece|provee|proporciona)\s+(?:un\s+)?monitoreo\s+autom[aá]tico",
        r"(?:incluye|ofrece|provee|proporciona|garantiza)\s+(?:una\s+)?cobertura\s+universal\s+de\s+fuentes",
        r"plataforma\s+(?:saas\s+)?(?:incluida|disponible)",
        r"(?:incluye|ofrece|provee|proporciona)\s+(?:una\s+)?vigilancia\s+autom[aá]tica\s+universal",
    ]
    joined = "\n".join(blocks)
    for pattern in forbidden:
        if re.search(pattern, joined, flags=re.I):
            fail(f"unsupported regulatory capability claim: {pattern}")


def main() -> None:
    if not CONTRACT.exists():
        fail("missing Regulatory Control contract")
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if data.get("status") != "regulatory-control-prototype":
        fail("contract must remain prototype-only")
    deep = data.get("deep_offers") or []
    if [item.get("id") for item in deep] != EXPECTED_DEEP_IDS:
        fail("contract must contain exactly the approved implementation and managed deep offers")
    blocks = [validate_route(data["route"])]
    blocks.extend(validate_deep(item) for item in deep)
    validate_boundaries(blocks)
    print("Regulatory Control v7 prototype: PASS (route + 2 deep offers, canonical support and capability boundaries preserved)")


if __name__ == "__main__":
    main()

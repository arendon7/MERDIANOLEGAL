#!/usr/bin/env python3
"""Fail-closed validation for v7 Legal Intelligence deep-offer positioning."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-deep-offers-v70.json"
EXPECTED_IDS = ["legal-ai-transformation", "contract-control"]


def fail(message: str) -> None:
    raise SystemExit(message)


def markers(item: dict) -> tuple[str, str]:
    key = item["id"].upper().replace("-", "_")
    return f"<!-- LEGAL-INTELLIGENCE-V70-{key}:START -->", f"<!-- LEGAL-INTELLIGENCE-V70-{key}:END -->"


def visible(value: str) -> str:
    return html.escape(value, quote=True)


def validate_source_support(item: dict, source: str) -> None:
    if item["id"] == "legal-ai-transformation":
        required = ["Diagnosticar", "piloto", "Operación gestionada", "automatización"]
    else:
        required = ["Playbook", "inventario", "obligaciones", "Ciclo de vida"]
    missing = [term for term in required if term.lower() not in source.lower()]
    if missing:
        fail(f"{item['id']}: canonical source no longer supports positioning terms: {missing}")


def main() -> None:
    if not CONTRACT.exists():
        fail("Missing v7 deep-offer contract")
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if data.get("status") != "deep-offer-prototype":
        fail("v7 deep-offer contract must remain prototype-only")
    targets = data.get("targets", [])
    if [item.get("id") for item in targets] != EXPECTED_IDS:
        fail("v7 deep-offer contract must contain exactly the two approved prototype targets")

    for item in targets:
        target = ROOT / item["target"]
        source_path = ROOT / item["catalog_source"]
        if not target.exists() or not source_path.exists():
            fail(f"{item['id']}: target or canonical source missing")
        source = source_path.read_text(encoding="utf-8")
        validate_source_support(item, source)

        content = target.read_text(encoding="utf-8")
        start, end = markers(item)
        if content.count(start) != 1 or content.count(end) != 1:
            fail(f"{item['target']}: expected one complete v7 deep-offer block")
        block = content.split(start, 1)[1].split(end, 1)[0]
        if block.count(f'data-v7-deep-offer="{item["id"]}"') != 1:
            fail(f"{item['target']}: deep-offer identity mismatch")
        if content.find(start) > content.find(item["insert_before"]):
            fail(f"{item['target']}: v7 block must appear before canonical deliverables")
        if content.find(start) < content.find('id="v6-result"'):
            fail(f"{item['target']}: v7 block must follow the canonical result section")

        expected_strings = [item["eyebrow"], item["title"], item["lead"], item["boundary"]]
        for row in item["items"]:
            expected_strings.extend([row["number"], row["title"], row["body"]])
        nxt = item["next_step"]
        expected_strings.extend([nxt["title"], nxt["body"], nxt["action"], nxt["href"]])
        for text in expected_strings:
            if visible(text) not in block:
                fail(f"{item['target']}: contract text drift: {text[:60]}")

        forbidden_positive_claims = [
            r"incluye\s+(?:un\s+)?(?:clm|saas|portal)",
            r"(?:clm|saas|portal)\s+(?:ya\s+)?(?:disponible|productivo|incluido)",
            r"monitoreo\s+autom[aá]tico\s+(?:incluido|disponible)",
        ]
        for pattern in forbidden_positive_claims:
            if re.search(pattern, block, flags=re.I):
                fail(f"{item['target']}: unsupported software capability claim: {pattern}")

    print("v7 Legal Intelligence deep-offer prototypes: PASS (2/2, canonical support and capability boundaries preserved)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate the approved v7 Legal Intelligence prototype surfaces."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-prototype-v70.json"
DEEP_CONTRACT = ROOT / "assets/data/v7/legal-intelligence-deep-offers-v70.json"
DEEP_VALIDATOR = ROOT / "scripts/validate_legal_intelligence_deep_offers_v70.py"
START = "<!-- LEGAL-INTELLIGENCE-V70:START -->"
END = "<!-- LEGAL-INTELLIGENCE-V70:END -->"


def fail(message: str) -> None:
    raise SystemExit(f"v7 Legal Intelligence prototype validation failed: {message}")


def validate_deep_offers() -> None:
    if not DEEP_CONTRACT.exists():
        return
    if not DEEP_VALIDATOR.exists():
        fail("deep-offer contract exists without validator")
    completed = subprocess.run([sys.executable, str(DEEP_VALIDATOR)], cwd=ROOT, capture_output=True, text=True)
    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.returncode:
        fail(completed.stderr.strip() or completed.stdout.strip() or "deep-offer validation failed")


def main() -> None:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if data.get("status") != "route-prototype":
        fail("contract must remain route-prototype in this phase")

    target = ROOT / data["target"]
    if not target.exists():
        fail(f"missing target {data['target']}")
    content = target.read_text(encoding="utf-8")

    if content.count(START) != 1 or content.count(END) != 1:
        fail("prototype markers must exist exactly once")
    if content.index(START) > content.index(data["insert_before"]):
        fail("prototype must appear before the existing intervention routes")
    if 'id="v7-legal-intelligence"' not in content:
        fail("missing prototype section id")
    if content.count('data-v7-intervention=') != 3:
        fail("prototype must expose exactly three intervention modes")

    section = data["section"]
    required_text = [
        section["eyebrow"],
        section["title"],
        section["boundary"],
        section["engineering"]["title"],
        *[item["title"] for item in section["modes"]],
    ]
    for text in required_text:
        if text not in content:
            fail(f"missing expected rendered text: {text}")

    forbidden_claims = [
        "portal de clientes incluido",
        "plataforma SaaS disponible",
        "monitoreo automático universal",
        "Meridiano Counsel disponible",
        "IA autónoma sin supervisión",
    ]
    lower = content.lower()
    for claim in forbidden_claims:
        if claim.lower() in lower:
            fail(f"forbidden capability claim found: {claim}")

    preserved = [
        'data-experience-system="v6"',
        'id="v6-solution-fit"',
        'id="v6-solution-routes"',
        'id="v6-solution-boundary"',
    ]
    for token in preserved:
        if token not in content:
            fail(f"existing v6 route contract was damaged: {token}")

    for mode in section["modes"]:
        href = mode["href"]
        if href.startswith("../index.html?"):
            continue
        path = href.split("#", 1)[0].split("?", 1)[0]
        resolved = (target.parent / path).resolve()
        if not resolved.exists():
            fail(f"prototype link target does not exist: {href}")

    engineering_href = section["engineering"]["href"]
    engineering_path = engineering_href.split("#", 1)[0].split("?", 1)[0]
    if not (target.parent / engineering_path).resolve().exists():
        fail(f"Legal Engineering link target does not exist: {engineering_href}")

    print("v7 Legal Intelligence route prototype: PASS")
    validate_deep_offers()


if __name__ == "__main__":
    main()

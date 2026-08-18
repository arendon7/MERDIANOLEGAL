#!/usr/bin/env python3
"""Fail-closed validation for the v7 Legal Intelligence architecture contract.

This validator intentionally validates architecture/capability truth only. It does not
materialize public HTML and therefore does not change the certified v6.3 surface count.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-architecture-v70.json"

ALLOWED_STATUSES = {
    "sellable-service",
    "sellable-managed-service",
    "implementation-pattern",
    "sellable-service-family",
    "sellable-custom-service",
    "not-public-product",
}

REQUIRED_IDS = {
    "legal-ai-diagnostic",
    "legal-ai-transformation",
    "legal-desk",
    "contract-control",
    "regulatory-control",
    "ai-governance-360",
    "legal-engineering-studio",
    "meridiano-counsel",
}

NO_SAAS_CLAIM_IDS = {
    "legal-desk",
    "contract-control",
    "regulatory-control",
    "meridiano-counsel",
}


def fail(message: str) -> None:
    raise SystemExit(f"v7 Legal Intelligence validation failed: {message}")


def main() -> None:
    if not CONTRACT.exists():
        fail(f"missing contract: {CONTRACT.relative_to(ROOT)}")

    data = json.loads(CONTRACT.read_text(encoding="utf-8"))

    if data.get("version") != "7.0.0-draft":
        fail("version must remain 7.0.0-draft until a public v7 release is explicitly opened")
    if data.get("status") != "prototype":
        fail("architecture contract must remain prototype in this phase")
    if data.get("public_release_unchanged") != "6.3.0":
        fail("prototype must explicitly preserve public release 6.3.0")

    brand = data.get("brand") or {}
    if brand.get("master") != "Meridiano Legal":
        fail("Meridiano Legal must remain the master brand")
    if brand.get("family") != "Meridiano Legal Intelligence":
        fail("family label drifted")

    solutions = data.get("solutions")
    if not isinstance(solutions, list):
        fail("solutions must be a list")

    ids = [item.get("id") for item in solutions]
    if len(ids) != len(set(ids)):
        fail("solution ids must be unique")
    if set(ids) != REQUIRED_IDS:
        fail(f"solution ids must be exactly {sorted(REQUIRED_IDS)}; found {sorted(set(ids))}")

    for item in solutions:
        sid = item["id"]
        if item.get("status") not in ALLOWED_STATUSES:
            fail(f"{sid}: unsupported status {item.get('status')!r}")
        if not item.get("problem") or not item.get("transformation"):
            fail(f"{sid}: problem and transformation are mandatory")
        if item.get("software_product_claim") is not False:
            fail(f"{sid}: software_product_claim must remain false in prototype phase")

        sources = item.get("canonical_sources", [])
        if not isinstance(sources, list):
            fail(f"{sid}: canonical_sources must be a list")
        for source in sources:
            source_path = ROOT / source
            if not source_path.exists():
                fail(f"{sid}: canonical source does not exist: {source}")
            if not (
                source.startswith("catalog-products-v41/")
                or source.startswith("catalog-services-v42/")
            ):
                fail(f"{sid}: unsupported canonical source family: {source}")

        if sid != "meridiano-counsel" and not sources:
            fail(f"{sid}: at least one current canonical offer must support the solution")

        if sid in NO_SAAS_CLAIM_IDS and item.get("software_product_claim") is not False:
            fail(f"{sid}: may not claim an autonomous SaaS capability")

    counsel = next(item for item in solutions if item["id"] == "meridiano-counsel")
    if counsel.get("status") != "not-public-product":
        fail("Meridiano Counsel must remain not-public-product in prototype phase")
    if counsel.get("public_transactional_offer") is not False:
        fail("Meridiano Counsel cannot be a public transactional offer in prototype phase")
    if counsel.get("canonical_sources") != []:
        fail("Meridiano Counsel cannot borrow current offer truth to imply a certified product")

    legal_desk = next(item for item in solutions if item["id"] == "legal-desk")
    limits = " ".join(legal_desk.get("capability_limits", [])).lower()
    if "portal" not in limits or "sla" not in limits:
        fail("Legal Desk must preserve explicit portal and SLA capability boundaries")

    contract_control = next(item for item in solutions if item["id"] == "contract-control")
    if contract_control.get("status") != "implementation-pattern":
        fail("Contract Control must remain an implementation-pattern until product capability exists")

    regulatory_control = next(item for item in solutions if item["id"] == "regulatory-control")
    if regulatory_control.get("status") != "implementation-pattern":
        fail("Regulatory Control must remain an implementation-pattern until product capability exists")

    print("v7 Legal Intelligence architecture contract: PASS")


if __name__ == "__main__":
    main()

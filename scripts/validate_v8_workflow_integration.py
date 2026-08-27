#!/usr/bin/env python3
"""Validate committed Builder/Pages integration with immutable W4.7 provenance and fail-closed W5 overlay."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/workflow-integration-v80.json"
BUILD = ROOT / ".github/workflows/build-canonical.yml"
PAGES = ROOT / ".github/workflows/pages.yml"

W47_ARTIFACT = {
    "id": 9585803169,
    "digest": "sha256:05b5fffb77a40b9726c23536dfad28e5ea3b2151fed870c2746f31424ce18dd1",
    "builder_sha256": "6a002a1e6f9049bc9c98ad767c6aca9083c92f6847af3bc8ec78af534b5345ea",
    "pages_sha256": "3e3ab999ead2f094d7a0b26b2d430dd1bf5e414b224f9e6275f961000e25be01",
}
INTEGRATED_FILES = [
    ".github/workflows/build-canonical.yml",
    ".github/workflows/pages.yml",
]
REQUIRED_CHECKS = [
    "canonical_pipeline",
    "pages_trigger",
    "ci_governance",
    "builder_adapter_check",
    "pages_quality_dual_view",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str]) -> None:
    completed = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def require_markers(text: str, markers: list[str], label: str) -> None:
    missing = [marker for marker in markers if marker not in text]
    if missing:
        fail(f"{label} W5 overlay missing required markers: {missing}")


def validate_historical_record(contract: dict) -> None:
    if contract.get("schema_version") not in {"1.0.0", "1.1.0"}:
        fail("workflow integration schema_version must be 1.0.0 or 1.1.0")
    if contract.get("contract") != "v8-workflow-integration":
        fail("unexpected workflow integration contract")
    if contract.get("status") != "candidate" or contract.get("depends_on") != "v8-pipeline-integration":
        fail("workflow integration must remain candidate and depend on W4.7")
    if contract.get("w47_artifact") != W47_ARTIFACT:
        fail("immutable W4.7 artifact provenance was rewritten")
    if contract.get("integrated_files") != INTEGRATED_FILES:
        fail("integrated workflow allowlist changed unexpectedly")

    policy = contract.get("policy") or {}
    for key in (
        "exact_w47_bytes_required",
        "base_regeneration_parity_required",
        "canonical_pipeline_governance_required",
        "pages_trigger_governance_required",
        "ci_governance_required",
        "builder_adapter_check_required",
        "pages_quality_dual_view_required",
    ):
        if policy.get(key) is not True:
            fail(f"historical W4.8 policy {key} must remain true")
    for key in ("deploy_during_w48", "main_modified", "stable_modified", "version_bump", "canonical_handoff"):
        if policy.get(key) is not False:
            fail(f"historical W4.8 policy {key} must remain false")


def validate_w5_overlay(contract: dict, build: str, pages: str) -> bool:
    overlay = contract.get("w5_overlay")
    if overlay is None:
        return False
    if contract.get("schema_version") != "1.1.0":
        fail("W5 overlay requires schema_version 1.1.0")
    expected = {
        "enabled": True,
        "phase": "W5.0E-pre-persistence",
        "historical_w47_artifact_immutable": True,
        "current_exact_w47_bytes_required": False,
        "fail_closed": True,
        "allowed_integrated_files": INTEGRATED_FILES,
        "required_checks": REQUIRED_CHECKS,
        "production_merge": False,
        "production_deploy": False,
        "main_modified": False,
        "stable_modified": False,
        "version_bump": False,
        "canonical_handoff": False,
    }
    for key, value in expected.items():
        if overlay.get(key) != value:
            fail(f"w5_overlay.{key} must remain {value!r}; got {overlay.get(key)!r}")

    builder_markers = overlay.get("builder_required_markers")
    pages_markers = overlay.get("pages_required_markers")
    if not isinstance(builder_markers, list) or len(builder_markers) < 8:
        fail("W5 overlay builder marker allowlist is missing or unexpectedly small")
    if not isinstance(pages_markers, list) or len(pages_markers) < 6:
        fail("W5 overlay Pages marker allowlist is missing or unexpectedly small")
    if len(builder_markers) != len(set(builder_markers)) or len(pages_markers) != len(set(pages_markers)):
        fail("W5 overlay marker allowlists must not contain duplicates")
    require_markers(build, builder_markers, "Builder")
    require_markers(pages, pages_markers, "Pages")
    return True


def validate_workflow_structure(build: str, pages: str) -> None:
    if len(re.findall(r"(?m)^      - name:", build)) != 30:
        fail("integrated Builder must preserve exactly 30 named steps")
    for marker in (
        "MERIDIANO_V8_PIPELINE_COMPAT",
        "python3 scripts/apply_v8_builder_compat.py",
        "if: env.MERIDIANO_V8_PIPELINE_COMPAT != 'true'",
        "git push origin HEAD:main",
    ):
        if marker not in build:
            fail(f"integrated Builder missing {marker!r}")
    for marker in (
        "MERIDIANO_V8_PIPELINE_COMPAT",
        "python3 scripts/apply_v8_builder_compat.py --check",
        "python3 scripts/validate_v8_pipeline_compat.py",
        "uses: actions/deploy-pages@",
        "git push origin HEAD:refs/heads/stable --force",
    ):
        if marker not in pages:
            fail(f"integrated Pages missing {marker!r}")


def main() -> int:
    contract = load(CONTRACT)
    validate_historical_record(contract)
    build = BUILD.read_text(encoding="utf-8")
    pages = PAGES.read_text(encoding="utf-8")
    overlay_active = validate_w5_overlay(contract, build, pages)

    current_hashes = {BUILD: digest(BUILD), PAGES: digest(PAGES)}
    if not overlay_active:
        for path, expected in ((BUILD, W47_ARTIFACT["builder_sha256"]), (PAGES, W47_ARTIFACT["pages_sha256"])):
            actual = current_hashes[path]
            if actual != expected:
                fail(f"{path.relative_to(ROOT)} differs from certified W4.7 bytes without an approved W5 overlay: {actual} != {expected}")
    else:
        if current_hashes[BUILD] == W47_ARTIFACT["builder_sha256"] and current_hashes[PAGES] == W47_ARTIFACT["pages_sha256"]:
            fail("W5 overlay is enabled but both workflows still equal W4.7 bytes; overlay state is inconsistent")

    validate_workflow_structure(build, pages)
    run([sys.executable, "scripts/canonical_pipeline_v524.py", "validate"])
    run([sys.executable, "scripts/validate_pages_trigger_v511.py"])
    run([sys.executable, "scripts/validate_ci_v56.py"])
    run([sys.executable, "scripts/apply_v8_builder_compat.py", "--check"])
    run([sys.executable, "scripts/run_v8_pages_quality_compat.py"])

    if overlay_active:
        print(
            "VALIDATE V8 WORKFLOW INTEGRATION OK: immutable W4.7 provenance preserved; fail-closed W5.0E overlay validated; "
            f"current Builder={current_hashes[BUILD]} Pages={current_hashes[PAGES]}; canonical, release, CI, Builder-adapter and dual-view Pages governance pass."
        )
    else:
        print(
            "VALIDATE V8 WORKFLOW INTEGRATION OK: committed Builder/Pages exactly match W4.7 artifact and pass "
            "canonical, release, CI, Builder-adapter and dual-view Pages governance."
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 WORKFLOW INTEGRATION FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

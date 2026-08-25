#!/usr/bin/env python3
"""Validate the W4.8 committed Builder/Pages integration candidate."""
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


def main() -> int:
    contract = load(CONTRACT)
    if contract.get("schema_version") != "1.0.0" or contract.get("contract") != "v8-workflow-integration":
        fail("invalid W4.8 workflow integration contract")
    if contract.get("status") != "candidate" or contract.get("depends_on") != "v8-pipeline-integration":
        fail("W4.8 must remain candidate and depend on W4.7")

    artifact = contract.get("w47_artifact") or {}
    if artifact.get("id") != 9585803169:
        fail("unexpected W4.7 artifact id")
    if artifact.get("digest") != "sha256:05b5fffb77a40b9726c23536dfad28e5ea3b2151fed870c2746f31424ce18dd1":
        fail("unexpected W4.7 artifact digest")
    expected_hashes = {
        BUILD: artifact.get("builder_sha256"),
        PAGES: artifact.get("pages_sha256"),
    }
    for path, expected in expected_hashes.items():
        actual = digest(path)
        if actual != expected:
            fail(f"{path.relative_to(ROOT)} differs from certified W4.7 bytes: {actual} != {expected}")

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
            fail(f"policy {key} must remain true")
    for key in ("deploy_during_w48", "main_modified", "stable_modified", "version_bump", "canonical_handoff"):
        if policy.get(key) is not False:
            fail(f"policy {key} must remain false")

    build = BUILD.read_text(encoding="utf-8")
    pages = PAGES.read_text(encoding="utf-8")
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

    run([sys.executable, "scripts/canonical_pipeline_v524.py", "validate"])
    run([sys.executable, "scripts/validate_pages_trigger_v511.py"])
    run([sys.executable, "scripts/validate_ci_v56.py"])
    run([sys.executable, "scripts/apply_v8_builder_compat.py", "--check"])
    run([sys.executable, "scripts/run_v8_pages_quality_compat.py"])

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

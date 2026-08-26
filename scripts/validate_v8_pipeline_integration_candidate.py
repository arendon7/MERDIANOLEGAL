#!/usr/bin/env python3
"""Validate W4.7 integrated Builder/Pages candidate against production contracts."""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/pipeline-integration-v80.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(args: list[str], cwd: Path) -> None:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"candidate command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def validate_contract() -> None:
    contract = load(CONTRACT)
    if contract.get("schema_version") != "1.0.0" or contract.get("contract") != "v8-pipeline-integration":
        fail("invalid W4.7 integration contract")
    if contract.get("status") != "candidate" or contract.get("depends_on") != "v8-pipeline-compat":
        fail("W4.7 must remain candidate and depend on W4.6")
    builder = contract.get("builder") or {}
    if builder.get("named_step_count_must_remain") != 30:
        fail("Builder named-step invariant must remain 30")
    if builder.get("adapter") != "scripts/apply_v8_builder_compat.py":
        fail("unexpected Builder adapter")
    pages = contract.get("pages") or {}
    if pages.get("adapter_check") != "python3 scripts/apply_v8_builder_compat.py --check":
        fail("unexpected Pages adapter check")
    governance = contract.get("governance") or {}
    for key in (
        "canonical_pipeline_manifest_must_pass",
        "pages_trigger_validator_must_pass",
        "ci_validator_must_pass",
        "w46_compatibility_must_pass",
    ):
        if governance.get(key) is not True:
            fail(f"governance {key} must remain true")
    for key in (
        "production_workflows_modified_in_w47",
        "deploy_executed_in_w47",
        "main_modified",
        "stable_modified",
    ):
        if governance.get(key) is not False:
            fail(f"governance {key} must remain false")


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("--candidate-root", required=True)
    args = parser.parse_args(argv)
    candidate = Path(args.candidate_root).resolve()
    if candidate == ROOT.resolve():
        fail("candidate root must be disposable and distinct from active checkout")

    validate_contract()
    manifest_path = candidate / ".v8-pipeline-integration-candidate.json"
    if not manifest_path.exists():
        fail("integration materialization manifest is missing")
    manifest = load(manifest_path)
    if manifest.get("status") != "candidate" or manifest.get("production_checkout_touched") is not False:
        fail("integration materialization manifest is invalid")

    source_builder = (ROOT / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    source_pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    candidate_builder = (candidate / ".github/workflows/build-canonical.yml").read_text(encoding="utf-8")
    candidate_pages = (candidate / ".github/workflows/pages.yml").read_text(encoding="utf-8")

    if "MERIDIANO_V8_PIPELINE_COMPAT" in source_builder or "MERIDIANO_V8_PIPELINE_COMPAT" in source_pages:
        fail("W4.7 must not modify production workflows in the active branch")
    if "apply_v8_builder_compat.py" in source_builder or "apply_v8_builder_compat.py" in source_pages:
        fail("production workflows already contain W4.7 integration unexpectedly")

    for label, text in (("builder", candidate_builder), ("Pages", candidate_pages)):
        if "MERIDIANO_V8_PIPELINE_COMPAT" not in text or "apply_v8_builder_compat.py" not in text:
            fail(f"{label} candidate lacks v8 integration markers")

    named_steps = re.findall(r"(?m)^      - name:", candidate_builder)
    if len(named_steps) != 30:
        fail(f"integrated Builder must preserve exactly 30 named steps; found {len(named_steps)}")

    if "python3 scripts/apply_v8_builder_compat.py\n" not in candidate_builder:
        fail("Builder candidate does not invoke apply adapter")
    if "if: env.MERIDIANO_V8_PIPELINE_COMPAT != 'true'" not in candidate_builder:
        fail("Builder candidate does not guard direct legacy extension path")
    if "python3 scripts/apply_v8_builder_compat.py --check" not in candidate_pages:
        fail("Pages candidate does not invoke adapter idempotence check")
    if "python3 scripts/validate_v8_pipeline_compat.py" not in candidate_pages:
        fail("Pages candidate does not route Growth through strict projection")

    commit_anchor = "      - name: Commit canonical outputs\n"
    if commit_anchor not in source_builder or commit_anchor not in candidate_builder:
        fail("Builder commit anchor missing")
    if source_builder.split(commit_anchor, 1)[1] != candidate_builder.split(commit_anchor, 1)[1]:
        fail("W4.7 candidate modified Builder commit/push semantics")

    deploy_anchor = "  deploy:\n"
    if deploy_anchor not in source_pages or deploy_anchor not in candidate_pages:
        fail("Pages deploy anchor missing")
    if source_pages.split(deploy_anchor, 1)[1] != candidate_pages.split(deploy_anchor, 1)[1]:
        fail("W4.7 candidate modified Pages deploy or downstream release semantics")

    # The historical pipeline source of truth must continue accepting the
    # integrated workflows because its canonical direct command sequence remains
    # present as the fallback path.
    run([sys.executable, "scripts/canonical_pipeline_v524.py", "validate"], candidate)
    run([sys.executable, "scripts/validate_pages_trigger_v511.py"], candidate)
    run([sys.executable, "scripts/validate_ci_v56.py"], candidate)

    # Integrated candidate must be idempotent on the certified W4.6/W4.5 tree.
    run([sys.executable, "scripts/apply_v8_builder_compat.py", "--check"], candidate)
    run([sys.executable, "scripts/run_v8_pages_quality_compat.py"], candidate)

    print(
        "VALIDATE V8 PIPELINE INTEGRATION CANDIDATE OK: integrated Builder/Pages copies preserve historical "
        "pipeline governance, deploy/commit semantics and W4.6 dual-view idempotence."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PIPELINE INTEGRATION CANDIDATE FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

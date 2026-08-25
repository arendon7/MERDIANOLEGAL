#!/usr/bin/env python3
"""Validate W4.9 integrated Builder→Pages shadow execution contract.

This gate proves the shadow workflow may exercise the committed W4.8 integration
without acquiring any production mutation primitive: no main push, no Pages
artifact/deploy action and no stable ref move.
"""
from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/pipeline-shadow-v80.json"
WORKFLOW = ROOT / ".github/workflows/v80-integrated-pipeline-shadow.yml"


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(args: list[str]) -> None:
    completed = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def validate_contract(contract: dict) -> None:
    if contract.get("schema_version") != "1.0.0":
        fail("shadow schema_version must be 1.0.0")
    if contract.get("contract") != "v8-integrated-pipeline-shadow":
        fail("unexpected W4.9 shadow contract")
    if contract.get("status") != "candidate" or contract.get("depends_on") != "v8-workflow-integration":
        fail("W4.9 must remain candidate and depend on W4.8")
    if contract.get("stages") != ["builder-shadow", "pages-quality-shadow", "pages-artifact-shadow"]:
        fail("W4.9 stages changed unexpectedly")

    builder = contract.get("builder") or {}
    required_builder = {
        "real_git_worktree": True,
        "npm_lockfile_step": True,
        "adapter_mode": "apply",
        "git_diff_must_be_clean": True,
        "push": False,
    }
    for key, expected in required_builder.items():
        if builder.get(key) != expected:
            fail(f"builder.{key} must remain {expected!r}")

    quality = contract.get("pages_quality") or {}
    required_quality = {
        "consume_builder_artifact": True,
        "adapter_mode": "check",
        "dual_view_quality": True,
        "javascript_syntax": True,
        "tree_must_remain_immutable": True,
    }
    for key, expected in required_quality.items():
        if quality.get(key) != expected:
            fail(f"pages_quality.{key} must remain {expected!r}")

    artifact = contract.get("pages_artifact") or {}
    required_artifact = {
        "consume_quality_artifact": True,
        "html_count": 49,
        "local_http_smoke": True,
        "upload_pages_artifact": False,
        "deploy_pages": False,
        "stable_move": False,
    }
    for key, expected in required_artifact.items():
        if artifact.get(key) != expected:
            fail(f"pages_artifact.{key} must remain {expected!r}")

    for key, expected in (contract.get("protected") or {}).items():
        if expected is not False:
            fail(f"protected.{key} must remain false")


def validate_workflow(text: str) -> None:
    required_jobs = ["builder_shadow:", "pages_quality_shadow:", "pages_artifact_shadow:"]
    for job in required_jobs:
        if text.count(job) != 1:
            fail(f"shadow workflow must contain exactly one {job}")

    for marker in (
        "python3 scripts/apply_v8_builder_compat.py",
        "python3 scripts/apply_v8_builder_compat.py --check",
        "python3 scripts/run_v8_pages_quality_compat.py",
        "gh run download",
        "python3 -m http.server 8000 --bind 127.0.0.1",
        "w49-builder-shadow-site",
        "w49-pages-quality-shadow-site",
        "w49-integrated-pages-shadow",
    ):
        if marker not in text:
            fail(f"shadow workflow missing {marker!r}")

    forbidden = (
        "actions/upload-pages-artifact@",
        "actions/deploy-pages@",
        "git push origin HEAD:main",
        "git push origin HEAD:refs/heads/stable",
        "refs/heads/stable --force",
        "pages: write",
        "id-token: write",
        "contents: write",
    )
    for marker in forbidden:
        if marker in text:
            fail(f"shadow workflow contains forbidden production primitive {marker!r}")

    if "actions: read" not in text:
        fail("shadow workflow requires actions: read for artifact handoff")
    if "contents: read" not in text:
        fail("shadow workflow must stay contents: read")
    if re.search(r"(?m)^\s+environment:\s*$", text):
        fail("shadow workflow must not target a deployment environment")


def main() -> int:
    validate_contract(load(CONTRACT))
    if not WORKFLOW.exists():
        fail("W4.9 shadow workflow is missing")
    validate_workflow(WORKFLOW.read_text(encoding="utf-8"))

    # Re-prove the exact W4.8 committed integration before shadowing it.
    run([sys.executable, "scripts/validate_v8_workflow_integration.py"])
    print(
        "VALIDATE V8 PIPELINE SHADOW OK: three-stage artifact handoff is defined without main push, "
        "Pages deploy primitive or stable movement; W4.8 integration remains certified."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PIPELINE SHADOW FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

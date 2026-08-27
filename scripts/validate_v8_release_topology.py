#!/usr/bin/env python3
"""Validate v8 release/promotion topology without merging or deploying.

W4.10 recorded the production baseline that existed when the release topology
was designed. After a certified promotion, later candidates must start from the
new main==stable snapshot rather than pretending the historical SHA is still
production. This validator therefore preserves the historical contract while
resolving a fail-closed runtime baseline for descendant candidates.
"""
from __future__ import annotations

from fnmatch import fnmatch
from pathlib import Path
import json
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "assets/data/v8/release-topology-v80.json"
BUILD = ROOT / ".github/workflows/build-canonical.yml"
PAGES = ROOT / ".github/workflows/pages.yml"
RELEASE_WORKFLOW = ROOT / ".github/workflows/v80-release-topology-candidate.yml"
HISTORICAL_BASELINE = "86813813e29dd6b47105ba7fb6259630fcd9cb5b"


def fail(message: str) -> None:
    raise AssertionError(message)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git(*args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True
    )
    if check and completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout.strip()


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def require_mapping(actual: dict, expected: dict, label: str) -> None:
    for key, value in expected.items():
        if actual.get(key) != value:
            fail(f"{label}.{key} must remain {value!r}; got {actual.get(key)!r}")


def validate_contract(contract: dict) -> tuple[str, str]:
    """Validate the immutable W4.10 design-time record."""
    if contract.get("schema_version") != "1.0.0":
        fail("release topology schema_version must be 1.0.0")
    if contract.get("contract") != "v8-release-topology":
        fail("unexpected W4.10 contract")
    if contract.get("status") != "candidate":
        fail("W4.10 must remain candidate")
    if contract.get("depends_on") != "v8-integrated-pipeline-shadow":
        fail("W4.10 must depend on W4.9 shadow certification")

    baseline = contract.get("baseline") or {}
    recorded_main = baseline.get("main_sha")
    recorded_stable = baseline.get("stable_sha")
    if recorded_main != HISTORICAL_BASELINE:
        fail("W4.10 historical production baseline was rewritten")
    if recorded_stable != recorded_main or baseline.get("version") != "7.4.0":
        fail("W4.10 historical main/stable record must remain the certified v7.4.0 commit")

    require_mapping(
        contract.get("promotion") or {},
        {
            "topology": "single-linear-candidate-from-main",
            "main_must_be_ancestor": True,
            "candidate_must_not_be_behind_main": True,
            "production_merge": False,
            "production_deploy": False,
            "stable_move": False,
        },
        "promotion",
    )
    require_mapping(
        contract.get("builder") or {},
        {
            "trigger": "push-main",
            "candidate_paths_must_trigger": True,
            "expected_candidate_drift": False,
            "generated_commit_prefix": "build: sincroniza sitio público canónico",
            "generated_commit_is_fallback_only": True,
            "candidate_adapter_apply": True,
        },
        "builder",
    )
    require_mapping(
        contract.get("pages") or {},
        {
            "trigger": "workflow_run-builder-completed",
            "requires_builder_success": True,
            "ignores_generated_build_commit_run": True,
            "quality_checkout": "main",
            "deploy_after_quality": True,
            "live_smoke_after_deploy": True,
            "browser_after_deploy_and_smoke": True,
            "lighthouse_after_deploy_and_smoke": True,
            "stable_after_browser_and_lighthouse": True,
        },
        "pages",
    )
    for key, value in (contract.get("fail_closed") or {}).items():
        if value is not True:
            fail(f"fail_closed.{key} must remain true")
    for key, value in (contract.get("protected") or {}).items():
        if value is not False:
            fail(f"protected.{key} must remain false")
    return recorded_main, recorded_stable


def resolve_runtime_baseline(recorded_main: str, recorded_stable: str) -> tuple[str, str]:
    """Choose the certified baseline for the candidate currently being tested.

    Priority:
    1. explicit workflow env, which must be complete and main==stable;
    2. current origin/main==origin/stable when current main is an ancestor of HEAD;
    3. historical W4.10 record for old branches/tests.
    """
    env_main = os.environ.get("W410_BASELINE_SHA", "").strip()
    env_stable = os.environ.get("W410_ROLLBACK_SHA", "").strip()
    if bool(env_main) != bool(env_stable):
        fail("runtime release baseline env must provide both main and stable SHA")
    if env_main:
        if env_main != env_stable:
            fail("runtime candidate must start from certified main==stable")
        return env_main, env_stable

    head = git("rev-parse", "HEAD")
    origin_main = git("rev-parse", "refs/remotes/origin/main", check=False)
    origin_stable = git("rev-parse", "refs/remotes/origin/stable", check=False)
    if origin_main and origin_stable and origin_main == origin_stable and is_ancestor(origin_main, head):
        return origin_main, origin_stable

    return recorded_main, recorded_stable


def validate_git_topology(main_sha: str, stable_sha: str) -> list[str]:
    head = git("rev-parse", "HEAD")
    merge_base = git("merge-base", main_sha, head)
    if merge_base != main_sha:
        fail(f"candidate merge-base drifted: expected {main_sha}, got {merge_base}")
    if not is_ancestor(main_sha, head):
        fail("certified production main baseline is not an ancestor of candidate HEAD")

    ahead = int(git("rev-list", "--count", f"{main_sha}..{head}"))
    behind = int(git("rev-list", "--count", f"{head}..{main_sha}"))
    if ahead <= 0 or behind != 0:
        fail(f"candidate topology must be ahead-only; ahead={ahead}, behind={behind}")

    for ref, expected, label in (
        ("refs/remotes/origin/main", main_sha, "origin/main"),
        ("refs/remotes/origin/stable", stable_sha, "origin/stable"),
    ):
        actual = git("rev-parse", ref)
        if actual != expected:
            fail(f"{label} moved during candidate certification: {actual} != {expected}")

    changed = [
        line for line in git("diff", "--name-only", f"{main_sha}..{head}").splitlines()
        if line.strip()
    ]
    if not changed:
        fail("candidate contains no changes relative to certified production main")
    print(f"V8 release runtime baseline: main=stable={main_sha}; candidate={head}.")
    return changed


def builder_path_patterns(text: str) -> list[str]:
    match = re.search(
        r"(?ms)^\s{4}paths:\s*$\n(?P<body>.*?)(?=^\s{2}workflow_dispatch:)",
        text,
    )
    if not match:
        fail("cannot locate Builder push.paths allowlist")
    patterns: list[str] = []
    for raw in match.group("body").splitlines():
        m = re.match(r"^\s{6}-\s+(.+?)\s*$", raw)
        if m:
            patterns.append(m.group(1).strip("'\""))
    if not patterns:
        fail("Builder push.paths allowlist is empty")
    return patterns


def job_section(text: str, name: str) -> str:
    match = re.search(
        rf"(?ms)^  {re.escape(name)}:\s*$\n(?P<body>.*?)(?=^  [a-zA-Z0-9_]+:\s*$|\Z)",
        text,
    )
    if not match:
        fail(f"cannot locate Pages job {name}")
    return match.group("body")


def validate_builder(build: str, changed: list[str]) -> None:
    for marker in (
        "name: Build canonical public site",
        "branches: [main]",
        "if: ${{ !startsWith(github.event.head_commit.message, 'build') }}",
        "assets/data/v8/pipeline-compat-v80.json",
        "python3 scripts/apply_v8_builder_compat.py",
        'git commit -m "build: sincroniza sitio público canónico"',
        "git push origin HEAD:main",
    ):
        if marker not in build:
            fail(f"Builder release contract missing {marker!r}")

    patterns = builder_path_patterns(build)
    triggering = sorted(
        path for path in changed if any(fnmatch(path, pattern) for pattern in patterns)
    )
    if not triggering:
        fail("candidate diff would not trigger canonical Builder on push to main")
    print(
        f"V8 Builder trigger proof: {len(triggering)}/{len(changed)} changed files match push.paths."
    )


def validate_pages(pages: str) -> None:
    for marker in (
        'workflows: ["Build canonical public site"]',
        "types: [completed]",
        "github.event.workflow_run.conclusion == 'success'",
        "!startsWith(github.event.workflow_run.head_commit.message, 'build: sincroniza sitio público canónico')",
    ):
        if marker not in pages:
            fail(f"Pages workflow_run contract missing {marker!r}")

    quality = job_section(pages, "quality")
    deploy = job_section(pages, "deploy")
    smoke = job_section(pages, "live_smoke")
    browser = job_section(pages, "browser_e2e")
    lighthouse = job_section(pages, "lighthouse_quality")
    snapshot = job_section(pages, "snapshot")

    if "ref: main" not in quality:
        fail("Pages quality must validate current main")
    if "needs: quality" not in deploy:
        fail("deploy must depend on quality")
    if "needs: deploy" not in smoke:
        fail("live_smoke must depend on deploy")
    if "needs: [deploy, live_smoke]" not in browser:
        fail("browser_e2e must depend on deploy + live_smoke")
    if "needs: [deploy, live_smoke]" not in lighthouse:
        fail("lighthouse_quality must depend on deploy + live_smoke")
    if "needs: [browser_e2e, lighthouse_quality]" not in snapshot:
        fail("stable snapshot must depend on both browser_e2e and lighthouse_quality")

    stable_cmd = "git push origin HEAD:refs/heads/stable --force"
    if pages.count(stable_cmd) != 1 or stable_cmd not in snapshot:
        fail("stable movement must occur exactly once and only in snapshot")
    if "contents: write" not in snapshot or "actions: read" not in snapshot:
        fail("snapshot permissions changed unexpectedly")

    prefix = "build: sincroniza sitio público canónico"
    cases = {
        ("workflow_run", "success", "release: v8 candidate"): True,
        ("workflow_run", "failure", "release: v8 candidate"): False,
        ("workflow_run", "success", prefix): False,
        ("workflow_dispatch", "", ""): True,
    }
    for (event, conclusion, message), expected in cases.items():
        actual = event != "workflow_run" or (
            conclusion == "success" and not message.startswith(prefix)
        )
        if actual is not expected:
            fail(f"internal Pages trigger truth-table mismatch for {(event, conclusion, message)}")


def validate_certification_workflow() -> None:
    if not RELEASE_WORKFLOW.exists():
        fail("v8 release certification workflow is missing")
    text = RELEASE_WORKFLOW.read_text(encoding="utf-8")
    for marker in (
        "contents: read",
        "actions: read",
        "python3 scripts/validate_v8_release_topology.py",
        "python3 scripts/apply_v8_builder_compat.py",
        "python3 scripts/apply_v8_builder_compat.py --check",
        "python3 scripts/run_v8_pages_quality_compat.py",
        "production_merge_executed\": false",
        "production_deploy_executed\": false",
        "stable_moved\": false",
    ):
        if marker not in text:
            fail(f"v8 certification workflow missing {marker!r}")

    forbidden_literals = (
        "actions/upload-pages-artifact@",
        "actions/deploy-pages@",
        "pages: write",
        "id-token: write",
        "contents: write",
    )
    for marker in forbidden_literals:
        if marker in text:
            fail(f"v8 certification workflow contains forbidden primitive {marker!r}")
    if re.search(r"(?m)^\s+git\s+push\b", text):
        fail("v8 certification workflow must never execute git push")
    if re.search(r"(?m)^\s+environment:\s*$", text):
        fail("v8 certification workflow must not target a deployment environment")


def main() -> int:
    contract = load_json(CONTRACT_PATH)
    recorded_main, recorded_stable = validate_contract(contract)
    runtime_main, runtime_stable = resolve_runtime_baseline(recorded_main, recorded_stable)
    changed = validate_git_topology(runtime_main, runtime_stable)
    build = BUILD.read_text(encoding="utf-8")
    pages = PAGES.read_text(encoding="utf-8")
    validate_builder(build, changed)
    validate_pages(pages)
    validate_certification_workflow()

    print(
        "VALIDATE V8 RELEASE TOPOLOGY OK: historical W4.10 baseline preserved; current candidate is linear from certified runtime main==stable; Builder will trigger; Pages/stable remains fail-closed."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError, ValueError) as exc:
        print(f"VALIDATE V8 RELEASE TOPOLOGY FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

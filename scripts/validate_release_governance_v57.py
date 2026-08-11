#!/usr/bin/env python3
"""Validate Meridiano Legal v5.7 release-governance contracts.

Dependency-free by design: this validator must run on the stock Python runtime used
by the canonical quality gate and on scheduled governance checks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "release-governance-v57.json"
WORKFLOW_DIR = ROOT / ".github" / "workflows"
DEPENDABOT_PATH = ROOT / ".github" / "dependabot.yml"
PACKAGE_PATH = ROOT / "package.json"

ACTION_RE = re.compile(
    r"^\s*(?:-\s*)?uses:\s*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([^\s#]+)(?:\s*#\s*([^\n]+))?",
    re.MULTILINE,
)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def workflow_texts() -> dict[str, str]:
    files = sorted([*WORKFLOW_DIR.glob("*.yml"), *WORKFLOW_DIR.glob("*.yaml")])
    return {path.name: path.read_text(encoding="utf-8") for path in files}


def parse_actions(workflows: dict[str, str]):
    inventory = []
    for workflow_name, text in workflows.items():
        for match in ACTION_RE.finditer(text):
            inventory.append(
                {
                    "workflow": workflow_name,
                    "action": match.group(1),
                    "ref": match.group(2),
                    "comment": (match.group(3) or "").strip(),
                }
            )
    return inventory


def validate(policy: dict, workflows: dict[str, str]) -> tuple[list[str], dict]:
    errors: list[str] = []
    inventory = parse_actions(workflows)
    allowed_actions = policy["actions"]

    required_workflows = set(policy["required_workflows"])
    missing = sorted(required_workflows - set(workflows))
    for workflow in missing:
        fail(errors, f"workflow requerido ausente: {workflow}")

    for workflow_name, text in workflows.items():
        if "pull_request_target:" in text:
            fail(errors, f"{workflow_name}: pull_request_target está prohibido")
        if re.search(r"(?m)^\s*permissions:\s*write-all\s*$", text):
            fail(errors, f"{workflow_name}: permissions: write-all está prohibido")
        if "concurrency:" not in text:
            fail(errors, f"{workflow_name}: falta concurrency")
        jobs = len(re.findall(r"(?m)^\s{2}[A-Za-z0-9_-]+:\s*$", text.split("jobs:", 1)[1])) if "jobs:" in text else 0
        timeouts = len(re.findall(r"(?m)^\s+timeout-minutes:\s*\d+\s*$", text))
        if jobs and timeouts < jobs:
            fail(errors, f"{workflow_name}: hay jobs sin timeout-minutes ({timeouts}/{jobs})")

    for item in inventory:
        action = item["action"]
        ref = item["ref"]
        comment = item["comment"]
        expected = allowed_actions.get(action)
        if expected is None:
            fail(errors, f"{item['workflow']}: Action no inventariada: {action}@{ref}")
            continue
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            fail(errors, f"{item['workflow']}: {action} debe fijarse a SHA completo, no {ref}")
            continue
        if ref != expected["sha"]:
            fail(
                errors,
                f"{item['workflow']}: {action} SHA {ref} difiere de policy {expected['sha']}",
            )
        expected_major = f"v{expected['major']}"
        if expected_major not in comment.split():
            fail(errors, f"{item['workflow']}: {action}@{ref[:8]} debe documentar # {expected_major}")

    used_actions = {item["action"] for item in inventory}
    for action in sorted(set(allowed_actions) - used_actions):
        fail(errors, f"Action policy sin uso observado: {action}")

    for workflow_name, fragments in policy["permission_contracts"].items():
        text = workflows.get(workflow_name, "")
        for fragment in fragments:
            if fragment not in text:
                fail(errors, f"{workflow_name}: falta contrato de permiso `{fragment}`")

    pages = workflows.get("pages.yml", "")
    if "needs: [browser_e2e, lighthouse_quality]" not in pages:
        fail(errors, "pages.yml: stable debe conservar gate dual Browser + Lighthouse")
    if "python3 scripts/validate_release_governance_v57.py" not in pages:
        fail(errors, "pages.yml: falta validator v5.7 en quality gate")
    if "release-governance-v57.json" not in pages:
        fail(errors, "pages.yml: policy v5.7 no está incluida en el contrato de build/JSON")

    checkout_sha = allowed_actions["actions/checkout"]["sha"]
    page_checkout_count = pages.count(f"actions/checkout@{checkout_sha}")
    page_hardened_count = pages.count("persist-credentials: false")
    if page_checkout_count < 6:
        fail(errors, f"pages.yml: inventario inesperado de checkout ({page_checkout_count} < 6)")
    if page_hardened_count < 5:
        fail(errors, f"pages.yml: al menos 5 checkouts read-only deben desactivar credenciales ({page_hardened_count}/5)")

    hygiene = workflows.get("actions-hygiene.yml", "")
    if re.search(r"(?m)^\s{2}push:\s*$", hygiene):
        fail(errors, "actions-hygiene.yml: higiene no debe competir en cada push")
    for fragment in (
        "workflow_dispatch:",
        "schedule:",
        "Site Quality and Deploy",
        "status=in_progress",
        "status=queued",
    ):
        if fragment not in hygiene:
            fail(errors, f"actions-hygiene.yml: falta guardia `{fragment}`")

    graphify = workflows.get("graphify-knowledge.yml", "")
    runtime = policy["qa_runtime"]
    for fragment in (
        f'python-version: "{runtime["python"]}"',
        f'"uv=={runtime["uv"]}"',
        f'GRAPHIFY_VERSION: "{runtime["graphify"]}"',
    ):
        if fragment not in graphify:
            fail(errors, f"graphify-knowledge.yml: runtime/tool fuera de policy: {fragment}")

    if not DEPENDABOT_PATH.exists():
        fail(errors, ".github/dependabot.yml ausente")
        dependabot = ""
    else:
        dependabot = DEPENDABOT_PATH.read_text(encoding="utf-8")
        for fragment in (
            'package-ecosystem: "npm"',
            'package-ecosystem: "github-actions"',
            "version-update:semver-major",
            "open-pull-requests-limit:",
        ):
            if fragment not in dependabot:
                fail(errors, f"dependabot.yml: falta política controlada `{fragment}`")

    package = load_json(PACKAGE_PATH)
    expected_deps = policy["qa_dependencies"]
    actual_deps = package.get("devDependencies", {})
    if actual_deps != expected_deps:
        fail(errors, f"package.json: devDependencies QA difieren de policy: {actual_deps}")
    if package.get("engines", {}).get("node") != f">={runtime['node']}":
        fail(errors, f"package.json: engines.node debe ser >={runtime['node']}")
    for dependency, version in actual_deps.items():
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
            fail(errors, f"package.json: {dependency} debe estar fijada exactamente, no `{version}`")

    budgets = load_json(ROOT / policy["protected_invariants"]["lighthouse_budget_file"])
    budget_surfaces = budgets.get("surfaces") or budgets.get("pages") or []
    if isinstance(budget_surfaces, dict):
        budget_count = len(budget_surfaces)
    else:
        budget_count = len(budget_surfaces)
    expected_lighthouse = policy["protected_invariants"]["lighthouse_surfaces"]
    if budget_count and budget_count != expected_lighthouse:
        fail(errors, f"Lighthouse surfaces: {budget_count} != {expected_lighthouse}")

    action_counts = Counter(item["action"] for item in inventory)
    workflow_actions: dict[str, list[dict]] = defaultdict(list)
    for item in inventory:
        workflow_actions[item["workflow"]].append(
            {"action": item["action"], "sha": item["ref"], "version": item["comment"]}
        )

    report = {
        "schema": 1,
        "release": policy["version"],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "workflow_count": len(workflows),
        "action_usage_count": len(inventory),
        "action_counts": dict(sorted(action_counts.items())),
        "workflow_actions": dict(sorted(workflow_actions.items())),
        "qa_runtime": runtime,
        "qa_dependencies": actual_deps,
        "protected_invariants": policy["protected_invariants"],
        "supply_chain": {
            "all_remote_actions_sha_pinned": all(re.fullmatch(r"[0-9a-f]{40}", item["ref"]) for item in inventory),
            "dependabot_controlled": DEPENDABOT_PATH.exists() and "version-update:semver-major" in dependabot,
            "pull_request_target_absent": all("pull_request_target:" not in text for text in workflows.values()),
        },
    }
    return errors, report


def write_report(report: dict, report_dir: Path) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "release-health.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lines = [
        "# Meridiano Legal — Release health v5.7",
        "",
        f"- Estado: **{report['status'].upper()}**",
        f"- Workflows: **{report['workflow_count']}**",
        f"- Usos de Actions: **{report['action_usage_count']}**",
        f"- Actions remotas fijadas a SHA: **{'sí' if report['supply_chain']['all_remote_actions_sha_pinned'] else 'no'}**",
        f"- Dependabot controlado: **{'sí' if report['supply_chain']['dependabot_controlled'] else 'no'}**",
        f"- `pull_request_target` ausente: **{'sí' if report['supply_chain']['pull_request_target_absent'] else 'no'}**",
        "",
        "## Runtime QA",
        "",
        f"- Node: {report['qa_runtime']['node']}",
        f"- Python: {report['qa_runtime']['python']}",
        f"- uv: {report['qa_runtime']['uv']}",
        f"- Graphify: {report['qa_runtime']['graphify']}",
        "",
        "## Dependencias QA",
        "",
    ]
    for name, version in sorted(report["qa_dependencies"].items()):
        lines.append(f"- `{name}`: `{version}`")
    lines.extend(["", "## Actions", ""])
    for name, count in sorted(report["action_counts"].items()):
        lines.append(f"- `{name}`: {count} uso(s)")
    if report["errors"]:
        lines.extend(["", "## Errores", ""])
        lines.extend(f"- {error}" for error in report["errors"])
    (report_dir / "release-health.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-dir", type=Path)
    args = parser.parse_args()

    policy = load_json(POLICY_PATH)
    workflows = workflow_texts()
    errors, report = validate(policy, workflows)
    if args.report_dir:
        write_report(report, args.report_dir)

    if errors:
        print("RELEASE GOVERNANCE V5.7 FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "RELEASE GOVERNANCE V5.7 OK: "
        f"{report['workflow_count']} workflows, {report['action_usage_count']} usos de Actions, "
        "SHA pinning + permisos + dependencias + gates protegidos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

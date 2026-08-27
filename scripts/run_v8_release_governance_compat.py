#!/usr/bin/env python3
"""Execute Release Governance on the correct historical topology.

Before W5 Home persistence, this reproduces the existing disposable-checkout
sequence directly. After persistence, the same v5.7→v5.31 chain executes inside
the strict 46-page/v7.4 projection while the real v8 Home is read-only and is
validated separately at the end.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile

from v8_legacy_projection import ProjectionError, prepare_projection, persisted_home

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "governance-artifacts/v5.7"

TAIL_VALIDATORS = (
    "scripts/validate_offer_narrative_v522.py",
    "scripts/validate_contact_compression_v523.py",
    "scripts/validate_professional_authority_v525.py",
    "scripts/validate_integral_visual_v526.py",
    "scripts/validate_conversion_path_v528.py",
    "scripts/validate_funnel_trust_v529.py",
    "scripts/validate_offer_commercial_v530.py",
    "scripts/validate_decision_compression_v531.py",
)


def fail(message: str) -> None:
    raise RuntimeError(message)


def run(args: list[str], cwd: Path) -> None:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"Release Governance command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def governance_chain(cwd: Path) -> None:
    run([sys.executable, "scripts/apply_handoff_v517.py"], cwd)
    run([sys.executable, "scripts/validate_growth_v51.py"], cwd)
    run([sys.executable, "scripts/validate_quality_v55.py"], cwd)
    run([sys.executable, "scripts/validate_ci_v56.py"], cwd)
    run([
        sys.executable,
        "scripts/validate_release_governance_v57.py",
        "--report-dir",
        str(REPORT_DIR),
    ], cwd)
    run([sys.executable, "scripts/validate_pages_trigger_v511.py"], cwd)

    run([sys.executable, "scripts/sync_public_version.py"], cwd)
    run([sys.executable, "scripts/apply_production_v50.py"], cwd)
    run([sys.executable, "scripts/validate_production_v50.py"], cwd)
    run([sys.executable, "scripts/validate_visual_assets.py"], cwd)

    run([sys.executable, "scripts/apply_decision_v58.py"], cwd)
    run([sys.executable, "scripts/validate_decision_v58.py"], cwd)

    run([sys.executable, "scripts/apply_operations_v49.py"], cwd)
    run([sys.executable, "scripts/apply_decision_v58.py"], cwd)
    run([sys.executable, "scripts/apply_commercial_v59.py"], cwd)
    run([sys.executable, "scripts/validate_commercial_v59.py"], cwd)

    for apply_script, validate_script in (
        ("scripts/apply_conversion_v510.py", "scripts/validate_conversion_v510.py"),
        ("scripts/apply_engagement_v511.py", "scripts/validate_engagement_v511.py"),
        ("scripts/apply_proof_v512.py", "scripts/validate_proof_v512.py"),
        ("scripts/apply_commercial_brief_v513.py", "scripts/validate_commercial_brief_v513.py"),
        ("scripts/apply_recommendation_v514.py", "scripts/validate_recommendation_v514.py"),
        ("scripts/apply_decision_action_v515.py", "scripts/validate_decision_action_v515.py"),
    ):
        run([sys.executable, apply_script], cwd)
        run([sys.executable, validate_script], cwd)

    run([sys.executable, "scripts/apply_handoff_v517.py"], cwd)
    run([sys.executable, "scripts/validate_handoff_v517.py"], cwd)
    run([sys.executable, "scripts/apply_handoff_observability_v518.py"], cwd)
    run([sys.executable, "scripts/validate_handoff_observability_v518.py"], cwd)
    for validator in TAIL_VALIDATORS:
        run([sys.executable, validator], cwd)


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    if persisted_home(ROOT):
        with tempfile.TemporaryDirectory(prefix="meridiano-release-governance-w5-") as tmp:
            projected = Path(tmp) / "site"
            restored = prepare_projection(ROOT, projected)
            if not restored:
                fail("persisted Release Governance requires v7.4 Home restoration")
            governance_chain(projected)
        run([sys.executable, "scripts/validate_v8_public_tree.py"], ROOT)
        run([sys.executable, "scripts/validate_v8_pipeline_compat.py"], ROOT)
        run([sys.executable, "scripts/validate_v8_home_persisted.py", "--expect-state", "persisted"], ROOT)
        print("V8 RELEASE GOVERNANCE COMPAT OK: historical v5.7→v5.31 chain passed in strict v7.4 projection; real W5 Home remained protected.")
    else:
        governance_chain(ROOT)
        print("V8 RELEASE GOVERNANCE COMPAT OK: pre-persist historical governance behavior preserved directly.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ProjectionError) as exc:
        print(f"V8 RELEASE GOVERNANCE COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

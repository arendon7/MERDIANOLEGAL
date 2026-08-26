#!/usr/bin/env python3
"""Run Pages static quality for the W4.6 additive v8 candidate.

Closed-topology historical validators are certified by validate_v8_pipeline_compat
inside its 46-page projection. All additive-safe Pages validators run directly
against the real 49-page tree.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

# These are owned by the strict 46-page projection contract and MUST NOT be
# silently removed from coverage.
STRICT_PROJECTION_VALIDATORS = {
    "scripts/validate_experience_v60.py",
    "scripts/validate_experience_solutions_v60.py",
    "scripts/validate_growth_v51.py",
}

REAL_TREE_VALIDATORS = [
    "scripts/validate_site.py",
    "scripts/validate_static_catalog.py",
    "scripts/validate_commercial_v44.py",
    "scripts/validate_ux_v45.py",
    "scripts/validate_detail_ux_v46.py",
    "scripts/validate_editorial_ux_v47.py",
    "scripts/validate_quality_v48.py",
    "scripts/validate_operations_v49.py",
    "scripts/validate_production_v50.py",
    "scripts/validate_cro_v52.py",
    "scripts/validate_authority_v53.py",
    "scripts/validate_browser_v54.py",
    "scripts/validate_quality_v55.py",
    "scripts/validate_ci_v56.py",
    "scripts/validate_release_governance_v57.py",
    "scripts/validate_pages_trigger_v511.py",
    "scripts/validate_decision_v58.py",
    "scripts/validate_commercial_v59.py",
    "scripts/validate_conversion_v510.py",
    "scripts/validate_engagement_v511.py",
    "scripts/validate_proof_v512.py",
    "scripts/validate_commercial_brief_v513.py",
    "scripts/validate_recommendation_v514.py",
    "scripts/validate_decision_action_v515.py",
    "scripts/validate_handoff_v517.py",
    "scripts/validate_handoff_observability_v518.py",
    "scripts/validate_offer_narrative_v522.py",
    "scripts/validate_decision_flow.py",
    "scripts/validate_page_context.py",
    "scripts/validate_editorial_context.py",
    "scripts/validate_visual_assets.py",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def run(script: str) -> None:
    path = ROOT / script
    if not path.exists():
        fail(f"Pages validator missing: {script}")
    completed = subprocess.run(
        [sys.executable, script], cwd=ROOT, text=True, capture_output=True
    )
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"Pages validator failed: {script}\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def main() -> int:
    # This call proves W4.5 real-tree invariants and executes every strict
    # historical validator in the allowlisted 46-page projection.
    run("scripts/validate_v8_pipeline_compat.py")

    overlap = STRICT_PROJECTION_VALIDATORS.intersection(REAL_TREE_VALIDATORS)
    if overlap:
        fail(f"strict validator accidentally scheduled on real tree: {sorted(overlap)}")

    for validator in REAL_TREE_VALIDATORS:
        run(validator)

    # Re-run the compatibility contract after the full real-tree suite to prove
    # no validator mutated the candidate or its three additive targets.
    run("scripts/validate_v8_pipeline_compat.py")
    print(
        "RUN V8 PAGES QUALITY COMPAT OK: strict closed-topology validators passed in 46-page projection; "
        "additive-safe Pages validators passed on real 49-page tree."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"RUN V8 PAGES QUALITY COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

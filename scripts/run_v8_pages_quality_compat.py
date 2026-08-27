#!/usr/bin/env python3
"""Run Pages static quality for additive v8 and W5 persisted-Home candidates.

Pre-persist mode preserves the certified W4.6 split. Persisted mode moves every
historical Pages validator into the immutable 46-page/v7.4 projection and
validates the real W5 tree only with v8-aware contracts. Historical validator
source is never weakened or rematerialized.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile

from v8_legacy_projection import ProjectionError, prepare_projection, persisted_home

ROOT = Path(__file__).resolve().parents[1]

STRICT_PROJECTION_VALIDATORS = (
    "scripts/validate_experience_v60.py",
    "scripts/validate_experience_solutions_v60.py",
    "scripts/validate_growth_v51.py",
)

HISTORICAL_PAGES_VALIDATORS = (
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
)

REAL_W5_VALIDATORS = (
    "scripts/validate_v8_pipeline_compat.py",
    "scripts/validate_v8_public_tree.py",
    "scripts/validate_v8_home_shell.py",
    "scripts/validate_v8_navigation_shell.py",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def run(script: str, *, cwd: Path = ROOT, extra: tuple[str, ...] = ()) -> None:
    path = cwd / script
    if not path.exists():
        fail(f"Pages validator missing: {script} in {cwd}")
    completed = subprocess.run(
        [sys.executable, script, *extra], cwd=cwd, text=True, capture_output=True
    )
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"Pages validator failed: {script} {' '.join(extra)}\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def pre_persist() -> None:
    run("scripts/validate_v8_pipeline_compat.py")
    overlap = set(STRICT_PROJECTION_VALIDATORS).intersection(HISTORICAL_PAGES_VALIDATORS)
    if overlap:
        fail(f"strict validator accidentally scheduled on real tree: {sorted(overlap)}")
    for validator in HISTORICAL_PAGES_VALIDATORS:
        run(validator)
    run("scripts/validate_v8_pipeline_compat.py")
    print(
        "RUN V8 PAGES QUALITY COMPAT OK: pre-persist W4.6 split preserved; strict closed-topology validators "
        "passed in 46-page projection; additive-safe validators passed on real 49-page tree."
    )


def persisted() -> None:
    with tempfile.TemporaryDirectory(prefix="meridiano-pages-w5-legacy-") as tmp:
        projected = Path(tmp) / "site"
        restored = prepare_projection(ROOT, projected)
        if not restored:
            fail("persisted Pages mode requires legacy Home restoration in projection")
        for validator in (*STRICT_PROJECTION_VALIDATORS, *HISTORICAL_PAGES_VALIDATORS):
            run(validator, cwd=projected)

    for validator in REAL_W5_VALIDATORS:
        run(validator)
    run("scripts/validate_v8_home_persisted.py", extra=("--expect-state", "persisted"))
    print(
        "RUN V8 PAGES QUALITY COMPAT OK: persisted W5 Home validated on real 49-page tree; every historical "
        "Pages validator passed unchanged against the exact 46-page/v7.4 fixture projection."
    )


def main() -> int:
    if persisted_home(ROOT):
        persisted()
    else:
        pre_persist()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ProjectionError) as exc:
        print(f"RUN V8 PAGES QUALITY COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

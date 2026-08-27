#!/usr/bin/env python3
"""Run v5.22→v5.31 governance validators on their certified topology."""
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys
import tempfile

from v8_legacy_projection import ProjectionError, TARGETS, prepare_projection, persisted_home

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/pipeline-compat-v80.json"
VALIDATORS = (
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


def run(args: list[str], cwd: Path = ROOT) -> None:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        detail = (result.stdout + "\n" + result.stderr).strip()
        fail(f"command failed ({' '.join(args)}):\n{detail}")
    if result.stdout.strip():
        print(result.stdout.strip())


def is_final_v8() -> bool:
    present = [(ROOT / target).exists() for target in TARGETS]
    if not CONTRACT.exists() and not any(present):
        return False
    if not CONTRACT.exists() or not all(present):
        fail("partial v8 final candidate: contract and all three additive targets must coexist")
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    tree = payload.get("public_tree") or {}
    declared = tuple(route.lstrip("/") for route in tree.get("additive_targets") or [])
    if declared != TARGETS:
        fail(f"unexpected additive target allowlist: {declared}")
    if tree.get("legacy_html_count") != 46 or tree.get("candidate_html_count") != 49:
        fail("v8 topology contract must remain 46 legacy + 3 additive = 49")
    return True


def historical_direct() -> None:
    for validator in VALIDATORS:
        run([sys.executable, validator])
    print("V8 LEGACY TAIL COMPAT PASS: historical tree validated directly.")


def final_projection() -> None:
    with tempfile.TemporaryDirectory(prefix="meridiano-v8-legacy-tail-") as tmp:
        projected = Path(tmp) / "site"
        restored = prepare_projection(ROOT, projected)
        run([sys.executable, "scripts/apply_handoff_observability_v518.py"], cwd=projected)
        for validator in VALIDATORS:
            run([sys.executable, validator], cwd=projected)
        print(f"LEGACY TAIL projection PASS: persisted-home-restored={str(restored).lower()}.")

    run([sys.executable, "scripts/validate_v8_public_tree.py"])
    if persisted_home(ROOT):
        run([sys.executable, "scripts/validate_v8_home_persisted.py", "--expect-state", "persisted"])
    print("V8 LEGACY TAIL COMPAT PASS: v5.22→v5.31 validators passed unchanged in strict projection; real v8 tree remained protected.")


def main() -> int:
    if is_final_v8():
        final_projection()
    else:
        historical_direct()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ProjectionError, json.JSONDecodeError) as exc:
        print(f"V8 LEGACY TAIL COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Stage-aware compatibility runner for historical CI gates on v8/W5 candidates."""
from __future__ import annotations

import os
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

from v8_legacy_projection import ProjectionError, TARGETS, prepare_projection, persisted_home

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/pipeline-compat-v80.json"
HOME = ROOT / "index.html"
HANDOFF_OBSERVABILITY_SCRIPT = '<script defer src="handoff-observability-v518.js"></script>'
TELEMETRY_ANCHOR = '<script defer src="telemetry-v50.js"></script>'


def fail(message: str) -> None:
    raise RuntimeError(message)


def run(args: list[str], cwd: Path = ROOT) -> None:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def final_candidate() -> bool:
    target_presence = [(ROOT / relative).exists() for relative in TARGETS]
    contract_exists = CONTRACT.exists()
    if not contract_exists and not any(target_presence):
        return False
    if not contract_exists or not all(target_presence):
        fail("partial v8 candidate detected: contract and all three additive targets must appear together")
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    tree = payload.get("public_tree") or {}
    declared = tuple(route.lstrip("/") for route in (tree.get("additive_targets") or []))
    if declared != TARGETS:
        fail(f"v8 target allowlist drifted: {declared}")
    if tree.get("legacy_html_count") != 46 or tree.get("candidate_html_count") != 49:
        fail("v8 topology contract must remain 46 legacy + 3 additive = 49")
    return True


def governed_projection() -> Path | None:
    raw = os.environ.get("MERIDIANO_RELEASE_GOVERNANCE_ROOT", "").strip()
    if not raw:
        return None
    projected = Path(raw).resolve()
    if not projected.is_dir():
        fail(f"governed historical projection missing: {projected}")
    html_count = len(list(projected.rglob("*.html")))
    if html_count != 46:
        fail(f"governed historical projection must contain 46 HTML; found {html_count}")
    home = projected / "index.html"
    if not home.is_file():
        fail("governed historical projection lost index.html")
    text = home.read_text(encoding="utf-8")
    if 'data-experience-system="v6"' not in text or 'data-v8-home-candidate="persisted"' in text:
        fail("governed historical projection is not the certified v7.4/v6 Home topology")
    for relative in TARGETS:
        if (projected / relative).exists():
            fail(f"governed historical projection leaked additive target: {relative}")
    return projected


def projection() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    holder = tempfile.TemporaryDirectory(prefix="meridiano-historical-gate-")
    projected = Path(holder.name) / "site"
    try:
        restored = prepare_projection(ROOT, projected)
        print(f"HISTORICAL GATE projection prepared: persisted-home-restored={str(restored).lower()}.")
    except ProjectionError:
        holder.cleanup()
        raise
    return holder, projected


def normalize_real_handoff_observability_runtime() -> None:
    if persisted_home(ROOT):
        fail("legacy handoff normalization is forbidden on persisted W5 Home")
    text = HOME.read_text(encoding="utf-8")
    observed = text.count(HANDOFF_OBSERVABILITY_SCRIPT)
    if TELEMETRY_ANCHOR not in text:
        fail("governance replay lost telemetry-v50.js before v5.18 normalization")
    text = re.sub(
        r"(?m)^[ \t]*" + re.escape(HANDOFF_OBSERVABILITY_SCRIPT) + r"[ \t]*(?:\r?\n)?",
        "",
        text,
    )
    text = text.replace(TELEMETRY_ANCHOR, TELEMETRY_ANCHOR + "\n  " + HANDOFF_OBSERVABILITY_SCRIPT, 1)
    if text.count(HANDOFF_OBSERVABILITY_SCRIPT) != 1:
        fail("v5.18 runtime normalization did not converge to exactly one script reference")
    if text.find(TELEMETRY_ANCHOR) > text.find(HANDOFF_OBSERVABILITY_SCRIPT):
        fail("v5.18 runtime must remain ordered after telemetry-v50.js")
    HOME.write_text(text, encoding="utf-8")
    print(f"HISTORICAL GATE COMPAT v5.18 runtime normalized: {observed} replay reference(s) → 1.")


def mode_route_contract(is_final: bool) -> None:
    if not is_final:
        run([sys.executable, "scripts/validate_route_contract_v80.py"])
        return
    holder, projected = projection()
    try:
        run([sys.executable, "scripts/validate_route_contract_v80.py"], cwd=projected)
    finally:
        holder.cleanup()
    run([sys.executable, "scripts/validate_v8_pipeline_compat.py"])
    print("HISTORICAL GATE COMPAT route-contract PASS.")


def mode_pilot_infra(is_final: bool) -> None:
    if not is_final:
        run([sys.executable, "scripts/validate_route_contract_v80.py"])
        run([sys.executable, "scripts/validate_v8_pilot_infra.py"])
        return
    holder, projected = projection()
    try:
        run([sys.executable, "scripts/validate_route_contract_v80.py"], cwd=projected)
        run([sys.executable, "scripts/validate_v8_pilot_infra.py"], cwd=projected)
    finally:
        holder.cleanup()
    run([sys.executable, "scripts/validate_v8_public_tree.py"])
    print("HISTORICAL GATE COMPAT pilot-infra PASS.")


def mode_growth(is_final: bool) -> None:
    if is_final:
        run([sys.executable, "scripts/validate_v8_pipeline_compat.py"])
        print("HISTORICAL GATE COMPAT growth PASS: Growth v5.1 remains strict in legacy projection.")
    else:
        run([sys.executable, "scripts/validate_growth_v51.py"])


def mode_v6_apply(is_final: bool) -> None:
    if is_final:
        run([sys.executable, "scripts/apply_v8_builder_compat.py"])
        print("HISTORICAL GATE COMPAT v6-apply PASS: v6 materialized through certified Builder adapter.")
        return
    commands = [
        [sys.executable, "scripts/sync_public_version.py"],
        [sys.executable, "scripts/apply_experience_v60.py"],
        [sys.executable, "scripts/apply_experience_solutions_v60.py"],
        [sys.executable, "scripts/apply_experience_sectors_v60.py"],
        [sys.executable, "scripts/apply_experience_perspectives_v60.py"],
        [sys.executable, "scripts/apply_experience_final_v60.py"],
        [sys.executable, "scripts/apply_funnel_trust_v529.py"],
        [sys.executable, "scripts/normalize_experience_compat_v60.py"],
    ]
    for command in commands:
        run(command)
    if (ROOT / "assets/data/v6/fit-scope-clarity-v64.json").exists():
        run([sys.executable, "scripts/apply_fit_scope_clarity_v64.py"])


def mode_v6_closed_check(is_final: bool) -> None:
    if is_final:
        run([sys.executable, "scripts/apply_v8_builder_compat.py", "--check"])
        run([sys.executable, "scripts/validate_v8_pipeline_compat.py"])
        print("HISTORICAL GATE COMPAT v6-closed-check PASS.")
        return
    run([sys.executable, "scripts/validate_experience_v60.py"])
    run([sys.executable, "scripts/validate_experience_solutions_v60.py"])


def mode_handoff_observability(is_final: bool) -> None:
    if not is_final:
        run([sys.executable, "scripts/apply_handoff_observability_v518.py"])
        run([sys.executable, "scripts/validate_handoff_observability_v518.py"])
        return

    governed = governed_projection()
    if governed is not None:
        run([sys.executable, "scripts/apply_handoff_observability_v518.py"], cwd=governed)
        run([sys.executable, "scripts/validate_handoff_observability_v518.py"], cwd=governed)
        run([sys.executable, "scripts/validate_v8_public_tree.py"])
        if persisted_home(ROOT):
            run([sys.executable, "scripts/validate_v8_home_persisted.py", "--expect-state", "persisted"])
        print("HISTORICAL GATE COMPAT handoff-observability PASS: reused governed 46-page projection; real W5 tree remained untouched.")
        return

    holder, projected = projection()
    try:
        run([sys.executable, "scripts/apply_handoff_observability_v518.py"], cwd=projected)
        run([sys.executable, "scripts/validate_handoff_observability_v518.py"], cwd=projected)
    finally:
        holder.cleanup()

    if persisted_home(ROOT):
        run([sys.executable, "scripts/validate_v8_home_persisted.py", "--expect-state", "persisted"])
    else:
        normalize_real_handoff_observability_runtime()
        run([sys.executable, "scripts/validate_handoff_observability_v518.py"])
    run([sys.executable, "scripts/validate_v8_public_tree.py"])
    print("HISTORICAL GATE COMPAT handoff-observability PASS: historical mutation remained in projection; real W5 Home protected when persisted.")


def main() -> int:
    allowed = {"detect", "route-contract", "pilot-infra", "growth", "v6-apply", "v6-closed-check", "handoff-observability"}
    if len(sys.argv) != 2 or sys.argv[1] not in allowed:
        raise SystemExit("usage: run_v8_historical_gate_compat.py [detect|route-contract|pilot-infra|growth|v6-apply|v6-closed-check|handoff-observability]")
    mode = sys.argv[1]
    is_final = final_candidate()
    if mode == "detect":
        print("v8-final" if is_final else "historical")
        return 0
    {
        "route-contract": mode_route_contract,
        "pilot-infra": mode_pilot_infra,
        "growth": mode_growth,
        "v6-apply": mode_v6_apply,
        "v6-closed-check": mode_v6_closed_check,
        "handoff-observability": mode_handoff_observability,
    }[mode](is_final)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ProjectionError, json.JSONDecodeError) as exc:
        print(f"HISTORICAL GATE COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

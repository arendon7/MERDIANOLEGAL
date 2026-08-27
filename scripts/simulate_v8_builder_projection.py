#!/usr/bin/env python3
"""Run canonical v6 extensions in an ephemeral strict legacy projection.

For a persisted W5 Home, index.html is intentionally excluded from byte
comparison because the projection restores the immutable v7.4 fixture while the
real tree retains the source-driven v8 Home. All other legacy outputs must remain
byte-idempotent and the three additive targets remain protected.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

from v8_legacy_projection import ProjectionError, prepare_projection, persisted_home

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/pipeline-compat-v80.json"

BUILDER_COMMANDS = [
    [sys.executable, "scripts/sync_public_version.py"],
    [sys.executable, "scripts/apply_experience_v60.py"],
    [sys.executable, "scripts/apply_experience_solutions_v60.py"],
    [sys.executable, "scripts/apply_experience_sectors_v60.py"],
    [sys.executable, "scripts/apply_experience_perspectives_v60.py"],
    [sys.executable, "scripts/apply_experience_final_v60.py"],
    [sys.executable, "scripts/apply_funnel_trust_v529.py"],
    [sys.executable, "scripts/normalize_experience_compat_v60.py"],
]

POST_VALIDATORS = [
    "scripts/validate_experience_v60.py",
    "scripts/validate_experience_solutions_v60.py",
    "scripts/validate_experience_sectors_v60.py",
    "scripts/validate_experience_perspectives_v60.py",
    "scripts/validate_experience_final_v60.py",
    "scripts/validate_funnel_trust_v529.py",
    "scripts/validate_proof_v512.py",
    "scripts/validate_capability_truth_v521.py",
    "scripts/validate_editorial_context.py",
]

IGNORE_PARTS = {".git", "node_modules", "playwright-report", "test-results", "__pycache__"}


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(args: list[str], cwd: Path) -> None:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"Builder projection command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def comparable_files(root: Path, excluded: set[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative_path = path.relative_to(root)
        relative = relative_path.as_posix()
        if relative in excluded:
            continue
        if any(part in IGNORE_PARTS for part in relative_path.parts) or path.suffix == ".pyc":
            continue
        result[relative] = digest(path)
    return result


def main() -> int:
    contract = load(CONTRACT)
    projection = contract.get("legacy_projection") or {}
    if projection.get("builder_strategy") != "run-v6-in-projection-then-prove-real-legacy-equivalence":
        fail("unexpected W4.6 builder strategy")
    removals = set(projection.get("remove_before_strict_validation") or [])
    if len(removals) != 3:
        fail("Builder projection must remove exactly three additive targets")

    home_is_persisted = persisted_home(ROOT)
    protected = set(removals)
    if home_is_persisted:
        protected.add("index.html")
    real_protected_hashes = {relative: digest(ROOT / relative) for relative in protected}
    real_legacy = comparable_files(ROOT, protected)

    with tempfile.TemporaryDirectory(prefix="meridiano-w46-builder-") as tmp:
        projected = Path(tmp) / "site"
        restored = prepare_projection(ROOT, projected)
        if restored != home_is_persisted:
            fail("projection Home restoration state mismatch")

        for command in BUILDER_COMMANDS:
            run(command, projected)
        fit = projected / "assets/data/v6/fit-scope-clarity-v64.json"
        if fit.exists():
            run([sys.executable, "scripts/apply_fit_scope_clarity_v64.py"], projected)
        for validator in POST_VALIDATORS:
            run([sys.executable, validator], projected)
        if fit.exists():
            run([sys.executable, "scripts/validate_fit_scope_clarity_v64.py"], projected)
            run([sys.executable, "scripts/apply_fit_scope_clarity_v64.py", "--check"], projected)

        projected_excluded = {"index.html"} if home_is_persisted else set()
        projected_legacy = comparable_files(projected, projected_excluded)
        extra = sorted(set(projected_legacy) - set(real_legacy))
        missing = sorted(set(real_legacy) - set(projected_legacy))
        changed = sorted(
            path for path in set(real_legacy) & set(projected_legacy)
            if real_legacy[path] != projected_legacy[path]
        )
        if extra or missing or changed:
            fail(
                "Builder projection is not byte-idempotent against comparable real legacy tree; "
                f"extra={extra[:8]}, missing={missing[:8]}, changed={changed[:12]}"
            )

    for relative, expected in real_protected_hashes.items():
        if digest(ROOT / relative) != expected:
            fail(f"real protected surface mutated during Builder projection: {relative}")

    if home_is_persisted:
        run([sys.executable, "scripts/validate_v8_home_persisted.py", "--expect-state", "persisted"], ROOT)
    state = "persisted-home-excluded-from-legacy-equivalence" if home_is_persisted else "legacy-home"
    print(
        "SIMULATE V8 BUILDER PROJECTION OK: v6 canonical extensions and validators pass on 46-page projection; "
        f"comparable legacy output equals real tree byte-for-byte; protected surfaces untouched; state={state}."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ProjectionError, json.JSONDecodeError) as exc:
        print(f"SIMULATE V8 BUILDER PROJECTION FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

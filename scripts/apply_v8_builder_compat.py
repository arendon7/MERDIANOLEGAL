#!/usr/bin/env python3
"""Apply the canonical legacy extension chain without touching additive v8 targets.

W4.7 production-adapter candidate:
- materialize inside an ephemeral 46-page legacy projection;
- allow only historically public/generated outputs to differ;
- in apply mode, copy those generated legacy outputs back to the real tree;
- in --check mode, fail if the real legacy tree is not already canonical;
- never delete or overwrite the three additive v8 targets.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/pipeline-compat-v80.json"

COMMANDS = [
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

ALLOWED_EXACT = {
    "index.html",
    "firma.html",
    "perspectivas.html",
    "experiencia.html",
    "demo.html",
    "demo.js",
    "404.html",
    "aviso-legal.html",
    "privacidad.html",
    "terminos.html",
    "catalog-home-v32.js",
    "decision-flow.js",
    "site-v3.js",
    "page-context.js",
    "sitemap.xml",
    "robots.txt",
    "runtime-config.js",
    "site-status.json",
    "manifest.webmanifest",
    "CNAME",
}
ALLOWED_PREFIXES = (
    "assets/",
    "servicios/",
    "productos/",
    "perspectivas/",
    "sectores/",
    "soluciones/",
)
IGNORE_PARTS = {".git", "node_modules", "playwright-report", "test-results", "__pycache__"}


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], cwd: Path) -> None:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"projection command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def inventory(root: Path, excluded: set[str]) -> dict[str, str]:
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


def allowed_output(relative: str) -> bool:
    return relative in ALLOWED_EXACT or relative.startswith(ALLOWED_PREFIXES)


def additive_targets(contract: dict) -> set[str]:
    projection = contract.get("legacy_projection") or {}
    if projection.get("builder_strategy") != "run-v6-in-projection-then-prove-real-legacy-equivalence":
        fail("W4.7 requires certified W4.6 builder strategy")
    removals = set(projection.get("remove_before_strict_validation") or [])
    expected = {
        "soluciones/sistema-contractual-empresarial.html",
        "practicas/corporativo-societario-gobierno.html",
        "servicios-continuos/direccion-juridica-externa.html",
    }
    if removals != expected:
        fail(f"unexpected additive target allowlist: {sorted(removals)}")
    return removals


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if legacy outputs would change")
    args = parser.parse_args(argv)

    contract = load(CONTRACT)
    removals = additive_targets(contract)
    target_hashes = {relative: digest(ROOT / relative) for relative in removals}
    before = inventory(ROOT, removals)

    with tempfile.TemporaryDirectory(prefix="meridiano-w47-builder-") as tmp:
        projected = Path(tmp) / "site"
        shutil.copytree(
            ROOT,
            projected,
            ignore=shutil.ignore_patterns(".git", "node_modules", "playwright-report", "test-results", "__pycache__"),
        )
        for relative in removals:
            target = projected / relative
            if not target.exists():
                fail(f"projection target missing before removal: {relative}")
            target.unlink()
        if len(list(projected.rglob("*.html"))) != 46:
            fail("projection must contain exactly 46 HTML before legacy materialization")

        for command in COMMANDS:
            run(command, projected)
        fit = projected / "assets/data/v6/fit-scope-clarity-v64.json"
        if fit.exists():
            run([sys.executable, "scripts/apply_fit_scope_clarity_v64.py"], projected)
        for validator in POST_VALIDATORS:
            run([sys.executable, validator], projected)
        if fit.exists():
            run([sys.executable, "scripts/validate_fit_scope_clarity_v64.py"], projected)
            run([sys.executable, "scripts/apply_fit_scope_clarity_v64.py", "--check"], projected)

        after = inventory(projected, set())
        missing = sorted(set(before) - set(after))
        changed = sorted(path for path in set(before) & set(after) if before[path] != after[path])
        extra = sorted(set(after) - set(before))
        if missing:
            fail(f"legacy Builder projection attempted deletions: {missing[:12]}")
        illegal = sorted(path for path in changed + extra if not allowed_output(path))
        if illegal:
            fail(f"legacy Builder projection changed non-output paths: {illegal[:16]}")

        pending = changed + extra
        if args.check and pending:
            fail(f"canonical legacy outputs are stale: {pending[:20]}")

        if not args.check:
            for relative in pending:
                source = projected / relative
                destination = ROOT / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)

    for relative, expected in target_hashes.items():
        if digest(ROOT / relative) != expected:
            fail(f"additive v8 target was mutated: {relative}")

    run([sys.executable, "scripts/validate_v8_pipeline_compat.py"], ROOT)
    mode = "CHECK" if args.check else "APPLY"
    print(
        f"APPLY V8 BUILDER COMPAT {mode} OK: legacy projection canonical; "
        f"{len(pending)} legacy output(s) {'pending' if args.check else 'synchronized'}; 3 v8 targets untouched."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"APPLY V8 BUILDER COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

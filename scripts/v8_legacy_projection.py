#!/usr/bin/env python3
"""Shared strict legacy projection for v8/W5 candidate validation.

The real candidate may persist a v8 Home while historical v5/v6 validators still
require the certified v7.4 Home. This module creates an isolated 46-page view by
removing only the three additive W4 targets and, when needed, restoring the exact
v7.4 Home fixture. It never writes to the source tree.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LEGACY_HOME_FIXTURE = Path("tests/fixtures/v8/home-v74.fixture")
LEGACY_HOME_GIT_BLOB = "4508e7a8fa298d4c19704cfb6269ca4488b1622d"
TARGETS = (
    "soluciones/sistema-contractual-empresarial.html",
    "practicas/corporativo-societario-gobierno.html",
    "servicios-continuos/direccion-juridica-externa.html",
)
IGNORE_PATTERNS = (".git", "node_modules", "playwright-report", "test-results", "__pycache__")
PERSISTED_MARKER = 'data-v8-home-candidate="persisted"'


class ProjectionError(RuntimeError):
    pass


def persisted_home(root: Path = ROOT) -> bool:
    home = root / "index.html"
    if not home.is_file():
        raise ProjectionError("index.html missing")
    return PERSISTED_MARKER in home.read_text(encoding="utf-8")


def validate_legacy_fixture(root: Path = ROOT) -> Path:
    fixture = root / LEGACY_HOME_FIXTURE
    if not fixture.is_file():
        raise ProjectionError(f"legacy Home fixture missing: {LEGACY_HOME_FIXTURE}")
    text = fixture.read_text(encoding="utf-8")
    for required in (
        'data-experience-system="v6"',
        'data-experience-surface="home"',
        "Web pública v7.4.0",
        'id="contact-form"',
    ):
        if required not in text:
            raise ProjectionError(f"legacy Home fixture lost certified marker: {required}")
    if PERSISTED_MARKER in text or 'data-experience-system="v8"' in text:
        raise ProjectionError("legacy Home fixture contains v8 persisted markers")
    completed = subprocess.run(
        ["git", "hash-object", str(fixture)], cwd=root, text=True, capture_output=True
    )
    if completed.returncode:
        raise ProjectionError(f"cannot hash legacy Home fixture: {completed.stderr.strip()}")
    observed = completed.stdout.strip()
    if observed != LEGACY_HOME_GIT_BLOB:
        raise ProjectionError(
            f"legacy Home fixture drifted: git blob {observed} != {LEGACY_HOME_GIT_BLOB}"
        )
    return fixture


def prepare_projection(source_root: Path, projected: Path) -> bool:
    """Create strict historical topology and return whether Home restoration occurred."""
    fixture = validate_legacy_fixture(source_root)
    if projected.exists():
        shutil.rmtree(projected)
    projected.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        source_root,
        projected,
        ignore=shutil.ignore_patterns(*IGNORE_PATTERNS),
    )
    for relative in TARGETS:
        path = projected / relative
        if not path.is_file():
            raise ProjectionError(f"projection target missing before removal: {relative}")
        path.unlink()

    restored = persisted_home(source_root)
    if restored:
        shutil.copyfile(fixture, projected / "index.html")

    count = len(list(projected.rglob("*.html")))
    if count != 46:
        raise ProjectionError(f"historical projection must contain exactly 46 HTML; found {count}")
    projected_home = (projected / "index.html").read_text(encoding="utf-8")
    if 'data-experience-system="v6"' not in projected_home:
        raise ProjectionError("historical projection did not expose certified v6 Home")
    if PERSISTED_MARKER in projected_home:
        raise ProjectionError("historical projection leaked persisted v8 Home")
    return restored


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, help="Create a strict projection at this path")
    args = parser.parse_args()
    fixture = validate_legacy_fixture(ROOT)
    state = "persisted" if persisted_home(ROOT) else "legacy"
    if args.output:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        restored = prepare_projection(ROOT, output)
        print(
            f"V8 LEGACY PROJECTION OK: output={output}; html=46; "
            f"home-restored={str(restored).lower()}; fixture-blob={LEGACY_HOME_GIT_BLOB}."
        )
    else:
        print(
            f"V8 LEGACY PROJECTION CONTRACT OK: fixture={fixture.relative_to(ROOT)}; "
            f"real-home={state}; fixture-blob={LEGACY_HOME_GIT_BLOB}."
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ProjectionError as exc:
        print(f"V8 LEGACY PROJECTION CONTRACT FAIL: {exc}")
        raise SystemExit(1)

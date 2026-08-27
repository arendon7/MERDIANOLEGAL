#!/usr/bin/env python3
"""W4.6+ pipeline compatibility gate for additive v8 targets and W5 persisted Home.

Historical validators with closed topologies remain strict. They execute against
an ephemeral 46-page projection; if the real Home has transitioned to W5.0E,
the projection restores the exact certified v7.4 Home fixture first. The real
49-page candidate is always validated independently.
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
VERSION = ROOT / "version.json"
HOME = ROOT / "index.html"
SITEMAP = ROOT / "sitemap.xml"


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(args: list[str], cwd: Path = ROOT) -> None:
    completed = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if completed.returncode:
        detail = (completed.stdout + "\n" + completed.stderr).strip()
        fail(f"command failed ({' '.join(args)}):\n{detail}")
    if completed.stdout.strip():
        print(completed.stdout.strip())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def validate_contract(contract: dict) -> list[str]:
    if contract.get("schema_version") != "1.0.0":
        fail("pipeline compat schema_version must be 1.0.0")
    if contract.get("contract") != "v8-pipeline-compat":
        fail("unexpected pipeline compatibility contract")
    if contract.get("status") != "candidate":
        fail("pipeline compatibility requires status=candidate")
    if contract.get("baseline_version") != "7.4.0":
        fail("pipeline baseline must remain 7.4.0")

    tree = contract.get("public_tree") or {}
    if tree.get("legacy_html_count") != 46 or tree.get("candidate_html_count") != 49:
        fail("topology must remain 46 legacy + 3 additive = 49")
    targets = tree.get("additive_targets") or []
    expected = [
        "/soluciones/sistema-contractual-empresarial.html",
        "/practicas/corporativo-societario-gobierno.html",
        "/servicios-continuos/direccion-juridica-externa.html",
    ]
    if targets != expected:
        fail(f"additive targets differ from certified W4.5 set: {targets}")

    projection = contract.get("legacy_projection") or {}
    if projection.get("strict_validators") != [
        "scripts/validate_experience_v60.py",
        "scripts/validate_experience_solutions_v60.py",
        "scripts/validate_growth_v51.py",
    ]:
        fail("strict validator allowlist changed unexpectedly")
    if projection.get("builder_strategy") != "run-v6-in-projection-then-prove-real-legacy-equivalence":
        fail("builder projection strategy changed unexpectedly")

    policy = contract.get("candidate_policy") or {}
    required_policy = {
        "targets_noindex": True,
        "targets_in_sitemap": False,
        "targets_in_home_navigation": False,
        "legacy_self_canonical": True,
        "version_bump": False,
        "canonical_handoff": False,
        "pages_deploy": False,
        "stable_move": False,
        "rc02_meridiano_contratos": False,
    }
    for key, expected_value in required_policy.items():
        if policy.get(key) is not expected_value:
            fail(f"candidate_policy {key} must remain {expected_value!r}")

    pipeline = contract.get("pipeline_policy") or {}
    required_pipeline = {
        "legacy_validators_remain_strict": True,
        "candidate_validated_additively": True,
        "builder_runs_in_legacy_projection": True,
        "builder_must_not_rewrite_v8_targets": True,
        "pages_artifact_may_include_noindex_targets": True,
        "production_activation_requires_later_wave": True,
    }
    for key, expected_value in required_pipeline.items():
        if pipeline.get(key) is not expected_value:
            fail(f"pipeline_policy {key} must remain {expected_value!r}")
    return targets


def validate_real_candidate(targets: list[str]) -> dict[str, str]:
    version = load(VERSION).get("version")
    if version != "7.4.0":
        fail(f"candidate must not bump public version; got {version!r}")

    html_files = sorted(ROOT.rglob("*.html"))
    if len(html_files) != 49:
        fail(f"real candidate must contain exactly 49 HTML; found {len(html_files)}")

    home = HOME.read_text(encoding="utf-8")
    sitemap = SITEMAP.read_text(encoding="utf-8")
    hashes: dict[str, str] = {}
    for route in targets:
        relative = route.lstrip("/")
        path = ROOT / relative
        if not path.exists():
            fail(f"missing additive target {route}")
        html = path.read_text(encoding="utf-8")
        if '<meta name="robots" content="noindex,follow">' not in html:
            fail(f"{route} must remain noindex,follow")
        if route in sitemap:
            fail(f"{route} must remain outside sitemap")
        if route in home:
            fail(f"{route} target route must remain outside public Home/navigation before SEO handoff")
        hashes[relative] = sha256(path)

    run([sys.executable, "scripts/validate_v8_public_tree.py"])
    run([sys.executable, "scripts/validate_v8_contrast_tokens.py"])
    run([sys.executable, "scripts/render_v8_pilot.py", "--check"])
    if persisted_home(ROOT):
        run([sys.executable, "scripts/validate_v8_home_persisted.py", "--expect-state", "persisted"])
    return hashes


def validate_legacy_projection(contract: dict, target_hashes: dict[str, str]) -> None:
    projection = contract.get("legacy_projection") or {}
    validators = projection.get("strict_validators") or []
    removals = projection.get("remove_before_strict_validation") or []
    if sorted(removals) != sorted(target_hashes):
        fail("legacy projection removal set must equal the three additive targets")

    with tempfile.TemporaryDirectory(prefix="meridiano-w46-legacy-") as tmp:
        legacy_root = Path(tmp) / "site"
        restored = prepare_projection(ROOT, legacy_root)
        for validator in validators:
            run([sys.executable, validator], cwd=legacy_root)
        print(f"PIPELINE legacy projection PASS: home-restored={str(restored).lower()}.")

    for relative, expected in target_hashes.items():
        actual = sha256(ROOT / relative)
        if actual != expected:
            fail(f"strict legacy projection mutated real target {relative}")


def main() -> int:
    contract = load(CONTRACT)
    targets = validate_contract(contract)
    target_hashes = validate_real_candidate(targets)
    validate_legacy_projection(contract, target_hashes)
    state = "persisted-home" if persisted_home(ROOT) else "legacy-home"
    print(
        "VALIDATE V8 PIPELINE COMPAT OK: real 49-page candidate + strict 46-page legacy projection; "
        f"closed historical topologies remain strict; real-state={state}."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, ProjectionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PIPELINE COMPAT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Gate W4.3 para infraestructura v8 no activada."""
from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "assets/data/v8/experience-model-v80.json"
CSS = [
    ROOT / "assets/css/v8/tokens.css",
    ROOT / "assets/css/v8/base.css",
    ROOT / "assets/css/v8/components.css",
    ROOT / "assets/css/v8/surfaces.css",
]
RENDERER = ROOT / "scripts/render_v8_pilot.py"


def fail(message: str) -> None:
    raise AssertionError(message)


def route_path(route: str) -> Path:
    clean = route.lstrip("/")
    return ROOT / clean


def main() -> int:
    if not MODEL.exists() or not RENDERER.exists():
        fail("faltan experience model o renderer v8")
    for path in CSS:
        if not path.exists() or path.stat().st_size < 100:
            fail(f"asset CSS v8 ausente o vacío: {path.relative_to(ROOT)}")

    model = json.loads(MODEL.read_text(encoding="utf-8"))
    policy = model.get("pilot_policy") or {}
    if policy.get("commit_target_html") is not False:
        fail("W4.3 infrastructure exige commit_target_html=false")
    if policy.get("legacy_routes_unchanged") is not True:
        fail("W4.3 infrastructure exige legacy_routes_unchanged=true")

    pilots = model.get("pilots") or []
    if len(pilots) != 3:
        fail("W4.3 debe tener exactamente tres pilotos")
    for pilot in pilots:
        target = route_path(pilot["target_route"])
        if target.exists():
            fail(f"W4.3 no puede materializar todavía target HTML: {target.relative_to(ROOT)}")
        legacy = route_path(pilot["legacy_route"])
        if not legacy.exists():
            fail(f"legacy route desapareció accidentalmente: {legacy.relative_to(ROOT)}")

    html_files = sorted(ROOT.rglob("*.html"))
    if len(html_files) != 46:
        fail(f"W4.3 infrastructure debe conservar 46 HTML; encontró {len(html_files)}")
    forbidden_refs = [
        "assets/css/v8/tokens.css",
        "assets/css/v8/base.css",
        "assets/css/v8/components.css",
        "assets/css/v8/surfaces.css",
    ]
    for path in html_files:
        value = path.read_text(encoding="utf-8")
        for ref in forbidden_refs:
            if ref in value or f"../{ref}" in value:
                fail(f"activación accidental: {path.relative_to(ROOT)} ya carga {ref}")

    compile_result = subprocess.run(
        [sys.executable, "-m", "py_compile", str(RENDERER)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if compile_result.returncode:
        fail(f"renderer no compila: {compile_result.stderr.strip()}")

    check_result = subprocess.run(
        [sys.executable, str(RENDERER), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if check_result.returncode:
        fail(f"renderer --check falla: {check_result.stdout.strip()} {check_result.stderr.strip()}")
    if "RENDER V8 PILOT CHECK OK" not in check_result.stdout:
        fail("renderer --check no emitió contrato de éxito esperado")

    print(
        "VALIDATE V8 PILOT INFRA OK: 3 pilotos source-driven, 4 CSS consolidados, "
        "46 HTML legacy intactos y 0 superficies públicas activadas con v8."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PILOT INFRA FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

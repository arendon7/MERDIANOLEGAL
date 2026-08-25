#!/usr/bin/env python3
"""Materializa los tres targets v8 para QA efímero.

No forma parte todavía del builder canónico. Requiere una raíz explícita y, si la
raíz es el checkout del repositorio, `--allow-working-tree`. CI usa esta opción
sobre un checkout desechable para navegador/axe sin publicar los archivos.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
import json
import sys

import render_v8_pilot as renderer

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise AssertionError(message)


def output_path(root: Path, route: str) -> Path:
    if not route.startswith("/") or route.endswith("/"):
        fail(f"target route inválida para piloto HTML: {route}")
    return root / route.lstrip("/")


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser()
    parser.add_argument("--root", required=True, help="Raíz de materialización del sitio candidato")
    parser.add_argument("--allow-working-tree", action="store_true")
    args = parser.parse_args(argv)

    target_root = Path(args.root).resolve()
    if target_root == ROOT.resolve() and not args.allow_working_tree:
        fail("materializar en el checkout requiere --allow-working-tree explícito")
    target_root.mkdir(parents=True, exist_ok=True)

    model = renderer.load_json(renderer.MODEL_PATH)
    route_contract = renderer.load_json(renderer.ROUTES_PATH)
    site = renderer.load_json(renderer.SITE_CONFIG)
    pilots, route_map = renderer.validate_model(model, route_contract)

    written: list[Path] = []
    for pilot in pilots:
        path = output_path(target_root, pilot["target_route"])
        if path.exists():
            fail(f"target ya existe; W4.4 no sobrescribe: {path}")
        source = renderer.load_source(pilot)
        html = renderer.render(pilot, source, route_map, site["base_url"])
        if '<meta name="robots" content="noindex,follow">' not in html:
            fail(f"{pilot['id']}: target materializado debe permanecer noindex")
        if '<form' in html.lower():
            fail(f"{pilot['id']}: target materializado no puede crear formulario")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        written.append(path)

    if len(written) != 3:
        fail(f"se esperaban tres targets y se escribieron {len(written)}")

    manifest = {
        "contract": "v8-pilot-materialization",
        "status": "ephemeral-candidate",
        "count": len(written),
        "targets": [str(path.relative_to(target_root)).replace("\\", "/") for path in written],
    }
    manifest_path = target_root / ".v8-pilot-materialization.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("MATERIALIZE V8 PILOT OK: " + ", ".join(manifest["targets"]))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"MATERIALIZE V8 PILOT FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

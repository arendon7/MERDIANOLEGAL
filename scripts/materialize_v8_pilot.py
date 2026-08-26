#!/usr/bin/env python3
"""Materializa los tres targets v8 para QA/candidate controlado.

W4.4 los usa en checkout efímero. W4.5 puede persistir exactamente esos bytes.
El renderer conserva la arquitectura target v8; este materializador aplica una
compatibilidad transicional: un link relacionado solo apunta a target v8 si ese
target pertenece al conjunto materializado en esta wave. Cuando el target futuro
aún no existe, conserva la ruta legacy física y válida para evitar 404.

El cierre W4.5 exige un run posterior sobre los targets ya persistidos; el commit
del bot que materializa o refresca bytes no sustituye esa certificación final.
"""
from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path, PurePosixPath
import json
import posixpath
import re
import sys

import render_v8_pilot as renderer

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise AssertionError(message)


def output_path(root: Path, route: str) -> Path:
    if not route.startswith("/") or route.endswith("/"):
        fail(f"target route inválida para piloto HTML: {route}")
    return root / route.lstrip("/")


def current_route(pilot: dict, href: str) -> str | None:
    if re.match(r"^[a-z]+://", href, flags=re.I) or href.startswith(("#", "mailto:", "tel:")):
        return None
    parent = posixpath.dirname(pilot["legacy_route"])
    current = posixpath.normpath(posixpath.join(parent, href))
    return current if current.startswith("/") else "/" + current


def relative_from_target(pilot: dict, absolute_route: str) -> str:
    from_dir = PurePosixPath(pilot["target_route"]).parent
    return posixpath.relpath(str(PurePosixPath(absolute_route)), str(from_dir))


def preserve_available_related_links(
    html: str,
    pilot: dict,
    source: dict,
    route_map: dict[str, str],
    available_targets: set[str],
) -> str:
    """Evita que un candidate parcial enlace targets v8 que aún no existen."""
    updated = html
    for item in source["related"]:
        href = item[3]
        current = current_route(pilot, href)
        if current is None:
            continue
        target = route_map.get(current, current)
        if target in available_targets:
            continue
        rendered_target = renderer.resolve_related_href(pilot, href, route_map)
        legacy_relative = relative_from_target(pilot, current)
        old = f'href="{renderer.e(rendered_target)}"'
        new = f'href="{renderer.e(legacy_relative)}"'
        if old not in updated:
            fail(f"{pilot['id']}: no se encontró link target transicional {rendered_target}")
        updated = updated.replace(old, new, 1)
    return updated


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
    available_targets = {pilot["target_route"] for pilot in pilots}

    written: list[Path] = []
    for pilot in pilots:
        path = output_path(target_root, pilot["target_route"])
        if path.exists():
            fail(f"target ya existe; materializador no sobrescribe: {path}")
        raw_source = renderer.load_source(pilot)
        source = renderer.apply_presentation_overrides(pilot, raw_source)
        html = renderer.render(pilot, source, route_map, site["base_url"])
        html = preserve_available_related_links(
            html, pilot, source, route_map, available_targets
        )
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
        "link_policy": "target-if-materialized-else-legacy",
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

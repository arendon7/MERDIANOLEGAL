#!/usr/bin/env python3
"""Valida Buying Clarity v7.2 contra las 16 fuentes canónicas y su lifecycle de release."""
from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/buying-clarity-v72.json"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
START = "<!-- BUYING-CLARITY-V72:START -->"
END = "<!-- BUYING-CLARITY-V72:END -->"
STYLE = '../assets/css/v7/buying-clarity-v72.css'
VALID_LIFECYCLE = {
    "buying-clarity-prototype": {"version_prefix": "7.2.0-prototype"},
    "release-candidate": {"version_exact": "7.2.0"},
    "certified": {"version_exact": "7.2.0"},
}


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    return json.loads(read(path))


def body_attr(value: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', value)
    return match.group(1) if match else ""


def load_sources() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            fail(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            payload = load_json(path)
            if len(payload) != 1:
                fail(f"{path.name}: fuente inválida")
            catalog_id, source = next(iter(payload.items()))
            if catalog_id in result:
                fail(f"catalog_id duplicado: {catalog_id}")
            result[catalog_id] = source
    if len(result) != 16:
        fail(f"se esperaban 16 fuentes; hay {len(result)}")
    return result


def load_paths() -> dict[str, Path]:
    paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(paths) != 16:
        fail(f"se esperaban 16 fichas; hay {len(paths)}")
    result: dict[str, Path] = {}
    for path in paths:
        value = read(path)
        catalog_id = body_attr(value, "data-catalog-id")
        if not catalog_id:
            fail(f"{path.relative_to(ROOT)}: falta data-catalog-id")
        result[catalog_id] = path
    return result


def summary_block(value: str, label: str) -> str:
    if value.count(START) != 1 or value.count(END) != 1:
        fail(f"{label}: markers Buying Clarity deben existir una sola vez")
    match = re.search(re.escape(START) + r"(.*?)" + re.escape(END), value, flags=re.S)
    if not match:
        fail(f"{label}: no se pudo aislar resumen")
    return unescape(match.group(1))


def contains(block: str, items: list[str], label: str) -> None:
    missing = [item for item in items if item not in block]
    if missing:
        fail(f"{label}: resumen perdió truth: {missing[:6]}")


def validate_contract() -> dict:
    if not CONTRACT.exists():
        fail("falta buying-clarity-v72.json")
    contract = load_json(CONTRACT)
    status = contract.get("status")
    if status not in VALID_LIFECYCLE:
        fail(f"status Buying Clarity inválido: {status}")
    version = str(contract.get("version", ""))
    lifecycle = VALID_LIFECYCLE[status]
    if "version_exact" in lifecycle and version != lifecycle["version_exact"]:
        fail(f"{status} debe declarar version {lifecycle['version_exact']}")
    if "version_prefix" in lifecycle and not version.startswith(lifecycle["version_prefix"]):
        fail(f"{status} debe declarar versión con prefijo {lifecycle['version_prefix']}")
    if contract.get("baseline") != "7.1.0":
        fail("baseline Buying Clarity debe ser v7.1.0")
    rules = contract.get("rules", {})
    for key in (
        "preserve_order",
        "preserve_quantities_verbatim",
        "preserve_existing_hero_and_nav",
        "no_duplicate_engagement_navigation",
        "no_new_pricing",
        "no_new_capabilities",
        "supplements_are_not_included",
        "material_information_must_be_visible",
    ):
        if rules.get(key) is not True:
            fail(f"regla Buying Clarity no fijada: {key}")
    return contract


def validate_page(catalog_id: str, path: Path, source: dict, contract: dict) -> None:
    value = read(path)
    label = str(path.relative_to(ROOT))
    if value.count(f'href="{STYLE}"') != 1:
        fail(f"{label}: CSS v7.2 debe cargarse exactamente una vez")
    if value.count('id="v72-buying-summary"') != 1:
        fail(f"{label}: resumen v7.2 debe existir una sola vez")
    if value.count('data-buying-clarity-v72="true"') != 1:
        fail(f"{label}: falta contrato DOM v7.2")
    if f'data-buying-catalog-id="{catalog_id}"' not in value:
        fail(f"{label}: catalog_id v7.2 no coincide")

    hero = value.find('<section class="v6-hero v6-detail-hero"')
    start = value.find(START)
    nav = value.find('<nav class="v6-detail-nav"')
    main = value.find('<main id="contenido"')
    if not (hero >= 0 and hero < start < nav < main):
        fail(f"{label}: resumen debe quedar después del hero y antes de nav/main")

    block = summary_block(value, label)
    summary = contract["summary"]
    contains(block, [summary["eyebrow"], summary["title"], summary["lead"], source["modality"], source["duration"], source["audience"]], label)

    expected: list[str] = []
    for title, copy in source.get("perimeter", [])[: int(summary["perimeter_limit"])]:
        expected.extend([title, copy])
    for title, _ in source.get("deliverables", [])[: int(summary["deliverables_limit"])]:
        expected.append(title)
    for field, limit_key in (("requirements", "requirements_limit"), ("acceptance", "acceptance_limit"), ("supplements", "supplements_limit")):
        for title, copy in source.get(field, [])[: int(summary[limit_key])]:
            expected.extend([title, copy])
    contains(block, expected, label)

    if "Estas ampliaciones no hacen parte del alcance base salvo que la propuesta las incluya expresamente." not in block:
        fail(f"{label}: falta boundary de suplementos")
    if '#v6-perimeter' not in block or '#v6-deliverables' not in block:
        fail(f"{label}: faltan enlaces de profundidad")
    if '#v6-engagement' in block:
        fail(f"{label}: Buying Clarity no debe duplicar la navegación canónica a #v6-engagement")
    if re.search(r"<form\b", block):
        fail(f"{label}: Buying Clarity no puede crear formularios")


def main() -> int:
    contract = validate_contract()
    sources = load_sources()
    paths = load_paths()
    if set(sources) != set(paths):
        fail(f"fuentes/fichas desalineadas: {sorted(set(sources) ^ set(paths))}")
    for catalog_id in sorted(sources):
        validate_page(catalog_id, paths[catalog_id], sources[catalog_id], contract)
    print(f"VALIDATE BUYING CLARITY V7.2 OK: 16/16 resúmenes visibles, source-driven y sin capability drift ({contract['status']}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE BUYING CLARITY V7.2 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

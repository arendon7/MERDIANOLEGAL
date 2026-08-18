#!/usr/bin/env python3
"""Materializa Fit & Scope Clarity v6.4 en las 16 fichas profundas.

No crea contenido jurídico nuevo: situations y supplements se reproducen
exclusivamente desde catalog-products-v41 y catalog-services-v42.
"""
from __future__ import annotations

from html import escape
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets" / "data" / "v6" / "fit-scope-clarity-v64.json"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
START = "<!-- FIT-SCOPE-CLARITY-V64:START -->"
END = "<!-- FIT-SCOPE-CLARITY-V64:END -->"
CSS_HREF = "../assets/css/v6/fit-scope-clarity-v64.css"
V63_CSS_HREF = "../assets/css/v6/engagement-clarity-v63.css"
V6_TOKENS_HREF = "../assets/css/v6/tokens.css"


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


def valid_matrix(path: Path, field: str, matrix: object) -> list[list[str]]:
    if not isinstance(matrix, list) or not matrix:
        raise RuntimeError(f"{path.name}: {field} debe ser una matriz no vacía")
    for row in matrix:
        if not isinstance(row, list) or len(row) != 2 or not all(isinstance(item, str) and item.strip() for item in row):
            raise RuntimeError(f"{path.name}: {field} contiene una fila inválida")
    return matrix


def load_sources() -> dict[str, dict]:
    sources: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            raise RuntimeError(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            payload = load_json(path)
            if len(payload) != 1:
                raise RuntimeError(f"{path.name}: debe declarar exactamente un catalog_id")
            catalog_id, source = next(iter(payload.items()))
            if catalog_id in sources:
                raise RuntimeError(f"catalog_id duplicado: {catalog_id}")
            valid_matrix(path, "situations", source.get("situations"))
            valid_matrix(path, "supplements", source.get("supplements"))
            sources[catalog_id] = source
    if len(sources) != 16:
        raise RuntimeError(f"se esperaban 16 fuentes y hay {len(sources)}")
    return sources


def discover_pages() -> dict[str, Path]:
    pages: dict[str, Path] = {}
    paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(paths) != 16:
        raise RuntimeError(f"se esperaban 16 fichas HTML y hay {len(paths)}")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        catalog_id = body_attr(text, "data-catalog-id")
        if not catalog_id:
            raise RuntimeError(f"{path.relative_to(ROOT)}: falta data-catalog-id")
        if catalog_id in pages:
            raise RuntimeError(f"data-catalog-id duplicado: {catalog_id}")
        pages[catalog_id] = path
    return pages


def render_rows(rows: list[list[str]], group: str) -> str:
    return "".join(
        f'<div class="v64-fit-scope-row" data-fit-scope-row="{e(group)}"><dt>{e(label)}</dt><dd>{e(copy)}</dd></div>'
        for label, copy in rows
    )


def render_section(catalog_id: str, source: dict, contract: dict) -> str:
    presentation = contract["presentation"]
    situations = render_rows(source["situations"], "situations")
    supplements = render_rows(source["supplements"], "supplements")
    return (
        f'{START}\n'
        f'<section class="v6-section v64-fit-scope" id="{e(presentation["section_id"])}" '
        f'data-fit-scope-clarity-v64="true" data-fit-scope-catalog-id="{e(catalog_id)}" '
        f'aria-labelledby="v64-fit-scope-title-{e(catalog_id)}">'
        '<div class="v6-container">'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{e(presentation["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v64-fit-scope-title-{e(catalog_id)}">{e(presentation["title"])}</h2>'
        f'<p class="v6-lead">{e(presentation["intro"])}</p>'
        '</div>'
        '<div class="v64-fit-scope-grid">'
        '<article class="v64-fit-scope-panel" data-fit-scope-group="situations">'
        f'<h3>{e(presentation["situations_title"])}</h3><dl class="v64-fit-scope-list">{situations}</dl>'
        '</article>'
        '<article class="v64-fit-scope-panel" data-fit-scope-group="supplements">'
        f'<h3>{e(presentation["supplements_title"])}</h3><dl class="v64-fit-scope-list">{supplements}</dl>'
        '</article>'
        '</div></div></section>\n'
        f'{END}'
    )


def ensure_stylesheet(text: str) -> str:
    text = re.sub(
        rf'(?m)^[ \t]*<link rel="stylesheet" href="{re.escape(CSS_HREF)}">[ \t]*(?:\r?\n)?',
        "",
        text,
    )
    anchor_href = V63_CSS_HREF if V63_CSS_HREF in text else V6_TOKENS_HREF
    anchor_pattern = re.compile(
        rf'(?m)^(?P<indent>[ \t]*)<link rel="stylesheet" href="{re.escape(anchor_href)}">[ \t]*$'
    )
    matches = list(anchor_pattern.finditer(text))
    if len(matches) != 1:
        raise RuntimeError(f"ficha debe cargar exactamente una hoja ancla {anchor_href}; encontró {len(matches)}")
    match = matches[0]
    if anchor_href == V63_CSS_HREF:
        insert_at = match.end()
        return text[:insert_at] + f'\n{match.group("indent")}<link rel="stylesheet" href="{CSS_HREF}">' + text[insert_at:]
    link = f'{match.group("indent")}<link rel="stylesheet" href="{CSS_HREF}">\n'
    return text[:match.start()] + link + text[match.start():]


def ensure_section(text: str, section: str) -> str:
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\s*', "", text, flags=re.S)
    result = re.search(r'<section class="v6-section v6-result" id="v6-result"[^>]*>.*?</section>', text, flags=re.S)
    if not result:
        raise RuntimeError("ficha sin sección v6-result para insertar Fit & Scope Clarity v6.4")
    return text[:result.end()] + "\n" + section + "\n" + text[result.end():]


def materialize(text: str, catalog_id: str, source: dict, contract: dict) -> str:
    text = ensure_stylesheet(text)
    text = ensure_section(text, render_section(catalog_id, source, contract))
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Comprueba drift sin escribir")
    args = parser.parse_args()

    if not CONTRACT.exists():
        return 0
    contract = load_json(CONTRACT)
    if contract.get("version") != "6.4.0":
        raise RuntimeError("Fit & Scope Clarity debe declarar version 6.4.0")
    if contract.get("scope", {}).get("detail_pages") != 16:
        raise RuntimeError("Fit & Scope Clarity debe gobernar exactamente 16 fichas")

    sources = load_sources()
    pages = discover_pages()
    if set(sources) != set(pages):
        raise RuntimeError(
            f"desalineación source/HTML: sin HTML={sorted(set(sources)-set(pages))}; "
            f"sin fuente={sorted(set(pages)-set(sources))}"
        )

    changed: list[Path] = []
    rendered: dict[Path, str] = {}
    for catalog_id in sorted(sources):
        path = pages[catalog_id]
        before = path.read_text(encoding="utf-8")
        after = materialize(before, catalog_id, sources[catalog_id], contract)
        if after != before:
            changed.append(path)
            rendered[path] = after

    if args.check:
        if changed:
            print("FIT & SCOPE CLARITY V6.4 DRIFT:", file=sys.stderr)
            for path in changed:
                print(f"- {path.relative_to(ROOT).as_posix()}", file=sys.stderr)
            return 1
        print("FIT & SCOPE CLARITY V6.4 CHECK OK: 16/16 fichas sincronizadas.")
        return 0

    for path, text in rendered.items():
        path.write_text(text, encoding="utf-8")
    print(f"FIT & SCOPE CLARITY V6.4 OK: {len(pages)}/16 fichas gobernadas; {len(changed)} actualizadas desde truth canónico.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

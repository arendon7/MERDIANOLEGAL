#!/usr/bin/env python3
"""Materializa Engagement Clarity v6.3 en las 16 fichas profundas.

No crea contenido jurídico nuevo: requirements y responsibilities se reproducen
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
CONTRACT = ROOT / "assets" / "data" / "v6" / "engagement-clarity-v63.json"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
START = "<!-- ENGAGEMENT-CLARITY-V63:START -->"
END = "<!-- ENGAGEMENT-CLARITY-V63:END -->"
CSS_HREF = "../assets/css/v6/engagement-clarity-v63.css"
V6_TOKENS_HREF = "../assets/css/v6/tokens.css"
NAV_ATTR = 'data-engagement-clarity-v63-nav="true"'


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


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
            for field in ("requirements", "responsibilities"):
                matrix = source.get(field)
                if not isinstance(matrix, list) or not matrix:
                    raise RuntimeError(f"{path.name}: {field} debe ser una matriz no vacía")
                for row in matrix:
                    if not isinstance(row, list) or len(row) != 2 or not all(isinstance(item, str) and item.strip() for item in row):
                        raise RuntimeError(f"{path.name}: {field} contiene una fila inválida")
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


def render_rows(rows: list[list[str]]) -> str:
    return "".join(
        f'<div class="v63-engagement-row"><dt>{e(label)}</dt><dd>{e(copy)}</dd></div>'
        for label, copy in rows
    )


def render_section(catalog_id: str, source: dict, contract: dict) -> str:
    presentation = contract["presentation"]
    requirements = render_rows(source["requirements"])
    responsibilities = render_rows(source["responsibilities"])
    return (
        f'{START}\n'
        f'<section class="v6-section v63-engagement" id="{e(presentation["section_id"])}" '
        f'data-engagement-clarity-v63="true" data-engagement-catalog-id="{e(catalog_id)}" '
        f'aria-labelledby="v63-engagement-title-{e(catalog_id)}">'
        '<div class="v6-container">'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{e(presentation["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v63-engagement-title-{e(catalog_id)}">{e(presentation["title"])}</h2>'
        '<p class="v6-lead">Antes de iniciar, la propuesta debe dejar claros los insumos, interlocutores y decisiones que sostienen el alcance. Estas condiciones provienen de la ficha canónica y solo cambian mediante una propuesta expresa.</p>'
        '</div>'
        '<div class="v63-engagement-grid">'
        '<article class="v63-engagement-panel" data-engagement-group="requirements">'
        f'<h3>{e(presentation["requirements_title"])}</h3><dl class="v63-engagement-list">{requirements}</dl>'
        '</article>'
        '<article class="v63-engagement-panel" data-engagement-group="responsibilities">'
        f'<h3>{e(presentation["responsibilities_title"])}</h3><dl class="v63-engagement-list">{responsibilities}</dl>'
        '</article>'
        '</div></div></section>\n'
        f'{END}'
    )


def ensure_stylesheet(text: str) -> str:
    """Preserva una hoja v6.3 existente si ya precede a tokens.

    El contrato depende del orden, no del whitespace editorial. Evitar borrar y
    reinsertar un `<link>` correcto impide drift puramente cosmético frente a
    materializadores posteriores como Fit & Scope v6.4.
    """
    css_pattern = re.compile(
        rf'(?m)^(?P<indent>[ \t]*)<link rel="stylesheet" href="{re.escape(CSS_HREF)}">[ \t]*$'
    )
    token_pattern = re.compile(
        rf'(?m)^(?P<indent>[ \t]*)<link rel="stylesheet" href="{re.escape(V6_TOKENS_HREF)}">[ \t]*$'
    )
    css_matches = list(css_pattern.finditer(text))
    token_matches = list(token_pattern.finditer(text))
    if len(css_matches) > 1:
        raise RuntimeError(f"ficha debe cargar como máximo una hoja {CSS_HREF}; encontró {len(css_matches)}")
    if len(token_matches) != 1:
        raise RuntimeError(f"ficha debe cargar exactamente una hoja {V6_TOKENS_HREF}; encontró {len(token_matches)}")

    token = token_matches[0]
    if len(css_matches) == 1:
        existing = css_matches[0]
        if existing.start() < token.start():
            return text
        # Si existe pero quedó después de tokens, moverla sin normalizar más HTML.
        text = text[:existing.start()] + text[existing.end():]
        text = re.sub(r'(?m)^\r?\n', "", text[existing.start():], count=1) if False else text
        token_matches = list(token_pattern.finditer(text))
        if len(token_matches) != 1:
            raise RuntimeError(f"ficha perdió la hoja ancla {V6_TOKENS_HREF} al reordenar v6.3")
        token = token_matches[0]

    link = f'{token.group("indent")}<link rel="stylesheet" href="{CSS_HREF}">\n'
    return text[:token.start()] + link + text[token.start():]


def ensure_nav(text: str, label: str) -> str:
    nav_match = re.search(r'<nav class="v6-detail-nav"[^>]*>.*?</nav>', text, flags=re.S)
    if not nav_match:
        raise RuntimeError("ficha sin navegación v6 para Engagement Clarity v6.3")
    nav = nav_match.group(0)
    nav = re.sub(r'<a\b[^>]*data-engagement-clarity-v63-nav="true"[^>]*>.*?</a>', "", nav, flags=re.S)
    boundary = '<a href="#v6-boundary">Límites</a>'
    if nav.count(boundary) != 1:
        raise RuntimeError("navegación v6 sin ancla única de Límites")
    engagement = f'<a {NAV_ATTR} href="#v6-engagement">{e(label)}</a>'
    nav = nav.replace(boundary, engagement + boundary, 1)
    return text[:nav_match.start()] + nav + text[nav_match.end():]


def ensure_section(text: str, section: str) -> str:
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\s*', "", text, flags=re.S)
    boundary = re.search(r'<section class="v6-section v6-boundary" id="v6-boundary"', text)
    if not boundary:
        raise RuntimeError("ficha sin sección v6-boundary para insertar Engagement Clarity v6.3")
    return text[:boundary.start()] + section + "\n" + text[boundary.start():]


def materialize(text: str, catalog_id: str, source: dict, contract: dict) -> str:
    text = ensure_stylesheet(text)
    text = ensure_nav(text, contract["presentation"]["nav_label"])
    text = ensure_section(text, render_section(catalog_id, source, contract))
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Comprueba drift sin escribir")
    args = parser.parse_args()

    if not CONTRACT.exists():
        return 0
    contract = load_json(CONTRACT)
    if contract.get("version") != "6.3.0":
        raise RuntimeError("Engagement Clarity debe declarar version 6.3.0")
    if contract.get("scope", {}).get("detail_pages") != 16:
        raise RuntimeError("Engagement Clarity debe gobernar exactamente 16 fichas")

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
            print("ENGAGEMENT CLARITY V6.3 DRIFT:", file=sys.stderr)
            for path in changed:
                print(f"- {path.relative_to(ROOT).as_posix()}", file=sys.stderr)
            return 1
        print("ENGAGEMENT CLARITY V6.3 CHECK OK: 16/16 fichas sincronizadas.")
        return 0

    for path, text in rendered.items():
        path.write_text(text, encoding="utf-8")
    print(f"ENGAGEMENT CLARITY V6.3 OK: {len(pages)}/16 fichas gobernadas; {len(changed)} actualizadas desde truth canónico.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

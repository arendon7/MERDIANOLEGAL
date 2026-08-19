#!/usr/bin/env python3
"""Materializa Buying Clarity v7.2 en las 16 fichas profundas desde catálogos canónicos."""
from __future__ import annotations

from html import escape
import argparse
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
STYLE = "../assets/css/v7/buying-clarity-v72.css"


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


def load_sources() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            raise RuntimeError(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            payload = load_json(path)
            if len(payload) != 1:
                raise RuntimeError(f"{path.name}: debe declarar exactamente un catalog_id")
            catalog_id, source = next(iter(payload.items()))
            if catalog_id in result:
                raise RuntimeError(f"catalog_id duplicado: {catalog_id}")
            result[catalog_id] = source
    if len(result) != 16:
        raise RuntimeError(f"se esperaban 16 fuentes y hay {len(result)}")
    return result


def load_paths() -> dict[str, Path]:
    paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(paths) != 16:
        raise RuntimeError(f"se esperaban 16 fichas y hay {len(paths)}")
    result: dict[str, Path] = {}
    for path in paths:
        value = path.read_text(encoding="utf-8")
        catalog_id = body_attr(value, "data-catalog-id")
        if not catalog_id:
            raise RuntimeError(f"{path.relative_to(ROOT)}: falta data-catalog-id")
        result[catalog_id] = path
    return result


def rows(items: list[list[str]], limit: int, cls: str) -> str:
    return "".join(
        f'<div class="{cls}-row"><strong>{e(title)}</strong><span>{e(copy)}</span></div>'
        for title, copy in items[:limit]
    )


def title_rows(items: list[list[str]], limit: int, cls: str) -> str:
    return "".join(
        f'<div class="{cls}-row"><strong>{e(title)}</strong></div>'
        for title, _ in items[:limit]
    )


def render_summary(catalog_id: str, source: dict, contract: dict) -> str:
    summary = contract["summary"]
    labels = contract["labels"]
    links = contract["links"]
    kind = "product" if source.get("type") == "Producto jurídico" else "service"

    meta = "".join([
        f'<div><span>{e(labels["modality"])}</span><strong>{e(source["modality"])}</strong></div>',
        f'<div><span>{e(labels["duration"])}</span><strong>{e(source["duration"])}</strong></div>',
        f'<div><span>{e(labels["audience"])}</span><strong>{e(source["audience"])}</strong></div>',
    ])

    perimeter = rows(source.get("perimeter", []), int(summary["perimeter_limit"]), "v72-buying")
    deliverables = title_rows(source.get("deliverables", []), int(summary["deliverables_limit"]), "v72-buying")
    requirements = rows(source.get("requirements", []), int(summary["requirements_limit"]), "v72-buying-mini")
    acceptance = rows(source.get("acceptance", []), int(summary["acceptance_limit"]), "v72-buying-mini")
    supplements = rows(source.get("supplements", []), int(summary["supplements_limit"]), "v72-buying-mini")
    acceptance_label = labels["acceptance_product"] if kind == "product" else labels["acceptance_service"]

    return f'''{START}
<section class="v72-buying-summary" id="v72-buying-summary" data-buying-clarity-v72="true" data-buying-catalog-id="{e(catalog_id)}" aria-labelledby="v72-buying-title-{e(catalog_id)}">
  <div class="v6-container v72-buying-shell">
    <div class="v72-buying-head"><p class="v6-eyebrow">{e(summary['eyebrow'])}</p><h2 class="v6-heading" id="v72-buying-title-{e(catalog_id)}">{e(summary['title'])}</h2><p class="v6-lead">{e(summary['lead'])}</p></div>
    <div class="v72-buying-meta">{meta}</div>
    <div class="v72-buying-main">
      <article class="v72-buying-panel"><h3>{e(labels['perimeter'])}</h3><div class="v72-buying-list">{perimeter}</div><a class="v6-text-link" href="#v6-perimeter">{e(links['perimeter'])} →</a></article>
      <article class="v72-buying-panel"><h3>{e(labels['deliverables'])}</h3><div class="v72-buying-list">{deliverables}</div><a class="v6-text-link" href="#v6-deliverables">{e(links['deliverables'])} →</a></article>
    </div>
    <div class="v72-buying-secondary">
      <article><h3>{e(labels['requirements'])}</h3><div class="v72-buying-mini-list">{requirements}</div></article>
      <article><h3>{e(acceptance_label)}</h3><div class="v72-buying-mini-list">{acceptance}</div></article>
      <article><h3>{e(labels['supplements'])}</h3><div class="v72-buying-mini-list">{supplements}</div><p class="v72-buying-note">Estas ampliaciones no hacen parte del alcance base salvo que la propuesta las incluya expresamente.</p></article>
    </div>
  </div>
</section>
{END}'''


def ensure_style(text: str) -> str:
    text = re.sub(rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(STYLE)}">\s*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("ficha sin </head>")
    return text.replace("</head>", f'  <link rel="stylesheet" href="{STYLE}">\n</head>', 1)


def patch(text: str, summary_html: str, label: str) -> str:
    text = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\s*", "", text, flags=re.S)
    hero = re.search(r'<section class="v6-hero v6-detail-hero"[^>]*>.*?</section>', text, flags=re.S)
    if not hero:
        raise RuntimeError(f"{label}: no se localizó hero v6")
    return text[:hero.end()] + "\n" + summary_html + "\n" + text[hero.end():]


def materialize(check: bool) -> int:
    if not CONTRACT.exists():
        return 0
    contract = load_json(CONTRACT)
    if not str(contract.get("version", "")).startswith("7.2."):
        raise RuntimeError("buying-clarity-v72.json debe declarar versión 7.2.x")
    sources = load_sources()
    paths = load_paths()
    if set(sources) != set(paths):
        raise RuntimeError("fuentes y fichas no coinciden")

    drift: list[str] = []
    for catalog_id in sorted(sources):
        path = paths[catalog_id]
        before = path.read_text(encoding="utf-8")
        after = ensure_style(before)
        after = patch(after, render_summary(catalog_id, sources[catalog_id], contract), str(path.relative_to(ROOT)))
        if after != before:
            if check:
                drift.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(after, encoding="utf-8")
    if drift:
        raise RuntimeError("Buying Clarity drift en: " + ", ".join(drift))
    print("BUYING CLARITY V7.2 OK: 16/16 fichas con resumen source-driven." if not check else "BUYING CLARITY V7.2 CHECK OK: 16/16 fichas sin drift.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    return materialize(args.check)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"BUYING CLARITY V7.2 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Materializa el panel demostrativo Legal Intelligence v7.3 en experiencia.html.

La superficie usa únicamente escenarios ficticios y deriva referencias cuantitativas
verbatim de los catálogos canónicos indicados por el contrato v7.3.
"""
from __future__ import annotations

import argparse
from html import escape
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-demo-v73.json"
TARGET = ROOT / "experiencia.html"
STYLE = "assets/css/v7/legal-intelligence-demo-v73.css"
TAB_START = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-TAB:START -->"
TAB_END = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-TAB:END -->"
PANEL_START = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-PANEL:START -->"
PANEL_END = "<!-- LEGAL-INTELLIGENCE-DEMO-V73-PANEL:END -->"
EMPRESAS_TAB = '<button class="experience-tab" type="button" data-target="empresas"><span>05</span><strong>Meridiano Empresas</strong><small>Seguimiento operativo</small></button>'
VALID_LIFECYCLE = {
    "demo-prototype": {"version_prefix": "7.3.0-prototype"},
    "release-candidate": {"version_exact": "7.3.0"},
    "certified": {"version_exact": "7.3.0"},
}


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_lifecycle(data: dict) -> str:
    status = str(data.get("status", ""))
    version = str(data.get("version", ""))
    if status not in VALID_LIFECYCLE:
        raise RuntimeError(f"status demo v7.3 inválido: {status}")
    lifecycle = VALID_LIFECYCLE[status]
    if "version_exact" in lifecycle and version != lifecycle["version_exact"]:
        raise RuntimeError(f"{status} debe declarar version {lifecycle['version_exact']}")
    if "version_prefix" in lifecycle and not version.startswith(lifecycle["version_prefix"]):
        raise RuntimeError(f"{status} debe declarar versión con prefijo {lifecycle['version_prefix']}")
    if data.get("baseline") != "7.2.0":
        raise RuntimeError("baseline demo v7.3 debe ser 7.2.0")
    return status


def source_for(scenario: dict) -> dict:
    path = ROOT / scenario["source"]
    if not path.exists():
        raise RuntimeError(f"Fuente demo inexistente: {scenario['source']}")
    payload = load_json(path)
    if len(payload) != 1:
        raise RuntimeError(f"Fuente demo inválida: {scenario['source']}")
    catalog_id, source = next(iter(payload.items()))
    if catalog_id != scenario["catalog_id"]:
        raise RuntimeError(
            f"{scenario['id']}: catalog_id {catalog_id!r} no coincide con {scenario['catalog_id']!r}"
        )
    return source


def metric_rows(scenario: dict, source: dict) -> str:
    rows: list[str] = []
    for section, index in scenario.get("metrics", []):
        items = source.get(section, [])
        if not isinstance(index, int) or index < 0 or index >= len(items):
            raise RuntimeError(f"{scenario['id']}: índice inválido {section}[{index}]")
        title, copy = items[index]
        rows.append(
            '<div class="li-demo-metric-v73">'
            f'<b>{e(title)}</b><span>{e(copy)}</span>'
            '</div>'
        )
    return "".join(rows)


def render_card(scenario: dict) -> str:
    source = source_for(scenario)
    flow = "".join(f'<span>{e(step)}</span>' for step in scenario["flow"])
    metrics = metric_rows(scenario, source)
    scope = ""
    if metrics:
        scope = (
            '<div class="li-demo-scope-v73">'
            '<strong>Referencia de alcance estándar</strong>'
            '<div class="li-demo-metrics-v73">' + metrics + '</div>'
            '</div>'
        )
    return (
        f'<article class="li-demo-card-v73" data-li-demo-scenario="{e(scenario["id"])}">'
        '<div class="li-demo-card-head-v73"><div>'
        '<span class="li-demo-badge-v73">DEMO</span>'
        f'<h3>{e(scenario["name"])}</h3>'
        '</div></div>'
        f'<p class="li-demo-problem-v73">{e(scenario["problem"])}</p>'
        f'<div class="li-demo-flow-v73" aria-label="Flujo demostrativo">{flow}</div>'
        '<div class="li-demo-artifact-v73"><strong>Artefacto demostrativo</strong>'
        f'<p>{e(scenario["artifact"])}</p></div>'
        '<div class="li-demo-result-v73"><strong>Resultado que ilustra</strong>'
        f'<p>{e(scenario["result"])}</p></div>'
        f'{scope}'
        f'<p class="li-demo-boundary-note-v73"><strong>Frontera.</strong> {e(scenario["boundary"])}</p>'
        f'<a class="v6-text-link" href="{e(scenario["href"])}">Ver oferta relacionada →</a>'
        '</article>'
    )


def render_tab() -> str:
    return (
        f'{TAB_START}\n'
        '<button class="experience-tab" type="button" data-target="intelligence">'
        '<span>06</span><strong>Legal Intelligence</strong><small>5 escenarios demostrativos</small>'
        '</button>\n'
        f'{TAB_END}'
    )


def render_panel(data: dict) -> str:
    cards = "".join(render_card(item) for item in data["scenarios"])
    chips = "".join(
        f'<span>{e(item.strip())}</span>'
        for item in data["boundary"].split("·")
        if item.strip()
    )
    return (
        f'{PANEL_START}\n'
        '<section class="experience-panel li-demo-v73" id="intelligence" '
        'data-panel="intelligence" data-li-demo-v73="true" hidden>'
        '<div class="container">'
        '<div class="section-heading">'
        '<p class="eyebrow dark">LEGAL INTELLIGENCE · DEMO</p>'
        f'<h2>{e(data["title"])}</h2>'
        f'<p>{e(data["lead"])}</p>'
        '</div>'
        f'<div class="li-demo-boundary-v73" aria-label="Condiciones del demo">{chips}</div>'
        f'<div class="li-demo-grid-v73">{cards}</div>'
        '</div></section>\n'
        f'{PANEL_END}'
    )


def strip_managed(text: str, start: str, end: str) -> str:
    if start not in text and end not in text:
        return text
    if text.count(start) != 1 or text.count(end) != 1:
        raise RuntimeError(f"Marcadores parciales/duplicados: {start}")
    # La indentación pertenece al bloque gestionado. Retirarla evita acumular
    # espacios en segundas pasadas sin consumir líneas vecinas.
    pattern = re.compile(
        r"(?m)^[ \t]*" + re.escape(start) + r".*?" + re.escape(end) + r"[ \t]*(?:\r?\n)?",
        re.S,
    )
    return pattern.sub("", text, count=1)


def ensure_style(text: str) -> str:
    text = re.sub(
        rf'(?m)^[ \t]*<link rel="stylesheet" href="{re.escape(STYLE)}">[ \t]*(?:\r?\n)?',
        "",
        text,
    )
    if "</head>" not in text:
        raise RuntimeError("experiencia.html no contiene </head>")
    return text.replace("</head>", f'  <link rel="stylesheet" href="{STYLE}">\n</head>', 1)


def expected_content(data: dict) -> str:
    if not TARGET.exists():
        raise RuntimeError("Falta experiencia.html")
    text = TARGET.read_text(encoding="utf-8")
    text = strip_managed(text, TAB_START, TAB_END)
    text = strip_managed(text, PANEL_START, PANEL_END)
    text = ensure_style(text)

    if text.count(EMPRESAS_TAB) != 1:
        raise RuntimeError("No se encontró exactamente una pestaña canónica Meridiano Empresas")
    text = text.replace(EMPRESAS_TAB, EMPRESAS_TAB + "\n        " + render_tab(), 1)

    main_close = "  </main>"
    if text.count(main_close) != 1:
        raise RuntimeError("experiencia.html debe contener un único cierre de main")
    text = text.replace(main_close, "    " + render_panel(data) + "\n" + main_close, 1)
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if not CONTRACT.exists():
        return 0
    data = load_json(CONTRACT)
    status = validate_lifecycle(data)
    if len(data.get("scenarios", [])) != 5:
        raise RuntimeError("El demo debe declarar exactamente cinco escenarios")

    before = TARGET.read_text(encoding="utf-8")
    after = expected_content(data)
    if args.check:
        if before != after:
            raise RuntimeError("Legal Intelligence Demo v7.3 drift en experiencia.html")
        print(f"LEGAL INTELLIGENCE DEMO V7.3 CHECK OK: experiencia.html sin drift ({status}).")
        return 0
    if before != after:
        TARGET.write_text(after, encoding="utf-8")
        print(f"LEGAL INTELLIGENCE DEMO V7.3 OK: experiencia.html materializado ({status}).")
    else:
        print(f"LEGAL INTELLIGENCE DEMO V7.3 OK: experiencia.html ya materializado ({status}).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"LEGAL INTELLIGENCE DEMO V7.3 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

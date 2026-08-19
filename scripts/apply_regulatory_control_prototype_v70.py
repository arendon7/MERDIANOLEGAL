#!/usr/bin/env python3
"""Materialize the Regulatory Control v7 prototype on existing canonical surfaces."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/regulatory-control-prototype-v70.json"
ROUTE_START = "<!-- REGULATORY-CONTROL-V70:START -->"
ROUTE_END = "<!-- REGULATORY-CONTROL-V70:END -->"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def deep_markers(item: dict) -> tuple[str, str]:
    key = item["id"].upper().replace("-", "_")
    return f"<!-- REGULATORY-CONTROL-V70-{key}:START -->", f"<!-- REGULATORY-CONTROL-V70-{key}:END -->"


def strip_block(content: str, start: str, end: str, label: str) -> str:
    if start not in content and end not in content:
        return content
    if content.count(start) != 1 or content.count(end) != 1:
        raise SystemExit(f"{label}: managed markers are partial or duplicated")
    before, tail = content.split(start, 1)
    _, after = tail.split(end, 1)
    return before.rstrip() + "\n" + after.lstrip("\n")


def render_route(route: dict) -> str:
    cards = []
    for stage in route["stages"]:
        cards.append(
            '<article class="v6-route-option" data-v7-regulatory-stage="%s">'
            '<p class="v6-eyebrow">%s · %s</p>'
            '<h3>%s</h3><p>%s</p><a href="%s">%s →</a></article>'
            % (
                esc(stage["label"].lower().replace(" ", "-")),
                esc(stage["number"]),
                esc(stage["label"]),
                esc(stage["title"]),
                esc(stage["body"]),
                esc(stage["href"]),
                esc(stage["action"]),
            )
        )
    return (
        f"{ROUTE_START}\n"
        '<section class="v6-section" id="v7-regulatory-control" aria-labelledby="v7-regulatory-control-title" data-v7-regulatory-control="route">'
        '<div class="v6-container"><div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(route["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v7-regulatory-control-title">{esc(route["title"])}</h2>'
        f'<p class="v6-lead">{esc(route["lead"])}</p></div>'
        '<div class="v6-route-list" aria-label="Etapas de Regulatory Control">' + ''.join(cards) + '</div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Frontera de alcance.</strong> {esc(route["boundary"])}</p>'
        '</div></div></section>\n'
        f"{ROUTE_END}\n"
    )


def render_deep(item: dict) -> str:
    start, end = deep_markers(item)
    rows = []
    for row in item["items"]:
        rows.append(
            '<div class="v6-result-item"><b>%s</b><span><strong>%s.</strong> %s</span></div>'
            % (esc(row["number"]), esc(row["title"]), esc(row["body"]))
        )
    continuity = item["continuity"]
    return (
        f"{start}\n"
        f'<section class="v6-section v6-result" id="v7-{esc(item["id"])}" aria-labelledby="v7-{esc(item["id"])}-title" data-v7-regulatory-deep="{esc(item["id"])}">'
        '<div class="v6-container v6-result-grid"><div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(item["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v7-{esc(item["id"])}-title">{esc(item["title"])}</h2>'
        f'<p class="v6-lead">{esc(item["lead"])}</p></div>'
        '<div class="v6-result-list">' + ''.join(rows) + '</div></div>'
        '<div class="v6-container"><div class="v6-pricing-note" data-v7-regulatory-continuity="true"><div>'
        '<p class="v6-eyebrow">CONTINUIDAD</p>'
        f'<h3>{esc(continuity["title"])}</h3><p>{esc(continuity["body"])}</p>'
        f'</div><a href="{esc(continuity["href"])}">{esc(continuity["action"])} →</a></div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Frontera de alcance.</strong> {esc(item["boundary"])}</p>'
        '</div></div></section>\n'
        f"{end}\n"
    )


def expected_route(route: dict) -> tuple[Path, str]:
    target = ROOT / route["target"]
    if not target.exists():
        raise SystemExit(f"Missing Regulatory Control route target: {route['target']}")
    content = strip_block(target.read_text(encoding="utf-8"), ROUTE_START, ROUTE_END, route["target"])
    anchor = route["insert_before"]
    if content.count(anchor) != 1:
        raise SystemExit(f"{route['target']}: expected exactly one route insertion anchor; found {content.count(anchor)}")
    return target, content.replace(anchor, render_route(route) + anchor, 1)


def expected_deep(item: dict) -> tuple[Path, str]:
    target = ROOT / item["target"]
    if not target.exists():
        raise SystemExit(f"Missing Regulatory Control deep target: {item['target']}")
    start, end = deep_markers(item)
    content = strip_block(target.read_text(encoding="utf-8"), start, end, item["target"])
    anchor = item["insert_before"]
    if content.count(anchor) != 1:
        raise SystemExit(f"{item['target']}: expected exactly one deep insertion anchor; found {content.count(anchor)}")
    return target, content.replace(anchor, render_deep(item) + anchor, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    surfaces = [expected_route(data["route"]), *[expected_deep(item) for item in data["deep_offers"]]]
    changed = []
    for target, expected in surfaces:
        current = target.read_text(encoding="utf-8")
        if args.check:
            if current != expected:
                raise SystemExit(f"Regulatory Control v7 drift detected in {target.relative_to(ROOT)}")
        elif current != expected:
            target.write_text(expected, encoding="utf-8")
            changed.append(str(target.relative_to(ROOT)))
    if args.check:
        print("Regulatory Control v7 prototype --check: PASS (3/3)")
    elif changed:
        print("Materialized Regulatory Control v7 prototype: " + ", ".join(changed))
    else:
        print("Regulatory Control v7 prototype already materialized: 3/3")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Materialize the v7 Legal Intelligence public discovery layer on home and solutions hub."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-discovery-v70.json"
HOME_START = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HOME:START -->"
HOME_END = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HOME:END -->"
HUB_START = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HUB:START -->"
HUB_END = "<!-- LEGAL-INTELLIGENCE-DISCOVERY-V70-HUB:END -->"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def strip_block(content: str, start: str, end: str, label: str) -> str:
    if start not in content and end not in content:
        return content
    if content.count(start) != 1 or content.count(end) != 1:
        raise SystemExit(f"{label}: managed discovery markers are partial or duplicated")
    before, tail = content.split(start, 1)
    _, after = tail.split(end, 1)
    return before.rstrip() + "\n" + after.lstrip("\n")


def render_home(data: dict) -> str:
    cards = []
    for path in data["paths"]:
        cards.append(
            '<article class="v6-outcome" data-v7-li-discovery="%s">'
            '<b>%s</b><p class="v6-eyebrow">%s</p><h3>%s</h3><p>%s</p>'
            '<a class="v6-text-link" href="%s">%s →</a></article>'
            % (
                esc(path["label"].lower()),
                esc(path["number"]),
                esc(path["label"]),
                esc(path["title"]),
                esc(path["body"]),
                esc(path["href"]),
                esc(path["action"]),
            )
        )
    return (
        f"{HOME_START}\n"
        '<section class="v6-section" id="v7-legal-intelligence-discovery" aria-labelledby="v7-legal-intelligence-discovery-title" data-v7-legal-intelligence-discovery="home">'
        '<div class="v6-container"><div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(data["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v7-legal-intelligence-discovery-title">{esc(data["title"])}</h2>'
        f'<p class="v6-lead">{esc(data["lead"])}</p></div>'
        '<div class="v6-outcome-grid">' + ''.join(cards) + '</div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Cómo leer esta capa.</strong> {esc(data["boundary"])}</p>'
        '</div></div></section>\n'
        f"{HOME_END}\n"
    )


def render_hub(data: dict) -> str:
    areas = []
    for area in data["areas"]:
        areas.append(
            '<a href="%s" data-v7-li-area="true"><strong>%s</strong><p>%s</p><span>%s →</span></a>'
            % (esc(area["href"]), esc(area["title"]), esc(area["body"]), esc(area["action"]))
        )
    return (
        f"{HUB_START}\n"
        '<section class="v6-section" id="v7-legal-intelligence-discovery" aria-labelledby="v7-legal-intelligence-discovery-title" data-v7-legal-intelligence-discovery="hub">'
        '<div class="v6-container"><div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(data["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v7-legal-intelligence-discovery-title">{esc(data["title"])}</h2>'
        f'<p class="v6-lead">{esc(data["lead"])}</p></div>'
        '<div class="v6-hub-guide">' + ''.join(areas) + '</div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Arquitectura de navegación.</strong> {esc(data["boundary"])}</p>'
        '</div></div></section>\n'
        f"{HUB_END}\n"
    )


def expected(surface: dict, start: str, end: str, renderer) -> tuple[Path, str]:
    target = ROOT / surface["target"]
    if not target.exists():
        raise SystemExit(f"Missing discovery target: {surface['target']}")
    content = strip_block(target.read_text(encoding="utf-8"), start, end, surface["target"])
    anchor = surface["insert_before"]
    if content.count(anchor) != 1:
        raise SystemExit(f"{surface['target']}: expected exactly one insertion anchor; found {content.count(anchor)}")
    return target, content.replace(anchor, renderer(surface) + anchor, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    surfaces = [
        expected(data["home"], HOME_START, HOME_END, render_home),
        expected(data["hub"], HUB_START, HUB_END, render_hub),
    ]
    changed = []
    for target, expected_text in surfaces:
        current = target.read_text(encoding="utf-8")
        if args.check:
            if current != expected_text:
                raise SystemExit(f"Legal Intelligence discovery v7 drift detected in {target.relative_to(ROOT)}")
        elif current != expected_text:
            target.write_text(expected_text, encoding="utf-8")
            changed.append(str(target.relative_to(ROOT)))
    if args.check:
        print("Legal Intelligence public discovery v7 --check: PASS (home + solutions hub)")
    elif changed:
        print("Materialized Legal Intelligence public discovery v7: " + ", ".join(changed))
    else:
        print("Legal Intelligence public discovery v7 already materialized: 2/2")


if __name__ == "__main__":
    main()

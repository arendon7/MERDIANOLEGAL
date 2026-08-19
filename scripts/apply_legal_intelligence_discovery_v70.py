#!/usr/bin/env python3
"""Materialize the v7 Legal Intelligence public discovery layer on home and solutions hub.

When the v7.1 commercial-clarity contract exists, it supersedes the compact v7.0
copy while preserving the same managed boundaries and normalization entry point.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_V70 = ROOT / "assets/data/v7/legal-intelligence-discovery-v70.json"
CONTRACT_V71 = ROOT / "assets/data/v7/home-commercial-clarity-v71.json"
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


def render_legacy_home(data: dict) -> str:
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


def render_home(data: dict) -> str:
    if "modes" not in data:
        return render_legacy_home(data)

    modes = []
    for mode in data["modes"]:
        modes.append(
            '<article class="v6-timeline-row" data-v71-mode="%s">'
            '<span class="v6-timeline-num">%s</span>'
            '<strong class="v6-timeline-title">%s · %s</strong>'
            '<p class="v6-timeline-copy">%s <strong>%s</strong></p></article>'
            % (
                esc(mode["label"].lower()),
                esc(mode["number"]),
                esc(mode["label"]),
                esc(mode["title"]),
                esc(mode["body"]),
                esc(mode["result"]),
            )
        )

    paths = []
    for path in data["intelligence"]["paths"]:
        paths.append(
            '<article class="v6-outcome" data-v71-li-path="%s">'
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

    installed = []
    for item in data["installed"]["items"]:
        installed.append(
            '<div class="v6-evidence-row" data-v71-installed="%s"><b>%s</b><span>'
            '<strong>%s · %s.</strong> %s %s '
            '<a class="v6-text-link" href="%s">%s →</a>'
            '</span></div>'
            % (
                esc(item["name"].lower().replace(" ", "-")),
                esc(item["number"]),
                esc(item["name"]),
                esc(item["title"]),
                esc(item["body"]),
                esc(item["outcome"]),
                esc(item["href"]),
                esc(item["action"]),
            )
        )

    intelligence = data["intelligence"]
    installed_data = data["installed"]
    return (
        f"{HOME_START}\n"
        '<section class="v6-section" id="v71-commercial-clarity" aria-labelledby="v71-commercial-clarity-title" data-v71-commercial-clarity="home">'
        '<div class="v6-container">'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(data["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v71-commercial-clarity-title">{esc(data["title"])}</h2>'
        f'<p class="v6-lead">{esc(data["lead"])}</p></div>'
        '<div class="v6-method-line"></div><div class="v6-timeline" data-v71-modes="true">' + ''.join(modes) + '</div>'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(intelligence["eyebrow"])}</p>'
        f'<h2 class="v6-heading">{esc(intelligence["title"])}</h2>'
        f'<p class="v6-lead">{esc(intelligence["lead"])}</p></div>'
        '<div class="v6-outcome-grid" data-v71-intelligence="true">' + ''.join(paths) + '</div>'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(installed_data["eyebrow"])}</p>'
        f'<h2 class="v6-heading">{esc(installed_data["title"])}</h2>'
        f'<p class="v6-lead">{esc(installed_data["lead"])}</p></div>'
        '<div class="v6-evidence-list" data-v71-installed-list="true">' + ''.join(installed) + '</div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Límites de esta capa.</strong> {esc(data["boundary"])}</p>'
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
    surface_id = "v71-commercial-clarity-hub" if "v7.1" in data.get("eyebrow", "").lower() else "v7-legal-intelligence-discovery"
    if data.get("eyebrow") == "LEGAL INTELLIGENCE · CAPACIDADES TRANSVERSALES":
        surface_id = "v71-commercial-clarity-hub"
    return (
        f"{HUB_START}\n"
        f'<section class="v6-section" id="{surface_id}" aria-labelledby="{surface_id}-title" data-v7-legal-intelligence-discovery="hub">'
        '<div class="v6-container"><div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(data["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="{surface_id}-title">{esc(data["title"])}</h2>'
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
    contract = CONTRACT_V71 if CONTRACT_V71.exists() else CONTRACT_V70
    data = json.loads(contract.read_text(encoding="utf-8"))
    surfaces = [
        expected(data["home"], HOME_START, HOME_END, render_home),
        expected(data["hub"], HUB_START, HUB_END, render_hub),
    ]
    changed = []
    for target, expected_text in surfaces:
        current = target.read_text(encoding="utf-8")
        if args.check:
            if current != expected_text:
                raise SystemExit(f"Legal Intelligence discovery drift detected in {target.relative_to(ROOT)}")
        elif current != expected_text:
            target.write_text(expected_text, encoding="utf-8")
            changed.append(str(target.relative_to(ROOT)))
    if args.check:
        print(f"Legal Intelligence public discovery --check: PASS ({contract.name}, home + solutions hub)")
    elif changed:
        print("Materialized Legal Intelligence public discovery: " + ", ".join(changed))
    else:
        print("Legal Intelligence public discovery already materialized: 2/2")


if __name__ == "__main__":
    main()

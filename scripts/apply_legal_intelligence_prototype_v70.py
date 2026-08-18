#!/usr/bin/env python3
"""Materialize the v7 Legal Intelligence prototype on one representative solution route.

The prototype is intentionally narrow: one existing public surface, no new URL, no
new CSS layer and no mutation of the 16 canonical offer catalogs.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-prototype-v70.json"
START = "<!-- LEGAL-INTELLIGENCE-V70:START -->"
END = "<!-- LEGAL-INTELLIGENCE-V70:END -->"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def render(data: dict) -> str:
    section = data["section"]
    modes = []
    for item in section["modes"]:
        modes.append(
            '<article class="v6-route-option" data-v7-intervention="%s">'
            '<p class="v6-eyebrow">%s · %s</p>'
            '<h3>%s</h3>'
            '<p>%s</p>'
            '<a href="%s">%s →</a>'
            '</article>'
            % (
                esc(item["label"].lower()),
                esc(item["number"]),
                esc(item["label"]),
                esc(item["title"]),
                esc(item["body"]),
                esc(item["href"]),
                esc(item["action"]),
            )
        )

    engineering = section["engineering"]
    return (
        f"{START}\n"
        '<section class="v6-section" id="v7-legal-intelligence" aria-labelledby="v7-legal-intelligence-title" data-v7-legal-intelligence="prototype">'
        '<div class="v6-container">'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(section["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="v7-legal-intelligence-title">{esc(section["title"])}</h2>'
        f'<p class="v6-lead">{esc(section["lead"])}</p>'
        '</div>'
        '<div class="v6-route-list" aria-label="Formas de intervención de Meridiano Legal Intelligence">'
        + ''.join(modes)
        + '</div>'
        '<div class="v6-pricing-note" data-v7-legal-engineering="true"><div>'
        '<p class="v6-eyebrow">LEGAL ENGINEERING</p>'
        f'<h3>{esc(engineering["title"])}</h3>'
        f'<p>{esc(engineering["body"])}</p>'
        f'</div><a href="{esc(engineering["href"])}">{esc(engineering["action"])} →</a></div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Alcance tecnológico.</strong> {esc(section["boundary"])}</p>'
        '</div>'
        '</div></section>\n'
        f"{END}\n"
    )


def strip_existing(content: str) -> str:
    if START not in content and END not in content:
        return content
    if content.count(START) != 1 or content.count(END) != 1:
        raise SystemExit("Prototype markers are partial or duplicated; refusing to continue.")
    before, tail = content.split(START, 1)
    _, after = tail.split(END, 1)
    return before.rstrip() + "\n" + after.lstrip("\n")


def materialized_content(data: dict) -> tuple[Path, str]:
    target = ROOT / data["target"]
    if not target.exists():
        raise SystemExit(f"Missing prototype target: {data['target']}")
    content = strip_existing(target.read_text(encoding="utf-8"))
    anchor = data["insert_before"]
    if content.count(anchor) != 1:
        raise SystemExit(f"Expected exactly one insertion anchor in {data['target']}; found {content.count(anchor)}")
    block = render(data)
    return target, content.replace(anchor, block + anchor, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if the committed prototype has drift.")
    args = parser.parse_args()

    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    target, expected = materialized_content(data)
    current = target.read_text(encoding="utf-8")

    if args.check:
        if current != expected:
            raise SystemExit(f"v7 Legal Intelligence prototype drift detected in {target.relative_to(ROOT)}")
        print(f"v7 Legal Intelligence prototype --check: PASS ({target.relative_to(ROOT)})")
        return

    if current == expected:
        print(f"v7 Legal Intelligence prototype already materialized: {target.relative_to(ROOT)}")
        return

    target.write_text(expected, encoding="utf-8")
    print(f"Materialized v7 Legal Intelligence prototype: {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

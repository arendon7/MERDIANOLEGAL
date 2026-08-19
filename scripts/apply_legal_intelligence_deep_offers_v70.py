#!/usr/bin/env python3
"""Materialize v7 Legal Intelligence positioning on two existing deep offers.

This layer does not mutate catalog truth or create new URLs. It only explains how
existing canonical offers connect to the Legal Intelligence architecture.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v7/legal-intelligence-deep-offers-v70.json"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def markers(item: dict) -> tuple[str, str]:
    key = item["id"].upper().replace("-", "_")
    return f"<!-- LEGAL-INTELLIGENCE-V70-{key}:START -->", f"<!-- LEGAL-INTELLIGENCE-V70-{key}:END -->"


def render(item: dict) -> str:
    start, end = markers(item)
    rows = []
    for row in item["items"]:
        rows.append(
            '<div class="v6-result-item">'
            f'<b>{esc(row["number"])}</b>'
            f'<span><strong>{esc(row["title"])}.</strong> {esc(row["body"])}</span>'
            '</div>'
        )
    nxt = item["next_step"]
    section_id = f'v7-{item["id"]}'
    return (
        f"{start}\n"
        f'<section class="v6-section v6-result" id="{esc(section_id)}" aria-labelledby="{esc(section_id)}-title" data-v7-deep-offer="{esc(item["id"])}">'
        '<div class="v6-container v6-result-grid">'
        '<div class="v6-section-head">'
        f'<p class="v6-eyebrow">{esc(item["eyebrow"])}</p>'
        f'<h2 class="v6-heading" id="{esc(section_id)}-title">{esc(item["title"])}</h2>'
        f'<p class="v6-lead">{esc(item["lead"])}</p>'
        '</div>'
        '<div class="v6-result-list">' + ''.join(rows) + '</div>'
        '</div>'
        '<div class="v6-container">'
        '<div class="v6-pricing-note" data-v7-next-step="true"><div>'
        '<p class="v6-eyebrow">CONTINUIDAD</p>'
        f'<h3>{esc(nxt["title"])}</h3>'
        f'<p>{esc(nxt["body"])}</p>'
        f'</div><a href="{esc(nxt["href"])}">{esc(nxt["action"])} →</a></div>'
        '<div class="v6-boundary-note" data-v7-capability-boundary="true">'
        f'<p><strong>Frontera de alcance.</strong> {esc(item["boundary"])}</p>'
        '</div>'
        '</div></section>\n'
        f"{end}\n"
    )


def strip_existing(content: str, item: dict) -> str:
    start, end = markers(item)
    if start not in content and end not in content:
        return content
    if content.count(start) != 1 or content.count(end) != 1:
        raise SystemExit(f"{item['target']}: deep-offer markers are partial or duplicated")
    before, tail = content.split(start, 1)
    _, after = tail.split(end, 1)
    return before.rstrip() + "\n" + after.lstrip("\n")


def expected_content(item: dict) -> tuple[Path, str]:
    target = ROOT / item["target"]
    if not target.exists():
        raise SystemExit(f"Missing deep-offer target: {item['target']}")
    content = strip_existing(target.read_text(encoding="utf-8"), item)
    anchor = item["insert_before"]
    if content.count(anchor) != 1:
        raise SystemExit(f"{item['target']}: expected exactly one insertion anchor; found {content.count(anchor)}")
    return target, content.replace(anchor, render(item) + anchor, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    changed = []
    for item in data["targets"]:
        target, expected = expected_content(item)
        current = target.read_text(encoding="utf-8")
        if args.check:
            if current != expected:
                raise SystemExit(f"v7 deep-offer drift detected in {target.relative_to(ROOT)}")
            continue
        if current != expected:
            target.write_text(expected, encoding="utf-8")
            changed.append(str(target.relative_to(ROOT)))
    if args.check:
        print("v7 Legal Intelligence deep offers --check: PASS (2/2)")
    elif changed:
        print("Materialized v7 Legal Intelligence deep offers: " + ", ".join(changed))
    else:
        print("v7 Legal Intelligence deep offers already materialized: 2/2")


if __name__ == "__main__":
    main()

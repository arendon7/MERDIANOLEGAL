#!/usr/bin/env python3
"""Valida Wave 4 v6: ocho sectores derivados de su HTML editorial canónico."""
from __future__ import annotations

from html import unescape
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SECTORS = ROOT / "sectores"
START = "<!-- EXPERIENCE-V60-SECTOR:START -->"
END = "<!-- EXPERIENCE-V60-SECTOR:END -->"
LEGACY_START = "<!-- EXPERIENCE-V60-SECTOR-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-SECTOR-LEGACY:END -->"
STYLE_PATHS = [
    "../assets/css/v6/tokens.css",
    "../assets/css/v6/base.css",
    "../assets/css/v6/components.css",
    "../assets/css/v6/surfaces.css",
    "../assets/css/v6/sectors.css",
]


def fail(message: str) -> None:
    raise AssertionError(message)


def clean(fragment: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(unescape(value).split())


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_once(value: str, needle: str, label: str) -> None:
    count = value.count(needle)
    if count != 1:
        fail(f"{label}: esperaba una ocurrencia de {needle!r}; encontró {count}")


def assert_contains(value: str, needles: list[str], label: str) -> None:
    missing = [item for item in needles if item and item not in value]
    if missing:
        fail(f"{label}: faltan {missing[:8]}" + (f" (+{len(missing)-8})" if len(missing) > 8 else ""))


def legacy_block(value: str, label: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r"(.*?)" + re.escape(LEGACY_END), value, flags=re.S)
    if not match:
        fail(f"{label}: falta documento editorial preservado")
    return match.group(1)


def first_layer(value: str, label: str) -> str:
    start = value.find(START)
    legacy = value.find(LEGACY_START, start + len(START)) if start >= 0 else -1
    if start < 0 or legacy < 0:
        fail(f"{label}: no se pudo aislar primera capa sectorial")
    return unescape(value[start:legacy])


def section_by_id(value: str, section_id: str) -> str:
    match = re.search(rf'<section\b[^>]*id="{re.escape(section_id)}"[^>]*>.*?</section>', value, flags=re.S)
    if not match:
        fail(f"legacy: falta #{section_id}")
    return match.group(0)


def section_containing(value: str, needle: str) -> str:
    pos = value.find(needle)
    if pos < 0:
        fail(f"legacy: falta {needle!r}")
    start = value.rfind("<section", 0, pos)
    end = value.find("</section>", pos)
    if start < 0 or end < 0:
        fail(f"legacy: no se aisló sección {needle!r}")
    return value[start:end + len("</section>")]


def tag_text(fragment: str, tag: str, class_name: str | None = None) -> str:
    class_part = rf'[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*' if class_name else r"[^>]*"
    match = re.search(rf"<{tag}{class_part}>(.*?)</{tag}>", fragment, flags=re.S | re.I)
    return clean(match.group(1)) if match else ""


def article_truth(fragment: str) -> list[str]:
    truth: list[str] = []
    for raw in re.findall(r"<article\b[^>]*>(.*?)</article>", fragment, flags=re.S | re.I):
        for tag in ("span", "h3", "strong", "p"):
            value = tag_text(raw, tag)
            if value:
                truth.append(value)
        link = re.search(r'<a\b[^>]*href="([^"]+)"[^>]*>', raw, flags=re.S | re.I)
        if link:
            truth.append(unescape(link.group(1)))
    return truth


def related_truth(fragment: str) -> list[str]:
    truth: list[str] = []
    for href, raw in re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', fragment, flags=re.S | re.I):
        truth.append(unescape(href))
        for tag in ("span", "strong", "small"):
            value = tag_text(raw, tag)
            if value:
                truth.append(value)
    return truth


def validate_sector(path: Path) -> None:
    slug = path.stem
    value = text(path)
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="sectors"',
        f'data-experience-surface="sector:{slug}"', f'data-experience-v60="sector:{slug}"',
    ], slug)
    for href in STYLE_PATHS:
        assert_once(value, f'href="{href}"', f"{slug}: estilos")
    assert_once(value, START, f"{slug}: marker")
    assert_once(value, END, f"{slug}: marker")
    if re.search(r"<form\b", value):
        fail(f"{slug}: un sector no debe crear formulario físico")

    old = legacy_block(value, slug)
    first = first_layer(value, slug)

    hero = section_containing(old, 'class="sector-hero"')
    focus = section_by_id(old, "sector-enfoque")
    decisions = section_by_id(old, "sector-decisiones")
    risks = section_by_id(old, "sector-riesgos")
    map_section = section_containing(old, 'class="map-grid"')
    intervention = section_containing(old, "INTERVENCIÓN MERIDIANO")
    fit = section_containing(old, 'class="fit-band"')
    related = section_containing(old, 'class="related-grid"')
    authority = re.search(r'<!-- AUTHORITY-V53-SECTOR:START -->(.*?)<!-- AUTHORITY-V53-SECTOR:END -->', old, flags=re.S)
    closing = section_by_id(old, "sector-contacto")
    if not authority:
        fail(f"{slug}: falta autoridad v5.3 en legacy")

    expected = [tag_text(hero, "h1"), tag_text(hero, "p", "lead"), tag_text(focus, "h2"), tag_text(decisions, "h2"), tag_text(map_section, "h2"), tag_text(risks, "h2"), tag_text(intervention, "h2"), tag_text(related, "h2"), tag_text(closing, "h2")]
    brief = re.search(r'<aside\b[^>]*class="[^"]*sector-brief[^"]*"[^>]*>(.*?)</aside>', hero, flags=re.S)
    if brief:
        expected.extend(clean(item) for item in re.findall(r"<li\b[^>]*>(.*?)</li>", brief.group(1), flags=re.S))
    prose = re.search(r'<div\b[^>]*class="[^"]*prose[^"]*"[^>]*>(.*?)</div>', focus, flags=re.S)
    if prose:
        expected.extend(clean(item) for item in re.findall(r"<p\b[^>]*>(.*?)</p>", prose.group(1), flags=re.S))
    expected.extend(article_truth(decisions))
    expected.extend(article_truth(map_section))
    expected.extend(article_truth(risks))
    expected.extend(article_truth(intervention))
    expected.extend(article_truth(fit))
    expected.extend(article_truth(authority.group(1)))
    related_grid = re.search(r'<div\b[^>]*class="[^"]*related-grid[^"]*"[^>]*>(.*?)</div>', related, flags=re.S)
    if related_grid:
        expected.extend(related_truth(related_grid.group(1)))
    assert_contains(first, expected, f"{slug}: primera capa/editorial truth")

    # El documento editorial completo y sus contratos gestionados deben seguir únicos.
    for marker in (
        "EDITORIAL-SEO:START", "EDITORIAL-JOURNEY:START", "EDITORIAL-SEQUENCE:START", "EDITORIAL-SCRIPT:START",
        "AUTHORITY-V53-SECTOR:START", 'data-authority-v53="item-list"', "MEASUREMENT-V53:START",
        'id="sector-enfoque"', 'id="sector-decisiones"', 'id="sector-riesgos"', 'id="sector-contacto"',
    ):
        assert_once(value, marker, f"{slug}: contrato editorial")
    for managed in re.findall(r'data-authority-solution="([^"]+)"', old):
        if value.count(f'data-authority-solution="{managed}"') != 1:
            fail(f"{slug}: data-authority-solution {managed} debe permanecer único")


def main() -> int:
    paths = sorted(SECTORS.glob("*.html"))
    if len(paths) != 8:
        fail(f"se esperaban 8 sectores y hay {len(paths)}")
    for path in paths:
        validate_sector(path)
    print("VALIDATE EXPERIENCE V6 WAVE 4 OK: 8/8 sectores con truth editorial visible y contratos SEO/authority/context preservados.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE EXPERIENCE V6 WAVE 4 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

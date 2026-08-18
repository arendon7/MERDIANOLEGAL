#!/usr/bin/env python3
"""Valida Wave 5 v6: seis perspectivas abiertas y hub editorial."""
from __future__ import annotations

from html import unescape
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PERSPECTIVES = ROOT / "perspectivas"
HUB = ROOT / "perspectivas.html"
ARTICLE_START = "<!-- EXPERIENCE-V60-PERSPECTIVE:START -->"
ARTICLE_END = "<!-- EXPERIENCE-V60-PERSPECTIVE:END -->"
HUB_START = "<!-- EXPERIENCE-V60-PERSPECTIVES-HUB:START -->"
HUB_END = "<!-- EXPERIENCE-V60-PERSPECTIVES-HUB:END -->"
HUB_LEGACY_START = "<!-- EXPERIENCE-V60-PERSPECTIVES-HUB-LEGACY:START -->"
HUB_LEGACY_END = "<!-- EXPERIENCE-V60-PERSPECTIVES-HUB-LEGACY:END -->"
ARTICLE_STYLES = [
    "../assets/css/v6/tokens.css",
    "../assets/css/v6/base.css",
    "../assets/css/v6/components.css",
    "../assets/css/v6/surfaces.css",
    "../assets/css/v6/perspectives.css",
]
HUB_STYLES = [href[3:] for href in ARTICLE_STYLES]


def fail(message: str) -> None:
    raise AssertionError(message)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def clean(fragment: str) -> str:
    value = re.sub(r"<[^>]+>", " ", fragment)
    return " ".join(unescape(value).split())


def assert_once(value: str, needle: str, label: str) -> None:
    count = value.count(needle)
    if count != 1:
        fail(f"{label}: esperaba una ocurrencia de {needle!r}; encontró {count}")


def assert_contains(value: str, needles: list[str], label: str) -> None:
    missing = [item for item in needles if item and item not in value]
    if missing:
        fail(f"{label}: faltan {missing[:8]}" + (f" (+{len(missing)-8})" if len(missing) > 8 else ""))


def tag_text(fragment: str, tag: str, class_name: str | None = None) -> str:
    class_part = rf'[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*' if class_name else r"[^>]*"
    match = re.search(rf"<{tag}{class_part}>(.*?)</{tag}>", fragment, flags=re.S | re.I)
    return clean(match.group(1)) if match else ""


def balanced_tag_block(value: str, tag: str, class_name: str) -> str:
    opening = re.search(
        rf'<{tag}\b[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*>',
        value,
        flags=re.I,
    )
    if not opening:
        fail(f"falta {tag}.{class_name}")
    token_re = re.compile(rf'</?{tag}\b[^>]*>', flags=re.I)
    depth = 0
    for token in token_re.finditer(value, opening.start()):
        raw = token.group(0)
        if raw.startswith("</"):
            depth -= 1
            if depth == 0:
                return value[opening.start():token.end()]
        elif not raw.rstrip().endswith("/>"):
            depth += 1
    fail(f"{tag}.{class_name} no está balanceado")
    return ""


def validate_article(path: Path) -> None:
    slug = path.stem
    value = text(path)
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="perspectives"',
        f'data-experience-surface="perspective:{slug}"', f'data-experience-v60="perspective:{slug}"',
    ], slug)
    for href in ARTICLE_STYLES:
        assert_once(value, f'href="{href}"', f"{slug}: estilos")
    assert_once(value, ARTICLE_START, f"{slug}: marker")
    assert_once(value, ARTICLE_END, f"{slug}: marker")
    assert_once(value, 'class="article-body"', f"{slug}: cuerpo editorial")
    assert_once(value, "AUTHORITY-V53-PERSPECTIVE:START", f"{slug}: autoridad")
    assert_once(value, "AUTHORITY-V53-PERSPECTIVE:END", f"{slug}: autoridad")
    assert_once(value, 'data-authority-v53="item-list"', f"{slug}: schema autoridad")
    assert_once(value, "EDITORIAL-V47-CONVERSION:START", f"{slug}: conversión editorial")
    assert_once(value, "EDITORIAL-SEQUENCE:START", f"{slug}: secuencia editorial")
    assert_once(value, "MEASUREMENT-V53:START", f"{slug}: medición")
    if re.search(r"<form\b", value):
        fail(f"{slug}: una perspectiva no debe crear formulario")

    article_pos = value.find('class="article-body"')
    if article_pos < 0:
        fail(f"{slug}: falta cuerpo")
    for details in re.finditer(r"<details\b[^>]*>.*?</details>", value, flags=re.S):
        if details.start() <= article_pos <= details.end():
            fail(f"{slug}: el cuerpo editorial no puede quedar plegado")

    hero = re.search(r'<section\b[^>]*class="[^"]*v6-perspective-hero[^"]*"[^>]*>(.*?)</section>', value, flags=re.S)
    guide = re.search(r'<section\b[^>]*class="[^"]*v6-reading-guide[^"]*"[^>]*>(.*?)</section>', value, flags=re.S)
    if not hero or not guide:
        fail(f"{slug}: hero o guía v6 ausente")
    body = balanced_tag_block(value, "article", "article-body")
    aside = balanced_tag_block(value, "aside", "article-aside")
    if not body or not aside:
        fail(f"{slug}: estructura de lectura v6 incompleta")

    title = tag_text(hero.group(1), "h1")
    lead = tag_text(hero.group(1), "p", "v6-lead")
    if not title or not lead:
        fail(f"{slug}: hero editorial incompleto")

    guide_links = re.findall(r'<a\b[^>]*href="#([^"]+)"', guide.group(1))
    if not guide_links:
        fail(f"{slug}: guía de lectura sin destinos")
    missing_targets = [target for target in guide_links if f'id="{target}"' not in body]
    if missing_targets:
        fail(f"{slug}: cuerpo editorial truncado; faltan destinos {missing_targets}")
    body_h2_ids = set(re.findall(r'<h2\b[^>]*id="([^"]+)"', body))
    if not set(guide_links).issubset(body_h2_ids):
        fail(f"{slug}: recorrido y secciones del cuerpo no coinciden")
    if body.count("<article") != body.count("</article>"):
        fail(f"{slug}: article-body quedó desbalanceado")

    if "LECTURAS RELACIONADAS" not in value or "DE LA LECTURA A LA DECISIÓN" not in value:
        fail(f"{slug}: faltan conexiones editoriales/autoridad")
    for managed in re.findall(r'data-authority-solution="([^"]+)"', value):
        if value.count(f'data-authority-solution="{managed}"') != 1:
            fail(f"{slug}: autoridad {managed} duplicada")


def hub_legacy(value: str) -> str:
    match = re.search(re.escape(HUB_LEGACY_START) + r"(.*?)" + re.escape(HUB_LEGACY_END), value, flags=re.S)
    if not match:
        fail("hub: falta biblioteca v5.31 preservada")
    return match.group(1)


def hub_cards(fragment: str) -> list[tuple[str, str, str]]:
    result = []
    seen = set()
    for href, raw in re.findall(r'<a\b[^>]*class="[^"]*(?:featured-card|insight-card)[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', fragment, flags=re.S):
        if href in seen:
            continue
        seen.add(href)
        result.append((unescape(href), tag_text(raw, "h2") or tag_text(raw, "h3"), tag_text(raw, "p")))
    return result


def validate_hub() -> None:
    value = text(HUB)
    assert_contains(value, [
        'data-experience-system="v6"', 'data-experience-wave="perspectives"',
        'data-experience-surface="perspectives-hub"', 'data-experience-v60="perspectives-hub"',
    ], "hub")
    for href in HUB_STYLES:
        assert_once(value, f'href="{href}"', "hub: estilos")
    assert_once(value, HUB_START, "hub marker")
    assert_once(value, HUB_END, "hub marker")
    old = hub_legacy(value)
    cards = hub_cards(old)
    if len(cards) != 6:
        fail(f"hub legacy: esperaba 6 lecturas únicas y encontró {len(cards)}")
    first_end = value.find(HUB_LEGACY_START)
    first = unescape(value[value.find(HUB_START):first_end])
    for href, title, copy in cards:
        assert_contains(first, [href, title, copy], "hub: tarjeta v6/source truth")
    if first.count('class="v6-library-card"') != 6:
        fail("hub: primera capa debe mostrar exactamente seis perspectivas")
    assert_contains(old, ["LECTURAS DESTACADAS", "BIBLIOTECA", "CRITERIOS EDITORIALES", "DE LA LECTURA A LA DECISIÓN"], "hub legacy")
    if re.search(r"<form\b", value):
        fail("hub perspectivas no debe crear formulario")


def main() -> int:
    paths = sorted(PERSPECTIVES.glob("*.html"))
    if len(paths) != 6:
        fail(f"se esperaban 6 perspectivas y hay {len(paths)}")
    for path in paths:
        validate_article(path)
    validate_hub()
    print("VALIDATE EXPERIENCE V6 WAVE 5 OK: 6 artículos abiertos completos + hub, autoridad/editorial intactos y recorrido proporcional al cuerpo.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE EXPERIENCE V6 WAVE 5 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

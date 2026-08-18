#!/usr/bin/env python3
"""Materializa Wave 4 v6 sobre los ocho sectores desde su HTML editorial canónico.

No crea un catálogo sectorial paralelo. La fuente sustantiva sigue siendo el HTML que
`enrich_editorial_pages.py` enriquece con SEO/contexto. v6 parsea esa fuente, construye
una primera lectura orientada a decisiones y conserva el documento editorial completo.
"""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
import re

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


def e(value: object) -> str:
    return escape(str(value), quote=True)


def clean(fragment: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(unescape(value).split())


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return unescape(match.group(1)) if match else ""


def find_tag(fragment: str, tag: str, class_name: str | None = None) -> str:
    class_part = rf'[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*' if class_name else r"[^>]*"
    match = re.search(rf"<{tag}{class_part}>(.*?)</{tag}>", fragment, flags=re.S | re.I)
    return clean(match.group(1)) if match else ""


def all_tags(fragment: str, tag: str) -> list[str]:
    return [clean(item) for item in re.findall(rf"<{tag}\b[^>]*>(.*?)</{tag}>", fragment, flags=re.S | re.I)]


def section_by_id(value: str, section_id: str) -> str:
    match = re.search(rf'<section\b[^>]*id="{re.escape(section_id)}"[^>]*>.*?</section>', value, flags=re.S)
    if not match:
        raise RuntimeError(f"sector: falta sección #{section_id}")
    return match.group(0)


def section_containing(value: str, needle: str) -> str:
    pos = value.find(needle)
    if pos < 0:
        raise RuntimeError(f"sector: falta bloque que contiene {needle!r}")
    start = value.rfind("<section", 0, pos)
    end = value.find("</section>", pos)
    if start < 0 or end < 0:
        raise RuntimeError(f"sector: no se pudo aislar sección con {needle!r}")
    return value[start:end + len("</section>")]


def articles(fragment: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for raw in re.findall(r"<article\b[^>]*>(.*?)</article>", fragment, flags=re.S | re.I):
        label = find_tag(raw, "span") or find_tag(raw, "b")
        title = find_tag(raw, "h3") or find_tag(raw, "strong")
        copy = find_tag(raw, "p") or (find_tag(raw, "span") if title else "")
        link = re.search(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', raw, flags=re.S | re.I)
        result.append({
            "label": label,
            "title": title,
            "copy": copy,
            "href": unescape(link.group(1)) if link else "",
            "link_text": clean(link.group(2)) if link else "",
        })
    return result


def related_links(fragment: str) -> list[dict[str, str]]:
    result = []
    for href, raw in re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', fragment, flags=re.S | re.I):
        result.append({
            "href": unescape(href),
            "label": find_tag(raw, "span"),
            "title": find_tag(raw, "strong"),
            "copy": find_tag(raw, "small"),
        })
    return result


def extract_legacy(main: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r"(.*?)" + re.escape(LEGACY_END), main, flags=re.S)
    return match.group(1) if match else main


def extract_main(text: str) -> tuple[re.Match[str], str]:
    match = re.search(r'<main id="contenido"[^>]*>(.*?)</main>', text, flags=re.S)
    if not match:
        raise RuntimeError("sector sin <main id=contenido>")
    return match, match.group(1)


def ensure_styles(text: str) -> str:
    for href in STYLE_PATHS:
        text = re.sub(rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(href)}">\s*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("sector sin </head>")
    links = "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in STYLE_PATHS)
    return text.replace("</head>", f"{links}\n</head>", 1)


def mark_body(text: str, slug: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        for attr in ("data-experience-system", "data-experience-wave", "data-experience-surface"):
            tag = re.sub(rf'\s{attr}="[^"]*"', "", tag)
        return tag[:-1] + f' data-experience-system="v6" data-experience-wave="sectors" data-experience-surface="sector:{e(slug)}">'
    return re.sub(r"<body\b[^>]*>", repl, text, count=1)


def parse_sector(legacy: str, full_text: str, slug: str) -> dict:
    hero = section_containing(legacy, 'class="sector-hero"')
    focus = section_by_id(legacy, "sector-enfoque")
    decisions = section_by_id(legacy, "sector-decisiones")
    risks = section_by_id(legacy, "sector-riesgos")
    map_section = section_containing(legacy, 'class="map-grid"')
    intervention = section_containing(legacy, "INTERVENCIÓN MERIDIANO")
    fit = section_containing(legacy, 'class="fit-band"')
    related = section_containing(legacy, 'class="related-grid"')
    authority_match = re.search(r'<!-- AUTHORITY-V53-SECTOR:START -->(.*?)<!-- AUTHORITY-V53-SECTOR:END -->', legacy, flags=re.S)
    if not authority_match:
        raise RuntimeError(f"{slug}: falta autoridad sectorial v5.3")
    authority = authority_match.group(1)
    closing = section_by_id(legacy, "sector-contacto")

    hero_title = find_tag(hero, "h1")
    hero_lead = find_tag(hero, "p", "lead")
    brief_match = re.search(r'<aside\b[^>]*class="[^"]*sector-brief[^"]*"[^>]*>(.*?)</aside>', hero, flags=re.S)
    brief = all_tags(brief_match.group(1), "li") if brief_match else []
    prose_match = re.search(r'<div\b[^>]*class="[^"]*prose[^"]*"[^>]*>(.*?)</div>', focus, flags=re.S)
    prose = all_tags(prose_match.group(1), "p") if prose_match else []
    if not hero_title or not hero_lead or len(brief) < 3 or len(prose) < 2:
        raise RuntimeError(f"{slug}: hero/enfoque editorial incompleto")

    related_grid = re.search(r'<div\b[^>]*class="[^"]*related-grid[^"]*"[^>]*>(.*?)</div>', related, flags=re.S)
    closing_link = re.search(r'<a\b[^>]*class="[^"]*btn-gold[^"]*"[^>]*href="([^"]+)"', closing, flags=re.S)
    if not closing_link:
        closing_link = re.search(r'<a\b[^>]*href="([^"]*#contacto)"', closing, flags=re.S)
    if not closing_link:
        raise RuntimeError(f"{slug}: cierre sin CTA contextual")

    return {
        "slug": slug,
        "page_title": body_attr(full_text, "data-page-title"),
        "need": body_attr(full_text, "data-page-need"),
        "eyebrow": find_tag(hero, "p", "eyebrow"),
        "hero_title": hero_title,
        "hero_lead": hero_lead,
        "brief": brief,
        "focus_title": find_tag(focus, "h2"),
        "focus_prose": prose,
        "decisions_title": find_tag(decisions, "h2"),
        "decisions": articles(decisions),
        "map_title": find_tag(map_section, "h2"),
        "map": articles(map_section),
        "risks_title": find_tag(risks, "h2"),
        "risks": articles(risks),
        "intervention_title": find_tag(intervention, "h2"),
        "interventions": articles(intervention),
        "moments": articles(fit),
        "readings_title": find_tag(related, "h2"),
        "readings": related_links(related_grid.group(1) if related_grid else ""),
        "routes": articles(authority),
        "closing_title": find_tag(closing, "h2"),
        "closing_copy": find_tag(closing, "p") if find_tag(closing, "p") != "SIGUIENTE PASO" else "",
        "contact_href": unescape(closing_link.group(1)),
    }


def render_offer_rows(items: list[dict[str, str]]) -> str:
    rows = []
    for item in items:
        link = f'<a href="{e(item["href"])}">{e(item["link_text"] or "Explorar →")}</a>' if item["href"] else ""
        rows.append(f'<article class="v6-sector-offer"><b>{e(item["label"])}</b><strong>{e(item["title"])}</strong><p>{e(item["copy"])}</p>{link}</article>')
    return "".join(rows)


def render_sector(data: dict, legacy: str) -> str:
    brief = "".join(f"<li>{e(item)}</li>" for item in data["brief"])
    prose = "".join(f"<p>{e(item)}</p>" for item in data["focus_prose"])
    decision_rows = "".join(
        f'<article class="v6-sector-decision-row"><b>{e(item["label"])}</b><strong>{e(item["title"])}</strong><p>{e(item["copy"])}</p></article>'
        for item in data["decisions"]
    )
    map_rows = "".join(
        f'<article class="v6-sector-map-item"><b>{idx:02d}</b><strong>{e(item["title"])}</strong><p>{e(item["copy"])}</p></article>'
        for idx, item in enumerate(data["map"], 1)
    )
    risk_rows = "".join(
        f'<article class="v6-sector-risk"><b>{e(item["label"])}</b><h3>{e(item["title"])}</h3><p>{e(item["copy"])}</p></article>'
        for item in data["risks"]
    )
    moments = "".join(
        f'<article class="v6-sector-moment"><strong>{e(item["title"])}</strong><span>{e(item["copy"])}</span></article>'
        for item in data["moments"]
    )
    readings = "".join(
        f'<article class="v6-sector-reading"><b>{e(item["label"])}</b><strong>{e(item["title"])}</strong><span>{e(item["copy"])}</span><a href="{e(item["href"])}">Leer →</a></article>'
        for item in data["readings"]
    )
    return f'''{START}
<section class="v6-hero v6-sector-hero" aria-labelledby="v6-sector-title"><div class="v6-container v6-hero-grid"><div class="v6-hero-copy"><p class="v6-eyebrow">{e(data['eyebrow'])}</p><h1 class="v6-display" id="v6-sector-title">{e(data['hero_title'])}</h1><p class="v6-lead">{e(data['hero_lead'])}</p><div class="v6-actions"><a class="v6-btn" href="{e(data['contact_href'])}">Presentar una necesidad →</a><a class="v6-btn v6-btn-secondary" href="#v6-sector-decisions">Ver decisiones frecuentes</a></div></div><aside class="v6-sector-brief"><span>DECISIONES FRECUENTES</span><ol>{brief}</ol></aside></div></section>
<section class="v6-section v6-sector-context" id="v6-sector-context" aria-labelledby="v6-sector-context-title"><div class="v6-container v6-sector-context-grid"><div class="v6-section-head"><p class="v6-eyebrow">CONTEXTO SECTORIAL</p><h2 class="v6-heading" id="v6-sector-context-title">{e(data['focus_title'])}</h2></div><div class="v6-sector-prose">{prose}</div></div></section>
<section class="v6-section v6-sector-decisions" id="v6-sector-decisions" aria-labelledby="v6-sector-decisions-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">DECISIONES JURÍDICAS</p><h2 class="v6-heading" id="v6-sector-decisions-title">{e(data['decisions_title'])}</h2></div><div class="v6-sector-decision-list">{decision_rows}</div></div></section>
<section class="v6-section v6-sector-map" id="v6-sector-map" aria-labelledby="v6-sector-map-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">MAPA JURÍDICO-OPERATIVO</p><h2 class="v6-heading" id="v6-sector-map-title">{e(data['map_title'])}</h2></div><div class="v6-sector-map-grid">{map_rows}</div></div></section>
<section class="v6-section v6-sector-risks" id="v6-sector-risks" aria-labelledby="v6-sector-risks-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">SEÑALES DE REVISIÓN</p><h2 class="v6-heading" id="v6-sector-risks-title">{e(data['risks_title'])}</h2></div><div class="v6-sector-risk-grid">{risk_rows}</div></div></section>
<section class="v6-section v6-sector-interventions" id="v6-sector-interventions" aria-labelledby="v6-sector-interventions-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">INTERVENCIÓN MERIDIANO</p><h2 class="v6-heading" id="v6-sector-interventions-title">{e(data['intervention_title'])}</h2></div><div class="v6-sector-offer-list">{render_offer_rows(data['interventions'])}</div></div></section>
<section class="v6-section v6-sector-moments" aria-labelledby="v6-sector-moments-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">MOMENTOS DE DECISIÓN</p><h2 class="v6-heading" id="v6-sector-moments-title">Cuándo conviene anticipar la revisión jurídica.</h2></div><div class="v6-sector-moment-grid">{moments}</div></div></section>
<section class="v6-section v6-sector-routes" aria-labelledby="v6-sector-routes-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">RUTAS POR SITUACIÓN</p><h2 class="v6-heading" id="v6-sector-routes-title">Conecte el contexto sectorial con la decisión concreta que debe resolver.</h2></div><div class="v6-sector-offer-list">{render_offer_rows(data['routes'])}</div></div></section>
<section class="v6-section" aria-labelledby="v6-sector-readings-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">LECTURAS RELACIONADAS</p><h2 class="v6-heading" id="v6-sector-readings-title">{e(data['readings_title'])}</h2></div><div class="v6-sector-reading-list">{readings}</div></div></section>
<section class="v6-section v6-sector-cta" aria-labelledby="v6-sector-cta-title"><div class="v6-container v6-sector-cta-grid"><div><p class="v6-eyebrow">SIGUIENTE PASO</p><h2 class="v6-heading" id="v6-sector-cta-title">{e(data['closing_title'])}</h2><p class="v6-lead">{e(data['closing_copy'])}</p></div><a class="v6-btn" href="{e(data['contact_href'])}">Presentar necesidad →</a></div></section>
<details class="v6-depth v6-sector-depth"><summary><span>PROFUNDIDAD SECTORIAL</span><strong>Ver lectura editorial completa, autoridad, navegación y referencias relacionadas</strong></summary><div class="v6-depth-inner">{LEGACY_START}{legacy}{LEGACY_END}</div></details>
{END}'''


def main() -> int:
    paths = sorted(SECTORS.glob("*.html"))
    if len(paths) != 8:
        raise RuntimeError(f"Wave 4 requiere 8 sectores y encontró {len(paths)}")
    for path in paths:
        slug = path.stem
        text = path.read_text(encoding="utf-8")
        text = ensure_styles(text)
        text = mark_body(text, slug)
        main_match, current_main = extract_main(text)
        legacy = extract_legacy(current_main)
        data = parse_sector(legacy, text, slug)
        if not data["page_title"] or not data["need"]:
            raise RuntimeError(f"{slug}: faltan metadata editorial de sector")
        if len(data["decisions"]) < 5 or len(data["map"]) < 4 or len(data["risks"]) < 3 or len(data["interventions"]) < 2 or len(data["moments"]) < 3 or len(data["readings"]) < 2 or len(data["routes"]) < 1:
            raise RuntimeError(f"{slug}: estructura editorial insuficiente para Wave 4")
        new_main = f'<main id="contenido" data-experience-v60="sector:{e(slug)}">\n{render_sector(data, legacy)}\n</main>'
        text = text[:main_match.start()] + new_main + text[main_match.end():]
        path.write_text(text, encoding="utf-8")
    print("EXPERIENCE V6 WAVE 4 OK: 8/8 sectores derivados del HTML editorial canónico; contenido completo preservado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

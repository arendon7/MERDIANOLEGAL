#!/usr/bin/env python3
"""Materializa Wave 5 v6: seis perspectivas abiertas + hub editorial.

Los artículos siguen siendo contenido de lectura: el cuerpo no se pliega. v6 reordena
hero/meta/guía y reutiliza los nodos editoriales canónicos (article-body, aside,
autoridad y relacionadas). El hub conserva su composición histórica como profundidad.
"""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
import re

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


def ensure_styles(text: str, hrefs: list[str]) -> str:
    for href in hrefs:
        text = re.sub(rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(href)}">\s*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("perspectiva sin </head>")
    links = "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in hrefs)
    return text.replace("</head>", f"{links}\n</head>", 1)


def mark_body(text: str, surface: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        for attr in ("data-experience-system", "data-experience-wave", "data-experience-surface"):
            tag = re.sub(rf'\s{attr}="[^"]*"', "", tag)
        return tag[:-1] + f' data-experience-system="v6" data-experience-wave="perspectives" data-experience-surface="{e(surface)}">'
    return re.sub(r"<body\b[^>]*>", repl, text, count=1)


def extract_main(text: str) -> tuple[re.Match[str], str]:
    match = re.search(r'<main id="contenido"[^>]*>(.*?)</main>', text, flags=re.S)
    if not match:
        raise RuntimeError("perspectiva sin <main id=contenido>")
    return match, match.group(1)


def tag_block(value: str, tag: str, class_name: str) -> str:
    match = re.search(rf'<{tag}\b[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*>.*?</{tag}>', value, flags=re.S)
    if not match:
        raise RuntimeError(f"perspectiva: falta {tag}.{class_name}")
    return match.group(0)


def authority_block(value: str) -> str:
    match = re.search(r'<!-- AUTHORITY-V53-PERSPECTIVE:START -->.*?<!-- AUTHORITY-V53-PERSPECTIVE:END -->', value, flags=re.S)
    if not match:
        raise RuntimeError("perspectiva: falta autoridad v5.3")
    return match.group(0)


def related_block(value: str) -> str:
    pos = value.find("LECTURAS RELACIONADAS")
    if pos < 0:
        raise RuntimeError("perspectiva: faltan lecturas relacionadas")
    start = value.rfind("<section", 0, pos)
    end = value.find("</section>", pos)
    if start < 0 or end < 0:
        raise RuntimeError("perspectiva: no se pudo aislar lecturas relacionadas")
    return value[start:end + len("</section>")]


def article_hero_parts(main: str) -> tuple[str, str, str, str]:
    old = re.search(r'<section\b[^>]*class="[^"]*article-hero[^"]*"[^>]*>(.*?)</section>', main, flags=re.S)
    if old:
        fragment = old.group(1)
        eyebrow = find_tag(fragment, "p", "eyebrow")
        title = find_tag(fragment, "h1")
        lead = find_tag(fragment, "p", "lead")
        meta = tag_block(fragment, "aside", "article-meta")
        return eyebrow, title, lead, meta
    v6 = re.search(r'<section\b[^>]*class="[^"]*v6-perspective-hero[^"]*"[^>]*>(.*?)</section>', main, flags=re.S)
    if not v6:
        raise RuntimeError("perspectiva: falta hero v5/v6")
    fragment = v6.group(1)
    return find_tag(fragment, "p", "v6-eyebrow"), find_tag(fragment, "h1"), find_tag(fragment, "p", "v6-lead"), tag_block(fragment, "aside", "article-meta")


def toc_block(main: str) -> str:
    return tag_block(main, "nav", "article-toc")


def central_decision(article_body: str) -> tuple[str, str]:
    match = re.search(r'<div\b[^>]*class="[^"]*decision-box[^"]*"[^>]*>(.*?)</div>', article_body, flags=re.S)
    if not match:
        # Algunas perspectivas usan otra caja; el artículo sigue siendo válido.
        return "Pregunta de lectura", "Use el recorrido del artículo para identificar qué decisión, evidencia o control requiere verificación."
    return find_tag(match.group(1), "strong") or "Decisión central", find_tag(match.group(1), "span")


def toc_links(toc: str) -> str:
    links = re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', toc, flags=re.S)
    return "".join(f'<a href="{e(href)}" data-index="{idx:02d}">{e(clean(label))}</a>' for idx, (href, label) in enumerate(links, 1))


def render_article(main: str, slug: str) -> str:
    eyebrow, title, lead, meta = article_hero_parts(main)
    article_body = tag_block(main, "article", "article-body")
    aside = tag_block(main, "aside", "article-aside")
    toc = toc_block(main)
    authority = authority_block(main)
    related = related_block(main)
    decision_label, decision_copy = central_decision(article_body)
    if not title or not lead:
        raise RuntimeError(f"{slug}: hero editorial incompleto")
    return f'''{ARTICLE_START}
<section class="v6-section v6-perspective-hero" aria-labelledby="v6-perspective-title"><div class="v6-container v6-perspective-hero-grid"><div><p class="v6-eyebrow">{e(eyebrow)}</p><h1 class="v6-display" id="v6-perspective-title">{e(title)}</h1><p class="v6-lead">{e(lead)}</p></div>{meta.replace('class="article-meta"', 'class="article-meta v6-reading-meta"', 1)}</div></section>
<section class="v6-section v6-reading-guide" aria-labelledby="v6-reading-guide-title"><div class="v6-container v6-reading-guide-grid"><div><p class="v6-eyebrow">LECTURA EJECUTIVA</p><h2 class="v6-heading" id="v6-reading-guide-title">La pregunta central antes de entrar al detalle.</h2><div class="v6-central-decision"><strong>{e(decision_label)}</strong><span>{e(decision_copy)}</span></div></div><nav class="v6-reading-toc" aria-label="Recorrido de esta perspectiva">{toc_links(toc)}</nav></div></section>
<section class="v6-section v6-article-reading"><div class="v6-container v6-article-shell">{article_body}{aside}</div></section>
<section class="v6-section v6-perspective-authority"><div class="v6-container">{authority}</div></section>
<section class="v6-section v6-perspective-related"><div class="v6-container">{related}</div></section>
{ARTICLE_END}'''


def extract_hub_legacy(main: str) -> str:
    match = re.search(re.escape(HUB_LEGACY_START) + r"(.*?)" + re.escape(HUB_LEGACY_END), main, flags=re.S)
    return match.group(1) if match else main


def hub_cards(legacy: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for href, raw in re.findall(r'<a\b[^>]*class="[^"]*(?:featured-card|insight-card)[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', legacy, flags=re.S):
        if href in seen:
            continue
        seen.add(href)
        result.append({
            "href": unescape(href),
            "label": find_tag(raw, "span"),
            "title": find_tag(raw, "h2") or find_tag(raw, "h3"),
            "copy": find_tag(raw, "p"),
        })
    return result


def hub_hero(legacy: str) -> tuple[str, str, str]:
    old = re.search(r'<section\b[^>]*class="[^"]*library-hero[^"]*"[^>]*>(.*?)</section>', legacy, flags=re.S)
    if not old:
        raise RuntimeError("hub perspectivas: falta library-hero")
    fragment = old.group(1)
    return find_tag(fragment, "p", "eyebrow"), find_tag(fragment, "h1"), find_tag(fragment, "p", "lead")


def hub_criteria(legacy: str) -> list[tuple[str, str]]:
    section_pos = legacy.find("CRITERIOS EDITORIALES")
    if section_pos < 0:
        raise RuntimeError("hub perspectivas: faltan criterios editoriales")
    start = legacy.rfind("<section", 0, section_pos)
    end = legacy.find("</section>", section_pos)
    fragment = legacy[start:end + len("</section>")]
    items = []
    for raw in re.findall(r"<article\b[^>]*>(.*?)</article>", fragment, flags=re.S):
        items.append((find_tag(raw, "strong"), find_tag(raw, "span")))
    return items


def render_hub(legacy: str) -> str:
    eyebrow, title, lead = hub_hero(legacy)
    cards = hub_cards(legacy)
    criteria = hub_criteria(legacy)
    if len(cards) != 6 or len(criteria) != 4:
        raise RuntimeError(f"hub perspectivas: esperaba 6 lecturas y 4 criterios; obtuvo {len(cards)} y {len(criteria)}")
    card_html = "".join(f'<a class="v6-library-card" href="{e(item["href"])}"><b>{e(item["label"])}</b><h2>{e(item["title"])}</h2><p>{e(item["copy"])}</p><span>Leer perspectiva completa →</span></a>' for item in cards)
    criterion_html = "".join(f'<article class="v6-library-criterion"><strong>{e(title)}</strong><span>{e(copy)}</span></article>' for title, copy in criteria)
    return f'''{HUB_START}
<section class="v6-section v6-library-hero" aria-labelledby="v6-library-title"><div class="v6-container"><p class="v6-eyebrow">{e(eyebrow)}</p><h1 class="v6-display" id="v6-library-title">{e(title)}</h1><p class="v6-lead">{e(lead)}</p><div class="v6-actions"><a class="v6-btn" href="#v6-library-grid">Explorar las seis perspectivas →</a><a class="v6-btn v6-btn-secondary" href="index.html#contacto">Presentar una necesidad</a></div></div></section>
<section class="v6-section" id="v6-library-grid" aria-labelledby="v6-library-grid-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">BIBLIOTECA</p><h2 class="v6-heading" id="v6-library-grid-title">Seis decisiones para leer antes de que el riesgo se convierta en fricción.</h2><p class="v6-lead">Cada perspectiva organiza una pregunta ejecutiva, el marco jurídico, señales de alerta, preguntas de control y una ruta de intervención cuando corresponde.</p></div><div class="v6-library-grid">{card_html}</div></div></section>
<section class="v6-section v6-library-criteria" aria-labelledby="v6-library-criteria-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">CRITERIOS EDITORIALES</p><h2 class="v6-heading" id="v6-library-criteria-title">Contenido útil sin simplificaciones que oculten los límites.</h2></div><div class="v6-library-criteria-grid">{criterion_html}</div></div></section>
<section class="v6-section v6-solution-cta" aria-labelledby="v6-library-cta-title"><div class="v6-container v6-solution-cta-inner"><div><p class="v6-eyebrow">DE LA LECTURA A LA DECISIÓN</p><h2 class="v6-heading" id="v6-library-cta-title">Una perspectiva puede orientar la pregunta. El alcance profesional depende del contexto.</h2><p class="v6-lead">Presente la decisión, el plazo, los actores y el resultado esperado sin enviar documentos confidenciales desde la web pública.</p></div><a class="v6-btn" href="index.html?context=Perspectivas%3A+Biblioteca+de+perspectivas&need=Otra+necesidad#contacto">Presentar necesidad →</a></div></section>
<details class="v6-depth v6-library-depth"><summary><span>ARQUITECTURA ANTERIOR</span><strong>Ver biblioteca y navegación editorial v5.31</strong></summary><div class="v6-depth-inner">{HUB_LEGACY_START}{legacy}{HUB_LEGACY_END}</div></details>
{HUB_END}'''


def patch_article(path: Path) -> None:
    slug = path.stem
    text = path.read_text(encoding="utf-8")
    text = ensure_styles(text, ARTICLE_STYLES)
    text = mark_body(text, f"perspective:{slug}")
    main_match, main = extract_main(text)
    rendered = render_article(main, slug)
    new_main = f'<main id="contenido" data-experience-v60="perspective:{e(slug)}">\n{rendered}\n</main>'
    text = text[:main_match.start()] + new_main + text[main_match.end():]
    path.write_text(text, encoding="utf-8")


def patch_hub() -> None:
    text = HUB.read_text(encoding="utf-8")
    text = ensure_styles(text, HUB_STYLES)
    text = mark_body(text, "perspectives-hub")
    main_match, main = extract_main(text)
    legacy = extract_hub_legacy(main)
    new_main = f'<main id="contenido" data-experience-v60="perspectives-hub">\n{render_hub(legacy)}\n</main>'
    text = text[:main_match.start()] + new_main + text[main_match.end():]
    HUB.write_text(text, encoding="utf-8")


def main() -> int:
    paths = sorted(PERSPECTIVES.glob("*.html"))
    if len(paths) != 6:
        raise RuntimeError(f"Wave 5 requiere 6 perspectivas y encontró {len(paths)}")
    for path in paths:
        patch_article(path)
    patch_hub()
    print("EXPERIENCE V6 WAVE 5 OK: 6 perspectivas con lectura abierta + hub editorial materializados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

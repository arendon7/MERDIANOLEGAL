#!/usr/bin/env python3
"""v5.3: conecta autoridad editorial/sectorial, schema de descubrimiento y medición CRO sin PII."""
from __future__ import annotations

from html import escape
from pathlib import Path
from urllib.parse import urljoin
import json
import re

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
BASE_URL = CONFIG["base_url"]
VERSION_DATA = json.loads((R / "version.json").read_text(encoding="utf-8"))
VERSION = VERSION_DATA["version"]
RELEASE_DATE = VERSION_DATA["release_date"]
AUTH = json.loads((R / "authority-v53.json").read_text(encoding="utf-8"))
V51 = json.loads((R / "growth-solutions-v51.json").read_text(encoding="utf-8"))
SOLUTIONS = {item["slug"]: item for item in V51["solutions"]}

MANAGED = (
    "AUTHORITY-V53-PERSPECTIVE",
    "AUTHORITY-V53-SECTOR",
    "AUTHORITY-V53-SCHEMA",
    "MEASUREMENT-V53",
)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def strip_managed(text: str) -> str:
    for name in MANAGED:
        text = re.sub(rf"\n?<!-- {name}:START -->[\s\S]*?<!-- {name}:END -->\n?", "\n", text)
    return text


def script_block(prefix: str) -> str:
    return (
        '<!-- MEASUREMENT-V53:START -->\n'
        f'<script src="{prefix}measurement-v53.js"></script>\n'
        '<!-- MEASUREMENT-V53:END -->'
    )


def item_list_schema(name: str, entries: list[tuple[str, str]]) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": name,
        "itemListElement": [
            {"@type": "ListItem", "position": index, "name": label, "url": url}
            for index, (label, url) in enumerate(entries, 1)
        ],
    }
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (
        '<!-- AUTHORITY-V53-SCHEMA:START -->\n'
        f'<script type="application/ld+json" data-authority-v53="item-list">{raw}</script>\n'
        '<!-- AUTHORITY-V53-SCHEMA:END -->'
    )


def solution_url(slug: str) -> str:
    return BASE_URL + f"soluciones/{slug}.html"


def patch_home_schema() -> None:
    path = R / "index.html"
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'(<!-- QUALITY-V48-SEO:START -->[\s\S]*?<script type="application/ld\+json">)'
        r'(\{[\s\S]*?\})'
        r'(</script>[\s\S]*?<!-- QUALITY-V48-SEO:END -->)'
    )
    match = pattern.search(text)
    if not match:
        raise RuntimeError("index.html: no se encontró JSON-LD principal")
    payload = json.loads(match.group(2))
    graph = payload.get("@graph") or []
    organization = next(
        (node for node in graph if isinstance(node, dict) and node.get("@id") == BASE_URL + "#organization"),
        None,
    )
    if not organization:
        raise RuntimeError("index.html: no se encontró Organization canónica")
    organization["logo"] = {
        "@type": "ImageObject",
        "url": BASE_URL + "assets/brand/meridiano-logo-horizontal-dark.svg",
    }
    organization["knowsAbout"] = AUTH["organization_knows_about"]
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    text = text[:match.start()] + match.group(1) + raw + match.group(3) + text[match.end():]
    path.write_text(text, encoding="utf-8")


def patch_solution(slug: str, item: dict) -> None:
    path = R / "soluciones" / f"{slug}.html"
    text = strip_managed(path.read_text(encoding="utf-8"))
    text = re.sub(r'\sdata-solution-slug="[^"]*"', "", text)
    text = re.sub(r'\sdata-page-need="[^"]*"', "", text)
    marker = 'data-growth-v51="solution"'
    if marker not in text:
        raise RuntimeError(f"{path.name}: falta marcador de solución v5.1")
    attrs = (
        f'{marker} data-solution-slug="{escape(slug, quote=True)}" '
        f'data-page-need="{escape(item["need"], quote=True)}"'
    )
    text = text.replace(marker, attrs, 1)
    routes = [(route["name"], urljoin(solution_url(slug), route["href"])) for route in item["routes"]]
    text = text.replace(
        "</head>",
        item_list_schema(f"Modalidades relacionadas con {item['title']}", routes) + "\n</head>",
        1,
    )
    text = text.replace("</body>", script_block("../") + "\n</body>", 1)
    path.write_text(text, encoding="utf-8")


def patch_hub() -> None:
    path = R / "soluciones" / "index.html"
    text = strip_managed(path.read_text(encoding="utf-8"))
    entries = [(item["title"], solution_url(item["slug"])) for item in V51["solutions"]]
    text = text.replace(
        "</head>",
        item_list_schema("Soluciones jurídicas por situación empresarial", entries) + "\n</head>",
        1,
    )
    path.write_text(text, encoding="utf-8")


def render_perspective_block(entry: dict) -> str:
    cards = []
    for related in entry["solutions"]:
        item = SOLUTIONS[related["slug"]]
        cards.append(
            f'<a data-authority-solution="{escape(related["slug"], quote=True)}" '
            f'href="../soluciones/{escape(related["slug"], quote=True)}.html">'
            f'<span>RUTA EMPRESARIAL</span><strong>{escape(item["short"])}</strong>'
            f'<small>{escape(related["reason"])}</small></a>'
        )
    return (
        '<!-- AUTHORITY-V53-PERSPECTIVE:START -->\n'
        '<section class="section related-section authority-v53"><div class="container">'
        '<div class="section-heading"><p class="eyebrow dark">DE LA LECTURA A LA DECISIÓN</p>'
        '<h2>Si este problema ya existe en la empresa, continúe por una ruta de decisión.</h2>'
        '<p>La perspectiva desarrolla criterio general. La ruta empresarial ayuda a delimitar señales, modalidad, '
        'entregables, límites y siguiente paso sin asumir que todos los casos requieren el mismo servicio.</p></div>'
        f'<div class="related-grid">{"".join(cards)}</div></div></section>\n'
        '<!-- AUTHORITY-V53-PERSPECTIVE:END -->'
    )


def render_sector_block(entry: dict) -> str:
    cards = []
    for related in entry["solutions"]:
        item = SOLUTIONS[related["slug"]]
        cards.append(
            f'<article><span>RUTA DE DECISIÓN</span><h3>{escape(item["short"])}</h3>'
            f'<p>{escape(related["reason"])}</p>'
            f'<a data-authority-solution="{escape(related["slug"], quote=True)}" '
            f'href="../soluciones/{escape(related["slug"], quote=True)}.html">Explorar situación →</a></article>'
        )
    return (
        '<!-- AUTHORITY-V53-SECTOR:START -->\n'
        '<section class="section authority-v53"><div class="container">'
        '<div class="section-heading"><p class="eyebrow dark">RUTAS POR SITUACIÓN</p>'
        '<h2>Conecte la lectura sectorial con la decisión que debe resolver.</h2>'
        '<p>El sector aporta contexto. Estas rutas ayudan a identificar si la necesidad exige priorización, '
        'capacidad recurrente, preparación para una transacción, gobernanza o estructuración regulatoria.</p></div>'
        f'<div class="solution-grid">{"".join(cards)}</div></div></section>\n'
        '<!-- AUTHORITY-V53-SECTOR:END -->'
    )


def patch_perspective(entry: dict) -> None:
    path = R / entry["path"]
    text = strip_managed(path.read_text(encoding="utf-8"))
    text = re.sub(
        r'(<meta property="article:modified_time" content=")[^"]*(">)',
        rf'\g<1>{RELEASE_DATE}\g<2>',
        text,
        count=1,
    )
    text = re.sub(r'("dateModified":")[^"]*(")', rf'\g<1>{RELEASE_DATE}\g<2>', text, count=1)
    marker = '<section class="section related-section">'
    if marker not in text:
        raise RuntimeError(f"{entry['path']}: falta related-section")
    text = text.replace(marker, render_perspective_block(entry) + "\n" + marker, 1)
    schema_entries = [
        (SOLUTIONS[item["slug"]]["title"], solution_url(item["slug"])) for item in entry["solutions"]
    ]
    text = text.replace(
        "</head>",
        item_list_schema(f"Rutas empresariales relacionadas con {entry['label']}", schema_entries) + "\n</head>",
        1,
    )
    text = text.replace("</body>", script_block("../") + "\n</body>", 1)
    path.write_text(text, encoding="utf-8")


def patch_sector(entry: dict) -> None:
    path = R / entry["path"]
    text = strip_managed(path.read_text(encoding="utf-8"))
    marker = '<section class="sector-closing"'
    if marker not in text:
        raise RuntimeError(f"{entry['path']}: falta sector-closing")
    text = text.replace(marker, render_sector_block(entry) + "\n" + marker, 1)
    schema_entries = [
        (SOLUTIONS[item["slug"]]["title"], solution_url(item["slug"])) for item in entry["solutions"]
    ]
    text = text.replace(
        "</head>",
        item_list_schema(f"Rutas jurídicas relacionadas con {entry['label']}", schema_entries) + "\n</head>",
        1,
    )
    text = text.replace("</body>", script_block("../") + "\n</body>", 1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if semver(VERSION) < (5, 3, 0):
        raise SystemExit("v5.3 requiere version.json >= 5.3.0")
    if AUTH.get("version") != "5.3.0":
        raise SystemExit("authority-v53.json debe declarar version 5.3.0")
    if len(AUTH.get("perspectives", [])) != 6 or len(AUTH.get("sectors", [])) != 8:
        raise SystemExit("v5.3 debe mapear exactamente 6 perspectivas y 8 sectores")

    patch_home_schema()
    patch_hub()
    for item in V51["solutions"]:
        patch_solution(item["slug"], item)
    for entry in AUTH["perspectives"]:
        patch_perspective(entry)
    for entry in AUTH["sectors"]:
        patch_sector(entry)

    print(
        f"Autoridad/descubrimiento v{VERSION} aplicado: 6 soluciones, 6 perspectivas, "
        "8 sectores, schema y medición CRO sin PII."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

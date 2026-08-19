#!/usr/bin/env python3
"""Valida Delivery Plan Clarity v6.5 contra truth canónico de las 16 fichas."""
from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets" / "data" / "v6" / "delivery-plan-clarity-v65.json"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
START = "<!-- DELIVERY-PLAN-CLARITY-V65:START -->"
END = "<!-- DELIVERY-PLAN-CLARITY-V65:END -->"
CSS_HREF = "../assets/css/v6/delivery-plan-clarity-v65.css"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def body_attr(text: str, name: str) -> str:
    match = re.search(rf'<body\b[^>]*\b{name}="([^"]*)"', text)
    return match.group(1) if match else ""


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(value)).strip()


def sources() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for folder in CATALOG_DIRS:
        files = sorted(folder.glob("*.json"))
        if len(files) != 8:
            raise AssertionError(f"{folder.name}: se esperaban 8 fuentes y hay {len(files)}")
        for path in files:
            payload = load_json(path)
            if len(payload) != 1:
                raise AssertionError(f"{path.name}: debe declarar un único catalog_id")
            catalog_id, source = next(iter(payload.items()))
            if catalog_id in result:
                raise AssertionError(f"catalog_id duplicado: {catalog_id}")
            for field in ("formats", "timeline"):
                rows = source.get(field)
                if not isinstance(rows, list) or not rows:
                    raise AssertionError(f"{path.name}: {field} vacío o inválido")
                if any(not isinstance(row, list) or len(row) != 2 for row in rows):
                    raise AssertionError(f"{path.name}: {field} contiene filas inválidas")
            result[catalog_id] = source
    if len(result) != 16:
        raise AssertionError(f"se esperaban 16 fuentes; hay {len(result)}")
    return result


def pages() -> dict[str, Path]:
    result: dict[str, Path] = {}
    paths = sorted(path for folder in DETAIL_DIRS for path in folder.glob("*.html"))
    if len(paths) != 16:
        raise AssertionError(f"se esperaban 16 fichas HTML; hay {len(paths)}")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        catalog_id = body_attr(text, "data-catalog-id")
        if not catalog_id:
            raise AssertionError(f"{path.relative_to(ROOT)}: falta data-catalog-id")
        if catalog_id in result:
            raise AssertionError(f"catalog_id HTML duplicado: {catalog_id}")
        result[catalog_id] = path
    return result


def extract_rows(section: str, group: str) -> list[list[str]]:
    panel = re.search(
        rf'<article class="v65-delivery-plan-panel" data-delivery-plan-group="{re.escape(group)}">(.*?)</article>',
        section,
        flags=re.S,
    )
    if not panel:
        raise AssertionError(f"falta panel {group}")
    rows = re.findall(
        rf'<div class="v65-delivery-plan-row" data-delivery-plan-row="{re.escape(group)}"><dt>(.*?)</dt><dd>(.*?)</dd></div>',
        panel.group(1),
        flags=re.S,
    )
    return [[normalize(label), normalize(copy)] for label, copy in rows]


def validate_page(path: Path, catalog_id: str, source: dict, contract: dict) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()
    if text.count(CSS_HREF) != 1:
        raise AssertionError(f"{rel}: debe cargar exactamente una hoja v6.5")
    if text.count(START) != 1 or text.count(END) != 1:
        raise AssertionError(f"{rel}: bloque v6.5 debe aparecer exactamente una vez")
    marker = re.search(re.escape(START) + r'(.*?)' + re.escape(END), text, flags=re.S)
    if not marker:
        raise AssertionError(f"{rel}: no se pudo extraer bloque v6.5")
    section = marker.group(1)
    presentation = contract["presentation"]
    if f'id="{presentation["section_id"]}"' not in section:
        raise AssertionError(f"{rel}: section_id v6.5 incorrecto")
    if 'data-delivery-plan-clarity-v65="true"' not in section:
        raise AssertionError(f"{rel}: falta marcador data-delivery-plan-clarity-v65")
    if f'data-delivery-plan-catalog-id="{catalog_id}"' not in section:
        raise AssertionError(f"{rel}: catalog_id v6.5 incorrecto")
    for value in (presentation["eyebrow"], presentation["title"], presentation["intro"], presentation["formats_title"], presentation["timeline_title"]):
        if normalize(value) not in normalize(section):
            raise AssertionError(f"{rel}: falta copy gobernado: {value}")
    actual_formats = extract_rows(section, "formats")
    actual_timeline = extract_rows(section, "timeline")
    expected_formats = [[normalize(a), normalize(b)] for a, b in source["formats"]]
    expected_timeline = [[normalize(a), normalize(b)] for a, b in source["timeline"]]
    if actual_formats != expected_formats:
        raise AssertionError(f"{rel}: formats visibles divergen del catálogo canónico")
    if actual_timeline != expected_timeline:
        raise AssertionError(f"{rel}: timeline visible diverge del catálogo canónico")
    deliverables_start = text.find('<section class="v6-section v6-deliverables" id="v6-deliverables"')
    delivery_start = text.find(START)
    perimeter_start = text.find('<section class="v6-section v6-perimeter" id="v6-perimeter"')
    if min(deliverables_start, delivery_start, perimeter_start) < 0 or not (deliverables_start < delivery_start < perimeter_start):
        raise AssertionError(f"{rel}: v6.5 debe ubicarse entre Entregables y Perímetro")
    nav = re.search(r'<nav class="v6-detail-nav"[^>]*>.*?</nav>', text, flags=re.S)
    if not nav:
        raise AssertionError(f"{rel}: falta navegación v6")
    if '#v6-delivery-plan' in nav.group(0):
        raise AssertionError(f"{rel}: v6.5 no debe aumentar la densidad del TOC")
    if nav.group(0).count('<a ') != 7:
        raise AssertionError(f"{rel}: TOC debe conservar exactamente 7 hitos")


def main() -> int:
    if not CONTRACT.exists():
        raise AssertionError("falta contrato Delivery Plan Clarity v6.5")
    contract = load_json(CONTRACT)
    if contract.get("version") != "6.5.0":
        raise AssertionError("contrato Delivery Plan Clarity debe declarar 6.5.0")
    if contract.get("scope") != {"detail_pages": 16, "products": 8, "services": 8}:
        raise AssertionError("scope v6.5 debe ser exactamente 16 = 8 productos + 8 servicios")
    if contract.get("truth", {}).get("catalog_fields") != ["formats", "timeline"]:
        raise AssertionError("truth v6.5 debe depender solo de formats y timeline")
    canonical = sources()
    rendered = pages()
    if set(canonical) != set(rendered):
        raise AssertionError(
            f"desalineación source/HTML: sin HTML={sorted(set(canonical)-set(rendered))}; "
            f"sin fuente={sorted(set(rendered)-set(canonical))}"
        )
    for catalog_id in sorted(canonical):
        validate_page(rendered[catalog_id], catalog_id, canonical[catalog_id], contract)
    print("DELIVERY PLAN CLARITY V6.5 VALIDATION OK: 16/16 fichas reproducen formats + timeline canónicos; TOC preservado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

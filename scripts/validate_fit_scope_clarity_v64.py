#!/usr/bin/env python3
"""Valida Fit & Scope Clarity v6.4 contra truth canónico de las 16 fichas."""
from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets" / "data" / "v6" / "fit-scope-clarity-v64.json"
CATALOG_DIRS = (ROOT / "catalog-products-v41", ROOT / "catalog-services-v42")
DETAIL_DIRS = (ROOT / "productos", ROOT / "servicios")
START = "<!-- FIT-SCOPE-CLARITY-V64:START -->"
END = "<!-- FIT-SCOPE-CLARITY-V64:END -->"
CSS_HREF = "../assets/css/v6/fit-scope-clarity-v64.css"


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
            for field in ("situations", "supplements"):
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
        rf'<article class="v64-fit-scope-panel" data-fit-scope-group="{re.escape(group)}">(.*?)</article>',
        section,
        flags=re.S,
    )
    if not panel:
        raise AssertionError(f"falta panel {group}")
    rows = re.findall(
        rf'<div class="v64-fit-scope-row" data-fit-scope-row="{re.escape(group)}"><dt>(.*?)</dt><dd>(.*?)</dd></div>',
        panel.group(1),
        flags=re.S,
    )
    return [[normalize(label), normalize(copy)] for label, copy in rows]


def validate_page(path: Path, catalog_id: str, source: dict, contract: dict) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()
    if text.count(CSS_HREF) != 1:
        raise AssertionError(f"{rel}: debe cargar exactamente una hoja v6.4")
    if text.count(START) != 1 or text.count(END) != 1:
        raise AssertionError(f"{rel}: bloque v6.4 debe aparecer exactamente una vez")
    marker = re.search(re.escape(START) + r'(.*?)' + re.escape(END), text, flags=re.S)
    if not marker:
        raise AssertionError(f"{rel}: no se pudo extraer bloque v6.4")
    section = marker.group(1)
    presentation = contract["presentation"]
    if f'id="{presentation["section_id"]}"' not in section:
        raise AssertionError(f"{rel}: section_id v6.4 incorrecto")
    if 'data-fit-scope-clarity-v64="true"' not in section:
        raise AssertionError(f"{rel}: falta marcador data-fit-scope-clarity-v64")
    if f'data-fit-scope-catalog-id="{catalog_id}"' not in section:
        raise AssertionError(f"{rel}: catalog_id v6.4 incorrecto")
    for value in (presentation["eyebrow"], presentation["title"], presentation["intro"], presentation["situations_title"], presentation["supplements_title"]):
        if normalize(value) not in normalize(section):
            raise AssertionError(f"{rel}: falta copy gobernado: {value}")
    actual_situations = extract_rows(section, "situations")
    actual_supplements = extract_rows(section, "supplements")
    expected_situations = [[normalize(a), normalize(b)] for a, b in source["situations"]]
    expected_supplements = [[normalize(a), normalize(b)] for a, b in source["supplements"]]
    if actual_situations != expected_situations:
        raise AssertionError(f"{rel}: situations visibles divergen del catálogo canónico")
    if actual_supplements != expected_supplements:
        raise AssertionError(f"{rel}: supplements visibles divergen del catálogo canónico")
    result_start = text.find('<section class="v6-section v6-result" id="v6-result"')
    fit_start = text.find(START)
    deliverables_start = text.find('<section class="v6-section v6-deliverables" id="v6-deliverables"')
    if min(result_start, fit_start, deliverables_start) < 0 or not (result_start < fit_start < deliverables_start):
        raise AssertionError(f"{rel}: v6.4 debe ubicarse entre Resultado y Entregables")
    nav = re.search(r'<nav class="v6-detail-nav"[^>]*>.*?</nav>', text, flags=re.S)
    if not nav:
        raise AssertionError(f"{rel}: falta navegación v6")
    if '#v6-fit-scope' in nav.group(0):
        raise AssertionError(f"{rel}: v6.4 no debe aumentar la densidad del TOC")


def main() -> int:
    if not CONTRACT.exists():
        raise AssertionError("falta contrato Fit & Scope Clarity v6.4")
    contract = load_json(CONTRACT)
    if contract.get("version") != "6.4.0":
        raise AssertionError("contrato Fit & Scope Clarity debe declarar 6.4.0")
    if contract.get("scope") != {"detail_pages": 16, "products": 8, "services": 8}:
        raise AssertionError("scope v6.4 debe ser exactamente 16 = 8 productos + 8 servicios")
    if contract.get("truth", {}).get("catalog_fields") != ["situations", "supplements"]:
        raise AssertionError("truth v6.4 debe depender solo de situations y supplements")
    canonical = sources()
    rendered = pages()
    if set(canonical) != set(rendered):
        raise AssertionError(
            f"desalineación source/HTML: sin HTML={sorted(set(canonical)-set(rendered))}; "
            f"sin fuente={sorted(set(rendered)-set(canonical))}"
        )
    for catalog_id in sorted(canonical):
        validate_page(rendered[catalog_id], catalog_id, canonical[catalog_id], contract)
    print("FIT & SCOPE CLARITY V6.4 VALIDATION OK: 16/16 fichas reproducen situations + supplements canónicos; TOC preservado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

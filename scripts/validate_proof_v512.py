#!/usr/bin/env python3
"""Valida v5.12 y su composición unificada de portada desde v5.20."""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
VERSION = ROOT / "version.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
HOME_START = "<!-- PROOF-V512-HOME:START -->"
HOME_END = "<!-- PROOF-V512-HOME:END -->"
DETAIL_START = "<!-- PROOF-V512-DETAIL:START -->"
DETAIL_END = "<!-- PROOF-V512-DETAIL:END -->"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"PROOF V5.12 FAIL: {message}")


def version_at_least(major: int, minor: int) -> bool:
    payload = json.loads(VERSION.read_text(encoding="utf-8"))
    raw = str(payload.get("version", "0.0.0")).split(".")
    try:
        return (int(raw[0]), int(raw[1])) >= (major, minor)
    except (ValueError, IndexError):
        return False


def load_catalog() -> dict[str, dict]:
    catalog: dict[str, dict] = {}
    paths = sorted((ROOT / "catalog-products-v41").glob("*.json")) + sorted((ROOT / "catalog-services-v42").glob("*.json"))
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        require(len(payload) == 1, f"{path.name}: se esperaba una ficha")
        key, value = next(iter(payload.items()))
        catalog[key] = value
    require(len(catalog) == 16, "deben existir 16 fuentes")
    return catalog


def source_pairs(values, limit: int = 3) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for item in values or []:
        if isinstance(item, list) and item:
            out.append((str(item[0]), str(item[1]) if len(item) > 1 else ""))
        elif isinstance(item, str):
            out.append((item, ""))
        if len(out) >= limit:
            break
    return out


def route_keys(block: str) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for raw_href in re.findall(r'href="([^"]+)"', block):
        parts = urlsplit(unescape(raw_href))
        keys.add((parts.path, parts.fragment))
    return keys


def validate_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    require(text.count(HOME_START) == 1 and text.count(HOME_END) == 1, "portada debe tener un bloque gestionado")
    require('<link rel="stylesheet" href="proof-v512.css">' in text, "falta CSS v5.12 en portada")
    block = text[text.index(HOME_START):text.index(HOME_END)]

    if version_at_least(5, 20):
        require('data-home-decision-v520="true"' in block, "v5.20 debe materializar prueba y modalidad en una única superficie")
        require('data-engagement-router-v58="true"' in block, "v5.20 debe conservar continuidad semántica con v5.8")
        require("<!-- DECISION-V58-HOME:START -->" not in text and "<!-- DECISION-V58-HOME:END -->" not in text, "v5.20 no debe reintroducir un selector v5.8 separado")
    else:
        require(text.index("<!-- DECISION-V58-HOME:END -->") < text.index(HOME_START), "v5.12 debe seguir a v5.8")

    require(block.count('data-proof-model-v512=') == 5, "deben existir cinco modalidades")
    for model in ("diagnostic", "audit", "product", "specialist", "recurring"):
        require(f'data-proof-model-v512="{model}"' in block, f"falta modalidad {model}")

    routes = route_keys(block)
    for route in (
        ("servicios/diagnostico-juridico-empresarial.html", ""),
        ("productos/diagnostico-juridico-empresarial.html", ""),
        ("", "productos"),
        ("", "servicios"),
        ("servicios/direccion-juridica-externa.html", ""),
    ):
        require(route in routes, f"falta ruta canónica {route[0] or '#'+route[1]}")

    require('data-proof-standard-v512="true"' in block, "falta estándar de prueba")
    require(block.count('<div class="proof-standard-grid-v512"><span>') == 1, "falta grid del estándar")
    require(block.count('</span><span>') == 3, "estándar debe contener cuatro verificaciones")
    require("testimonio" not in block.lower() and "caso de éxito" not in block.lower(), "no deben aparecer pruebas sociales inventadas")


def validate_detail(path: Path, catalog: dict[str, dict]) -> None:
    text = path.read_text(encoding="utf-8")
    require(text.count(DETAIL_START) == 1 and text.count(DETAIL_END) == 1, f"{path.name}: bloque gestionado inválido")
    require('<link rel="stylesheet" href="../proof-v512.css">' in text, f"{path.name}: falta CSS v5.12")
    match = re.search(r'data-catalog-id="([^"]+)"', text)
    require(bool(match), f"{path.name}: falta data-catalog-id")
    catalog_id = match.group(1)
    require(catalog_id in catalog, f"{path.name}: fuente inexistente")

    proof_start = text.index(DETAIL_START)
    proof_end = text.index(DETAIL_END)
    body_end = text.index("<!-- STATIC-CATALOG-BODY:END -->")
    detail_start = text.index('<div id="detail-page" data-static-catalog="true">')
    require(detail_start < proof_start < proof_end < body_end, f"{path.name}: orden de runtime incorrecto")
    require(re.search(r'</div>\s*' + re.escape(DETAIL_START), text) is not None, f"{path.name}: prueba debe ser hermana posterior de #detail-page")
    require(text.index(DETAIL_END) < text.index("</main>", proof_end), f"{path.name}: prueba debe permanecer dentro de main")

    block = text[proof_start:proof_end]
    require(block.count('data-proof-dimension-v512=') == 4, f"{path.name}: deben existir cuatro dimensiones")
    data = catalog[catalog_id]
    for field in ("method", "deliverables", "formats", "acceptance"):
        require(f'data-proof-dimension-v512="{field}"' in block, f"{path.name}: falta dimensión {field}")
        pairs = source_pairs(data.get(field))
        require(len(pairs) == 3, f"{path.name}: {field} necesita tres elementos fuente")
        for title, description in pairs:
            require(escape(title) in block, f"{path.name}: falta título fuente {field}/{title}")
            if description:
                require(escape(description) in block, f"{path.name}: falta descripción fuente {field}/{title}")


def main() -> int:
    require(len(DETAIL_TARGETS) == 16, "deben existir 16 fichas profundas")
    css = (ROOT / "proof-v512.css").read_text(encoding="utf-8")
    require(".proof-router-v512" in css and ".proof-detail-v512" in css, "CSS v5.12 incompleto")
    require(".proof-standard-v512 h3{margin:0 0 7px;color:#fff;" in css, "el título del panel oscuro debe fijar contraste WCAG explícito")
    require("@media(max-width:760px)" in css, "CSS v5.12 sin responsive móvil")
    catalog = load_catalog()
    validate_home()
    for path in DETAIL_TARGETS:
        validate_detail(path, catalog)
    print("PROOF V5.12 OK: cinco modalidades y 16 pruebas derivadas preservadas; portada compacta validada cuando aplica.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

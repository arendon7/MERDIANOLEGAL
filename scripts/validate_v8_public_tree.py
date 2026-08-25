#!/usr/bin/env python3
"""Valida W4.5: tres targets v8 persistidos sin activar descubrimiento público.

Estados permitidos:
- bootstrap: 0/3 targets, baseline físico de 46 HTML;
- persisted: 3/3 targets, candidate físico de 49 HTML.

Cualquier estado parcial falla. En persisted, todos los enlaces locales visibles
de los targets deben resolver físicamente: durante rollout parcial se admite
fallback a legacy, pero nunca una ruta v8 futura inexistente.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "assets/data/v8/experience-model-v80.json"
ROUTES = ROOT / "assets/data/v8/route-contract-v80.json"
SITE = ROOT / "site-config.json"
VERSION = ROOT / "version.json"
SITEMAP = ROOT / "sitemap.xml"
HOME = ROOT / "index.html"

CSS_REFS = (
    "../assets/css/v8/tokens.css",
    "../assets/css/v8/base.css",
    "../assets/css/v8/components.css",
    "../assets/css/v8/surfaces.css",
)


def fail(message: str) -> None:
    raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def physical_path(route: str) -> Path:
    if route == "/":
        return ROOT / "index.html"
    if route.endswith("/"):
        return ROOT / route.lstrip("/") / "index.html"
    return ROOT / route.lstrip("/")


def canonical_from_html(html: str) -> str | None:
    match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
    return match.group(1) if match else None


def validate_local_links(page: Path, html: str, pilot_id: str) -> None:
    hrefs = re.findall(r'<a\b[^>]*\bhref="([^"]+)"', html, flags=re.I)
    if not hrefs:
        fail(f"{pilot_id}: target no contiene enlaces")
    for href in hrefs:
        if href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            continue
        path = unquote(parsed.path)
        if not path:
            continue
        resolved = (page.parent / path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError as exc:
            raise AssertionError(f"{pilot_id}: link sale del repositorio {href}") from exc
        if not resolved.exists():
            fail(f"{pilot_id}: enlace local roto {href} -> {resolved.relative_to(ROOT)}")


def validate_non_activation(pilots: list[dict], route_contract: dict) -> None:
    sitemap = SITEMAP.read_text(encoding="utf-8")
    home = HOME.read_text(encoding="utf-8")
    target_routes = [pilot["target_route"] for pilot in pilots]

    for route in target_routes:
        if route in sitemap:
            fail(f"target v8 apareció prematuramente en sitemap: {route}")
        if route in home:
            fail(f"Home activó prematuramente target v8: {route}")

    version = load(VERSION).get("version")
    if version != "7.4.0":
        fail(f"W4.5 no debe activar versión v8; version.json={version!r}")

    recurring = route_contract.get("target_families", {}).get("recurring", [])
    rc02 = next((item for item in recurring if item and item[0] == "RC02"), None)
    if not rc02 or len(rc02) < 3 or rc02[2] is not False:
        fail("RC02 Meridiano Contratos debe continuar publishable=false")


def validate_legacy(route_contract: dict, base_url: str) -> None:
    fields = route_contract.get("legacy_route_fields") or []
    rows = route_contract.get("legacy_routes") or []
    if len(rows) != 46:
        fail(f"route contract legacy debe conservar 46 filas; encontró {len(rows)}")
    index = {name: idx for idx, name in enumerate(fields)}
    required = {"id", "current", "indexed"}
    if not required.issubset(index):
        fail("route contract carece de campos legacy requeridos")

    for row in rows:
        route_id = row[index["id"]]
        current = row[index["current"]]
        indexed = bool(row[index["indexed"]])
        path = physical_path(current)
        if not path.exists():
            fail(f"{route_id}: legacy desapareció {current}")
        if path.suffix.lower() != ".html":
            continue
        html = path.read_text(encoding="utf-8")
        robots_match = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"', html)
        noindex = bool(robots_match and "noindex" in robots_match.group(1).lower())
        if indexed and noindex:
            fail(f"{route_id}: legacy indexable pasó a noindex")
        if indexed:
            expected = base_url + current.lstrip("/")
            if current == "/":
                expected = base_url
            canonical = canonical_from_html(html)
            if canonical != expected:
                fail(f"{route_id}: canonical legacy cambió {canonical!r} != {expected!r}")


def validate_persisted(pilots: list[dict], base_url: str) -> None:
    html_files = sorted(ROOT.rglob("*.html"))
    if len(html_files) != 49:
        fail(f"persisted candidate debe tener 49 HTML (46+3); encontró {len(html_files)}")

    for pilot in pilots:
        route = pilot["target_route"]
        path = physical_path(route)
        if not path.exists():
            fail(f"{pilot['id']}: target ausente {route}")
        html = path.read_text(encoding="utf-8")
        expected_canonical = base_url + route.lstrip("/")
        required = [
            '<meta name="robots" content="noindex,follow">',
            f'<link rel="canonical" href="{expected_canonical}">',
            f'data-v8-pilot="{pilot["id"]}"',
            f'data-source-catalog-id="{pilot["catalog_id"]}"',
            '<main id="contenido">',
            'class="ml-disclosure"',
            *[f'href="{href}"' for href in CSS_REFS],
        ]
        missing = [item for item in required if item not in html]
        if missing:
            fail(f"{pilot['id']}: target persistido incompleto {missing}")
        if len(re.findall(r"<h1\b", html)) != 1:
            fail(f"{pilot['id']}: target debe tener exactamente un H1")
        if re.search(r"<form\b", html, flags=re.I):
            fail(f"{pilot['id']}: target no puede crear form físico")
        validate_local_links(path, html, pilot["id"])


def main() -> int:
    model = load(MODEL)
    route_contract = load(ROUTES)
    site = load(SITE)
    pilots = model.get("pilots") or []
    if len(pilots) != 3:
        fail(f"W4.5 requiere exactamente 3 pilotos; encontró {len(pilots)}")

    target_paths = [physical_path(pilot["target_route"]) for pilot in pilots]
    present = sum(path.exists() for path in target_paths)
    if present not in {0, 3}:
        fail(f"estado parcial no permitido: {present}/3 targets persistidos")

    base_url = str(site.get("base_url", ""))
    parsed = urlsplit(base_url)
    if parsed.scheme != "https" or not parsed.netloc or not base_url.endswith("/"):
        fail("site-config base_url inválida")

    validate_non_activation(pilots, route_contract)
    validate_legacy(route_contract, base_url)

    if present == 0:
        html_files = sorted(ROOT.rglob("*.html"))
        if len(html_files) != 46:
            fail(f"bootstrap W4.5 debe partir de 46 HTML; encontró {len(html_files)}")
        print("VALIDATE V8 PUBLIC TREE BOOTSTRAP OK: 46 legacy intactos, 0/3 targets y cero activación v8.")
        return 0

    validate_persisted(pilots, base_url)
    print("VALIDATE V8 PUBLIC TREE PERSISTED OK: 49 HTML = 46 legacy + 3 targets noindex, sin activación pública y sin links locales rotos.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 PUBLIC TREE FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

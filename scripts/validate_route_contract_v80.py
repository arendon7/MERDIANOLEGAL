#!/usr/bin/env python3
"""Valida W4.2: contrato estructurado de rutas v8 contra baseline v7.4 certificado.

Este validator NO activa rutas v8 ni altera canonical/sitemap. Su función en estado
planning es demostrar que el mapping cubre exactamente la topología certificada y
que ningún cambio de arquitectura parte de un inventario incompleto.
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v8/route-contract-v80.json"
VERSION = ROOT / "version.json"
SITE_CONFIG = ROOT / "site-config.json"
SITEMAP = ROOT / "sitemap.xml"

FIELDS = ["id", "current", "target", "action", "family", "indexed", "sitemap", "priority"]
ACTIONS = {"KEEP", "RENAME", "MOVE", "MERGE", "ALIAS", "REVIEW"}
PRIORITIES = {"P0", "P1", "P2", "P3"}
TARGET_ROOTS = {"practicas", "soluciones", "servicios-continuos", "sectores", "perspectivas"}


def fail(message: str) -> None:
    raise AssertionError(message)


def route_to_path(route: str) -> Path:
    if route == "/":
        return ROOT / "index.html"
    clean = route.lstrip("/")
    if clean.endswith("/"):
        return ROOT / clean / "index.html"
    return ROOT / clean


def route_to_url(base_url: str, route: str) -> str:
    return base_url if route == "/" else base_url + route.lstrip("/")


def canonical_from_html(path: Path) -> str | None:
    value = path.read_text(encoding="utf-8")
    match = re.search(r'<link rel="canonical" href="([^"]+)">', value)
    return match.group(1) if match else None


def robots_from_html(path: Path) -> str:
    value = path.read_text(encoding="utf-8")
    match = re.search(r'<meta name="robots" content="([^"]+)">', value)
    return match.group(1).lower() if match else ""


def main() -> int:
    if not CONTRACT.exists():
        fail("falta assets/data/v8/route-contract-v80.json")

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if contract.get("schema_version") != "1.0.0":
        fail("schema_version v8 route contract debe ser 1.0.0")
    if contract.get("contract") != "v8-route-compatibility":
        fail("contract id inválido")
    if contract.get("status") != "planning":
        fail("W4.2 baseline validator espera status=planning")
    if contract.get("legacy_route_fields") != FIELDS:
        fail("legacy_route_fields cambió sin actualizar validator")

    version = json.loads(VERSION.read_text(encoding="utf-8"))
    baseline = contract.get("baseline") or []
    if len(baseline) != 4:
        fail("baseline debe declarar version, commit, html_count y sitemap_count")
    baseline_version, baseline_commit, html_expected, sitemap_expected = baseline
    if version.get("version") != baseline_version:
        fail(f"version baseline={baseline_version!r} pero version.json={version.get('version')!r}")
    if baseline_commit != "86813813e29dd6b47105ba7fb6259630fcd9cb5b":
        fail("commit baseline W4.2 no coincide con v7.4 certificado")
    if html_expected != 46 or sitemap_expected != 43:
        fail("baseline W4.2 debe conservar 46 HTML y 43 URLs de sitemap antes de migrar")

    raw_routes = contract.get("legacy_routes") or []
    if len(raw_routes) != 46:
        fail(f"se esperaban 46 legacy_routes y hay {len(raw_routes)}")

    routes: list[dict] = []
    for row in raw_routes:
        if not isinstance(row, list) or len(row) != len(FIELDS):
            fail(f"fila legacy inválida: {row!r}")
        item = dict(zip(FIELDS, row))
        routes.append(item)

    ids = [item["id"] for item in routes]
    currents = [item["current"] for item in routes]
    if len(ids) != len(set(ids)):
        fail("IDs legacy duplicados")
    if len(currents) != len(set(currents)):
        fail("current routes duplicadas")

    for item in routes:
        if item["action"] not in ACTIONS:
            fail(f"{item['id']}: action inválida {item['action']!r}")
        if item["priority"] not in PRIORITIES:
            fail(f"{item['id']}: priority inválida {item['priority']!r}")
        for key in ("current", "target"):
            route = item[key]
            if not isinstance(route, str) or not route.startswith("/"):
                fail(f"{item['id']}: {key} debe ser ruta absoluta de sitio")
            parsed = urlsplit(route)
            if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
                fail(f"{item['id']}: {key} no puede contener host/query/fragment")
        path = route_to_path(item["current"])
        if not path.exists():
            fail(f"{item['id']}: legacy física inexistente {path.relative_to(ROOT)}")

    actual_html = sorted(ROOT.rglob("*.html"))
    if len(actual_html) != html_expected:
        fail(f"baseline físico esperado={html_expected} HTML; encontrado={len(actual_html)}")
    physical_routes = set()
    for path in actual_html:
        rel = path.relative_to(ROOT).as_posix()
        if rel == "index.html":
            route = "/"
        elif rel.endswith("/index.html"):
            route = "/" + rel[:-len("index.html")]
        else:
            route = "/" + rel
        physical_routes.add(route)
    if physical_routes != set(currents):
        missing = sorted(set(currents) - physical_routes)
        extra = sorted(physical_routes - set(currents))
        fail(f"contract/árbol divergen; missing={missing}, extra={extra}")

    config = json.loads(SITE_CONFIG.read_text(encoding="utf-8"))
    base_url = str(config.get("base_url", ""))
    if not base_url.startswith("https://") or not base_url.endswith("/"):
        fail("site-config base_url inválida")

    sitemap_text = SITEMAP.read_text(encoding="utf-8")
    sitemap_urls = re.findall(r"<loc>([^<]+)</loc>", sitemap_text)
    if len(sitemap_urls) != sitemap_expected:
        fail(f"sitemap baseline esperado={sitemap_expected}; encontrado={len(sitemap_urls)}")
    expected_sitemap = {
        route_to_url(base_url, item["current"])
        for item in routes if item["sitemap"]
    }
    if set(sitemap_urls) != expected_sitemap:
        missing = sorted(expected_sitemap - set(sitemap_urls))
        extra = sorted(set(sitemap_urls) - expected_sitemap)
        fail(f"sitemap/contract divergen; missing={missing}, extra={extra}")

    for item in routes:
        path = route_to_path(item["current"])
        robots = robots_from_html(path)
        if item["indexed"]:
            if "noindex" in robots:
                fail(f"{item['id']}: contract indexed=true pero HTML declara noindex")
            expected = route_to_url(base_url, item["current"])
            canonical = canonical_from_html(path)
            if canonical != expected:
                fail(f"{item['id']}: baseline debe ser self-canonical; {canonical!r} != {expected!r}")
        else:
            if item["id"] in {"T04", "T09"} and "noindex" not in robots:
                fail(f"{item['id']}: demo/404 deben permanecer noindex")

    families = contract.get("target_families") or {}
    practices = families.get("practices") or []
    solutions = families.get("solutions") or []
    recurring = families.get("recurring") or []
    if len(practices) != 6:
        fail(f"target practices debe contener 6 y contiene {len(practices)}")
    if len(solutions) != 8:
        fail(f"target solutions debe contener 8 y contiene {len(solutions)}")
    if len(recurring) != 2:
        fail(f"target recurring debe contener 2 y contiene {len(recurring)}")

    target_codes = []
    target_routes = []
    for family_name, rows in (("practices", practices), ("solutions", solutions)):
        for row in rows:
            if not isinstance(row, list) or len(row) != 2:
                fail(f"{family_name}: target row inválida {row!r}")
            code, route = row
            target_codes.append(code); target_routes.append(route)
    for row in recurring:
        if not isinstance(row, list) or len(row) != 3:
            fail(f"recurring target row inválida {row!r}")
        code, route, publishable = row
        target_codes.append(code); target_routes.append(route)
        if code == "RC02" and publishable is not False:
            fail("RC02 Meridiano Contratos debe permanecer publishable=false en W4.2")
    if len(target_codes) != len(set(target_codes)):
        fail("target codes duplicados")
    if len(target_routes) != len(set(target_routes)):
        fail("target routes duplicadas")
    for route in target_routes:
        root = route.strip("/").split("/", 1)[0]
        if root not in TARGET_ROOTS:
            fail(f"target route fuera de familias v8: {route}")

    policies = contract.get("policies") or {}
    if policies.get("legacy_removal") != "forbidden_until_w42_certified":
        fail("W4.2 no permite retirar legacy routes")
    if policies.get("github_pages_server_redirects") != "not_assumed":
        fail("W4.2 no puede asumir redirects de servidor en GitHub Pages")
    if policies.get("stable") != "do_not_modify_manually":
        fail("stable debe permanecer protegido por promoción certificada")

    print(
        "VALIDATE ROUTE CONTRACT V8.0 OK: 46/46 legacy routes, 43/43 sitemap URLs, "
        "baseline self-canonical, 6 practices, 8 solutions, 2 recurring y RC02 bloqueado."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"VALIDATE ROUTE CONTRACT V8.0 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

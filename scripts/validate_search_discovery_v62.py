#!/usr/bin/env python3
"""Valida Search Discovery Readiness v6.2 y su frontera de indexación."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET

from apply_search_discovery_v62 import (
    CONTRACT,
    ROOT,
    expected_self_url,
    indexable_canonicals,
    page_signals,
    public_html_targets,
    render_sitemap,
)
from site_config import load_site_config

SITEMAP = ROOT / "sitemap.xml"
ROBOTS = ROOT / "robots.txt"
HOME = ROOT / "index.html"
RUNTIME = ROOT / "runtime-config.js"
VERIFICATION_TAG = re.compile(
    r"<meta\b(?=[^>]*\bname=[\"']google-site-verification[\"'])[^>]*\bcontent=[\"']([^\"']*)[\"'][^>]*>",
    re.IGNORECASE,
)


def fail(errors: list[str]) -> int:
    print("SEARCH DISCOVERY V6.2 FAIL", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


def main() -> int:
    errors: list[str] = []
    try:
        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        config = load_site_config()
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as exc:
        return fail([str(exc)])

    expected_contract = {
        "status": "readiness-not-verified",
        "provider": "google-search-console",
        "property_type": "url-prefix",
    }
    for key, expected in expected_contract.items():
        if contract.get(key) != expected:
            errors.append(f"contrato: {key} debe ser {expected!r}")
    verification = contract.get("verification") or {}
    if verification.get("method") != "html-meta" or verification.get("config_key") != "search_console_verification":
        errors.append("contrato: verificación debe usar html-meta desde search_console_verification")
    if verification.get("requires_authentic_token") is not True:
        errors.append("contrato: debe exigir token auténtico")
    sitemap_contract = contract.get("sitemap") or {}
    for key in ("include_optional_lastmod", "include_priority", "include_changefreq"):
        if sitemap_contract.get(key) is not False:
            errors.append(f"contrato: {key} debe permanecer false en readiness")

    html_targets = public_html_targets()
    if len(html_targets) != 46:
        errors.append(f"frontera pública: se esperaban 46 HTML y se encontraron {len(html_targets)}")

    noindex_paths: set[str] = set()
    try:
        entries = indexable_canonicals(config["base_url"])
    except ValueError as exc:
        errors.extend(str(exc).splitlines())
        entries = []

    for path in html_targets:
        signals = page_signals(path)
        relative = path.relative_to(ROOT).as_posix()
        robots_values = {
            part.strip()
            for value in signals.robots
            for part in value.split(",")
            if part.strip()
        }
        if "noindex" in robots_values:
            noindex_paths.add(relative)
        elif len(signals.canonicals) == 1:
            expected = expected_self_url(path, config["base_url"])
            if signals.canonicals[0] != expected:
                errors.append(f"{relative}: canonical debe ser autorreferencial")

    expected_noindex = {"404.html", "demo.html", "experiencia.html"}
    if noindex_paths != expected_noindex:
        errors.append(f"frontera noindex debe ser exactamente {sorted(expected_noindex)} y es {sorted(noindex_paths)}")
    if len(entries) != 43:
        errors.append(f"sitemap/indexación: se esperaban 43 páginas indexables y se encontraron {len(entries)}")

    sitemap_text = SITEMAP.read_text(encoding="utf-8") if SITEMAP.exists() else ""
    if any(tag in sitemap_text for tag in ("<lastmod>", "<priority>", "<changefreq>")):
        errors.append("sitemap.xml: readiness v6.2 no debe publicar lastmod, priority ni changefreq no verificables")
    try:
        root = ET.fromstring(sitemap_text)
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        locs = [(node.text or "").strip() for node in root.findall(f"{ns}url/{ns}loc")]
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml: XML inválido: {exc}")
        locs = []
    expected_locs = [url for _, url in entries]
    if locs != expected_locs:
        errors.append("sitemap.xml: la secuencia de loc debe coincidir exactamente con las páginas indexables autorreferenciales")
    if len(locs) != len(set(locs)):
        errors.append("sitemap.xml: existen URLs duplicadas")
    if sitemap_text and sitemap_text != render_sitemap(config["base_url"]):
        errors.append("sitemap.xml: no coincide con la representación canónica v6.2")

    robots = ROBOTS.read_text(encoding="utf-8") if ROBOTS.exists() else ""
    sitemap_line = f"Sitemap: {config['base_url']}sitemap.xml"
    if robots.count(sitemap_line) != 1:
        errors.append("robots.txt: debe declarar exactamente una referencia al sitemap canónico")
    if "/demo.html" not in robots:
        errors.append("robots.txt: falta exclusión explícita de demo.html")

    home = HOME.read_text(encoding="utf-8")
    verification_values = VERIFICATION_TAG.findall(home)
    token = config["search_console_verification"]
    if token:
        if verification_values != [token]:
            errors.append("index.html: token configurado requiere exactamente una meta google-site-verification con valor exacto")
    elif verification_values:
        errors.append("index.html: no puede publicar google-site-verification mientras el token canónico esté vacío")

    runtime = RUNTIME.read_text(encoding="utf-8") if RUNTIME.exists() else ""
    expected_runtime_flag = '"searchConsoleConfigured":true' if token else '"searchConsoleConfigured":false'
    if expected_runtime_flag not in runtime:
        errors.append("runtime-config.js: searchConsoleConfigured no coincide con la existencia del token canónico")

    if errors:
        return fail(errors)
    print(
        "SEARCH DISCOVERY V6.2 OK: 46 HTML clasificados, 43 indexables con canonical propio, "
        "3 noindex fuera del sitemap y Search Console sin afirmaciones ficticias."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

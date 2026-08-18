#!/usr/bin/env python3
"""Sincroniza versión y metadatos públicos de release en cualquier baseline canónica.

Este paso corre tanto en baselines legacy como en Experience v6. En una baseline ya
v6, donde apply_production_v50.py no vuelve a ejecutarse, debe mantener alineadas
las etiquetas públicas ya versionadas, los metadatos de modificación editorial,
runtime-config.js, site-status.json y los lastmod del sitemap con version.json sin
alterar capabilities, fechas de publicación ni configuración productiva.

`--check` no escribe: retorna 0 solo cuando todas las superficies versionadas y los
metadatos de release coinciden exactamente con version.json + site-config.json.
"""
from pathlib import Path
import json
import re
import sys

from site_config import load_site_config

ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "version.json"
WEB_PUBLIC_PATTERN = re.compile(r"Web pública v\d+\.\d+\.\d+")
WEB_DEMO_PATTERN = re.compile(r"Web demostrativa v\d+\.\d+\.\d+")
DETAIL_PATTERN = re.compile(r"Ficha v\d+\.\d+\.\d+")
ARTICLE_MODIFIED_PATTERN = re.compile(r'<meta property="article:modified_time" content="\d{4}-\d{2}-\d{2}">')
SCHEMA_MODIFIED_PATTERN = re.compile(r'"dateModified":"\d{4}-\d{2}-\d{2}"')
LASTMOD_PATTERN = re.compile(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>")
PUBLIC_DIRS = ("servicios", "productos", "soluciones", "sectores", "perspectivas")


def render_runtime(config: dict, version_data: dict) -> str:
    portal = config["capabilities"]["client_portal"]
    safe = {
        "name": config.get("name", "Meridiano Legal"),
        "baseUrl": config["base_url"],
        "publicPath": config["public_path"],
        "version": version_data["version"],
        "releaseDate": version_data["release_date"],
        "environment": config.get("environment", "public"),
        "deployment": config.get("deployment", "github-pages"),
        "contact": config["contact"],
        "analytics": config["analytics"],
        "searchConsoleConfigured": bool(config["search_console_verification"]),
        "capabilities": {
            "clientPortal": {"enabled": portal["enabled"], "url": portal["url"]}
        },
    }
    payload = json.dumps(safe, ensure_ascii=False, separators=(",", ":"))
    return f"window.MERIDIANO_PUBLIC_CONFIG = Object.freeze({payload});\n"


def render_status(config: dict, version_data: dict) -> str:
    portal = config["capabilities"]["client_portal"]
    status = {
        "name": config.get("name", "Meridiano Legal"),
        "version": version_data["version"],
        "release_date": version_data["release_date"],
        "environment": config.get("environment", "public"),
        "deployment": config.get("deployment", "github-pages"),
        "base_url": config["base_url"],
        "public_path": config["public_path"],
        "custom_domain": config["custom_domain"] or None,
        "analytics": "enabled" if config["analytics"]["enabled"] else "disabled",
        "contact_channel": "whatsapp",
        "demo_indexing": "noindex",
        "client_portal": "enabled" if portal["enabled"] else "disabled",
        "client_portal_url": portal["url"] or None,
    }
    return json.dumps(status, ensure_ascii=False, indent=2) + "\n"


def version_data() -> dict:
    data = json.loads(VERSION_PATH.read_text(encoding="utf-8"))
    version = str(data["version"])
    release_date = str(data["release_date"])
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit(f"version.json contiene semver inválido: {version!r}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", release_date):
        raise SystemExit(f"version.json contiene release_date inválida: {release_date!r}")
    return data


def public_html_targets() -> list[Path]:
    targets = list(ROOT.glob("*.html"))
    for folder in PUBLIC_DIRS:
        targets.extend((ROOT / folder).glob("*.html"))
    return sorted(set(targets))


def synchronize_html(text: str, version: str, release_date: str) -> str:
    text = WEB_PUBLIC_PATTERN.sub(f"Web pública v{version}", text)
    text = WEB_DEMO_PATTERN.sub(f"Web demostrativa v{version}", text)
    text = DETAIL_PATTERN.sub(f"Ficha v{version}", text)
    text = ARTICLE_MODIFIED_PATTERN.sub(
        f'<meta property="article:modified_time" content="{release_date}">', text
    )
    text = SCHEMA_MODIFIED_PATTERN.sub(f'"dateModified":"{release_date}"', text)
    return text


def synchronize_sitemap(text: str, release_date: str) -> str:
    if not LASTMOD_PATTERN.search(text):
        raise SystemExit("sitemap.xml no contiene lastmod versionables")
    return LASTMOD_PATTERN.sub(f"<lastmod>{release_date}</lastmod>", text)


def expected_texts(config: dict, data: dict) -> dict[str, str]:
    version = str(data["version"])
    release_date = str(data["release_date"])
    expected: dict[str, str] = {}

    for path in public_html_targets():
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        updated = synchronize_html(text, version, release_date)
        if updated != text:
            expected[relative] = updated

    for relative in ("catalog-home-v32.js", "decision-flow.js"):
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated = WEB_PUBLIC_PATTERN.sub(f"Web pública v{version}", text)
        updated = WEB_DEMO_PATTERN.sub(f"Web demostrativa v{version}", updated)
        updated = DETAIL_PATTERN.sub(f"Ficha v{version}", updated)
        if updated != text:
            expected[relative] = updated

    sitemap = ROOT / "sitemap.xml"
    if sitemap.exists():
        current_sitemap = sitemap.read_text(encoding="utf-8")
        updated_sitemap = synchronize_sitemap(current_sitemap, release_date)
        if updated_sitemap != current_sitemap:
            expected["sitemap.xml"] = updated_sitemap

    expected["runtime-config.js"] = render_runtime(config, data)
    expected["site-status.json"] = render_status(config, data)
    return expected


def pending_changes(config: dict, data: dict) -> list[str]:
    pending: list[str] = []
    for relative, expected in expected_texts(config, data).items():
        path = ROOT / relative
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != expected:
            pending.append(relative)
    return sorted(pending)


def apply(config: dict, data: dict) -> list[str]:
    expected = expected_texts(config, data)
    changed = pending_changes(config, data)
    for relative in changed:
        (ROOT / relative).write_text(expected[relative], encoding="utf-8")
    return changed


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    data = version_data()
    config = load_site_config()
    pending = pending_changes(config, data)

    if args == ["--check"]:
        if pending:
            print("RELEASE METADATA DRIFT")
            for relative in pending:
                print(f"- {relative}")
            return 1
        print(f"RELEASE METADATA SYNC OK: {data['version']} ({data['release_date']})")
        return 0
    if args:
        raise SystemExit(f"uso: {Path(sys.argv[0]).name} [--check]")

    changed = apply(config, data)
    print(f"Release pública sincronizada: {data['version']} ({data['release_date']})")
    for relative in changed:
        print(f"- {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

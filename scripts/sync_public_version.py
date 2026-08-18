#!/usr/bin/env python3
"""Sincroniza versión y metadatos públicos de release en cualquier baseline canónica.

Este paso corre tanto en baselines legacy como en Experience v6. En una baseline ya
v6, donde apply_production_v50.py no vuelve a ejecutarse, debe mantener alineados el
rótulo visible, runtime-config.js y site-status.json con version.json sin alterar
capabilities ni configuración productiva.
"""
from pathlib import Path
import json
import re

from site_config import load_site_config

ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "version.json"
PATTERN = re.compile(r"Web (?:demostrativa|pública) v\d+\.\d+\.\d+")


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


def write_if_changed(path: Path, content: str, changed: list[str]) -> None:
    before = path.read_text(encoding="utf-8") if path.exists() else ""
    if before != content:
        path.write_text(content, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def main() -> int:
    version_data = json.loads(VERSION_PATH.read_text(encoding="utf-8"))
    version = str(version_data["version"])
    release_date = str(version_data["release_date"])
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit(f"version.json contiene semver inválido: {version!r}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", release_date):
        raise SystemExit(f"version.json contiene release_date inválida: {release_date!r}")

    config = load_site_config()
    changed: list[str] = []

    # index.html es siempre la superficie pública, incluso cuando la release está
    # en canal candidate. El canal describe estado de certificación, no capability.
    replacements = {
        "index.html": f"Web pública v{version}",
        "catalog-home-v32.js": f"Web demostrativa v{version}",
        "decision-flow.js": f"Web demostrativa v{version}",
    }
    for relative, replacement in replacements.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated, count = PATTERN.subn(replacement, text)
        if count and updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(relative)

    write_if_changed(ROOT / "runtime-config.js", render_runtime(config, version_data), changed)
    write_if_changed(ROOT / "site-status.json", render_status(config, version_data), changed)

    print(f"Release pública sincronizada: {version} ({release_date})")
    for relative in changed:
        print(f"- {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

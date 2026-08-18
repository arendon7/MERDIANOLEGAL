#!/usr/bin/env python3
"""Sincroniza versión y metadatos públicos de release en cualquier baseline canónica.

Este paso corre tanto en baselines legacy como en Experience v6. En una baseline ya
v6, donde apply_production_v50.py no vuelve a ejecutarse, debe mantener alineados el
rótulo visible, runtime-config.js y site-status.json con version.json sin alterar
capabilities ni configuración productiva.

`--check` no escribe: retorna 0 solo cuando las cinco superficies de metadata ya
coinciden exactamente con version.json + site-config.json.
"""
from pathlib import Path
import json
import re
import sys

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


def version_data() -> dict:
    data = json.loads(VERSION_PATH.read_text(encoding="utf-8"))
    version = str(data["version"])
    release_date = str(data["release_date"])
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise SystemExit(f"version.json contiene semver inválido: {version!r}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", release_date):
        raise SystemExit(f"version.json contiene release_date inválida: {release_date!r}")
    return data


def expected_texts(config: dict, data: dict) -> dict[str, str]:
    version = str(data["version"])
    expected: dict[str, str] = {}
    for relative, replacement in {
        "index.html": f"Web pública v{version}",
        "catalog-home-v32.js": f"Web demostrativa v{version}",
        "decision-flow.js": f"Web demostrativa v{version}",
    }.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        expected[relative] = PATTERN.sub(replacement, text)
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
    return pending


def apply(config: dict, data: dict) -> list[str]:
    changed = pending_changes(config, data)
    expected = expected_texts(config, data)
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

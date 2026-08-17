#!/usr/bin/env python3
"""Sincroniza la versión visible distinguiendo superficie pública y componentes demostrativos."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "version.json"
PATTERN = re.compile(r"Web (?:demostrativa|pública) v\d+\.\d+\.\d+")


def main() -> int:
    data = json.loads(VERSION_PATH.read_text(encoding="utf-8"))
    version = data["version"]
    # index.html es siempre la superficie pública, incluso cuando la release está
    # en canal candidate. El canal describe estado de certificación, no capability.
    replacements = {
        "index.html": f"Web pública v{version}",
        "catalog-home-v32.js": f"Web demostrativa v{version}",
        "decision-flow.js": f"Web demostrativa v{version}",
    }
    changed = []

    for relative, replacement in replacements.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated, count = PATTERN.subn(replacement, text)
        if count and updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(relative)

    print(f"Versión pública sincronizada: Web pública v{version}")
    for relative in changed:
        print(f"- {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

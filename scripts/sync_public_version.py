#!/usr/bin/env python3
"""Sincroniza las etiquetas visibles de versión con version.json."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "version.json"
TARGETS = {
    "index.html": re.compile(r"Web demostrativa v\d+\.\d+\.\d+"),
    "catalog-home-v32.js": re.compile(r"Web demostrativa v\d+\.\d+\.\d+"),
    "decision-flow.js": re.compile(r"Web demostrativa v\d+\.\d+\.\d+"),
}


def main() -> int:
    version = json.loads(VERSION_PATH.read_text(encoding="utf-8"))["version"]
    replacement = f"Web demostrativa v{version}"
    changed = []
    for relative, pattern in TARGETS.items():
        path = ROOT / relative
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated, count = pattern.subn(replacement, text)
        if count and updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(relative)
    print(f"Versión pública sincronizada: {version}")
    for relative in changed:
        print(f"- {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

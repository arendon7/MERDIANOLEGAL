#!/usr/bin/env python3
"""Aplica v5.18: observabilidad local del handoff manual, sin PII ni persistencia."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SCRIPT = '<script defer src="handoff-observability-v518.js"></script>'
ANCHOR = '<script defer src="telemetry-v50.js"></script>'


def main() -> int:
    text = HOME.read_text(encoding="utf-8")
    text = re.sub(r'(?m)^[ \t]*' + re.escape(SCRIPT) + r'[ \t]*(?:\r?\n)?', "", text)
    if ANCHOR not in text:
        raise RuntimeError("index.html: falta telemetry-v50.js para ordenar observabilidad v5.18")
    text = text.replace(ANCHOR, ANCHOR + "\n  " + SCRIPT, 1)
    if text.count(SCRIPT) != 1:
        raise RuntimeError("index.html: v5.18 debe cargar una sola vez handoff-observability-v518.js")
    if text.find(ANCHOR) > text.find(SCRIPT):
        raise RuntimeError("index.html: observabilidad v5.18 debe cargar después de telemetry-v50.js")
    HOME.write_text(text, encoding="utf-8")
    print("HANDOFF OBSERVABILITY V5.18 OK: runtime local insertado después de telemetry-v50.js.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

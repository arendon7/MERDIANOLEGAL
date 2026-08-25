#!/usr/bin/env python3
"""Valida contraste mínimo de tokens textuales críticos del sistema visual v8."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "assets/css/v8/tokens.css"
AA_NORMAL = 4.5


def parse_tokens() -> dict[str, str]:
    text = TOKENS.read_text(encoding="utf-8")
    pairs = dict(re.findall(r"(--ml-[\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\s*;", text))
    if not pairs:
        raise AssertionError("no se pudieron leer tokens hex v8")
    return {key: value.lower() for key, value in pairs.items()}


def channel(value: int) -> float:
    c = value / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(color: str) -> float:
    values = [int(color[i : i + 2], 16) for i in (1, 3, 5)]
    r, g, b = (channel(value) for value in values)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(foreground: str, background: str) -> float:
    a, b = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def require(tokens: dict[str, str], foreground: str, background: str, label: str) -> None:
    if foreground not in tokens or background not in tokens:
        raise AssertionError(f"{label}: faltan tokens {foreground}/{background}")
    value = ratio(tokens[foreground], tokens[background])
    if value < AA_NORMAL:
        raise AssertionError(
            f"{label}: contraste {value:.2f}:1 < {AA_NORMAL:.1f}:1 "
            f"({foreground}={tokens[foreground]} sobre {background}={tokens[background]})"
        )
    print(f"PASS {label}: {value:.2f}:1")


def main() -> int:
    tokens = parse_tokens()
    checks = (
        ("--ml-muted", "--ml-white", "texto secundario / blanco"),
        ("--ml-muted", "--ml-ivory", "texto secundario / ivory"),
        ("--ml-muted", "--ml-soft", "texto secundario / soft"),
        ("--ml-gold-ink", "--ml-white", "etiqueta oro textual / blanco"),
        ("--ml-gold-ink", "--ml-ivory", "etiqueta oro textual / ivory"),
        ("--ml-white", "--ml-navy", "botón primario / navy"),
        ("--ml-white", "--ml-navy-deep", "texto inverso / navy deep"),
        ("--ml-navy", "--ml-white", "acción secundaria / blanco"),
        ("--ml-ink", "--ml-white", "copy principal / blanco"),
    )
    for foreground, background, label in checks:
        require(tokens, foreground, background, label)

    brand_gold = tokens.get("--ml-gold")
    gold_ink = tokens.get("--ml-gold-ink")
    if not brand_gold or not gold_ink or brand_gold == gold_ink:
        raise AssertionError("v8 debe separar oro de marca y oro textual accesible")

    print("VALIDATE V8 CONTRAST TOKENS OK: pares textuales críticos cumplen WCAG AA 4.5:1.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE V8 CONTRAST TOKENS FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

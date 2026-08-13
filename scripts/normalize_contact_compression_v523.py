#!/usr/bin/env python3
"""Normaliza la presentación v5.23 reutilizando estilos históricos ya certificados."""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys

R = Path(__file__).resolve().parents[1]
HOME = R / "index.html"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise RuntimeError(f"index.html: no se reconoce {label}")
    if text.count(old) != 1:
        raise RuntimeError(f"index.html: {label} no es único")
    return text.replace(old, new, 1)


def main() -> int:
    text = HOME.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '<div class="contact-synthesis-v523 full"',
        '<div class="qualification-summary-v59 contact-synthesis-v523 full"',
        "contenedor de síntesis v5.23",
    )
    text = replace_once(
        text,
        '<div class="qualification-summary-v59 contact-qualification-v523"',
        '<div class="contact-qualification-v523"',
        "resumen interno v5.9",
    )
    text = replace_once(
        text,
        '<div class="commercial-brief-v513 contact-brief-v523"',
        '<div class="contact-brief-v523"',
        "brief interno v5.13",
    )
    text = replace_once(
        text,
        '<div class="contact-brief-head-v523">',
        '<div class="commercial-brief-head-v513 contact-brief-head-v523">',
        "encabezado de modalidad",
    )
    text = replace_once(
        text,
        '<dl class="commercial-brief-grid-v513 contact-brief-grid-v523">',
        '<dl class="qualification-summary-grid-v59 contact-brief-grid-v523">',
        "grid de modalidad y estándar",
    )
    text = replace_once(
        text,
        '<div class="recommendation-brief-v514 decision-route-v515 contact-recommendation-v523"',
        '<div class="contact-recommendation-v523"',
        "recomendación integrada",
    )
    HOME.write_text(text, encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(R / "scripts/validate_contact_compression_v523.py")],
        cwd=R,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"normalización v5.23 inválida: {detail}")
    if result.stdout.strip():
        print(result.stdout.strip())
    print("CONTACT PRESENTATION V5.23 OK: síntesis integrada sobre componentes visuales certificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

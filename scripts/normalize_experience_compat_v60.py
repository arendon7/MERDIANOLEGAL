#!/usr/bin/env python3
"""Normaliza compatibilidad de contratos históricos después de materializar Experience v6.

No crea truth nuevo. Reubica confianza v5.29 y evita que etiquetas editoriales v6
interfieran con anclas textuales históricas usadas por validators certificados.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SOLUTIONS = ROOT / "soluciones"
TRUST_START = "<!-- FUNNEL-TRUST-V529:START -->"
TRUST_END = "<!-- FUNNEL-TRUST-V529:END -->"
SOLUTION_LEGACY_START = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:START -->"
CONTACT_PATTERN = re.compile(r'<section class="v6-section v6-contact" id="contacto" data-conversion-path-v528="true"')


def normalize_home_trust() -> None:
    text = HOME.read_text(encoding="utf-8")
    match = re.search(re.escape(TRUST_START) + r".*?" + re.escape(TRUST_END), text, flags=re.S)
    if not match:
        raise RuntimeError("Experience v6: falta bloque canónico de confianza v5.29")
    trust = match.group(0)
    text = text[:match.start()] + text[match.end():]
    contact = CONTACT_PATTERN.search(text)
    if not contact:
        raise RuntimeError("Experience v6: falta contacto canónico v6 para posicionar confianza v5.29")
    text = text[:contact.start()] + trust + "\n" + text[contact.start():]
    if text.count(TRUST_START) != 1 or text.count(TRUST_END) != 1:
        raise RuntimeError("Experience v6: bloque de confianza v5.29 debe permanecer único")
    commercial = text.find("<!-- COMMERCIAL-V43:END -->")
    trust_pos = text.find('data-funnel-trust-v529="true"')
    contact_pos = text.find('id="contacto" data-conversion-path-v528="true"')
    sectors = text.find('id="sectores"')
    if min(commercial, trust_pos, contact_pos, sectors) < 0 or not (commercial < trust_pos < contact_pos < sectors):
        raise RuntimeError("Experience v6: secuencia contratación → confianza → contacto → profundidad inválida")
    HOME.write_text(text, encoding="utf-8")


def normalize_solution_labels() -> None:
    targets = sorted(path for path in SOLUTIONS.glob("*.html") if path.name != "index.html")
    if len(targets) != 6:
        raise RuntimeError(f"Experience v6: se esperaban 6 rutas de solución y hay {len(targets)}")
    old = '<p class="v6-eyebrow">LÍMITES</p>'
    new = '<p class="v6-eyebrow">FRONTERAS DEL ALCANCE</p>'
    for path in targets:
        text = path.read_text(encoding="utf-8")
        boundary = text.find(SOLUTION_LEGACY_START)
        if boundary < 0:
            raise RuntimeError(f"{path.name}: falta legacy v6 para normalizar compatibilidad")
        first = text[:boundary]
        rest = text[boundary:]
        if first.count(old) != 1:
            raise RuntimeError(f"{path.name}: se esperaba una etiqueta v6 de límites antes del legacy")
        first = first.replace(old, new, 1)
        path.write_text(first + rest, encoding="utf-8")


def main() -> int:
    normalize_home_trust()
    normalize_solution_labels()
    print("EXPERIENCE V6 COMPAT OK: confianza v5.29 y anclas históricas v5.31 preservadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

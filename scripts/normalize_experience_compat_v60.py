#!/usr/bin/env python3
"""Normaliza compatibilidad de contratos históricos después de materializar Experience v6.

No crea contenido nuevo: reubica el bloque canónico de confianza v5.29 para conservar
la secuencia material contratación → confianza → contacto → profundidad exigida por v5.29.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
TRUST_START = "<!-- FUNNEL-TRUST-V529:START -->"
TRUST_END = "<!-- FUNNEL-TRUST-V529:END -->"
CONTACT_PATTERN = re.compile(r'<section class="v6-section v6-contact" id="contacto" data-conversion-path-v528="true"')


def main() -> int:
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
    print("EXPERIENCE V6 COMPAT OK: confianza v5.29 preservada antes del contacto v6.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

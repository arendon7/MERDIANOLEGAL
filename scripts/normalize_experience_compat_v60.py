#!/usr/bin/env python3
"""Normaliza compatibilidad de contratos históricos después de materializar Experience v6.

No crea truth nuevo. Reubica confianza v5.29, preserva el contrato de contacto v5.28
y evita que etiquetas editoriales v6 interfieran con anclas históricas certificadas.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SOLUTIONS = ROOT / "soluciones"
TRUST_START = "<!-- FUNNEL-TRUST-V529:START -->"
TRUST_END = "<!-- FUNNEL-TRUST-V529:END -->"
READINESS_START = "<!-- CONVERSION-READINESS-V528:START -->"
READINESS_END = "<!-- CONVERSION-READINESS-V528:END -->"
SOLUTION_LEGACY_START = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:START -->"
CONTACT_PATTERN = re.compile(r'<section class="v6-section v6-contact" id="contacto" data-conversion-path-v528="true"')
READINESS_MARKUP = f'''{READINESS_START}
<div class="contact-readiness-v528" data-conversion-readiness-v528="true" role="region" aria-label="Información mínima para presentar una necesidad">
  <div class="contact-readiness-copy-v528">
    <span>PARA AVANZAR</span>
    <strong>Cuéntenos tres cosas. El alcance profesional se define después.</strong>
    <p>No envíe documentos ni información confidencial en esta etapa. Primero validamos contexto, conflicto, disponibilidad y el alcance a cotizar.</p>
  </div>
  <div class="contact-readiness-items-v528" tabindex="0" role="region" aria-label="Datos mínimos de la solicitud">
    <span><b>1</b><small>Decisión o problema</small></span>
    <span><b>2</b><small>Plazo o urgencia</small></span>
    <span><b>3</b><small>Resultado esperado</small></span>
  </div>
</div>
{READINESS_END}'''


def normalize_home_contact_contract(text: str) -> str:
    if not CONTACT_PATTERN.search(text):
        raise RuntimeError("Experience v6: falta contacto canónico v6 para preservar v5.28")

    # v6 conserva toda la profundidad histórica, por lo que el bloque v5.28 puede
    # quedar dentro del legacy. Se extrae y se reubica, nunca se duplica.
    managed = re.search(re.escape(READINESS_START) + r".*?" + re.escape(READINESS_END), text, flags=re.S)
    readiness = managed.group(0) if managed else READINESS_MARKUP
    if managed:
        text = text[:managed.start()] + text[managed.end():]

    pattern = re.compile(r'(<div class="v6-contact-copy">.*?)(</div><div class="v6-contact-form">)', re.S)
    text, count = pattern.subn(lambda match: match.group(1) + readiness + match.group(2), text, count=1)
    if count != 1:
        raise RuntimeError("Experience v6: no fue posible reubicar preparación v5.28 dentro del contacto")

    if text.count('data-conversion-readiness-v528="true"') != 1:
        raise RuntimeError("Experience v6: preparación v5.28 debe permanecer única")
    if text.count(READINESS_START) != 1 or text.count(READINESS_END) != 1:
        raise RuntimeError("Experience v6: marcadores de preparación v5.28 deben permanecer únicos")

    # El portal real continúa deshabilitado. En el shell v6 se evita la etiqueta
    # heredada 'Demo de cliente' y se conserva una frontera demostrativa explícita.
    text = re.sub(
        r'(<a\b[^>]*\bhref="demo\.html(?:#[^"]*)?"[^>]*>)\s*Demo de cliente\s*(</a>)',
        r'\1Centro demo\2',
        text,
    )
    if re.search(r'>\s*Demo de cliente\s*<', text, re.I):
        raise RuntimeError("Experience v6: el shell público no debe presentar la demo como 'Demo de cliente'")
    return text


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
    text = normalize_home_contact_contract(text)
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
    print("EXPERIENCE V6 COMPAT OK: confianza v5.29, contacto v5.28, capability truth y anclas v5.31 preservados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Normaliza compatibilidad de contratos históricos después de materializar Experience v6.

No crea truth jurídico nuevo. Reubica confianza v5.29, preserva el contrato de
contacto v5.28, evita que etiquetas editoriales v6 interfieran con anclas
históricas certificadas y cablea el adapter de medición v6.1 en las superficies
que ya exponen telemetría local. La activación de terceros sigue gobernada por
site-config.json y permanece deshabilitada por defecto.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SOLUTIONS = ROOT / "soluciones"
TRUST_START = "<!-- FUNNEL-TRUST-V529:START -->"
TRUST_END = "<!-- FUNNEL-TRUST-V529:END -->"
READINESS_START = "<!-- CONVERSION-READINESS-V528:START -->"
READINESS_END = "<!-- CONVERSION-READINESS-V528:END -->"
SOLUTION_LEGACY_START = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:START -->"
CONTACT_PATTERN = re.compile(r'<section class="v6-section v6-contact" id="contacto" data-conversion-path-v528="true"')
ANALYTICS_SCRIPT = "assets/js/v6/analytics-adapter-v61.js"
TELEMETRY_SCRIPT = "telemetry-v50.js"
PUBLIC_DIRS = ("servicios", "productos", "soluciones", "sectores", "perspectivas")
EXPECTED_INSTRUMENTED = 43
EXPECTED_UNTOUCHED = 3
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


def public_html_targets() -> list[Path]:
    targets = list(ROOT.glob("*.html"))
    for folder in PUBLIC_DIRS:
        targets.extend((ROOT / folder).glob("*.html"))
    return sorted(set(targets))


def normalize_measurement_runtime() -> tuple[int, int]:
    """Inserta el adapter v6.1 solo donde la telemetría local ya existe."""
    instrumented = 0
    untouched = 0
    adapter_pattern = re.compile(
        r'^[ \t]*<script defer src="[^"]*assets/js/v6/analytics-adapter-v61\.js"></script>[ \t]*(?:\r?\n)?',
        re.M,
    )
    telemetry_pattern = re.compile(r'<script defer src="([^"]*?)telemetry-v50\.js"></script>')

    for path in public_html_targets():
        text = path.read_text(encoding="utf-8")
        telemetry_matches = list(telemetry_pattern.finditer(text))
        adapter_count = text.count(ANALYTICS_SCRIPT)
        if not telemetry_matches:
            if adapter_count:
                raise RuntimeError(f"{path.relative_to(ROOT)}: adapter v6.1 no debe existir sin telemetría v5.0")
            untouched += 1
            continue
        if len(telemetry_matches) != 1:
            raise RuntimeError(f"{path.relative_to(ROOT)}: se esperaba una única telemetría v5.0")

        text = adapter_pattern.sub("", text)
        telemetry_match = telemetry_pattern.search(text)
        if not telemetry_match:
            raise RuntimeError(f"{path.relative_to(ROOT)}: telemetría desapareció durante normalización")
        prefix = telemetry_match.group(1)
        telemetry_tag = telemetry_match.group(0)
        adapter_tag = f'<script defer src="{prefix}{ANALYTICS_SCRIPT}"></script>'
        text = text[:telemetry_match.start()] + adapter_tag + "\n  " + telemetry_tag + text[telemetry_match.end():]

        if text.count(ANALYTICS_SCRIPT) != 1 or text.count(TELEMETRY_SCRIPT) != 1:
            raise RuntimeError(f"{path.relative_to(ROOT)}: runtime de medición v6.1 debe permanecer único")
        if text.find(ANALYTICS_SCRIPT) > text.find(TELEMETRY_SCRIPT):
            raise RuntimeError(f"{path.relative_to(ROOT)}: adapter v6.1 debe cargar antes de telemetría")
        path.write_text(text, encoding="utf-8")
        instrumented += 1

    if instrumented != EXPECTED_INSTRUMENTED or untouched != EXPECTED_UNTOUCHED:
        raise RuntimeError(
            "Measurement v6.1: topología inesperada; "
            f"esperaba {EXPECTED_INSTRUMENTED}/{EXPECTED_UNTOUCHED} y obtuvo {instrumented}/{untouched}"
        )
    return instrumented, untouched


def validate_measurement_readiness() -> None:
    validator = ROOT / "scripts" / "validate_measurement_readiness_v61.py"
    if not validator.exists():
        raise RuntimeError("Measurement v6.1: falta validator de readiness")
    completed = subprocess.run(
        [sys.executable, str(validator)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if completed.stdout:
        print(completed.stdout.rstrip())
    if completed.returncode:
        detail = completed.stderr.strip() or "validator terminó sin detalle"
        raise RuntimeError(f"Measurement v6.1 inválido: {detail}")


def main() -> int:
    normalize_home_trust()
    normalize_solution_labels()
    instrumented, untouched = normalize_measurement_runtime()
    validate_measurement_readiness()
    print(
        "EXPERIENCE V6 COMPAT OK: confianza v5.29, contacto v5.28, capability truth y anclas v5.31 "
        f"preservados; measurement readiness v6.1 en {instrumented} superficies, {untouched} sin telemetría previa."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

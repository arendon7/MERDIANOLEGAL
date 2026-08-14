#!/usr/bin/env python3
"""Valida v5.28: contacto adelantado, único y sin pérdida de profundidad comercial."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
CSS = ROOT / "conversion-path-v528.css"
VERSION = ROOT / "version.json"


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"CONVERSION PATH V5.28 FAIL: {message}")


def main() -> int:
    version = json.loads(VERSION.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 28, 0):
        print("CONVERSION PATH V5.28 SKIP: version anterior a 5.28.0")
        return 0

    text = HOME.read_text(encoding="utf-8")
    css = CSS.read_text(encoding="utf-8")

    require(text.count('<link rel="stylesheet" href="conversion-path-v528.css">') == 1, "CSS v5.28 debe cargarse exactamente una vez")
    require(text.count('data-conversion-path-v528="true"') == 1, "debe existir una sola sección de contacto v5.28")
    require(text.count('data-conversion-readiness-v528="true"') == 1, "debe existir una sola franja de preparación")
    require(text.count('data-conversion-depth-v528="true"') == 1, "debe existir una sola navegación de profundidad")
    require(text.count('<form class="contact-form" id="contact-form"') == 1, "debe preservarse un único formulario físico canónico")
    require(text.count('data-contact-synthesis-v523="true"') == 1, "debe preservarse la síntesis v5.23")
    require(text.count('data-contact-process-v523="true"') == 1, "debe preservarse el disclosure de proceso v5.23")
    require('class="contact-prelude"' not in text, "el preámbulo redundante de tres tarjetas debe quedar consolidado")

    focusable_regions = (
        '<div class="contact-readiness-items-v528" tabindex="0" role="region" aria-label="Datos mínimos de la solicitud">',
        '<dl class="qualification-summary-grid-v59 contact-synthesis-grid-v523" tabindex="0" role="region" aria-label="Síntesis de la solicitud">',
        '<dl class="qualification-summary-grid-v59 contact-brief-grid-v523" tabindex="0" role="region" aria-label="Modalidad y estándar de trabajo">',
    )
    for region in focusable_regions:
        require(text.count(region) == 1, f"región desplazable debe ser focable y etiquetada: {region}")

    commercial = text.find('<!-- COMMERCIAL-V43:END -->')
    contact = text.find('id="contacto" data-conversion-path-v528="true"')
    sectors = text.find('id="sectores"')
    perspectives = text.find('id="perspectivas"')
    firm = text.find('id="firma"')
    faq = text.find('id="preguntas"')
    require(min(commercial, contact, sectors, perspectives, firm, faq) >= 0, "faltan anclas materiales de la portada")
    require(commercial < contact < sectors < perspectives < firm < faq, "la secuencia debe ser cierre comercial → contacto → profundidad opcional")

    for anchor in ('href="#sectores"', 'href="#perspectivas"', 'href="#firma"', 'href="#preguntas"'):
        require(anchor in text[text.find('data-conversion-depth-v528="true"'):], f"la navegación posterior debe conservar {anchor}")
    for label in ('Decisión o problema', 'Plazo o urgencia', 'Resultado esperado'):
        require(label in text, f"la franja de preparación pierde: {label}")

    required_css = (
        '.contact-readiness-v528',
        '.contact-readiness-items-v528',
        '.post-contact-depth-v528',
        '.contact-synthesis-grid-v523,.contact-brief-grid-v523',
        'color:#725431',
        'overflow-x:auto',
        'overflow-y:hidden',
        'scroll-snap-type:x proximity',
        '@media(max-width:620px)',
    )
    for marker in required_css:
        require(marker in css, f"CSS v5.28 carece de {marker}")
    for forbidden in ('display:none', 'visibility:hidden', 'content-visibility:hidden'):
        require(forbidden not in css, f"v5.28 no puede ocultar contenido material con {forbidden}")

    print("CONVERSION PATH V5.28 OK: contacto adelantado, un solo formulario, decks focables, contraste reforzado y profundidad preservada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

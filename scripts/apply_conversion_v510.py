#!/usr/bin/env python3
"""Aplica v5.10: intención de cierre, ruta de propuesta y continuidad comercial sin backend."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
PRODUCTS = sorted((ROOT / "productos").glob("*.html"))
SERVICES = sorted((ROOT / "servicios").glob("*.html"))
START = "<!-- CLOSE-V510:START -->"
END = "<!-- CLOSE-V510:END -->"
STYLE = '<link rel="stylesheet" href="conversion-close-v510.css">'
SCRIPT = '<script defer src="conversion-close-v510.js"></script>'


def remove_block(text: str) -> str:
    pattern = (
        r'(?ms)^[ \t]*' + re.escape(START) + r'[ \t]*\r?\n'
        r'.*?'
        r'^[ \t]*' + re.escape(END) + r'[ \t]*(?:\r?\n)?'
    )
    return re.sub(pattern, '', text, count=1)


def close_block() -> str:
    return f'''{START}
<div class="close-path-v510 full" data-close-path-v510="true" aria-labelledby="close-path-v510-title">
  <div class="close-head-v510">
    <div>
      <span class="close-kicker-v510">DE INTERÉS A PROPUESTA</span>
      <h3 id="close-path-v510-title">Sepa qué ocurre antes de que exista una propuesta y qué habilita el inicio.</h3>
      <p>La intención de contratar ayuda a avanzar más rápido, pero una propuesta seria todavía exige confirmar encaje, alcance, disponibilidad, responsabilidades y condiciones de inicio.</p>
    </div>
    <span class="close-route-v510" data-close-route-v510>Ruta de orientación</span>
  </div>
  <div class="close-steps-v510" aria-label="Ruta comercial de cierre">
    <article class="close-step-v510" data-close-step-v510="request" data-state="current"><strong>Solicitud y contexto mínimo</strong><span>Necesidad, decisión, horizonte y resultado esperado sin documentos confidenciales.</span></article>
    <article class="close-step-v510" data-close-step-v510="fit" data-state="next"><strong>Encaje, disponibilidad y alcance</strong><span>Se valida la modalidad correcta, conflictos, perímetro, actores y dependencias antes de cotizar.</span></article>
    <article class="close-step-v510" data-close-step-v510="proposal" data-state="next"><strong>Propuesta verificable</strong><span>Objetivo, entregables, cronograma, honorarios, responsabilidades, supuestos y exclusiones.</span></article>
    <article class="close-step-v510" data-close-step-v510="start" data-state="next"><strong>Aceptación e inicio</strong><span>La relación profesional comienza solo con aceptación expresa y las verificaciones aplicables; después se habilita el canal de trabajo.</span></article>
  </div>
  <div class="proposal-anatomy-v510">
    <strong>Qué debe permitir comparar una propuesta de Meridiano</strong>
    <div class="proposal-anatomy-grid-v510"><span>Objetivo</span><span>Perímetro</span><span>Entregables</span><span>Cronograma</span><span>Honorarios</span><span>Responsabilidades</span><span>Supuestos y exclusiones</span></div>
  </div>
  <div class="close-gate-v510"><strong data-close-gate-title-v510>Objetivo de este punto de entrada</strong><p data-close-gate-copy-v510>Comprender la decisión y determinar la modalidad adecuada antes de estructurar una propuesta.</p></div>
  <p class="close-legal-v510">Un formulario, mensaje o solicitud de propuesta no constituye aceptación del encargo, asesoría jurídica, reserva de disponibilidad ni promesa de resultado. Los documentos confidenciales se comparten únicamente después de habilitar un canal seguro.</p>
</div>
{END}'''


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    text = remove_block(text)
    text = re.sub(r'\sdata-commercial-close-v510="true"', '', text)

    form_marker = '<form class="contact-form" id="contact-form" data-contact-v49="true" data-commercial-intake-v59="true">'
    if form_marker not in text:
        raise RuntimeError("index.html: falta formulario comercial v5.9")
    text = text.replace(
        form_marker,
        '<form class="contact-form" id="contact-form" data-contact-v49="true" data-commercial-intake-v59="true" data-commercial-close-v510="true">',
        1,
    )

    anchor = '<!-- COMMERCIAL-V59-QUALIFICATION:END -->'
    if anchor not in text:
        raise RuntimeError("index.html: falta cierre del bloque v5.9")
    text = text.replace(anchor, anchor + "\n" + close_block(), 1)

    text = re.sub(r'(?m)^[ \t]*' + re.escape(STYLE) + r'[ \t]*(?:\r?\n)?', '', text)
    style_anchor = '<link rel="stylesheet" href="commercial-intake-v59.css">'
    if style_anchor not in text:
        raise RuntimeError("index.html: falta commercial-intake-v59.css")
    text = text.replace(style_anchor, style_anchor + "\n  " + STYLE, 1)

    text = re.sub(r'(?m)^[ \t]*' + re.escape(SCRIPT) + r'[ \t]*(?:\r?\n)?', '', text)
    script_anchor = '<script defer src="telemetry-v50.js"></script>'
    if script_anchor not in text:
        raise RuntimeError("index.html: falta telemetry-v50.js")
    text = text.replace(script_anchor, script_anchor + "\n  " + SCRIPT, 1)

    INDEX.write_text(text, encoding="utf-8")


def patch_detail(path: Path, intent: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<a class="buying-clarity-cta-v58" data-decision-v58-cta="true"(?: data-close-intent-v510="[^"]+")? href="([^"]+)">[^<]*</a>'
    )
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f"{path}: falta CTA v5.8")
    href = re.sub(r'([?&])commercial_intent=[^&#]*&?', lambda m: m.group(1), match.group(1))
    href = href.replace('?&', '?').replace('&&', '&').replace('&#contacto', '#contacto')
    if href.endswith('?'):
        href = href[:-1]
    if '#contacto' not in href:
        raise RuntimeError(f"{path}: CTA v5.8 no apunta a contacto")
    base, fragment = href.split('#', 1)
    separator = '&' if '?' in base else '?'
    href = f"{base}{separator}commercial_intent={intent}#{fragment}"
    replacement = (
        '<a class="buying-clarity-cta-v58" data-decision-v58-cta="true" '
        f'data-close-intent-v510="{intent}" href="{href}">{label}</a>'
    )
    text = pattern.sub(replacement, text, count=1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(PRODUCTS) != 8 or len(SERVICES) != 8:
        raise RuntimeError(f"Se esperaban 8 productos y 8 servicios; hay {len(PRODUCTS)} y {len(SERVICES)}")
    patch_index()
    for path in PRODUCTS:
        patch_detail(path, "proposal", "Solicitar propuesta con este alcance →")
    for path in SERVICES:
        patch_detail(path, "scope", "Definir alcance y propuesta →")
    print("CONVERSION V5.10 OK: intención preservada + ruta de propuesta/cierre + 16 CTA contextuales, sin backend.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

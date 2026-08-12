#!/usr/bin/env python3
"""Aplica v5.9: calificación comercial y brief previo a propuesta sin backend."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
START = "<!-- COMMERCIAL-V59-QUALIFICATION:START -->"
END = "<!-- COMMERCIAL-V59-QUALIFICATION:END -->"
STYLE = '<link rel="stylesheet" href="commercial-intake-v59.css">'
SCRIPT = '<script src="commercial-intake-v59.js"></script>'


def remove_block(text: str) -> str:
    pattern = (
        r'(?ms)^[ \t]*' + re.escape(START) + r'[ \t]*\r?\n'
        r'.*?'
        r'^[ \t]*' + re.escape(END) + r'[ \t]*(?:\r?\n)?'
    )
    return re.sub(pattern, '', text, count=1)


def qualification_block() -> str:
    return f'''{START}
<div class="qualification-v59 full" data-qualification-v59="true" aria-labelledby="qualification-v59-title">
  <div class="qualification-head-v59">
    <div>
      <span class="qualification-kicker-v59">CALIFICACIÓN PARA PROPUESTA</span>
      <h3 id="qualification-v59-title">Tres datos para que la primera conversación avance hacia el siguiente paso correcto.</h3>
      <p>No pedimos documentos ni información confidencial. Solo necesitamos saber en qué momento está la decisión, cuándo espera avanzar y, si ya existe, el rango de inversión previsto.</p>
    </div>
    <div class="qualification-safety-v59"><strong>Privacidad por diseño.</strong> Esta web no almacena estas respuestas. Se incorporan al mensaje únicamente cuando usted decide abrir y enviar la solicitud por WhatsApp.</div>
  </div>
  <div class="qualification-fields-v59">
    <label>Momento de decisión
      <select name="decision_stage" required>
        <option value="">Seleccione</option>
        <option>Quiero recibir una propuesta</option>
        <option>Necesito definir mejor el alcance</option>
        <option>Estoy comparando alternativas</option>
        <option>Estoy explorando la necesidad</option>
      </select>
    </label>
    <label>Horizonte para decidir o iniciar
      <select name="urgency" required>
        <option value="">Seleccione</option>
        <option>Esta semana</option>
        <option>En 2 a 4 semanas</option>
        <option>En 1 a 3 meses</option>
        <option>Sin fecha definida</option>
      </select>
    </label>
    <label class="full">Rango de inversión jurídica previsto <span class="qualification-help-v59">Opcional. Ayuda a proponer una modalidad proporcional al alcance; no determina por sí solo si la solicitud puede ser atendida.</span>
      <select name="budget">
        <option>Por definir</option>
        <option>Hasta $3 millones COP</option>
        <option>$3 a $8 millones COP</option>
        <option>$8 a $20 millones COP</option>
        <option>Más de $20 millones COP</option>
      </select>
    </label>
  </div>
  <div class="qualification-summary-v59" data-qualification-summary-v59="true" role="status" aria-live="polite">
    <strong>Resumen para la conversación comercial</strong>
    <dl class="qualification-summary-grid-v59">
      <div><dt>Contexto identificado</dt><dd data-qualification-context-v59>Necesidad presentada desde la portada</dd></div>
      <div><dt>Necesidad</dt><dd data-qualification-need-v59>Por seleccionar</dd></div>
      <div><dt>Momento de decisión</dt><dd data-qualification-stage-v59>Por seleccionar</dd></div>
      <div><dt>Horizonte</dt><dd data-qualification-urgency-v59>Por seleccionar</dd></div>
      <div><dt>Inversión</dt><dd data-qualification-budget-v59>Por definir</dd></div>
      <div><dt>Siguiente paso sugerido</dt><dd data-qualification-next-step-v59>Orientación inicial</dd></div>
    </dl>
    <div class="qualification-next-v59"><b data-qualification-next-step-v59>Orientación inicial</b><p data-qualification-next-copy-v59>El primer paso es comprender la decisión y determinar si corresponde orientación, diagnóstico, producto, proyecto o plan recurrente.</p></div>
  </div>
  <p class="qualification-legal-v59">La clasificación orienta el proceso comercial. No constituye aceptación del encargo, cotización, asesoría jurídica, reserva de disponibilidad ni promesa de resultado.</p>
</div>
{END}'''


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    text = remove_block(text)
    text = re.sub(r'\sdata-commercial-intake-v59="true"', '', text)

    # v5.9 es una capa intermedia. Debe reconocer el formulario aunque capas
    # posteriores (v5.10+) añadan atributos data-* propios. Normaliza solo sus
    # marcadores y conserva extensiones ajenas para mantener composición e
    # idempotencia en segundas pasadas del builder.
    form_match = re.search(r'<form class="contact-form" id="contact-form"(?P<attrs>[^>]*)>', text)
    if not form_match:
        raise RuntimeError("index.html: falta formulario operativo v4.9")
    attrs = form_match.group("attrs")
    attrs = re.sub(r'\s+data-contact-v49="true"', '', attrs)
    attrs = re.sub(r'\s+data-commercial-intake-v59="true"', '', attrs)
    marker = (
        '<form class="contact-form" id="contact-form" '
        'data-contact-v49="true" data-commercial-intake-v59="true"' + attrs + '>'
    )
    text = text[:form_match.start()] + marker + text[form_match.end():]

    need_pattern = re.compile(r'(<label>Necesidad<select name="need" required>[\s\S]*?</select></label>)')
    text, count = need_pattern.subn(lambda match: match.group(1) + "\n" + qualification_block(), text, count=1)
    if count != 1:
        raise RuntimeError("index.html: no se encontró el selector de necesidad")

    text = re.sub(r'(?m)^[ \t]*' + re.escape(STYLE) + r'[ \t]*(?:\r?\n)?', '', text)
    style_anchor = '<link rel="stylesheet" href="decision-v58.css">'
    if style_anchor not in text:
        raise RuntimeError("index.html: falta decision-v58.css")
    text = text.replace(style_anchor, style_anchor + "\n  " + STYLE, 1)

    text = re.sub(r'(?m)^[ \t]*' + re.escape(SCRIPT) + r'[ \t]*(?:\r?\n)?', '', text)
    script_anchor = '<script src="commercial-conversion-v44.js"></script>'
    if script_anchor not in text:
        raise RuntimeError("index.html: falta commercial-conversion-v44.js")
    text = text.replace(script_anchor, script_anchor + "\n  " + SCRIPT, 1)

    INDEX.write_text(text, encoding="utf-8")


def patch_site_js() -> None:
    text = SITE_JS.read_text(encoding="utf-8")
    labels = (
        "Etapa de decisión:",
        "Horizonte comercial:",
        "Presupuesto orientativo:",
        "Siguiente paso sugerido:",
    )
    for label in labels:
        text = re.sub(r'(?m)^\s*`' + re.escape(label) + r'.*?`,\s*\n', '', text)

    anchor = "      `Necesidad: ${cleanContactValue(data.get('need'), 160)}`,\n"
    if anchor not in text:
        raise RuntimeError("site-v3.js: falta línea de necesidad del handoff")
    addition = (
        anchor
        + "      `Etapa de decisión: ${cleanContactValue(data.get('decision_stage'), 160)}`,\n"
        + "      `Horizonte comercial: ${cleanContactValue(data.get('urgency'), 160)}`,\n"
        + "      `Presupuesto orientativo: ${cleanContactValue(data.get('budget'), 160) || 'Por definir'}`,\n"
        + "      `Siguiente paso sugerido: ${cleanContactValue(form.dataset.proposalNextStep, 120) || 'Orientación inicial'}`,\n"
    )
    text = text.replace(anchor, addition, 1)

    old_event = "window.dispatchEvent(new CustomEvent('meridiano:lead-prepared', { detail: { reference, need: cleanContactValue(data.get('need'), 160), context } }));"
    new_event = "window.dispatchEvent(new CustomEvent('meridiano:lead-prepared', { detail: { reference, need: cleanContactValue(data.get('need'), 160), context, readiness: cleanContactValue(form.dataset.proposalReadiness, 32) } }));"
    if old_event in text:
        text = text.replace(old_event, new_event, 1)
    elif new_event not in text:
        raise RuntimeError("site-v3.js: falta evento lead-prepared esperado")

    SITE_JS.write_text(text, encoding="utf-8")


def main() -> int:
    patch_index()
    patch_site_js()
    print("COMMERCIAL V5.9 OK: intake de decisión, horizonte e inversión + brief previo a propuesta, sin persistencia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

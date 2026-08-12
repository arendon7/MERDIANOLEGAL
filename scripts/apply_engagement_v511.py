#!/usr/bin/env python3
"""Aplica v5.11: diferencia propuesta, aceptación e inicio del encargo."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
START = "<!-- ENGAGEMENT-V511:START -->"
END = "<!-- ENGAGEMENT-V511:END -->"
STYLE = '<link rel="stylesheet" href="engagement-v511.css">'


def remove_block(text: str) -> str:
    pattern = r'(?ms)^[ \t]*' + re.escape(START) + r'[ \t]*\r?\n.*?^[ \t]*' + re.escape(END) + r'[ \t]*(?:\r?\n)?'
    return re.sub(pattern, '', text, count=1)


def block() -> str:
    return f'''{START}
<div class="engagement-v511 full" data-engagement-v511="true" aria-labelledby="engagement-v511-title">
  <div class="engagement-head-v511">
    <div>
      <span class="engagement-kicker-v511">DESPUÉS DE LA PROPUESTA</span>
      <h3 id="engagement-v511-title">Propuesta preparada, propuesta aceptada y encargo iniciado son estados distintos.</h3>
      <p>La claridad también importa después de cotizar. Meridiano distingue la solicitud comercial, la propuesta emitida, la aceptación expresa y el momento en que quedan cumplidas las condiciones necesarias para comenzar el trabajo.</p>
    </div>
    <div class="engagement-principle-v511"><strong>Regla de inicio.</strong> El inicio operativo se confirma conforme a la propuesta y a sus condiciones aplicables; nunca se presume por completar este formulario, abrir WhatsApp o visitar una página.</div>
  </div>
  <div class="engagement-states-v511" aria-label="Estados previos al inicio del encargo">
    <article class="engagement-state-v511" data-engagement-state-v511="request"><b>Estado 01</b><strong>Solicitud preparada</strong><p>El cliente comparte contexto mínimo y decide si envía el mensaje por WhatsApp.</p><em>No equivale a propuesta, asesoría ni contratación.</em></article>
    <article class="engagement-state-v511" data-engagement-state-v511="proposal"><b>Estado 02</b><strong>Propuesta emitida</strong><p>Se presenta un alcance verificable con entregables, cronograma, honorarios, responsabilidades, supuestos y exclusiones.</p><em>No equivale por sí sola a aceptación.</em></article>
    <article class="engagement-state-v511" data-engagement-state-v511="accepted"><b>Estado 03</b><strong>Propuesta aceptada</strong><p>Existe aceptación expresa conforme al mecanismo y a las condiciones indicadas en la propia propuesta.</p><em>Su efecto se interpreta según esos términos y verificaciones aplicables.</em></article>
    <article class="engagement-state-v511" data-engagement-state-v511="started"><b>Estado 04</b><strong>Encargo iniciado</strong><p>Se confirman las condiciones de inicio, responsables, canal de trabajo e información inicial necesaria.</p><em>Desde aquí puede comenzar la ejecución del alcance acordado.</em></article>
  </div>
  <div class="engagement-ready-v511">
    <div><strong>Qué se confirma antes del inicio operativo</strong><p>La profundidad exacta depende del asunto y de la propuesta. Estas verificaciones no se sustituyen con un clic público.</p></div>
    <ul class="engagement-checks-v511">
      <li>Partes relevantes y posibles conflictos, cuando corresponda.</li>
      <li>Alcance, entregables, exclusiones y responsables.</li>
      <li>Honorarios, gastos, facturación y demás condiciones económicas aplicables.</li>
      <li>Fecha o condición de inicio y prioridades iniciales.</li>
      <li>Interlocutores autorizados y reglas de coordinación.</li>
      <li>Canal adecuado para información y documentos confidenciales.</li>
    </ul>
  </div>
  <div class="engagement-noauto-v511" data-engagement-automatic-v511="false">
    <strong>Esta web pública no ejecuta automáticamente estos actos</strong>
    <div class="engagement-noauto-grid-v511"><span>No acepta contratos</span><span>No cobra pagos</span><span>No reserva agenda</span><span>No crea un expediente</span><span>No habilita carga documental</span><span>No inicia el encargo</span></div>
  </div>
  <p class="engagement-legal-v511">La aceptación y el inicio se rigen por la propuesta, sus condiciones y las verificaciones aplicables al asunto. Cualquier canal seguro, intercambio documental o mecanismo posterior se habilita fuera de este formulario público.</p>
</div>
{END}'''


def main() -> int:
    text = INDEX.read_text(encoding="utf-8")
    text = remove_block(text)
    anchor = "<!-- CLOSE-V510:END -->"
    if anchor not in text:
        raise RuntimeError("index.html: falta cierre de la arquitectura v5.10")
    text = text.replace(anchor, anchor + "\n" + block(), 1)
    text = re.sub(r'(?m)^[ \t]*' + re.escape(STYLE) + r'[ \t]*(?:\r?\n)?', '', text)
    style_anchor = '<link rel="stylesheet" href="conversion-close-v510.css">'
    if style_anchor not in text:
        raise RuntimeError("index.html: falta conversion-close-v510.css")
    text = text.replace(style_anchor, style_anchor + "\n  " + STYLE, 1)
    INDEX.write_text(text, encoding="utf-8")
    print("ENGAGEMENT V5.11 OK: estados de propuesta, aceptación e inicio aplicados sin backend.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

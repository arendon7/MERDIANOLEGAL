#!/usr/bin/env python3
"""v5.23: comprime el tramo final de contacto sin alterar la lógica comercial histórica."""
from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import sys

R = Path(__file__).resolve().parents[1]
HOME = R / "index.html"
VERSION_PATH = R / "version.json"

SYN_START = "<!-- CONTACT-SYNTHESIS-V523:START -->"
SYN_END = "<!-- CONTACT-SYNTHESIS-V523:END -->"
PROCESS_START = "<!-- CONTACT-PROCESS-V523:START -->"
PROCESS_END = "<!-- CONTACT-PROCESS-V523:END -->"

V59_START = "<!-- COMMERCIAL-V59-QUALIFICATION:START -->"
V59_END = "<!-- COMMERCIAL-V59-QUALIFICATION:END -->"
V513_START = "<!-- COMMERCIAL-BRIEF-V513:START -->"
V513_END = "<!-- COMMERCIAL-BRIEF-V513:END -->"
V514_START = "<!-- RECOMMENDATION-V514-FORM:START -->"
V514_END = "<!-- RECOMMENDATION-V514-FORM:END -->"
V510_START = "<!-- CLOSE-V510:START -->"
V510_END = "<!-- CLOSE-V510:END -->"
V511_START = "<!-- ENGAGEMENT-V511:START -->"
V511_END = "<!-- ENGAGEMENT-V511:END -->"


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def managed_pattern(start: str, end: str) -> re.Pattern[str]:
    return re.compile(r"\s*" + re.escape(start) + r".*?" + re.escape(end) + r"\s*", re.S)


def remove_managed(text: str, start: str, end: str) -> str:
    return managed_pattern(start, end).sub("\n", text, count=1)


def block(text: str, start: str, end: str, label: str) -> str:
    a = text.find(start)
    b = text.find(end, a + len(start)) if a >= 0 else -1
    if a < 0 or b < 0:
        raise RuntimeError(f"index.html: falta bloque {label}")
    return text[a : b + len(end)]


def remove_exact_once(text: str, fragment: str, label: str) -> str:
    if text.count(fragment) != 1:
        raise RuntimeError(f"index.html: {label} debe existir exactamente una vez")
    return text.replace(fragment, "", 1)


def qualification_without_summary(v59: str) -> str:
    summary_start = v59.find('<div class="qualification-summary-v59"')
    legal_start = v59.find('  <p class="qualification-legal-v59">', summary_start)
    if summary_start < 0 or legal_start < 0:
        raise RuntimeError("index.html: v5.9 no contiene resumen/legal canónicos")
    compact = v59[:summary_start] + v59[legal_start:]
    if 'data-qualification-summary-v59="true"' in compact:
        raise RuntimeError("index.html: resumen v5.9 no pudo extraerse del bloque de campos")
    return compact


def synthesis_markup() -> str:
    return f'''{SYN_START}
<section class="contact-synthesis-v523 full" data-contact-synthesis-v523="true" aria-labelledby="contact-synthesis-v523-title">
  <div class="contact-synthesis-head-v523">
    <div><span>SÍNTESIS PARA AVANZAR</span><h3 id="contact-synthesis-v523-title">Una sola lectura de su necesidad, la modalidad y el siguiente paso.</h3></div>
    <p>La web organiza el contexto que usted ya indicó. No asigna puntajes, no decide por usted y no convierte esta solicitud en asesoría, propuesta o encargo.</p>
  </div>
  <div class="qualification-summary-v59 contact-qualification-v523" data-qualification-summary-v59="true" role="status" aria-live="polite">
    <dl class="qualification-summary-grid-v59 contact-synthesis-grid-v523">
      <div><dt>Contexto</dt><dd data-qualification-context-v59>Necesidad presentada desde la portada</dd></div>
      <div><dt>Necesidad</dt><dd data-qualification-need-v59>Por seleccionar</dd></div>
      <div><dt>Momento</dt><dd data-qualification-stage-v59>Por seleccionar</dd></div>
      <div><dt>Horizonte</dt><dd data-qualification-urgency-v59>Por seleccionar</dd></div>
      <div><dt>Inversión</dt><dd data-qualification-budget-v59>Por definir</dd></div>
    </dl>
    <div class="qualification-next-v59 contact-next-v523"><span>SIGUIENTE PASO</span><b data-qualification-next-step-v59>Orientación inicial</b><p data-qualification-next-copy-v59>El primer paso es comprender la decisión y determinar si corresponde orientación, diagnóstico, producto, proyecto o plan recurrente.</p></div>
  </div>
{V513_START}
  <div class="commercial-brief-v513 contact-brief-v523" data-commercial-brief-v513="true" aria-labelledby="commercial-brief-v513-title">
    <div class="contact-brief-head-v523"><span id="commercial-brief-v513-title">Modalidad y estándar de trabajo</span><b class="commercial-brief-badge-v513" data-brief-status-v513>Contexto por completar</b></div>
    <dl class="commercial-brief-grid-v513 contact-brief-grid-v523">
      <div><dt>Modalidad considerada</dt><dd data-brief-modality-v513>Por confirmar según el alcance</dd></div>
      <div><dt>Estándar verificable</dt><dd data-brief-proof-v513>Se definirá en la propuesta aplicable</dd></div>
    </dl>
    <p class="commercial-brief-note-v513">Estas categorías orientan la conversación y no constituyen una propuesta, aceptación del encargo ni garantía de que la modalidad inicialmente considerada sea la definitiva.</p>
  </div>
{V513_END}
{V514_START}
  <div class="recommendation-brief-v514 decision-route-v515 contact-recommendation-v523" data-recommendation-brief-v514="true" data-decision-route-v515="true" aria-labelledby="recommendation-brief-v514-title">
    <span id="recommendation-brief-v514-title">CRITERIO PARA AVANZAR</span>
    <p class="decision-fit-v515"><strong>Por qué podría encajar</strong><span data-recommendation-fit-v514>Por confirmar: primero debe entenderse la necesidad y el resultado esperado.</span></p>
    <div class="decision-route-panel-v515" data-route-panel-v515="true">
      <div><span data-route-source-v515>Contexto aún abierto</span><strong data-route-label-v515>Orientación inicial</strong><p data-route-copy-v515>Comprender primero la decisión y confirmar qué modalidad merece avanzar.</p></div>
      <button type="button" data-apply-route-v515>Usar orientación inicial</button>
    </div>
    <details class="recommendation-details-v515" data-recommendation-details-v515="true">
      <summary>Ver límite y alternativa de la modalidad</summary>
      <dl class="recommendation-brief-grid-v514">
        <div><dt>Límite</dt><dd data-recommendation-boundary-v514>No se recomienda una modalidad sin contexto suficiente.</dd></div>
        <div><dt>Alternativa si…</dt><dd data-recommendation-alternative-v514>El siguiente paso es delimitar la necesidad antes de comparar modalidades.</dd></div>
      </dl>
    </details>
    <p class="recommendation-brief-state-v514" data-recommendation-state-v514>Sin modalidad preseleccionada. La web no asigna puntajes ni presume una recomendación.</p>
  </div>
{V514_END}
</section>
{SYN_END}'''


def process_markup(close: str, engagement: str) -> str:
    return f'''{PROCESS_START}
<details class="contact-process-v523 commercial-disclosure-v516 commercial-disclosure-v519 full" data-contact-process-v523="true" data-mobile-disclosure-v516="contact-process" data-commercial-disclosure-v519="contact-process" data-default-state-v519="collapsed-secondary" data-default-state-v523="collapsed-secondary">
  <summary><strong>Ver proceso, límites y condiciones de inicio</strong><span>Ruta a propuesta, contenido mínimo de la propuesta, aceptación, verificaciones previas y actos que esta web no ejecuta.</span></summary>
  <div class="contact-process-body-v523">
{close}
{engagement}
  </div>
</details>
{PROCESS_END}'''


def normalize_form_marker(text: str) -> str:
    match = re.search(r'<form class="contact-form" id="contact-form"(?P<attrs>[^>]*)>', text)
    if not match:
        raise RuntimeError("index.html: falta formulario canónico")
    attrs = re.sub(r'\s+data-contact-compression-v523="true"', "", match.group("attrs"))
    replacement = '<form class="contact-form" id="contact-form" data-contact-compression-v523="true"' + attrs + '>'
    return text[: match.start()] + replacement + text[match.end() :]


def patch_home() -> None:
    text = HOME.read_text(encoding="utf-8")

    # En segunda pasada los aplicadores históricos pueden haber vaciado o dejado
    # incompletos los wrappers v5.23. Se eliminan primero y se reconstruye siempre
    # desde los bloques históricos recién materializados.
    text = remove_managed(text, SYN_START, SYN_END)
    text = remove_managed(text, PROCESS_START, PROCESS_END)

    v59 = block(text, V59_START, V59_END, "v5.9")
    v513 = block(text, V513_START, V513_END, "v5.13")
    v514 = block(text, V514_START, V514_END, "v5.14 form")
    v510 = block(text, V510_START, V510_END, "v5.10")
    v511 = block(text, V511_START, V511_END, "v5.11")

    compact_v59 = qualification_without_summary(v59)
    for fragment, label in ((v59, "v5.9"), (v513, "v5.13"), (v514, "v5.14"), (v510, "v5.10"), (v511, "v5.11")):
        text = remove_exact_once(text, fragment, label)

    combined = compact_v59 + "\n" + synthesis_markup() + "\n" + process_markup(v510, v511)
    need = re.search(r'(<label>Necesidad<select name="need" required>[\s\S]*?</select></label>)', text)
    if not need:
        raise RuntimeError("index.html: falta selector de necesidad para insertar v5.23")
    text = text[: need.end()] + "\n" + combined + text[need.end() :]
    text = normalize_form_marker(text)

    if text.count('data-contact-synthesis-v523="true"') != 1 or text.count('data-contact-process-v523="true"') != 1:
        raise RuntimeError("index.html: v5.23 debe materializar una síntesis y un disclosure")
    HOME.write_text(text, encoding="utf-8")


def validate_materialized_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(R / "scripts/validate_contact_compression_v523.py")],
        cwd=R,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"v5.23 no supera validator de contacto: {detail}")
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    version = json.loads(VERSION_PATH.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 23, 0):
        return 0
    patch_home()
    validate_materialized_contract()
    print("CONTACT COMPRESSION V5.23 OK: una síntesis comercial + un disclosure de proceso, con lógica histórica intacta.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

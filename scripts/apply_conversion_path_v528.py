#!/usr/bin/env python3
"""v5.28: acerca el contacto al cierre comercial y conserva la profundidad opcional."""
from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
VERSION_PATH = ROOT / "version.json"
CSS_LINK = '<link rel="stylesheet" href="conversion-path-v528.css">'
CSS_ANCHOR = '<link rel="stylesheet" href="integral-v526.css">'
COMMERCIAL_END = '<!-- COMMERCIAL-V43:END -->'
READINESS_START = '<!-- CONVERSION-READINESS-V528:START -->'
READINESS_END = '<!-- CONVERSION-READINESS-V528:END -->'
DEPTH_START = '<!-- CONVERSION-DEPTH-V528:START -->'
DEPTH_END = '<!-- CONVERSION-DEPTH-V528:END -->'
SYNTHESIS_DECK = '<dl class="qualification-summary-grid-v59 contact-synthesis-grid-v523" tabindex="0" role="region" aria-label="Síntesis de la solicitud">'
BRIEF_DECK = '<dl class="qualification-summary-grid-v59 contact-brief-grid-v523" tabindex="0" role="region" aria-label="Modalidad y estándar de trabajo">'


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def remove_managed(text: str, start: str, end: str) -> str:
    pattern = re.compile(r"\s*" + re.escape(start) + r".*?" + re.escape(end) + r"\s*", re.S)
    return pattern.sub("\n", text)


def extract_contact_section(text: str) -> tuple[int, int, str]:
    start_match = re.search(r'<section class="section contact-section" id="contacto"[^>]*>', text)
    if not start_match:
        raise RuntimeError("index.html: falta la sección canónica #contacto")
    token_re = re.compile(r"<section\b[^>]*>|</section>", re.I)
    depth = 0
    for token in token_re.finditer(text, start_match.start()):
        raw = token.group(0).lower()
        if raw.startswith("<section"):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return start_match.start(), token.end(), text[start_match.start() : token.end()]
    raise RuntimeError("index.html: no fue posible cerrar la sección #contacto")


def readiness_markup() -> str:
    return f'''{READINESS_START}
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


def depth_markup() -> str:
    return f'''{DEPTH_START}
<nav class="post-contact-depth-v528" data-conversion-depth-v528="true" aria-label="Profundizar antes de decidir">
  <div class="container post-contact-depth-inner-v528">
    <div class="post-contact-depth-copy-v528"><span>¿PREFIERE PROFUNDIZAR?</span><strong>La evidencia y el contexto de la firma siguen disponibles después del punto de contacto.</strong></div>
    <div class="post-contact-depth-links-v528">
      <a href="#sectores">Sectores</a>
      <a href="#perspectivas">Perspectivas</a>
      <a href="#firma">Firma y trayectoria</a>
      <a href="#preguntas">Preguntas frecuentes</a>
    </div>
  </div>
</nav>
{DEPTH_END}'''


def normalize_focusable_decks(block: str) -> str:
    block = re.sub(
        r'<dl class="qualification-summary-grid-v59 contact-synthesis-grid-v523"[^>]*>',
        SYNTHESIS_DECK,
        block,
        count=1,
    )
    block = re.sub(
        r'<dl class="qualification-summary-grid-v59 contact-brief-grid-v523"[^>]*>',
        BRIEF_DECK,
        block,
        count=1,
    )
    if block.count(SYNTHESIS_DECK) != 1 or block.count(BRIEF_DECK) != 1:
        raise RuntimeError("index.html: no fue posible normalizar accesibilidad de los decks v5.28")
    return block


def normalize_contact_block(block: str) -> str:
    block = remove_managed(block, READINESS_START, READINESS_END)
    block = re.sub(r'<div class="contact-prelude">.*?</div>', "", block, count=1, flags=re.S)
    block = re.sub(
        r'<section class="section contact-section" id="contacto"[^>]*>',
        '<section class="section contact-section" id="contacto" data-conversion-path-v528="true">',
        block,
        count=1,
    )
    block = normalize_focusable_decks(block)
    anchor = '<section class="section contact-section" id="contacto" data-conversion-path-v528="true"><div class="container">'
    if anchor not in block:
        raise RuntimeError("index.html: no se reconoce el contenedor de #contacto para v5.28")
    block = block.replace(anchor, anchor + "\n" + readiness_markup() + "\n", 1)
    return block


def normalize_css_link(text: str) -> str:
    text = re.sub(r'(?m)^\s*' + re.escape(CSS_LINK) + r'\s*(?:\r?\n)?', "", text)
    if CSS_ANCHOR not in text:
        raise RuntimeError("index.html: falta integral-v526.css para insertar v5.28")
    return text.replace(CSS_ANCHOR, CSS_ANCHOR + "\n  " + CSS_LINK, 1)


def normalize_layout_whitespace(text: str) -> str:
    """Fija separadores que generadores históricos pueden variar entre pasadas."""
    text = re.sub(
        r'(<link rel="stylesheet" href="commercial-v43\.css">)\s*'
        r'(<link rel="stylesheet" href="visual-v39\.css">)',
        r'\1\n\n  \2',
        text,
        count=1,
    )
    text = re.sub(
        re.escape(READINESS_END) + r'\s*<div class="contact-layout">',
        READINESS_END + '\n<div class="contact-layout">',
        text,
        count=1,
    )
    text = re.sub(r'\n[ \t]*\n[ \t]*\n  </main>', '\n\n  </main>', text, count=1)
    return text


def patch_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    text = remove_managed(text, DEPTH_START, DEPTH_END)
    start, end, contact = extract_contact_section(text)
    contact = normalize_contact_block(contact)
    text = text[:start] + text[end:]
    if text.count(COMMERCIAL_END) != 1:
        raise RuntimeError("index.html: el cierre comercial v4.3 debe existir exactamente una vez")
    insertion = COMMERCIAL_END + "\n\n" + contact + "\n" + depth_markup()
    text = text.replace(COMMERCIAL_END, insertion, 1)
    text = normalize_css_link(text)
    text = normalize_layout_whitespace(text)

    if text.count('data-conversion-path-v528="true"') != 1:
        raise RuntimeError("index.html: v5.28 debe marcar una sola sección de contacto")
    if text.count('data-conversion-readiness-v528="true"') != 1:
        raise RuntimeError("index.html: v5.28 debe materializar una sola franja de preparación")
    if text.count('data-conversion-depth-v528="true"') != 1:
        raise RuntimeError("index.html: v5.28 debe materializar una sola navegación de profundidad")
    HOME.write_text(text, encoding="utf-8")


def validate_materialized_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_conversion_path_v528.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"v5.28 no supera validator de ruta de conversión: {detail}")
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    version = json.loads(VERSION_PATH.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 28, 0):
        return 0
    patch_home()
    validate_materialized_contract()
    print("CONVERSION PATH V5.28 OK: contacto adelantado, preparación compacta, decks accesibles y profundidad preservada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

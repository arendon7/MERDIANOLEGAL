#!/usr/bin/env python3
"""Aplica v5.14: recomendación de modalidad explicable, sin puntajes ni persistencia."""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
CONTRACT = ROOT / "recommendation-v514.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
HOME_START = "<!-- RECOMMENDATION-V514-HOME:START -->"
HOME_END = "<!-- RECOMMENDATION-V514-HOME:END -->"
FORM_START = "<!-- RECOMMENDATION-V514-FORM:START -->"
FORM_END = "<!-- RECOMMENDATION-V514-FORM:END -->"
JS_START = "    // RECOMMENDATION-V514:START"
JS_END = "    // RECOMMENDATION-V514:END"
STYLE = '<link rel="stylesheet" href="recommendation-v514.css">'
SCRIPT = '<script src="recommendation-v514.js"></script>'
PROOF_STANDARD = "Método + entregables + formatos + aceptación/cierre"


def remove_block(text: str, start: str, end: str) -> str:
    pattern = r'(?ms)^[ \t]*' + re.escape(start) + r'[ \t]*\r?\n.*?^[ \t]*' + re.escape(end) + r'[ \t]*(?:\r?\n)?'
    return re.sub(pattern, "", text, count=1)


def ensure_head_item(text: str, item: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(item) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("index.html sin </head>")
    return text.replace("</head>", f"  {item}\n</head>", 1)


def load_contract() -> dict:
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    modalities = payload.get("modalities") or {}
    if payload.get("scoring") is not False or len(modalities) != 5:
        raise RuntimeError("recommendation-v514.json debe declarar scoring=false y cinco modalidades")
    required = {"label", "fit", "boundary", "alternative", "href", "cta"}
    for code, rule in modalities.items():
        if not required.issubset(rule):
            raise RuntimeError(f"Modalidad {code} incompleta")
    return payload


def home_block(contract: dict) -> str:
    cards = []
    for idx, (code, rule) in enumerate(contract["modalities"].items(), start=1):
        cards.append(
            f'<article class="recommendation-card-v514" data-recommendation-model-v514="{escape(code)}">'
            f'<span>{idx:02d} · {escape(rule["label"])}</span><h3>{escape(rule["label"])}</h3>'
            '<dl>'
            f'<div><dt>Por qué encaja</dt><dd>{escape(rule["fit"])}</dd></div>'
            f'<div><dt>Límite</dt><dd>{escape(rule["boundary"])}</dd></div>'
            f'<div><dt>Alternativa si…</dt><dd>{escape(rule["alternative"])}</dd></div>'
            '</dl>'
            f'<a href="{escape(rule["href"], quote=True)}">{escape(rule["cta"])} →</a>'
            '</article>'
        )
    contract_json = json.dumps(contract, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'''{HOME_START}
<section class="recommendation-v514" data-recommendation-v514="true" aria-labelledby="recommendation-v514-title">
  <div class="container">
    <div class="section-heading"><p class="eyebrow dark">RECOMENDACIÓN EXPLICABLE</p><h2 id="recommendation-v514-title">No basta con nombrar una modalidad: debe poder entender por qué encaja y cuándo dejaría de encajar.</h2><p>Esta comparación no asigna puntajes ni decide por usted. Expone una regla comprensible para contrastar la forma de trabajo con el tipo de incertidumbre y alcance.</p></div>
    <div class="recommendation-grid-v514">{''.join(cards)}</div>
    <p class="recommendation-note-v514"><strong>Regla de decisión:</strong> la modalidad mostrada es orientativa hasta validar hechos, perímetro, dependencias, disponibilidad y posibles conflictos. Si esas condiciones cambian, también puede cambiar la modalidad más adecuada.</p>
  </div>
</section>
<script type="application/json" id="recommendation-contract-v514">{contract_json}</script>
{HOME_END}'''


def form_block() -> str:
    return f'''{FORM_START}
<div class="recommendation-brief-v514 full" data-recommendation-brief-v514="true" aria-labelledby="recommendation-brief-v514-title">
  <span>POR QUÉ ESTA MODALIDAD PODRÍA ENCAJAR</span>
  <h3 id="recommendation-brief-v514-title">Criterio visible, sin puntaje opaco.</h3>
  <p>Si llegó desde una ficha con modalidad identificada, esta explicación acompaña el brief. Si no existe contexto suficiente, la web no inventa una recomendación.</p>
  <dl class="recommendation-brief-grid-v514">
    <div><dt>Por qué encaja</dt><dd data-recommendation-fit-v514>Por confirmar: primero debe entenderse la necesidad y el resultado esperado.</dd></div>
    <div><dt>Límite</dt><dd data-recommendation-boundary-v514>No se recomienda una modalidad sin contexto suficiente.</dd></div>
    <div><dt>Alternativa si…</dt><dd data-recommendation-alternative-v514>El siguiente paso es delimitar la necesidad antes de comparar modalidades.</dd></div>
  </dl>
  <p class="recommendation-brief-state-v514" data-recommendation-state-v514>Sin modalidad preseleccionada. La web no asigna puntajes ni presume una recomendación.</p>
</div>
{FORM_END}'''


def patch_home(contract: dict) -> None:
    text = HOME.read_text(encoding="utf-8")
    text = remove_block(text, HOME_START, HOME_END)
    text = remove_block(text, FORM_START, FORM_END)
    proof_anchor = "<!-- PROOF-V512-HOME:END -->"
    if proof_anchor not in text:
        raise RuntimeError("index.html: falta cierre v5.12")
    text = text.replace(proof_anchor, proof_anchor + "\n" + home_block(contract), 1)
    brief_anchor = "<!-- COMMERCIAL-BRIEF-V513:END -->"
    if brief_anchor not in text:
        raise RuntimeError("index.html: falta cierre v5.13")
    text = text.replace(brief_anchor, brief_anchor + "\n" + form_block(), 1)
    text = ensure_head_item(text, STYLE)
    text = re.sub(r'(?m)^[ \t]*' + re.escape(SCRIPT) + r'[ \t]*(?:\r?\n)?', "", text)
    script_anchor = '  <script src="commercial-brief-v513.js"></script>'
    if script_anchor not in text:
        raise RuntimeError("index.html: falta script v5.13")
    text = text.replace(script_anchor, script_anchor + "\n  " + SCRIPT, 1)
    HOME.write_text(text, encoding="utf-8")


def patch_site_js() -> None:
    text = SITE_JS.read_text(encoding="utf-8")
    text = remove_block(text, JS_START, JS_END)
    anchor = "    if (context) lines.push(`Contexto comercial: ${context}`);"
    if anchor not in text:
        raise RuntimeError("site-v3.js: falta ancla de contexto")
    block = f'''{JS_START}
    const recommendationFitV514 = cleanContactValue(form.dataset.recommendationFitV514 || '', 420);
    const recommendationBoundaryV514 = cleanContactValue(form.dataset.recommendationBoundaryV514 || '', 420);
    const recommendationAlternativeV514 = cleanContactValue(form.dataset.recommendationAlternativeV514 || '', 420);
    if (recommendationFitV514) lines.push(`Por qué encaja la modalidad: ${{recommendationFitV514}}`);
    if (recommendationBoundaryV514) lines.push(`Límite de la modalidad: ${{recommendationBoundaryV514}}`);
    if (recommendationAlternativeV514) lines.push(`Alternativa si cambia el alcance: ${{recommendationAlternativeV514}}`);
{JS_END}
'''
    text = text.replace(anchor, block + anchor, 1)
    SITE_JS.write_text(text, encoding="utf-8")


def modality_from_detail(text: str) -> str:
    match = re.search(r'<section class="proof-detail-v512"[^>]*data-commercial-modality-v513="([^"]+)"[^>]*>', text)
    if not match:
        raise RuntimeError("ficha sin modalidad v5.13")
    return match.group(1)


def existing_direct_context(href: str) -> tuple[str, str]:
    parts = urlsplit(unescape(href))
    message = unquote(parse_qs(parts.query).get("text", [""])[0])
    title_match = re.search(r'^Hola, revisé la ficha de (.+?) en Meridiano Legal', message)
    if not title_match:
        raise RuntimeError("WhatsApp directo v5.13 sin título reconocible")
    return title_match.group(1), parts.netloc


def direct_href(title: str, code: str, contract: dict) -> str:
    rule = contract["modalities"][code]
    message = (
        f"Hola, revisé la ficha de {title} en Meridiano Legal y quiero presentar una necesidad relacionada.\n\n"
        f"Modalidad considerada: {rule['label']}\n"
        f"Estándar verificable: {PROOF_STANDARD}\n"
        f"Por qué encaja la modalidad: {rule['fit']}\n"
        f"Límite de la modalidad: {rule['boundary']}\n"
        f"Alternativa si cambia el alcance: {rule['alternative']}\n\n"
        "Entiendo que la modalidad y el alcance definitivos deben confirmarse antes de una propuesta."
    )
    return "https://wa.me/573008507813?text=" + quote(message, safe="")


def patch_detail(path: Path, contract: dict) -> None:
    text = path.read_text(encoding="utf-8")
    code = modality_from_detail(text)
    if code not in contract["modalities"]:
        raise RuntimeError(f"{path.name}: modalidad v5.13 desconocida {code}")

    desktop = re.search(r'<a class="btn btn-gold" href="(https://wa\.me/573008507813\?text=[^"]+)" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a>', text)
    if not desktop:
        raise RuntimeError(f"{path.name}: WhatsApp directo no encontrado")
    title, _host = existing_direct_context(desktop.group(1))
    href = direct_href(title, code, contract)
    text = text[:desktop.start(1)] + href + text[desktop.end(1):]

    mobile = re.search(r'(<div class="detail-mobile-cta-v46"[^>]*>.*?<a href=")(https://wa\.me/573008507813\?text=[^"]+)(" target="_blank" rel="noopener noreferrer">WhatsApp</a>)', text, flags=re.S)
    if not mobile:
        raise RuntimeError(f"{path.name}: WhatsApp móvil no encontrado")
    text = text[:mobile.start(2)] + href + text[mobile.end(2):]
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(DETAIL_TARGETS) != 16:
        raise RuntimeError(f"Se esperaban 16 fichas profundas y se encontraron {len(DETAIL_TARGETS)}")
    contract = load_contract()
    patch_home(contract)
    patch_site_js()
    for path in DETAIL_TARGETS:
        patch_detail(path, contract)
    print("RECOMMENDATION V5.14 OK: cinco reglas explicables + brief + WhatsApp directo, sin scoring ni storage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

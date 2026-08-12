#!/usr/bin/env python3
"""Aplica v5.15: consolida selector + recomendación y alinea la ruta comercial sin automatismos."""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
from urllib.parse import parse_qs, parse_qsl, quote, urlencode, urlsplit, urlunsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
CONTRACT = ROOT / "recommendation-v514.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
HOME_START = "<!-- RECOMMENDATION-V514-HOME:START -->"
HOME_END = "<!-- RECOMMENDATION-V514-HOME:END -->"
FORM_START = "<!-- RECOMMENDATION-V514-FORM:START -->"
FORM_END = "<!-- RECOMMENDATION-V514-FORM:END -->"
STYLE = '<link rel="stylesheet" href="decision-action-v515.css">'
SCRIPT = '<script src="decision-action-v515.js"></script>'

ROUTE_BY_MODALITY = {
    "diagnostic": "scope",
    "audit": "proposal",
    "product": "proposal",
    "specialist": "scope",
    "recurring": "scope",
}
ROUTE_LABEL = {
    "proposal": "Propuesta verificable",
    "scope": "Definición de alcance",
    "orientation": "Orientación inicial",
}


def load_contract() -> dict:
    payload = json.loads(CONTRACT.read_text(encoding="utf-8"))
    modalities = payload.get("modalities") or {}
    if payload.get("scoring") is not False or tuple(modalities) != ("diagnostic", "audit", "product", "specialist", "recurring"):
        raise RuntimeError("recommendation-v514.json no conserva el contrato canónico de cinco modalidades sin scoring")
    return payload


def ensure_head_item(text: str, item: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(item) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("index.html sin </head>")
    return text.replace("</head>", f"  {item}\n</head>", 1)


def replace_marked(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"No se pudo reemplazar bloque {start}")
    return text


def recommendation_card(code: str, rule: dict, idx: int) -> str:
    return (
        f'<article class="recommendation-card-v514" data-recommendation-model-v514="{escape(code)}">'
        f'<span>{idx:02d} · {escape(rule["label"])}</span><h3>{escape(rule["label"])}</h3>'
        '<dl>'
        f'<div class="recommendation-fit-source-v515"><dt>Por qué encaja</dt><dd>{escape(rule["fit"])}</dd></div>'
        f'<div><dt>Límite</dt><dd>{escape(rule["boundary"])}</dd></div>'
        f'<div><dt>Alternativa si…</dt><dd>{escape(rule["alternative"])}</dd></div>'
        '</dl>'
        f'<a href="{escape(rule["href"], quote=True)}">{escape(rule["cta"])} →</a>'
        '</article>'
    )


def recommendation_home(contract: dict) -> str:
    cards = "".join(recommendation_card(code, rule, idx) for idx, (code, rule) in enumerate(contract["modalities"].items(), start=1))
    return f'''{HOME_START}
<section class="recommendation-v514 decision-action-v515" data-recommendation-v514="true" data-decision-action-v515="true" aria-labelledby="recommendation-v514-title">
  <div class="container">
    <div class="decision-action-head-v515">
      <div class="decision-action-copy-v515"><p class="eyebrow dark">DE RECOMENDACIÓN A ACCIÓN</p><h2 id="recommendation-v514-title">El selector ya explica cuándo encaja cada modalidad; aquí solo necesita confirmar el siguiente paso o contrastar sus límites.</h2><p>Meridiano no asigna puntajes ni decide por usted. La recomendación sigue siendo explicable y puede cambiar cuando cambian hechos, perímetro, dependencias o recurrencia.</p></div>
      <aside class="decision-action-live-v515" data-decision-action-live-v515="true"><span>ACCIÓN CONTEXTUAL</span><strong data-action-label-v515>Elija una modalidad arriba</strong><p data-action-fit-v515>Cada opción reúne encaje y siguiente acción. Use la comparación ampliada solo si necesita contrastar límites y alternativas.</p><a data-action-cta-v515 href="#proof-router-v512-title">Ir al selector →</a></aside>
    </div>
    <details class="recommendation-compare-v515" data-recommendation-compare-v515="true">
      <summary>Comparar límites y alternativas de las cinco modalidades <span>· análisis ampliado</span></summary>
      <div class="recommendation-grid-v514">{cards}</div>
    </details>
    <p class="recommendation-note-v514"><strong>Regla de decisión:</strong> esta comparación no asigna puntajes. La modalidad es orientativa hasta validar hechos, alcance, disponibilidad y posibles conflictos; si esas condiciones cambian, también puede cambiar la ruta adecuada.</p>
  </div>
</section>
{HOME_END}'''


def recommendation_form() -> str:
    return f'''{FORM_START}
<div class="recommendation-brief-v514 decision-route-v515 full" data-recommendation-brief-v514="true" data-decision-route-v515="true" aria-labelledby="recommendation-brief-v514-title">
  <span>RECOMENDACIÓN → SIGUIENTE PASO</span>
  <h3 id="recommendation-brief-v514-title">Una razón visible y una ruta comercial que usted controla.</h3>
  <p>La modalidad considerada orienta el siguiente paso; un punto de entrada explícito siempre tiene prioridad y la web nunca cambia su etapa de decisión automáticamente.</p>
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
{FORM_END}'''


def patch_proof_cards(text: str, contract: dict) -> str:
    for code, rule in contract["modalities"].items():
        pattern = re.compile(r'(<a class="proof-model-card-v512"[^>]*data-proof-model-v512="' + re.escape(code) + r'"[^>]*>)(.*?)(</a>)', re.S)
        match = pattern.search(text)
        if not match:
            raise RuntimeError(f"index.html: falta tarjeta v5.12 {code}")
        opening = re.sub(r'\s+data-decision-action-source-v515="[^"]*"', "", match.group(1))
        opening = opening[:-1] + f' data-decision-action-source-v515="{code}">'
        body = re.sub(r'<em class="proof-fit-v515">.*?</em>', "", match.group(2), flags=re.S)
        fit = f'<em class="proof-fit-v515"><small>Encaja si</small>{escape(rule["fit"])}</em>'
        if "<b>" not in body:
            raise RuntimeError(f"index.html: tarjeta v5.12 {code} sin CTA")
        body = body.replace("<b>", fit + "<b>", 1)
        replacement = opening + body + match.group(3)
        text = text[:match.start()] + replacement + text[match.end():]
    return text


def patch_home(contract: dict) -> None:
    text = HOME.read_text(encoding="utf-8")
    text = patch_proof_cards(text, contract)
    text = replace_marked(text, HOME_START, HOME_END, recommendation_home(contract))
    text = replace_marked(text, FORM_START, FORM_END, recommendation_form())
    text = ensure_head_item(text, STYLE)
    text = re.sub(r'(?m)^[ \t]*' + re.escape(SCRIPT) + r'[ \t]*(?:\r?\n)?', "", text)
    script_anchor = '<script src="recommendation-v514.js"></script>'
    if script_anchor not in text:
        raise RuntimeError("index.html: falta recommendation-v514.js")
    text = text.replace(script_anchor, script_anchor + "\n  " + SCRIPT, 1)
    HOME.write_text(text, encoding="utf-8")


def modality_from_detail(text: str) -> str:
    match = re.search(r'<section class="proof-detail-v512"[^>]*data-commercial-modality-v513="([^"]+)"[^>]*>', text)
    if not match:
        raise RuntimeError("ficha sin modalidad v5.13")
    return match.group(1)


def with_query_param(href: str, key: str, value: str) -> str:
    parts = urlsplit(unescape(href))
    pairs = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k != key]
    pairs.append((key, value))
    rebuilt = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(pairs), parts.fragment))
    return escape(rebuilt, quote=True)


def patch_tag_route(tag: str, route: str) -> str:
    tag = re.sub(r'\s+data-action-route-v515="[^"]*"', "", tag)
    tag = tag[:-1] + f' data-action-route-v515="{route}">'
    href_match = re.search(r'href="([^"]+)"', tag)
    if not href_match:
        raise RuntimeError("CTA sin href")
    href = with_query_param(href_match.group(1), "commercial_intent", route)
    return tag[:href_match.start(1)] + href + tag[href_match.end(1):]


def whatsapp_with_route(href: str, route: str) -> str:
    parts = urlsplit(unescape(href))
    message = parse_qs(parts.query).get("text", [""])[0]
    if not message:
        raise RuntimeError("WhatsApp directo sin texto")
    lines = [line for line in message.splitlines() if not line.startswith("Siguiente paso sugerido:")]
    insert_at = next((idx for idx, line in enumerate(lines) if line.startswith("Entiendo que")), len(lines))
    while insert_at > 0 and not lines[insert_at - 1].strip():
        insert_at -= 1
    lines.insert(insert_at, f"Siguiente paso sugerido: {ROUTE_LABEL[route]}.")
    if insert_at + 1 < len(lines) and lines[insert_at + 1].strip():
        lines.insert(insert_at + 1, "")
    message = "\n".join(lines)
    return "https://wa.me/573008507813?text=" + quote(message, safe="")


def patch_detail(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    code = modality_from_detail(text)
    if code not in ROUTE_BY_MODALITY:
        raise RuntimeError(f"{path.name}: modalidad desconocida {code}")
    route = ROUTE_BY_MODALITY[code]

    cta = re.search(r'<a class="buying-clarity-cta-v58"[^>]*data-decision-v58-cta="true"[^>]*>', text)
    if not cta:
        raise RuntimeError(f"{path.name}: falta CTA principal")
    cta_tag = patch_tag_route(cta.group(0), route)
    text = text[:cta.start()] + cta_tag + text[cta.end():]

    general = re.search(r'<a class="btn btn-outline-light" href="([^"]+)">Formulario general</a>', text)
    if not general:
        raise RuntimeError(f"{path.name}: falta Formulario general")
    general_href = with_query_param(general.group(1), "commercial_intent", route)
    text = text[:general.start(1)] + general_href + text[general.end(1):]

    desktop = re.search(r'<a class="btn btn-gold" href="(https://wa\.me/573008507813\?text=[^"]+)" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a>', text)
    if not desktop:
        raise RuntimeError(f"{path.name}: falta WhatsApp desktop")
    direct_href = whatsapp_with_route(desktop.group(1), route)
    text = text[:desktop.start(1)] + direct_href + text[desktop.end(1):]

    mobile = re.search(r'(<div class="detail-mobile-cta-v46"[^>]*>.*?<a href=")(https://wa\.me/573008507813\?text=[^"]+)(" target="_blank" rel="noopener noreferrer">WhatsApp</a>)', text, flags=re.S)
    if not mobile:
        raise RuntimeError(f"{path.name}: falta WhatsApp móvil")
    text = text[:mobile.start(2)] + direct_href + text[mobile.end(2):]
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(DETAIL_TARGETS) != 16:
        raise RuntimeError(f"Se esperaban 16 fichas profundas y se encontraron {len(DETAIL_TARGETS)}")
    contract = load_contract()
    patch_home(contract)
    for path in DETAIL_TARGETS:
        patch_detail(path)
    print("DECISION ACTION V5.15 OK: selector consolidado + comparación secundaria + ruta comercial controlada en 16 fichas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Aplica v5.13: continuidad de modalidad y prueba verificable hasta el brief comercial."""
from __future__ import annotations

from html import escape, unescape
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit, quote
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SITE_JS = ROOT / "site-v3.js"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
BLOCK_START = "<!-- COMMERCIAL-BRIEF-V513:START -->"
BLOCK_END = "<!-- COMMERCIAL-BRIEF-V513:END -->"
JS_START = "    // COMMERCIAL-BRIEF-V513:START"
JS_END = "    // COMMERCIAL-BRIEF-V513:END"
HOME_STYLE = '<link rel="stylesheet" href="commercial-brief-v513.css">'
HOME_SCRIPT = '<script src="commercial-brief-v513.js"></script>'
PROOF_STANDARD_LABEL = "Método + entregables + formatos + aceptación/cierre"

MODALITIES = {
    "diagnostic": "Diagnóstico jurídico",
    "audit": "Auditoría jurídica de alcance cerrado",
    "product": "Producto de alcance cerrado",
    "specialist": "Servicio jurídico especializado",
    "recurring": "Acompañamiento jurídico recurrente",
}

SPECIAL_BY_CATALOG = {
    "product-diagnostic": "audit",
    "service-diagnostic": "diagnostic",
    "service-direction": "recurring",
}


def modality_for(catalog_id: str, page_type: str) -> str:
    if catalog_id in SPECIAL_BY_CATALOG:
        return SPECIAL_BY_CATALOG[catalog_id]
    if page_type == "Producto jurídico":
        return "product"
    if page_type == "Servicio profesional":
        return "specialist"
    raise RuntimeError(f"No se pudo resolver modalidad para {catalog_id}/{page_type}")


def remove_block(text: str, start: str, end: str) -> str:
    pattern = r'(?ms)^[ \t]*' + re.escape(start) + r'[ \t]*\r?\n.*?^[ \t]*' + re.escape(end) + r'[ \t]*(?:\r?\n)?'
    return re.sub(pattern, "", text, count=1)


def ensure_head_item(text: str, item: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(item) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("Documento sin </head>")
    return text.replace("</head>", f"  {item}\n</head>", 1)


def add_query_params(href: str, **params: str) -> str:
    raw = unescape(href)
    parts = urlsplit(raw)
    current = dict(parse_qsl(parts.query, keep_blank_values=True))
    current.update(params)
    rebuilt = urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(current), parts.fragment))
    return escape(rebuilt, quote=True)


def brief_block() -> str:
    return f'''{BLOCK_START}
<div class="commercial-brief-v513 full" data-commercial-brief-v513="true" aria-labelledby="commercial-brief-v513-title">
  <div class="commercial-brief-head-v513">
    <div><span>CONTEXTO QUE ACOMPAÑA LA SOLICITUD</span><h3 id="commercial-brief-v513-title">La modalidad y el estándar verificable no se pierden al pasar a la conversación comercial.</h3><p>Cuando llega desde una ficha con alcance definido, el formulario conserva esas categorías para reducir repeticiones y preparar un brief más comparable.</p></div>
    <b class="commercial-brief-badge-v513" data-brief-status-v513>Contexto por completar</b>
  </div>
  <dl class="commercial-brief-grid-v513">
    <div><dt>Modalidad considerada</dt><dd data-brief-modality-v513>Por confirmar según el alcance</dd></div>
    <div><dt>Estándar verificable</dt><dd data-brief-proof-v513>Se definirá en la propuesta aplicable</dd></div>
  </dl>
  <p class="commercial-brief-note-v513">Estas categorías orientan la conversación y no constituyen una propuesta, aceptación del encargo ni garantía de que la modalidad inicialmente considerada sea la definitiva.</p>
</div>
{BLOCK_END}'''


def patch_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    text = remove_block(text, BLOCK_START, BLOCK_END)
    anchor = "<!-- COMMERCIAL-V59-QUALIFICATION:END -->"
    if anchor not in text:
        raise RuntimeError("index.html: falta ancla v5.9")
    text = text.replace(anchor, anchor + "\n" + brief_block(), 1)
    text = ensure_head_item(text, HOME_STYLE)
    text = re.sub(r'(?m)^[ \t]*' + re.escape(HOME_SCRIPT) + r'[ \t]*(?:\r?\n)?', "", text)
    script_anchor = '  <script src="commercial-intake-v59.js"></script>'
    if script_anchor not in text:
        raise RuntimeError("index.html: falta script v5.9")
    text = text.replace(script_anchor, script_anchor + "\n  " + HOME_SCRIPT, 1)

    for code in MODALITIES:
        pattern = re.compile(r'(<a class="proof-model-card-v512"\s+)([^>]*data-proof-model-v512="' + re.escape(code) + r'"[^>]*>)')
        match = pattern.search(text)
        if not match:
            raise RuntimeError(f"index.html: falta tarjeta v5.12 {code}")
        attrs = match.group(2)
        attrs = re.sub(r'\s+data-commercial-modality-v513="[^"]*"', "", attrs)
        attrs = attrs.replace(f'data-proof-model-v512="{code}"', f'data-proof-model-v512="{code}" data-commercial-modality-v513="{code}"', 1)
        href_match = re.search(r'href="([^"]+)"', attrs)
        if href_match and '.html' in unescape(href_match.group(1)):
            href = add_query_params(href_match.group(1), modality=code)
            attrs = attrs[:href_match.start(1)] + href + attrs[href_match.end(1):]
        text = text[:match.start()] + match.group(1) + attrs + text[match.end():]

    HOME.write_text(text, encoding="utf-8")


def patch_site_js() -> None:
    text = SITE_JS.read_text(encoding="utf-8")
    text = remove_block(text, JS_START, JS_END)
    anchor = "    if (context) lines.push(`Contexto comercial: ${context}`);"
    if anchor not in text:
        raise RuntimeError("site-v3.js: falta ancla de brief")
    block = f'''{JS_START}
    const commercialModalityV513 = cleanContactValue(form.dataset.commercialModalityV513 || '', 160);
    const proofExpectationV513 = cleanContactValue(form.dataset.proofExpectationV513 || '', 180);
    if (commercialModalityV513) lines.push(`Modalidad considerada: ${{commercialModalityV513}}`);
    if (proofExpectationV513) lines.push(`Estándar verificable: ${{proofExpectationV513}}`);
{JS_END}
'''
    text = text.replace(anchor, block + anchor, 1)
    SITE_JS.write_text(text, encoding="utf-8")


def direct_whatsapp_href(title: str, modality_label: str) -> str:
    message = (
        f"Hola, revisé la ficha de {title} en Meridiano Legal y quiero presentar una necesidad relacionada.\n\n"
        f"Modalidad considerada: {modality_label}\n"
        f"Estándar verificable: {PROOF_STANDARD_LABEL}\n\n"
        "Entiendo que la modalidad y el alcance definitivos deben confirmarse antes de una propuesta."
    )
    return "https://wa.me/573008507813?text=" + quote(message, safe="")


def patch_detail(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    body = re.search(r'<body\s+([^>]+)>', text)
    if not body:
        raise RuntimeError(f"{path.name}: falta body")
    attrs = body.group(1)
    catalog_match = re.search(r'data-catalog-id="([^"]+)"', attrs)
    type_match = re.search(r'data-page-type="([^"]+)"', attrs)
    title_match = re.search(r'data-page-title="([^"]+)"', attrs)
    need_match = re.search(r'data-page-need="([^"]+)"', attrs)
    if not all((catalog_match, type_match, title_match, need_match)):
        raise RuntimeError(f"{path.name}: metadatos de página incompletos")
    catalog_id = unescape(catalog_match.group(1))
    page_type = unescape(type_match.group(1))
    title = unescape(title_match.group(1))
    need = unescape(need_match.group(1))
    code = modality_for(catalog_id, page_type)
    label = MODALITIES[code]

    proof_tag = re.search(r'<section class="proof-detail-v512"[^>]*>', text)
    if not proof_tag:
        raise RuntimeError(f"{path.name}: falta bloque de prueba v5.12")
    tag = re.sub(r'\s+data-commercial-modality-v513="[^"]*"', "", proof_tag.group(0))
    tag = tag[:-1] + f' data-commercial-modality-v513="{code}">'
    text = text[:proof_tag.start()] + tag + text[proof_tag.end():]

    cta = re.search(r'<a class="buying-clarity-cta-v58"([^>]*)data-decision-v58-cta="true"([^>]*)href="([^"]+)"([^>]*)>', text)
    if not cta:
        cta = re.search(r'<a class="buying-clarity-cta-v58"([^>]*)href="([^"]+)"([^>]*)data-decision-v58-cta="true"([^>]*)>', text)
    if not cta:
        raise RuntimeError(f"{path.name}: falta CTA v5.8")
    tag = cta.group(0)
    href_match = re.search(r'href="([^"]+)"', tag)
    href = add_query_params(href_match.group(1), modality=code, proof_standard="source")
    tag = tag[:href_match.start(1)] + href + tag[href_match.end(1):]
    text = text[:cta.start()] + tag + text[cta.end():]

    form_url = "../index.html?" + urlencode({
        "context": f"{page_type}: {title}",
        "need": need,
        "commercial_intent": "proposal",
        "modality": code,
        "proof_standard": "source",
    }) + "#contacto"
    text = re.sub(
        r'<a class="btn btn-outline-light" href="[^"]*">Formulario general</a>',
        f'<a class="btn btn-outline-light" href="{escape(form_url, quote=True)}">Formulario general</a>',
        text,
        count=1,
    )

    direct_href = direct_whatsapp_href(title, label)
    text = re.sub(
        r'(<a class="btn btn-gold" href=")https://wa\.me/573008507813\?text=[^"]+(" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp →</a>)',
        lambda m: m.group(1) + direct_href + m.group(2),
        text,
        count=1,
    )
    text = re.sub(
        r'(<div class="detail-mobile-cta-v46"[^>]*>.*?<a href=")https://wa\.me/573008507813\?text=[^"]+(" target="_blank" rel="noopener noreferrer">WhatsApp</a>)',
        lambda m: m.group(1) + direct_href + m.group(2),
        text,
        count=1,
        flags=re.S,
    )
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(DETAIL_TARGETS) != 16:
        raise RuntimeError(f"Se esperaban 16 fichas y se encontraron {len(DETAIL_TARGETS)}")
    patch_home()
    patch_site_js()
    for path in DETAIL_TARGETS:
        patch_detail(path)
    print("COMMERCIAL BRIEF V5.13 OK: modalidad + estándar verificable conservados hasta formulario/WhatsApp en 16 fichas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

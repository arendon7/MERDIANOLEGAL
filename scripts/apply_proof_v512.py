#!/usr/bin/env python3
"""Aplica v5.12: apoyo de modalidad y prueba verificable derivada del catálogo jurídico."""
from __future__ import annotations

from html import escape
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
VERSION = ROOT / "version.json"
DETAIL_TARGETS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
HOME_START = "<!-- PROOF-V512-HOME:START -->"
HOME_END = "<!-- PROOF-V512-HOME:END -->"
DETAIL_START = "<!-- PROOF-V512-DETAIL:START -->"
DETAIL_END = "<!-- PROOF-V512-DETAIL:END -->"
HOME_STYLE = '<link rel="stylesheet" href="proof-v512.css">'
DETAIL_STYLE = '<link rel="stylesheet" href="../proof-v512.css">'


def remove_block(text: str, start: str, end: str) -> str:
    pattern = r'(?ms)^[ \t]*' + re.escape(start) + r'[ \t]*\r?\n.*?^[ \t]*' + re.escape(end) + r'[ \t]*(?:\r?\n)?'
    return re.sub(pattern, "", text, count=1)


def ensure_style(text: str, style: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(style) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("Documento sin cierre </head>")
    return text.replace("</head>", f"  {style}\n</head>", 1)


def version_at_least(major: int, minor: int) -> bool:
    payload = json.loads(VERSION.read_text(encoding="utf-8"))
    raw = str(payload.get("version", "0.0.0")).split(".")
    try:
        return (int(raw[0]), int(raw[1])) >= (major, minor)
    except (ValueError, IndexError):
        return False


def load_catalog() -> dict[str, dict]:
    catalog: dict[str, dict] = {}
    paths = sorted((ROOT / "catalog-products-v41").glob("*.json")) + sorted((ROOT / "catalog-services-v42").glob("*.json"))
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if len(payload) != 1:
            raise RuntimeError(f"{path.name}: se esperaba una ficha")
        key, value = next(iter(payload.items()))
        catalog[key] = value
    if len(catalog) != 16:
        raise RuntimeError(f"Se esperaban 16 fichas y se encontraron {len(catalog)}")
    return catalog


def pairs(values, limit: int = 3) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for item in values or []:
        if isinstance(item, list) and item:
            title = str(item[0])
            description = str(item[1]) if len(item) > 1 else ""
            out.append((title, description))
        elif isinstance(item, str):
            out.append((item, ""))
        if len(out) >= limit:
            break
    if not out:
        raise RuntimeError("Fuente sin elementos verificables")
    return out


def pair_list(items: list[tuple[str, str]]) -> str:
    parts: list[str] = []
    for title, description in items:
        detail = f"<small>{escape(description)}</small>" if description else ""
        parts.append(f"<li><strong>{escape(title)}</strong>{detail}</li>")
    return "<ul>" + "".join(parts) + "</ul>"


def detail_block(data: dict) -> str:
    method = pairs(data.get("method"))
    deliverables = pairs(data.get("deliverables"))
    formats = pairs(data.get("formats"))
    acceptance = pairs(data.get("acceptance"))
    return f'''{DETAIL_START}
<section class="proof-detail-v512" data-proof-v512="true" aria-labelledby="proof-detail-v512-title">
  <div class="container">
    <div class="proof-detail-head-v512">
      <div><p class="eyebrow">PRUEBA VERIFICABLE DEL TRABAJO</p><h2 id="proof-detail-v512-title">Qué puede comprobar durante y al cierre de esta solución.</h2><p>Este bloque no añade promesas comerciales: resume método, entregables, formatos y criterios de aceptación directamente desde la fuente jurídica de la ficha.</p></div>
      <a href="../firma.html#metodo">Ver método y principios →</a>
    </div>
    <div class="proof-detail-grid-v512">
      <article class="proof-detail-card-v512" data-proof-dimension-v512="method"><span>01 · MÉTODO</span><h3>Cómo se ejecuta</h3>{pair_list(method)}</article>
      <article class="proof-detail-card-v512" data-proof-dimension-v512="deliverables"><span>02 · ENTREGABLES</span><h3>Qué evidencia material recibe</h3>{pair_list(deliverables)}</article>
      <article class="proof-detail-card-v512" data-proof-dimension-v512="formats"><span>03 · FORMATOS</span><h3>Cómo queda documentado</h3>{pair_list(formats)}</article>
      <article class="proof-detail-card-v512" data-proof-dimension-v512="acceptance"><span>04 · ACEPTACIÓN</span><h3>Cómo se verifica el cierre</h3>{pair_list(acceptance)}</article>
    </div>
    <p class="proof-detail-note-v512">La calidad se evalúa contra el perímetro, la evidencia disponible, los entregables y los criterios pactados; no contra resultados externos que dependan de autoridades, contrapartes o terceros.</p>
  </div>
</section>
{DETAIL_END}'''


def home_block() -> str:
    return f'''{HOME_START}
<section class="proof-router-v512" data-proof-router-v512="true" aria-labelledby="proof-router-v512-title">
  <div class="container">
    <div class="section-heading"><p class="eyebrow dark">ELEGIR LA MODALIDAD</p><h2 id="proof-router-v512-title">El tipo de trabajo debe corresponder al tipo de incertidumbre.</h2><p>No es lo mismo explorar una exposición, auditar integralmente, comprar un resultado cerrado, resolver un asunto especializado o sostener una función jurídica recurrente.</p></div>
    <div class="proof-model-grid-v512">
      <a class="proof-model-card-v512" data-proof-model-v512="diagnostic" href="servicios/diagnostico-juridico-empresarial.html"><span>Exploración dirigida</span><h3>Diagnóstico jurídico</h3><p>Cuando todavía debe identificarse qué exposiciones importan, qué priorizar y qué trabajo posterior es proporcional.</p><b>2–4 semanas · Ver diagnóstico →</b></a>
      <a class="proof-model-card-v512" data-proof-model-v512="audit" href="productos/diagnostico-juridico-empresarial.html"><span>Revisión integral cerrada</span><h3>Auditoría jurídica</h3><p>Cuando se necesita una revisión transversal documentada, con perímetro, volúmenes, hallazgos y cierre ejecutivo predefinidos.</p><b>5–6 semanas · Ver auditoría →</b></a>
      <a class="proof-model-card-v512" data-proof-model-v512="product" href="#productos"><span>Resultado predefinido</span><h3>Producto de alcance cerrado</h3><p>Cuando el resultado permite fijar desde el inicio cantidades, entregables, cronograma y criterios objetivos de aceptación.</p><b>Comparar productos →</b></a>
      <a class="proof-model-card-v512" data-proof-model-v512="specialist" href="#servicios"><span>Proyecto adaptable</span><h3>Servicio especializado</h3><p>Cuando la decisión está identificada, pero hechos, regulación, negociación o actores obligan a ajustar el alcance.</p><b>Explorar servicios →</b></a>
      <a class="proof-model-card-v512" data-proof-model-v512="recurring" href="servicios/direccion-juridica-externa.html"><span>Capacidad recurrente</span><h3>Dirección jurídica externa</h3><p>Cuando la empresa necesita triage, criterio, seguimiento, memoria y gobierno continuo de su demanda jurídica.</p><b>Ver dirección jurídica →</b></a>
    </div>
    <div class="proof-standard-v512" data-proof-standard-v512="true">
      <div><h3>Qué debería poder verificar antes de contratar</h3><p>Una propuesta comparable no depende de reputación abstracta: debe permitir entender cómo se trabajará y contra qué se evaluará el cierre.</p></div>
      <div class="proof-standard-grid-v512"><span>Perímetro y exclusiones explícitos</span><span>Entregables y formatos identificables</span><span>Método, responsables y dependencias</span><span>Criterios de aceptación y cierre</span></div>
    </div>
  </div>
</section>
{HOME_END}'''


def patch_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    if version_at_least(5, 20) and 'data-home-decision-v520="true"' in text:
        text = ensure_style(text, HOME_STYLE)
        HOME.write_text(text, encoding="utf-8")
        return
    text = remove_block(text, HOME_START, HOME_END)
    anchor = "<!-- DECISION-V58-HOME:END -->"
    if anchor not in text:
        raise RuntimeError("index.html: falta bloque v5.8")
    text = text.replace(anchor, anchor + "\n" + home_block(), 1)
    text = ensure_style(text, HOME_STYLE)
    HOME.write_text(text, encoding="utf-8")


def patch_detail(path: Path, catalog: dict[str, dict]) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.search(r'data-catalog-id="([^"]+)"', text)
    if not match:
        raise RuntimeError(f"{path.name}: falta data-catalog-id")
    catalog_id = match.group(1)
    if catalog_id not in catalog:
        raise RuntimeError(f"{path.name}: catálogo {catalog_id} inexistente")

    if 'data-experience-system="v6"' in text:
        if text.count(DETAIL_START) != 1 or text.count(DETAIL_END) != 1:
            raise RuntimeError(f"{path.name}: v6 debe preservar exactamente un bloque v5.12")
        text = ensure_style(text, DETAIL_STYLE)
        path.write_text(text, encoding="utf-8")
        return

    text = remove_block(text, DETAIL_START, DETAIL_END)
    anchor = re.compile(r'</div>\s*</main>\s*<!-- STATIC-CATALOG-BODY:END -->')
    replacement = '</div>\n' + detail_block(catalog[catalog_id]) + '\n</main>\n<!-- STATIC-CATALOG-BODY:END -->'
    text, count = anchor.subn(lambda _m: replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"{path.name}: falta ancla de cierre canónica")
    text = ensure_style(text, DETAIL_STYLE)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    if len(DETAIL_TARGETS) != 16:
        raise RuntimeError(f"Se esperaban 16 fichas profundas y se encontraron {len(DETAIL_TARGETS)}")
    catalog = load_catalog()
    patch_home()
    for path in DETAIL_TARGETS:
        patch_detail(path, catalog)
    print("PROOF V5.12 OK: matriz de modalidad + prueba verificable derivada en 16 fichas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Render the W5.0C v8 Home as an ephemeral, non-indexable preview.

The renderer is source-driven and intentionally does not overwrite index.html.
It points contact CTAs to the single existing canonical contact form until the
form itself is migrated through a dedicated gate.
"""
from __future__ import annotations

from argparse import ArgumentParser
from html import escape
from pathlib import Path
import json
import sys

from v8_shell import load_model, prefixed, render_footer, render_header, resolve_item_href

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / ".w5-preview/index.html"


def e(value: object) -> str:
    return escape(str(value), quote=True)


def route_map(model: dict) -> dict[str, list]:
    result: dict[str, list] = {}
    for rows in model["navigation"]["mega_groups"].values():
        for row in rows:
            result[row[0]] = row
    return result


def href_for(model: dict, route_id: str, prefix: str) -> str | None:
    row = route_map(model)[route_id]
    return resolve_item_href(row, prefix)


def linked_title(model: dict, route_id: str, prefix: str, class_name: str = "") -> str:
    row = route_map(model)[route_id]
    href = resolve_item_href(row, prefix)
    label = row[1]
    if not href:
        return f'<span class="{e(class_name)}" data-ml-route-id="{e(route_id)}">{e(label)}</span>'
    return f'<a class="{e(class_name)}" data-ml-route-id="{e(route_id)}" href="{e(href)}">{e(label)}</a>'


def render_hero(home: dict, contact_href: str) -> str:
    hero = home["hero"]
    return f'''<section class="ml-home-hero" data-v8-home-section="H01" aria-labelledby="ml-home-title">
  <div class="ml-container ml-home-hero-grid">
    <div class="ml-home-hero-copy">
      <p class="ml-eyebrow">{e(hero["eyebrow"])}</p>
      <h1 id="ml-home-title">{e(hero["title"])}</h1>
      <p class="ml-lead">{e(hero["lead"])}</p>
      <div class="ml-actions">
        <a class="ml-btn" data-ml-event="cta_click" href="{e(contact_href)}">Hablar con Meridiano</a>
        <a class="ml-btn ml-btn--secondary" href="#soluciones">{e(hero["secondary"][0])}</a>
      </div>
      <div class="ml-home-signals" aria-label="Ámbitos de trabajo">
        <span>EMPRESA</span><span>CONTRATOS</span><span>REGULACIÓN</span><span>TECNOLOGÍA</span><span>PROYECTOS</span>
      </div>
    </div>
    <div class="ml-home-m" aria-hidden="true">
      <span class="ml-home-m-line ml-home-m-line--a"></span>
      <span class="ml-home-m-line ml-home-m-line--b"></span>
      <span class="ml-home-m-line ml-home-m-line--c"></span>
      <span class="ml-home-m-node ml-home-m-node--1"></span>
      <span class="ml-home-m-node ml-home-m-node--2"></span>
      <span class="ml-home-m-node ml-home-m-node--3"></span>
      <span class="ml-home-m-label">M</span>
    </div>
  </div>
</section>'''


def render_situations(model: dict, home: dict, prefix: str) -> str:
    data = home["situations"]
    cards = []
    for index, (label, route_id) in enumerate(data["items"], start=1):
        href = href_for(model, route_id, prefix)
        if not href:
            raise ValueError(f"H02 route {route_id} has no candidate-safe href")
        cards.append(
            f'<a class="ml-home-problem" data-ml-route-id="{e(route_id)}" href="{e(href)}">'
            f'<span>{index:02d}</span><strong>{e(label)}</strong><b aria-hidden="true">→</b></a>'
        )
    return f'''<section class="ml-section ml-home-situations" data-v8-home-section="H02" aria-labelledby="ml-situations-title">
  <div class="ml-container">
    <div class="ml-section-head"><p class="ml-eyebrow">SU SITUACIÓN</p><h2 id="ml-situations-title">{e(data["title"])}</h2><p class="ml-lead">No necesita conocer de antemano el nombre jurídico de la solución. Empiece por la decisión o fricción empresarial que necesita ordenar.</p></div>
    <div class="ml-home-problem-grid">{"".join(cards)}</div>
  </div>
</section>'''


def render_featured(model: dict, home: dict, prefix: str) -> str:
    data = home["featured_solutions"]
    rows = []
    descriptions = {
        "SO01": "Entender el estado jurídico, priorizar hallazgos y convertirlos en una hoja de ruta.",
        "SO07": "Pasar de contratos aislados a modelos, reglas, aprobaciones, playbook y control contractual.",
        "SO04": "Preparar estructura societaria, cap table, contratos, intangibles y data room antes de inversión.",
        "SO06": "Integrar regulación, permisos, contratos, actores, riesgos y condiciones de ejecución de un proyecto.",
    }
    for index, route_id in enumerate(data["route_ids"], start=1):
        row = route_map(model)[route_id]
        href = resolve_item_href(row, prefix)
        if not href:
            raise ValueError(f"H03 route {route_id} has no candidate-safe href")
        rows.append(
            f'<a class="ml-home-solution-row" data-ml-route-id="{e(route_id)}" data-ml-event="solution_view" href="{e(href)}">'
            f'<span>{index:02d}</span><strong>{e(row[1])}</strong><p>{e(descriptions[route_id])}</p><b aria-hidden="true">Explorar →</b></a>'
        )
    return f'''<section class="ml-section ml-section--soft" id="soluciones" data-v8-home-section="H03" aria-labelledby="ml-solutions-title">
  <div class="ml-container">
    <div class="ml-section-head"><p class="ml-eyebrow">SOLUCIONES</p><h2 id="ml-solutions-title">{e(data["title"])}</h2><p class="ml-lead">Cada solución parte de una necesidad empresarial y termina en entregables, responsabilidades y límites definidos.</p></div>
    <div class="ml-home-solution-list">{"".join(rows)}</div>
  </div>
</section>'''


def render_contracts(model: dict, home: dict, prefix: str) -> str:
    data = home["meridiano_contracts"]
    loop = "".join(f'<li><span>{index:02d}</span><strong>{e(step)}</strong></li>' for index, step in enumerate(data["loop"], start=1))
    guardrails = "".join(f'<li>{e(item)}</li>' for item in data["guardrails"][:2])
    system_href = href_for(model, "SO07", prefix)
    return f'''<section class="ml-section ml-home-contracts" data-v8-home-section="H04" aria-labelledby="ml-contracts-title">
  <div class="ml-container ml-home-contracts-grid">
    <div>
      <p class="ml-eyebrow">CONTINUIDAD CONTRACTUAL</p>
      <h2 id="ml-contracts-title">{e(data["title"])}</h2>
      <p class="ml-home-contracts-headline">{e(data["headline"])}</p>
      <p>{e(data["body"])}</p>
      <ul class="ml-home-guardrails">{guardrails}</ul>
      <div class="ml-actions"><a class="ml-btn ml-btn--secondary" href="{e(system_href)}">Estructurar primero el sistema contractual →</a></div>
    </div>
    <ol class="ml-home-contract-loop" aria-label="Ciclo de Meridiano Contratos">{loop}</ol>
  </div>
</section>'''


def render_practices(model: dict, home: dict, prefix: str) -> str:
    data = home["practices"]
    rows = []
    for index, route_id in enumerate(data["route_ids"], start=1):
        row = route_map(model)[route_id]
        href = resolve_item_href(row, prefix)
        if not href:
            raise ValueError(f"H05 route {route_id} has no candidate-safe href")
        rows.append(
            f'<a class="ml-home-practice-row" data-ml-route-id="{e(route_id)}" data-ml-event="practice_view" href="{e(href)}">'
            f'<span>{index:02d}</span><strong>{e(row[1])}</strong><b aria-hidden="true">→</b></a>'
        )
    return f'''<section class="ml-section" data-v8-home-section="H05" aria-labelledby="ml-practices-title">
  <div class="ml-container ml-home-editorial-split">
    <div class="ml-section-head"><p class="ml-eyebrow">PRÁCTICAS</p><h2 id="ml-practices-title">{e(data["title"])}</h2><p class="ml-lead">La práctica expresa profundidad jurídica. La solución expresa el resultado concreto que la empresa necesita construir.</p></div>
    <div class="ml-home-practice-list">{"".join(rows)}</div>
  </div>
</section>'''


def render_method(home: dict) -> str:
    data = home["method"]
    steps = "".join(f'<li><span>{index:02d}</span><strong>{e(step)}</strong></li>' for index, step in enumerate(data["steps"], start=1))
    return f'''<section class="ml-section ml-section--dark ml-home-method" data-v8-home-section="H06" aria-labelledby="ml-method-title">
  <div class="ml-container ml-home-method-grid">
    <div><p class="ml-eyebrow">MÉTODO</p><h2 id="ml-method-title">{e(data["title"])}</h2><p>El trabajo jurídico debe terminar en una estructura que la dirección pueda ejecutar, controlar y volver a consultar.</p></div>
    <ol>{steps}</ol>
  </div>
</section>'''


def render_evidence(home: dict, prefix: str) -> str:
    data = home["evidence"]
    return f'''<section class="ml-section ml-home-evidence" data-v8-home-section="H07" aria-labelledby="ml-evidence-title">
  <div class="ml-container ml-home-editorial-split">
    <div><p class="ml-eyebrow">EXPERIENCIA Y CRITERIO</p><h2 id="ml-evidence-title">{e(data["title"])}</h2></div>
    <div class="ml-home-evidence-body"><p>Meridiano evita convertir experiencia en una colección de logos o afirmaciones imposibles de verificar. La evidencia se presenta con el contexto suficiente para entender el tipo de decisión, la intervención jurídica y sus límites.</p><a class="ml-text-link" href="{e(prefixed("firma.html#trayectoria", prefix))}">Conocer la firma y su trayectoria →</a></div>
  </div>
</section>'''


def render_external_direction(model: dict, home: dict, prefix: str, contact_href: str) -> str:
    data = home["external_legal_direction"]
    href = href_for(model, data["route_id"], prefix)
    dimensions = "".join(f'<li>{e(item)}</li>' for item in data["commercial_dimensions"])
    return f'''<section class="ml-section ml-home-direction" data-v8-home-section="H08" aria-labelledby="ml-direction-title">
  <div class="ml-container ml-home-direction-grid">
    <div><p class="ml-eyebrow">RELACIÓN CONTINUA</p><h2 id="ml-direction-title">{e(data["title"])}</h2><p>Para empresas que necesitan criterio jurídico recurrente, seguimiento y una contraparte que entienda el negocio sin construir un departamento jurídico completo desde cero.</p><div class="ml-actions"><a class="ml-btn" href="{e(href)}">Explorar Dirección Jurídica Externa →</a><a class="ml-btn ml-btn--secondary" href="{e(contact_href)}">Evaluar este modelo</a></div></div>
    <div><p class="ml-home-direction-label">La relación se estructura por</p><ul class="ml-home-direction-dimensions">{dimensions}</ul><p class="ml-home-direction-note">No se presenta como una bolsa pública de horas. El alcance se define por cobertura, complejidad, prioridad, nivel de servicio y gobierno.</p></div>
  </div>
</section>'''


def render_sectors(home: dict, prefix: str) -> str:
    data = home["sectors"]
    rows = []
    for index, (label, legacy_href, _target) in enumerate(data["items"], start=1):
        href = prefixed(legacy_href, prefix)
        rows.append(f'<a class="ml-home-sector" href="{e(href)}"><span>{index:02d}</span><strong>{e(label)}</strong><b aria-hidden="true">→</b></a>')
    return f'''<section class="ml-section ml-section--soft" id="sectores" data-v8-home-section="H09" aria-labelledby="ml-sectors-title">
  <div class="ml-container"><div class="ml-section-head"><p class="ml-eyebrow">SECTORES</p><h2 id="ml-sectors-title">{e(data["title"])}</h2></div><div class="ml-home-sector-grid">{"".join(rows)}</div></div>
</section>'''


def render_legal_intelligence(home: dict, prefix: str) -> str:
    data = home["legal_intelligence"]
    return f'''<section class="ml-section ml-home-intelligence" data-v8-home-section="H10" aria-labelledby="ml-intelligence-title">
  <div class="ml-container ml-home-intelligence-grid"><div><p class="ml-eyebrow">LEGAL INTELLIGENCE</p><h2 id="ml-intelligence-title">{e(data["title"])}</h2></div><div><p>{e(data["body"])}</p><a class="ml-text-link" href="{e(prefixed(data["href"], prefix))}">Ver cómo trabajamos →</a></div></div>
</section>'''


def render_insights(home: dict, prefix: str) -> str:
    data = home["insights"]
    items = []
    for title, href in data["items"]:
        items.append(f'<a class="ml-home-insight" href="{e(prefixed(href, prefix))}"><span>INSIGHT</span><strong>{e(title)}</strong><b aria-hidden="true">Leer →</b></a>')
    return f'''<section class="ml-section" data-v8-home-section="H11" aria-labelledby="ml-insights-title"><div class="ml-container"><div class="ml-section-head"><p class="ml-eyebrow">INSIGHTS</p><h2 id="ml-insights-title">{e(data["title"])}</h2></div><div class="ml-home-insight-grid">{"".join(items)}</div></div></section>'''


def render_final_cta(model: dict, home: dict, prefix: str, contact_href: str) -> str:
    data = home["final_cta"]
    diagnostic = next(row for row in model["navigation"]["actions"] if row[0] == "diagnostic")
    return f'''<section class="ml-section ml-section--dark ml-home-final" data-v8-home-section="H12" aria-labelledby="ml-final-title"><div class="ml-container ml-home-final-grid"><div><p class="ml-eyebrow">SIGUIENTE PASO</p><h2 id="ml-final-title">{e(data["title"])}</h2><p>Puede empezar por una conversación o por el diagnóstico jurídico empresarial si todavía necesita ordenar prioridades.</p></div><div class="ml-actions"><a class="ml-btn ml-home-btn-light" href="{e(contact_href)}">Hablar con Meridiano</a><a class="ml-btn ml-btn--secondary ml-home-btn-outline" href="{e(prefixed(diagnostic[3], prefix))}">Solicitar diagnóstico</a></div></div></section>'''


def render_home(model: dict, *, prefix: str = "../", contact_href: str = "../index.html#contacto") -> str:
    home = model["home"]
    sections = {
        "H01": render_hero(home, contact_href),
        "H02": render_situations(model, home, prefix),
        "H03": render_featured(model, home, prefix),
        "H04": render_contracts(model, home, prefix),
        "H05": render_practices(model, home, prefix),
        "H06": render_method(home),
        "H07": render_evidence(home, prefix),
        "H08": render_external_direction(model, home, prefix, contact_href),
        "H09": render_sectors(home, prefix),
        "H10": render_legal_intelligence(home, prefix),
        "H11": render_insights(home, prefix),
        "H12": render_final_cta(model, home, prefix, contact_href),
    }
    body = "\n".join(sections[item] for item in home["section_order"])
    return f'''<!doctype html>
<html lang="es-CO" data-v8-home-preview="true">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <meta name="description" content="Meridiano Legal integra derecho empresarial, comprensión del negocio y tecnología aplicada para estructurar decisiones que necesitan avanzar.">
  <meta name="theme-color" content="#13263a">
  <title>Meridiano Legal | Derecho empresarial para decisiones que necesitan avanzar</title>
  <link rel="icon" href="{e(prefixed("assets/brand/favicon.svg", prefix))}" type="image/svg+xml">
  <link rel="stylesheet" href="{e(prefixed("assets/css/v8/tokens.css", prefix))}">
  <link rel="stylesheet" href="{e(prefixed("assets/css/v8/base.css", prefix))}">
  <link rel="stylesheet" href="{e(prefixed("assets/css/v8/components.css", prefix))}">
  <link rel="stylesheet" href="{e(prefixed("assets/css/v8/surfaces.css", prefix))}">
  <script defer src="{e(prefixed("assets/js/v8/navigation.js", prefix))}"></script>
</head>
<body class="ml-home-preview">
  <a class="ml-skip-link" href="#contenido">Saltar al contenido</a>
  {render_header(model, prefix=prefix, contact_href=contact_href)}
  <main id="contenido" data-v8-home-shell="candidate">
    {body}
  </main>
  {render_footer(model, prefix=prefix, contact_href=contact_href)}
</body>
</html>
'''


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--prefix", default="../")
    parser.add_argument("--contact-href", default="../index.html#contacto")
    args = parser.parse_args()

    model = load_model()
    if model.get("status") != "candidate" or model.get("activation", {}).get("public"):
        raise SystemExit("W5 Home renderer refuses non-candidate/public activation state")
    html = render_home(model, prefix=args.prefix, contact_href=args.contact_href)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"RENDER V8 W5 HOME OK: {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"RENDER V8 W5 HOME FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Materializa Wave 3 de Experience v6 sobre las seis rutas de necesidad y su hub.

Fuentes:
- growth-solutions-v51.json: situación, señales, preguntas, rutas, entregables y límites.
- cro-solutions-v52.json: encaje, pricing, CTA y contenido secundario.

La composición v5.31 completa permanece en el DOM dentro de details nativo.
"""
from __future__ import annotations

from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
GROWTH = ROOT / "growth-solutions-v51.json"
CRO = ROOT / "cro-solutions-v52.json"
SOLUTIONS_DIR = ROOT / "soluciones"

START = "<!-- EXPERIENCE-V60-SOLUTION:START -->"
END = "<!-- EXPERIENCE-V60-SOLUTION:END -->"
LEGACY_START = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:START -->"
LEGACY_END = "<!-- EXPERIENCE-V60-SOLUTION-LEGACY:END -->"
HUB_START = "<!-- EXPERIENCE-V60-SOLUTION-HUB:START -->"
HUB_END = "<!-- EXPERIENCE-V60-SOLUTION-HUB:END -->"

STYLE_PATHS = [
    "../assets/css/v6/tokens.css",
    "../assets/css/v6/base.css",
    "../assets/css/v6/components.css",
    "../assets/css/v6/surfaces.css",
    "../assets/css/v6/solutions.css",
]


def e(value: object) -> str:
    return escape(str(value), quote=True)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_styles(text: str) -> str:
    for href in STYLE_PATHS:
        text = re.sub(rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(href)}">\s*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("solución sin </head>")
    links = "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in STYLE_PATHS)
    return text.replace("</head>", f"{links}\n</head>", 1)


def mark_body(text: str, surface: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        for attr in ("data-experience-system", "data-experience-wave", "data-experience-surface"):
            tag = re.sub(rf'\s{attr}="[^"]*"', "", tag)
        return tag[:-1] + f' data-experience-system="v6" data-experience-wave="solutions" data-experience-surface="{e(surface)}">'
    return re.sub(r"<body\b[^>]*>", repl, text, count=1)


def extract_main(text: str) -> tuple[re.Match[str], str]:
    match = re.search(r'<main id="contenido"[^>]*>(.*?)</main>', text, flags=re.S)
    if not match:
        raise RuntimeError("solución sin <main id=contenido>")
    return match, match.group(1)


def extract_legacy(main: str) -> str:
    match = re.search(re.escape(LEGACY_START) + r"(.*?)" + re.escape(LEGACY_END), main, flags=re.S)
    return match.group(1) if match else main


def contact_href(growth: dict) -> str:
    query = urlencode({"context": growth["title"], "need": growth["need"], "experience": "v6"})
    return f"../index.html?{query}#contacto"


def rows(items: list[str], cls: str) -> str:
    return "".join(
        f'<div class="{cls}"><b>{idx:02d}</b><p>{e(item)}</p></div>'
        for idx, item in enumerate(items, 1)
    )


def render_routes(routes: list[dict]) -> str:
    return "".join(
        f'<article class="v6-route-option"><h3>{e(item["name"])}</h3><p>{e(item["summary"])}</p><a href="{e(item["href"])}">Revisar alcance →</a></article>'
        for item in routes
    )


def render_deliverables(items: list[str]) -> str:
    return "".join(
        f'<div class="v6-deliverable-item"><b>{idx:02d}</b><span>{e(item)}</span></div>'
        for idx, item in enumerate(items, 1)
    )


def render_solution(growth: dict, cro: dict, legacy: str) -> str:
    href = contact_href(growth)
    fit = "".join(f"<li>{e(item)}</li>" for item in cro["fit"])
    not_fit = "".join(f"<li>{e(item)}</li>" for item in cro["not_fit"])
    return f'''{START}
<section class="v6-hero v6-solution-hero" aria-labelledby="v6-solution-title"><div class="v6-container v6-hero-grid"><div class="v6-hero-copy"><p class="v6-eyebrow">{e(growth['eyebrow'])}</p><h1 class="v6-display" id="v6-solution-title">{e(growth['title'])}</h1><p class="v6-lead">{e(growth['description'])}</p><p class="v6-solution-intent">{e(growth['intent'])}</p><div class="v6-actions"><a class="v6-btn" href="{e(href)}">Presentar esta situación →</a><a class="v6-btn v6-btn-secondary" href="#v6-solution-fit">Comprobar encaje</a></div></div></div></section>
<section class="v6-section" id="v6-solution-signals" aria-labelledby="v6-solution-signals-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">SEÑALES</p><h2 class="v6-heading" id="v6-solution-signals-title">Cuándo conviene tratar esta necesidad como una decisión abierta.</h2></div><div class="v6-signal-list">{rows(growth['signals'], 'v6-signal-row')}</div></div></section>
<section class="v6-section v6-solution-fit" id="v6-solution-fit" aria-labelledby="v6-solution-fit-title"><div class="v6-container"><div class="v6-fit-intro"><strong id="v6-solution-fit-title">{e(cro['decision_label'])}</strong><p>{e(cro['decision_copy'])}</p></div><div class="v6-fit-grid"><article class="v6-fit-column"><h3>Conviene explorar esta ruta cuando…</h3><ul>{fit}</ul></article><article class="v6-fit-column is-not"><h3>No necesariamente es la ruta correcta cuando…</h3><ul>{not_fit}</ul></article></div></div></section>
<section class="v6-section v6-solution-decisions" id="v6-solution-decisions" aria-labelledby="v6-solution-decisions-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">DECISIONES</p><h2 class="v6-heading" id="v6-solution-decisions-title">Las preguntas que deben quedar resueltas antes de escoger modalidad.</h2></div><div class="v6-decision-list">{rows(growth['questions'], 'v6-decision-row')}</div></div></section>
<section class="v6-section" id="v6-solution-routes" aria-labelledby="v6-solution-routes-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">RUTAS DE INTERVENCIÓN</p><h2 class="v6-heading" id="v6-solution-routes-title">La misma necesidad puede requerir un producto cerrado, un servicio adaptable o capacidad recurrente.</h2><p class="v6-lead">La modalidad depende del resultado, perímetro, urgencia, volumen, negociación y seguimiento que realmente se necesiten.</p></div><div class="v6-route-list">{render_routes(growth['routes'])}</div></div></section>
<section class="v6-section v6-solution-result" id="v6-solution-result" aria-labelledby="v6-solution-result-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">RESULTADO ADMINISTRABLE</p><h2 class="v6-heading" id="v6-solution-result-title">Qué puede quedar instalado al resolver esta situación.</h2></div><div class="v6-deliverable-list">{render_deliverables(growth['deliverables'])}</div><div class="v6-context-links"><a href="{e(growth['perspective']['href'])}">Perspectiva relacionada: {e(growth['perspective']['name'])} →</a><a href="{e(growth['sector']['href'])}">{e(growth['sector']['name'])} →</a></div></div></section>
<section class="v6-section" id="v6-solution-pricing" aria-labelledby="v6-solution-pricing-title"><div class="v6-container"><div class="v6-pricing-note"><div><p class="v6-eyebrow">ALCANCE Y HONORARIOS</p><h3 id="v6-solution-pricing-title">{e(cro['pricing']['title'])}</h3><p>{e(cro['pricing']['copy'])}</p></div><a href="{e(cro['pricing']['href'])}">Revisar referencias públicas →</a></div></div></section>
<section class="v6-section v6-boundary" id="v6-solution-boundary" aria-labelledby="v6-solution-boundary-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">LÍMITES</p><h2 class="v6-heading" id="v6-solution-boundary-title">La ruta orienta la intervención; no convierte el alcance en una obligación abierta.</h2></div><ul class="v6-boundary-list"><li>{e(growth['limits'])}</li></ul></div></section>
<section class="v6-section v6-solution-cta" aria-labelledby="v6-solution-cta-title"><div class="v6-container v6-solution-cta-inner"><div><p class="v6-eyebrow">SIGUIENTE PASO</p><h2 class="v6-heading" id="v6-solution-cta-title">{e(cro['cta_title'])}</h2><p class="v6-lead">{e(cro['cta_copy'])}</p></div><a class="v6-btn" href="{e(href)}">Presentar necesidad →</a></div></section>
<details class="v6-depth v6-solution-depth" id="v6-solution-depth"><summary><span>PROFUNDIDAD ADICIONAL</span><strong>Ver objeciones, FAQ, rutas relacionadas, prueba y composición completa v5.31</strong></summary><div class="v6-depth-inner">{LEGACY_START}{legacy}{LEGACY_END}</div></details>
{END}'''


def render_hub(growth_solutions: list[dict], hub: dict, legacy: str) -> str:
    guides = "".join(
        f'<a href="{e(item["href"])}"><strong>{e(item["title"])}</strong><p>{e(item["copy"])}</p><span>Ver punto de entrada →</span></a>'
        for item in hub["guides"]
    )
    routes = "".join(
        f'<a class="v6-index-row" href="{e(item["slug"])}.html"><span class="v6-index-num">{idx:02d}</span><strong class="v6-index-title">{e(item["short"])}</strong><span class="v6-index-action">{e(item["intent"])} →</span></a>'
        for idx, item in enumerate(growth_solutions, 1)
    )
    return f'''{HUB_START}
<section class="v6-section v6-hub-hero" aria-labelledby="v6-solutions-hub-title"><div class="v6-container"><p class="v6-eyebrow">SOLUCIONES POR SITUACIÓN EMPRESARIAL</p><h1 class="v6-display" id="v6-solutions-hub-title">{e(hub['headline'])}</h1><p class="v6-lead">{e(hub['intro'])}</p><div class="v6-actions"><a class="v6-btn" href="../index.html#contacto">Presentar una necesidad →</a><a class="v6-btn v6-btn-secondary" href="#v6-solutions-routes">Ver las seis rutas</a></div></div></section>
<section class="v6-section" aria-labelledby="v6-solutions-guide-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">GUÍA RÁPIDA</p><h2 class="v6-heading" id="v6-solutions-guide-title">Tres formas de reconocer su punto de entrada.</h2></div><div class="v6-hub-guide">{guides}</div></div></section>
<section class="v6-section v6-hub-routes" id="v6-solutions-routes" aria-labelledby="v6-solutions-routes-title"><div class="v6-container"><div class="v6-section-head"><p class="v6-eyebrow">SEIS DECISIONES</p><h2 class="v6-heading" id="v6-solutions-routes-title">Empiece por lo que está ocurriendo; la modalidad viene después.</h2></div><div class="v6-index">{routes}</div></div></section>
<section class="v6-section v6-solution-cta" aria-labelledby="v6-solutions-hub-cta"><div class="v6-container v6-solution-cta-inner"><div><p class="v6-eyebrow">SI SU SITUACIÓN NO ENCAJA</p><h2 class="v6-heading" id="v6-solutions-hub-cta">Puede presentar directamente la decisión o el resultado esperado.</h2><p class="v6-lead">Meridiano calificará si corresponde orientación, diagnóstico, producto cerrado, servicio, plan recurrente o coordinación con otra especialidad.</p></div><a class="v6-btn" href="../index.html#contacto">Presentar necesidad →</a></div></section>
<details class="v6-depth v6-solution-depth"><summary><span>PROFUNDIDAD DEL HUB</span><strong>Ver guía y catálogo materializado v5.31</strong></summary><div class="v6-depth-inner">{LEGACY_START}{legacy}{LEGACY_END}</div></details>
{HUB_END}'''


def patch_page(path: Path, surface: str, rendered: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_styles(text)
    text = mark_body(text, surface)
    main_match, current_main = extract_main(text)
    legacy = extract_legacy(current_main)
    # rendered se calcula de nuevo con legacy fuera de esta función; placeholder no se usa.
    raise RuntimeError("patch_page helper no debe invocarse directamente")


def main() -> int:
    growth_payload = load(GROWTH)
    cro_payload = load(CRO)
    growth_solutions = growth_payload.get("solutions", [])
    cro_solutions = cro_payload.get("solutions", [])
    if len(growth_solutions) != 6 or len(cro_solutions) != 6:
        raise RuntimeError("Wave 3 requiere exactamente 6 soluciones en Growth y 6 en CRO")
    growth_map = {item["slug"]: item for item in growth_solutions}
    cro_map = {item["slug"]: item for item in cro_solutions}
    if set(growth_map) != set(cro_map):
        raise RuntimeError("Growth y CRO no comparten los mismos seis slugs")

    for slug in sorted(growth_map):
        path = SOLUTIONS_DIR / f"{slug}.html"
        if not path.exists():
            raise RuntimeError(f"falta ruta materializada {path.name}")
        text = path.read_text(encoding="utf-8")
        text = ensure_styles(text)
        text = mark_body(text, f"solution:{slug}")
        main_match, current_main = extract_main(text)
        legacy = extract_legacy(current_main)
        new_main = f'<main id="contenido" data-experience-v60="solution:{e(slug)}">\n{render_solution(growth_map[slug], cro_map[slug], legacy)}\n</main>'
        text = text[:main_match.start()] + new_main + text[main_match.end():]
        path.write_text(text, encoding="utf-8")

    hub_path = SOLUTIONS_DIR / "index.html"
    text = hub_path.read_text(encoding="utf-8")
    text = ensure_styles(text)
    text = mark_body(text, "solutions-hub")
    main_match, current_main = extract_main(text)
    legacy = extract_legacy(current_main)
    new_main = f'<main id="contenido" data-experience-v60="solutions-hub">\n{render_hub(growth_solutions, cro_payload["hub"], legacy)}\n</main>'
    text = text[:main_match.start()] + new_main + text[main_match.end():]
    hub_path.write_text(text, encoding="utf-8")

    print("EXPERIENCE V6 WAVE 3 OK: 6 rutas + hub de soluciones materializados desde Growth/CRO; profundidad v5.31 preservada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

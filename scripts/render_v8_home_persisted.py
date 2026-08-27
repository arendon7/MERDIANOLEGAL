#!/usr/bin/env python3
"""Render the exact W5.0E future-root Home candidate without mutating index.html.

This renderer keeps v8 content/navigation while deliberately bridging the three
noindex pilot routes back to their certified legacy/indexable URLs. It also
materializes the future privacy-first contact intake. Publication remains a
separate E2 gate.
"""
from __future__ import annotations

from argparse import ArgumentParser
from copy import deepcopy
from html import escape
from pathlib import Path
import json
import sys

from render_v8_home import (
    render_contracts,
    render_evidence,
    render_external_direction,
    render_featured,
    render_final_cta,
    render_hero,
    render_insights,
    render_legal_intelligence,
    render_method,
    render_practices,
    render_sectors,
    render_situations,
)
from v8_shell import load_model, render_footer, render_header

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / ".w5-persisted/index.html"
CANONICAL_URL = "https://arendon7.github.io/MERDIANOLEGAL/"

PUBLIC_BRIDGES = {
    "PR02": "servicios/sociedades-gobierno-inversion.html",
    "SO07": "productos/sistema-contractual-empresarial.html",
    "RC01": "servicios/direccion-juridica-externa.html",
}


def e(value: object) -> str:
    return escape(str(value), quote=True)


def production_bridge_model(model: dict) -> dict:
    candidate = deepcopy(model)
    if candidate.get("status") != "candidate" or candidate.get("activation", {}).get("public"):
        raise ValueError("W5.0E requires candidate/non-public source model")
    observed: set[str] = set()
    for rows in candidate["navigation"]["mega_groups"].values():
        for row in rows:
            code = row[0]
            if code not in PUBLIC_BRIDGES:
                continue
            row[3] = PUBLIC_BRIDGES[code]
            row[4] = "legacy_bridge"
            observed.add(code)
    if observed != set(PUBLIC_BRIDGES):
        raise ValueError(f"persisted bridge set drifted: {sorted(observed)}")
    return candidate


def render_contact() -> str:
    return '''<section class="ml-section ml-home-contact" id="contacto" data-v8-home-contact="true" aria-labelledby="ml-contact-title">
  <div class="ml-container ml-home-contact-grid">
    <div class="ml-home-contact-copy">
      <p class="ml-eyebrow">PRESENTAR UNA NECESIDAD</p>
      <h2 id="ml-contact-title">Cuéntenos qué decisión necesita estructurar.</h2>
      <p class="ml-lead">La primera conversación busca entender contexto, urgencia, resultado esperado y la forma proporcional de intervenir. No envíe secretos empresariales, expedientes completos ni información sensible en este primer contacto.</p>
      <div class="ml-home-contact-facts" aria-label="Qué ocurre después">
        <span><b>01</b> Contexto y necesidad</span>
        <span><b>02</b> Alcance y siguiente paso</span>
        <span><b>03</b> Propuesta cuando corresponda</span>
      </div>
    </div>
    <form class="ml-home-contact-form" id="contact-form" data-v8-contact-form="true" novalidate>
      <label class="ml-hp" aria-hidden="true">Sitio web<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
      <div class="ml-form-grid">
        <label>Nombre<input type="text" name="name" autocomplete="name" maxlength="120" required></label>
        <label>Empresa<input type="text" name="company" autocomplete="organization" maxlength="160"></label>
        <label>Correo corporativo<input type="email" name="email" autocomplete="email" maxlength="180" required></label>
        <label>Necesidad<select name="need" required>
          <option value="">Seleccione</option>
          <option>Diagnóstico jurídico</option>
          <option>Dirección jurídica externa</option>
          <option>Contratos y negociaciones</option>
          <option>Socios, gobierno o inversión</option>
          <option>Marca, software o intangibles</option>
          <option>Gobernanza de IA</option>
          <option>Proyecto regulado</option>
          <option>Legal Operations</option>
          <option>Programa de cumplimiento digital</option>
          <option>Otra necesidad</option>
        </select></label>
        <label>Momento de decisión<select name="decision_stage" required>
          <option value="">Seleccione</option>
          <option>Necesito definir mejor el alcance</option>
          <option>Estoy comparando alternativas</option>
          <option>Quiero recibir una propuesta</option>
        </select></label>
        <label>Urgencia<select name="urgency" required>
          <option value="">Seleccione</option>
          <option>Esta semana</option>
          <option>En 2 a 4 semanas</option>
          <option>En 1 a 3 meses</option>
          <option>Sin fecha definida</option>
        </select></label>
        <label>Presupuesto orientativo<select name="budget">
          <option value="">Prefiero definirlo después</option>
          <option>Menos de COP 5 millones</option>
          <option>COP 5 a 15 millones</option>
          <option>COP 15 a 40 millones</option>
          <option>Más de COP 40 millones</option>
        </select></label>
        <label class="ml-form-wide">Contexto<textarea name="message" rows="5" maxlength="1600" placeholder="Describa brevemente la decisión, problema o resultado que necesita. No incluya información confidencial sensible."></textarea></label>
      </div>
      <label class="ml-form-consent"><input type="checkbox" name="privacy" required><span>He leído la <a href="privacidad.html">política de privacidad</a> y autorizo usar estos datos únicamente para gestionar este contacto.</span></label>
      <p class="ml-form-note">La web no crea automáticamente una relación abogado-cliente ni confirma aceptación del encargo. El envío final ocurre únicamente cuando usted confirma el mensaje en WhatsApp.</p>
      <div class="ml-actions"><button class="ml-btn" type="submit" data-v8-contact-submit>Abrir solicitud en WhatsApp</button></div>
      <p class="ml-form-status" data-v8-contact-status role="status" aria-live="polite"></p>
      <section class="ml-handoff" data-v8-handoff hidden aria-labelledby="ml-handoff-title">
        <p class="ml-eyebrow">HANDOFF PREPARADO</p>
        <h3 id="ml-handoff-title">Revise el mensaje antes de enviarlo.</h3>
        <p data-v8-handoff-copy>WhatsApp se abrió con un resumen preparado. Esta web no puede confirmar si el mensaje fue enviado, entregado o leído.</p>
        <div class="ml-actions">
          <button class="ml-btn ml-btn--secondary" type="button" data-v8-handoff-reopen>Volver a abrir WhatsApp</button>
          <button class="ml-btn ml-btn--secondary" type="button" data-v8-handoff-copy-button>Copiar resumen</button>
        </div>
      </section>
    </form>
  </div>
</section>'''


def render_document(source_model: dict) -> str:
    model = production_bridge_model(source_model)
    home = model["home"]
    sections = {
        "H01": render_hero(home, "#contacto"),
        "H02": render_situations(model, home, ""),
        "H03": render_featured(model, home, ""),
        "H04": render_contracts(model, home, ""),
        "H05": render_practices(model, home, ""),
        "H06": render_method(home),
        "H07": render_evidence(home, ""),
        "H08": render_external_direction(model, home, "", "#contacto"),
        "H09": render_sectors(home, ""),
        "H10": render_legal_intelligence(home, ""),
        "H11": render_insights(home, ""),
        "H12": render_final_cta(model, home, "", "#contacto"),
    }
    body = "\n".join(sections[item] for item in home["section_order"])
    schema = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["Organization", "LegalService"],
                "@id": f"{CANONICAL_URL}#organization",
                "name": "Meridiano Legal",
                "url": CANONICAL_URL,
                "description": "Firma jurídica empresarial que integra derecho, comprensión del negocio y tecnología aplicada.",
                "telephone": "+57 300 850 7813",
                "areaServed": {"@type": "Country", "name": "Colombia"},
                "address": {"@type": "PostalAddress", "addressLocality": "Medellín", "addressCountry": "CO"},
            },
            {
                "@type": "WebSite",
                "@id": f"{CANONICAL_URL}#website",
                "url": CANONICAL_URL,
                "name": "Meridiano Legal",
                "inLanguage": "es-CO",
                "publisher": {"@id": f"{CANONICAL_URL}#organization"},
            },
        ],
    }, ensure_ascii=False, separators=(",", ":"))
    return f'''<!doctype html>
<html lang="es-CO" data-v8-home-candidate="persisted">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="description" content="Meridiano Legal integra derecho empresarial, comprensión del negocio y tecnología aplicada para estructurar decisiones que necesitan avanzar.">
  <meta name="theme-color" content="#13263a">
  <meta property="og:site_name" content="Meridiano Legal">
  <meta property="og:locale" content="es_CO">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Meridiano Legal | Derecho empresarial para decisiones que necesitan avanzar">
  <meta property="og:description" content="Criterio jurídico, comprensión del negocio y tecnología aplicada para estructurar decisiones, contratos, gobierno y proyectos complejos.">
  <meta property="og:url" content="{CANONICAL_URL}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Meridiano Legal | Derecho empresarial para decisiones que necesitan avanzar">
  <meta name="twitter:description" content="Firma jurídica empresarial para decisiones, contratos, gobierno, tecnología y proyectos complejos.">
  <title>Meridiano Legal | Derecho empresarial para decisiones que necesitan avanzar</title>
  <link rel="canonical" href="{CANONICAL_URL}">
  <link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="manifest.webmanifest">
  <link rel="stylesheet" href="assets/css/v8/tokens.css">
  <link rel="stylesheet" href="assets/css/v8/base.css">
  <link rel="stylesheet" href="assets/css/v8/components.css">
  <link rel="stylesheet" href="assets/css/v8/surfaces.css">
  <link rel="stylesheet" href="assets/css/v8/home-persisted.css">
  <script type="application/ld+json">{schema}</script>
  <script defer src="runtime-config.js"></script>
  <script defer src="assets/js/v6/analytics-adapter-v61.js"></script>
  <script defer src="assets/js/v8/measurement.js"></script>
  <script defer src="assets/js/v8/navigation.js"></script>
  <script defer src="assets/js/v8/contact.js"></script>
</head>
<body class="ml-home-preview ml-home-persisted" data-experience-system="v8" data-page-type="home">
  <a class="ml-skip-link" href="#contenido">Saltar al contenido</a>
  {render_header(model, prefix="", contact_href="#contacto")}
  <main id="contenido" data-v8-home-shell="persisted-candidate">
    {body}
    {render_contact()}
  </main>
  {render_footer(model, prefix="", contact_href="#contacto")}
</body>
</html>
'''


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    model = load_model()
    html = render_document(model)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"RENDER V8 W5.0E PERSISTED HOME OK: {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"RENDER V8 W5.0E PERSISTED HOME FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

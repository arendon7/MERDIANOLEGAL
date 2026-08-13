#!/usr/bin/env python3
"""v5.22: integra narrativa de oferta, diferenciación de modalidad y lente jurídica."""
from __future__ import annotations

from html import escape
from pathlib import Path
import json
import re
import subprocess
import sys

R = Path(__file__).resolve().parents[1]
VERSION_PATH = R / "version.json"
CONTRACT_PATH = R / "offer-narrative-v522.json"
HOME = R / "index.html"
CSS_LINK_HOME = '<link rel="stylesheet" href="offer-v522.css">'
CSS_LINK_DEEP = '<link rel="stylesheet" href="../offer-v522.css">'
START = "<!-- OFFER-NARRATIVE-V522:START -->"
END = "<!-- OFFER-NARRATIVE-V522:END -->"
UNSAFE_PLATFORM_PHRASES = (
    "Meridiano Empresas o SharePoint/OneDrive",
    "Meridiano Empresas o Microsoft 365",
    "Meridiano Empresas o tablero acordado",
    "Meridiano Empresas o entorno disponible",
)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def load_contract() -> dict:
    payload = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    offers = payload.get("offers") or {}
    if payload.get("version") != "5.22.0" or len(offers) != 16:
        raise RuntimeError("offer-narrative-v522.json debe declarar versión 5.22.0 y exactamente 16 ofertas")
    return payload


def ensure_css(text: str, link: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(link) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("HTML sin </head> para cargar offer-v522.css")
    return text.replace("</head>", f"  {link}\n</head>", 1)


def remove_existing_block(text: str) -> str:
    pattern = re.compile(r"\s*" + re.escape(START) + r".*?" + re.escape(END) + r"\s*", re.S)
    return pattern.sub("\n", text, count=1)


def preserve_source_platform_copy(static_body: str, path: Path) -> str:
    """No reescribe contenido contractual después del render.

    Capability truth debe vivir en la fuente. Las menciones condicionales como
    "Meridiano Empresas cuando esté habilitado productivamente" y los enlaces
    marcados como demostración son válidos; las formulaciones ambiguas obligan
    a corregir el JSON fuente en lugar de mutarlo silenciosamente aquí.
    """
    for phrase in UNSAFE_PLATFORM_PHRASES:
        if phrase in static_body:
            raise RuntimeError(
                f"{path.relative_to(R)}: copy de plataforma ambiguo {phrase!r}; corríjalo en el catálogo fuente"
            )
    return static_body


def narrative_block(catalog_id: str, entry: dict) -> str:
    lens = "".join(
        f'<article><strong>{escape(title)}</strong><p>{escape(copy)}</p></article>'
        for title, copy in entry["legal_lens"]
    )
    alt = entry["alternative"]
    return f'''{START}
<section class="offer-positioning-v522" data-offer-narrative-v522="{escape(catalog_id)}" aria-labelledby="offer-positioning-v522-title-{escape(catalog_id)}">
  <div class="container">
    <div class="offer-positioning-head-v522">
      <p class="eyebrow">CRITERIO DE CONTRATACIÓN</p>
      <h2 id="offer-positioning-v522-title-{escape(catalog_id)}">Qué decisión compra la empresa y por qué esta modalidad.</h2>
      <p>Esta lectura no sustituye el alcance técnico de la ficha. Lo organiza para que dirección pueda distinguir el problema empresarial, la lógica de contratación y el criterio jurídico que gobierna el trabajo.</p>
    </div>
    <div class="offer-positioning-grid-v522">
      <article class="offer-positioning-card-v522"><span>01 · DECISIÓN EMPRESARIAL</span><h3>Qué debe poder decidir.</h3><p>{escape(entry["decision"])}</p></article>
      <article class="offer-positioning-card-v522"><span>02 · POR QUÉ ESTA MODALIDAD</span><h3>Qué justifica este tipo de intervención.</h3><p>{escape(entry["modality_reason"])}</p></article>
      <article class="offer-positioning-card-v522"><span>03 · CAPACIDAD QUE QUEDA INSTALADA</span><h3>Qué permanece administrable después del trabajo.</h3><p>{escape(entry["installed"])}</p></article>
    </div>
    <div class="offer-alternative-v522"><div><span>ALTERNATIVA CERCANA</span><strong>{escape(alt["label"])}</strong><p>{escape(alt["copy"])}</p></div><a href="{escape(alt["href"], quote=True)}">Comparar alternativa →</a></div>
    <details class="offer-legal-lens-v522">
      <summary><span>LENTE JURÍDICA</span> Ver regímenes y preguntas de control que orientan el análisis</summary>
      <div class="offer-legal-lens-grid-v522">{lens}</div>
    </details>
  </div>
</section>
{END}'''


def patch_deep_page(path: Path, offers: dict) -> str:
    text = path.read_text(encoding="utf-8")
    catalog_match = re.search(r'data-catalog-id="([^"]+)"', text)
    if not catalog_match:
        raise RuntimeError(f"{path.relative_to(R)}: falta data-catalog-id")
    catalog_id = catalog_match.group(1)
    if catalog_id not in offers:
        raise RuntimeError(f"{path.relative_to(R)}: falta contrato v5.22 para {catalog_id}")

    text = remove_existing_block(text)
    text = ensure_css(text, CSS_LINK_DEEP)

    body_pattern = re.compile(r'(<!-- STATIC-CATALOG-BODY:START -->)(.*?)(<!-- STATIC-CATALOG-BODY:END -->)', re.S)
    body_match = body_pattern.search(text)
    if not body_match:
        raise RuntimeError(f"{path.relative_to(R)}: falta STATIC-CATALOG-BODY")
    static_body = preserve_source_platform_copy(body_match.group(2), path)
    situations_anchor = '<section class="detail-section soft" aria-labelledby="situaciones-title">'
    if situations_anchor not in static_body:
        raise RuntimeError(f"{path.relative_to(R)}: falta ancla de situaciones para v5.22")
    block = narrative_block(catalog_id, offers[catalog_id])
    static_body = static_body.replace(situations_anchor, block + "\n" + situations_anchor, 1)
    text = text[: body_match.start(2)] + static_body + text[body_match.end(2) :]
    path.write_text(text, encoding="utf-8")
    return catalog_id


def normalize_once(text: str, old: str, new: str, label: str) -> str:
    new_count = text.count(new)
    old_count = text.count(old)
    if new_count == 1 and old_count == 0:
        return text
    if old_count == 1 and new_count == 0:
        return text.replace(old, new, 1)
    raise RuntimeError(
        f"index.html: {label} en estado inesperado; histórico={old_count}, v5.22={new_count}"
    )


def patch_home() -> None:
    text = HOME.read_text(encoding="utf-8")
    text = ensure_css(text, CSS_LINK_HOME)
    text, hero_count = re.subn(
        r'<section class="hero(?: home-narrative-v522)?"(?: data-home-narrative-v522="true")?>',
        '<section class="hero home-narrative-v522" data-home-narrative-v522="true">',
        text,
        count=1,
    )
    if hero_count != 1:
        raise RuntimeError("index.html: no se pudo normalizar la sección hero v5.22")

    text = normalize_once(
        text,
        '<h1>Dirección jurídica <em>para empresas que avanzan.</em></h1>',
        '<h1>Dirección jurídica <em>para decisiones que deben avanzar.</em></h1>',
        "hero H1",
    )
    text = normalize_once(
        text,
        '<p class="lead">Integramos criterio jurídico, lectura empresarial y seguimiento para convertir decisiones complejas en estructuras, documentos, responsables y rutas de implementación administrables.</p>',
        '<p class="lead">Integramos criterio jurídico, comprensión empresarial y tecnología aplicada para estructurar decisiones, proteger activos y convertir asuntos complejos en documentos, responsables y rutas de implementación administrables.</p>',
        "hero lead",
    )
    text = normalize_once(
        text,
        '<div class="hero-card"><strong>El trabajo jurídico debe ayudar a decidir y también poder ejecutarse.</strong><small>Contexto · riesgo · evidencia · implementación</small></div>',
        '<div class="hero-card"><strong>No entregamos respuestas aisladas: el criterio jurídico debe convertirse en decisiones, instrumentos y acciones verificables.</strong><small>Contexto · riesgo · alcance · evidencia · implementación</small></div>',
        "hero card",
    )
    text = normalize_once(
        text,
        '<h2 id="proof-router-v512-title">Elija la modalidad por el tipo de incertidumbre y por el resultado que necesita.</h2>\n      <p>La situación empresarial define qué debe resolverse; la modalidad define cómo conviene contratar el trabajo. No necesita recorrer varios selectores para llegar a la misma decisión.</p>',
        '<h2 id="proof-router-v512-title">Primero defina qué necesita resolver; después elija cómo conviene contratarlo.</h2>\n      <p>La necesidad define la decisión jurídica. La modalidad define la relación de trabajo: diagnóstico para delimitar, auditoría para revisar un perímetro cerrado, producto para instalar un resultado definido, servicio para adaptar criterio a hechos y actores, o acompañamiento para gobernar demanda recurrente.</p>',
        "selector de modalidad",
    )
    text = normalize_once(
        text,
        '<p class="eyebrow dark">ANTES DE CONTRATAR</p><h2>La prueba pública debe poder revisarse, no solo prometerse.</h2><p>Por eso la web expone alcance, método, límites, conocimiento sectorial y una demostración ficticia antes de pedir información confidencial.</p>',
        '<p class="eyebrow dark">CÓMO SE VE EL CRITERIO SENIOR</p><h2>La experiencia se demuestra en las preguntas, el alcance y la capacidad de ejecutar.</h2><p>Antes de contratar, revise si la propuesta identifica régimen, fuentes, supuestos, responsables, límites, entregables y cierre. El seniority no depende de adjetivos: debe poder leerse en cómo se estructura la decisión.</p>',
        "prueba pública",
    )
    text = normalize_once(
        text,
        '<p class="eyebrow dark">SERVICIOS PROFESIONALES</p><h2>Soluciones jurídicas conectadas con la empresa.</h2></div><p>Para asuntos complejos o a la medida que requieren análisis, negociación, implementación o coordinación profesional y no pueden reducirse a una plantilla.</p>',
        '<p class="eyebrow dark">SERVICIOS PROFESIONALES</p><h2>Intervenciones para hechos, actores y negociaciones que exigen criterio adaptable.</h2></div><p>Elija un servicio cuando la decisión está identificada, pero el alcance debe evolucionar con la evidencia, la negociación, la regulación o las actuaciones de terceros. Aquí el valor está en el juicio profesional aplicado al caso, no en forzar un paquete estándar.</p>',
        "intro servicios",
    )
    text = normalize_once(
        text,
        '<p class="eyebrow">PRODUCTOS DE ALCANCE CERRADO</p><h2>Resultados definidos, metodología y límites explícitos.</h2></div><p>Cada producto parte de una pregunta ejecutiva y termina en entregables verificables. Las fichas indican duración orientativa, exclusiones y relación con el servicio profesional correspondiente.</p>',
        '<p class="eyebrow">PRODUCTOS DE ALCANCE CERRADO</p><h2>Resultados jurídicos con perímetro, entregables y cierre definidos desde el inicio.</h2></div><p>Elija un producto cuando el problema permite fijar cantidades, método, responsables, formatos y aceptación antes de comenzar. La ficha muestra exactamente qué se instala y cuándo una necesidad exige pasar a un servicio a medida.</p>',
        "intro productos",
    )
    HOME.write_text(text, encoding="utf-8")


def validate_materialized_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(R / "scripts/validate_offer_narrative_v522.py")],
        cwd=R,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"v5.22 no supera validator editorial: {detail}")
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    version = json.loads(VERSION_PATH.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 22, 0):
        return 0
    contract = load_contract()
    offers = contract["offers"]
    target_paths = sorted((R / "servicios").glob("*.html")) + sorted((R / "productos").glob("*.html"))
    if len(target_paths) != 16:
        raise RuntimeError(f"v5.22 esperaba 16 fichas y encontró {len(target_paths)}")
    seen = {patch_deep_page(path, offers) for path in target_paths}
    if seen != set(offers):
        missing = sorted(set(offers) - seen)
        extra = sorted(seen - set(offers))
        raise RuntimeError(f"v5.22 desalineada con catálogo; faltan={missing}, extra={extra}")
    patch_home()
    validate_materialized_contract()
    print("OFFER NARRATIVE V5.22 OK: portada reconciliada + 16 ofertas diferenciadas con lente jurídica y alternativa explícita.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

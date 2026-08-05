#!/usr/bin/env python3
"""Valida continuidad de navegación, contexto explícito y SEO de fichas."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG_FILES = {
    "servicios/diagnostico-juridico-empresarial.html",
    "servicios/direccion-juridica-externa.html",
    "servicios/contratacion-estrategica.html",
    "servicios/sociedades-gobierno-inversion.html",
    "servicios/propiedad-intelectual.html",
    "servicios/tecnologia-inteligencia-artificial.html",
    "servicios/proyectos-regulados.html",
    "servicios/legal-operations.html",
    "productos/diagnostico-juridico-empresarial.html",
    "productos/empresa-juridicamente-organizada.html",
    "productos/activos-intangibles-protegidos.html",
    "productos/empresa-lista-para-inversion.html",
    "productos/programa-gobernanza-ia.html",
    "productos/proyecto-regulado-estructurado.html",
    "productos/sistema-contractual-empresarial.html",
    "productos/proteccion-datos-consumidor.html",
}

REQUIRED_FILES = {
    "page-context.js",
    "page-context.css",
    "catalog-home-v32.js",
    *CATALOG_FILES,
}

HTML_MARKERS = {
    "data-page-type=",
    "data-page-title=",
    "data-page-need=",
    "page-context.css",
    "page-context.js",
    "application/ld+json",
    "og:url",
    "twitter:card",
    "data-journey-bar",
    'aria-current="page"',
}

JS_MARKERS = {
    "meridiano.contactContext",
    "restoreContextIntoLocation",
    "meridiano-legalservice-schema",
    "rewriteContactLinks",
    "rewriteGeneratedActions",
    "window.MeridianoContext",
}

HOME_MARKERS = {
    "page-context.css",
    "page-context.js",
    "data-page-context",
    "dataset.contextLabel",
    "Web demostrativa v3.6.0",
}


def validate() -> list[str]:
    errors: list[str] = []
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    if missing:
        return [f"Faltan archivos de contexto y navegación: {', '.join(missing)}"]

    context_js = (ROOT / "page-context.js").read_text(encoding="utf-8")
    home_js = (ROOT / "catalog-home-v32.js").read_text(encoding="utf-8")
    context_css = (ROOT / "page-context.css").read_text(encoding="utf-8")

    for marker in sorted(JS_MARKERS):
        if marker not in context_js:
            errors.append(f"page-context.js no contiene {marker!r}")

    for marker in sorted(HOME_MARKERS):
        if marker not in home_js:
            errors.append(f"catalog-home-v32.js no contiene {marker!r}")

    for marker in (".journey-bar", ":focus-visible", ".full-detail-link", ".sector-deep-link"):
        if marker not in context_css:
            errors.append(f"page-context.css no contiene {marker!r}")

    for relative in sorted(CATALOG_FILES):
        text = (ROOT / relative).read_text(encoding="utf-8")
        for marker in sorted(HTML_MARKERS):
            if marker not in text:
                errors.append(f"{relative}: falta {marker!r}")
        if "?context=" not in text or "&amp;need=" not in text:
            errors.append(f"{relative}: el enlace de contacto no conserva contexto explícito")
        if text.count("application/ld+json") < 2:
            errors.append(f"{relative}: debe contener esquema principal y breadcrumb")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN DE CONTEXTO FALLIDA")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDACIÓN DE CONTEXTO OK: 16 fichas, navegación, contacto y datos estructurados íntegros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

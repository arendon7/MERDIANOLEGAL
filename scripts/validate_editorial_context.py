#!/usr/bin/env python3
"""Valida SEO, continuidad y navegación de firma, perspectivas y sectores."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

FIRM_PAGE = "firma.html"
ARTICLE_PAGES = {
    "perspectivas/gobierno-juridico-inteligencia-artificial.html",
    "perspectivas/contratos-administrables.html",
    "perspectivas/propiedad-intelectual-cadena-titularidad.html",
    "perspectivas/socios-inversion-gobierno.html",
    "perspectivas/proyectos-regulados-secuencia-viabilidad.html",
    "perspectivas/legal-operations-modelo-operativo.html",
}
SECTOR_PAGES = {
    "sectores/tecnologia-software-ia.html",
    "sectores/servicios-publicos-aseo-economia-circular.html",
    "sectores/agroindustria-fertilizantes-sostenibilidad.html",
    "sectores/salud-negocios-regulados.html",
    "sectores/comercio-distribucion.html",
    "sectores/startups-inversion.html",
    "sectores/proyectos-publicos-territoriales.html",
    "sectores/operaciones-juridicas.html",
}
ALL_PAGES = {FIRM_PAGE, *ARTICLE_PAGES, *SECTOR_PAGES}
COMMON_MARKERS = {
    "EDITORIAL-SEO:START",
    "EDITORIAL-JOURNEY:START",
    "EDITORIAL-SEQUENCE:START",
    "EDITORIAL-SCRIPT:START",
    'property="og:url"',
    'name="twitter:card"',
    "page-context.css",
    "page-context.js",
    "BreadcrumbList",
    "data-page-type=",
    "data-page-title=",
    "data-page-need=",
    "editorial-journey",
    "editorial-sequence",
    "context=",
    "need=",
}


def validate() -> list[str]:
    errors: list[str] = []
    required_files = {
        "scripts/enrich_editorial_pages.py",
        "scripts/validate_editorial_context.py",
        ".github/workflows/enrich-editorial.yml",
        "page-context.css",
        "page-context.js",
        *ALL_PAGES,
    }
    missing = sorted(path for path in required_files if not (ROOT / path).exists())
    if missing:
        errors.append(f"Faltan archivos editoriales: {', '.join(missing)}")
        return errors

    for path in sorted(ALL_PAGES):
        text = (ROOT / path).read_text(encoding="utf-8")
        for marker in sorted(COMMON_MARKERS):
            if marker not in text:
                errors.append(f"{path}: falta {marker!r}")
        if path in ARTICLE_PAGES:
            for marker in ('"@type":"Article"', 'name="author"', "article:published_time", "article:modified_time", '"author":{"@type":"Person"'):
                if marker not in text:
                    errors.append(f"{path}: falta el marcador editorial {marker!r}")
        elif path in SECTOR_PAGES:
            for marker in ('"@type":"WebPage"', '"about":{"@type":"Thing"'):
                if marker not in text:
                    errors.append(f"{path}: falta el marcador sectorial {marker!r}")
        else:
            for marker in ('"@type":"AboutPage"', '"@type":"LegalService"', '"@type":"Person"'):
                if marker not in text:
                    errors.append(f"{path}: falta el marcador institucional {marker!r}")

    css = (ROOT / "page-context.css").read_text(encoding="utf-8")
    for marker in (".editorial-sequence", ".editorial-journey", ":focus-visible"):
        if marker not in css:
            errors.append(f"page-context.css no contiene {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN EDITORIAL FALLIDA")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDACIÓN EDITORIAL OK: firma, 6 perspectivas y 8 sectores con contexto, SEO y navegación íntegros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

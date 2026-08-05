#!/usr/bin/env python3
"""Valida el selector guiado, el contacto contextual y su integración en portada."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "decision-flow.js",
    "decision-flow.css",
    "page-context.js",
    "page-context.css",
    "catalog-home-v32.js",
}

FLOW_MARKERS = {
    "selector-guiado-meridiano",
    "solution-guide-form",
    "recommendationFor",
    "pageContextFromLocation",
    "applyContactContext",
    "nav-mobile-utility",
    "decision-flow.css",
}

LOADER_MARKERS = {
    "decision-flow.js",
    "data-decision-flow",
    "page-context.js",
    "data-page-context",
    "Web demostrativa v3.6.0",
}

RECOMMENDED_ROUTES = {
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
    "productos/sistema-contractual-empresarial.html",
    "productos/empresa-lista-para-inversion.html",
    "productos/activos-intangibles-protegidos.html",
    "productos/programa-gobernanza-ia.html",
    "productos/proyecto-regulado-estructurado.html",
    "productos/proteccion-datos-consumidor.html",
}


def validate() -> list[str]:
    errors: list[str] = []
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    if missing:
        return [f"Faltan archivos del flujo de decisión: {', '.join(missing)}"]

    flow_text = (ROOT / "decision-flow.js").read_text(encoding="utf-8")
    loader_text = (ROOT / "catalog-home-v32.js").read_text(encoding="utf-8")
    css_text = (ROOT / "decision-flow.css").read_text(encoding="utf-8")

    missing_flow = sorted(marker for marker in FLOW_MARKERS if marker not in flow_text)
    if missing_flow:
        errors.append(f"decision-flow.js está incompleto; faltan: {', '.join(missing_flow)}")

    missing_loader = sorted(marker for marker in LOADER_MARKERS if marker not in loader_text)
    if missing_loader:
        errors.append(f"catalog-home-v32.js no carga correctamente el flujo; faltan: {', '.join(missing_loader)}")

    missing_routes = sorted(route for route in RECOMMENDED_ROUTES if route not in flow_text)
    if missing_routes:
        errors.append(f"El selector perdió rutas recomendadas: {', '.join(missing_routes)}")

    for marker in (".solution-guide-section", ".contact-context", ".main-nav.open", ".nav-mobile-utility"):
        if marker not in css_text:
            errors.append(f"decision-flow.css no contiene {marker}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN DEL FLUJO FALLIDA")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDACIÓN DEL FLUJO OK: selector, rutas, contexto y navegación móvil íntegros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

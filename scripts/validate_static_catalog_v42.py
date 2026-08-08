#!/usr/bin/env python3
"""Valida que las 16 fichas sean legibles, indexables y útiles sin JavaScript."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PAGES = {
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


class ContentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1 = 0
        self.h2 = 0
        self.h3 = 0
        self.sections = 0
        self.aria_sections = 0
        self.text: list[str] = []
        self._ignored = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag in {"script", "style"}:
            self._ignored += 1
        if tag == "h1":
            self.h1 += 1
        elif tag == "h2":
            self.h2 += 1
        elif tag == "h3":
            self.h3 += 1
        elif tag == "section" and "detail-section" in values.get("class", "").split():
            self.sections += 1
            if values.get("aria-labelledby"):
                self.aria_sections += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._ignored:
            self._ignored -= 1

    def handle_data(self, data: str) -> None:
        if not self._ignored and data.strip():
            self.text.append(data.strip())


def validate() -> list[str]:
    errors: list[str] = []
    required_files = {
        "catalog-page.js",
        "catalog-v32.js",
        "scripts/render_catalog_static.mjs",
        "scripts/render_services_v42.mjs",
        "catalog-services-v42/s01-diagnostico.json",
        "catalog-services-v42/s02-direccion.json",
        "catalog-services-v42/s03-contratos.json",
        "catalog-services-v42/s04-societario.json",
        "catalog-services-v42/s05-intangibles.json",
        "catalog-services-v42/s06-tecnologia-ia.json",
        "catalog-services-v42/s07-regulados.json",
        "catalog-services-v42/s08-legal-ops.json",
        "catalog-products-v41/p01-auditoria.json",
        "catalog-products-v41/p02-organizada.json",
        "catalog-products-v41/p03-intangibles.json",
        "catalog-products-v41/p04-inversion.json",
        "catalog-products-v41/p05-ia.json",
        "catalog-products-v41/p06-regulado.json",
        "catalog-products-v41/p07-contractual.json",
        "catalog-products-v41/p08-datos-consumidor.json",
        *CATALOG_PAGES,
    }
    missing = sorted(name for name in required_files if not (ROOT / name).exists())
    if missing:
        return [f"Faltan archivos del catálogo estático: {', '.join(missing)}"]

    for relative in sorted(CATALOG_PAGES):
        text = (ROOT / relative).read_text(encoding="utf-8")
        parser = ContentParser()
        parser.feed(text)
        words = re.findall(r"\b[\wáéíóúüñÁÉÍÓÚÜÑ]+\b", " ".join(parser.text), flags=re.UNICODE)

        required = {
            "STATIC-CATALOG-HERO:START",
            "STATIC-CATALOG-BODY:START",
            'data-static-catalog="true"',
            'id="pregunta-title"',
            'id="resultado-title"',
            'id="situaciones-title"',
            'id="alcance-title"',
            'id="perimetro-title"',
            'id="metodo-title"',
            'id="entregables-title"',
            'id="formatos-title"',
            'id="cronograma-title"',
            'id="requisitos-title"',
            'id="responsabilidades-title"',
            'id="aceptacion-title"',
            'id="limites-title"',
            'id="relacionadas-title"',
            'id="contacto-title"',
            '<script defer src="../catalog-page.js"></script>',
            '<script defer src="../page-context.js"></script>',
            'name="twitter:title"',
            'name="twitter:description"',
            'property="og:site_name"',
        }
        for marker in sorted(required):
            if marker not in text:
                errors.append(f"{relative}: falta {marker!r}")

        if '<script src="../catalog-v32.js"></script>' in text:
            errors.append(f"{relative}: todavía descarga el catálogo completo en el navegador")
        if '<div class="container detail-hero-grid" id="detail-hero-content"></div>' in text:
            errors.append(f"{relative}: el hero sigue dependiendo de JavaScript")
        if '<main id="contenido"><div id="detail-page"></div></main>' in text:
            errors.append(f"{relative}: el cuerpo sigue dependiendo de JavaScript")
        if parser.h1 != 1:
            errors.append(f"{relative}: debe contener exactamente un h1 y contiene {parser.h1}")

        expected_sections = 15
        minimum_h2 = 15
        minimum_h3 = 24
        minimum_words = 950
        if parser.h2 < minimum_h2:
            errors.append(f"{relative}: debe contener al menos {minimum_h2} h2 y contiene {parser.h2}")
        if parser.h3 < minimum_h3:
            errors.append(f"{relative}: debe contener al menos {minimum_h3} h3 y contiene {parser.h3}")
        if parser.sections != expected_sections or parser.aria_sections != parser.sections:
            errors.append(f"{relative}: las {expected_sections} secciones editoriales deben usar aria-labelledby")
        if len(words) < minimum_words:
            errors.append(f"{relative}: contenido estático insuficiente ({len(words)} palabras)")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN DEL CATÁLOGO ESTÁTICO FALLIDA")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDACIÓN DEL CATÁLOGO ESTÁTICO OK: 8 servicios v4.2 y 8 productos v4.1 con 15 secciones, indexables y funcionales sin JavaScript.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

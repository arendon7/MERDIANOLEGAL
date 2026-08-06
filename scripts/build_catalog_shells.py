#!/usr/bin/env python3
"""Genera las 16 fichas públicas desde una plantilla canónica y metadatos únicos."""

from __future__ import annotations

from html import escape
import json
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://arendon7.github.io/MERDIANOLEGAL/"

PAGES = [
    ("servicios/diagnostico-juridico-empresarial.html", "service-diagnostic", "service", "Diagnóstico Jurídico Empresarial", "Diagnóstico Jurídico Empresarial de Meridiano Legal: alcance, método, entregables, requisitos y límites para priorizar la exposición jurídica de una empresa.", "Diagnóstico jurídico"),
    ("servicios/direccion-juridica-externa.html", "service-direction", "service", "Dirección Jurídica Externa", "Dirección Jurídica Externa de Meridiano Legal: gobierno jurídico recurrente, priorización, seguimiento y memoria institucional para empresas.", "Dirección jurídica externa"),
    ("servicios/contratacion-estrategica.html", "service-contracts", "service", "Contratación Estratégica y Gestión Contractual", "Servicio de contratación estratégica de Meridiano Legal: estructuración, revisión, negociación y administración de obligaciones contractuales.", "Contratos y negociaciones"),
    ("servicios/sociedades-gobierno-inversion.html", "service-corporate", "service", "Sociedades, Gobierno e Inversión", "Servicio societario de Meridiano Legal para capital, gobierno corporativo, acuerdos entre socios, inversión, formalización y salida.", "Socios, gobierno o inversión"),
    ("servicios/propiedad-intelectual.html", "service-ip", "service", "Propiedad Intelectual y Activos Intangibles", "Servicio de propiedad intelectual de Meridiano Legal para marcas, software, titularidad, licencias, secretos empresariales y activos digitales.", "Marca, software o intangibles"),
    ("servicios/tecnologia-inteligencia-artificial.html", "service-ai", "service", "Gobernanza Jurídica de Tecnología e Inteligencia Artificial", "Servicio de gobernanza jurídica de tecnología e inteligencia artificial: casos de uso, datos, proveedores, contratos, controles y supervisión.", "Gobernanza de IA"),
    ("servicios/proyectos-regulados.html", "service-regulated", "service", "Estructuración Jurídica de Proyectos Regulados", "Servicio de Meridiano Legal para viabilidad, autoridades, permisos, actores, contratos y condiciones de avance en proyectos regulados.", "Proyecto regulado"),
    ("servicios/legal-operations.html", "service-ops", "service", "Legal Operations y Transformación de la Función Jurídica", "Servicio de Legal Operations de Meridiano Legal para procesos, solicitudes, documentos, obligaciones, métricas, tecnología y gestión del cambio.", "Legal Operations"),
    ("productos/diagnostico-juridico-empresarial.html", "product-diagnostic", "product", "Diagnóstico Jurídico Empresarial", "Producto jurídico de alcance cerrado para identificar, priorizar y convertir exposiciones jurídicas en un plan ejecutivo de 90 días.", "Diagnóstico jurídico"),
    ("productos/empresa-juridicamente-organizada.html", "product-organized", "product", "Empresa Jurídicamente Organizada", "Producto de Meridiano Legal para ordenar gobierno, atribuciones, contratos, obligaciones y documentación esencial de la empresa.", "Diagnóstico jurídico"),
    ("productos/activos-intangibles-protegidos.html", "product-assets", "product", "Marca, Software y Activos Intangibles Protegidos", "Producto jurídico para inventariar, regularizar y proteger marcas, software, contenidos, licencias y otros activos intangibles.", "Marca, software o intangibles"),
    ("productos/empresa-lista-para-inversion.html", "product-investment", "product", "Empresa Lista para Inversión", "Producto jurídico para preparar gobierno, capital, activos, contratos, contingencias y data room antes de una inversión.", "Socios, gobierno o inversión"),
    ("productos/programa-gobernanza-ia.html", "product-ai", "product", "Programa de Gobernanza de IA", "Programa de Meridiano Legal para inventariar casos de uso de IA, clasificar riesgos y definir roles, controles e incidentes.", "Gobernanza de IA"),
    ("productos/proyecto-regulado-estructurado.html", "product-regulated", "product", "Proyecto Regulado Estructurado", "Producto jurídico para definir viabilidad, autoridades, permisos, actores, contratos y condiciones precedentes de un proyecto regulado.", "Proyecto regulado"),
    ("productos/sistema-contractual-empresarial.html", "product-contract-system", "product", "Sistema Contractual Empresarial", "Producto jurídico para convertir contratos aislados en criterios, modelos, aprobaciones, obligaciones y seguimiento administrable.", "Contratos y negociaciones"),
    ("productos/proteccion-datos-consumidor.html", "product-data-consumer", "product", "Programa de Protección de Datos y Consumidor", "Programa jurídico para convertir políticas de datos y consumidor en procesos, responsables, evidencias y respuestas consistentes.", "Legal Operations"),
]


def json_ld(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def render(path: str, catalog_id: str, page_type: str, title: str, description: str, need: str) -> str:
    is_service = page_type == "service"
    kind = "Servicio profesional" if is_service else "Producto jurídico"
    section = "Servicios" if is_service else "Productos"
    anchor = "servicios" if is_service else "productos"
    schema_type = "Service" if is_service else "Product"
    canonical = f"{BASE_URL}{path}"
    context_label = f"{kind}: {title}"
    contact = escape(f"../index.html?{urlencode({'context': context_label, 'need': need})}#contacto", quote=True)

    schema = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "name": title,
        "description": description,
        "url": canonical,
        "provider": {
            "@type": "LegalService",
            "name": "Meridiano Legal",
            "url": BASE_URL,
            "areaServed": "Colombia",
        },
        "category": kind,
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE_URL},
            {"@type": "ListItem", "position": 2, "name": section, "item": f"{BASE_URL}#{anchor}"},
            {"@type": "ListItem", "position": 3, "name": title, "item": canonical},
        ],
    }

    return f'''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#13263a">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="{escape(title, quote=True)} | Meridiano Legal">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="../assets/images/global/home-hero.webp">
  <meta name="twitter:card" content="summary_large_image">
  <title>{escape(title)} | Meridiano Legal</title>
  <link rel="canonical" href="{canonical}">
  <link rel="icon" href="../assets/brand/meridiano-logo-horizontal-dark.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../catalog-v32.css">
  <link rel="stylesheet" href="../page-context.css">
  <script type="application/ld+json">{json_ld(schema)}</script>
  <script type="application/ld+json">{json_ld(breadcrumb)}</script>
</head>
<body data-catalog-id="{catalog_id}" data-page-type="{kind}" data-page-title="{escape(title, quote=True)}" data-page-need="{escape(need, quote=True)}">
  <a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="detail-header">
    <div class="container detail-header-inner">
      <a class="detail-brand" href="../index.html" aria-label="Meridiano Legal, inicio"><img src="../assets/brand/meridiano-logo-horizontal-dark.svg" alt="Meridiano Legal"></a>
      <button class="detail-menu" type="button" aria-expanded="false" aria-controls="detail-nav" aria-label="Abrir menú"><span></span><span></span><span></span></button>
      <nav class="detail-nav" id="detail-nav" aria-label="Navegación principal"><a href="../index.html#servicios">Servicios</a><a href="../index.html#productos">Productos</a><a href="../index.html#sectores">Sectores</a><a href="../perspectivas.html">Perspectivas</a><a href="../experiencia.html">Centro demo</a><a href="{contact}">Contacto</a></nav>
      <div class="detail-header-actions"><a class="btn btn-outline" href="../index.html#{anchor}">Portafolio</a><a class="btn btn-navy" href="../demo.html">Área de clientes</a></div>
    </div>
  </header>
  <div class="journey-bar" data-journey-bar><div class="container"><span>{kind}</span><strong>{escape(title)}</strong><div><a href="../index.html#{anchor}">Volver al portafolio</a><a href="{contact}">Presentar esta necesidad →</a></div></div></div>
  <section class="detail-hero"><div class="container detail-breadcrumb" aria-label="Ruta de navegación"><a href="../index.html">Inicio</a> · <a href="../index.html#{anchor}">{section}</a> · <span aria-current="page">{escape(title)}</span></div><div class="container detail-hero-grid" id="detail-hero-content"></div></section>
  <main id="contenido"><div id="detail-page"></div></main>
  <div class="detail-disclaimer"><div class="container">Información general y demostrativa. La ficha no constituye asesoría jurídica ni propuesta vinculante.</div></div>
  <footer class="detail-footer">
    <div class="container detail-footer-grid"><div><img src="../assets/brand/meridiano-logo-horizontal-light.svg" alt="Meridiano Legal"><p>Dirección jurídica para empresas, innovación y proyectos regulados.</p></div><div><strong>Oferta</strong><a href="../index.html#servicios">Servicios</a><a href="../index.html#productos">Productos</a><a href="../index.html#planes">Planes</a></div><div><strong>Experiencia</strong><a href="../index.html#sectores">Sectores</a><a href="../perspectivas.html">Perspectivas</a><a href="../experiencia.html">Centro demo</a><a href="../demo.html">Meridiano Empresas</a></div><div><strong>Información</strong><a href="../privacidad.html">Privacidad</a><a href="../terminos.html">Términos</a><a href="../aviso-legal.html">Aviso legal</a></div></div>
    <div class="container detail-footer-bottom"><span>© <span id="year"></span> Meridiano Legal</span><span>Medellín, Colombia</span><span>Ficha v3.6</span></div>
  </footer>
  <div class="floating-detail"><a href="https://wa.me/573008507813" target="_blank" rel="noopener noreferrer" aria-label="Contactar por WhatsApp">W</a><button type="button" data-top aria-label="Volver arriba">↑</button></div>
  <script src="../catalog-v32.js"></script>
  <script src="../page-context.js"></script>
</body>
</html>
'''


def main() -> None:
    for page in PAGES:
        path = ROOT / page[0]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(*page), encoding="utf-8")
    print(f"Generadas {len(PAGES)} fichas canónicas.")


if __name__ == "__main__":
    main()

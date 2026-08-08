# Meridiano Legal · Web canónica v4.1.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.1 consolida el catálogo comercial-jurídico de los ocho productos de alcance cerrado. Cada producto incorpora perímetro cuantificado, método, entregables, formatos, cronograma, requisitos, responsabilidades, criterios de aceptación, límites, complementos y soluciones relacionadas. Los ocho servicios profesionales permanecen preservados en su última versión pública aprobada y serán objeto de un ciclo editorial dedicado posterior, sin degradar la v4.1.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa controles, despliegue y actualización automática de `stable`.
- Si una validación falla, GitHub Pages conserva la última versión aprobada.
- No se usan ramas ordinarias, pull requests temporales ni copias con nombres `final`, `nuevo` o sufijos de versión.

## Arquitectura pública

- Portada comercial con selector guiado y contacto contextual.
- Página institucional de la firma y su método.
- 8 servicios profesionales y 8 productos jurídicos con HTML estático.
- 8 páginas sectoriales y 6 perspectivas jurídicas.
- 5 planes recurrentes, 6 documentos guiados, centro demo y portal demostrativo.
- Páginas legales, sitemap, robots, manifiesto y página 404.

## Catálogo comercial-jurídico v4.1

- `catalog-products-v41/`: ocho definiciones de producto con alcance comercial y jurídico detallado.
- `catalog-home-v32.js`: navegación y presentación resumida del portafolio desde la portada.
- `catalog-v32.js`: catálogo público compatible con las fichas y servicios preservados.
- `scripts/build_catalog_shells.py`: genera únicamente las fichas de producto en esta release y preserva los servicios hasta su ciclo dedicado.
- `scripts/render_catalog_static.mjs`: prerenderiza el contenido sustantivo hacia HTML semántico.
- `scripts/validate_static_catalog.py`: controla que el contenido aprobado permanezca disponible sin depender de JavaScript.

## Identidad visual canónica

La base visual vigente procede de la v3.9 y continúa siendo la identidad canónica de la v4.1:

- `assets/brand/meridiano-logo-horizontal-dark.svg`: logotipo para fondos claros.
- `assets/brand/meridiano-logo-horizontal-light.svg`: logotipo para fondos oscuros.
- `assets/brand/meridiano-monogram.svg`: monograma M sobrio.
- `assets/brand/favicon.svg`: favicon e icono PWA.
- `assets/images/global/home-hero.webp`: hero fotográfico optimizado.
- `visual-v39.css`: reglas visuales comunes, recortes y tratamiento responsive.
- `visual-v39.js`: selección automática de variantes de marca y mejora progresiva del hero.
- `scripts/apply_visual_assets.py`: aplicación idempotente de la identidad en páginas raíz y profundas.
- `scripts/validate_visual_assets.py`: control de archivos, cabecera WebP, rutas, versión y ausencia de logotipos legados.

La marca utiliza la M arquitectónica en azul marino, dos filetes dorados y el descriptor “Derecho, Empresa y Tecnología”. Se descartaron brújulas, globos, balanzas, escudos y variaciones generadas inconsistentes como sistema principal.

## Archivos funcionales canónicos

- `index.html`, `site-v3.css`, `clarity-v31.css` y `site-v3.js`: portada.
- `catalog-home-v32.js`: enlaces entre portada, fichas, sectores y perspectivas.
- `decision-flow.js` y `decision-flow.css`: selector, formulario contextual y menú móvil.
- `page-context.js` y `page-context.css`: continuidad, autoría, revisión editorial y CTA contextuales.
- `catalog-v32.js`: catálogo público de las 16 fichas y compatibilidad con los servicios preservados.
- `catalog-v32.css` y `catalog-page.js`: presentación y controlador ligero de fichas.
- `catalog-products-v41/`: fuente editorial modular de los ocho productos v4.1.
- `scripts/build_catalog_shells.py`: plantilla, metadatos y generación de fichas de producto.
- `scripts/render_catalog_static.mjs`: prerender del catálogo hacia HTML semántico.
- `scripts/enrich_editorial_pages.py`: SEO, breadcrumbs y navegación editorial.
- `scripts/sync_public_version.py`: sincronización de etiquetas con `version.json`.

## Construcción canónica

El workflow `.github/workflows/build-canonical.yml` ejecuta, en orden:

```bash
python3 scripts/build_catalog_shells.py
node scripts/render_catalog_static.mjs
python3 scripts/enrich_editorial_pages.py
python3 scripts/sync_public_version.py
python3 scripts/apply_visual_assets.py
```

La capa visual se aplica después de los generadores funcionales. El aplicador elimina cualquier copia previa de sus etiquetas y las reinserta en una única posición canónica, de modo que ejecuciones sucesivas producen exactamente el mismo HTML.

## Accesibilidad y rendimiento

- contenido jurídico disponible sin JavaScript;
- un único `h1` y secciones editoriales identificadas;
- soporte de `prefers-reduced-motion`;
- cierre del menú con `Escape` y recuperación de foco;
- `content-visibility` para diferir contenido inferior;
- hero WebP con dimensiones, texto alternativo y prioridad alta;
- favicon y manifiesto alineados con la marca vigente;
- estilos de impresión y foco visible compartido.

## Validación

```bash
python3 scripts/build_catalog_shells.py
node scripts/render_catalog_static.mjs
python3 scripts/enrich_editorial_pages.py
python3 scripts/sync_public_version.py
python3 scripts/apply_visual_assets.py
python3 scripts/validate_site.py
python3 scripts/validate_static_catalog.py
python3 scripts/validate_decision_flow.py
python3 scripts/validate_page_context.py
python3 scripts/validate_editorial_context.py
python3 scripts/validate_visual_assets.py
node --check site-v3.js
node --check catalog-v32.js
node --check catalog-page.js
node --check catalog-home-v32.js
node --check decision-flow.js
node --check page-context.js
node --check experiencia.js
node --check demo.js
node --check visual-v39.js
python3 -m json.tool manifest.webmanifest
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` comprueba la idempotencia de los generadores y despliega únicamente después de aprobar todas las verificaciones.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- La firma: `https://arendon7.github.io/MERDIANOLEGAL/firma.html`
- Perspectivas: `https://arendon7.github.io/MERDIANOLEGAL/perspectivas.html`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

## Límites

La versión publicada es demostrativa. No autentica usuarios reales, no almacena expedientes, no recibe archivos y no debe utilizarse para transmitir información confidencial o datos personales sensibles.

La biblioteca visual temática completa se incorporará por grupos funcionales, conservando una imagen maestra por ubicación y variantes derivadas para escritorio, móvil y Open Graph. El historial funcional se conserva en `CHANGELOG.md`.
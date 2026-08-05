# Meridiano Legal · Web canónica v3.7.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa controles, despliegue y actualización automática de `stable`.
- Si una validación falla, GitHub Pages conserva la última versión aprobada.
- No se usan ramas ordinarias, pull requests temporales ni copias con nombres `final`, `nuevo` o sufijos de versión.

## Arquitectura pública

- Portada comercial con selector guiado y contacto contextual.
- Página institucional de la firma y su método.
- 8 servicios profesionales con ficha profunda.
- 8 productos jurídicos de alcance cerrado.
- 8 páginas sectoriales.
- Biblioteca con 6 perspectivas jurídicas.
- 5 planes recurrentes y 6 documentos guiados.
- Centro de demostración y portal demostrativo por perfiles.
- Páginas legales, sitemap, robots, manifiesto y página 404.

## Archivos canónicos

- `index.html`, `site-v3.css`, `clarity-v31.css` y `site-v3.js`: portada.
- `catalog-home-v32.js`: enlaces entre portada, fichas, sectores y perspectivas.
- `decision-flow.js` y `decision-flow.css`: selector, formulario contextual y menú móvil.
- `page-context.js` y `page-context.css`: continuidad, autoría, revisión editorial, foco y CTA contextuales.
- `catalog-v32.js` y `catalog-v32.css`: contenido y presentación de las fichas.
- `scripts/build_catalog_shells.py`: plantilla y metadatos de las 16 fichas.
- `scripts/enrich_editorial_pages.py`: SEO, breadcrumbs y navegación de firma, perspectivas y sectores.
- `scripts/sync_public_version.py`: sincronización de etiquetas visibles con `version.json`.
- `sectores/`, `perspectivas/`, `servicios/` y `productos/`: páginas públicas profundas.

## Construcción canónica

La construcción pública se concentra en un único workflow:

`.github/workflows/build-canonical.yml`

Este ejecuta, en orden:

```bash
python3 scripts/build_catalog_shells.py
python3 scripts/enrich_editorial_pages.py
python3 scripts/sync_public_version.py
```

Cuando detecta diferencias, confirma todos los archivos derivados en un solo commit. Esto evita workflows paralelos, divergencias entre páginas y actualizaciones manuales repetitivas.

Las fichas incorporan:

- metadatos sociales;
- canonical y descripción específica;
- esquema `Service` o `Product`;
- breadcrumb estructurado;
- contexto explícito hacia contacto;
- barra de continuidad del recorrido.

La firma, las perspectivas y los sectores incorporan:

- esquemas `AboutPage`, `Article` o `WebPage` según el caso;
- autoría y fecha editorial cuando corresponde;
- Open Graph y Twitter Card;
- breadcrumbs estructurados;
- navegación anterior y siguiente;
- CTA con necesidad preseleccionada.

## Validación

```bash
python3 scripts/build_catalog_shells.py
python3 scripts/enrich_editorial_pages.py
python3 scripts/sync_public_version.py
python3 scripts/validate_site.py
python3 scripts/validate_decision_flow.py
python3 scripts/validate_page_context.py
python3 scripts/validate_editorial_context.py
node --check site-v3.js
node --check catalog-v32.js
node --check catalog-home-v32.js
node --check decision-flow.js
node --check page-context.js
node --check experiencia.js
node --check demo.js
python3 -m json.tool manifest.webmanifest
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` comprueba que los generadores sean idempotentes y despliega únicamente después de aprobar todas las verificaciones.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- La firma: `https://arendon7.github.io/MERDIANOLEGAL/firma.html`
- Perspectivas: `https://arendon7.github.io/MERDIANOLEGAL/perspectivas.html`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

## Límites

La versión publicada es demostrativa. No autentica usuarios reales, no almacena expedientes, no recibe archivos y no debe utilizarse para transmitir información confidencial o datos personales sensibles.

El historial funcional se conserva exclusivamente en `CHANGELOG.md`.

# Meridiano Legal · Web canónica v4.2.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.2 completa la profundización comercial-jurídica del portafolio público. Conserva íntegramente los ocho productos v4.1 y eleva los ocho servicios profesionales al mismo estándar de claridad: resultado empresarial, arquitectura jurídica, perímetro de referencia, método, entregables, formatos, cronograma, requisitos, responsabilidades, criterios de aceptación, límites, extensiones y continuidad.

Los servicios mantienen su naturaleza profesional y adaptable. Las cantidades publicadas funcionan como perímetros de referencia comercial y deben confirmarse en cada propuesta según materialidad, volumen, actores, urgencia y especialidades aplicables.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa construcción canónica, controles, despliegue y actualización automática de `stable`.
- Si una validación falla, GitHub Pages conserva la última versión aprobada.
- No se usan ramas ordinarias, pull requests temporales ni copias con nombres `final`, `nuevo` o sufijos de versión.

## Arquitectura pública

- Portada comercial con selector guiado y contacto contextual.
- Página institucional de la firma y su método.
- 8 servicios profesionales v4.2 y 8 productos jurídicos v4.1 con HTML estático.
- 8 páginas sectoriales y 6 perspectivas jurídicas.
- 5 planes recurrentes, 6 documentos guiados, centro demo y portal demostrativo.
- Páginas legales, sitemap, robots, manifiesto y página 404.

## Catálogo comercial-jurídico

- `catalog-products-v41/`: ocho definiciones modulares de producto con alcance cerrado y cuantificado.
- `catalog-services-v42/`: ocho definiciones modulares de servicio con profundidad jurídica y perímetros comerciales de referencia.
- `catalog-v32.js`: base histórica y compatibilidad del catálogo.
- `catalog-home-v32.js`: navegación y presentación resumida del portafolio desde la portada.
- `scripts/render_catalog_static.mjs`: prerender de los productos v4.1.
- `scripts/render_services_v42.mjs`: prerender dedicado de los servicios v4.2.
- `scripts/validate_static_catalog.py`: impide regresiones hacia fichas superficiales, vacías o dependientes de JavaScript.

## Estándar editorial v4.2

Cada servicio publica quince bloques sustantivos: pregunta ejecutiva, resultado empresarial, situaciones de uso, arquitectura del servicio, perímetro de referencia, método, entregables, formatos, cronograma, requisitos, responsabilidades, criterios de aceptación, límites, extensiones/continuidad y contacto contextual.

La estructura busca resolver cuatro preguntas antes de una conversación comercial: qué problema se atiende, qué puede incluir el servicio, qué recibe la empresa y dónde termina el alcance. Esto evita presentar la asesoría como disponibilidad abierta o como una lista genérica de materias jurídicas.

## Identidad visual canónica

La base visual vigente procede de la v3.9 y continúa siendo la identidad canónica de la v4.2:

- `assets/brand/meridiano-logo-horizontal-dark.svg`: logotipo para fondos claros.
- `assets/brand/meridiano-logo-horizontal-light.svg`: logotipo para fondos oscuros.
- `assets/brand/meridiano-monogram.svg`: monograma M sobrio.
- `assets/brand/favicon.svg`: favicon e icono PWA.
- `assets/images/global/home-hero.webp`: hero fotográfico optimizado.
- `visual-v39.css`: reglas visuales comunes, recortes y tratamiento responsive.
- `visual-v39.js`: selección automática de variantes de marca y mejora progresiva del hero.
- `scripts/apply_visual_assets.py`: aplicación idempotente de la identidad.
- `scripts/validate_visual_assets.py`: control de archivos, rutas y ausencia de logotipos legados.

## Construcción canónica

El workflow `.github/workflows/build-canonical.yml` ejecuta, en orden:

```bash
python3 scripts/build_catalog_shells.py
node scripts/render_catalog_static.mjs
node scripts/render_services_v42.mjs
python3 scripts/enrich_editorial_pages.py
python3 scripts/sync_public_version.py
python3 scripts/apply_visual_assets.py
```

La separación de renderers preserva la release de productos v4.1 y permite evolucionar los servicios v4.2 sin reescribir la capa anterior. La construcción completa debe ser idempotente: ejecutarla nuevamente sobre los mismos archivos no puede producir diferencias.

## Accesibilidad y rendimiento

- contenido jurídico disponible sin JavaScript;
- un único `h1` y quince secciones editoriales identificadas por ficha;
- soporte de `prefers-reduced-motion`;
- cierre del menú con `Escape` y recuperación de foco;
- `content-visibility` para diferir contenido inferior;
- hero WebP con dimensiones, texto alternativo y prioridad alta;
- estilos de impresión y foco visible compartido.

## Validación

```bash
python3 scripts/build_catalog_shells.py
node scripts/render_catalog_static.mjs
node scripts/render_services_v42.mjs
python3 scripts/enrich_editorial_pages.py
python3 scripts/sync_public_version.py
python3 scripts/apply_visual_assets.py
python3 scripts/validate_site.py
python3 scripts/validate_static_catalog.py
python3 scripts/validate_decision_flow.py
python3 scripts/validate_page_context.py
python3 scripts/validate_editorial_context.py
python3 scripts/validate_visual_assets.py
node --check scripts/render_catalog_static.mjs
node --check scripts/render_services_v42.mjs
python3 -m json.tool version.json
```

El workflow `.github/workflows/pages.yml` verifica idempotencia, HTML y recursos, profundidad del catálogo, navegación, datos estructurados, identidad visual, JavaScript y metadatos antes de desplegar.

## Accesos

- Web pública: `https://arendon7.github.io/MERDIANOLEGAL/`
- La firma: `https://arendon7.github.io/MERDIANOLEGAL/firma.html`
- Perspectivas: `https://arendon7.github.io/MERDIANOLEGAL/perspectivas.html`
- Centro de demostración: `https://arendon7.github.io/MERDIANOLEGAL/experiencia.html`
- Portal demostrativo: `https://arendon7.github.io/MERDIANOLEGAL/demo.html`

## Límites

La versión publicada es demostrativa. No autentica usuarios reales, no almacena expedientes, no recibe archivos y no debe utilizarse para transmitir información confidencial o datos personales sensibles.

El historial funcional se conserva en `CHANGELOG.md` y en el historial de commits del repositorio.
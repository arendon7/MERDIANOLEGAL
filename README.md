# Meridiano Legal · Web canónica v4.8.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.8 cierra el ciclo de calidad pública iniciado con la arquitectura comercial de v4.1–v4.4, la reorganización de portada v4.5, la experiencia de fichas v4.6 y la unificación editorial/demostrativa v4.7.

El foco de esta release no es añadir más contenido jurídico, sino asegurar que el estado correcto de la web exista desde el primer HTML servido. La portada deja de depender de JavaScript para corregir el hero, los nombres del catálogo o las rutas profundas; servicios, productos, sectores, perspectivas y necesidades principales son navegables de forma nativa y JavaScript queda reservado para mejora progresiva.

La release añade además un cierre de SEO técnico, accesibilidad, rendimiento y control de indexación: metadatos sociales y schema.org en portada, `lang="es-CO"`, preload del hero WebP, semántica `aria-pressed` para filtros, navegación móvil mejorada, `noindex,nofollow` para el portal ficticio y `lastmod` actualizado en sitemap.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio funcional de fuente activa la construcción canónica.
- GitHub Pages solo publica después de aprobar idempotencia y toda la batería de validadores.
- Si una validación falla, Pages conserva la última versión aprobada y `stable` no se mueve.
- La construcción pública es reproducible: un segundo ciclo completo debe producir diff cero.

## Arquitectura pública

- Portada comercial v4.8 con seis rutas nativas por necesidad, selector guiado, ocho servicios, ocho productos, cinco planes, ocho sectores, perspectivas, honorarios, contratación, firma y contacto.
- Hero fotográfico WebP disponible desde el HTML inicial, sin sustitución posterior por JavaScript.
- Página institucional de la firma con método, principios, dirección y ocho rutas sectoriales.
- 8 servicios profesionales v4.2 y 8 productos jurídicos v4.1 con contenido jurídico estático profundo y UX/UI v4.6.
- 8 páginas sectoriales con recorrido por enfoque, decisiones, riesgos y siguiente paso.
- 6 perspectivas jurídicas únicas, índice de lectura, relaciones y conversión contextual.
- Centro de Demostración con recorrido, entregables, caso integral, simulador y conexión con Meridiano Empresas.
- Meridiano Empresas con tres perfiles ficticios y nueve módulos demostrativos; el portal se declara expresamente `noindex,nofollow`.
- Páginas legales, sitemap, robots, manifiesto y página 404.

## Catálogo comercial-jurídico

- `catalog-products-v41/`: ocho productos de alcance cerrado y cuantificado.
- `catalog-services-v42/`: ocho servicios profesionales con perímetros comerciales y jurídicos de referencia.
- `scripts/render_catalog_static.mjs`: prerender de productos.
- `scripts/render_services_v42.mjs`: prerender de servicios.
- `scripts/validate_static_catalog.py`: protege las 16 fichas frente a regresiones superficiales o dependencias de JavaScript.

Cada ficha mantiene quince bloques sustantivos: pregunta ejecutiva, resultado empresarial, situaciones de uso, alcance, perímetro, método, entregables, formatos, cronograma, requisitos, responsabilidades, aceptación, límites, continuidad y contacto contextual.

## Portada static-first v4.8

`scripts/apply_quality_v48.py` consolida el estado público correcto directamente en `index.html`:

- seis tarjetas de necesidad son enlaces nativos y no botones dependientes de un `routeMap`;
- “Mi operación jurídica” conduce a `servicios/legal-operations.html`, evitando la asociación previa con el Sistema Contractual Empresarial;
- ocho servicios y ocho productos publican su enlace profundo en HTML;
- los ocho productos muestran desde el primer render sus nombres y resúmenes canónicos;
- los ocho sectores son navegables directamente y utilizan la taxonomía sectorial vigente;
- las tres perspectivas destacadas, la biblioteca y la página de la firma tienen enlaces estáticos;
- el hero canónico es `assets/images/global/home-hero.webp` desde el documento inicial;
- el footer publica el año sin depender de JavaScript.

`catalog-home-v32.js` y `site-v3.js` permanecen como mejora progresiva para modales, filtros, contexto y navegación; ya no son necesarios para descubrir el contenido principal.

## SEO, indexación y metadata

La portada publica:

- `lang="es-CO"`;
- canonical URL;
- Open Graph con sitio, locale, URL e imagen;
- Twitter Card de imagen grande;
- JSON-LD con `Organization`/`LegalService` y `WebSite`;
- `robots=index,follow,max-image-preview:large`;
- preload del hero WebP con prioridad alta.

`sitemap.xml` utiliza la fecha de release como `lastmod` de las páginas públicas vigentes. `demo.html`, al ser un entorno ficticio para demostración y no una página de captación o contenido indexable, permanece fuera del sitemap y declara `noindex,nofollow` en el propio documento.

## Accesibilidad y rendimiento

`quality-v48.css`, `site-v3.js` y la capa static-first incorporan:

- filtros de producto como grupo de botones con `aria-pressed`, en lugar de semántica de tabs impropia;
- actualización del `aria-label` del menú entre “Abrir menú” y “Cerrar menú”;
- cierre por `Escape` con retorno de foco al control de menú;
- bloqueo de scroll del documento cuando el menú móvil está abierto;
- foco visible reforzado en rutas y enlaces profundos;
- objetivos táctiles mínimos en acciones móviles;
- respeto a `prefers-reduced-motion` también en desplazamientos programáticos;
- hero con dimensiones declaradas, `loading="eager"`, `decoding="async"` y `fetchpriority="high"` para mejorar estabilidad y LCP.

## UX/UI acumulada

### Portada v4.5

`ux-v45.css` y `scripts/apply_ux_v45.py` organizan la narrativa comercial, reducen duplicaciones, simplifican la navegación y presentan la oferta de forma secuencial.

### Fichas profundas v4.6

`detail-v46.css`, `detail-v46.js` y `scripts/apply_detail_ux_v46.py` gobiernan la experiencia de las 16 fichas: cabecera compacta, índice ejecutivo, jerarquía editorial, panel de límites, CTA contextual y lectura completa sin JavaScript.

### Editorial, sectores y demos v4.7

`editorial-v47.css`, `editorial-v47.js` y `scripts/apply_editorial_ux_v47.py` extienden navegación móvil, progreso de lectura, recorridos sectoriales, cierres de conversión y orientación demostrativa a Firma, Perspectivas, Sectores, Centro Demo y Meridiano Empresas.

`scripts/normalize_editorial_v47.py` mantiene deterministas las 18 salidas administradas por v4.7.

### Calidad final v4.8

- `quality-v48.css`: capa final de accesibilidad y comportamiento responsive.
- `scripts/apply_quality_v48.py`: estado static-first, rutas, metadata, sitemap y control de indexación.
- `scripts/normalize_quality_v48.py`: normalización determinista de whitespace y residuos ARIA administrados por la capa.
- `scripts/validate_quality_v48.py`: control específico de static-first, SEO, accesibilidad, indexación, sitemap, rutas y sintaxis.

## Identidad visual canónica

La identidad permanece basada en la M arquitectónica sobria de Meridiano Legal, con azul marino, marfil y dorado:

- `assets/brand/meridiano-logo-horizontal-dark.svg`
- `assets/brand/meridiano-logo-horizontal-light.svg`
- `assets/brand/meridiano-monogram.svg`
- `assets/brand/favicon.svg`
- `assets/images/global/home-hero.webp`
- `visual-v39.css` y `visual-v39.js`

La v4.8 no reabre el sistema de marca; únicamente garantiza que los activos correctos estén presentes desde el HTML inicial.

## Construcción canónica

El workflow `.github/workflows/build-canonical.yml` ejecuta, en orden:

```bash
python3 scripts/build_catalog_shells.py
node scripts/render_catalog_static.mjs
node scripts/render_services_v42.mjs
python3 scripts/enrich_editorial_pages.py
python3 scripts/apply_commercial_v43.py
python3 scripts/apply_visual_assets.py
python3 scripts/apply_ux_v45.py
python3 scripts/apply_detail_ux_v46.py
python3 scripts/apply_editorial_ux_v47.py
python3 scripts/normalize_editorial_v47.py
python3 scripts/apply_quality_v48.py
python3 scripts/normalize_quality_v48.py
python3 scripts/sync_public_version.py
```

`pages.yml` repite la secuencia y exige diff cero antes de ejecutar:

- integridad HTML, rutas, IDs, anchors y recursos;
- catálogo estático de 16 fichas;
- conversión comercial v4.4;
- UX de portada v4.5;
- UX de fichas v4.6;
- editorial y demos v4.7;
- calidad final v4.8;
- selector guiado;
- contexto y datos estructurados;
- firma, perspectivas y sectores;
- sistema visual;
- sintaxis JavaScript;
- metadatos JSON.

Durante el cierre v4.8, las barreras automáticas bloquearon el despliegue ante tres incompatibilidades sucesivas: whitespace acumulativo del bloque SEO, una expectativa sectorial legada en `validate_site.py` y una referencia defensiva a `aria-selected`. En los tres casos se corrigió la fuente o el validador para expresar el estado canónico más fuerte; no se desactivó ni relajó el control. La ejecución final obtuvo idempotencia y toda la matriz de calidad en verde antes de publicar.

## Desarrollo local

Puede abrirse `index.html` directamente para una revisión básica. Para reproducir el comportamiento más cercano a GitHub Pages, se recomienda servir el repositorio con un servidor estático y ejecutar previamente la secuencia canónica de construcción.

## Publicación

GitHub Pages publica únicamente después de que `Site Quality and Deploy` aprueba todos los controles. Al finalizar correctamente, `stable` se mueve al mismo commit desplegado en `main`.

# Meridiano Legal · Web canónica v4.7.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.7 completa la unificación de experiencia pública iniciada en la portada v4.5 y extendida a las 16 fichas profundas en v4.6. La nueva capa se aplica a la página de la firma, la biblioteca y las seis perspectivas, los ocho sectores, el Centro de Demostración y Meridiano Empresas.

El cambio es de UX/UI, continuidad y conversión. El contenido jurídico, editorial y demostrativo previo se conserva; la nueva capa mejora navegación móvil, lectura de páginas largas, conexión entre contenidos y oferta, rutas sectoriales y orientación dentro de los entornos demostrativos.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa construcción canónica, controles, despliegue y actualización automática de `stable`.
- Si una validación falla, GitHub Pages conserva la última versión aprobada.
- La construcción pública es reproducible e idempotente; un segundo ciclo sobre las mismas fuentes debe producir diff cero.

## Arquitectura pública

- Portada comercial v4.5 con navegación simplificada, selector guiado, precios, mockup de Meridiano Empresas y contacto contextual.
- Página institucional de la firma con método, principios, dirección y ocho rutas sectoriales navegables.
- 8 servicios profesionales v4.2 y 8 productos jurídicos v4.1 con contenido estático profundo y UX/UI v4.6.
- Navegación ejecutiva en las 16 fichas: decisión, alcance, entregables, implementación, límites y siguiente paso.
- 8 páginas sectoriales con recorrido rápido por enfoque, decisiones, riesgos y siguiente paso.
- 6 perspectivas jurídicas únicas, sin duplicación entre destacadas y biblioteca, con índice de lectura y conversión contextual.
- 5 planes recurrentes con capacidad y límites definidos y referencias públicas de honorarios.
- Centro de Demostración con recorrido, entregables, caso integral, simulador y conexión con Meridiano Empresas.
- Meridiano Empresas con tres perfiles ficticios y nueve módulos demostrativos.
- Páginas legales, sitemap, robots, manifiesto y página 404.

## Catálogo comercial-jurídico

- `catalog-products-v41/`: ocho definiciones modulares de producto con alcance cerrado y cuantificado.
- `catalog-services-v42/`: ocho definiciones modulares de servicio con profundidad jurídica y perímetros comerciales de referencia.
- `catalog-v32.js`: base histórica y compatibilidad del catálogo.
- `catalog-home-v32.js`: navegación contextual desde la portada.
- `scripts/render_catalog_static.mjs`: prerender de los productos v4.1.
- `scripts/render_services_v42.mjs`: prerender dedicado de los servicios v4.2.
- `scripts/validate_static_catalog.py`: impide regresiones hacia fichas superficiales, vacías o dependientes de JavaScript.

Cada ficha mantiene quince bloques sustantivos: pregunta ejecutiva, resultado empresarial, situaciones de uso, alcance, perímetro, método, entregables, formatos, cronograma, requisitos, responsabilidades, aceptación, límites, extensiones/continuidad y contacto contextual.

## Sistema comercial

La portada distingue cuatro modalidades: orientación focal, servicio profesional, producto de alcance cerrado y plan recurrente. Los planes publican capacidades y referencias mensuales; las referencias de honorarios se presentan como precios o rangos sujetos a perímetro, volumen, complejidad, urgencia, especialidades, IVA, tasas y terceros cuando corresponda.

El proceso de contratación deja expresos necesidad, calificación, propuesta, aceptación e inicio. Una conversación preliminar no constituye por sí sola un mandato profesional abierto.

## UX/UI de portada v4.5

`ux-v45.css` y `scripts/apply_ux_v45.py` controlan la arquitectura final de la portada: menú principal reducido, navegación y CTA móvil, evidencia concreta de la oferta, eliminación de bloques redundantes, resumen de entregables, mockup demostrativo y orden narrativo validado automáticamente.

## UX/UI de fichas v4.6

`detail-v46.css`, `detail-v46.js` y `scripts/apply_detail_ux_v46.py` aplican una capa única a las 16 fichas de servicios y productos sin modificar el contenido jurídico sustantivo.

Incluye cabecera compacta, hero de menor densidad, índice sticky de seis hitos, resaltado de sección activa, jerarquía editorial, panel de límites, CTA móvil contextual, soporte de reducción de movimiento e impresión, y lectura completa sin JavaScript.

`scripts/validate_detail_ux_v46.py` exige exactamente 16 fichas profundas, una sola carga de la capa, seis hitos de navegación, CTA, responsive y versión pública correctos.

## UX/UI editorial, sectorial y demostrativa v4.7

`editorial-v47.css`, `editorial-v47.js` y `scripts/apply_editorial_ux_v47.py` extienden una capa progresiva a 18 páginas: Firma, Biblioteca de Perspectivas, seis perspectivas, ocho sectores, Centro Demo y Meridiano Empresas.

La capa incorpora:

- menú móvil accesible en páginas institucionales, editoriales y sectoriales;
- barra de progreso de lectura y resaltado de navegación activa;
- corrección del offset entre cabeceras sticky y barra de continuidad;
- CTA contextual persistente en móvil;
- ocho enlaces sectoriales directos desde la página de la firma;
- biblioteca de seis perspectivas únicas, sin repetir las tres lecturas destacadas;
- cierre de conversión en cada perspectiva;
- recorrido sectorial rápido por enfoque, decisiones, riesgos y siguiente paso;
- franja de confianza en Centro Demo sobre datos ficticios, procesamiento local y ausencia de cargas sensibles;
- cierre comercial entre recorrido demostrativo y alcance profesional;
- guía de uso de Meridiano Empresas y continuidad móvil entre portal, centro demo y web pública.

`scripts/normalize_editorial_v47.py` normaliza exclusivamente whitespace de las 18 salidas administradas por la capa. Se añadió después de que el control de idempotencia detectara acumulación de líneas vacías: el despliegue fue bloqueado, la normalización se hizo determinista y el ciclo completo volvió a ejecutarse hasta obtener diff cero.

`scripts/validate_editorial_ux_v47.py` verifica conteos, recursos, navegación, CTA, rutas sectoriales, perspectivas únicas, recorridos internos, módulos demo y sintaxis JavaScript sin depender de paquetes Python externos.

## Identidad visual canónica

La identidad continúa basada en la M arquitectónica sobria de Meridiano Legal, con azul marino, marfil y dorado:

- `assets/brand/meridiano-logo-horizontal-dark.svg`: logotipo para fondos claros.
- `assets/brand/meridiano-logo-horizontal-light.svg`: logotipo para fondos oscuros.
- `assets/brand/meridiano-monogram.svg`: monograma M.
- `assets/brand/favicon.svg`: favicon e icono PWA.
- `assets/images/global/home-hero.webp`: hero fotográfico optimizado.
- `visual-v39.css` y `visual-v39.js`: capa visual compartida.
- `scripts/apply_visual_assets.py`: aplicación idempotente de la identidad.
- `scripts/validate_visual_assets.py`: control de archivos, rutas y ausencia de logotipos legados.

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
python3 scripts/sync_public_version.py
```

`pages.yml` repite la secuencia y exige diff cero antes de validar HTML, rutas, catálogo estático, conversión comercial, portada v4.5, fichas v4.6, capa editorial/demos v4.7, flujo guiado, contexto, capa editorial histórica, sistema visual, JavaScript y metadatos.

## Accesibilidad y rendimiento

- contenido jurídico profundo disponible sin JavaScript en servicios y productos;
- menús móviles con cierre por `Escape` y foco visible;
- progreso de lectura e indicadores activos como mejora progresiva;
- soporte de `prefers-reduced-motion`;
- navegación horizontal desplazable en fichas, sectores y portal demo cuando corresponde;
- CTA móvil persistente;
- `content-visibility` en secciones inferiores de fichas profundas;
- activos locales y ausencia de dependencias externas para la operación básica de la web pública.

## Desarrollo local

Puede abrirse `index.html` directamente para una revisión básica. Para reproducir el comportamiento más cercano a GitHub Pages se recomienda servir el directorio con un servidor estático local y ejecutar antes la secuencia canónica de construcción.

## Publicación

GitHub Pages publica únicamente después de que el workflow `Site Quality and Deploy` aprueba todos los controles. Al finalizar correctamente, `stable` se mueve al mismo commit desplegado en `main`.

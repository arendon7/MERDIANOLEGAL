# Meridiano Legal · Web canónica v4.6.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.6 extiende a las 16 fichas profundas la arquitectura de experiencia consolidada en la portada v4.5. Conserva íntegramente los ocho productos jurídicos v4.1 y los ocho servicios profesionales v4.2, así como planes, honorarios, contratación, sectores, perspectivas y contenido jurídico previamente aprobado.

El cambio es de UX/UI y conversión: servicios y productos ahora comparten una navegación ejecutiva más corta, hero y cabecera de menor densidad, un índice sticky de seis hitos, jerarquía editorial más clara, CTA contextual y una experiencia móvil coherente con la portada. El contenido jurídico continúa disponible en HTML estático y no depende de JavaScript para poder leerse.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa construcción canónica, controles, despliegue y actualización automática de `stable`.
- Si una validación falla, GitHub Pages conserva la última versión aprobada.
- No se usan ramas ordinarias, pull requests temporales ni copias con nombres `final`, `nuevo` o sufijos de versión.

## Arquitectura pública

- Portada comercial v4.5 con navegación simplificada, selector guiado, precios, mockup de Meridiano Empresas y contacto contextual.
- Página institucional de la firma y su método.
- 8 servicios profesionales v4.2 y 8 productos jurídicos v4.1 con contenido estático profundo y UX/UI v4.6.
- Navegación ejecutiva en las 16 fichas: decisión, alcance, entregables, implementación, límites y siguiente paso.
- 8 páginas sectoriales y 6 perspectivas jurídicas.
- 5 planes recurrentes con capacidad y límites definidos.
- Referencias públicas de honorarios y documentos guiados.
- Centro demo y portal demostrativo Meridiano Empresas.
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

`ux-v45.css` y `scripts/apply_ux_v45.py` controlan la arquitectura final de la portada:

- menú principal reducido y CTA visible;
- navegación móvil y CTA persistente;
- evidencia concreta de la oferta: 8 servicios, 8 productos, 5 planes y 8 sectores;
- eliminación de bloques redundantes;
- resumen de entregables en cuatro resultados operativos;
- mockup demostrativo de Meridiano Empresas;
- orden narrativo validado automáticamente.

## UX/UI de fichas v4.6

`detail-v46.css`, `detail-v46.js` y `scripts/apply_detail_ux_v46.py` aplican una capa única a las 16 fichas de servicios y productos, después de sus renderers jurídicos. La capa no modifica el contenido sustantivo.

Incluye:

- cabecera compacta y navegación alineada con la portada;
- hero con menor altura y metadatos más escaneables;
- índice sticky con seis hitos: decisión, alcance, entregables, implementación, límites y siguiente paso;
- resaltado progresivo de la sección activa mediante `IntersectionObserver`;
- re-vinculación del índice cuando un producto se mejora dinámicamente, mediante `MutationObserver`;
- encabezados editoriales de dos columnas y menor densidad vertical;
- tarjetas, método, relaciones y límites con jerarquía visual más clara;
- panel de límites sticky en escritorio;
- CTA móvil persistente con mensaje contextual de WhatsApp;
- soporte de `prefers-reduced-motion` e impresión;
- lectura completa del contenido jurídico sin JavaScript.

`scripts/validate_detail_ux_v46.py` exige que las 16 fichas carguen la capa exactamente una vez, con navegación, anclas, CTA, versión y recursos correctos. Durante la implementación, el control de idempotencia detectó una alteración de espacios alrededor de los bloques gestionados; el aplicador fue corregido para preservar exactamente el HTML de las capas anteriores, sin relajar la validación.

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
python3 scripts/sync_public_version.py
```

La construcción completa debe ser idempotente: ejecutarla nuevamente sobre los mismos archivos no puede producir diferencias. `pages.yml` valida HTML, rutas, catálogo estático, conversión comercial, UX/UI de portada, UX/UI de fichas profundas, flujo guiado, contexto, capa editorial, sistema visual, JavaScript y metadatos antes de publicar.

## Accesibilidad y rendimiento

- contenido jurídico profundo disponible sin JavaScript en servicios y productos;
- selector, resaltado activo y mejoras de navegación como mejora progresiva;
- soporte de `prefers-reduced-motion`;
- cierre de menús con `Escape` y foco visible para teclado;
- navegación profunda horizontal desplazable en pantallas intermedias;
- CTA móvil persistente;
- `content-visibility` en secciones inferiores;
- activos locales y ausencia de dependencias externas para la operación básica de la web pública.

## Desarrollo local

Puede abrirse `index.html` directamente para una revisión básica. Para reproducir el comportamiento más cercano a GitHub Pages se recomienda servir el directorio con un servidor estático local y ejecutar antes la secuencia canónica de construcción.

## Publicación

GitHub Pages publica únicamente después de que el workflow `Site Quality and Deploy` aprueba todos los controles. Al finalizar correctamente, `stable` se mueve al mismo commit desplegado en `main`.

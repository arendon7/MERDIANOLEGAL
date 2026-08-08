# Meridiano Legal · Web canónica v4.5.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.5 consolida la arquitectura comercial construida entre v4.1 y v4.4 y simplifica de manera transversal la experiencia de la portada. Conserva íntegramente los ocho productos jurídicos v4.1 y los ocho servicios profesionales v4.2, mantiene los cinco planes recurrentes y las referencias de honorarios v4.3, y preserva el flujo de conversión y contratación v4.4.

El cambio principal es de UX/UI: la portada deja de repetir modalidades, criterios de encaje y rutas de trabajo en múltiples bloques. El recorrido público sigue ahora una secuencia más corta: necesidad, modalidad, servicios, productos, entregables, demostración, planes y precios, contratación, sectores, perspectivas, firma, preguntas frecuentes y contacto.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit validado y desplegado correctamente.
- Cada cambio en `main` activa construcción canónica, controles, despliegue y actualización automática de `stable`.
- Si una validación falla, GitHub Pages conserva la última versión aprobada.
- No se usan ramas ordinarias, pull requests temporales ni copias con nombres `final`, `nuevo` o sufijos de versión.

## Arquitectura pública

- Portada comercial v4.5 con navegación simplificada, selector guiado, precios, mockup de Meridiano Empresas y contacto contextual.
- Página institucional de la firma y su método.
- 8 servicios profesionales v4.2 y 8 productos jurídicos v4.1 con HTML estático profundo.
- 8 páginas sectoriales y 6 perspectivas jurídicas.
- 5 planes recurrentes con capacidad y límites definidos.
- Referencias públicas de honorarios y documentos guiados.
- Centro demo y portal demostrativo Meridiano Empresas.
- Páginas legales, sitemap, robots, manifiesto y página 404.

## Catálogo comercial-jurídico

- `catalog-products-v41/`: ocho definiciones modulares de producto con alcance cerrado y cuantificado.
- `catalog-services-v42/`: ocho definiciones modulares de servicio con profundidad jurídica y perímetros comerciales de referencia.
- `catalog-v32.js`: base histórica y compatibilidad del catálogo.
- `catalog-home-v32.js`: navegación contextual hacia fichas profundas, sectores, perspectivas y flujo guiado.
- `scripts/render_catalog_static.mjs`: prerender de los productos v4.1.
- `scripts/render_services_v42.mjs`: prerender dedicado de los servicios v4.2.
- `scripts/validate_static_catalog.py`: impide regresiones hacia fichas superficiales, vacías o dependientes de JavaScript.

## Sistema comercial

La portada distingue cuatro modalidades:

- orientación focal para preguntas concretas;
- servicio profesional para asuntos complejos o a medida;
- producto de alcance cerrado para resultados delimitables;
- plan recurrente para capacidad jurídica continua.

Los planes publican capacidades y referencias mensuales. Las referencias de honorarios sirven para orientar una primera decisión y se presentan como precios o rangos sujetos al perímetro, volumen, complejidad, urgencia, especialidades, IVA, tasas y terceros cuando corresponda.

El proceso de contratación deja expresos necesidad, calificación, propuesta, aceptación e inicio. Una conversación preliminar no constituye por sí sola un mandato profesional abierto.

## UX/UI v4.5

La capa `ux-v45.css` y `scripts/apply_ux_v45.py` aplican la arquitectura de portada posterior a las capas comercial y visual. Entre sus controles se encuentran:

- menú principal reducido y CTA de contacto visible;
- navegación móvil con acceso a demo, clientes y contacto;
- franja superior con evidencia concreta de la oferta: 8 servicios, 8 productos, 5 planes y 8 sectores;
- eliminación de bloques redundantes de modalidades, capacidades estratégicas, documentos, encaje y ruta duplicada;
- resumen de entregables en cuatro resultados operativos;
- mockup demostrativo de Meridiano Empresas sin datos reales;
- planes redistribuidos para mejorar legibilidad en escritorio;
- CTA persistente en móvil;
- foco visible y reducción de densidad vertical;
- orden narrativo validado automáticamente.

`scripts/validate_ux_v45.py` impide que regresen los bloques eliminados, las inyecciones dinámicas que saturaban el menú o un orden de secciones distinto del canónico.

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
python3 scripts/sync_public_version.py
```

La construcción completa debe ser idempotente: ejecutarla nuevamente sobre los mismos archivos no puede producir diferencias. `pages.yml` valida HTML, rutas, catálogo estático, conversión comercial, UX/UI, flujo guiado, contexto, capa editorial, sistema visual, JavaScript y metadatos antes de publicar.

## Accesibilidad y rendimiento

- contenido jurídico profundo disponible sin JavaScript en servicios y productos;
- selector y mejoras de navegación como mejora progresiva;
- soporte de `prefers-reduced-motion`;
- cierre del menú con `Escape`;
- foco visible para teclado;
- navegación móvil desplazable y CTA persistente;
- hero WebP optimizado y activos locales;
- ausencia de dependencias externas para la operación básica de la web pública.

## Desarrollo local

Puede abrirse `index.html` directamente para una revisión básica. Para reproducir el comportamiento más cercano a GitHub Pages se recomienda servir el directorio con un servidor estático local y ejecutar antes la secuencia canónica de construcción.

## Publicación

GitHub Pages publica únicamente después de que el workflow `Site Quality and Deploy` aprueba todos los controles. Al finalizar correctamente, `stable` se mueve al mismo commit desplegado en `main`.
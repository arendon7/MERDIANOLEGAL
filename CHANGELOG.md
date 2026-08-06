# Historial de versiones

## v3.9.0 — 2026-08-05

### Identidad visual canónica

- Se sustituyó la identidad angular y la brújula como sistema principal por una M arquitectónica sobria, con azul marino, marfil y dos filetes dorados.
- Se crearon variantes SVG para fondos claros y oscuros, monograma y favicon.
- Encabezados, pies, páginas profundas, centro demo y portal utilizan la misma familia de marca.
- El manifiesto PWA y el favicon quedaron alineados con la identidad vigente.

### Base fotográfica y experiencia

- La portada utiliza un hero WebP optimizado, con contexto empresarial de Medellín, dimensiones declaradas, texto alternativo y prioridad alta.
- `visual-v39.css` concentra el tratamiento de recortes, superposiciones, contraste, responsive y reducción de movimiento.
- `visual-v39.js` selecciona las variantes de marca según el nivel de la página y aplica mejora progresiva al hero y al monograma institucional.
- Se eliminaron dependencias visuales de versiones legadas dentro de las páginas activas.

### Construcción y control de calidad

- Se creó `scripts/apply_visual_assets.py` como aplicador idempotente posterior a los generadores funcionales.
- El aplicador normaliza la posición de sus recursos para que ejecuciones sucesivas no alteren el orden del HTML.
- Se creó `scripts/validate_visual_assets.py` para validar archivos, cabecera WebP, rutas, versión y ausencia de logotipos retirados.
- `validate_site.py` exige ahora la identidad canónica, el favicon, el hero WebP y las hojas visuales vigentes.
- GitHub Pages solo publicó después de aprobar idempotencia, 39 páginas, catálogo, contexto, datos estructurados, capa editorial, JavaScript y activos visuales.

## v3.8.0 — 2026-08-05

### Catálogo estático e indexable

- Las ocho fichas de servicios y las ocho fichas de productos publican ahora su contenido jurídico completo en HTML.
- Títulos, pregunta ejecutiva, situaciones, alcance, método, entregables, requisitos, límites y soluciones relacionadas están disponibles sin ejecutar JavaScript.
- `catalog-v32.js` permanece como fuente única del contenido para evitar divergencias editoriales.
- Se creó `scripts/render_catalog_static.mjs`, que convierte el catálogo central en HTML semántico durante la construcción.
- Cada ficha contiene un único `h1`, nueve secciones editoriales identificadas y un volumen sustantivo mínimo validado.

### Rendimiento y mejora progresiva

- Las fichas dejaron de descargar y ejecutar el catálogo completo en el navegador.
- Se creó `catalog-page.js` como controlador ligero para menú, teclado, año y regreso al inicio.
- Los scripts de ficha cargan con `defer`.
- Las secciones inferiores utilizan `content-visibility` para reducir trabajo inicial de renderizado.
- Año, versión y contenido permanecen visibles como respaldo cuando JavaScript no está disponible.

### Accesibilidad y presentación

- Se incorporó soporte de `prefers-reduced-motion`.
- El menú móvil conserva cierre con Escape, recuperación de foco, bloqueo del fondo y desplazamiento interno.
- Los títulos extensos ajustan su contenido en pantallas estrechas.
- Se añadieron estilos de impresión que eliminan navegación, controles flotantes y fondos decorativos.
- Se conservó foco visible compartido y objetivos táctiles para controles móviles.

### Construcción y calidad

- `build-canonical.yml` ejecuta shells, prerender, enriquecimiento editorial y sincronización de versión en una secuencia única.
- Los cambios en `catalog-v32.js` regeneran automáticamente las 16 fichas.
- Se creó `validate_static_catalog.py` para impedir regresiones hacia páginas vacías o dependientes de JavaScript.
- `pages.yml` comprueba idempotencia del prerender, estructura semántica, contenido mínimo, scripts ligeros y sintaxis antes de publicar.

## v3.7.0 — 2026-08-05

### Autoridad y capa editorial

- La página de la firma, las seis perspectivas y los ocho sectores incorporan metadatos sociales, URL canónica y breadcrumbs estructurados.
- Las perspectivas publican esquema `Article`, autoría de Agustín Rendón Calle y fecha de revisión editorial.
- Los sectores publican esquema `WebPage` con materia sectorial identificada.
- La página institucional publica esquemas `AboutPage`, `LegalService` y `Person` sin incorporar reconocimientos o resultados no verificados.
- Se agregó una franja visible de autoría, revisión y carácter general del contenido.

### Navegación y conversión

- Las 15 páginas editoriales incorporan una barra de continuidad para volver a la biblioteca, al portafolio o a los sectores.
- Se añadió navegación anterior y siguiente entre perspectivas y entre sectores.
- Los CTA trasladan contexto y materia al formulario público mediante parámetros explícitos.
- La navegación conserva el contexto dentro de la sesión y evita solicitar información confidencial en la web pública.

### Flujo de mantenimiento

- Se creó `scripts/enrich_editorial_pages.py` como enriquecedor idempotente que preserva el cuerpo jurídico de cada página.
- Se creó `scripts/sync_public_version.py` para sincronizar etiquetas visibles con `version.json`.
- Los workflows separados de catálogo y contenido editorial fueron sustituidos por `build-canonical.yml`.
- El constructor único procesa catálogo, páginas editoriales y versión pública en orden y confirma todos los archivos derivados en un solo commit.
- `pages.yml` comprueba la idempotencia de los tres generadores antes de desplegar.

## v3.6.0 — 2026-08-05

### Continuidad, SEO y fichas canónicas

- Los enlaces desde la portada hacia servicios, productos, sectores y perspectivas incorporan contexto explícito.
- El contexto se conserva en la sesión y puede recuperarse al regresar al formulario.
- Las 16 fichas incluyen barra de continuidad, CTA contextual y metadatos sociales específicos.
- Los servicios publican esquema `Service`; los productos utilizan `Product`; todas las fichas incorporan `BreadcrumbList`.
- Se creó `scripts/build_catalog_shells.py` como fuente canónica de la estructura de las fichas.
- Se consolidaron foco visible, cierre de menú por Escape y estilos compartidos en `page-context.css`.

## v3.5.0 — 2026-08-05

### Selector y conversión

- Se incorporó un selector guiado que recomienda orientación, servicio, producto o plan según materia, resultado esperado y horizonte.
- Cada recomendación enlaza el alcance completo y permite trasladar la necesidad al formulario de contacto.
- El menú móvil utiliza una ventana compacta, desplazable y con bloqueo del fondo.
- `decision-flow.js` y `decision-flow.css` concentran selector, contacto contextual y navegación móvil.

## v3.4.0 — 2026-08-05

### Arquitectura sectorial

- Se publicaron ocho páginas profundas para tecnología, servicios públicos y economía circular, agroindustria, salud, comercio, startups, proyectos públicos y operaciones jurídicas.
- Cada página incorpora decisiones frecuentes, mapa jurídico-operativo, riesgos tempranos, soluciones relacionadas y lecturas recomendadas.
- Las tarjetas sectoriales de la portada enlazan sus páginas completas.

## v3.3.1 — 2026-08-05

### Biblioteca de perspectivas

- Se creó una biblioteca pública de contenido jurídico y empresarial.
- Se publicaron seis perspectivas sobre IA, contratos, propiedad intelectual, socios e inversión, proyectos regulados y Legal Operations.
- Cada artículo incorpora pregunta ejecutiva, marco de análisis, señales de alerta, preguntas de control, acciones y límites.

## v3.3.0 — 2026-08-04

### Autoridad institucional y flujo directo

- Se creó una página profunda de la firma con dirección, método, principios, experiencia sectorial y modelo de colaboración.
- `main` pasó a ser la línea única de trabajo y publicación.
- La rama `stable` conserva automáticamente el último commit desplegado con éxito.
- Se eliminaron recursos heredados que ninguna página activa consumía.

## v3.2.0 — 2026-08-04

### Fichas profundas

- Se crearon páginas individuales para ocho servicios y ocho productos.
- Cada ficha incorpora pregunta ejecutiva, situaciones de uso, alcance, método, entregables, requisitos, exclusiones y soluciones relacionadas.
- El validador controla 16 identificadores únicos, rutas internas y recursos.

## v3.1.0 — 2026-08-04

### Claridad y conversión

- Se explicó para quién es Meridiano y cuándo puede agregar mayor valor.
- Se diferenciaron orientación focal, servicio profesional, producto cerrado y plan recurrente.
- Se agregaron entregables, criterios de encaje, preguntas frecuentes y proceso de contacto.

## v3.0.0 — 2026-08-04

### Reconstrucción canónica

- Se consolidó la identidad visual angular v3 en marino, marfil, azul y dorado.
- Se restauró la arquitectura de ocho servicios, ocho productos, cinco planes, seis documentos y ocho sectores.
- Se incorporaron logotipo, hero gráfico, Ruta Meridiano y controles antirregresión.

## Línea v2 — 2026-08-04

- Migración inicial del sitio autocontenido a GitHub Pages.
- Incorporación de demo pública, portal por perfiles, páginas legales, sitemap, robots, manifiesto, página 404 y validaciones automáticas.
- El detalle histórico completo permanece disponible en el historial de commits del repositorio.

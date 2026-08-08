# Historial de versiones

## v4.8.0 — 2026-08-08

### Calidad pública y arquitectura static-first

- La portada deja de depender de JavaScript para alcanzar su estado canónico: hero, rutas por necesidad, nombres de productos, enlaces profundos, sectores, perspectivas y acceso a la firma están presentes desde el HTML inicial.
- Las seis tarjetas de necesidad se convirtieron en enlaces nativos. “Mi operación jurídica” conduce ahora a Legal Operations, corrigiendo la asociación previa con el Sistema Contractual Empresarial.
- Los ocho servicios y los ocho productos publican sus fichas profundas directamente desde la portada; los ocho productos muestran sus nombres y resúmenes v4.1 canónicos sin esperar a `catalog-home-v32.js`.
- Los ocho sectores se alinearon con la taxonomía canónica y quedaron navegables en HTML estático.
- Las tres perspectivas destacadas enlazan sus artículos completos y se añadieron rutas estáticas hacia la biblioteca de Perspectivas y la página institucional de la firma.

### Rendimiento, accesibilidad y SEO

- El hero fotográfico WebP se sirve desde el primer render con dimensiones declaradas, `loading="eager"`, `decoding="async"`, `fetchpriority="high"` y preload de imagen.
- El idioma documental de las páginas públicas se normalizó a `es-CO`.
- La portada incorpora metadata Open Graph, Twitter Card, `robots` y JSON-LD para `Organization`/`LegalService` y `WebSite`.
- Los filtros de productos dejaron la semántica de tabs y utilizan un grupo de botones con `aria-pressed`.
- El menú móvil actualiza su etiqueta Abrir/Cerrar, cierra con `Escape`, devuelve foco al control y bloquea el scroll del documento mientras está abierto.
- Los desplazamientos programáticos respetan `prefers-reduced-motion` y se reforzó el foco visible de rutas y enlaces profundos.
- `demo.html` declara `noindex,nofollow`; permanece fuera del sitemap por tratarse de un portal ficticio demostrativo.
- Todos los `lastmod` de `sitemap.xml` se sincronizaron con la fecha de release, 2026-08-08.

### Construcción y control

- Se añadieron `quality-v48.css`, `scripts/apply_quality_v48.py`, `scripts/normalize_quality_v48.py` y `scripts/validate_quality_v48.py`.
- La secuencia canónica aplica v4.8 después de las capas v4.5–v4.7 y antes de sincronizar la versión pública.
- El control de idempotencia bloqueó inicialmente Pages por una línea vacía acumulativa antes del bloque SEO; se añadió una normalización determinista específica y se repitió la cadena hasta obtener diff cero.
- `validate_site.py` fue actualizado para exigir el nuevo estado static-first: hero canónico en HTML, 16 enlaces profundos y ocho rutas sectoriales, en vez de conservar una etiqueta sectorial legada.
- El validador v4.8 detectó una referencia defensiva restante a `aria-selected`; se eliminó de la salida canónica para mantener semántica `aria-pressed` de principio a fin.
- La ejecución final aprobó idempotencia, integridad de 39 páginas, catálogo de 16 fichas, conversión v4.4, portada v4.5, fichas v4.6, editorial/demos v4.7, calidad v4.8, selector, contexto, sistema visual, JavaScript y JSON antes de desplegar.
- GitHub Pages publicó correctamente la release y `stable` quedó sincronizada con el commit funcional desplegado.

## v4.7.0 — 2026-08-08

### UX/UI editorial, sectorial y demostrativa

- La capa de experiencia pública se extendió a 18 páginas: Firma, Biblioteca de Perspectivas, seis perspectivas, ocho sectores, Centro de Demostración y Meridiano Empresas.
- Se incorporó navegación móvil accesible en las páginas institucionales, editoriales y sectoriales que antes ocultaban su menú en pantallas pequeñas.
- Se añadió progreso de lectura y resaltado de navegación activa como mejora progresiva.
- Se corrigió el offset entre cabeceras sticky y barra de continuidad para evitar superposiciones en páginas largas.
- Todas las páginas v4.7 cuentan con CTA móvil contextual y rutas claras de regreso hacia oferta, biblioteca, sectores o demostración.

### Firma, perspectivas y sectores

- La tarjeta de dirección de la firma utiliza el monograma M canónico y los ocho frentes de experiencia enlazan ahora a sus páginas sectoriales correspondientes.
- La Biblioteca de Perspectivas conserva seis lecturas únicas: tres destacadas y tres complementarias, eliminando duplicaciones de IA, contratos y proyectos regulados.
- Las seis perspectivas mantienen su índice editorial y añaden un cierre de conversión que conecta la lectura con una necesidad profesional concreta.
- Los ocho sectores incorporan un recorrido rápido por enfoque, decisiones, riesgos y siguiente paso, con resaltado progresivo de la sección activa.
- Las secuencias anterior/siguiente y los metadatos editoriales existentes se preservaron.

### Centro Demo y Meridiano Empresas

- El Centro de Demostración incorpora una franja explícita sobre datos ficticios, procesamiento local y ausencia de cargas de información sensible.
- Se añadió un cierre de conversión entre el recorrido demostrativo y la presentación de una necesidad profesional.
- Meridiano Empresas incorpora una guía de uso en tres pasos y continuidad móvil hacia Centro Demo y la web pública.
- Se conservaron los tres perfiles ficticios y los nueve módulos demostrativos: resumen, solicitudes, expedientes, documentos guiados, archivos, obligaciones, calendario, riesgos y analítica.

### Construcción y control

- Se añadieron `editorial-v47.css`, `editorial-v47.js`, `scripts/apply_editorial_ux_v47.py` y `scripts/validate_editorial_ux_v47.py`.
- El primer control posterior al constructor detectó acumulación de whitespace alrededor de los bloques administrados por v4.7 y bloqueó Pages antes del despliegue.
- Se añadió `scripts/normalize_editorial_v47.py` como fase determinista limitada a las 18 salidas v4.7; la cadena completa volvió a ejecutarse hasta obtener diff cero.
- El validador v4.7 dejó de depender de `packaging` y utiliza comparación SemVer local para evitar dependencias incidentales del runner.
- La ejecución final aprobó idempotencia, integridad HTML, catálogo, conversión v4.4, portada v4.5, fichas v4.6, capa v4.7, flujo guiado, contexto, editorial, identidad visual, JavaScript y metadatos antes de publicar.

## v4.6.0 — 2026-08-08

### UX/UI de fichas profundas

- Las ocho fichas de servicios y las ocho fichas de productos comparten ahora una arquitectura visual y de navegación coherente con la portada v4.5.
- Se redujeron la altura y la densidad de cabecera y hero sin eliminar metadatos, alcance ni contenido jurídico.
- Se incorporó un índice ejecutivo sticky con acceso directo a decisión, alcance, entregables, implementación, límites y siguiente paso.
- Los encabezados editoriales, tarjetas, método, relaciones y límites fueron reorganizados para facilitar lectura rápida y profundización posterior.
- El contenido sustantivo de los productos v4.1 y servicios v4.2 permanece íntegro y disponible en HTML estático.

### Navegación, conversión y móvil

- Las fichas profundas usan una navegación común: Servicios, Productos, Planes y precios, Sectores y Firma.
- Centro demo y Presentar necesidad funcionan como acciones principales de cabecera.
- `detail-v46.js` resalta progresivamente el hito activo mediante `IntersectionObserver` y vuelve a enlazar el índice cuando el contenido de producto se actualiza mediante mejora progresiva.
- En móvil, los controles circulares se sustituyen por una barra persistente con Presentar necesidad y WhatsApp contextualizado con el nombre de la ficha.
- El panel de límites puede permanecer visible en escritorio mientras se revisan exclusiones, y el índice horizontal se adapta a pantallas intermedias.

### Construcción y control

- Se añadieron `detail-v46.css`, `detail-v46.js`, `scripts/apply_detail_ux_v46.py` y `scripts/validate_detail_ux_v46.py`.
- El aplicador v4.6 se ejecuta después de los renderers jurídicos y de las capas visuales anteriores, por lo que no modifica la fuente sustantiva del catálogo.
- La validación exige exactamente 16 fichas profundas, una sola carga de la capa v4.6, seis hitos de navegación, CTA contextual, responsive y versión pública correcta.
- El primer control de idempotencia detectó una alteración de espacios producida por el normalizador; el despliegue fue bloqueado, se corrigió el aplicador y se repitió la secuencia sin relajar el control.
- La ejecución final aprobó idempotencia, HTML y recursos, catálogo estático, conversión v4.4, portada v4.5, fichas v4.6, flujo guiado, contexto, editorial, identidad visual, JavaScript y metadatos antes de publicar.

## v4.5.0 — 2026-08-07

### UX/UI y arquitectura narrativa de portada

- La portada se reorganizó para seguir una secuencia más corta: necesidad, modalidad, servicios, productos, entregables, demostración, planes y precios, contratación, sectores, perspectivas, firma, preguntas frecuentes y contacto.
- Se retiraron de la portada cinco bloques redundantes: modalidades de trabajo duplicadas, capacidades estratégicas repetidas, documentos guiados duplicados, bloque de encaje y Ruta Meridiano separada.
- La información jurídica profunda permanece en las 16 fichas canónicas y en las páginas sectoriales y editoriales.
- La franja superior ahora comunica evidencia concreta de la oferta: 8 servicios, 8 productos, 5 planes, 8 sectores y acceso al centro demo.
- “Qué recibe la empresa” se simplificó a cuatro resultados operativos: decisión, estructura, ejecución y control.

### Navegación, móvil y demostración

- El menú principal se redujo y dejó de recibir enlaces dinámicos posteriores a la carga.
- Se eliminaron las inyecciones legadas de Selector, Perspectivas, Centro demo y Área de clientes que saturaban el menú.
- El selector guiado continúa funcionando dentro de la página y conserva sus rutas hacia servicios y productos.
- Se incorporó una barra de conversión persistente en móvil.
- Se añadió un mockup ilustrativo de Meridiano Empresas para explicar cómo se conectan expediente, riesgos, obligaciones, documentos y decisiones.
- El bloque de contratación recupera la visual de Ruta Meridiano sin duplicar una sección completa.

### Construcción y control

- Se creó `ux-v45.css` como capa final de layout y responsive de la portada.
- Se creó `scripts/apply_ux_v45.py` como aplicador idempotente posterior a las capas comercial y visual.
- Se creó `scripts/validate_ux_v45.py` para controlar orden narrativo, eliminación de bloques redundantes, navegación, mockup, accesibilidad y comportamiento móvil.
- `validate_site.py` y `validate_decision_flow.py` fueron alineados con la nueva arquitectura.

## v4.4.0 — 2026-08-07

### Conversión y contratación

- Los CTA de planes y honorarios trasladan contexto hacia el formulario o hacia la ficha profunda correspondiente.
- Se incorporó el bloque “Cómo se contrata” con necesidad, calificación, propuesta, aceptación e inicio.
- Se aclaró que una conversación preliminar no constituye por sí sola un mandato abierto.
- Se eliminó la doble carga de `catalog-home-v32.js` desde la portada.
- Se creó validación específica para conversión comercial, contexto y ausencia de cargas duplicadas.

## v4.3.0 — 2026-08-07

### Planes y honorarios

- Se publicaron cinco modalidades recurrentes: Esencial, Empresarial, Dirección, Regulado y Banco Documental/Legal Operations.
- Se conservaron los valores comerciales previamente definidos y se distinguieron precio fijo, valor “desde” y alcance a medida.
- Se publicaron referencias orientativas de honorarios para diagnóstico, IA, propiedad intelectual, societario, documentos y conceptos.
- Se explicitaron IVA, tasas, gastos de terceros, horas adicionales, capacidad, SLA y exclusiones.
- La capa comercial quedó integrada al constructor canónico y protegida por validación automática.

## v4.2.0 — 2026-08-07

### Servicios profesionales

- Los ocho servicios profesionales fueron profundizados al estándar comercial-jurídico de los productos v4.1.
- Cada servicio publica resultado empresarial, arquitectura jurídica, perímetro de referencia, método, entregables, formatos, cronograma, requisitos, responsabilidades, aceptación, límites y extensiones.
- Se mantuvo la naturaleza adaptable del servicio profesional y se evitó presentarlo como disponibilidad ilimitada.
- Se creó `catalog-services-v42/` y un prerender dedicado de servicios para conservar la separación frente a productos de alcance cerrado.

## v4.1.0 — 2026-08-07

### Catálogo comercial-jurídico de productos

- Se consolidaron los ocho productos jurídicos de alcance cerrado en `catalog-products-v41/` como módulos editoriales independientes.
- Las fichas de producto incorporan perímetro cuantificado, método, entregables, formatos, cronograma, requisitos, responsabilidades, criterios de aceptación, límites, complementos y soluciones relacionadas.
- La Auditoría Jurídica Empresarial Integral quedó definida con alcance de una sociedad colombiana, hasta 8 entrevistas, hasta 60 documentos, hasta 8 frentes jurídicos, hasta 80 hallazgos y hasta 5 instrumentos correctivos de complejidad estándar.
- Se reforzó la orientación comercial de las fichas para explicar con precisión qué recibe el cliente, en qué formato, dentro de qué alcance y bajo qué condiciones.

### Construcción y preservación

- `scripts/build_catalog_shells.py` genera en esta release únicamente las ocho fichas de producto y preserva deliberadamente los servicios profesionales hasta su ciclo editorial dedicado.
- `scripts/render_catalog_static.mjs`, `validate_site.py` y `validate_static_catalog.py` fueron ajustados para soportar y validar el catálogo v4.1.
- Se eliminaron workflows y artefactos temporales de instalación usados durante la migración, conservando únicamente la arquitectura canónica de construcción y despliegue.
- La publicación final aprobó idempotencia de generadores, HTML y recursos locales, catálogo estático, flujo guiado, contexto y datos estructurados, capa editorial, identidad visual, JavaScript y metadatos JSON.
- GitHub Pages desplegó correctamente la release y `stable` quedó sincronizada con `main`.

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
- Se creó `scripts/validate_visual_assets.py` para validar archivos, rutas y ausencia de logotipos retirados.
- `validate_site.py` exige la identidad canónica, favicon, hero WebP y hojas visuales vigentes.
- GitHub Pages solo publicó después de aprobar idempotencia, catálogo, contexto, datos estructurados, capa editorial, JavaScript y activos visuales.

## v3.8.0 — 2026-08-05

### Catálogo estático e indexable

- Las ocho fichas de servicios y las ocho fichas de productos publican su contenido jurídico completo en HTML.
- Títulos, pregunta ejecutiva, situaciones, alcance, método, entregables, requisitos, límites y soluciones relacionadas están disponibles sin ejecutar JavaScript.
- Se creó `scripts/render_catalog_static.mjs` para convertir el catálogo central en HTML semántico durante la construcción.
- Cada ficha conserva contenido sustantivo, navegación contextual y mejora progresiva.

### Rendimiento, accesibilidad y calidad

- Las fichas dejaron de depender del catálogo completo para mostrar su contenido principal.
- Se mantuvo soporte de `prefers-reduced-motion`, foco visible, menú móvil y estilos de impresión.
- La construcción canónica comprueba estructura, sintaxis, metadatos y ausencia de regresiones antes de publicar.

## v3.7.0 — 2026-08-05

### Autoridad y capa editorial

- La página de la firma, las seis perspectivas y los ocho sectores incorporan metadatos sociales, URL canónica y breadcrumbs estructurados.
- Las perspectivas publican esquema `Article`, autoría y fecha de revisión editorial.
- Los sectores publican esquema `WebPage` con materia sectorial identificada.
- Los CTA trasladan contexto y materia al formulario público mediante parámetros explícitos.

## v3.6.0 — 2026-08-05

### Continuidad, SEO y fichas canónicas

- Los enlaces desde la portada hacia servicios, productos, sectores y perspectivas incorporan contexto explícito.
- El contexto se conserva en la sesión y puede recuperarse al regresar al formulario.
- Las 16 fichas incluyen barra de continuidad, CTA contextual y metadatos sociales específicos.
- Se consolidó el generador canónico de shells y el foco visible compartido.

## v3.5.0 — 2026-08-05

### Selector y conversión

- Se incorporó un selector guiado para orientar al usuario hacia la modalidad y ficha más adecuada.
- Se añadió contexto de recorrido al formulario para evitar que el usuario tenga que repetir desde dónde llega.

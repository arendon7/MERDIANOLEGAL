# Historial de versiones

## v5.3.0 — 2026-08-08

### Autoridad y descubrimiento

- Se creó `authority-v53.json` como mapa canónico entre las seis rutas de `soluciones/`, las seis perspectivas editoriales y los ocho sectores públicos.
- Las perspectivas incorporan un bloque “DE LA LECTURA A LA DECISIÓN” que conecta criterio general con una o dos rutas empresariales relacionadas.
- Los sectores incorporan “RUTAS POR SITUACIÓN” para derivar el contexto sectorial hacia necesidades concretas sin duplicar servicios ni productos.
- Las seis soluciones quedan cubiertas por el sistema de descubrimiento y conservan intactos sus bloques jurídicos, CRO, FAQ, honorarios, límites y CTA v5.2.
- La relación funciona en ambos sentidos: soluciones → evidencia editorial/sectorial y perspectivas/sectores → soluciones.

### Datos estructurados y señales de autoridad

- El JSON-LD `Organization` de la portada añade el logotipo canónico como `ImageObject` y ocho materias `knowsAbout` coherentes con la oferta pública.
- El hub `soluciones/` publica un `ItemList` con las seis rutas empresariales.
- Cada solución publica un `ItemList` con sus modalidades relacionadas; perspectivas y sectores publican `ItemList` con las rutas de decisión que corresponden a su contenido.
- Las seis perspectivas modificadas por v5.3 sincronizan `article:modified_time` y `dateModified` con `2026-08-08`.
- No se crearon páginas artificiales para keywords ni se duplicó el catálogo: los datos estructurados describen relaciones ya presentes en el contenido público.

### Contrato de medición CRO

- Se añadieron `measurement-contract-v53.json` y `measurement-v53.js`.
- El contrato define exactamente seis eventos: `solution_view`, `authority_open`, `evidence_open`, `route_open`, `faq_open` y `contact_intent`.
- Los payloads se limitan a `stage`, `target` y `need` con valores controlados; no incorporan nombre, correo, empresa, teléfono, mensaje, documentos ni contenido del formulario.
- La capa declara `piiAllowed: false`, `networkTransport: false` y `persistentStorage: false`.
- `measurement-v53.js` utiliza `MeridianoTelemetry` y un `CustomEvent` local, sin `fetch`, XHR, `sendBeacon`, cookies ni almacenamiento persistente.
- La analítica de terceros continúa desactivada y Search Console permanece sin token; v5.3 prepara un contrato de medición, no activa un proveedor ficticio.

### Construcción, validación y smoke live

- Se añadieron `scripts/apply_authority_v53.py`, `scripts/apply_authority_v53_core.py`, `scripts/validate_authority_v53.py` y `scripts/validate_live_v53.py`.
- La cadena canónica ejecuta v5.3 después de v5.2 y vuelve a exigir diff cero sobre todas las salidas públicas.
- El validador v5.3 comprueba 6 perspectivas, 8 sectores, cobertura de las 6 soluciones, 8 materias de autoridad, Organization/ItemList, fechas editoriales, contrato de eventos, ausencia de PII/red/almacenamiento y continuidad de v5.2.
- El smoke live v5.3 ejecuta primero todo el smoke v5.2 y luego consulta portada, hub, seis soluciones, seis perspectivas, ocho sectores y `measurement-v53.js` sobre la URL realmente servida.

### Barreras e incidencias

- Una llamada de prueba del conector creó accidentalmente un archivo vacío temporal `__no_such_path__` en `main`. Fue eliminado inmediatamente antes de activar el paquete v5.3 y no formó parte de la release aprobada.
- El primer constructor v5.3 generó correctamente contenido, schema y medición, pero la segunda pasada fue bloqueada por idempotencia: perspectivas y sectores alternaban un salto de línea alrededor de los bloques administrados.
- La lógica funcional se preservó en `apply_authority_v53_core.py`; `apply_authority_v53.py` pasó a aplicar esa lógica y normalizar determinísticamente los límites de bloque.
- La siguiente ejecución obtuvo diff cero y aprobó catálogo, conversión, UX v4.5–v4.7, calidad v4.8, operación v4.9, producción v5.0, crecimiento v5.1, CRO/SEO v5.2, autoridad/medición v5.3, selector, contexto, editorial, visual, JavaScript y JSON.
- GitHub Pages desplegó correctamente, el smoke público v5.3 quedó verde y `stable` se sincronizó con el commit funcional antes del cierre documental.

## v5.2.0 — 2026-08-08

### Conversión y calificación

- Las seis rutas de `soluciones/` conservan el contenido jurídico v5.1 y añaden una capa de conversión orientada a reducir fricción antes del contacto, sin transformar las fichas en páginas comerciales superficiales.
- Cada landing publica un bloque de encaje con al menos tres señales de que la ruta es pertinente y un bloque de no encaje con situaciones en las que conviene otra intervención o especialidad.
- Se añadieron tres objeciones específicas por ruta, con respuestas desarrolladas que delimitan alcance, expectativas, coordinación con equipos internos y relación con otras disciplinas.
- El cierre genérico v5.1 fue sustituido por un CTA específico para cada necesidad: riesgo jurídico, dirección externa, IA, inversión, proyectos regulados y Legal Operations.
- El hub `soluciones/` conserva la arquitectura v5.1 y añade una guía rápida para distinguir entre priorización de riesgos, capacidad jurídica recurrente y decisiones de crecimiento o regulación.

### SEO de intención y FAQ

- Se creó `cro-solutions-v52.json` como fuente editorial/comercial de la capa v5.2, separada del catálogo jurídico canónico.
- Las seis páginas reciben títulos SEO y meta descriptions de alta intención alineados con búsquedas empresariales reales.
- Se incorporaron **18 preguntas frecuentes nuevas**, tres por landing, con respuestas visibles en HTML.
- Cada ruta publica un bloque independiente `FAQPage` en JSON-LD con exactamente tres preguntas y respuestas.
- El hub y las seis páginas cargan `cro-v52.css`, una hoja limitada a los componentes de calificación, objeciones, honorarios, FAQ, interlinking y guía rápida.
- No se crearon páginas adicionales únicamente para capturar keywords: el SEO se concentra en rutas que ya corresponden a necesidades y ofertas jurídicas reales.

### Honorarios e interlinking

- Cada landing explica qué variables determinan el alcance y remite a las secciones canónicas `#honorarios` o `#planes`.
- `cro-solutions-v52.json` no replica valores monetarios, evitando discrepancias entre páginas, desactualización de precios y confusión entre referencia pública y cotización definitiva.
- Cada solución enlaza dos rutas relacionadas, además de conservar sus vínculos v5.1 hacia productos, servicios, sectores, perspectivas, Firma y Centro Demo.
- Se mantiene la política pública de honorarios orientativos sujetos a alcance final e IVA, con tasas y gastos de terceros excluidos salvo estipulación expresa.

### Credibilidad y límites

- La v5.2 conserva la prohibición de inventar testimonios, casos de éxito, logos de clientes, tasas de éxito o resultados no sustentados.
- La prueba pública continúa apoyándose en 16 fichas profundas, 8 lecturas sectoriales, 6 perspectivas, Centro Demo, método, límites y contenido jurídico inspeccionable.
- Las FAQ aclaran expresamente cuándo la función jurídica debe coordinarse con capacidades técnicas, financieras, tributarias, contables, ambientales o de ingeniería en vez de simular que puede sustituirlas.

### Construcción y control

- Se añadieron `cro-v52.css`, `scripts/apply_cro_v52.py`, `scripts/validate_cro_v52.py` y `scripts/validate_live_v52.py`.
- La cadena canónica ejecuta v5.2 después de `apply_growth_v51.py` y `finalize_growth_v51.py`, por lo que la nueva capa no altera la fuente de los 16 productos/servicios ni los contratos static-first anteriores.
- `scripts/validate_cro_v52.py` exige seis slugs coincidentes con v5.1, SEO razonable, encaje/no encaje, tres objeciones, tres FAQ, JSON-LD válido, rutas relacionadas, enlaces de honorarios canónicos y ausencia de prueba social o precios duplicados.
- `scripts/validate_live_v52.py` ejecuta primero todo el smoke v5.1 y después comprueba sobre la URL servida títulos SEO, calificación, objeciones, honorarios, FAQ schema y CTA específicos.

### Barreras detectadas y correcciones

- Una actualización movió inicialmente `version.json` antes que el paquete completo. El constructor produjo una salida intermedia etiquetada v5.2 sobre la arquitectura previa; no se forzó `main` ni se declaró publicada esa salida.
- El paquete v5.2 se reconstruyó sobre el HEAD canónico más reciente y se integró mediante fast-forward.
- La primera ejecución de calidad aprobó idempotencia, 46 páginas y todos los controles v4.8–v5.0, pero el validador v5.1 bloqueó los CTA específicos porque esperaba literalmente el cierre genérico anterior.
- `scripts/validate_growth_v51.py` se hizo version-aware: hasta v5.1 exige el CTA original; desde v5.2 exige continuidad del bloque `SIGUIENTE PASO`, mientras el validador v5.2 verifica el CTA específico.
- El job fallido se reejecutó sin relajar los gates. La ejecución funcional final aprobó idempotencia, catálogo, conversión, UX v4.5–v4.7, calidad v4.8, operación v4.9, producción v5.0, crecimiento v5.1, CRO/SEO v5.2, selector, contexto, editorial, visual, JavaScript y JSON.
- GitHub Pages desplegó correctamente, el smoke público v5.2 terminó en verde y `stable` se sincronizó con el commit funcional antes del cierre documental.

## v5.1.0 — 2026-08-08

### Rutas por situación empresarial

- La portada deja de exigir que un prospecto traduzca primero su problema al nombre de un servicio jurídico y conserva seis puntos de entrada static-first por situación empresarial.
- Se creó el hub indexable `soluciones/` y seis rutas de alta intención: ordenar riesgo jurídico, dirección jurídica externa, gobernanza de IA, preparación para inversión, estructuración de proyectos regulados y Legal Operations.
- Cada ruta explica señales de que la necesidad está abierta, preguntas de decisión, modalidades posibles, entregables, límites, evidencia pública y siguiente paso.
- Las rutas no duplican las 16 fichas canónicas: funcionan como capa de calificación y derivan a producto cerrado, servicio adaptable o capacidad recurrente según el resultado y el perímetro.
- Los CTA llevan contexto y necesidad al formulario público sin pedir documentos confidenciales antes de delimitar el asunto.

### Evidencia pública y criterio comercial

- Se incorporó a la portada un bloque de prueba verificable basado en activos existentes: 16 fichas profundas, 8 lecturas sectoriales, 6 perspectivas y Centro Demo.
- La release prohíbe expresamente en su validador frases de prueba social no sustentada como “casos de éxito”, “nuestros clientes confían”, “tasa de éxito” o “testimonio de cliente”.
- No se inventaron clientes, resultados, porcentajes ni endorsements. La lógica de credibilidad se apoya en alcance, método, límites, criterio publicado y experiencia demostrable.
- La ruta de Legal Operations conserva continuidad con la arquitectura anterior: portada → página de decisión → servicio profesional de Legal Operations.

### SEO, generación e interlinking

- Se añadieron `growth-solutions-v51.json` y `growth-v51.css` como fuente estructurada y capa visual de crecimiento.
- `scripts/apply_growth_v51.py` genera el hub, las seis páginas, el nuevo bloque de necesidades, la sección de evidencia y las entradas v5.1 de `sitemap.xml`.
- `scripts/finalize_growth_v51.py` reutiliza la lógica de producción v5.0 para añadir canonical, `og:url`, runtime y telemetría a las páginas nuevas y normaliza el canonical limpio del hub a `/soluciones/`.
- Las siete páginas nuevas publican HTML estático, `lang="es-CO"`, metadata indexable, JSON-LD y BreadcrumbList cuando corresponde.
- La publicación pasa de 39 a **46 páginas HTML** sin alterar las ocho fichas de servicios, ocho productos, ocho sectores, seis perspectivas ni las superficies demo existentes.

### Compatibilidad e idempotencia

- La primera integración v5.1 reveló que v4.8 conserva un contrato literal de seis enlaces `class="need-card"` en portada. La salida final mantiene exactamente ese contrato mientras cambia contenido y destino hacia las nuevas rutas.
- Un intento posterior demostró que la compatibilidad debía resolverse antes de ejecutar v4.8 en reconstrucciones sucesivas. Se añadió `scripts/normalize_growth_compat_v51.py` como fase previa y se conserva el finalizador v5.1 al cierre de la cadena.
- `scripts/validate_quality_v48.py` se hizo version-aware para Legal Operations: desde v5.1 valida la cadena completa portada → ruta de operación jurídica → servicio Legal Operations, en vez de exigir un enlace directo de la arquitectura anterior.
- El control de idempotencia terminó en verde después de estas correcciones; no se relajó el gate ni se excluyeron las salidas nuevas del diff canónico.

### Canal público, validación y despliegue

- El primer canal `github-pages-growth-ready` no contenía la señal `public`, por lo que el sincronizador lo interpretaba como demostrativo. Se corrigió a `github-pages-public-growth-ready` para conservar “Web pública v5.1.0” en la superficie pública.
- Se añadieron `scripts/validate_growth_v51.py` y `scripts/validate_live_v51.py`.
- El validador v5.1 exige seis slugs únicos, siete páginas exactas, canonical y `og:url`, profundidad mínima, tres rutas de modalidad, evidencia interna, sitemap y ausencia de prueba social inventada.
- El smoke live v5.1 ejecuta primero todo el smoke v5.0 y después consulta portada, hub y las seis páginas de solución sobre la URL realmente servida.
- La ejecución técnica final sobre `5318bc3aaf03a44a84665e7c81f34a6bff05829f` aprobó idempotencia, 46 páginas, catálogo, conversión, UX v4.5–v4.7, calidad v4.8, operación v4.9, producción v5.0, crecimiento v5.1, selector, contexto, editorial, visual, JavaScript y JSON.
- GitHub Pages desplegó correctamente, el smoke público v5.1 terminó en verde y `stable` se sincronizó antes del cierre documental.

## v5.0.0 — 2026-08-08

### Configuración pública y dominio-ready

- Se creó `site-config.json` como fuente única para URL pública, despliegue, entorno, dominio personalizado, WhatsApp, analítica y verificación de buscadores.
- `scripts/site_config.py` valida que `base_url` sea HTTPS absoluta, que la ruta pública sea coherente, que un eventual dominio personalizado coincida con el host y que los parámetros externos no queden parcialmente configurados.
- La URL pública vigente continúa siendo `https://arendon7.github.io/MERDIANOLEGAL/`; `custom_domain` permanece vacío y no se creó un dominio ficticio.
- `scripts/apply_production_v50.py` deriva desde la configuración los canonical, `og:url`, `robots.txt`, `sitemap.xml`, la ruta pública de `page-context.js` y el estado runtime.
- `CNAME` se genera únicamente si existe un `custom_domain` real configurado; en la base v5.0 no existe.
- Se dejó preparado `search_console_verification`, pero permanece vacío. La meta de verificación solo se incorpora si existe un token real.
- La portada pasa a declarar `Web pública v5.0.0`; los componentes orientados a demostración conservan deliberadamente la etiqueta `Web demostrativa v5.0.0`.

### Runtime, estado y telemetría

- Se añadió `runtime-config.js` como representación pública y segura de la configuración de ejecución, sin secretos.
- Se añadió `site-status.json` para exponer de forma verificable versión, URL base, entorno, despliegue, estado de dominio, analítica, canal de contacto y política de indexación del demo.
- Se añadió `telemetry-v50.js` como bus de eventos first-party en memoria del navegador para `page_view`, CTA relevantes y `lead_prepared`.
- La telemetría base no utiliza `fetch`, `XMLHttpRequest`, `sendBeacon`, cookies, `localStorage`, `sessionStorage` propio, píxeles ni proveedores externos.
- `analytics.enabled` permanece en `false`, `provider` en `none` y `site_id` vacío; no se activó analítica de terceros sin una decisión y configuración reales.
- Se dejó un punto de extensión para un futuro `MeridianoAnalyticsAdapter`, condicionado a que la configuración pública habilite expresamente un proveedor válido.

### Privacidad y contacto

- `privacidad.html` se actualizó a versión 1.1 para reflejar el comportamiento técnico real de la web.
- La política aclara que el formulario se procesa localmente, que abrir WhatsApp no equivale a enviar el mensaje y que la web no conserva una copia del formulario en un servidor propio.
- Se documentó el uso ya existente de `sessionStorage` exclusivamente para conservar contexto comercial de navegación durante la sesión.
- Se documentó que la instrumentación v5.0 mantiene eventos no identificadores solo en memoria y que la analítica de terceros está actualmente desactivada.
- Se conservó íntegro el flujo operativo v4.9: referencia única, saneamiento, honeypot, contexto, fallback y WhatsApp como canal real.

### Construcción, validación y despliegue

- Se añadieron `scripts/validate_production_v50.py` y `scripts/validate_live_v50.py`.
- La construcción canónica aplica ahora v5.0 después de v4.9 y de la sincronización visible de versión.
- El control de calidad repite toda la cadena v4.1→v5.0 y exige diff cero antes de validar y desplegar.
- El validador v5.0 comprueba configuración, runtime, status, canonical, `og:url`, robots, sitemap, privacidad, CNAME, Search Console condicional, telemetría sin red y sintaxis JavaScript.
- El smoke live v5.0 consulta la URL realmente servida y comprueba `site-status.json`, portada, Firma, una ficha de servicio, una ficha de producto, Perspectivas, Privacidad, Demo, runtime, telemetría, conversión, sitemap y robots.
- `stable` continúa condicionado al smoke post-deploy; un despliegue interno exitoso no basta para promover la versión.

### Barreras detectadas y correcciones

- Una carrera inicial movió temporalmente `version.json` antes de incorporar el paquete completo; se reconstruyó el cambio sobre el HEAD generado más reciente sin forzar `main`.
- La primera salida canónica v5.0 fue bloqueada por idempotencia: `meta referrer` cambiaba de posición y la nueva subsección de privacidad acumulaba diferencias de whitespace.
- Se estabilizó la subsección de privacidad y la posición de `referrer`; una segunda ejecución identificó además el caso de cabeceras HTML compactadas, que fue normalizado para producir desde la primera pasada un orden determinista.
- El validador visual legado exigía “Web demostrativa” en la portada. Se actualizó para derivar la etiqueta esperada desde `version.json.channel`, manteniendo un control semántico más preciso.
- No se deshabilitó ninguna barrera. La ejecución técnica final aprobó idempotencia, 39 páginas, 16 fichas, conversión, UX v4.5–v4.7, calidad v4.8, operación v4.9, producción v5.0, selector, contexto, editorial, visual, JavaScript y JSON; GitHub Pages desplegó, el smoke v5.0 fue verde y `stable` se sincronizó.

## v4.9.0 — 2026-08-08

### Preparación para operación pública

- El formulario público conserva WhatsApp como canal real y mantiene la arquitectura estática: la web no crea un backend ficticio ni afirma almacenar o recibir información que no puede verificar.
- Cada solicitud preparada incorpora una referencia única `ML-YYYYMMDD-XXXXX`, necesidad seleccionada, contexto comercial y ruta de origen.
- Se añadieron límites de longitud y normalización de valores antes de construir el mensaje.
- El formulario incorpora un honeypot silencioso y un control temporal básico contra envíos automatizados.
- La interfaz distingue expresamente entre abrir WhatsApp y enviar efectivamente el mensaje; la solicitud solo queda remitida cuando el usuario confirma el envío en WhatsApp.
- Se añadió un acceso directo alternativo a WhatsApp y fallback de navegación cuando el navegador bloquea la nueva ventana.

### Conversión y navegación

- Se corrigió la reconstrucción de enlaces con fragmento en `commercial-conversion-v44.js`.
- Rutas como `demo.html#documentos` conservan ahora correctamente los parámetros de contexto antes del fragmento: `demo.html?context=...&need=...#documentos`.
- El desplazamiento hacia el formulario contextual respeta `prefers-reduced-motion`.

### Despliegue y verificación live

- Se añadieron `operations-v49.css`, `scripts/apply_operations_v49.py`, `scripts/validate_operations_v49.py` y `scripts/validate_live_v49.py`.
- La construcción canónica aplica v4.9 después del cierre static-first v4.8 y antes de sincronizar la versión pública.
- `pages.yml` ejecuta ahora un smoke test HTTP después del despliegue de GitHub Pages y antes de actualizar `stable`.
- El smoke live valida la versión realmente servida, portada, Firma, fichas profundas, Perspectivas, Centro Demo, `noindex` del portal ficticio, JavaScript de conversión, sitemap y robots.
- `stable` dejó de depender únicamente del éxito del job de despliegue: solo se mueve cuando la URL pública también supera el smoke test.
- Se eliminó ruido de ejecuciones directas sobre commits canónicos generados; la ruta autoritativa sigue siendo constructor → calidad → deploy → smoke público → stable.
- El primer constructor v4.9 fue bloqueado por una interpretación de `\s` en el reemplazo Python del JavaScript; se corrigió usando un reemplazo funcional que preserva literalmente el regex y se repitió la cadena completa sin relajar controles.
- La ejecución funcional final aprobó idempotencia, 39 páginas, 16 fichas, conversión, UX v4.5–v4.7, calidad v4.8, operación v4.9, selector, contexto, visual, JavaScript y JSON; GitHub Pages desplegó y el smoke público terminó en verde antes de sincronizar `stable`.

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

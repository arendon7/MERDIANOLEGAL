# Meridiano Legal · Web canónica v5.1.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.1 conserva la base production-ready de v5.0 y añade una capa de crecimiento orientada a que una empresa pueda empezar por su **situación o decisión empresarial**, sin tener que conocer previamente el nombre de un producto o servicio jurídico.

## Estado de la release

La publicación v5.1 está compuesta por **46 páginas HTML** y mantiene como base:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- página institucional de Firma;
- Centro Demo;
- Meridiano Empresas, con datos ficticios y `noindex,nofollow`;
- 1 hub de soluciones y 6 nuevas rutas de decisión empresarial.

La URL pública canónica continúa siendo `https://arendon7.github.io/MERDIANOLEGAL/`. No existe todavía dominio personalizado, CRM, backend propio, analítica de terceros ni token de Search Console. WhatsApp continúa siendo el canal real de contacto y la telemetría first-party v5.0 permanece local y sin transmisión externa.

## v5.1 · Empezar por el problema, no por el catálogo

La portada conserva seis rutas navegables static-first, pero su contenido pasa de categorías jurídicas genéricas a situaciones de alta intención comercial:

1. **Ordenar el riesgo jurídico de una empresa**.
2. **Dirección jurídica externa para empresas**.
3. **Gobernanza jurídica de inteligencia artificial**.
4. **Preparar una empresa para inversión y due diligence**.
5. **Estructurar jurídicamente un proyecto regulado**.
6. **Legal Operations: ordenar la operación jurídica**.

El hub `soluciones/` reúne las seis rutas. Cada página explica:

- cuándo conviene actuar;
- señales observables de que la necesidad ya está abierta;
- preguntas que deben quedar resueltas;
- diferencia entre producto cerrado, servicio adaptable y capacidad recurrente;
- entregables posibles;
- límites que no deben asumirse dentro del alcance;
- perspectivas, sectores, Centro Demo y Firma que pueden revisarse antes del contacto;
- CTA contextual hacia la presentación de la necesidad.

Las páginas son HTML estático, indexables, cuentan con canonical, `og:url`, datos estructurados, breadcrumbs y la misma configuración runtime/telemetría de la capa v5.0.

## Prueba pública verificable

La v5.1 no inventa testimonios, clientes, tasas de éxito ni cifras de resultados. La sección de evidencia de la portada se apoya únicamente en activos que el visitante puede inspeccionar directamente:

- **16 fichas profundas** con alcance, entregables, responsabilidades y límites;
- **8 lecturas sectoriales** con decisiones, dependencias y riesgos;
- **6 perspectivas desarrolladas** que muestran criterio jurídico;
- **Centro Demo** con información ficticia para visualizar método, entregables y seguimiento.

El principio comercial es deliberado: antes de pedir información confidencial, la firma debe permitir revisar qué hace, cómo estructura el trabajo y dónde termina el alcance.

## Fuente estructurada de las rutas

`growth-solutions-v51.json` concentra el contenido canónico de las seis rutas: slug, título, intención, señales, preguntas, modalidades relacionadas, entregables, límites, perspectiva, sector y necesidad comercial.

`scripts/apply_growth_v51.py` genera a partir de esa fuente:

- `soluciones/index.html`;
- las seis páginas de decisión;
- el bloque `#necesidades` de la portada;
- la sección de evidencia pública;
- el bloque v5.1 de `sitemap.xml`.

`growth-v51.css` concentra el sistema visual de hub, páginas de solución y componentes de crecimiento.

## Compatibilidad e idempotencia

La arquitectura acumulada mantiene controles históricos estrictos. En particular, v4.8 exige que la portada conserve exactamente seis enlaces `need-card` navegables sin JavaScript.

Para que v5.1 pueda cambiar el destino y el contenido de esas rutas sin romper ese contrato:

- `scripts/normalize_growth_compat_v51.py` normaliza el HTML previo **antes de v4.8** cuando se reconstruye una salida v5.1 ya generada;
- `scripts/finalize_growth_v51.py` aplica la lógica de producción v5.0 a las siete páginas nuevas, normaliza el canonical limpio del hub `soluciones/` y restituye la compatibilidad exacta de las seis tarjetas de portada al final.

El validador v4.8 también se hizo version-aware para Legal Operations: en v5.1 exige la cadena completa **portada → ruta de decisión de operación jurídica → servicio Legal Operations**, en vez de limitarse a un enlace directo antiguo.

## Configuración de producción v5.0 preservada

`site-config.json` sigue siendo la fuente única para URL pública, despliegue, entorno, dominio, WhatsApp, analítica y verificación de buscadores.

La capa v5.0 continúa generando y validando:

- `runtime-config.js`;
- `site-status.json`;
- canonical y `og:url`;
- `robots.txt` y `sitemap.xml`;
- `CNAME` únicamente si existe un dominio real;
- Search Console únicamente si existe un token real;
- telemetría first-party en memoria mediante `telemetry-v50.js`;
- privacidad v1.1 coherente con el comportamiento técnico del sitio.

El canal de la release v5.1 es `github-pages-public-growth-ready`, por lo que la superficie pública declara **Web pública v5.1.0** y los componentes específicamente demostrativos conservan su etiqueta de demo.

## Construcción canónica

El orden vigente es:

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
python3 scripts/normalize_growth_compat_v51.py
python3 scripts/apply_quality_v48.py
python3 scripts/normalize_quality_v48.py
python3 scripts/apply_operations_v49.py
python3 scripts/sync_public_version.py
python3 scripts/apply_production_v50.py
python3 scripts/apply_growth_v51.py
python3 scripts/finalize_growth_v51.py
```

`Site Quality and Deploy` repite la cadena completa y exige **diff cero** antes de validar:

- integridad de 46 páginas, rutas y recursos;
- catálogo estático de 16 fichas;
- conversión v4.4;
- UX v4.5, v4.6 y v4.7;
- calidad static-first v4.8;
- operación pública v4.9;
- producción v5.0;
- crecimiento y rutas de decisión v5.1;
- selector guiado;
- contexto y datos estructurados;
- Firma, Perspectivas y Sectores;
- sistema visual;
- JavaScript;
- JSON.

Después del deploy, `scripts/validate_live_v51.py` ejecuta primero el smoke v5.0 y después consulta la portada, el hub y las seis nuevas rutas sobre la URL realmente servida. Comprueba contenido, canonical, `og:url`, telemetría e inclusión en sitemap. `stable` solo avanza después de ese smoke.

## Incidencias detectadas durante el cierre v5.1

Las barreras automáticas bloquearon varios estados intermedios y permitieron corregir la arquitectura antes de publicar:

1. v4.8 exigía el contrato literal `class="need-card"` en las seis rutas; se conservó ese contrato en la portada y se reservó la nueva clase visual para el hub;
2. una reconstrucción sucesiva demostró que la compatibilidad debía normalizarse **antes** de ejecutar v4.8, por lo que se añadió un normalizador previo además del finalizador;
3. el validador v4.8 esperaba un enlace directo a Legal Operations; se convirtió en una comprobación version-aware de la cadena portada → ruta → servicio;
4. el primer canal v5.1 no contenía la señal `public` y el sincronizador lo interpretó como demostrativo; se corrigió a `github-pages-public-growth-ready`.

No se desactivó ninguna barrera. La salida técnica final aprobó idempotencia, los validadores acumulados, Pages, smoke v5.1 y sincronización de `stable`.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit que pasó construcción, idempotencia, validadores, GitHub Pages y smoke live.
- Los cambios funcionales activan `Build canonical public site`.
- Pages despliega únicamente una salida validada.
- El smoke post-deploy verifica la URL servida, no solo el artefacto local.
- `stable` se mueve únicamente después de superar ese smoke.

## Próximas activaciones externas

La arquitectura está preparada para crecer sin inventar dependencias. Las siguientes decisiones requieren datos reales antes de activarse:

- dominio personalizado y DNS;
- Google Search Console;
- analítica privacy-friendly con proveedor e identificador definidos;
- CRM, backend de formularios o correo transaccional si se decide ampliar WhatsApp;
- medición CRO de las nuevas rutas de decisión una vez exista una fuente real de datos.

Cada integración debe tener propósito, configuración verificable, tratamiento de datos documentado y prueba de extremo a extremo.

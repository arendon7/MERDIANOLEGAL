# Meridiano Legal · Web canónica v4.9.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado directamente desde GitHub Pages.

## Estado de la release

La v4.9 convierte la base pública cerrada en v4.8 en una versión preparada para operación comercial real dentro de las capacidades de una web estática. No introduce un backend ficticio ni cambia el contenido jurídico, los precios o los alcances aprobados: refuerza el contacto, la trazabilidad comercial y el control posterior al despliegue.

La publicación vigente mantiene la arquitectura `static-first` de v4.8, las 16 fichas profundas, los ocho sectores, las seis perspectivas, cinco planes recurrentes, Centro Demo y Meridiano Empresas.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit que pasó validaciones locales, despliegue de GitHub Pages y smoke test sobre la URL pública real.
- Los cambios funcionales activan `Build canonical public site`.
- La construcción aplica todas las capas canónicas, sincroniza la versión y genera el HTML público.
- `Site Quality and Deploy` vuelve a ejecutar toda la cadena y exige diff cero.
- Después de validar, Pages despliega el commit actual.
- Un smoke test HTTP revisa la versión realmente servida por GitHub.
- `stable` solo se mueve si el smoke público también queda verde.

## Contacto operativo v4.9

El formulario público sigue siendo deliberadamente estático y no almacena expedientes ni información confidencial.

`scripts/apply_operations_v49.py` y `operations-v49.css` incorporan:

- honeypot silencioso contra automatizaciones básicas;
- límites explícitos de longitud para nombre, empresa, correo y contexto;
- referencia única por solicitud con formato `ML-YYYYMMDD-XXXXX`;
- inclusión de necesidad, contexto comercial y ruta de origen en el mensaje preparado;
- limpieza y acotación de valores antes de construir el texto de WhatsApp;
- fallback de navegación si el navegador bloquea la nueva ventana;
- acceso directo alternativo a WhatsApp;
- mensajes de estado que distinguen correctamente entre “WhatsApp abierto” y “mensaje enviado”.

La solicitud solo se considera remitida cuando el usuario confirma el envío dentro de WhatsApp. La web no afirma una recepción que no pueda verificar.

## Conversión y rutas

`commercial-conversion-v44.js` conserva el contexto de planes, honorarios y fichas profundas y en v4.9 corrige la reconstrucción de URLs con fragmentos.

Un enlace como:

```text
demo.html#documentos
```

se contextualiza correctamente como:

```text
demo.html?context=...&need=...#documentos
```

y no coloca la query después del fragmento.

## Arquitectura pública

- Portada comercial static-first con seis rutas por necesidad.
- 8 servicios profesionales y 8 productos jurídicos con contenido profundo en HTML.
- 5 planes recurrentes y referencias públicas de honorarios.
- 8 páginas sectoriales.
- 6 perspectivas jurídicas.
- Página institucional de Firma.
- Centro de Demostración.
- Meridiano Empresas con perfiles y datos ficticios, declarado `noindex,nofollow`.
- Páginas legales, sitemap, robots, manifiesto y 404.

## Calidad acumulada

### v4.5 · Portada

`ux-v45.css` y `scripts/apply_ux_v45.py` organizan la narrativa, reducen redundancias y simplifican navegación y CTA.

### v4.6 · Fichas profundas

`detail-v46.css`, `detail-v46.js` y `scripts/apply_detail_ux_v46.py` gobiernan las 16 fichas con navegación ejecutiva, CTA contextual, límites visibles y lectura completa sin JavaScript.

### v4.7 · Editorial, sectores y demos

`editorial-v47.css`, `editorial-v47.js`, `scripts/apply_editorial_ux_v47.py` y `scripts/normalize_editorial_v47.py` unifican Firma, Perspectivas, Sectores, Centro Demo y Meridiano Empresas.

### v4.8 · Static-first, SEO y accesibilidad

`quality-v48.css`, `scripts/apply_quality_v48.py`, `scripts/normalize_quality_v48.py` y `scripts/validate_quality_v48.py` consolidan HTML inicial, rutas, hero WebP, metadata, indexación, sitemap, ARIA, menú móvil y rendimiento.

### v4.9 · Operación pública

- `operations-v49.css`
- `scripts/apply_operations_v49.py`
- `scripts/validate_operations_v49.py`
- `scripts/validate_live_v49.py`

La validación v4.9 comprueba formulario, anti-bot, trazabilidad, contexto, fallback y reconstrucción de fragmentos. El smoke live consulta la URL desplegada y revisa portada, Firma, fichas, Perspectivas, Centro Demo, portal ficticio, JavaScript de conversión, sitemap y robots.

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
python3 scripts/apply_quality_v48.py
python3 scripts/normalize_quality_v48.py
python3 scripts/apply_operations_v49.py
python3 scripts/sync_public_version.py
```

`pages.yml` repite la cadena y valida, entre otros controles:

- idempotencia de generadores;
- HTML, rutas, IDs, anchors y recursos;
- catálogo estático de 16 fichas;
- conversión comercial;
- UX v4.5, v4.6 y v4.7;
- calidad v4.8;
- operación pública v4.9;
- selector guiado;
- contexto y datos estructurados;
- Firma, Perspectivas y Sectores;
- identidad visual;
- sintaxis JavaScript y JSON;
- respuesta real del sitio desplegado.

## Identidad y SEO

La identidad canónica continúa basada en la M arquitectónica de Meridiano Legal, azul marino, marfil y dorado. La portada conserva hero WebP priorizado, `lang="es-CO"`, canonical, Open Graph, Twitter Card y JSON-LD. `demo.html` permanece fuera del sitemap y declara `noindex,nofollow`.

## Desarrollo local

Puede abrirse `index.html` para una revisión básica. Para reproducir el comportamiento de Pages, se recomienda servir el repositorio con un servidor estático y ejecutar previamente la cadena canónica completa.

## Dependencias externas pendientes

La web está preparada para operar sobre GitHub Pages. Un dominio personalizado, correo transaccional, CRM o analítica de terceros solo deben incorporarse cuando exista una decisión explícita sobre proveedor, dominio, tratamiento de datos y configuración. v4.9 no introduce dependencias externas implícitas.

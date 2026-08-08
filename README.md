# Meridiano Legal · Web canónica v5.0.0

Sitio público, responsive y autocontenido de Meridiano Legal, publicado mediante GitHub Pages y preparado para una transición controlada hacia dominio propio, verificación de buscadores y medición comercial cuando existan decisiones y credenciales reales.

## Estado de la release

La v5.0 consolida la web como una base **production-ready dentro de una arquitectura estática**. Esto significa que el sitio público, el catálogo jurídico, el contacto por WhatsApp, SEO, privacidad, configuración, construcción, despliegue y verificación live están gobernados y reproducibles. No significa que se hayan inventado o activado servicios externos que todavía no existen.

La publicación mantiene íntegra la arquitectura comercial y jurídica acumulada: ocho servicios, ocho productos, cinco planes recurrentes, ocho sectores, seis perspectivas, Firma, Centro Demo y Meridiano Empresas.

Actualmente:

- la URL pública canónica es `https://arendon7.github.io/MERDIANOLEGAL/`;
- no hay dominio personalizado configurado;
- WhatsApp continúa siendo el canal real de contacto;
- no hay CRM, backend ni almacenamiento propio del formulario;
- la analítica de terceros está desactivada;
- no hay token de Google Search Console configurado;
- `demo.html` continúa siendo un entorno ficticio y `noindex,nofollow`.

Estas ausencias son deliberadas: v5.0 deja preparada la infraestructura para activarlas correctamente cuando exista un dominio, proveedor, identificador o credencial real.

## Fuente única de configuración pública

`site-config.json` es la fuente canónica de configuración operacional:

```json
{
  "name": "Meridiano Legal",
  "base_url": "https://arendon7.github.io/MERDIANOLEGAL/",
  "deployment": "github-pages",
  "environment": "public",
  "custom_domain": "",
  "contact": {
    "whatsapp": "573008507813"
  },
  "analytics": {
    "enabled": false,
    "provider": "none",
    "site_id": ""
  },
  "search_console_verification": ""
}
```

`scripts/site_config.py` valida la configuración antes de construir: URL HTTPS absoluta, ruta pública, coherencia de dominio, número de contacto, estado de analítica y token opcional de verificación.

La consecuencia principal es que un cambio futuro de dominio no debe resolverse editando manualmente decenas de HTML, canonical, Open Graph, sitemap y robots. La capa v5.0 deriva esos elementos desde esta configuración.

## Dominio personalizado y Search Console

La release está preparada para dominio propio, pero no lo activa sin un dominio real.

Cuando exista un dominio aprobado, el procedimiento canónico será:

1. actualizar `base_url` con la URL HTTPS final;
2. informar el hostname en `custom_domain`;
3. configurar DNS en el proveedor del dominio;
4. dejar que el constructor genere `CNAME` y sincronice canonical, `og:url`, sitemap, robots y contexto;
5. ejecutar toda la matriz de calidad y el smoke live antes de mover `stable`.

`CNAME` solo existe cuando `custom_domain` está configurado. El token de Search Console funciona de igual manera: `search_console_verification` permanece vacío y la meta de verificación solo se publica cuando se incorpora un valor real.

## Runtime y estado público

La capa v5.0 genera dos artefactos operativos:

- `runtime-config.js`: configuración pública segura para JavaScript, sin secretos;
- `site-status.json`: estado verificable de versión, URL, entorno, despliegue, canal de contacto, analítica y política de indexación del demo.

Estos archivos permiten que el smoke post-deploy compruebe no solo que Pages responde, sino que está sirviendo la configuración que corresponde a la release actual.

## Telemetría v5.0: preparada, pero sin transmisión

`telemetry-v50.js` incorpora una capa de instrumentación first-party para preparar medición de funnel sin introducir todavía un proveedor externo.

Actualmente registra únicamente en memoria del navegador, con un máximo acotado de eventos no identificadores:

- `page_view`;
- aperturas de CTA relevantes;
- navegación hacia fichas, sectores, perspectivas o demos;
- `lead_prepared` cuando el flujo de contacto prepara una referencia.

La implementación base no utiliza:

- `fetch`;
- `XMLHttpRequest`;
- `sendBeacon`;
- cookies;
- `localStorage`;
- `sessionStorage` propio de telemetría;
- píxeles ni scripts de analítica de terceros.

`window.MeridianoTelemetry` expone el estado local para diagnóstico. Existe un punto de extensión `MeridianoAnalyticsAdapter`, pero solo podría transmitir si `analytics.enabled` se configura explícitamente en `true` con un proveedor e identificador válidos. La v5.0 mantiene `analytics.enabled=false` y `provider=none`.

## Privacidad v1.1

`privacidad.html` fue actualizada para reflejar con precisión el comportamiento técnico vigente.

La política aclara que:

- el formulario se procesa localmente y no se almacena en un servidor propio;
- abrir WhatsApp no equivale a haber enviado la solicitud;
- el mensaje se considera remitido cuando el usuario confirma el envío dentro de WhatsApp;
- `sessionStorage` puede conservar durante la sesión únicamente contexto de navegación comercial ya utilizado por `page-context.js`;
- la telemetría v5.0 permanece en memoria y no transmite eventos a terceros;
- no se utilizan cookies, `localStorage`, píxeles o `sendBeacon` para esa instrumentación;
- cualquier activación futura de analítica deberá reflejarse previamente en configuración y política.

## Contacto operativo v4.9 preservado

La v5.0 mantiene el flujo operativo validado en v4.9:

- honeypot silencioso;
- límites de longitud y saneamiento;
- referencia `ML-YYYYMMDD-XXXXX`;
- necesidad, contexto comercial y ruta de origen;
- fallback si el navegador bloquea la nueva ventana;
- acceso directo alternativo a WhatsApp;
- mensajes que distinguen correctamente entre abrir WhatsApp y enviar el mensaje.

No se incorpora un backend o CRM ficticio.

## SEO y URLs canónicas

`scripts/apply_production_v50.py` actúa como capa final después de v4.9 y sincroniza:

- canonical de páginas indexables;
- `og:url`;
- política `referrer=strict-origin-when-cross-origin`;
- `sitemap.xml`;
- `robots.txt`;
- ruta pública usada por `page-context.js`;
- verificación Search Console, únicamente si existe token;
- `CNAME`, únicamente si existe dominio configurado.

Las páginas `noindex` no reciben la instrumentación runtime pública. `demo.html` permanece fuera del sitemap.

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
python3 scripts/apply_production_v50.py
```

`Site Quality and Deploy` vuelve a ejecutar la cadena completa y exige diff cero antes de validar:

- integridad HTML, rutas y recursos;
- catálogo estático de 16 fichas;
- conversión comercial v4.4;
- UX v4.5, v4.6 y v4.7;
- calidad static-first v4.8;
- operación pública v4.9;
- **configuración de producción v5.0**;
- selector guiado;
- contexto y datos estructurados;
- Firma, Perspectivas y Sectores;
- sistema visual;
- JavaScript;
- JSON.

Después del deploy, `scripts/validate_live_v50.py` consulta la URL realmente servida y comprueba `site-status.json`, portada, canonical, Firma, fichas, Perspectivas, Privacidad, Demo, runtime, telemetría, conversión, sitemap y robots. `stable` solo se mueve después de superar este smoke.

## Incidencias detectadas durante el cierre v5.0

Las barreras automáticas bloquearon correctamente varios estados intermedios antes de publicación:

1. una carrera inicial dejó `version.json` temporalmente separado del resto del paquete; el cambio completo se reconstruyó sobre el HEAD nuevo sin forzar `main`;
2. la primera salida v5.0 no era idempotente por la posición de `meta referrer` y whitespace de la nueva sección de privacidad;
3. una segunda pasada reveló el caso específico de `<head>` compactados; el normalizador se hizo determinista desde la primera ejecución;
4. el validador visual legado seguía exigiendo la etiqueta “Web demostrativa” en la portada pública; se alineó con `version.json.channel`, manteniendo “Web pública” para el sitio y “Web demostrativa” para componentes demo.

Ninguno de estos controles fue desactivado. La release solo se publicó cuando la construcción produjo diff cero y toda la matriz quedó verde.

## Flujo operativo

- `main`: código vigente y fuente de publicación.
- `stable`: último commit que pasó construcción, idempotencia, validadores, GitHub Pages y smoke live.
- Los cambios funcionales activan `Build canonical public site`.
- Los cambios documentales o de QA pueden pasar directamente por `Site Quality and Deploy` cuando no requieren regenerar salidas.
- Pages despliega únicamente una versión validada.
- `stable` solo avanza después de verificar la URL pública.

## Próximas activaciones externas

La infraestructura queda preparada, pero estas decisiones requieren datos reales antes de ejecutarse:

- dominio personalizado y DNS;
- Google Search Console y su token de verificación;
- analítica real y privacy-friendly, con proveedor e identificador definidos;
- CRM, formulario backend o correo transaccional, si se decide utilizar un canal adicional a WhatsApp.

No deben activarse únicamente para “completar” la arquitectura: cada integración debe tener propósito, configuración verificable, tratamiento de datos documentado y prueba de extremo a extremo.

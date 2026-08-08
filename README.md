# Meridiano Legal · Web canónica v5.3.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.3 conserva íntegra la base jurídica, comercial, CRO y production-ready acumulada hasta v5.2 y añade una capa específica de **autoridad, descubrimiento y preparación de medición**.

## Estado de la release

La publicación mantiene **46 páginas HTML**:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- página institucional de Firma;
- Centro Demo;
- Meridiano Empresas con información ficticia y `noindex,nofollow`;
- 1 hub de soluciones y 6 rutas de decisión empresarial.

La URL pública canónica continúa siendo `https://arendon7.github.io/MERDIANOLEGAL/`. No existe todavía dominio personalizado, CRM, backend propio, analítica de terceros ni token de Search Console. WhatsApp continúa siendo el canal real de contacto.

## v5.3 · Autoridad conectada con decisiones empresariales

Hasta v5.2, las soluciones ya podían conducir al visitante hacia perspectivas y sectores. v5.3 cierra el circuito en sentido inverso: **perspectivas y sectores conducen ahora explícitamente hacia las rutas empresariales que ayudan a convertir una lectura general en una decisión concreta**.

La fuente `authority-v53.json` mapea:

- 6 perspectivas → una o dos rutas de solución relacionadas;
- 8 sectores → una o dos rutas de solución relacionadas;
- las 6 soluciones v5.1/v5.2 quedan cubiertas por el sistema de descubrimiento;
- 8 materias jurídicas canónicas para `Organization.knowsAbout`.

Las páginas editoriales incorporan el bloque **“DE LA LECTURA A LA DECISIÓN”**. Las páginas sectoriales incorporan **“RUTAS POR SITUACIÓN”**. Ninguno de esos bloques sustituye el contenido profundo existente: actúan como capa de continuidad hacia la decisión empresarial.

## Datos estructurados y autoridad semántica

La portada conserva el JSON-LD `Organization` y añade:

- `logo` como `ImageObject` con el logotipo canónico;
- `knowsAbout` con ocho materias: riesgo jurídico empresarial, contratación, sociedades/gobierno/inversión, propiedad intelectual, datos/consumidor, tecnología/IA, proyectos regulados y Legal Operations.

Además:

- `soluciones/` publica un `ItemList` con las seis rutas empresariales;
- cada solución publica un `ItemList` con sus modalidades relacionadas —producto, servicio o capacidad recurrente—;
- cada perspectiva publica un `ItemList` con sus rutas empresariales relacionadas;
- cada sector publica un `ItemList` con las rutas que mejor corresponden a su contexto;
- las seis perspectivas actualizadas en esta release sincronizan `article:modified_time` y `dateModified` con `2026-08-08`.

La arquitectura no crea páginas artificiales para keywords ni duplica la oferta. El objetivo es hacer explícitas relaciones que ya existen jurídicamente entre criterio, contexto sectorial, necesidad y modalidad de intervención.

## Medición CRO preparada, pero sin tracking externo

`measurement-contract-v53.json` define un contrato estable de medición con seis eventos:

1. `solution_view`: carga de una ruta de solución;
2. `authority_open`: paso desde perspectiva o sector hacia una solución;
3. `evidence_open`: paso desde una solución hacia perspectiva o sector;
4. `route_open`: navegación entre soluciones relacionadas;
5. `faq_open`: apertura de una FAQ v5.2;
6. `contact_intent`: intención de pasar desde una solución a contacto o WhatsApp.

Los payloads se limitan a tokens controlados de `stage`, `target` y `need`. El contrato prohíbe expresamente incorporar nombre, correo, empresa, teléfono, mensaje, documentos o contenido del formulario.

`measurement-v53.js` utiliza el bus local `MeridianoTelemetry` de v5.0 y un `CustomEvent` first-party. La capa v5.3 declara y valida:

- `piiAllowed: false`;
- `networkTransport: false`;
- `persistentStorage: false`.

No utiliza `fetch`, `XMLHttpRequest`, `sendBeacon`, cookies, `localStorage` ni `sessionStorage` propio. La analítica externa continúa desactivada en `site-config.json` y Search Console permanece sin token.

Cuando exista un proveedor real, deberá adaptarse a este contrato; no se permitirá redefinir el funnel enviando PII o contenido libre simplemente porque una herramienta externa lo soporte.

## Archivos v5.3

- `authority-v53.json`: mapa canónico perspectiva/sector → solución y materias de autoridad.
- `measurement-contract-v53.json`: contrato de eventos y restricciones de privacidad.
- `measurement-v53.js`: instrumentación first-party sin transporte externo.
- `scripts/apply_authority_v53.py`: wrapper de aplicación + normalización determinista.
- `scripts/apply_authority_v53_core.py`: lógica de autoridad, schema y medición.
- `scripts/validate_authority_v53.py`: gate local de relaciones, schema y contrato de medición.
- `scripts/validate_live_v53.py`: smoke HTTP que conserva v5.2 y comprueba v5.3 sobre la URL servida.

## Construcción canónica

La secuencia vigente culmina así:

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
python3 scripts/apply_cro_v52.py
python3 scripts/apply_authority_v53.py
```

`Site Quality and Deploy` repite la cadena completa y exige **diff cero** antes de validar:

- integridad de 46 páginas y recursos;
- catálogo estático de 16 fichas;
- conversión v4.4;
- UX v4.5, v4.6 y v4.7;
- calidad static-first v4.8;
- operación pública v4.9;
- producción v5.0;
- rutas de decisión v5.1;
- CRO y SEO de intención v5.2;
- autoridad, descubrimiento y medición v5.3;
- selector, contexto, editorial, visual, JavaScript y JSON.

Después del deploy, `scripts/validate_live_v53.py` ejecuta primero todo el smoke v5.2 y luego comprueba portada, hub, seis soluciones, seis perspectivas, ocho sectores y `measurement-v53.js` sobre la URL realmente servida. `stable` solo avanza después de esa verificación.

## Incidencias detectadas durante v5.3

Las barreras volvieron a bloquear estados que no debían publicarse:

1. durante una operación del conector se creó accidentalmente un archivo vacío temporal `__no_such_path__` en `main`; fue eliminado inmediatamente antes de activar el paquete v5.3 y no formó parte de la release aprobada;
2. el primer constructor v5.3 generó correctamente autoridad, schema y medición, pero la segunda pasada falló idempotencia porque perspectivas y sectores alternaban un salto de línea alrededor de los bloques administrados;
3. la lógica funcional se preservó en `apply_authority_v53_core.py` y el aplicador público añadió una normalización determinista de los límites de bloque;
4. la siguiente ejecución produjo diff cero y aprobó toda la matriz v4.4→v5.3, Pages, smoke live y promoción de `stable`.

No se debilitó ningún gate ni se excluyeron archivos de la comprobación de idempotencia.

## Principios que se mantienen

- No inventar clientes, testimonios, casos de éxito ni tasas de éxito.
- No duplicar precios en landings: la fuente monetaria continúa en `#honorarios` y `#planes`.
- No afirmar que la web recibe o almacena formularios en un backend inexistente.
- No activar analítica, Search Console, CRM o dominio personalizado sin datos reales.
- Mantener `main` como fuente vigente y `stable` como último commit desplegado y verificado en vivo.

## Próximo ciclo lógico

La siguiente mejora no debería ser otra capa de contenido por inercia. Con autoridad, rutas, CRO y contrato de eventos ya definidos, el siguiente ciclo útil es **browser/E2E y revisión responsive real**: navegación, menús, filtros, FAQ, CTAs contextuales, formularios, enlaces con query/hash, Centro Demo, Meridiano Empresas, errores de consola y solicitudes 404.

Una vez exista dominio o un proveedor real de medición, esa infraestructura podrá activarse sobre una base cuyo comportamiento y contrato de datos ya están definidos.

# Meridiano Legal v6.1.0 — Measurement Readiness

Fecha de release funcional: 2026-08-18

## Objetivo

v6.1 prepara la observabilidad agregada del funnel de Meridiano Legal sin activar analítica de terceros ni convertir la web pública en un sistema de seguimiento de personas.

La decisión central fue **hacer observable el funnel sin volver observable al usuario**.

La release aprovecha la telemetría local y el funnel ya certificados en v5/v6, añade un adapter privacy-first gobernado y deja la activación de un proveedor como una decisión futura, explícita y condicionada a revisión técnica y jurídica.

## Alcance completado

### 1. Contrato de Measurement Readiness

Se incorporó `assets/data/v6/measurement-readiness-v61.json` como contrato canónico de:

- estado `readiness-disabled`;
- fuente de eventos;
- allowlist de etapas;
- deduplicación;
- límites de privacidad;
- estado de proveedores evaluados;
- requisitos previos a una futura activación.

Producción permanece con:

- `analytics.enabled=false`;
- `provider=none`;
- `site_id=""`.

### 2. Adapter privacy-first

`assets/js/v6/analytics-adapter-v61.js`:

- escucha exclusivamente `meridiano:funnel-v529`;
- acepta únicamente `detail.stage`;
- ignora `event`, `target` y cualquier otro campo;
- conserva `MeridianoAnalyticsAdapter.track(name,event)` como `no-op` por compatibilidad histórica;
- transforma solo seis etapas allowlisted en nombres externos;
- no incorpora propiedades custom;
- deduplica la primera emisión de cada etapa durante la vida de la página;
- no introduce cookies, storage, fingerprinting, `fetch`, XHR o `sendBeacon` propios.

Las etapas posibles son:

- `need`;
- `offer`;
- `evidence`;
- `decision`;
- `contact`;
- `handoff`.

El payload custom aportado por Meridiano queda limitado al nombre del evento.

### 3. Plausible preparado, no activado

Plausible quedó como primer adapter técnicamente preparado, pero:

- no existe site id/token real en producción;
- el proveedor sigue deshabilitado;
- `autoCapturePageviews:false` evita pageviews automáticos;
- la metadata estándar que el proveedor pueda procesar al transmitir un custom event no se confunde con el payload custom de Meridiano y debe revisarse antes de activar;
- cualquier activación exige actualización previa de política y configuración.

Umami quedó evaluado como alternativa no cableada. Cloudflare Web Analytics fue evaluado para pageviews/RUM, pero no seleccionado como solución del funnel custom.

## Topología pública

La materialización v6.1 quedó cerrada con una topología exacta:

- **43 superficies** que ya tenían `telemetry-v50.js` reciben un único adapter v6.1, antes de telemetría;
- **3 superficies** permanecen deliberadamente sin adapter: `404.html`, `demo.html`, `experiencia.html`;
- total clasificado: 46/46 HTML públicos.

No se creó un paso 31. La integración ocurre dentro de la extensión v6 existente y los 30 pasos históricos del builder permanecen intactos.

## Contrato de privacidad preservado

v6.1 no exporta desde Meridiano:

- nombre;
- empresa;
- correo;
- teléfono;
- mensaje;
- referencia de handoff;
- presupuesto;
- urgencia;
- contenido del formulario;
- `event` o `target` del funnel;
- propiedades custom arbitrarias.

Además:

- `contact` no significa mensaje enviado;
- `handoff` no significa mensaje entregado;
- `handoff` no significa propuesta aceptada;
- ningún evento significa cliente convertido.

La política pública no se modificó como si existiera analítica externa activa, porque no existe.

## Release engineering endurecido durante v6.1

v6.1 reveló y cerró varios problemas transversales de release sin desactivar ningún gate.

### 1. Primera materialización v6.1 e idempotencia

Canonical Equivalence pasó a distinguir:

- baseline v6 sin measurement materializado;
- baseline v6.1 ya materializada;
- drift de metadata de release.

La primera transición exige exactamente las superficies esperadas; la segunda pasada debe ser idempotente.

### 2. Sincronización completa de versión

`sync_public_version.py` dejó de ser un reemplazo parcial del rótulo Home y pasó a sincronizar de forma canónica:

- etiquetas `Web pública vX.Y.Z`;
- etiquetas `Web demostrativa vX.Y.Z`;
- etiquetas `Ficha vX.Y.Z`;
- `runtime-config.js`;
- `site-status.json`;
- todos los `<lastmod>` de `sitemap.xml`;
- `article:modified_time` y `dateModified` de perspectivas.

`datePublished` no se altera.

El modo `--check` es fail-closed: detecta drift de release sin escribir.

### 3. Paridad en Candidate, Browser y Measurement

Los gates pre-merge reproducen `sync_public_version.py` antes de validar una baseline v6, evitando certificar `version.json=6.1.0` con runtime, fichas, sitemap o metadata editorial todavía en 6.0.0.

### 4. Canonical Equivalence por conjunto exacto

El gate dejó de depender de una lista rígida de cuatro o cinco archivos de metadata. Ahora calcula:

**cambios esperados = superficies measurement esperadas ∪ drift exacto declarado por `sync_public_version.py --check`**.

El diff real debe coincidir exactamente con ese conjunto.

### 5. Sitemap y contratos v4.8

El bump de release reveló que `sitemap.xml` conservaba `lastmod` del día anterior. El sincronizador pasó a mantener todos los `lastmod` alineados con `version.json.release_date`, preservando el validator v4.8.

### 6. Metadata editorial y contrato v5.3

Las perspectivas conservaban `article:modified_time` y `dateModified` de la release previa. Se incorporó su sincronización con la fecha de release sin alterar `datePublished`, preservando authority/discovery v5.3.

### 7. Carrera de concurrencia Pages/build-output

Después del merge funcional se identificó una carrera potencial:

1. el Builder válido materializa `main`;
2. si hay cambios, genera un commit `build: sincroniza sitio público canónico`;
3. ese commit vuelve a activar Builder, cuyo job se omite por diseño;
4. ambas finalizaciones pueden disparar Pages;
5. con un único `concurrency.group` y `cancel-in-progress:true`, la ejecución ignorada podía cancelar una release válida.

PR #155 separó los runs originados por el commit `build:` en el grupo `ignored-build-output`, manteniendo `cancel-in-progress` para releases reales.

### 8. Corrección YAML del grupo dinámico

La primera versión del hotfix de concurrencia dejó el valor dinámico sin comillas y contenía el literal `build: ...`, lo que podía producir `ScannerError` de YAML.

PR #156 corrigió la expresión envolviendo todo `concurrency.group` entre comillas dobles y endureció `validate_pages_trigger_v511.py` para exigir:

- grupo dinámico quoted;
- aislamiento `ignored-build-output`;
- ausencia del antiguo grupo fijo;
- preservación de `cancel-in-progress:true`.

La incidencia se documenta expresamente como parte del cierre; no se oculta ni se resolvió desactivando controles.

## Evidencia funcional certificada

SHA funcional certificado:

`8ffe0e923fc626281870ca2bd38d6c55a665b31b`

Ese SHA fue promovido automáticamente a `stable` después de la cadena productiva.

Evidencia:

- v6.1.0 materializada en `main`;
- adapter v6.1 presente antes de `telemetry-v50.js` en las superficies aplicables;
- runtime con analytics externa deshabilitada;
- V6 Candidate: PASS;
- V6.1 Measurement Readiness: PASS;
- V6 Browser Candidate: PASS;
- Canonical Builder Equivalence: PASS;
- Release Governance: PASS;
- Graphify: PASS;
- Browser E2E + axe sobre Pages: PASS;
- Lighthouse sobre Pages: PASS con budgets existentes;
- `stable` promovido automáticamente al SHA funcional;
- cobertura reducida: no;
- budgets relajados: no;
- tests eliminados para aprobar la release: no.

## PRs del ciclo

- **#154** — Measurement Readiness v6.1, privacy firewall, exact topology, release metadata parity y gates.
- **#155** — aislamiento de la carrera de concurrencia Pages/build-output.
- **#156** — corrección YAML quoted del grupo dinámico y guard de regresión.

## Invariantes preservados

v6.1 mantiene:

- 46 HTML públicos;
- 8 productos + 8 servicios;
- 7 superficies de soluciones;
- 8 sectores;
- 6 perspectivas + hub;
- 16 fichas profundas;
- un único formulario físico canónico;
- WhatsApp manual;
- 30 pasos históricos exactos;
- portal real deshabilitado;
- sin auth, CRM, pagos, firma, agenda o upload ficticios;
- analytics externa deshabilitada;
- funnel/measurement sin PII ni propiedades custom exportadas;
- contacto/handoff sin equivalencia automática con conversión;
- Browser, axe y Lighthouse sin relajación.

## Canal definitivo

El cierre documental cambia el canal de:

`github-pages-measurement-readiness-candidate`

A:

`github-pages-production-measurement-readiness-certified`

Este cambio describe el estado de certificación. **No activa Plausible ni ningún otro proveedor.**

## Condición de cierre definitivo

v6.1.0 queda documentalmente cerrada únicamente cuando el commit que contiene:

- `RELEASE-v6.1.md`;
- README v6.1;
- `CONTEXTO_RAPIDO.md`;
- `ESTADO_ACTUAL.md`;
- `TAREA_ACTIVA.md`;
- canal `certified` en `version.json`;
- hotfixes de topología #155 y #156 ya presentes en la base;

atraviese nuevamente los gates aplicables, Builder → Pages → smoke → Browser/axe → Lighthouse → release-health/snapshot y termine con `main == stable`.

## Próximo ciclo

No se activa automáticamente analytics ni se abre una v6.2 por inercia.

El próximo ciclo debe partir de una necesidad observable o de una decisión explícita de negocio. Si el siguiente paso es activar medición real, deberá existir proveedor e identificador auténticos, revisión de metadata estándar, actualización previa de política/configuración, validación exacta de tráfico saliente y nueva certificación completa.

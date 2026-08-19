# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Frente vigente

**v7.0.0 — cierre documental / `candidate → certified`.**

Rama:

`docs/v700-release-closure`

La release funcional **Meridiano Legal Intelligence v7.0.0 ya está publicada y certificada**. Este frente no añade funcionalidades ni cambia la oferta pública: únicamente convierte la metadata y memoria de release desde candidate a certified y vuelve a someter ese cierre a la cadena completa de certificación.

## Baseline funcional certificada

Antes de abrir este cierre:

- `main == stable == 291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`;
- versión pública: **7.0.0**;
- PR funcional: **#167**, fusionado;
- candidate final pre-merge: `50646aadb514611241c0210a6bcfaac8ba7fe2d8` — 9/9 workflows verdes;
- merge funcional: `6b655fbf502196473a0457fd8e47d0c29e74ab41`;
- Builder productivo: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`;
- GitHub Pages completó quality, deploy, live smoke, Browser/axe y Lighthouse antes de promover `stable` automáticamente;
- `stable` no se movió manualmente.

## Arquitectura funcional cerrada

Meridiano Legal permanece como marca madre. **Meridiano Legal Intelligence** es una capa transversal que organiza:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece como concepto futuro/no producto público.

La capa v7 se materializa en 11 superficies existentes y conserva las seis rutas públicas v6. Los 8 productos y 8 servicios canónicos continúan gobernando entregables, tiempos, honorarios, responsabilidades y límites.

## Alcance exacto de este cierre

El cierre debe modificar únicamente estas siete fuentes documentales/metadata:

1. `version.json`;
2. `assets/data/v7/legal-intelligence-architecture-v70.json`;
3. `README.md`;
4. `RELEASE-v7.0.md`;
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`;
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`;
7. `knowledge/00_CANON/TAREA_ACTIVA.md`.

Cambios permitidos:

- canal `github-pages-legal-intelligence-candidate` → `github-pages-production-legal-intelligence-certified`;
- contrato arquitectónico `release-candidate` → `certified`;
- documentación de SHAs y evidencia de promoción funcional;
- memoria canónica del ciclo.

## Fuera de alcance

Este cierre **no debe** modificar:

- HTML público;
- catálogos de productos o servicios;
- precios, tiempos, entregables, responsabilidades o límites;
- materializadores v7;
- validators v7, salvo que apareciera una inconsistencia real de fase previamente no cubierta;
- tests E2E;
- workflows de producción;
- portal, auth, CRM, pagos, firma, agenda o upload;
- los seis recorridos públicos de solución.

## Capability truth preservado

- Contract Control y Regulatory Control siguen siendo patrones de implementación/operación, no SaaS autónomos;
- no existe CLM productivo implícito;
- no se promete monitoreo automático universal;
- no se prometen certificaciones técnicas no incluidas;
- no se garantizan permisos, licencias o decisiones de autoridades;
- Legal Desk mantiene SLA, canales y capacidad sujetos al alcance pactado;
- Meridiano Counsel continúa fuera de la oferta pública;
- agentes, automatizaciones, integraciones y herramientas solo se incluyen cuando el encargo lo establece expresamente.

## Gate del cierre documental

Una vez abierto el PR de `docs/v700-release-closure` contra `main`:

1. comprobar que el diff contiene exactamente las siete fuentes anteriores;
2. fijar el SHA final del cierre;
3. exigir nuevamente todos los workflows aplicables sobre ese mismo SHA;
4. no reutilizar la certificación del candidate funcional como sustituto de la certificación del cierre;
5. solo después de gates verdes, marcar ready y fusionar con `expected_head_sha`;
6. observar el Builder post-merge y capturar el SHA canónico resultante;
7. dejar que Pages ejecute quality → deploy → live smoke → Browser/axe + Lighthouse → snapshot;
8. no mover `stable` manualmente.

## Criterio de cierre definitivo

v7.0.0 queda totalmente cerrada solo cuando:

- el PR documental haya sido fusionado;
- `main` y `stable` vuelvan a coincidir en el SHA canónico posterior al cierre;
- `stable/version.json` declare `github-pages-production-legal-intelligence-certified`;
- el contrato arquitectónico permanezca en `status: certified`;
- no exista drift funcional ni reducción de cobertura.

Después de ese punto:

- cerrar PR #163 **sin merge** como superseded por #167 y la reconciliación sobre v6.4;
- no abrir otra versión por inercia;
- cualquier nuevo ciclo debe partir de una necesidad observable de negocio, conversión, contenido u operación jurídica.

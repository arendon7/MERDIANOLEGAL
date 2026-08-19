# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**Cierre documental v7.2.0 — Buying Clarity candidate → certified.**

Rama: `docs/v720-certified-closure`.

## Evidencia previa ya cerrada

### Funcional #174

- SHA funcional final: `5e9b04487b92b0e47327d1f61880d2a4ac48c629`.
- Gates funcionales: 9/9 PASS.
- Merge funcional: `0b8211ce9aeecda737bec0a11af50496cc6aeccf`.

### Candidate #175

- SHA candidate: `f11329f40cfcd7d097ff16019dcb462dd97acc70`.
- Gates candidate: 10/10 PASS.
- Merge candidate: `a5d14d34cd73aa2772a66adfd6d5ea0f07c34a2e`.
- Builder canónico: `356f755db67a678142769b3a80ee69837679648d`.
- Pages quality/deploy/live smoke, Browser/axe y Lighthouse: PASS.
- `stable` promovido automáticamente a `356f755db67a678142769b3a80ee69837679648d`.
- `stable/version.json`: 7.2.0 canal `github-pages-buying-clarity-candidate` antes de este cierre.

## Boundary del cierre

Exactamente siete fuentes de metadata/documentación:

1. `version.json` → `github-pages-production-buying-clarity-certified`.
2. `assets/data/v7/buying-clarity-v72.json` → `status: certified`.
3. `README.md`.
4. `RELEASE-v7.2.md`.
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`.
7. `knowledge/00_CANON/TAREA_ACTIVA.md`.

No tocar HTML, CSS, catálogos, materializadores, validators funcionales, E2E, workflows ni capabilities.

## Gate del cierre

1. confirmar boundary exacto de siete archivos;
2. fijar SHA final;
3. superar nuevamente todos los workflows aplicables same-SHA;
4. fusionar solo con `expected_head_sha`;
5. observar Builder canónico;
6. completar Pages quality/deploy/live smoke → Browser/axe + Lighthouse;
7. permitir únicamente promoción automática de `stable`;
8. terminar con `main == stable` y canal production-certified.

`stable` no se mueve manualmente.

## Siguiente frente tras el cierre

**Centro Demo — Legal Intelligence Scenarios.**

Objetivo: que un comprador pueda ver, con datos enteramente ficticios, cómo se materializan cinco capacidades:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

El demo debe conectar problema → workflow → artefacto → resultado → siguiente decisión, manteniendo:

- etiqueta DEMO visible;
- datos ficticios;
- procesamiento local cuando aplique;
- cero carga de información real;
- cero auth/portal productivo implícito;
- cero Meridiano Counsel;
- cero precios nuevos;
- cero monitoreo automático universal;
- ningún output presentado como asesoría o resultado real de cliente.

# Release v7.2.0 — Buying Clarity

Fecha: 2026-08-19.

## Objetivo

Hacer explícitamente comprables las 16 ofertas profundas de Meridiano Legal sin modificar los catálogos jurídicos canónicos, introducir precios no aprobados ni convertir capacidades de Legal Intelligence en software autónomo.

## Cambio funcional

Cada ficha de producto/servicio incorpora un **Resumen de contratación** inmediatamente después del hero con:

- modalidad;
- horizonte/cadencia;
- destinatario;
- hasta cuatro elementos principales del perímetro;
- hasta cuatro entregables principales;
- hasta dos requisitos para iniciar;
- hasta dos criterios de aceptación/cierre;
- hasta dos ampliaciones/continuidades, expresamente no incluidas salvo pacto.

La información se deriva exclusivamente de `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.

## Evidencia funcional

- Baseline v7.1 certificado: `0a01942c9a2b7868768e0b454af5a600c65ad01a`.
- SHA funcional final: `5e9b04487b92b0e47327d1f61880d2a4ac48c629`.
- Gates funcionales same-SHA: 9/9 PASS.
- PR funcional #174 fusionado con `expected_head_sha`.
- Merge funcional: `0b8211ce9aeecda737bec0a11af50496cc6aeccf`.

## Candidate formal

- SHA candidate: `f11329f40cfcd7d097ff16019dcb462dd97acc70`.
- Gates aplicables same-SHA: 10/10 PASS.
- PR #175 fusionado con `expected_head_sha`.
- Merge candidate: `a5d14d34cd73aa2772a66adfd6d5ea0f07c34a2e`.
- Builder canónico: `356f755db67a678142769b3a80ee69837679648d`.
- Pages quality/deploy/live smoke: PASS.
- Browser E2E/axe desplegado: PASS.
- Lighthouse: PASS.
- `stable` promovido automáticamente a `356f755db67a678142769b3a80ee69837679648d`.

## Correcciones de composición

Durante el desarrollo se corrigieron, sin relajar gates:

1. duplicación transitoria de navegación a `#v6-engagement`;
2. reaplicación de Buying Clarity tras reconstrucciones v6;
3. normalización de whitespace de stylesheet para no consumir saltos vecinos;
4. coexistencia idempotente entre Engagement v6.3, Fit & Scope v6.4 y Buying Clarity v7.2;
5. lifecycle monotónico de v7.1 certificada para permitir releases posteriores sin invalidar capas anteriores.

## Invariantes

- 8 productos + 8 servicios canónicos permanecen intactos;
- seis rutas públicas permanecen intactas;
- no se publican precios nuevos;
- Contract Control y Regulatory Control no se presentan como SaaS autónomos;
- Legal Desk no equivale a acceso a software ni bolsa de horas ilimitada;
- AI Governance 360 no sustituye controles técnicos;
- Meridiano Counsel continúa fuera de la oferta pública;
- no se habilitan portal/auth/upload/CRM/firma/pagos/agenda;
- no se promete monitoreo automático universal.

## Cierre certified

El cierre documental cambia únicamente metadata y memoria:

- `version.json` → `github-pages-production-buying-clarity-certified`;
- `assets/data/v7/buying-clarity-v72.json` → `status: certified`;
- README y memoria canónica actualizados;
- este documento de release.

La release queda definitivamente cerrada cuando este propio cierre supere nuevamente todos los gates, se fusione con SHA protegido y la cadena productiva termine otra vez con `main == stable` y `stable/version.json` en canal production-certified.

## Siguiente frente

**Centro Demo — Legal Intelligence Scenarios**: escenarios ficticios y artefactos demostrativos para Legal AI Transformation, Contract Control, AI Governance 360, Regulatory Control y Meridiano Legal Desk, sin representar funcionalidades productivas no habilitadas.

# Meridiano Legal · Web canónica v7.2.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v7.2.0 — Buying Clarity** sobre **Meridiano Legal Intelligence**.

La release hace explícitamente comprables las 16 ofertas profundas sin modificar su verdad jurídica: cada ficha muestra inmediatamente después del hero un **Resumen de contratación** derivado de los catálogos canónicos.

### Evidencia de release

- Baseline certificado anterior v7.1.0: `0a01942c9a2b7868768e0b454af5a600c65ad01a`.
- SHA funcional v7.2: `5e9b04487b92b0e47327d1f61880d2a4ac48c629` — 9/9 gates verdes.
- Merge funcional #174: `0b8211ce9aeecda737bec0a11af50496cc6aeccf`.
- Candidate formal 7.2.0: `f11329f40cfcd7d097ff16019dcb462dd97acc70` — 10/10 gates verdes.
- Merge candidate #175: `a5d14d34cd73aa2772a66adfd6d5ea0f07c34a2e`.
- Builder/snapshot productivo candidate: `356f755db67a678142769b3a80ee69837679648d`.
- Pages quality → deploy → live smoke → Browser/axe + Lighthouse → snapshot: PASS.
- `stable` fue promovido automáticamente a `356f755db67a678142769b3a80ee69837679648d`; no se movió manualmente.
- Canal de cierre: `github-pages-production-buying-clarity-certified`.

## Qué hace Buying Clarity

Las 8 fichas de producto y 8 fichas de servicio hacen visible, antes de entrar a toda la profundidad jurídica:

1. modalidad;
2. duración o cadencia;
3. destinatario;
4. principales cantidades del perímetro;
5. principales entregables;
6. requisitos para empezar;
7. criterios de cierre o verificación de prestación;
8. rutas de ampliación o continuidad, expresamente fuera del alcance base salvo pacto.

La fuente de verdad continúa siendo exclusivamente:

- `catalog-products-v41/*.json`;
- `catalog-services-v42/*.json`.

Buying Clarity no introduce precios, cantidades, entregables o capacidades nuevas.

## Arquitectura preservada

Meridiano Legal permanece como marca madre. **Meridiano Legal Intelligence** continúa como capa transversal, no como catálogo paralelo.

Capacidades organizadas:

- Legal AI Diagnostic;
- Legal AI Transformation;
- Meridiano Legal Desk;
- Contract Control;
- Regulatory Control;
- AI Governance 360;
- Legal Engineering Studio.

`Meridiano Counsel` permanece fuera de la oferta pública.

## Capability truth

- seis rutas públicas preservadas;
- 8 productos + 8 servicios canónicos preservados;
- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada bajo alcance pactado;
- AI Governance 360 no sustituye auditoría técnica, seguridad o evaluación científica;
- no existe monitoreo automático universal implícito;
- portal real, auth, CRM, pagos, firma, agenda y upload permanecen deshabilitados/no implementados;
- Legal Engineering incorpora desarrollo o integraciones solo cuando se pactan expresamente;
- no se publicaron tarifas nuevas.

## Compatibilidad y calidad

v7.2 conserva:

- v7.1 Commercial Clarity;
- v7.0 Legal Intelligence;
- v6.4 Fit & Scope Clarity;
- v6.3 Engagement Clarity;
- v6.2 Search Discovery;
- v6.1 Measurement privacy-first;
- v6.0 Experience System;
- 46 superficies HTML, 16 fichas profundas, seis rutas públicas y un único formulario físico canónico.

La composición v6.3/v6.4/v7.2 fue endurecida para mantener primera pasada canónica e idempotencia sin tolerar drift.

## Release engineering v7.2

- `assets/data/v7/buying-clarity-v72.json`: contrato source-driven y phase-aware.
- `knowledge/20_DESIGN/BUYING-CLARITY-v72.md`: brief de producto/UX.
- `scripts/apply_buying_clarity_v72.py`: materialización determinista.
- `scripts/validate_buying_clarity_v72.py`: validación source-truth, capability boundaries y lifecycle.
- `scripts/normalize_experience_compat_v60.py`: recomposición canónica.
- `tests/e2e/buying-clarity-v72.spec.mjs`: regresión en las 16 fichas.
- `.github/workflows/v72-buying-clarity-candidate.yml`: gate dedicado.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial.
- `assets/data/v7/`: contratos Legal Intelligence / Commercial Clarity / Buying Clarity.
- `knowledge/00_CANON/`: memoria operativa actual.

## Siguiente frente

Después del cierre certificado v7.2, la siguiente ola es **Centro Demo — Legal Intelligence Scenarios**: mostrar con datos ficticios cómo se materializan Legal AI Transformation, Contract Control, AI Governance 360, Regulatory Control y Meridiano Legal Desk. Debe permanecer claramente DEMO, sin carga real de información, sin portal productivo implícito y sin ampliar capabilities.

Ver `RELEASE-v7.2.md` para evidencia y límites de la release.

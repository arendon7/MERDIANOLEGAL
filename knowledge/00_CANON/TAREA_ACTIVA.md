# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.2.0 — Buying Clarity / release candidate.**

Rama: `release/v720-buying-clarity-candidate`.

La fase funcional quedó certificada y fusionada mediante PR #174.

- SHA funcional certificado: `5e9b04487b92b0e47327d1f61880d2a4ac48c629`.
- Merge funcional: `0b8211ce9aeecda737bec0a11af50496cc6aeccf`.
- 9/9 workflows aplicables verdes sobre el SHA funcional.
- Baseline anterior certificado: v7.1.0.

## Qué cambia en v7.2

Las 16 fichas profundas incorporan inmediatamente después del hero un **Resumen de contratación** construido exclusivamente desde los catálogos canónicos de 8 productos + 8 servicios.

Hace visible, antes de recorrer toda la profundidad jurídica:

1. modalidad;
2. duración/cadencia;
3. destinatario;
4. principales cantidades del perímetro;
5. principales entregables;
6. requisitos para empezar;
7. criterios de cierre o verificación de prestación;
8. rutas de ampliación/continuidad expresamente no incluidas salvo pacto.

## Fuente de verdad

- `catalog-products-v41/*.json`;
- `catalog-services-v42/*.json`;
- `knowledge/20_DESIGN/BUYING-CLARITY-v72.md`;
- `assets/data/v7/buying-clarity-v72.json`.

No se modifica el contenido jurídico canónico ni se introducen tarifas nuevas.

## Arquitectura e idempotencia

- `scripts/apply_buying_clarity_v72.py`: materialización source-driven.
- `scripts/validate_buying_clarity_v72.py`: truth + capability boundaries + lifecycle.
- `scripts/normalize_experience_compat_v60.py`: reaplica Buying Clarity después de reconstrucciones v6.
- `scripts/apply_engagement_clarity_v63.py`: compatibilidad de composición de stylesheet sin cambio de truth.
- `tests/e2e/buying-clarity-v72.spec.mjs`: cobertura de las 16 fichas.
- `.github/workflows/v72-buying-clarity-candidate.yml`: gate específico.

El ciclo funcional resolvió la coexistencia v6.3/v6.4/v7.2 sin tolerar drift: Canonical Builder terminó con first-pass boundary e idempotencia verdes.

## Candidate formal

Este branch cambia únicamente lifecycle/release metadata respecto de la funcionalidad ya fusionada:

- `version.json`: 7.1.0 → 7.2.0, canal `github-pages-buying-clarity-candidate`;
- `assets/data/v7/buying-clarity-v72.json`: prototype → `release-candidate`;
- `scripts/validate_buying_clarity_v72.py`: lifecycle phase-aware `prototype → release-candidate → certified`;
- esta memoria de tarea.

No debe introducir cambios nuevos en HTML, CSS funcional, catálogos o capacidades.

## Capability truth preservado

- Meridiano Legal permanece como marca madre;
- Legal Intelligence continúa como capa transversal;
- seis rutas públicas y 8 productos + 8 servicios canónicos permanecen intactos;
- no crear SaaS, CLM, CRM, portal, firma, pagos, agenda, upload o monitoreo automático implícito;
- Meridiano Counsel permanece fuera de oferta pública;
- suplementos y ampliaciones no se presentan como incluidos;
- no introducir tarifas sin pricing truth aprobado.

## Gate del candidate

Antes de merge:

1. fijar SHA final;
2. superar todos los workflows aplicables sobre ese mismo SHA;
3. fusionar únicamente con `expected_head_sha`;
4. observar Builder canónico;
5. exigir Pages quality/deploy → live smoke → Browser/axe + Lighthouse;
6. permitir únicamente promoción automática de `stable`;
7. terminar con `main == stable` antes del cierre documental.

`stable` no se mueve manualmente.

## Fase 2 pendiente

Después de certificar productivamente v7.2 fase 1, mejorar el **Centro Demo** para mostrar cómo se materializan Legal AI Transformation, Contract Control, AI Governance 360, Regulatory Control y Legal Desk mediante escenarios ficticios, artefactos y resultados demostrativos. Todo debe quedar marcado como DEMO y sin presentar Meridiano Empresas como capability productiva no habilitada.

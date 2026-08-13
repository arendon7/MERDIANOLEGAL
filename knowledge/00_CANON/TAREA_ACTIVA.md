# Meridiano Legal — Tarea activa

Actualizado: 2026-08-13.

## Estado

**v5.24.0 — orquestación canónica verificable: activa.**

Baseline funcional certificado: `stable = 8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca` (v5.23.0).

Baseline documental al abrir el ciclo: `main = 71ce6a39b6207f38554920bfeea7d9d045e9652d`.

## Problema observable

La secuencia de composición pública está declarada en más de un lugar: builder, segunda pasada de Pages y encadenamientos internos de releases posteriores. Durante v5.23 esta fragmentación expuso incompatibilidades de orden y de estado materializado en capas históricas. Graphify registra 75 scripts Python, por lo que seguir agregando rutas de ejecución independientes aumenta el riesgo de drift.

## Objetivo

Crear una única fuente de verdad ejecutable para el orden de composición canónica y hacer que builder y segunda pasada/idempotencia consuman esa misma secuencia.

## Contrato v5.24

1. `scripts/canonical_pipeline_v524.py` declara una secuencia ordenada, identificable y sin pasos duplicados.
2. Build canónico y segunda pasada de Pages invocan el mismo orquestador.
3. Los scripts históricos siguen existiendo y conservan sus contratos; v5.24 no los fusiona ni reescribe por conveniencia.
4. Release Governance valida la estructura del orquestador y vigila directamente sus archivos.
5. El sitio público no debe cambiar intencionalmente como consecuencia de esta release.
6. Ningún budget, validator, E2E, axe gate o requisito de promoción a `stable` se reduce.

## No objetivos

- no rediseño visual;
- no cambios de copy, precios, productos, servicios o firma;
- no backend, CRM, portal real, storage, PII, scoring ni red nueva;
- no eliminación masiva de scripts históricos;
- no alteración retrospectiva del contrato funcional v5.23.

## Criterios de cierre

- manifiesto/orquestador v5.24 validado;
- builder consume una sola secuencia canónica;
- segunda pasada consume exactamente la misma secuencia;
- builder completo PASS;
- idempotencia PASS;
- todos los validators históricos PASS;
- Pages + smoke PASS;
- Browser E2E/axe sin reducción de cobertura PASS;
- Lighthouse 6/6 dentro de budgets vigentes;
- release-health PASS;
- solo entonces promoción de `stable`;
- documentación y Graphify frescos antes del cierre formal.

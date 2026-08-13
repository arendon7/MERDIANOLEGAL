# Meridiano Legal — Tarea activa

Actualizado: 2026-08-13.

## Estado

**v5.24.0 — orquestación canónica verificable: activa.**

Baseline funcional certificado: `stable = 8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca` (v5.23.0).

Baseline documental al abrir el ciclo: `main = 71ce6a39b6207f38554920bfeea7d9d045e9652d`.

## Problema observable

La secuencia de composición pública está declarada en más de un lugar: builder, segunda pasada de Pages y encadenamientos internos de releases posteriores. Durante v5.23 esta fragmentación expuso incompatibilidades de orden y de estado materializado en capas históricas. Graphify registra 75 scripts Python, por lo que seguir agregando rutas de ejecución independientes aumenta el riesgo de drift.

## Objetivo

Establecer una fuente de verdad declarativa y ejecutable para el orden canónico y convertir cualquier divergencia entre builder, segunda pasada y manifiesto en un fallo verificable del pipeline.

## Contrato v5.24

1. `scripts/canonical_pipeline_v524.py` declara los 30 pasos canónicos, con identidad, orden y comando normalizado.
2. El manifiesto compara la secuencia real de `build-canonical.yml` y la segunda pasada de `pages.yml`; ambas deben coincidir exactamente con esos 30 pasos.
3. `apply_handoff_observability_v518.py`, ya ejecutado por builder, Pages y Governance, activa este guard para `version >= 5.24.0`.
4. Los workflows siguen explícitos en esta release; v5.24 no modifica Actions ni permisos. El objetivo es eliminar drift silencioso antes de cualquier futura migración de ejecución.
5. Los scripts históricos siguen existiendo y conservan sus contratos; v5.24 no los fusiona ni reescribe por conveniencia.
6. El sitio público no debe cambiar intencionalmente como consecuencia de esta release.
7. Ningún budget, validator, E2E, axe gate o requisito de promoción a `stable` se reduce.

## No objetivos

- no rediseño visual;
- no cambios de copy, precios, productos, servicios o firma;
- no backend, CRM, portal real, storage, PII, scoring ni red nueva;
- no eliminación masiva de scripts históricos;
- no modificación de permisos, triggers ni estructura de GitHub Actions;
- no alteración retrospectiva del contrato funcional v5.23.

## Criterios de cierre

- manifiesto v5.24 declara exactamente 30 pasos únicos;
- builder == segunda pasada == manifiesto en contenido y orden;
- cualquier drift probado produce fallo determinista;
- builder completo PASS;
- idempotencia PASS;
- todos los validators históricos PASS;
- Pages + smoke PASS;
- Browser E2E/axe sin reducción de cobertura PASS;
- Lighthouse 6/6 dentro de budgets vigentes;
- release-health PASS;
- sitio público sin cambio funcional intencional;
- solo entonces promoción de `stable`;
- documentación y Graphify frescos antes del cierre formal.

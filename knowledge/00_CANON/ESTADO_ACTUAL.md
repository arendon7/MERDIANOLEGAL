# Meridiano Legal — Estado canónico

Última verificación funcional: 2026-08-18.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance**.
- SHA funcional certificado: `0045588f795f5f0a0b9144786bc61cdf89f34319`.
- Canal de cierre: `github-pages-production-fit-scope-clarity-certified`.
- La referencia documental definitiva se obtiene por los refs vigentes `main` y `stable`, que deben coincidir después de este cierre documental.

## Resultado v6.4

v6.4 eleva a primer nivel dos matrices de verdad jurídica/comercial que ya existían en los 16 catálogos y ayudan al comprador a reconocer encaje y cambios previsibles de alcance.

### Encaje y cambio de alcance

- 16/16 fichas profundas gobernadas.
- 8/8 productos y 8/8 servicios.
- Cada ficha incorpora exactamente una sección `#v6-fit-scope`.
- La sección está situada después de Resultado y antes de Entregables.
- `situations` se presenta como **Señales de que esta modalidad encaja**.
- `supplements` se presenta como **Situaciones que amplían el alcance**.
- Las filas visibles coinciden exactamente y en orden con el catálogo canónico correspondiente.
- El TOC conserva exactamente los 7 hitos de v6.3 y no contiene `#v6-fit-scope`.
- No se alteran `perimeter`, `limits`, entregables, método, honorarios, cronogramas o contacto.

### Capas previas preservadas

- Engagement Clarity v6.3: 16/16 fichas con `requirements` + `responsibilities` y `#v6-engagement`.
- Search Discovery v6.2: 43 indexables + 3 `noindex`; sitemap canónico de 43 URLs.
- Measurement v6.1: privacy-first, sin PII exportada y analytics externa deshabilitada.
- Experience System v6.0: 46/46 superficies estructurales preservadas.
- 1/1 formulario físico canónico.
- WhatsApp manual.
- Portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados.
- 30/30 pasos históricos exactos del builder.

## Evidencia funcional

- SHA técnico pre-bump: `ecc90b17f0784f53fb4a035c3d91d2ff2938e627` — 6/6 gates técnicos aplicables verdes.
- Candidate final 6.4.0: `38c140f5ec943f6a527f88278e78d2e9a7cb0bd1`.
- Nueve workflows aplicables sobre ese SHA: PASS:
  - V6.4 Fit & Scope Clarity;
  - V6.3 Engagement Clarity;
  - V6.2 Search Discovery Readiness;
  - V6.1 Measurement Readiness / Browser E2E;
  - V6 Candidate Validation;
  - V6 Canonical Builder Equivalence;
  - Release Governance;
  - Graphify;
  - V6 Browser Candidate / axe.
- PR #162 fusionado con expected head SHA.
- Merge funcional: `8937a985c94e9f29f6dafbc6a53ab8ff5cb24ee0`.
- Builder post-merge produjo `0045588f795f5f0a0b9144786bc61cdf89f34319`.
- GitHub Pages público sirve v6.4.0.
- Smoke público, Browser/axe y Lighthouse: PASS.
- `stable` fue promovido automáticamente a `0045588f…` después del snapshot oficial.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para aprobar la release: no.

## Incidencia productiva

El primer run oficial de Pages (`32203459870`) falló únicamente en Lighthouse porque `demo` respondió HTTP 503 de forma transitoria. Quality, deploy, smoke y Browser E2E ya habían pasado, por lo que snapshot quedó `skipped`.

Se abrió #164 como diagnóstico temporal no desplegable. Contra la URL pública se reprodujeron en verde smoke, Browser/axe y Lighthouse. #164 se cerró sin merge.

Se reejecutaron los jobs fallidos del mismo run oficial, sin modificar código. Lighthouse pasó; el snapshot generó la certificación CI y el health report de gobernanza; `Move stable to deployed commit` terminó success.

No se introdujeron retries laxos en los budgets, no se cambió el producto y no se movió `stable` manualmente.

## Release engineering endurecido durante v6.4

1. **Truth reutilizado, no duplicado.** El renderer consume `situations` y `supplements` directamente de los catálogos v4.1/v4.2.
2. **Validación fila por fila.** La representación HTML debe coincidir exactamente y en orden con su fuente canónica.
3. **Boundary exacto.** La transición modifica únicamente las 16 fichas previstas; ninguna otra superficie recibe `#v6-fit-scope`.
4. **TOC deliberadamente estable.** v6.4 no agrega un octavo hito; la sección se descubre dentro del recorrido natural Resultado → Entregables.
5. **Idempotencia CSS.** La hoja v6.4 se inserta en posición estable frente a v6.3/tokens para evitar order drift.
6. **Equivalencia exacta.** Canonical Equivalence incorpora `fit/scope drift` al conjunto `measurement ∪ release ∪ discovery ∪ engagement ∪ fit/scope`.
7. **Builder == Pages == manifiesto.** `canonical_pipeline_v524.py` registra los mismos comandos v6.4 sin alterar los 30 pasos históricos.
8. **Trigger coverage.** `validate_pages_trigger_v511.py` exige que el materializador v6.4 dispare Builder.
9. **Measurement integrado.** La suite privacy-first materializa v6.4 antes de Browser E2E; la corrección no redujo pruebas ni expectativas.
10. **Gate phase-aware desde origen.** 0/16 exige 16 drift; 16/16 exige 0; cualquier estado parcial falla.

## PR principal

- #162 — Fit & Scope Clarity v6.4: contrato, renderer, validator, estilos, gates, E2E, integración canónica y release candidate.
- #164 — diagnóstico temporal post-deploy; cerrado sin merge.

## Invariantes preservadas

46 HTML; 16 fichas profundas; 1 formulario físico; WhatsApp manual; portal real deshabilitado; analytics externa deshabilitada; Search Console no verificada sin token real; no PII; no criterios de encaje inventados; no tarifas inventadas; exactamente 30 pasos históricos; Browser/axe/Lighthouse sin relajación; `stable` solo después de gates verdes.

## Estado del ciclo

**v6.4.0 está implementada, materializada, publicada y certificada funcionalmente. El frente restante es exclusivamente este cierre documental `candidate → certified`. Cuando el commit de cierre atraviese Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y `main == stable`, no queda un ciclo funcional nuevo abierto.**

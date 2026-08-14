# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**No existe un ciclo funcional activo. v5.29.0 — funnel observable y confianza contextual — está cerrada funcionalmente y en proceso de cierre documental certificado.**

Baseline funcional certificada:

`main = stable = 8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70` (v5.29.0, antes del commit documental final).

## Qué quedó resuelto en v5.29

1. Funnel observable unificado: `awareness → need → offer → evidence → decision → contact → handoff`.
2. Cola limitada a 48 eventos y mantenida únicamente en memoria.
3. Cero lectura de valores del formulario y cero PII, persistencia, identificador cross-session, fingerprinting o transporte de red nuevo.
4. Checkpoints de portada y cobertura de las 16 fichas profundas mediante `data-catalog-id`.
5. Umbral observable contractual de 5% de superficie visible, válido para secciones más altas que el viewport móvil.
6. Límites semánticos expresos: contacto/handoff no equivalen a envío, aceptación, encargo ni cliente convertido.
7. `<aside>` compacto de confianza entre `#contratacion` y `#contacto`, derivado exclusivamente de `professional-authority-v525.json`.
8. Invariante v5.28 preservada: `#contacto` continúa siendo la siguiente `<section>` narrativa después de `#contratacion`.
9. Pipeline canónico preservado en exactamente 30 pasos, con v5.29 encadenada después de v5.28 dentro de `v5.18+`.
10. Validator, E2E, axe, Lighthouse, Pages, Release Governance e idempotencia verdes.

## Evidencia funcional

- SHA: `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`.
- Builder: `31823965908`.
- Site Quality and Deploy: `31823985048`.
- Release Governance final relevante: `31823922160`.
- Browser E2E/axe: 88 observados · 86 PASS · 2 SKIP · 0 FAIL · 0 retries.
- Lighthouse: PASS.
- promoción de `stable`: PASS.

## Fuentes v5.29

- `funnel-contract-v529.json`.
- `funnel-observability-v529.js`.
- `funnel-trust-v529.css`.
- `scripts/apply_funnel_trust_v529.py`.
- `scripts/validate_funnel_trust_v529.py`.
- `tests/e2e/funnel-trust-v529.spec.mjs`.
- `knowledge/10_DECISIONES/ADR-003-funnel-trust-v529.md`.
- `knowledge/00_CANON/RELEASE-v5.29.md`.

## Siguiente ciclo

No se abre automáticamente una v5.30. Debe partir del SHA documental finalmente certificado de v5.29 y declarar un problema observable nuevo antes de modificar la arquitectura.

## Cierre pendiente de esta rama documental

Cambiar canal a `github-pages-production-funnel-trust-certified`, aceptar ADR-003, sincronizar memoria canónica y registrar release note. Ese commit documental debe recorrer nuevamente Release Governance, builder, idempotencia, 37 validaciones, Pages/smoke, Browser E2E/axe, Lighthouse, promoción de `stable` y Graphify. Solo ese SHA será la referencia definitiva de v5.29.

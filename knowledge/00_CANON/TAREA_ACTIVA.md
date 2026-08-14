# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**No existe un ciclo funcional activo. v5.29.0 — funnel observable y confianza contextual — está implementada, publicada, certificada, documentada y cerrada.**

La baseline para cualquier trabajo posterior es la release 5.29.0 en canal `github-pages-production-funnel-trust-certified`. Antes de iniciar un nuevo ciclo deben verificarse `main`, `stable`, `version.json` y `knowledge/graphify-live/graphify-out/BUILD_META.json`.

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
10. Validator, E2E, axe, Lighthouse, Pages, Release Governance, idempotencia y promoción de `stable` verdes.

## Evidencia de cierre

- Builder documental: `31824748343`.
- Site Quality and Deploy #375: `31824770838`.
- Graphify documental: `31824748359`.
- Pipeline canónico: 30 pasos PASS.
- Idempotencia: PASS.
- Validaciones estáticas: 37/37 PASS.
- Pages + smoke: PASS.
- Browser E2E/axe: PASS.
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

No se abre automáticamente una v5.30. Un nuevo ciclo debe declarar primero un problema observable y conservar como baseline todos los invariantes ya certificados. No debe reinterpretar las señales v5.29 como conversiones reales ni habilitar capacidades externas sin contrato, implementación y QA propios.

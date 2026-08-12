# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Capas vigentes

v5.8 claridad de compra → v5.9 calificación → v5.10 propuesta/cierre → v5.11 engagement readiness → v5.12 prueba verificable → v5.13 continuidad comercial → v5.14 recomendación explicable → v5.15 recomendación→acción → hardening v5.16 → v5.17 continuidad manual del handoff → **v5.18 observabilidad verificable del handoff**.

## Estado funcional v5.18

- Release declarada: `5.18.0`.
- PR fuente: #67.
- Merge fuente: `3dd01285bcb28a568e2d5a65e2fa88ad284142cb`.
- SHA funcional materializado/certificado: `a082b4d9139ae929367cac0085597365e75dbaaf`.
- Run funcional: `31631855996`.
- Antes del cierre documental: `main == stable == a082b4d9139ae929367cac0085597365e75dbaaf`.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY; 7 superficies axe limpias.
- Lighthouse: 6/6 PASS; accesibilidad 1.00 en las seis superficies; performance 0.98–1.00; `accessibilityAuditGaps` vacío.
- CI: 200 s hasta `stable`, 28.3% mejor que baseline v5.5 de 279 s.
- cobertura reducida: no; budgets relajados: no.

## Qué hace v5.18

Mide exclusivamente seis hechos verificables dentro de la página: handoff preparado, reapertura solicitada, copia exitosa, copia fallida, edición solicitada y borrador stale.

El runtime transforma señales internas únicamente a `stage/target` y usa `MeridianoTelemetry`. No introduce PII, contenido de formulario, referencia, resumen, URL de WhatsApp, storage persistente, cookies, identificadores cross-session, fetch/XHR/sendBeacon, backend, CRM ni analítica externa.

La web no puede inferir y v5.18 prohíbe representar como eventos: envío, entrega, lectura, aceptación de propuesta, inicio del encargo o conversión completada.

## Fuentes principales

- `handoff-observability-v518.json` — contrato de seis eventos y límites de privacidad;
- `handoff-observability-v518.js` — runtime de medición local;
- `scripts/apply_handoff_observability_v518.py` / `validate_handoff_observability_v518.py` — composición y contrato v5.18;
- `handoff-continuity-v517.js` — señales internas del handoff manual;
- `measurement-contract-v53.json` / `telemetry-v50.js` — telemetría first-party/local;
- `tests/e2e/` — Browser + axe;
- `quality-budgets-v55.json` + `scripts/run_quality_v55.mjs` — Lighthouse/budgets;
- workflows builder, Pages y Release Governance.

## Secuencia de release

fuentes → builder canónico → capas comerciales hasta v5.18 → idempotencia/validators → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Graphify

Graphify conserva el `source_commit` realmente extraído. Si el builder genera un commit exclusivo de sincronización visible tras este cierre, documentar equivalencia por comparación real; no falsificar procedencia.

## Regla de continuidad

Antes de cualquier ciclo futuro: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir solo el conjunto mínimo de archivos afectados. Este cierre no inicia v5.19.

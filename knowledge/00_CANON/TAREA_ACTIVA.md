# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release en cierre formal

**v5.18.0 — observabilidad verificable del handoff manual.**

La funcionalidad ya está certificada. Esta tarea únicamente formaliza la versión y alinea documentación/memoria canónica con el estado real del repositorio.

Evidencia funcional previa al cierre documental:

- PR #67;
- merge fuente `3dd01285bcb28a568e2d5a65e2fa88ad284142cb`;
- SHA funcional `a082b4d9139ae929367cac0085597365e75dbaaf`;
- run `31631855996`;
- `main == stable` en ese SHA;
- validators históricos + v5.17 + v5.18: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse 6/6 PASS, a11y 1.00 en seis superficies, `accessibilityAuditGaps` vacío;
- CI hasta `stable`: 200 s, 28.3% mejor que baseline 279 s;
- cobertura reducida: no;
- budgets relajados: no.

## Contrato v5.18

Se observan únicamente seis acciones locales verificables: preparado, reapertura solicitada, copia exitosa, copia fallida, editar y borrador stale.

No se transmite ni almacena PII, contenido del formulario, referencia, resumen o URL WhatsApp. No se introduce red nueva, storage persistente, cookies, identificador cross-session, CRM/backend ni analítica externa.

Nunca inferir ni registrar como hechos: mensaje enviado/entregado/leído, propuesta aceptada, encargo iniciado o conversión completada.

## Condición de finalización

1. mergear este cierre formal 5.18.0;
2. dejar que el builder sincronice la versión visible;
3. certificar el SHA generado final con idempotencia y todos los validators;
4. Pages + smoke;
5. Browser E2E + axe;
6. Lighthouse;
7. release-health;
8. promoción de `stable`;
9. confirmar `main == stable`;
10. revisar procedencia Graphify y documentar equivalencia si el único delta posterior es output/versionado generado.

## No objetivos

- no v5.19;
- no nuevas features;
- no backend/CRM;
- no automatización externa de WhatsApp;
- no PII nueva;
- no persistencia nueva;
- no relajar budgets, axe o E2E.

Cuando los diez puntos estén verdes, **la tarea queda finalizada**.

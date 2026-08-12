# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Release en cierre formal: `5.18.0`.
- Merge fuente funcional: `3dd01285bcb28a568e2d5a65e2fa88ad284142cb`.
- SHA funcional certificado antes del cierre documental: `a082b4d9139ae929367cac0085597365e75dbaaf`.
- Run funcional final: `31631855996`.
- Estado de refs antes del cierre documental: `main == stable == a082b4d9139ae929367cac0085597365e75dbaaf`.

Refs, Pages, validators y tests son la autoridad para el estado productivo.

## Estado funcional

**v5.18 está implementada, desplegada y funcionalmente certificada; este cambio formaliza el versionado y corrige la memoria canónica que todavía la describía como no iniciada.**

### Observabilidad v5.18

El contrato `handoff-observability-v518.json` define exactamente seis hechos observables: `handoff_prepared`, `handoff_reopen_requested`, `handoff_copy_succeeded`, `handoff_copy_failed`, `handoff_edit_requested` y `handoff_draft_stale`.

El runtime usa únicamente `stage` y `target` sobre la cola local existente. Permanecen en `false`: PII permitida, transporte nuevo, storage persistente, identificador cross-session y contenido del formulario.

No son hechos conocidos por la web y están expresamente prohibidos como eventos: envío, entrega, lectura, aceptación de propuesta, inicio del encargo y conversión completada.

v5.17 sigue siendo la capa que gestiona el borrador manual/efímero, reabrir, copiar, editar y stale protection. v5.18 solo observa acciones verificables de esa superficie.

## Evidencia funcional final v5.18

Run `31631855996`, SHA `a082b4d9139ae929367cac0085597365e75dbaaf`:

- builder/idempotencia + validators históricos + v5.17 + v5.18: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- reporter Browser: 82 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance: portada 1.00, solución IA 1.00, producto IA 1.00, sector tecnología 0.98, perspectiva IA 0.98, demo 1.00;
- `accessibilityAuditGaps`: vacío;
- CI hasta `stable`: 200 s;
- baseline v5.5: 279 s;
- mejora: 28.3%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos:
- Lighthouse `9155454712`, `sha256:9d82ef0cfd5ec470ce66111d95fbf99518e9e6e1f8f233e78fa07598849ae659`;
- CI `9155489175`, `sha256:169f15d32fb09f9be53c0bb40c39167b16e099d63f0f5ac2757e0df514ed727e`;
- release-health `9155489589`, `sha256:eefe9976b09ea64aac499c00f8e8b00db1668cf2ce597256c24c250c2f50d205`.

## Contratos vigentes

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- analítica externa apagada (`provider:none`);
- WhatsApp manual;
- sin CRM/backend, almacenamiento servidor, firma, pagos, agenda o portal documental ficticios;
- `stable` solo después de gates verdes.

## Graphify / procedencia

Graphify debe conservar el `source_commit` realmente extraído. Si el builder genera un commit posterior exclusivamente de sincronización visible de 5.18.0, la equivalencia se documenta por comparación y no mediante alteración artificial de `source_commit`.

## Gate de cierre formal

El SHA que contiene este versionado debe volver a pasar builder, idempotencia, Pages, smoke, Browser/axe, Lighthouse, release-health y promoción de `stable`, terminando en `main == stable`. No se inicia v5.19 dentro de esta tarea.

# Meridiano Legal v5.18.0 — observabilidad verificable del handoff manual

Fecha: 2026-08-12.

## Objetivo

Medir únicamente hechos que la web estática sí conoce después de preparar el handoff manual a WhatsApp, sin convertir señales locales en afirmaciones falsas sobre envío, entrega, lectura, aceptación, contratación o conversión.

## Alcance

v5.18 añade un contrato propio de observabilidad para seis hechos:

1. `handoff_prepared` — borrador válido preparado;
2. `handoff_reopen_requested` — usuario solicita reabrir WhatsApp;
3. `handoff_copy_succeeded` — navegador confirma copia explícita;
4. `handoff_copy_failed` — navegador no logra copiar;
5. `handoff_edit_requested` — usuario vuelve a editar la solicitud;
6. `handoff_draft_stale` — el formulario cambia y el borrador queda desactualizado.

El runtime traduce señales internas únicamente a `stage` y `target` y reutiliza `MeridianoTelemetry`, que continúa siendo first-party/local.

## Límites semánticos y privacidad

v5.18 no registra nombre, correo, empresa, teléfono, mensaje, contenido del formulario, referencia, resumen ni URL de WhatsApp. No introduce `fetch`, XHR, `sendBeacon`, cookies, `localStorage`, `sessionStorage`, identificador cross-session, backend, CRM ni proveedor de analítica externa.

Quedan expresamente prohibidos como hechos observables: `handoff_sent`, `handoff_delivered`, `handoff_read`, `proposal_accepted`, `engagement_started` y `conversion_completed`.

La capa v5.17 conserva el handoff manual, el borrador efímero y la protección contra borrador desactualizado. v5.18 solo observa acciones verificables dentro de la página.

## Gobierno y QA

Builder, Pages y Release Governance terminan en v5.18. El validator comprueba contrato, privacidad, eventos permitidos/prohibidos, wiring, sintaxis JS, analítica externa apagada y cobertura E2E. La suite protegida continúa en 37 entradas.

## Evidencia funcional certificada

Fuente funcional: PR #67 / merge `3dd01285bcb28a568e2d5a65e2fa88ad284142cb`.

SHA funcional materializado y promovido a `stable`: `a082b4d9139ae929367cac0085597365e75dbaaf`.

Run Pages final funcional: `31631855996`.

- `main == stable == a082b4d9139ae929367cac0085597365e75dbaaf`;
- idempotencia + validadores históricos + v5.17 + v5.18: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- Browser reporter: 82 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- `accessibilityAuditGaps`: vacío en las seis superficies;
- performance: 1.00 portada, solución IA, producto IA y demo; 0.98 sector tecnología y perspectiva IA;
- CI hasta `stable`: 200 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 28.3%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos de referencia:

- Lighthouse `9155454712`, digest `sha256:9d82ef0cfd5ec470ce66111d95fbf99518e9e6e1f8f233e78fa07598849ae659`;
- CI `9155489175`, digest `sha256:169f15d32fb09f9be53c0bb40c39167b16e099d63f0f5ac2757e0df514ed727e`;
- release-health `9155489589`, digest `sha256:eefe9976b09ea64aac499c00f8e8b00db1668cf2ce597256c24c250c2f50d205`.

## Contratos preservados

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- WhatsApp como handoff manual;
- telemetría sin PII;
- analítica externa desactivada;
- `stable` solo después de todos los gates verdes.

## Procedencia

Graphify debe conservar el `source_commit` realmente extraído. Si este cierre formal provoca un commit generado exclusivamente para sincronizar la versión visible, su equivalencia se documentará mediante comparación real y no reescribiendo la procedencia.

## Condición de cierre definitivo

El SHA versionado 5.18.0 debe volver a superar builder, idempotencia, Pages, smoke, Browser/axe, Lighthouse, release-health y promoción de `stable`, terminando en `main == stable`. No se inicia v5.19 dentro de este cierre.

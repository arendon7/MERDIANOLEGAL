# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente.

## Qué es el proyecto

Sitio público y centro demostrativo de Meridiano Legal. Combina servicios jurídicos especializados, productos de alcance cerrado, planes recurrentes, rutas por necesidad, sectores, perspectivas y una experiencia demo estática.

## Arquitectura comercial y de calidad vigente

- 8 servicios especializados;
- 8 productos de alcance cerrado;
- 5 planes recurrentes;
- 6 rutas de decisión en `soluciones/` más su hub;
- 8 sectores;
- 6 perspectivas más biblioteca;
- Firma/método y Centro Demo;
- v5.8 claridad de compra;
- v5.9 calificación comercial y privacidad;
- v5.10 propuesta/cierre contextual;
- v5.11 solicitud, propuesta, aceptación e inicio real;
- v5.12 5 modalidades + prueba verificable;
- v5.13 continuidad de modalidad/prueba hasta formulario y WhatsApp;
- v5.14 recomendación explicable con `scoring:false`;
- v5.15 consolidación recomendación→acción;
- v5.16 UX móvil + accesibilidad verificable + observabilidad Lighthouse;
- v5.17 continuidad manual del handoff a WhatsApp + borrador efímero + protección stale + hardening de composición.

Principio comercial: el contexto debe sobrevivir hasta la conversación comercial y cualquier recomendación debe poder explicarse sin puntajes opacos ni cambios automáticos de etapa. La web no debe declarar entrega, lectura, aceptación o inicio que no puede verificar.

## Estado funcional v5.17

- Release declarada en este cierre: `5.17.0`.
- SHA funcional certificado: `56f99a5398b1e0505da5acd601bac3aec8588c1d`.
- Run funcional final: `31628244159`.
- Antes del cierre documental: `main == stable == 56f99a5398b1e0505da5acd601bac3aec8588c1d`.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY; 7 superficies axe limpias.
- Lighthouse: 6/6 PASS; accesibilidad `1.00` en las seis superficies; `accessibilityAuditGaps` vacío.
- Portada: performance 1.00 / a11y 1.00 / LCP 1276 ms / CLS 0 / TBT 1 ms.
- Producto IA: performance 1.00 / a11y 1.00 / LCP 919 ms / CLS 0 / TBT 0 ms.
- CI: 181 s hasta `stable`, 35.1% mejor que baseline v5.5 de 279 s.
- cobertura reducida: no; budgets relajados: no.

## Qué hizo v5.17

1. conserva un único formulario físico canónico en `index.html`;
2. las 16 fichas profundas preservan modalidad, estándar de prueba e intención mediante rutas contextuales a `index.html#contacto`;
3. después de preparar la solicitud muestra referencia y acciones manuales para reabrir WhatsApp, copiar resumen o editar;
4. elimina la copia automática silenciosa al portapapeles;
5. mantiene el borrador solo en memoria de la página, sin storage persistente ni transporte propio;
6. si cambia el formulario, marca el borrador como desactualizado y bloquea copiar/reabrir hasta prepararlo de nuevo;
7. evita repetir nombre, empresa, email o mensaje completo dentro del panel DOM;
8. declara que la web no conoce entrega, lectura, aceptación contractual, apertura de expediente ni inicio del encargo;
9. endurece applicator, Pages y Governance para que v5.17 sea idempotente y pueda reparar outputs materializados rotos sin debilitar validators históricos.

## Defectos reales detectados durante el ciclo

- `bed3baf0…` / Pages `31622876902`: fallo de idempotencia porque Pages terminaba en v5.15;
- `b9387731…` / Pages `31623621877`: ID `handoff-v517-title` duplicado, panel residual y cierre de formulario perdido;
- PR #65 reparó limpieza semántica, cierre canónico y preflight Governance;
- candidato final `56f99a53…`: todos los gates verdes.

## Fuentes principales

- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica;
- `measurement-contract-v53.json` — telemetría sin PII;
- `recommendation-v514.json` — explicación canónica sin scoring;
- `decision-action-v515.*` — consolidación y rutas comerciales;
- `handoff-continuity-v517.css` / `.js` — superficie y runtime del handoff manual;
- `scripts/apply_handoff_v517.py` / `validate_handoff_v517.py` — composición, reparación y contratos v5.17;
- `proof-v512.css` — hardening de targets/contraste en fichas profundas;
- `quality-budgets-v55.json` + `scripts/run_quality_v55.mjs` — Lighthouse/budgets/diagnóstico;
- `tests/e2e/` — Browser + axe;
- workflows builder, Pages y Release Governance.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15 → hardening v5.16 → v5.17 → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Graphify

Graphify debe conservar el `source_commit` realmente extraído. El cierre formal 5.17.0 debe reconstruir/alinear la memoria desde el commit real correspondiente. Si el builder genera después un commit exclusivo de sincronización visible, la equivalencia debe demostrarse por comparación y documentarse sin falsificar procedencia.

## Gate de transición

El siguiente ciclo no inicia por el solo cambio de `version.json`. El SHA que contiene este cierre 5.17.0 debe volver a atravesar builder, sincronización visible, Pages, Browser/axe, Lighthouse, release-health, alineación Graphify y terminar con `main == stable`.

## Próximo ciclo candidato

**v5.18 — no iniciado.** El alcance se definirá únicamente después del cierre formal. Como dirección preliminar puede auditarse la medición y continuidad comercial posterior al handoff, siempre sin inventar CRM/backend, automatizaciones externas o PII nueva.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

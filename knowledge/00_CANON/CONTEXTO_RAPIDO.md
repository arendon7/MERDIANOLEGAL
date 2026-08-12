# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente.

## Qué es el proyecto

Sitio público y centro demostrativo de Meridiano Legal. Combina servicios jurídicos especializados, productos de alcance cerrado, planes recurrentes, rutas por necesidad, sectores, perspectivas y una experiencia demo estática.

## Arquitectura comercial vigente

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
- v5.14 recomendación explicable: encaje, límite y alternativa, con `scoring:false`;
- v5.15 consolidación recomendación→acción y ruta comercial controlada por el usuario.

Principio comercial: el contexto debe sobrevivir hasta la conversación comercial y cualquier recomendación debe poder explicarse sin puntajes opacos ni cambios automáticos de etapa.

## Estado productivo

- Versión: `5.15.0`.
- `main == stable == 2dd960fe168f2d15665e4fa695267b2746d58cba`.
- Run final: `31610848709`.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY; 7 superficies axe limpias.
- Lighthouse: 6/6; portada 1.00 performance / 0.97 accesibilidad / LCP 1250 ms / CLS 0 / TBT 8 ms.
- CI: 211 s hasta `stable`, 24.4% mejor que baseline 279 s.
- cobertura reducida: no; budgets relajados: no.
- Graphify: `source_commit = cccf2e9e…`, versión 5.15.0, 544 nodos / 877 relaciones / 88 notas; equivalente estructuralmente al SHA productivo final, un commit generado por delante.

## Fuentes principales

- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica;
- `measurement-contract-v53.json` — telemetría sin PII;
- `recommendation-v514.json` — explicación canónica sin scoring;
- `decision-action-v515.*` — consolidación y rutas comerciales;
- `quality-budgets-v55.json` + `scripts/run_quality_v55.mjs` — Lighthouse/budgets;
- `tests/e2e/` — Browser + axe;
- workflows builder, Pages y Release Governance.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15 → futuras capas → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Tarea activa

**v5.16 — UX móvil y accesibilidad del recorrido comercial.**

Prioridad inicial: el runner actual solo conserva el score Lighthouse agregado. v5.16 debe registrar auditorías de accesibilidad con score < 1 y sus nodos relevantes; después corregir causas reales y compactar móvil sin ocultar contenido material.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

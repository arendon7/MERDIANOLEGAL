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
- v5.14 recomendación explicable: encaje, límite y alternativa, con `scoring:false`.

Principio comercial: el usuario puede empezar por su situación empresarial; el contexto debe sobrevivir hasta la conversación comercial y cualquier recomendación debe poder explicarse sin puntajes opacos.

## Fuentes principales

- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica de productos/servicios;
- `measurement-contract-v53.json` — telemetría sin PII;
- capas `decision-v58`, `commercial-intake-v59`, `conversion-close-v510`, `engagement-v511`;
- `proof-v512.css` + applicator/validator v5.12 — modalidad y prueba derivada de fuente;
- `commercial-brief-v513.*` + applicator/validator v5.13 — continuidad comercial;
- `recommendation-v514.json`, `.css`, `.js` + applicator/validator v5.14 — recomendación explicable sin scoring;
- `scripts/validate_pages_trigger_v511.py` — topología builder→Pages;
- `release-governance-v57.json`;
- `tests/e2e/`.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Estado actual resumido

- Versión declarada en este cierre: v5.14.0.
- Funcionalidad v5.14 certificada en run `31570619885`, SHA `42e482241a818e0c94137810e1224558a58f397d`.
- Antes del cierre documental: `main == stable` en ese SHA.
- Browser E2E + axe: PASS sobre 37 entradas protegidas y 7 superficies axe.
- Lighthouse: 6/6 dentro de budget.
- CI: 264 s hasta `stable`, 5.4% mejor que baseline v5.5 de 279 s.
- cobertura reducida: no; budgets relajados: no.
- Release Governance, trigger builder→Pages y validator v5.14: PASS.
- v5.14 no añade cuestionario, storage, backend, fetch/XHR ni PII.
- No hay aceptación contractual, pagos, agenda, expediente, carga documental ni inicio automático desde la web pública.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

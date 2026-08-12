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

- Versión productiva: v5.14.0.
- SHA final: `9435f65ca129099a8a59f12ec5fd2f9e3aa58762`.
- `main == stable` en ese SHA.
- Run final: `31571937528`.
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY; 7 superficies axe limpias.
- Lighthouse: 6/6 dentro de budget; portada 1.00 performance / 0.97 a11y / LCP 1232 ms.
- CI: 202 s hasta `stable`, 27.6% mejor que baseline v5.5 de 279 s.
- cobertura reducida: no; budgets relajados: no.
- Release Governance, trigger builder→Pages y validator v5.14: PASS.
- Graphify: fuente `547b97e2…`, 513 nodos / 818 relaciones / 85 notas; el SHA final está un commit generado por delante con solo 28 outputs versionados, equivalencia estructural documentada.
- v5.14 no añade cuestionario, storage, backend, fetch/XHR propio ni PII.
- No hay aceptación contractual, pagos, agenda, expediente, carga documental ni inicio automático desde la web pública.

## Tarea activa

**v5.15 — Eficiencia recomendación→acción.**

Reducir solapamiento entre selección, explicación y CTA; mejorar jerarquía y escaneabilidad; conservar el contexto hacia propuesta/WhatsApp; no añadir cuestionario, scoring, storage o backend.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

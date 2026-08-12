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
- v5.16 UX móvil + accesibilidad verificable + observabilidad Lighthouse.

Principio comercial: el contexto debe sobrevivir hasta la conversación comercial y cualquier recomendación debe poder explicarse sin puntajes opacos ni cambios automáticos de etapa. Compactar móvil no autoriza eliminar límites, exclusiones, prueba verificable ni condiciones de inicio.

## Estado funcional v5.16

- Release declarada en este cierre: `5.16.0`.
- SHA funcional certificado: `2cd5fb0d2b428187c08cf21e562427f9bc44508c`.
- Run funcional final: `31618614227`.
- Antes del cierre documental: `main == stable == 2cd5fb0d2b428187c08cf21e562427f9bc44508c`.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY; 7 superficies axe limpias.
- Lighthouse: 6/6 PASS; accesibilidad `1.00` en las seis superficies; `accessibilityAuditGaps` vacío.
- Portada: performance 1.00 / a11y 1.00 / LCP 1255 ms / CLS 0 / TBT 7 ms.
- Producto IA: performance 1.00 / a11y 1.00 / LCP 905 ms / CLS 0 / TBT 0 ms.
- CI: 187 s hasta `stable`, 33.0% mejor que baseline v5.5 de 279 s.
- cobertura reducida: no; budgets relajados: no.

## Qué hizo v5.16

1. Lighthouse conserva auditorías de accesibilidad con score < 1 y detalles acotados en sus resúmenes;
2. tres CTA de Perspectivas pasan a targets táctiles >=44 px;
3. en móvil, detalle secundario v5.10/v5.11 se agrupa en `<details>` nativos sin eliminar contenido;
4. regiones horizontalmente desplazables son accesibles por teclado y tienen nombre accesible;
5. se corrigió contraste móvil expuesto por axe;
6. menú, enlaces y CTA de ficha profunda cumplen targets/contraste móvil;
7. portada y ficha profunda se auditan en viewport 390×844 dentro del conteo E2E existente.

## Fuentes principales

- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica;
- `measurement-contract-v53.json` — telemetría sin PII;
- `recommendation-v514.json` — explicación canónica sin scoring;
- `decision-action-v515.*` — consolidación, rutas y hardening móvil v5.16;
- `proof-v512.css` — hardening final de targets/contraste en fichas profundas;
- `quality-budgets-v55.json` + `scripts/run_quality_v55.mjs` — Lighthouse/budgets/diagnóstico;
- `tests/e2e/` — Browser + axe;
- workflows builder, Pages y Release Governance.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15 → hardening v5.16 → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Graphify

El snapshot funcional más reciente apunta exactamente a `source_commit = 2cd5fb0d2b428187c08cf21e562427f9bc44508c`, Graphify 0.9.26, 548 nodos, 882 relaciones y 88 notas. Su campo declarativo de versión aún refleja 5.15.0 porque fue construido antes de elevar `version.json`; el cierre formal debe reconstruirlo sin falsificar `source_commit`.

## Gate de transición

El siguiente ciclo no inicia por el solo cambio de `version.json`. El SHA que contiene este cierre 5.16.0 debe volver a atravesar builder, sincronización visible, Pages, Browser/axe, Lighthouse, release-health y terminar con `main == stable`.

## Próximo ciclo candidato

**v5.17 — continuidad del handoff comercial.** Auditar y simplificar la transición entre resumen preparado, WhatsApp manual y expectativa de respuesta, especialmente en móvil, sin backend, CRM, envío automático, storage persistente adicional ni PII nueva.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

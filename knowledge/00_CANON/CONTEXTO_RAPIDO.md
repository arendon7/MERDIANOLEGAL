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
- v5.12 5 modalidades + prueba verificable en las 16 fichas;
- v5.13 conserva modalidad + estándar verificable hasta formulario y WhatsApp.

Principio comercial: el usuario puede empezar por su situación empresarial y el contexto útil debe sobrevivir hasta la conversación comercial sin pedirle repetirlo.

## Diferenciaciones que no deben perderse

- Diagnóstico jurídico ≠ Auditoría Jurídica Empresarial Integral.
- Dirección Jurídica Externa ≠ disponibilidad jurídica ilimitada.
- Contratación Estratégica ≠ Sistema Contractual Empresarial.
- Sociedades/Gobierno/Inversión ≠ Empresa Lista para Inversión.
- Propiedad Intelectual como servicio ≠ paquete cerrado de activos protegidos.
- Gobernanza jurídica de IA como servicio ≠ programa cerrado de gobernanza.
- Proyecto regulado como servicio ≠ producto estructurado de alcance cerrado.
- Legal Operations ≠ Dirección Jurídica Externa.

## Fuentes principales

- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica de productos/servicios;
- `measurement-contract-v53.json` — telemetría sin PII;
- capas `decision-v58`, `commercial-intake-v59`, `conversion-close-v510`, `engagement-v511`;
- `proof-v512.css` + applicator/validator v5.12 — modalidad y prueba derivada de fuente;
- `commercial-brief-v513.css`, `commercial-brief-v513.js` + applicator/validator v5.13 — continuidad de modalidad/prueba;
- `scripts/validate_pages_trigger_v511.py` — topología builder→Pages sin carrera directa por push;
- `release-governance-v57.json`;
- `tests/e2e/`.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Estado actual resumido

- Versión declarada en este cierre: v5.13.0.
- Funcionalidad v5.13 certificada en run `31568876368`, SHA `e77a7e824117d3f8f3f67cc3fc71f11f3fc858c3`.
- Antes del cierre documental: `main == stable` en ese SHA.
- Browser: 35 passed / 2 skipped / 0 failed / 0 retries sobre 37 entradas.
- axe: 7 superficies sin violaciones serias/críticas.
- Lighthouse: 6/6 dentro de budget.
- CI: 177 s hasta `stable`, 36.6% mejor que baseline v5.5 de 279 s.
- Release Governance, trigger builder→Pages y validator v5.13: PASS.
- Correcciones de composición certificadas: tipo `Servicio profesional`; rutas v5.12 por path/fragment tolerando query params aditivos.
- La capa v5.13 no añade storage, backend ni PII.
- No hay aceptación contractual, pagos, agenda, expediente, carga documental ni inicio automático desde la web pública.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

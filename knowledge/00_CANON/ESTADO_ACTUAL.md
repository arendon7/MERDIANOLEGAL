# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-11.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en cierre: `5.9.0`.
- Evidencia funcional v5.9 previa al cierre: run `31547313170`, SHA `a64d2d957e3ca6c96fec855be85019680ebe6a03`.

Los SHA actuales de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; los refs, Pages y gates son la autoridad.

## Estado funcional

**La implementación funcional v5.9 está certificada. El commit documental que declara 5.9.0 debe volver a atravesar la certificación pública completa antes de considerarse release definitiva.**

La cadena vigente exige:

- construcción e idempotencia canónica;
- validadores históricos v4.4→v5.7;
- contrato de decisión v5.8;
- contrato de calificación comercial/privacidad v5.9;
- 46 páginas y recursos;
- catálogo de 16 fichas;
- JavaScript y JSON;
- GitHub Pages + smoke público;
- Browser E2E, axe y seis Lighthouse;
- resumen CI y release-health;
- promoción de `stable` únicamente con ambos rails pesados verdes.

## v5.9 — Calificación comercial y propuesta

El formulario público añade tres datos estructurados:

1. momento de decisión;
2. horizonte para decidir o iniciar;
3. rango de inversión jurídica previsto, opcional.

Antes del handoff se presenta un resumen que combina el contexto comercial v5.8, la necesidad seleccionada y la nueva información. La web orienta el siguiente paso como `Orientación inicial`, `Llamada de alcance` o `Propuesta estructurada`.

No existe un score de valor del lead, rechazo automático ni promesa de aceptación. La clasificación orienta el proceso comercial y no constituye asesoría, cotización, aceptación del encargo, reserva de disponibilidad ni promesa de resultado.

La web sigue siendo estática: no guarda el formulario en servidor. Los datos de calificación solo se incorporan al texto cuando el usuario decide abrir WhatsApp. La telemetría no debe contener nombre, correo, empresa ni texto libre del caso.

## Compatibilidad de construcción v5.9

Los gates bloquearon dos incompatibilidades antes de `stable`:

- v4.9 exigía una firma exacta del `<form>` y no toleraba el atributo añadido por v5.9; el generador se volvió extensible sin perder sus invariantes históricas;
- el builder ejecutaba v5.8 nuevamente después de v5.9 y cambiaba el orden final de la capa visual; la cadena quedó corregida para terminar en `v5.8 → v5.9`.

Governance ahora vigila también el generador v4.9 y prueba explícitamente la composición `v4.9 → v5.9`. No se redujo cobertura ni se relajaron pruebas.

## Evidencia funcional v5.9 previa al cierre

Run `31547313170`, SHA `a64d2d957e3ca6c96fec855be85019680ebe6a03`:

### Browser E2E + axe

- 37 entradas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 0 retries;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe sin violaciones serias/críticas.

El test de contacto valida el flujo v5.9 dentro de la cobertura existente, incluida preparación de WhatsApp y ausencia de PII en telemetría.

### Lighthouse

- portada: performance 1.00, a11y 0.97, LCP 1286 ms, CLS 0, TBT 0 ms, 80,365 B;
- solución IA: 1.00 / 1.00, LCP 1011 ms, CLS 0, TBT 0 ms, 23,195 B;
- producto IA: 1.00 / 1.00, LCP 1005 ms, CLS 0, TBT 0 ms, 35,409 B;
- sector tecnología: 0.98 / 1.00, LCP 1005 ms, CLS 0.087, TBT 0 ms, 24,220 B;
- perspectiva IA: 0.98 / 1.00, LCP 904 ms, CLS 0.087, TBT 0 ms, 25,814 B;
- demo: 1.00 / 1.00, LCP 1095 ms, CLS 0, TBT 0 ms, 22,073 B.

Las seis superficies aprobaron sin relajar presupuestos.

### Eficiencia CI

- baseline v5.5: 279 s;
- run funcional v5.9: 196 s hasta `stable`;
- mejora: 29.7%;
- cobertura reducida: no;
- presupuestos relajados: no.

## Contratos preservados

- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- gate dual Browser + Lighthouse;
- idempotencia;
- Actions inventariadas y fijadas a SHA;
- permisos controlados;
- upgrades major no automáticos;
- fuente jurídica única para alcance/entregables;
- capa v5.8 persistente con y sin JavaScript;
- capa v5.9 posterior a v5.8 y privacy-safe.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff, contexto comercial local/de sesión, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario o email transaccional.

## Memoria de ingeniería

Graphify + Obsidian siguen operativos. Al retomar: confirmar `main`/`stable`, leer `CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md`, `TAREA_ACTIVA.md`, comparar `BUILD_META.source_commit` con `main`, usar Graphify para acotar y confirmar luego en fuente/tests.

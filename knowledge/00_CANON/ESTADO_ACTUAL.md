# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en este cierre: `5.13.0`.
- Evidencia funcional v5.13 previa al cierre documental: run `31568876368`, SHA `e77a7e824117d3f8f3f67cc3fc71f11f3fc858c3`.

Los SHA actuales de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; refs, Pages y gates son la autoridad.

## Estado funcional

**La implementación funcional v5.13 está certificada. El commit documental que declara 5.13.0 debe volver a atravesar la certificación pública completa antes de considerar cerrada la release definitiva.**

## v5.13 — Continuidad del brief comercial

La modalidad considerada y el estándar verificable de v5.12 acompañan el recorrido desde las 16 fichas profundas hasta el formulario y el handoff manual por WhatsApp. El brief visible reduce repetición y preserva el contexto comercial sin convertirlo en propuesta o aceptación automática.

Implementación: `commercial-brief-v513.css`, `commercial-brief-v513.js`, `scripts/apply_commercial_brief_v513.py`, `scripts/validate_commercial_brief_v513.py`.

La capa no añade `localStorage`, `sessionStorage`, backend, XHR/fetch propio ni nuevos campos PII.

## Correcciones de composición certificadas

1. Las fichas de servicio usan `data-page-type="Servicio profesional"`; applicator y validator v5.13 ahora respetan ese tipo canónico y las excepciones por catálogo.
2. v5.12 valida sus cinco rutas por path + fragmento, permitiendo query params aditivos de capas posteriores sin perder identidad de ruta.

## Evidencia funcional v5.13

Run `31568876368`:

- Browser E2E: 37 entradas, 35 aprobadas, 2 omitidas, 0 fallos, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- portada: performance 1.00, a11y 0.97, LCP 1319 ms, CLS 0, TBT 89 ms, 91,193 B;
- solución IA: 1.00 / 1.00, LCP 903 ms, 23,254 B;
- producto IA: 1.00 / 1.00, LCP 994 ms, 37,334 B;
- sector tecnología: 1.00 / 1.00, LCP 997 ms, CLS 0, 24,286 B;
- perspectiva IA: 0.98 / 1.00, LCP 904 ms, CLS 0.087, 25,908 B;
- demo: 1.00 / 1.00, LCP 1033 ms, 21,932 B;
- CI hasta `stable`: 177 s;
- mejora frente a baseline v5.5 de 279 s: 36.6%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger builder→workflow_run→Pages: PASS;
- Commercial Brief v5.13 validator: PASS.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- idempotencia y composición canónica v5.8→v5.13;
- Actions fijadas a SHA y permisos controlados;
- fuente jurídica única para alcance/entregables;
- telemetría sin PII;
- WhatsApp manual;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Memoria de ingeniería

Graphify + Obsidian siguen operativos. Tras el cierre documental debe compararse `BUILD_META.source_commit` con el SHA final y documentarse cualquier delta puramente generado/versionado.

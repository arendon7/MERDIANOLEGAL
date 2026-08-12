# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión vigente: `5.14.0`.
- SHA final certificado: `9435f65ca129099a8a59f12ec5fd2f9e3aa58762`.
- Run público final: `31571937528`.
- Estado de refs al cierre: `main == stable == 9435f65ca129099a8a59f12ec5fd2f9e3aa58762`.

Refs, Pages y gates son la autoridad para el estado productivo. Las notas canónicas documentan el cierre y el siguiente ciclo.

## Estado funcional

**v5.14.0 está cerrada, desplegada y certificada.**

La recomendación explicable compara cinco modalidades sin scoring opaco y expone, cuando existe contexto suficiente, `fit`, `boundary` y `alternative`. La explicación acompaña el recorrido comercial hasta el brief y el handoff manual por WhatsApp; si falta contexto, la web no inventa una recomendación.

Implementación principal: `recommendation-v514.json`, `recommendation-v514.css`, `recommendation-v514.js`, `scripts/apply_recommendation_v514.py`, `scripts/validate_recommendation_v514.py`.

La capa no añade cuestionario, `localStorage`, `sessionStorage`, backend, XHR/fetch propio ni PII adicional.

## Evidencia final v5.14

Run `31571937528`, SHA `9435f65ca129099a8a59f12ec5fd2f9e3aa58762`:

- builder/idempotencia + validadores históricos + composición v5.8→v5.14: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe: sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- portada: performance 1.00, a11y 0.97, LCP 1232 ms, CLS 0, TBT 85 ms, 95,383 B;
- solución IA: 1.00 / 1.00, LCP 903 ms, 23,484 B;
- producto IA: 1.00 / 1.00, LCP 904 ms, 37,661 B;
- sector tecnología: 1.00 / 1.00, LCP 914 ms, CLS 0, 24,338 B;
- perspectiva IA: 0.98 / 1.00, LCP 903 ms, CLS 0.087, 25,860 B;
- demo: 1.00 / 1.00, LCP 903 ms, 22,057 B;
- CI hasta `stable`: 202 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 27.6%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger builder→workflow_run→Pages: PASS;
- validator v5.14: PASS.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- idempotencia y composición canónica v5.8→v5.14;
- Actions fijadas a SHA y permisos controlados;
- fuente jurídica única para alcance/entregables;
- telemetría sin PII;
- WhatsApp manual;
- scoring opaco desactivado;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Graphify / procedencia

El snapshot vivo de Graphify fue construido sobre el commit fuente de cierre `547b97e22eb51c9664eb5b4a0884a90963be891f` y reporta 513 nodos, 818 relaciones y 85 notas wiki con Graphify 0.9.26.

El SHA final `9435f65ca129099a8a59f12ec5fd2f9e3aa58762` está exactamente un commit generado por delante. La comparación `547b97e2… → 9435f65c…` contiene únicamente 28 outputs públicos/versionados, con cambios de una línea por archivo; no modifica fuentes jurídicas, scripts, tests ni relaciones estructurales. Se considera equivalencia estructural documentada, sin falsificar `BUILD_META.source_commit`.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Ciclo activo

**v5.15 — Eficiencia recomendación→acción.**

Objetivo: reducir fricción y solapamiento entre selector, explicación y CTA, acercando la recomendación al siguiente paso correcto sin nuevo cuestionario, scoring, storage o backend y preservando todos los contratos de calidad anteriores.

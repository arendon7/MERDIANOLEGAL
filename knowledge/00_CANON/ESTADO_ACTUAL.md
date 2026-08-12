# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión productiva: `5.15.0`.
- SHA final certificado: `2dd960fe168f2d15665e4fa695267b2746d58cba`.
- Run final: `31610848709`.
- Estado de refs al cierre: `main == stable == 2dd960fe168f2d15665e4fa695267b2746d58cba`.

## Estado funcional

**v5.15.0 está cerrada, desplegada y certificada.**

La capa consolida recomendación→acción: el encaje de cada modalidad queda junto al CTA del selector v5.12; límites y alternativas v5.14 se conservan como comparación secundaria; el formulario muestra una ruta comercial controlada por el usuario; y el handoff directo conserva modalidad, prueba verificable, explicación y siguiente paso.

Rutas canónicas: diagnóstico→`scope`; auditoría→`proposal`; producto→`proposal`; servicio especializado→`scope`; recurrente→`scope`; sin contexto→`orientation`. Un `commercial_intent` explícito tiene prioridad y la web nunca cambia automáticamente la etapa declarada.

v5.15 no añade cuestionario, scoring, `localStorage`, `sessionStorage`, backend, XHR/fetch propio ni PII adicional.

## Evidencia final v5.15

Run `31610848709`, SHA `2dd960fe168f2d15665e4fa695267b2746d58cba`:

- builder/idempotencia + validadores históricos + composición v5.8→v5.15: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe: sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- portada: performance 1.00, a11y 0.97, LCP 1250 ms, CLS 0, TBT 8 ms, 99,703 B;
- solución IA: 1.00 / 1.00, LCP 903 ms, 23,323 B;
- producto IA: 1.00 / 1.00, LCP 904 ms, 37,751 B;
- sector tecnología: 0.98 / 1.00, LCP 936 ms, CLS 0.087, 24,385 B;
- perspectiva IA: 0.98 / 1.00, LCP 900 ms, CLS 0.087, 25,934 B;
- demo: 1.00 / 1.00, LCP 900 ms, 22,035 B;
- CI hasta `stable`: 211 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 24.4%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance + trigger builder→Pages + validator v5.15: PASS.

## Compatibilidad preservada

Los gates detectaron y bloquearon tres regresiones durante v5.15 sin ser relajados: forma CTA v5.10, contrato JSON embebido v5.14 y una aserción E2E que confundía orden de query con semántica. La solución final conserva los contratos históricos y valida rutas mediante sus valores reales.

## Graphify / procedencia

El snapshot vivo final de v5.15 se construyó sobre `source_commit = cccf2e9eb6bf8c745b854de796b691cb06871222`, ya con versión declarada 5.15.0, Graphify 0.9.26, 544 nodos, 877 relaciones y 88 notas wiki.

El SHA productivo `2dd960fe…` está exactamente un commit generado por delante. La comparación contiene solo 28 outputs públicos/versionados, con una línea sustituida por archivo; no modifica catálogos fuente, scripts, tests, workflows ni relaciones estructurales. La equivalencia está documentada en `knowledge/graphify-live/graphify-out/CANONICAL_EQUIVALENCE.md` sin falsificar `source_commit`.

## Contratos vigentes

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- workers Playwright CI = 1;
- fuente jurídica única para alcance/entregables;
- telemetría sin PII;
- WhatsApp manual;
- scoring opaco desactivado;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Ciclo activo

**v5.16 — UX móvil y accesibilidad del recorrido comercial.**

Objetivo: reducir scroll/fricción en móvil y cerrar causas reales de accesibilidad/escaneabilidad. El runner Lighthouse actual solo conserva el score agregado; v5.16 debe primero exponer las auditorías de accesibilidad con score < 1 para evitar correcciones a ciegas.

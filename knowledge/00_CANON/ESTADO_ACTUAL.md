# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Versión declarada en este cierre: `5.14.0`.
- Evidencia funcional v5.14 previa al cierre documental: run `31570619885`, SHA `42e482241a818e0c94137810e1224558a58f397d`.

Los SHA actuales de `main` y `stable` deben consultarse dinámicamente. Las notas documentan hitos; refs, Pages y gates son la autoridad.

## Estado funcional

**La implementación funcional v5.14 está certificada. El commit documental que declara 5.14.0 debe volver a atravesar la certificación pública completa antes de considerar cerrada la release definitiva.**

## v5.14 — Recomendación explicable de modalidad

Cinco reglas determinísticas comparan diagnóstico, auditoría, producto cerrado, servicio especializado y acompañamiento recurrente. Cada regla expone `fit`, `boundary` y `alternative`; `scoring` permanece desactivado.

La explicación aparece en portada y, cuando existe una modalidad contextual, acompaña el brief y el handoff manual por WhatsApp. Si falta contexto, la web no inventa una recomendación.

Implementación: `recommendation-v514.json`, `recommendation-v514.css`, `recommendation-v514.js`, `scripts/apply_recommendation_v514.py`, `scripts/validate_recommendation_v514.py`.

La capa no añade cuestionario, `localStorage`, `sessionStorage`, backend, XHR/fetch ni PII adicional.

## Evidencia funcional v5.14

Run `31570619885`:

- Browser E2E + axe: PASS sobre 37 entradas protegidas y 7 superficies axe;
- Lighthouse: 6/6 dentro de presupuesto;
- portada: performance 0.99, a11y 0.97, LCP 1307 ms, CLS 0, TBT 106 ms, 95,461 B;
- solución IA: 1.00 / 1.00, LCP 904 ms, 23,279 B;
- producto IA: 1.00 / 1.00, LCP 907 ms, 37,657 B;
- sector tecnología: 0.98 / 1.00, LCP 988 ms, CLS 0.087, 24,564 B;
- perspectiva IA: 1.00 / 1.00, LCP 906 ms, CLS 0, 25,918 B;
- demo: 1.00 / 1.00, LCP 903 ms, 22,048 B;
- CI hasta `stable`: 264 s;
- mejora frente a baseline v5.5 de 279 s: 5.4%;
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

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Memoria de ingeniería

Graphify + Obsidian siguen operativos. Tras el cierre documental debe compararse `BUILD_META.source_commit` con el SHA final y documentarse cualquier delta puramente generado/versionado.

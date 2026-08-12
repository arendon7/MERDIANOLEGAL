# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Release declarada en este cierre: `5.15.0`.
- SHA funcional certificado antes del cierre documental: `48a0692e8e4f999a85cfd8619fe2e293528945c2`.
- Run público funcional: `31609518536`.
- Estado de refs antes del cierre documental: `main == stable == 48a0692e8e4f999a85cfd8619fe2e293528945c2`.

Refs, Pages y gates son la autoridad para el estado productivo. El SHA definitivo de 5.15.0 será el que contenga este cierre y vuelva a superar la certificación completa.

## Estado funcional

**v5.15 está funcionalmente certificada y en cierre formal.**

La capa consolida la arquitectura de decisión ya existente en lugar de apilar otra superficie: el encaje de cada modalidad queda junto al CTA del selector v5.12; límites y alternativas v5.14 se conservan en comparación secundaria; el formulario muestra una ruta comercial controlada por el usuario y el handoff directo conserva el siguiente paso sugerido.

Implementación principal: `decision-action-v515.css`, `decision-action-v515.js`, `scripts/apply_decision_action_v515.py`, `scripts/validate_decision_action_v515.py`.

Rutas canónicas: diagnóstico→`scope`; auditoría→`proposal`; producto→`proposal`; servicio especializado→`scope`; recurrente→`scope`; sin contexto→`orientation`. Un `commercial_intent` explícito siempre tiene prioridad y la web no cambia automáticamente la etapa declarada.

La capa no añade cuestionario, scoring, `localStorage`, `sessionStorage`, backend, XHR/fetch propio ni PII adicional.

## Evidencia funcional v5.15

Run `31609518536`, SHA `48a0692e8e4f999a85cfd8619fe2e293528945c2`:

- builder/idempotencia + validadores históricos + composición v5.8→v5.15: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe: sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- portada: performance 1.00, a11y 0.97, LCP 1322 ms, CLS 0, TBT 3 ms, 99,735 B;
- solución IA: 1.00 / 1.00, LCP 989 ms, 23,234 B;
- producto IA: 1.00 / 1.00, LCP 999 ms, 37,677 B;
- sector tecnología: 0.98 / 1.00, LCP 1006 ms, CLS 0.087, 24,289 B;
- perspectiva IA: 1.00 / 1.00, LCP 1044 ms, 25,796 B;
- demo: 1.00 / 1.00, LCP 906 ms, 21,994 B;
- CI hasta `stable`: 209 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 25.1%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger builder→workflow_run→Pages: PASS;
- validator v5.15: PASS.

## Gates que v5.15 preservó

Durante la certificación, tres incompatibilidades fueron detectadas y corregidas sin relajar contratos:

1. el CTA profundo debe conservar la forma canónica v5.10; v5.15 eliminó un atributo redundante y usa `commercial_intent`;
2. el contrato JSON embebido v5.14 debe sobrevivir a la consolidación; v5.15 lo conserva y exige igualdad estructural con `recommendation-v514.json`;
3. E2E debe validar semántica de query, no orden textual; ahora exige los valores exactos mediante `URLSearchParams` y `#contacto`.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- idempotencia y composición canónica v5.8→v5.15;
- Actions fijadas a SHA y permisos controlados;
- fuente jurídica única para alcance/entregables;
- telemetría sin PII;
- WhatsApp manual;
- scoring opaco desactivado;
- sin CRM/backend ni almacenamiento servidor del formulario;
- sin firma, pagos, agenda o portal documental ficticios.

## Graphify / procedencia

Para el cierre funcional, el snapshot vivo de Graphify apunta exactamente a `source_commit = 48a0692e8e4f999a85cfd8619fe2e293528945c2`, con Graphify 0.9.26, 544 nodos, 877 relaciones y 88 notas wiki.

El campo declarativo `version` del snapshot sigue en 5.14.0 porque el cierre formal 5.15.0 aún no había actualizado `version.json` cuando se construyó ese snapshot. Después del merge documental y del posible commit generado de sincronización visible, la procedencia se verificará de nuevo sin falsificar `source_commit`.

## Integraciones externas

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin evidencia real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Próximo ciclo

**v5.16 — UX móvil y accesibilidad del recorrido comercial.**

Objetivo: reducir scroll/fricción en móvil y revisar la brecha restante de Lighthouse Accessibility de la portada sin recortar profundidad jurídica, controles de decisión ni cobertura QA.

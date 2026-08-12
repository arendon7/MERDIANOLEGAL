# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release cerrada

**v5.15.0 — Eficiencia recomendación→acción** está definitivamente cerrada.

- SHA final: `2dd960fe168f2d15665e4fa695267b2746d58cba`;
- run final: `31610848709`;
- `main == stable`;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse: 6/6 PASS;
- CI: 211 s, 24.4% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- Graphify fuente `cccf2e9e…`, versión 5.15.0, 544 nodos / 877 relaciones / 88 notas, equivalente estructuralmente al SHA final mediante un único commit generado de 28 outputs públicos/versionados.

## Ciclo activo

**v5.16 — UX móvil y accesibilidad del recorrido comercial.**

### Objetivo

Reducir fricción y scroll en pantallas pequeñas y resolver causas reales de accesibilidad/escaneabilidad sin ocultar profundidad jurídica ni alterar el modelo de decisión controlado por el usuario.

### Fase 1 — observabilidad de accesibilidad

El runner Lighthouse v5.5/v5.6 conserva actualmente `accessibilityScore` pero descarta qué auditorías concretas tienen score < 1 cuando el presupuesto global sigue verde. La portada final v5.15 obtiene 0.97 mientras axe serio/crítico está limpio.

v5.16 debe:

1. registrar en `summary.json` las auditorías Lighthouse de accesibilidad con score < 1;
2. conservar id, título, score, descripción breve y un conjunto acotado de nodos/detalles diagnósticos no sensibles;
3. mostrar un resumen compacto en `summary.md`/Step Summary;
4. no cambiar budgets ni convertir fluctuaciones de accesibilidad en retries;
5. usar esa evidencia para corregir únicamente causas verificadas.

### Fase 2 — UX móvil

1. medir y reducir repetición visible/scroll entre selector, recomendación, brief y estados comerciales;
2. revisar foco visible, orden de teclado, `details`, navegación por anclas y devolución de foco;
3. revisar targets táctiles, espaciado, densidad y legibilidad;
4. preservar acceso a límites, exclusiones, prueba verificable y condiciones de inicio;
5. mantener rutas proposal/scope/orientation y ausencia de cambios automáticos;
6. ampliar assertions dentro de las 37 entradas protegidas antes de crear nuevos tests.

### No objetivos

- no nuevo cuestionario;
- no scoring/ranking opaco;
- no `localStorage`/`sessionStorage` para decisión comercial;
- no backend/CRM;
- no fetch/XHR propio;
- no PII adicional;
- no testimonios/clientes/resultados fabricados;
- no firma, pagos, agenda, expediente o carga documental ficticios;
- no esconder contenido jurídico para mejorar métricas;
- no relajar Lighthouse/axe/budgets.

## Contratos que v5.16 debe preservar

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E salvo necesidad independiente demostrada;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- fuente jurídica única;
- WhatsApp manual;
- telemetría sin PII;
- builder idempotente;
- `stable` solo después de todos los gates verdes.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-11.

## Ciclo en cierre

**v5.8 — Arquitectura de decisión y claridad de compra.**

La implementación funcional está certificada. Este cierre declara `5.8.0` y solo constituye la release definitiva cuando atraviesa nuevamente la certificación pública completa y termina con `main == stable`.

## Implementado

1. selector de cuatro formas de contratación en portada;
2. capa ejecutiva en las 16 fichas con `ENCAJA SI`, `QUÉ COMPRA`, `QUÉ RECIBE`, `QUÉ APORTA` y `QUÉ NO ASUMIR`;
3. generación determinista desde `situations`, `perimeter`, `deliverables`, `requirements`, `limits`, duración, modalidad y audiencia de las fuentes jurídicas existentes;
4. CTA contextual para solicitar propuesta con el alcance identificado;
5. `decision-v58.css` como capa visual específica;
6. `scripts/apply_decision_v58.py` como generador canónico;
7. `scripts/validate_decision_v58.py` como contrato fuente→resumen y runtime-safe;
8. integración v5.8 dentro del gate de catálogo estático;
9. integración de la generación v5.8 al final de la cadena canónica para preservar idempotencia;
10. cobertura Browser añadida dentro de la entrada existente, sin incrementar ni reducir las 37 entradas protegidas;
11. parser histórico v4.5 robustecido frente a indentación variable;
12. bloque v5.8 movido fuera de `#detail-page` para sobrevivir al render de `catalog-page.js`;
13. validator reforzado para impedir futuras regresiones de ubicación runtime;
14. `RELEASE-v5.8.md`, README y memoria canónica alineados con la release.

## Evidencia funcional previa al cierre documental

Run `31541197197`, SHA `681c252f09a50447af0557a2039b34b8a79faed9`:

- construcción e idempotencia: success;
- validadores históricos v4.4→v5.7 + contrato v5.8: success;
- Pages + smoke: success;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- CI: 232 s hasta gate de `stable`, 16.8% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- `stable` promovido correctamente.

## Regresiones detectadas durante el ciclo

Los controles bloquearon dos problemas antes de certificación:

1. una dependencia histórica de indentación exacta rompía la segunda pasada idempotente;
2. el runtime de productos eliminaba la primera ubicación del bloque v5.8 al reemplazar `#detail-page`.

Ambos se corrigieron en generadores/contratos. No se modificó la suite para ocultarlos y `stable` no avanzó con gates rojos.

## Contratos preservados

- 37 entradas E2E;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- gate dual Browser + Lighthouse;
- idempotencia;
- Actions inventariadas y fijadas a SHA;
- permisos controlados;
- no upgrades major automáticos;
- full public certification antes de `stable`;
- fuente jurídica única para alcance y entregables;
- persistencia v5.8 con y sin JavaScript.

## Condición de cierre

La v5.8 queda cerrada cuando el commit que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores históricos + contrato v5.8 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health verde;
7. `main == stable`;
8. `version.json` y etiqueta pública declaran 5.8.0;
9. Graphify queda alineado con el estado final o se documenta de forma verificable cualquier diferencia puramente generada.

## Próximo ciclo después del cierre

Priorizar mejora comercial medible sobre nueva infraestructura: hacer más fuerte el paso desde claridad de alcance hacia **calificación del lead, propuesta y cierre**, preservando privacidad y sin declarar CRM, analítica externa o automatizaciones que todavía no estén realmente configuradas.
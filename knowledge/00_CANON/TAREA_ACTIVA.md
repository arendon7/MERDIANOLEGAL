# Meridiano Legal — Tarea activa

Actualizado: 2026-08-11.

## Ciclo en cierre

**v5.9 — Calificación comercial y preparación de propuesta.**

La implementación funcional está certificada. Este cierre declara `5.9.0` y solo constituye la release definitiva cuando el commit documental vuelve a atravesar la certificación pública completa y termina con `main == stable`.

## Implementado

1. calificación comercial dentro del formulario público;
2. momento de decisión y horizonte como campos requeridos;
3. rango de inversión jurídica como dato opcional;
4. resumen visible que combina contexto, necesidad, momento, horizonte e inversión;
5. siguiente paso sugerido sin scoring de valor: orientación, llamada de alcance o propuesta estructurada;
6. handoff a WhatsApp con el brief comercial preparado, sin envío automático;
7. privacidad por diseño y prohibición de PII/texto libre en telemetría;
8. `commercial-intake-v59.css` y `commercial-intake-v59.js`;
9. `scripts/apply_commercial_intake_v59.py` y `scripts/validate_commercial_intake_v59.py`;
10. cobertura v5.9 incorporada dentro de las 37 entradas Browser protegidas;
11. generador v4.9 robustecido para permitir atributos posteriores del formulario;
12. Governance ampliado para vigilar el generador v4.9 y probar `v4.9 → v5.9`;
13. builder corregido para terminar siempre en `v5.8 → v5.9`;
14. `RELEASE-v5.9.md`, README, versionado y memoria canónica alineados.

## Evidencia funcional previa al cierre documental

Run `31547313170`, SHA `a64d2d957e3ca6c96fec855be85019680ebe6a03`:

- idempotencia y validadores: success;
- Pages + smoke: success;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 196 s hasta `stable`, 29.7% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- antes de este cierre: `main == stable == a64d2d957e3ca6c96fec855be85019680ebe6a03`.

## Regresiones detectadas durante el ciclo

1. v4.9 rechazaba el nuevo atributo v5.9 en el formulario por una coincidencia demasiado estricta;
2. el builder volvía a ejecutar v5.8 después de v5.9 y alteraba el orden final de CSS.

Ambos problemas fueron bloqueados antes de `stable`, corregidos en la composición canónica y convertidos en contratos verificables. No se debilitó la suite.

## Contratos preservados

- 37 entradas E2E;
- Chromium desktop/mobile y WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- gate dual Browser + Lighthouse;
- idempotencia;
- SHA pinning y permisos de Actions;
- no upgrades major automáticos;
- fuente jurídica única para alcance y entregables;
- v5.8 persiste tras render runtime;
- v5.9 queda después de v5.8;
- telemetría sin PII;
- sin CRM/backend ni almacenamiento servidor inventados.

## Condición de cierre

v5.9 queda cerrada cuando el commit que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores históricos + v5.8 + v5.9 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health verde;
7. `main == stable`;
8. `version.json` y etiqueta pública declaran 5.9.0;
9. Graphify queda alineado con el estado final o cualquier desfase puramente generado queda documentado y verificable.

## Próximo ciclo después del cierre

Priorizar **conversión comercial medible y preparación del cierre** sin inventar infraestructura: mejorar CTA/propuesta, señales de confianza, rutas de contacto y observabilidad first-party compatible con privacidad. Un CRM o almacenamiento de leads debe entrar solo cuando exista una integración real y gobernada.

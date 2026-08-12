# Meridiano Legal — Tarea activa

Actualizado: 2026-08-11.

## Ciclo en cierre

**v5.10 — Conversión, propuesta y cierre.**

La implementación funcional está certificada. Este cierre declara `5.10.0` y solo constituye la release definitiva cuando el commit documental vuelve a atravesar la certificación pública completa y termina con `main == stable`.

## Implementado

1. intención comercial contextual desde las 16 fichas profundas;
2. productos orientados a solicitud de propuesta y servicios a definición de alcance;
3. preselección trasladada al formulario sin impedir que el usuario la cambie;
4. ruta visible `calificación → alcance/propuesta → aceptación → inicio`;
5. anatomía de propuesta: objetivo, perímetro, entregables, cronograma y supuestos/exclusiones;
6. límites claros: preparar WhatsApp no equivale a contratación, aceptación ni reserva;
7. handoff a WhatsApp sin envío automático;
8. telemetría sin PII ni texto libre del caso;
9. `conversion-close-v510.css`;
10. `scripts/apply_conversion_v510.py` y `scripts/validate_conversion_v510.py`;
11. cobertura v5.10 dentro de las 37 entradas Browser protegidas;
12. v5.9 robustecido para preservar atributos de capas posteriores;
13. contraste WCAG de `.close-legal-v510` corregido sin relajar axe;
14. builder nuevamente idempotente con `Canonical public files are current.`;
15. `RELEASE-v5.10.md`, README, versionado y memoria canónica alineados en este cierre.

## Evidencia funcional previa al cierre documental

Run `31558953560`, SHA `f8b47f2ec2885cc39ff64a2448792f352619f9c3`:

- idempotencia y validadores: success;
- Pages + smoke: success;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 173 s hasta `stable`, 38.0% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- antes de este cierre: `main == stable == f8b47f2ec2885cc39ff64a2448792f352619f9c3`.

## Regresiones detectadas durante el ciclo

1. v5.9 rechazaba el atributo de extensión de v5.10 durante la segunda pasada canónica;
2. axe detectó contraste insuficiente en el aviso legal de la nueva ruta de cierre.

Ambos problemas fueron bloqueados antes de `stable`, corregidos y convertidos en evidencia verificable. No se debilitó la suite.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
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
- v5.8 → v5.9 → v5.10;
- telemetría sin PII;
- sin CRM/backend ni almacenamiento servidor inventados.

## Condición de cierre

v5.10 queda cerrada cuando el commit que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores históricos + v5.8 + v5.9 + v5.10 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health verde;
7. `main == stable`;
8. `version.json` y etiqueta pública declaran 5.10.0;
9. Graphify queda alineado con el estado final o cualquier desfase puramente generado queda documentado y verificable.

## Próximo ciclo después del cierre

**v5.11 — Contratación e inicio del encargo + higiene de CI.**

Prioridades:

- aclarar qué ocurre después de aceptar una propuesta: verificaciones de conflicto/capacidad, términos del encargo, información inicial y kickoff, sin inventar firma, pagos, agenda o portal documental;
- distinguir visualmente `propuesta preparada`, `propuesta aceptada` y `encargo iniciado`;
- mantener la privacidad del formulario y el handoff real por WhatsApp;
- revisar el disparador de `Site Quality` para evitar carreras sobre commits fuente previos al builder, sin debilitar gates ni `stable`.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-11.

## Ciclo en cierre

**v5.11 — Contratación, inicio del encargo e higiene de CI.**

La implementación funcional está certificada. Este cierre declara `5.11.0` y solo constituye la release definitiva cuando el commit documental vuelve a atravesar la certificación pública completa y termina con `main == stable`.

## Implementado

1. Pages serializado detrás del builder canónico, sin trigger directo por `push`;
2. `scripts/validate_pages_trigger_v511.py` como guardrail permanente de topología;
3. contrato v5.6 actualizado para exigir la secuencia builder → Pages sin perder cobertura ni budgets;
4. cuatro estados jurídicos/comerciales: solicitud preparada, propuesta emitida, propuesta aceptada y encargo iniciado;
5. verificaciones previas al inicio: partes/conflictos cuando corresponda, alcance/exclusiones, condiciones económicas, inicio/prioridades, interlocutores y canal confidencial;
6. límites explícitos de la web pública: sin aceptación automática, pagos, reserva de agenda, expediente, carga documental ni inicio automático;
7. `engagement-v511.css`;
8. `scripts/apply_engagement_v511.py` y `scripts/validate_engagement_v511.py`;
9. cobertura v5.11 integrada dentro de las 37 entradas Playwright existentes;
10. `RELEASE-v5.11.md`, README, versionado y memoria canónica alineados en este cierre.

## Evidencia funcional previa al cierre documental

Run `31560805174`, SHA `cf4341eb9ec051a3e583b4675263b228ee5f0839`:

- idempotencia y validadores: success;
- Pages + smoke: success;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 193 s hasta `stable`, 30.8% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- `PAGES TRIGGER V5.11 OK`;
- antes de este cierre: `main == stable == cf4341eb9ec051a3e583b4675263b228ee5f0839`.

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
- v5.8 → v5.9 → v5.10 → v5.11;
- telemetría sin PII;
- sin CRM/backend ni almacenamiento servidor inventados;
- sin firma, pagos, agenda o carga documental ficticios.

## Condición de cierre

v5.11 queda cerrada cuando el commit que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores históricos + v5.8 + v5.9 + v5.10 + v5.11 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health y trigger guard verdes;
7. `main == stable`;
8. `version.json` y etiqueta pública declaran 5.11.0;
9. Graphify queda alineado con el estado final o cualquier desfase puramente generado queda documentado y verificable.

## Próximo ciclo después del cierre

**v5.12 — Prueba comercial verificable y apoyo a la decisión.**

Prioridades:

- reforzar cómo se demuestra método, seniority y calidad del trabajo sin inventar clientes, testimonios o resultados;
- ayudar a elegir entre diagnóstico, auditoría, producto cerrado, servicio especializado y dirección jurídica continua;
- hacer visibles criterios de evidencia y entregables que el cliente puede verificar antes y después de contratar;
- mantener la web estática, jurídicamente rigurosa y orientada a conversión;
- evitar nuevas capas de infraestructura salvo que exista una necesidad funcional concreta.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Ciclo en cierre

**v5.12 — Prueba comercial verificable y apoyo a la decisión.**

La implementación funcional está certificada. Este cierre declara `5.12.0` y solo constituye la release definitiva cuando el commit documental vuelve a atravesar la certificación pública completa y termina con `main == stable`.

## Implementado

1. selector de 5 modalidades en portada: diagnóstico, auditoría, producto cerrado, servicio especializado y acompañamiento recurrente;
2. prueba verificable en las 16 fichas profundas;
3. paridad de cada prueba con `method`, `deliverables`, `formats` y `acceptance` de la fuente canónica;
4. `proof-v512.css`;
5. `scripts/apply_proof_v512.py` y `scripts/validate_proof_v512.py`;
6. integración en builder, Pages y Release Governance;
7. cobertura v5.12 dentro de las 37 entradas Playwright existentes;
8. corrección del único fallo axe de contraste sin relajar el gate, más guardrail permanente;
9. conservación de la topología builder → Pages de v5.11.

## Evidencia funcional previa al cierre documental

Run `31562692907`, SHA `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`:

- antes del cierre: `main == stable`;
- idempotencia y validadores: success;
- Pages + smoke: success;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 187 s hasta `stable`, 33.0% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger: PASS.

## Condición de cierre

v5.12 queda cerrada cuando el SHA final que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores históricos + v5.8 a v5.12 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health y trigger guard verdes;
7. `main == stable`;
8. `version.json` y etiqueta pública declaran 5.12.0;
9. Graphify queda alineado con el estado final o cualquier desfase puramente generado queda documentado y verificable.

## Próximo ciclo después del cierre

**v5.13 — Continuidad entre prueba verificable y brief comercial.**

Prioridades propuestas:

- conservar la modalidad elegida durante el recorrido hacia contacto;
- hacer que el brief preparado para WhatsApp refleje modalidad, alcance esperado y expectativas verificables de entrega;
- reducir incertidumbre entre ficha profunda, propuesta y conversación comercial;
- mejorar interlinking entre modalidad, prueba y CTA sin introducir páginas innecesarias;
- mantener privacidad, no persistencia servidor y ausencia de claims no demostrables;
- preservar las 37 pruebas y budgets salvo necesidad independiente real.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Ciclo en cierre

**v5.14 — Recomendación explicable de modalidad.**

La implementación funcional está certificada. Este cierre declara `5.14.0` y solo constituye la release definitiva cuando el commit documental vuelve a atravesar la certificación pública completa y termina con `main == stable`.

## Implementado

1. contrato `recommendation-v514.json` con cinco modalidades y `scoring:false`;
2. comparación visible: por qué encaja / límite / alternativa;
3. brief del formulario reutiliza la explicación cuando existe modalidad contextual;
4. WhatsApp preparado y WhatsApp directo de las 16 fichas conservan la explicación;
5. si falta contexto, no se inventa recomendación;
6. sin nuevo cuestionario, storage, backend, PII adicional ni transporte propio de red;
7. cobertura v5.14 dentro de las 37 entradas Playwright;
8. integración como última capa canónica v5.14 en builder, Pages y Release Governance.

## Evidencia funcional previa al cierre documental

Run `31570619885`, SHA `42e482241a818e0c94137810e1224558a58f397d`:

- `main == stable`;
- idempotencia + validadores históricos + v5.8→v5.14: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: PASS sobre 37 entradas protegidas y 7 superficies;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 264 s hasta `stable`, 5.4% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance + Pages trigger + validator v5.14: PASS.

## Condición de cierre

v5.14 queda cerrada cuando el SHA final que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores históricos + v5.8 a v5.14 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health y trigger guard verdes;
7. `main == stable`;
8. `version.json` y etiqueta pública declaran 5.14.0;
9. Graphify queda alineado con el estado final o cualquier desfase puramente generado queda documentado y verificable.

## Próximo ciclo después del cierre

**v5.15 — Eficiencia recomendación→acción.**

Prioridades iniciales:

- reducir solapamiento entre selector v5.12 y explicación v5.14 sin perder contenido útil;
- acercar la recomendación al CTA correcto;
- mejorar jerarquía y escaneabilidad del recorrido de decisión;
- conservar contexto sin nuevo cuestionario ni scoring;
- preservar privacidad, static-first, 46 páginas, 37 pruebas y budgets salvo necesidad independiente real.

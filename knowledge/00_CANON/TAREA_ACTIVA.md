# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release cerrada

**v5.14.0 — Recomendación explicable de modalidad.**

Cierre definitivo:

- SHA: `9435f65ca129099a8a59f12ec5fd2f9e3aa58762`;
- run: `31571937528`;
- `main == stable`;
- builder/idempotencia y validadores v5.8→v5.14: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- Lighthouse: 6/6 PASS;
- CI: 202 s, 27.6% mejor que baseline v5.5;
- cobertura reducida: no;
- budgets relajados: no.

Graphify quedó estructuralmente equivalente: snapshot fuente `547b97e2…` y SHA final `9435f65c…` separado por un único commit generado que modifica solo 28 outputs públicos/versionados.

## Ciclo activo

**v5.15 — Eficiencia recomendación→acción.**

### Objetivo

Hacer que la persona llegue con menos fricción desde “qué modalidad me conviene y por qué” hasta el CTA correcto, sin duplicar contenido ni degradar la profundidad jurídica/comercial ya construida.

### Prioridades

1. reducir solapamiento visual y semántico entre selector v5.12 y explicación v5.14;
2. acercar cada recomendación al CTA correcto: explorar alcance, solicitar propuesta o iniciar orientación según modalidad/contexto;
3. mejorar jerarquía, escaneabilidad y continuidad del recorrido en desktop y móvil;
4. preservar `modality`, `proof_standard`, contexto comercial y recomendación explicable hasta formulario/WhatsApp;
5. mantener fallback explícito cuando no existe contexto suficiente, sin inventar recomendaciones;
6. reutilizar los 37 tests protegidos y ampliar assertions antes de aumentar conteo;
7. integrar v5.15 como última capa canónica después de v5.14 en builder, Pages y Release Governance.

### No objetivos

- no nuevo cuestionario;
- no scoring ni ranking opaco;
- no `localStorage`/`sessionStorage` para decisión comercial;
- no backend/CRM;
- no transporte XHR/fetch propio;
- no PII adicional en telemetría;
- no testimonios, clientes o resultados fabricados;
- no firma, pagos, agenda, expediente o carga documental ficticios.

## Contratos que no deben degradarse

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E salvo necesidad independiente demostrada;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- fuente jurídica única para alcance/entregables;
- WhatsApp manual;
- telemetría sin PII;
- builder idempotente;
- `stable` solo después de Pages + Browser/axe + Lighthouse + release-health verdes.

## Condición de cierre de v5.15

El ciclo solo se considera cerrado cuando el SHA final generado cumple simultáneamente:

1. applicator/validator v5.15 verdes e idempotentes;
2. validadores históricos + composición v5.8→v5.15 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. Release Governance + trigger guard verdes;
7. `main == stable`;
8. versión pública y documentación alineadas;
9. procedencia Graphify verificable sin falsificar `source_commit`.

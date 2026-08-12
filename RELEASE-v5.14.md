# Meridiano Legal v5.14.0 — Recomendación explicable de modalidad

Fecha: 2026-08-12

## Objetivo

v5.14 reduce fricción al comparar diagnóstico, auditoría, producto cerrado, servicio especializado y acompañamiento recurrente. La recomendación es determinística y explicable: cada modalidad expone por qué puede encajar, su límite y qué alternativa considerar si cambia el alcance. No usa puntajes opacos.

## Implementado

- contrato único `recommendation-v514.json` con `scoring: false` y cinco modalidades;
- comparación visible en portada con **por qué encaja / límite / alternativa**;
- `recommendation-v514.css` y `recommendation-v514.js`;
- `scripts/apply_recommendation_v514.py` y `scripts/validate_recommendation_v514.py`;
- explicación reutilizada en el brief del formulario;
- continuidad hasta WhatsApp preparado y WhatsApp directo de las 16 fichas;
- sin nuevo cuestionario, backend, `localStorage`, `sessionStorage`, `fetch`, XHR ni PII adicional;
- E2E ampliado dentro de las 37 entradas protegidas existentes;
- composición canónica `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14`.

## Evidencia funcional certificada

Run: `31570619885`

SHA certificado: `42e482241a818e0c94137810e1224558a58f397d`

Antes de este cierre documental:

- `main == stable == 42e482241a818e0c94137810e1224558a58f397d`;
- builder, idempotencia y validadores históricos + v5.14: PASS;
- Pages + smoke público: PASS;
- Browser E2E + axe: PASS sobre las 37 entradas protegidas y 7 superficies axe;
- Lighthouse: 6/6 dentro de presupuesto;
- CI hasta `stable`: 264 s;
- baseline v5.5: 279 s;
- mejora: 5.4%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger builder→workflow_run→Pages: PASS;
- validator v5.14: PASS.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 0.99 | 0.97 | 1307 ms | 0 | 106 ms | 95,461 B |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,279 B |
| Producto IA | 1.00 | 1.00 | 907 ms | 0 | 0 ms | 37,657 B |
| Sector tecnología | 0.98 | 1.00 | 988 ms | 0.087 | 0 ms | 24,564 B |
| Perspectiva IA | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 25,918 B |
| Demo | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 22,048 B |

### Evidencia archivada

- Lighthouse `9131218027`, SHA256 `c89f296fb29ccd4de2b6f828b27057d519c58ea21f67d869033778c89c272ef2`;
- CI `9131263082`, SHA256 `b118f94b9f2285e68f7b3910c93398ecb9208870c5c3dbf79efc50ce4e33ebba`;
- Release Governance `9131263656`, SHA256 `7fff1043b3a1f1c9972ce8525a4beb221c2b095b3d534e62634e705b6289e5b9`.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas Playwright;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- WhatsApp sigue siendo handoff manual;
- sin CRM/backend, almacenamiento servidor, email transaccional, firma, pagos, agenda ni carga documental ficticios.

## Condición de cierre definitivo

Este documento declara `5.14.0`. La release queda definitivamente cerrada solo cuando el SHA que contiene este cierre atraviesa nuevamente builder, idempotencia, Pages, Browser/axe, Lighthouse, release-health, sincronización pública de versión y termina con `main == stable`.

## Próximo ciclo

v5.15 debe concentrarse en **eficiencia recomendación→acción**: reducir solapamiento entre los bloques de decisión existentes, hacer más directa la transición desde una recomendación explicada hacia el CTA correcto y conservar static-first, privacidad y ausencia de scoring opaco.

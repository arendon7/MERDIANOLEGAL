# Meridiano Legal v5.13.0 — Continuidad entre modalidad, prueba y brief comercial

Fecha: 2026-08-12

## Objetivo

v5.13 evita que el contexto comercial construido en v5.12 se pierda al pasar desde una ficha profunda al formulario o a WhatsApp. La modalidad considerada y el estándar verificable acompañan el recorrido hasta el handoff comercial, sin backend, persistencia adicional ni nuevos datos personales.

## Implementado

- `commercial-brief-v513.css` y `commercial-brief-v513.js`;
- brief visible en el formulario con modalidad considerada y estándar verificable;
- parámetros estructurados `modality` y `proof_standard` desde las fichas;
- continuidad en las 16 fichas profundas;
- mensaje preparado de WhatsApp incluye modalidad + estándar verificable;
- WhatsApp directo de ficha incorpora el mismo contexto y un disclaimer de alcance;
- no se añadió `localStorage`, `sessionStorage`, `fetch`, XHR, backend ni telemetría con PII;
- E2E v5.13 integrado dentro de las 37 entradas existentes;
- composición canónica `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13`.

## Correcciones de composición antes de `stable`

1. Las fichas de servicios usan el tipo canónico `Servicio profesional`; el applicator inicial asumía `Servicio jurídico`. Se corrigió applicator + validator para aceptar únicamente los tipos canónicos y las tres excepciones de modalidad por catálogo.
2. El validator histórico v5.12 exigía `href` literales sin query. v5.13 añade parámetros de continuidad sin alterar la ruta. Se corrigió v5.12 para validar `path + fragment` canónicos permitiendo query params aditivos posteriores, sin reducir ninguna de sus cinco rutas obligatorias.

Ninguna de estas correcciones relajó gates, cobertura o budgets.

## Evidencia funcional certificada

Run: `31568876368`

SHA certificado: `e77a7e824117d3f8f3f67cc3fc71f11f3fc858c3`

Antes de este cierre documental:

- `main == stable == e77a7e824117d3f8f3f67cc3fc71f11f3fc858c3`;
- builder/idempotencia y todos los validadores: PASS;
- Pages + smoke público: PASS;
- Browser E2E: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI hasta `stable`: 177 s;
- baseline v5.5: 279 s;
- mejora: 36.6%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger builder→workflow_run→Pages: PASS;
- validator comercial v5.13: PASS.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1319 ms | 0 | 89 ms | 91,193 B |
| Solución IA | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 23,254 B |
| Producto IA | 1.00 | 1.00 | 994 ms | 0 | 0 ms | 37,334 B |
| Sector tecnología | 1.00 | 1.00 | 997 ms | 0 | 0 ms | 24,286 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,908 B |
| Demo | 1.00 | 1.00 | 1033 ms | 0 | 0 ms | 21,932 B |

## Evidencia archivada

- Lighthouse artifact `9130570828`, SHA256 `07a528cc96c07d25feb9a67f10a6bd33aefc338d4bc1a86735d17728a6048f42`;
- CI artifact `9130577730`, SHA256 `1856a6145d4f67680a1947de5e43fd4e91366aa8a395b53dcad201f5f8cee6e7`;
- release-health artifact `9130578054`, SHA256 `0fa6ff640d63ae733d6d2953f50a84eded355407a88b5074bcf7a88c0b196013`.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas Playwright;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- WhatsApp sigue siendo handoff manual;
- no CRM/backend, storage servidor, email transaccional, firma, pagos, agenda ni carga documental ficticios.

## Condición de cierre definitivo

Este documento declara `5.13.0`. La release queda definitivamente cerrada solo cuando el SHA que contiene este cierre atraviesa nuevamente builder, idempotencia, Pages, Browser/axe, Lighthouse, release-health, sincronización pública de versión y termina con `main == stable`.

## Próximo ciclo

v5.14 debe enfocarse en **reducción de fricción y precisión de recomendación comercial** sobre la arquitectura ya estable: mejorar cuándo conviene diagnóstico, auditoría, producto, servicio o acompañamiento recurrente y cómo se compara esa recomendación antes del contacto, sin crear integraciones inexistentes.

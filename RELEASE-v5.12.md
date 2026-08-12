# Meridiano Legal v5.12.0 — Prueba verificable y elección de modalidad

Fecha: 2026-08-12

## Objetivo

v5.12 mejora la confianza de decisión sin recurrir a clientes, testimonios, casos de éxito, métricas ni resultados no demostrables. La prueba comercial se deriva de la propia fuente jurídica del catálogo y la portada ayuda a distinguir la modalidad adecuada según el tipo de necesidad.

## Implementado

- matriz de 5 modalidades en portada: diagnóstico, auditoría, producto cerrado, servicio especializado y acompañamiento recurrente;
- bloque de prueba verificable en las 16 fichas profundas;
- cada bloque se deriva de `method`, `deliverables`, `formats` y `acceptance` de la fuente canónica;
- `proof-v512.css`;
- `scripts/apply_proof_v512.py` y `scripts/validate_proof_v512.py`;
- composición canónica v5.8 → v5.9 → v5.10 → v5.11 → v5.12;
- cobertura incorporada dentro de las 37 entradas Playwright existentes.

## Corrección de accesibilidad previa al cierre

El primer candidato funcional `0ed8fe96f244497693c5a45771489489a904fc9d` fue bloqueado correctamente por axe por contraste insuficiente en el título del panel oscuro de prueba de la portada. No se relajó el gate.

PR #45 fijó explícitamente el título en blanco y añadió un guardrail al validador v5.12. El candidato corregido es `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`.

## Evidencia funcional certificada

Run: `31562692907`

SHA certificado: `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`

Antes de este cierre documental:

- `main == stable == f8c4d1abc38929040f1ce67b04a2c2c4193c3690`;
- builder e idempotencia: success;
- validadores históricos + v5.8 a v5.12: success;
- Pages + smoke público: success;
- Browser E2E: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- tiempo hasta `stable`: 187 s;
- baseline v5.5: 279 s;
- mejora: 33.0%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger v5.11: PASS, builder antes de Pages y sin carrera directa por push.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1263 ms | 0 | 2 ms | 88,599 B |
| Solución IA | 1.00 | 1.00 | 908 ms | 0 | 0 ms | 23,343 B |
| Producto IA | 1.00 | 1.00 | 908 ms | 0 | 0 ms | 37,309 B |
| Sector tecnología | 0.98 | 1.00 | 960 ms | 0.087 | 0 ms | 24,400 B |
| Perspectiva IA | 0.98 | 1.00 | 906 ms | 0.087 | 0 ms | 26,003 B |
| Demo | 1.00 | 1.00 | 978 ms | 0 | 0 ms | 22,076 B |

## Evidencia archivada

- Lighthouse artifact `9128349512`, SHA256 `cb715e01e74bcaa90d737e45671f6471eac332337468c7952836f04552d02451`;
- CI artifact `9128364000`, SHA256 `9aaa59e1c9396aa83afbb0cd8678ec81906b7af546c97cb882efd3c8bc92a094`;
- release-health artifact `9128364217`, SHA256 `24a790e538efff0c7d43f77c1724bb4c54e070f219da361193d5d54262991f3`.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas Playwright;
- Chromium desktop/mobile y WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- WhatsApp como handoff manual, sin autoenvío;
- sin CRM/backend, almacenamiento servidor, firma, pagos, agenda ni carga documental ficticios.

## Condición de release definitiva

Este documento declara `5.12.0`. La release queda definitivamente cerrada solo cuando el SHA que contiene el cierre atraviesa nuevamente builder, idempotencia, Pages, Browser/axe, Lighthouse, release-health, sincronización pública de versión y termina con `main == stable`.

## Próximo ciclo

v5.13 debe concentrarse en **confianza de decisión y continuidad entre prueba verificable y brief comercial**: hacer que la modalidad elegida y las expectativas de prueba/entrega acompañen el recorrido hasta la preparación de WhatsApp, sin añadir persistencia servidor ni afirmaciones no verificables.

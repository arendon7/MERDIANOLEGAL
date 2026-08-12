# Meridiano Legal v5.11.0 — Contratación, inicio e higiene de CI

Fecha: 2026-08-11

## Objetivo

v5.11 cierra dos fricciones distintas pero relacionadas con la confiabilidad del recorrido comercial: elimina la carrera entre el builder canónico y Pages, y aclara jurídicamente cuándo una solicitud o propuesta pasa a un encargo realmente iniciado. La web sigue siendo estática y no inventa firma electrónica, pagos, agenda, CRM, expediente ni carga documental.

## 1. Release serializada detrás del builder

`Site Quality and Deploy` ya no se dispara directamente por `push`. La topología canónica es:

`push de fuente → Build canonical public site → workflow_run exitoso → Site Quality and Deploy → Browser/axe + Lighthouse → stable`.

Cambios principales:

- se eliminó el trigger directo `push` de `.github/workflows/pages.yml`;
- se conserva `workflow_dispatch` y el `workflow_run` del builder canónico;
- `scripts/validate_pages_trigger_v511.py` impide reintroducir la carrera;
- `scripts/validate_ci_v56.py` se actualizó para exigir la nueva topología más fuerte;
- Release Governance y el snapshot final validan también este contrato.

Evidencia de topología: tras mergear el cambio, builder `31560235195` terminó con `Canonical public files are current.` y solo después se creó un único `Site Quality and Deploy` `31560254312`, evento `workflow_run`, sin ejecución directa por `push`.

## 2. Preparación jurídica del encargo

La portada/contacto diferencia ahora cuatro estados que no deben confundirse:

1. **Solicitud preparada** — contexto mínimo listo para que el usuario decida si envía WhatsApp;
2. **Propuesta emitida** — alcance, entregables, cronograma, honorarios, responsabilidades, supuestos y exclusiones;
3. **Propuesta aceptada** — aceptación expresa según el mecanismo y condiciones de la propia propuesta;
4. **Encargo iniciado** — condiciones de inicio, responsables, canal de trabajo e información inicial confirmados.

Antes del inicio operativo se explicitan, según corresponda:

- partes relevantes y posibles conflictos;
- alcance, entregables, exclusiones y responsables;
- honorarios, gastos, facturación y condiciones económicas;
- fecha o condición de inicio y prioridades;
- interlocutores autorizados y reglas de coordinación;
- canal adecuado para información y documentos confidenciales.

La web pública deja expresamente indicado que no acepta contratos, no cobra pagos, no reserva agenda, no crea expedientes, no habilita carga documental y no inicia el encargo automáticamente.

Implementación:

- `engagement-v511.css`;
- `scripts/apply_engagement_v511.py`;
- `scripts/validate_engagement_v511.py`;
- cobertura añadida dentro de las 37 entradas Playwright existentes, sin aumentar el total.

## Evidencia funcional previa al cierre documental

Run: `31560805174`

SHA certificado: `cf4341eb9ec051a3e583b4675263b228ee5f0839`

Antes del cierre documental:

- `main == stable == cf4341eb9ec051a3e583b4675263b228ee5f0839`;
- builder e idempotencia: success;
- validadores históricos + v5.8 + v5.9 + v5.10 + v5.11: success;
- Pages + smoke público: success;
- Browser E2E: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- tiempo hasta gate de `stable`: 193 s;
- baseline v5.5: 279 s;
- mejora frente a baseline: 30.8%;
- cobertura reducida: no;
- budgets relajados: no;
- release governance: 5 workflows, 22 usos de Actions, SHA pinning, permisos, dependencias y gates protegidos;
- `PAGES TRIGGER V5.11 OK`: Pages espera al builder canónico y no compite por push.

### Browser/axe

- Chromium desktop: flujo comercial y engagement readiness pass;
- Chromium mobile: pass;
- WebKit desktop: pass;
- axe: 7/7 superficies sin violaciones serias/críticas.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1247 ms | 0 | 74 ms | 86,682 B |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,310 B |
| Producto IA | 1.00 | 1.00 | 907 ms | 0 | 0 ms | 35,468 B |
| Sector tecnología | 0.98 | 1.00 | 922 ms | 0.087 | 0 ms | 24,507 B |
| Perspectiva IA | 0.98 | 1.00 | 902 ms | 0.087 | 0 ms | 25,914 B |
| Demo | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 22,058 B |

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas Playwright;
- Chromium desktop/mobile y WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- workers Playwright CI = 1;
- idempotencia canónica;
- `stable` solo después de Browser + Lighthouse verdes;
- telemetría sin PII;
- handoff real por WhatsApp sin envío automático;
- sin almacenamiento servidor ni integraciones contractuales ficticias.

## Condición de release definitiva

Este documento declara `5.11.0`, pero la release solo queda definitivamente cerrada cuando el commit que contiene este cierre vuelve a aprobar builder, idempotencia, Pages, Browser/axe, Lighthouse y release-health y termina nuevamente con `main == stable`.

## Próximo ciclo

v5.12 debe concentrarse en **prueba comercial verificable y apoyo a la decisión de compra**: explicar mejor método, evidencia y criterios de elección entre servicios/productos sin inventar clientes, testimonios, casos de éxito ni resultados no demostrables.

# Meridiano Legal v5.9.0 — Calificación comercial y preparación de propuesta

Fecha: 2026-08-11

## Objetivo

v5.9 fortalece el paso entre la claridad de compra introducida en v5.8 y una conversación comercial útil. La web sigue siendo estática: no crea CRM, no almacena formularios en servidor y no declara automatizaciones inexistentes.

## Cambios principales

- capa de calificación comercial integrada en el formulario público;
- tres datos estructurados: momento de decisión, horizonte y rango de inversión opcional;
- resumen visible antes del handoff;
- recomendación de siguiente paso operativo —orientación, llamada de alcance o propuesta estructurada— sin puntuar ni excluir al lead;
- incorporación del contexto v5.8 y de la calificación al mensaje preparado para WhatsApp;
- privacidad por diseño: las respuestas solo se incorporan cuando el usuario decide abrir WhatsApp;
- telemetría protegida contra nombre, correo, empresa y texto libre del caso;
- `commercial-intake-v59.json` como contrato de fuente de la capa;
- `commercial-intake-v59.js` y `commercial-intake-v59.css` como runtime/presentación;
- `scripts/apply_commercial_v59.py` y `scripts/validate_commercial_v59.py` integrados a la cadena canónica;
- cobertura v5.9 añadida dentro de las 37 entradas Playwright existentes.

## Compatibilidad canónica corregida

Durante el ciclo los gates bloquearon dos problemas antes de promover `stable`:

1. el generador histórico v4.9 exigía una firma exacta del `<form>` y rechazaba el nuevo atributo de extensión v5.9; se volvió tolerante a atributos posteriores sin debilitar el contrato histórico;
2. el builder volvía a ejecutar v5.8 después de v5.9 y alteraba el orden final de CSS; la topología se corrigió para terminar siempre en `v5.8 → v5.9`.

Governance se reforzó para probar explícitamente la composición `v4.9 → v5.9` y vigilar el generador v4.9. No se redujo cobertura ni se relajaron presupuestos.

## Evidencia funcional previa al cierre documental

Run: `31547313170`

SHA certificado: `a64d2d957e3ca6c96fec855be85019680ebe6a03`

Antes del cierre documental:

- `main == stable == a64d2d957e3ca6c96fec855be85019680ebe6a03`;
- idempotencia canónica: success;
- validadores históricos + v5.8 + v5.9: success;
- Pages + smoke: success;
- Browser E2E: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- tiempo hasta gate de `stable`: 196 s;
- baseline v5.5: 279 s;
- mejora: 29.7%;
- cobertura reducida: no;
- budgets relajados: no;
- governance: 5 workflows y 22 usos de Actions validados con SHA pinning, permisos y dependencias protegidas.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1286 ms | 0 | 0 ms | 80,365 B |
| Solución IA | 1.00 | 1.00 | 1011 ms | 0 | 0 ms | 23,195 B |
| Producto IA | 1.00 | 1.00 | 1005 ms | 0 | 0 ms | 35,409 B |
| Sector tecnología | 0.98 | 1.00 | 1005 ms | 0.087 | 0 ms | 24,220 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,814 B |
| Demo | 1.00 | 1.00 | 1095 ms | 0 | 0 ms | 22,073 B |

## Condición de release definitiva

Este documento declara `5.9.0`, pero la release solo se considera cerrada cuando el commit que contiene este cierre vuelve a aprobar la certificación pública completa y termina nuevamente con `main == stable`.

## Integraciones: verdad operativa

Activas:

- GitHub Pages;
- WhatsApp como handoff real;
- contexto comercial local/de sesión;
- telemetría first-party/local sin PII;
- demo estático/noindex;
- builder, idempotencia, Browser E2E, axe, Lighthouse, governance health y `stable`.

No deben declararse activas sin configuración verificable:

- CRM/backend de leads;
- almacenamiento servidor del formulario;
- proveedor externo de analítica;
- email transaccional;
- dominio personalizado/CNAME;
- Search Console.

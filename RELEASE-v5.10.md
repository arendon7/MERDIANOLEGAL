# Meridiano Legal v5.10.0 — De intención comercial a propuesta y cierre

Fecha: 2026-08-11

## Objetivo

v5.10 convierte la claridad de compra de v5.8 y la calificación comercial de v5.9 en una ruta explícita hacia propuesta y contratación, sin inventar CRM, backend, almacenamiento de leads, firma electrónica, pagos ni automatizaciones externas.

## Cambios principales

- las 16 fichas profundas transmiten intención comercial contextual desde su CTA;
- los productos orientan a solicitud de propuesta y los servicios a definición de alcance;
- el formulario recibe ese contexto y permite modificarlo libremente;
- se incorpora una ruta visible `calificación → alcance/propuesta → aceptación → inicio`;
- se explica qué debe contener una propuesta: objetivo, perímetro, entregables, cronograma y supuestos/exclusiones;
- se explicitan las verificaciones que aún deben ocurrir antes de considerar contratado un encargo;
- el handoff continúa siendo WhatsApp preparado por el usuario, sin envío automático;
- la telemetría conserva el contrato sin PII ni texto libre del asunto;
- `conversion-close-v510.css`, `scripts/apply_conversion_v510.py` y `scripts/validate_conversion_v510.py` quedan integrados a la cadena canónica;
- la cobertura v5.10 se incorporó dentro de las 37 entradas Playwright protegidas.

## Regresiones bloqueadas y corregidas

Los gates detectaron dos incompatibilidades antes de promover `stable`:

1. **composición v5.9 → v5.10:** `apply_commercial_v59.py` exigía una firma del formulario incompatible con atributos añadidos por capas posteriores. Se corrigió para normalizar solo su propio contrato y preservar extensiones futuras. El builder volvió a quedar idempotente y terminó con `Canonical public files are current.`;
2. **contraste WCAG:** axe detectó una violación `color-contrast` seria únicamente en `.close-legal-v510`. Se corrigió el color y la suite pública posterior pasó sin fallos ni retries.

No se redujo cobertura, no se relajó axe y no se modificaron los presupuestos Lighthouse.

## Evidencia funcional previa al cierre documental

Run: `31558953560`

SHA certificado: `f8b47f2ec2885cc39ff64a2448792f352619f9c3`

Antes del cierre documental:

- `main == stable == f8b47f2ec2885cc39ff64a2448792f352619f9c3`;
- builder e idempotencia: success;
- validadores históricos + v5.8 + v5.9 + v5.10: success;
- Pages + smoke público: success;
- Browser E2E: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- tiempo hasta gate de `stable`: 173 s;
- baseline v5.5: 279 s;
- mejora frente a baseline: 38.0%;
- cobertura reducida: no;
- budgets relajados: no;
- governance: 5 workflows y 22 usos de Actions con SHA pinning, permisos, dependencias y gates protegidos.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1250 ms | 0 | 0 ms | 84,524 B |
| Solución IA | 1.00 | 1.00 | 955 ms | 0 | 0 ms | 23,213 B |
| Producto IA | 1.00 | 1.00 | 905 ms | 0 | 0 ms | 35,506 B |
| Sector tecnología | 0.98 | 1.00 | 945 ms | 0.087 | 0 ms | 24,226 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,867 B |
| Demo | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 22,040 B |

## Contrato preservado

- 46 páginas HTML;
- 16 fichas profundas con fuente jurídica única;
- 37 entradas Playwright;
- Chromium desktop/mobile y WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- idempotencia canónica;
- `stable` solo después de Browser + Lighthouse verdes;
- telemetría sin PII;
- sin almacenamiento servidor ni integraciones comerciales ficticias.

## Condición de release definitiva

Este documento declara `5.10.0`, pero la release solo queda definitivamente cerrada cuando el commit que contiene este cierre vuelve a aprobar builder, idempotencia, Pages, Browser/axe, Lighthouse, release-health y termina nuevamente con `main == stable`.

## Próximo ciclo

v5.11 debe mejorar el paso **propuesta aceptada → contratación e inicio**, y corregir ruido/carreras innecesarias de CI si se confirma que el workflow de calidad puede dispararse sobre un commit fuente antes del builder. No se añadirán firma electrónica, pagos, CRM, calendario o carga documental mientras no exista integración real y gobernada.

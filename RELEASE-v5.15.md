# Meridiano Legal v5.15.0 — Eficiencia recomendación→acción

Fecha: 2026-08-12

## Objetivo

v5.15 reduce fricción entre la selección de modalidad, la explicación de por qué puede encajar y el siguiente paso comercial. La mejora consolida superficies existentes en lugar de añadir otro bloque de decisión: el encaje queda junto al CTA, los límites y alternativas pasan a comparación secundaria y la ruta comercial se mantiene explícita y controlada por el usuario.

## Implementado

- `decision-action-v515.css` y `decision-action-v515.js`;
- `scripts/apply_decision_action_v515.py` y `scripts/validate_decision_action_v515.py`;
- el `fit` canónico v5.14 se muestra directamente dentro de las cinco tarjetas de modalidad v5.12;
- la comparación ampliada v5.14 conserva cinco modalidades, límites y alternativas, pero inicia colapsada para evitar duplicación visual;
- el brief del formulario prioriza una razón visible, una ruta comercial y un detalle secundario para límite/alternativa;
- las rutas canónicas quedan: diagnóstico→`scope`, auditoría→`proposal`, producto→`proposal`, servicio especializado→`scope`, recurrente→`scope`, sin contexto→`orientation`;
- una intención explícita de entrada tiene prioridad y la web nunca cambia automáticamente la etapa del usuario;
- la aplicación de una ruta sugerida requiere clic del usuario y reutiliza el flujo comercial existente;
- se corrigió el drift del enlace `Formulario general`: productos/auditoría conservan propuesta; diagnóstico/servicios/recurrente conservan definición de alcance;
- WhatsApp directo de las 16 fichas incluye el siguiente paso sugerido y conserva modalidad, estándar verificable, encaje, límite, alternativa y disclaimer;
- composición canónica `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15`;
- las 37 entradas Playwright existentes se reforzaron sin aumentar ni reducir el conteo.

## Privacidad y límites preservados

v5.15 no introduce:

- cuestionario nuevo;
- scoring o ranking opaco;
- `localStorage` o `sessionStorage` para decisión comercial;
- backend o CRM;
- transporte `fetch`/XHR propio de la capa;
- PII adicional en telemetría;
- testimonios, clientes o resultados fabricados;
- firma, pagos, agenda, expediente o carga documental ficticios.

`window.MeridianoDecisionActionV515` declara `automaticChange: false`, `scoring: false`, `networkTransport: false`, `persistentStorage: false` y `piiInTelemetry: false`.

## Compatibilidad: gates que detectaron regresiones y cómo se corrigieron

La release no se cerró ocultando fallos. Tres gates detectaron incompatibilidades y se conservaron intactos:

1. **Contrato CTA v5.10.** La primera candidata añadió `data-action-route-v515` al CTA profundo y rompió la forma canónica protegida por `validate_conversion_v510.py`. v5.15 eliminó el atributo redundante y conserva la ruta exclusivamente mediante `commercial_intent`. El validator v5.10 no se relajó.
2. **Contrato JSON embebido v5.14.** La consolidación inicial reemplazó el bloque visible y omitió `recommendation-contract-v514`. v5.15 volvió a insertar el mismo JSON canónico y su validator exige igualdad estructural con `recommendation-v514.json`. El validator v5.14 no se relajó.
3. **Semántica de query en E2E.** Browser encontró que las URLs tenían correctamente `commercial_intent`, `modality` y `proof_standard`, pero el test asumía un orden textual fijo. E2E pasó a verificar los valores exactos con `URLSearchParams` y `#contacto`, sin reducir cobertura ni omitir axe.

## Evidencia funcional certificada antes del cierre documental

Run: `31609518536`

SHA funcional certificado: `48a0692e8e4f999a85cfd8619fe2e293528945c2`

- `main == stable == 48a0692e8e4f999a85cfd8619fe2e293528945c2`;
- builder/idempotencia + validadores históricos + composición v5.8→v5.15: PASS;
- Pages + smoke público: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe: sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI hasta `stable`: 209 s;
- baseline v5.5: 279 s;
- mejora: 25.1%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- trigger builder→workflow_run→Pages: PASS;
- validator v5.15: PASS.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1322 ms | 0 | 3 ms | 99,735 B |
| Solución IA | 1.00 | 1.00 | 989 ms | 0 | 0 ms | 23,234 B |
| Producto IA | 1.00 | 1.00 | 999 ms | 0 | 0 ms | 37,677 B |
| Sector tecnología | 0.98 | 1.00 | 1006 ms | 0.087 | 0 ms | 24,289 B |
| Perspectiva IA | 1.00 | 1.00 | 1044 ms | 0 | 0 ms | 25,796 B |
| Demo | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 21,994 B |

### Evidencia archivada

- Lighthouse artifact `9146643912`, SHA256 `f76b194a8dea5a8a782bc528203426f90a9009858fd383e135ee23cf9cf4241c`;
- CI artifact `9146680067`, SHA256 `d2d2206525568a189bfaae9743f9c0d13a229ed2dc6d448fd9252ca64b7ceaf0`;
- Release Governance artifact `9146680564`, SHA256 `e481b173075db9d44ba934c60a92b48984e66bb553e265fcb057b4a27a2fd10b`.

## Graphify

En el cierre funcional, `knowledge/graphify-live` apunta exactamente a `source_commit = 48a0692e8e4f999a85cfd8619fe2e293528945c2`, con 544 nodos, 877 relaciones y 88 notas wiki. La versión declarativa del snapshot sigue en 5.14.0 hasta que este cierre formal atraviese el builder y la nueva sincronización pública.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas Playwright;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- workers Playwright CI = 1;
- fuente jurídica única para alcance/entregables;
- telemetría sin PII;
- WhatsApp como handoff manual;
- sin scoring opaco;
- sin CRM/backend ni almacenamiento servidor del formulario.

## Condición de cierre definitivo

Este documento declara `5.15.0`. La release queda definitivamente cerrada solo cuando el SHA que contiene este cierre atraviesa nuevamente builder, sincronización pública de versión, idempotencia, Pages, Browser/axe, Lighthouse, release-health y termina con `main == stable`.

## Próximo ciclo

v5.16 se concentrará en **UX móvil y accesibilidad del recorrido comercial**: reducir scroll/fricción en pantallas pequeñas y revisar la diferencia restante de Lighthouse Accessibility de la portada, sin recortar contenido jurídico, cobertura ni controles de decisión.

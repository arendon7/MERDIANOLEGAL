# Meridiano Legal v5.16.0 — UX móvil y accesibilidad verificable

Fecha: 2026-08-12.

## Objetivo

Reducir fricción y scroll en móvil y resolver causas reales de accesibilidad/escaneabilidad sin ocultar contenido jurídico material, sin alterar la decisión controlada por el usuario y sin relajar ningún gate de calidad.

## Implementación

### 1. Observabilidad Lighthouse de accesibilidad

`scripts/run_quality_v55.mjs` conserva en `summary.json` y `summary.md` las auditorías de accesibilidad con score menor a 1, con detalles acotados. `scripts/validate_quality_v55.py` blinda esa observabilidad y confirma que budgets, superficies y política de retries no cambian.

### 2. Targets táctiles de portada

El diagnóstico identificó `target-size` en tres CTA “Explorar la práctica” de Perspectivas. v5.16 eleva esos targets a un mínimo de 44 px. La portada pasó de A11y 0.97 a 1.00 en Lighthouse.

### 3. Progressive disclosure móvil sin pérdida material

En viewport <=760 px, los bloques largos de v5.10 y v5.11 mantienen sus encabezados visibles y agrupan el detalle secundario en `<details>` nativos. Calificación v5.9, contexto v5.13 y recomendación/ruta v5.14-v5.15 permanecen visibles. Sin JavaScript, el HTML conserva el contenido expandido original.

### 4. Foco y regiones desplazables

Axe móvil reveló tres regiones horizontalmente desplazables sin acceso de teclado en Safari. v5.16 añade `tabindex=0`, `role=region`, `aria-label` y foco visible a esas superficies en móvil. También corrige el contraste del primer paso comercial que se hizo auditable al abrir el disclosure.

### 5. Fichas profundas

El diagnóstico ampliado detectó en Programa de Gobernanza IA una A11y 0.91 por contraste del CTA móvil y `target-size` del menú/enlaces profundos. La release no se cerró con esa deuda conocida. El hardening final exige:

- botón de menú >=44×44 px;
- cinco enlaces del menú abierto >=44 px de alto;
- CTA móvil con contraste explícito;
- auditoría axe de la ficha en viewport 390×844 con el menú abierto.

La ficha pasó finalmente a A11y 1.00.

## Gates que detectaron problemas reales

v5.16 no convirtió fallos en excepciones ni debilitó tests:

1. Lighthouse expuso el `target-size` detrás del 0.97 de portada;
2. Browser/axe móvil expuso contraste y regiones desplazables sin foco;
3. el nuevo diagnóstico Lighthouse expuso A11y 0.91 en la ficha profunda;
4. cada causa se corrigió en fuente y se volvió a certificar antes de promover `stable`.

## Evidencia funcional certificada

Run: `31618614227`  
SHA funcional: `2cd5fb0d2b428187c08cf21e562427f9bc44508c`

- `main == stable` en el cierre funcional;
- builder/idempotencia + validadores: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- tiempo de pared Browser reporter: 76 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- `accessibilityAuditGaps`: vacío en las seis superficies;
- CI hasta `stable`: 187 s;
- baseline v5.5: 279 s;
- mejora: 33.0%;
- cobertura reducida: no;
- budgets relajados: no.

### Lighthouse final funcional

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|
| Portada | 1.00 | 1.00 | 1255 ms | 0 | 7 ms |
| Solución IA | 1.00 | 1.00 | 902 ms | 0 | 0 ms |
| Producto IA | 1.00 | 1.00 | 905 ms | 0 | 0 ms |
| Sector tecnología | 0.98 | 1.00 | 905 ms | 0.087 | 0 ms |
| Perspectiva IA | 1.00 | 1.00 | 902 ms | 0 | 0 ms |
| Demo | 1.00 | 1.00 | 905 ms | 0 | 0 ms |

Artefactos:

- Lighthouse `9150367908` — `sha256:73290506d7149c03299ffd43c82a30f13b11ad2af801cc5a19aa411f8c0e002d`;
- CI `9150389424` — `sha256:a130b599977430eb908f59a33be8eab127d6f490b9c3acb86d79b70b4ce58b33`.

## Privacidad y límites preservados

v5.16 no añade:

- cuestionario nuevo;
- scoring/ranking opaco;
- `localStorage` o `sessionStorage` adicional para la decisión;
- backend/CRM;
- transporte XHR/fetch propio;
- PII adicional;
- testimonios, clientes o resultados fabricados;
- firma, pagos, agenda, expediente o carga documental ficticios.

WhatsApp continúa siendo handoff manual. La telemetría permanece sin PII.

## Contratos preservados

- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- workers Playwright CI = 1;
- builder idempotente;
- fuente jurídica única;
- `stable` solo después de todos los gates verdes.

## Graphify / procedencia

El snapshot funcional previo al versionado formal apunta exactamente a `source_commit = 2cd5fb0d2b428187c08cf21e562427f9bc44508c`, Graphify 0.9.26, 548 nodos, 882 relaciones y 88 notas. Su `version` todavía era 5.15.0 porque se generó antes de elevar `version.json`.

No se debe falsificar ese campo. El merge de este cierre debe provocar un nuevo snapshot Graphify con el commit fuente real correspondiente. Si el builder genera después un commit exclusivo de sincronización visible, cualquier equivalencia deberá documentarse mediante comparación de commits, no reescribiendo la procedencia.

## Condición de cierre definitivo

Este documento declara 5.16.0, pero la release solo queda definitivamente cerrada cuando el SHA versionado vuelva a superar builder, idempotencia, Pages, Browser/axe, Lighthouse y release-health, y `main == stable` sobre ese SHA final.

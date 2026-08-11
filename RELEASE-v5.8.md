# Meridiano Legal v5.8.0 — Arquitectura de decisión y claridad de compra

Fecha: 2026-08-11.

## Objetivo

Reducir la fricción comercial de la web pública sin simplificar el contenido jurídico ni crear afirmaciones que no estén respaldadas por las fuentes canónicas.

v5.8 responde más rápido tres preguntas del visitante:

1. ¿qué forma de contratación corresponde a mi situación?;
2. ¿qué estoy comprando exactamente?;
3. ¿qué recibiré, qué debo aportar y qué queda fuera del alcance?

## Implementación

### Portada

Se añadió un selector de cuatro formas de contratación:

- entender primero el problema;
- contratar un resultado cerrado;
- obtener dirección jurídica recurrente;
- abordar una decisión o proyecto especializado.

La selección dirige a superficies existentes y evita obligar al usuario a conocer previamente el nombre técnico del servicio.

### 16 fichas profundas

Cada servicio y producto incorpora una lectura ejecutiva de cinco bloques:

1. `ENCAJA SI` — derivado de `situations`;
2. `QUÉ COMPRA` — derivado de `perimeter`;
3. `QUÉ RECIBE` — derivado de `deliverables`;
4. `QUÉ APORTA` — derivado de `requirements`;
5. `QUÉ NO ASUMIR` — derivado de `limits`.

También muestra duración, modalidad y audiencia provenientes de la misma fuente jurídica.

No se duplicó una segunda fuente de marketing: `scripts/apply_decision_v58.py` genera la capa directamente desde `catalog-products-v41/` y `catalog-services-v42/`.

### Contrato de integridad

`scripts/validate_decision_v58.py` comprueba:

- cuatro modalidades en portada;
- 16 fichas profundas;
- cinco bloques ejecutivos por ficha;
- correspondencia fuente→resumen;
- metadatos de contratación;
- ubicación runtime-safe del bloque antes de `#detail-page`.

La validación v5.8 forma parte del gate del catálogo estático y también se prueba en Release Governance para cambios relevantes.

### Runtime

El bloque ejecutivo se ubica como hermano anterior de `#detail-page`. De esta forma permanece visible cuando `catalog-page.js` re-renderiza el contenido del producto y también funciona sin JavaScript.

## Regresiones detectadas y corregidas por los gates

Durante la construcción se detectaron dos incompatibilidades antes de promover `stable`:

1. el parser histórico v4.5 asumía cuatro espacios exactos antes de una sección; se hizo tolerante a indentación sin debilitar la idempotencia;
2. el primer bloque v5.8 estaba dentro de `#detail-page` y el runtime de productos lo reemplazaba; Browser E2E lo detectó y `stable` no se movió. La capa se trasladó fuera del contenedor mutable y el validator ahora protege esa ubicación.

No se modificaron los tests para ocultar los fallos.

## Certificación funcional

Run final funcional: `31541197197`.

SHA certificado: `681c252f09a50447af0557a2039b34b8a79faed9`.

### Browser E2E + axe

- 37 entradas observadas;
- 35 aprobadas;
- 2 omitidas por diseño;
- 0 fallos;
- 0 retries;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe sin violaciones serias/críticas.

La cobertura v5.8 se añadió dentro de la entrada E2E existente, conservando las 37 entradas protegidas.

### Lighthouse

Las seis superficies aprobaron sin relajar presupuestos:

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1425 ms | 0 | 0 ms | 76,009 B |
| Solución IA | 1.00 | 1.00 | 978 ms | 0 | 0 ms | 23,234 B |
| Producto IA | 1.00 | 1.00 | 909 ms | 0 | 0 ms | 35,406 B |
| Sector tecnología | 1.00 | 1.00 | 938 ms | 0 | 0 ms | 24,260 B |
| Perspectiva IA | 1.00 | 1.00 | 1003 ms | 0 | 0 ms | 25,728 B |
| Demo | 1.00 | 1.00 | 970 ms | 0 | 0 ms | 22,045 B |

### CI

- tiempo hasta gate de `stable`: 232 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 16.8%;
- cobertura reducida: no;
- presupuestos relajados: no.

## Invariantes preservados

- 37 entradas Playwright;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- Chromium + WebKit;
- Actions fijadas por SHA;
- permisos controlados;
- release-health v5.7;
- `stable` solo después de Browser + Lighthouse;
- sin precios, clientes, testimonios, integraciones ni resultados inventados.

## Condición de cierre

La release 5.8.0 queda cerrada cuando el commit que declara esta versión vuelve a atravesar la certificación pública completa, `main == stable` y la memoria estructural queda alineada con el estado final.
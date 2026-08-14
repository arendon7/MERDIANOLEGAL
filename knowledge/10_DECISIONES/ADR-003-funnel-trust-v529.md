# ADR-003 — Observar el funnel sin PII y acercar confianza verificable a la decisión

Fecha: 2026-08-14
Estado: aceptada e implementada en v5.29

## Contexto

v5.28 redujo la distancia editorial entre contratación y contacto, pero la web mantenía dos limitaciones distintas:

1. existían eventos de telemetría v5.0, medición v5.3 y observabilidad de handoff v5.18, pero no formaban un funnel semántico único que permitiera distinguir exposición a necesidad, oferta, evidencia, decisión, contacto y handoff;
2. la trayectoria profesional verificable v5.25 estaba disponible en `firma.html` y en un bloque institucional de portada, pero no aparecía de forma compacta en el punto inmediatamente anterior a presentar una necesidad.

La solución no debía crear analytics invasivo ni social proof ficticio. Tampoco podía interpretar un clic o un borrador preparado como venta, aceptación o inicio de encargo.

## Decisión

1. `funnel-contract-v529.json` define una taxonomía explícita de siete etapas observables: `awareness`, `need`, `offer`, `evidence`, `decision`, `contact` y `handoff`.
2. `funnel-observability-v529.js` agrega eventos en memoria, con máximo 48 entradas y sin identificador de sesión.
3. Se reutilizan los eventos ya sanitizados de `MeridianoTelemetry` y se añaden únicamente checkpoints de exposición a secciones públicas y a las 16 fichas mediante `data-catalog-id`.
4. No se leen valores de formularios ni se introducen `localStorage`, `sessionStorage`, cookies, IndexedDB, fingerprinting, UUID, `fetch`, XHR o `sendBeacon`.
5. El transporte público actual permanece deshabilitado. v5.29 reutiliza el adaptador existente pero no habilita proveedor ni red.
6. El estado máximo `handoff` significa que el navegador observó preparación/interacción del handoff manual. No significa envío, entrega, lectura, aceptación, inicio del encargo ni conversión a cliente.
7. Entre `#contratacion` y `#contacto` se inserta un `<aside>` de confianza derivado únicamente de `professional-authority-v525.json`.
8. El `<aside>` no crea una nueva `<section>` y preserva la invariante v5.28 según la cual `#contacto` es la siguiente sección narrativa después de `#contratacion`.
9. La señal de confianza declara expresamente que la trayectoria no constituye lista de clientes ni prueba de resultados específicos.
10. Los checkpoints de portada consideran exposición cuando al menos 5% de la superficie está visible. Este umbral evita exigir una proporción simultáneamente visible imposible para secciones más altas que el viewport móvil.
11. v5.29 se ejecuta dentro de la extensión canónica `v5.18+`, después de v5.28, sin alterar los 30 pasos del pipeline v5.24.

## Consecuencias

### Positivas

- La web dispone de una taxonomía de funnel verificable y testeable sin aumentar exposición de datos personales.
- Las 16 fichas profundas participan en el mismo modelo observacional que la portada.
- Se distingue intención/progreso observable sin inflar una métrica de conversión.
- La trayectoria relevante aparece cerca del punto de decisión sin repetir una biografía completa.
- Se mantiene el contrato de v5.28 y el único formulario físico.

### Límites deliberados

- No existe analítica agregada entre sesiones mientras el adaptador público permanezca deshabilitado.
- No se atribuyen clientes, resultados, premios, testimonios o métricas de éxito.
- No se observa el contenido del formulario.
- No se sabe si un mensaje de WhatsApp fue enviado, entregado o leído.
- No se sabe si una propuesta fue aceptada ni si comenzó una relación profesional.

## Verificación final

- `scripts/validate_funnel_trust_v529.py` protege privacidad, semántica, orden, fuente de autoridad, umbral observable y cobertura de las 16 fichas.
- `tests/e2e/funnel-trust-v529.spec.mjs` verifica navegación, memoria local, ausencia de contenido del formulario, ficha profunda, checkpoints reales y compatibilidad con v5.28.
- Los validators históricos, axe, Lighthouse, Pages/smoke y Release Governance permanecieron obligatorios.
- Certificación funcional final: `31823985048` sobre `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70` — PASS.
- Browser E2E/axe: 88 observados · 86 PASS · 2 SKIP · 0 FAIL · 0 retries.

## Estado

La decisión quedó implementada y certificada funcionalmente. El commit documental que marque el canal `certified` debe volver a atravesar todos los gates antes de convertirse en la referencia final de v5.29.

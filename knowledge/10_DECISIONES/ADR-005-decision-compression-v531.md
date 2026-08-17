# ADR-005 — Compresión decisional mediante divulgación progresiva v5.31

Estado: aceptado · implementado · certificado funcionalmente.
Fecha: 2026-08-17.

## Contexto

Entre v5.8 y v5.30 se añadieron capas válidas para encaje, modalidad, prueba, cierre y lógica de contratación. La auditoría posterior confirmó que, vistas como sistema, varias repetían decisiones antes del núcleo técnico. El problema era de jerarquía de información, no de falta de contenido.

## Decisión

v5.31 usa elementos HTML nativos `<details>/<summary>` para hacer progresiva la profundidad secundaria, sin borrar ni cargar contenido de forma diferida.

En las 16 fichas:

- `buying-clarity-v58` + v5.30 permanecen abiertos como primer grupo de decisión;
- pregunta ejecutiva + resultado se agrupan visualmente como segundo grupo abierto;
- `offer-narrative-v522` se conserva íntegro dentro de un `<details>` cerrado por defecto.

En las 6 rutas de necesidad:

- permanecen abiertos hero, señales, encaje, decisiones, modalidad, honorarios, resultado, límites y CTA;
- objeciones, FAQ, rutas relacionadas y prueba/contexto pasan a `<details>` independientes.

## Razones

1. Reduce scroll y carga cognitiva sin eliminar verdad jurídica/comercial.
2. Mantiene el contenido en el DOM y disponible para usuarios, indexación y validadores.
3. Usa semántica HTML nativa con teclado, evitando JavaScript de acordeón y nuevas dependencias.
4. Conserva las capas históricas v5.8, v5.22 y v5.30 para no romper contratos ni reescribir fuentes.
5. Se integra como normalización final después de v5.30 dentro del paso canónico existente v5.18+, manteniendo 30 pasos.

## Validación

- SHA funcional certificado: `159be8a9e467a303faa8d302bfac93b33c2e7b29`.
- Builder #161 (`32059316508`): PASS con 30 pasos canónicos.
- Site Quality and Deploy #383 (`32059355395`): PASS.
- Browser E2E/axe: 112 observados · 110 PASS · 2 SKIP · 0 FAIL · 0 reintentos.
- Lighthouse: PASS con budgets existentes.
- Graphify #314: PASS sobre el mismo SHA funcional; 800 nodos, 1.368 relaciones y 106 notas wiki.
- `stable` fue promovido únicamente después de todos los gates verdes.

## Consecuencias

- Los tests distinguen contenido siempre visible de contenido secundario accesible bajo interacción.
- Los validadores históricos siguen pasando porque el contenido y marcadores permanecen.
- No se permite `display:none`, `visibility:hidden`, atributo `hidden` ni borrado de copy para simular menor densidad.
- Las correcciones de compatibilidad E2E reforzaron activación por teclado y selectores semánticos sin rebajar cobertura.
- La decisión deberá revisarse si `<details>` genera problemas demostrables de accesibilidad, SEO o comprensión.

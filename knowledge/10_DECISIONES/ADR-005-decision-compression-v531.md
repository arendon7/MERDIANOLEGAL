# ADR-005 — Compresión decisional mediante divulgación progresiva v5.31

Estado: propuesto.
Fecha: 2026-08-17.

## Contexto

Entre v5.8 y v5.30 se añadieron capas válidas para encaje, modalidad, prueba, cierre y lógica de contratación. La auditoría posterior confirmó que, vistas como sistema, varias repiten decisiones antes del núcleo técnico. El problema es de jerarquía de información, no de falta de contenido.

## Decisión

v5.31 usará elementos HTML nativos `<details>/<summary>` para hacer progresiva la profundidad secundaria, sin borrar ni cargar contenido de forma diferida.

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

## Consecuencias

- Los tests deben distinguir contenido siempre visible de contenido secundario accesible bajo interacción.
- Los validadores históricos deben seguir pasando porque el contenido y marcadores permanecen.
- No se permite `display:none`, `visibility:hidden`, atributo `hidden` ni borrado de copy para simular menor densidad.
- La decisión deberá revisarse si `<details>` genera problemas demostrables de accesibilidad, SEO o comprensión.

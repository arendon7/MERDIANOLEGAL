# Auditoría de recorrido público — baseline v5.31

Fecha: 2026-08-17.
Baseline: `main = stable = 48b4deb97087f651d07628467be148807873f6fa` · v5.30.0 certificada.

## Hallazgo

La web ya tiene suficiente profundidad jurídica, comercial, de autoridad y de cierre. La fricción observable no es ausencia de información, sino **acumulación de capas decisionales válidas que permanecen abiertas simultáneamente**.

### Portada

La portada permite entrada directa por necesidad y contacto, pero también expone sucesivamente necesidades, modalidades, prueba, 8 servicios, 8 productos, entregables, demo, planes, honorarios y contratación. No se propone retirar ninguna de estas superficies en v5.31 porque los accesos directos ya permiten saltarlas y porque allí viven referencias públicas de honorarios aprobadas.

### Rutas de necesidad

Las seis rutas funcionales siguen una secuencia extensa: hero → señales → encaje → decisiones → tres modalidades → objeciones → honorarios → resultado → límites → FAQ → rutas relacionadas → prueba → CTA.

La ruta primaria es útil. La fricción aparece en cuatro capas secundarias —objeciones, FAQ, rutas relacionadas y prueba/contexto— que se muestran abiertas aunque el usuario ya haya identificado su necesidad.

### 16 fichas profundas

Todas comparten cinco capas de framing antes de entrar al núcleo técnico:

1. `buying-clarity-v58`;
2. `offer-commercial-v530`, integrado dentro de v5.8;
3. pregunta ejecutiva;
4. resultado empresarial;
5. `offer-narrative-v522`.

v5.8/v5.30 ya responden encaje, compra, entregables, límites, unidad, honorarios, cambio de alcance y cierre. v5.22 vuelve a explicar decisión, modalidad, capacidad instalada y alternativa antes del alcance detallado. El contenido es correcto, pero la exposición simultánea es redundante.

## Baseline medible

- 16/16 fichas presentan el patrón acumulativo.
- 6/6 rutas de necesidad presentan cuatro capas secundarias abiertas.
- La profundidad no debe eliminarse ni ocultarse mediante CSS.
- Las referencias públicas de honorarios de la portada son verdad aprobada y quedan fuera del cambio.

## Objetivo v5.31

Aplicar divulgación progresiva nativa:

- en fichas, mantener siempre abiertos v5.8/v5.30 como primer grupo y pregunta+resultado como segundo grupo compacto;
- conservar v5.22 completo dentro de `<details>` cerrado por defecto y accesible por teclado;
- en rutas, mantener hero, señales, encaje, decisiones, modalidad, honorarios, resultado, límites y CTA abiertos;
- mover solo objeciones, FAQ, rutas relacionadas y prueba/contexto a `<details>` nativos;
- no eliminar copy, fuentes, honorarios, límites, alternativas o evidencia.

## No objetivos

No rediseñar la marca, no reescribir las 16 ofertas, no modificar precios, no añadir cotizador/CRM/backend, no alterar el formulario, no cambiar funnel/handoff, no reducir accesibilidad ni budgets y no cambiar los 30 pasos canónicos.

# ADR-004 — Hacer explícita la lógica de contratación dentro del resumen ejecutivo de cada oferta

Fecha: 2026-08-14
Estado: aceptada e implementada en v5.30

## Contexto

Las 16 ofertas de Meridiano Legal ya contenían profundidad jurídica y comercial significativa. Los catálogos fuente definían perímetro, método, entregables, formatos, cronograma, responsabilidades, aceptación, límites y extensiones. Además, v5.8 materializaba una lectura ejecutiva de encaje, compra, entregables, participación y límites; v5.22 explicaba decisión empresarial, modalidad, capacidad instalada, alternativa y lente jurídica.

La auditoría v5.30 identificó que la fricción remanente no consistía en falta de contenido, sino en la necesidad de reconstruir manualmente cinco preguntas de contratación distribuidas a lo largo de la ficha: unidad de contratación, lógica de honorarios, variables de dimensionamiento, regla de ampliación y definición de cierre.

Crear otra sección larga habría duplicado v5.8/v5.22 y aumentado densidad. Publicar tarifas genéricas o un cotizador automático también habría sido incorrecto, porque varias ofertas dependen de entidades, documentos, rondas, actores, urgencia y especialidades que modifican materialmente el esfuerzo.

## Decisión implementada

1. `offer-commercial-v530.json` funciona como contrato complementario para exactamente las 16 ofertas.
2. `catalog-products-v41/` y `catalog-services-v42/` permanecen como fuente jurídica principal de perímetro, entregables, aceptación, límites y suplementos.
3. Cada oferta declara `engagement_basis`, `fee_logic`, tres `drivers`, `change_rule` y `close_rule`.
4. El contrato v5.30 no almacena importes, monedas, descuentos ni tarifas.
5. `scripts/apply_offer_commercial_v530.py` materializa la información dentro de `buying-clarity-v58`, inmediatamente después de `buying-clarity-meta-v58`.
6. No se creó una nueva `<section>` narrativa; la extensión permanece subordinada al resumen ejecutivo existente.
7. El bloque enlaza a `#perimetro-title`, `#aceptacion-title` y `#contacto`.
8. Los tres drivers se muestran en un `<details>` nativo para mantener visible la síntesis y dejar la explicación ampliada bajo demanda.
9. No se introdujo JavaScript funcional para la capa v5.30.
10. v5.30 se ejecuta después de v5.29 dentro de `apply_handoff_observability_v518.py`, conservando exactamente los 30 pasos canónicos del pipeline v5.24.
11. La capa quedó protegida por validator estático, E2E, axe, Lighthouse, Release Governance, idempotencia, Pages y promoción de `stable`.

## Consecuencias positivas

- La profundidad ya existente es más fácil de comprar sin reducir rigor.
- Los productos explican con mayor claridad la relación entre paquete base y suplementos.
- Los servicios explican cómo se dimensiona una propuesta sin fingir una tarifa universal.
- El cliente puede distinguir alcance inicial, variables de ampliación y cierre antes de recorrer la ficha completa.
- La solución reutiliza v5.8 y evita otra capa narrativa redundante.

## Límites deliberados

- v5.30 no publica precios ni produce cotizaciones.
- No existe cálculo automático de honorarios.
- No se altera el significado de contacto, handoff o conversión definido en v5.29.
- No se modifica el único formulario físico.
- No se crean capacidades de CRM, pago, firma, agenda, autenticación o portal.
- Las cantidades exactas siguen viviendo en los catálogos fuente; v5.30 no las replica como segunda verdad.

## Verificación final

- PR #134: integrada.
- Release Governance `31834565612`: PASS.
- Builder canónico `31834618506`: PASS.
- SHA funcional canónico: `ee88b8ced3347255cf85ee62e3bf4022b7c34a42`.
- Site Quality and Deploy `31834646140`: PASS.
- Idempotencia y 37/37 validaciones estáticas: PASS.
- Browser E2E/axe: **100 observados · 98 PASS · 2 SKIP · 0 FAIL · 0 reintentos**.
- Lighthouse: PASS contra budgets existentes.
- Promoción de `stable`: PASS.

## Estado

La decisión quedó implementada y certificada funcionalmente. El cierre documental se considera definitivo cuando el commit que contiene esta ADR haya atravesado el mismo pipeline público y los refs vigentes `main` y `stable` coincidan.

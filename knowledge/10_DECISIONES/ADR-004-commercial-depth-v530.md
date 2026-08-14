# ADR-004 — Hacer explícita la lógica de contratación dentro del resumen ejecutivo de cada oferta

Fecha: 2026-08-14
Estado: propuesta para v5.30

## Contexto

Las 16 ofertas de Meridiano Legal ya contienen profundidad jurídica y comercial significativa. Los catálogos fuente definen perímetro, método, entregables, formatos, cronograma, responsabilidades, aceptación, límites y extensiones. Además, v5.8 materializa una lectura ejecutiva de encaje, compra, entregables, participación y límites; v5.22 explica decisión empresarial, modalidad, capacidad instalada, alternativa y lente jurídica.

La auditoría v5.30 identificó que la fricción remanente no consiste en falta de contenido, sino en la necesidad de reconstruir manualmente cinco preguntas de contratación distribuidas a lo largo de la ficha: unidad de contratación, lógica de honorarios, variables de dimensionamiento, regla de ampliación y definición de cierre.

Crear otra sección larga duplicaría v5.8/v5.22 y aumentaría densidad. Publicar tarifas genéricas o un cotizador automático sería igualmente incorrecto, porque varias ofertas dependen de entidades, documentos, rondas, actores, urgencia y especialidades que modifican materialmente el esfuerzo.

## Decisión

1. Crear `offer-commercial-v530.json` como contrato complementario para exactamente las 16 ofertas.
2. Mantener `catalog-products-v41/` y `catalog-services-v42/` como fuente jurídica principal de perímetro, entregables, aceptación, límites y suplementos.
3. Exigir por oferta cinco elementos: `engagement_basis`, `fee_logic`, tres `drivers`, `change_rule` y `close_rule`.
4. No almacenar importes, monedas, descuentos ni tarifas en el contrato v5.30.
5. Materializar la información mediante `scripts/apply_offer_commercial_v530.py` dentro del bloque `buying-clarity-v58`, inmediatamente después de `buying-clarity-meta-v58`.
6. No crear una nueva `<section>` narrativa. La extensión debe ser un bloque compacto subordinado al resumen ejecutivo existente.
7. Enlazar desde el bloque a `#perimetro-title`, `#aceptacion-title` y `#contacto` para que la síntesis remita a la fuente detallada y al siguiente paso.
8. Mostrar los tres drivers dentro de un `<details>` para mantener visible la conclusión comercial y dejar la explicación ampliada bajo demanda.
9. No introducir JavaScript funcional para la capa v5.30; la interacción nativa de `<details>` es suficiente.
10. Encadenar v5.30 después de v5.29 dentro de `apply_handoff_observability_v518.py`, conservando exactamente los 30 pasos canónicos del pipeline v5.24.
11. Proteger la capa con validator estático, E2E, axe, Lighthouse, Release Governance, idempotencia, Pages y promoción de `stable`.

## Consecuencias positivas

- La profundidad ya existente se vuelve más fácil de comprar sin reducir rigor.
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

## Verificación

- `scripts/validate_offer_commercial_v530.py` verifica cobertura exacta de 16 ofertas, estructura contractual, ausencia de importes/monedas, ubicación dentro de v5.8, enlaces a perímetro/aceptación/contacto y tres drivers exactos por ficha.
- `tests/e2e/offer-commercial-v530.spec.mjs` verifica las 16 rutas, transparencia de honorarios sin cifras, servicio recurrente, foco nativo y ausencia de overflow móvil.
- Los gates históricos permanecen obligatorios y no deben relajarse para certificar v5.30.

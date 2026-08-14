# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**v5.30.0 — profundidad comercial de las 16 ofertas: activa como candidata.**

Baseline funcional certificada:

`main = stable = 36e014fd0cc852ce8835b6befdeb673328e838bd` al inicio del ciclo (v5.29.0).

Mientras v5.30 no supere Release Governance, builder, idempotencia, Pages/smoke, Browser E2E/axe y Lighthouse, `stable` debe continuar representando la última release certificada.

## Problema observable

Las 16 fichas ya contienen profundidad jurídica, perímetro, entregables, responsabilidades, aceptación, límites y extensiones. Sin embargo, la lógica de compra sigue distribuida entre varias secciones: el cliente debe inferir cuál es la unidad comercial que se cotiza, cómo se dimensionan honorarios, qué variables cambian el alcance, qué ocurre si la necesidad crece y qué criterio determina el cierre.

v5.8 ya ofrece una lectura ejecutiva y v5.22 explica decisión/modalidad. Por tanto, la solución no puede ser otra sección larga ni una reescritura del catálogo.

## Contrato v5.30

1. Mantener `catalog-products-v41/` y `catalog-services-v42/` como verdad jurídica de las 16 ofertas.
2. Crear `offer-commercial-v530.json` como capa complementaria, con exactamente 16 entradas.
3. Cada oferta debe declarar `engagement_basis`, `fee_logic`, exactamente tres `drivers`, `change_rule` y `close_rule`.
4. Explicar honorarios por lógica de dimensionamiento, sin publicar importes, monedas, descuentos ni una tarifa universal inventada.
5. Materializar v5.30 dentro de `buying-clarity-v58`, después de sus metadatos y sin crear una nueva `<section>` narrativa.
6. Enlazar la síntesis con `#perimetro-title`, `#aceptacion-title` y `#contacto`.
7. Mantener los tres drivers bajo `<details>` para evitar densidad permanente.
8. No añadir JavaScript funcional ni cotizador automático.
9. Preservar un único formulario físico, WhatsApp manual y todos los límites semánticos v5.29.
10. Encadenar v5.30 después de v5.29 dentro de `apply_handoff_observability_v518.py`, conservando exactamente 30 pasos canónicos.
11. Añadir validator y E2E específicos y conservar todos los gates históricos sin relajación.

## Fuentes y archivos del ciclo

- `offer-commercial-v530.json`: lógica comercial complementaria de 16 ofertas.
- `offer-commercial-v530.css`: presentación compacta.
- `scripts/apply_offer_commercial_v530.py`: compositor final.
- `scripts/validate_offer_commercial_v530.py`: contrato estático.
- `tests/e2e/offer-commercial-v530.spec.mjs`: comportamiento real.
- `knowledge/30_RUNBOOKS/AUDIT-OFERTAS-v5.30.md`: auditoría de línea base.
- `knowledge/10_DECISIONES/ADR-004-commercial-depth-v530.md`: decisión arquitectónica.

## No objetivos

No publicar precios o tarifas no aprobadas; no crear cotizador, scoring, CRM, backend, pago, firma electrónica, agenda, autenticación, carga documental o portal; no duplicar perímetro/entregables/aceptación; no inventar clientes, resultados o garantías; no reinterpretar contacto/handoff como conversión.

## Cierre requerido

Composición v5.30 sobre las 16 fichas, validator propio, idempotencia, validadores históricos, Release Governance, Pages/smoke, Browser E2E/axe, Lighthouse, promoción de `stable` y Graphify alineado deben quedar verdes antes de declarar v5.30 cerrada.

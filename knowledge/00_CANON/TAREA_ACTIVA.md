# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**v5.30.0 — profundidad comercial de las 16 ofertas: cerrada funcionalmente.**

SHA funcional certificado:

`ee88b8ced3347255cf85ee62e3bf4022b7c34a42`.

No hay una release funcional posterior activa. El commit que contiene esta memoria debe atravesar el pipeline completo de cierre y quedar con `main = stable` antes de considerar terminada también la sincronización documental.

## Problema resuelto

Las 16 fichas ya contenían profundidad jurídica, perímetro, entregables, responsabilidades, aceptación, límites y extensiones. La brecha era la necesidad de inferir, entre varias secciones, cómo se contrata cada oferta, cómo se dimensionan honorarios, qué variables amplían el alcance y cómo se verifica el cierre.

v5.30 resolvió esa fricción dentro del resumen ejecutivo existente, sin añadir una sección narrativa redundante ni reescribir los catálogos fuente.

## Contrato implementado

1. `catalog-products-v41/` y `catalog-services-v42/` permanecen como verdad jurídica de las 16 ofertas.
2. `offer-commercial-v530.json` cubre exactamente las 16 ofertas.
3. Cada oferta declara `engagement_basis`, `fee_logic`, exactamente tres `drivers`, `change_rule` y `close_rule`.
4. Los honorarios se explican por lógica de dimensionamiento, sin publicar importes, monedas, descuentos ni una tarifa universal inventada.
5. v5.30 se materializa dentro de `buying-clarity-v58`, después de sus metadatos y sin crear una nueva `<section>` narrativa.
6. La síntesis enlaza a `#perimetro-title`, `#aceptacion-title` y `#contacto`.
7. Los tres drivers permanecen bajo `<details>` para evitar densidad permanente.
8. No se añadió JavaScript funcional ni cotizador automático.
9. Se preservaron un único formulario físico, WhatsApp manual y todos los límites semánticos v5.29.
10. v5.30 corre después de v5.29 dentro de `apply_handoff_observability_v518.py`, conservando exactamente 30 pasos canónicos.
11. Validator, E2E, axe, Lighthouse, Release Governance, idempotencia, Pages y promoción de `stable` quedaron obligatorios.

## Evidencia funcional

- PR #134 — integrada.
- Release Governance `31834565612` — PASS.
- Builder `31834618506` — PASS.
- Site Quality and Deploy `31834646140` — PASS.
- Idempotencia — PASS.
- 37/37 validaciones estáticas — PASS.
- Pages/smoke — PASS.
- Browser E2E/axe — **100 observados · 98 PASS · 2 SKIP · 0 FAIL · 0 reintentos**.
- Lighthouse — PASS.
- Promoción de `stable` — PASS.

## No objetivos preservados

No se publicaron precios o tarifas no aprobadas; no se creó cotizador, scoring, CRM, backend, pago, firma electrónica, agenda, autenticación, carga documental o portal; no se duplicaron perímetro/entregables/aceptación; no se inventaron clientes, resultados o garantías; no se reinterpretó contacto/handoff como conversión.

## Próximo ciclo

No abrir v5.31 por inercia. Antes de código debe definirse un problema observable, baseline, contrato, no objetivos y plan de verificación. No reabrir v5.30 salvo regresión real de las 16 fichas o de sus contratos.

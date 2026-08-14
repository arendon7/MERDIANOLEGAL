# Meridiano Legal — Release v5.30.0

Fecha de cierre funcional: 2026-08-14.

## Alcance

v5.30 mejora la profundidad comercial de las 16 ofertas sin reescribir su contenido jurídico ni introducir precios, cotizadores o capacidades inexistentes.

La auditoría de las 8 fichas de producto y 8 de servicio concluyó que el catálogo ya contenía suficiente profundidad en perímetro, método, entregables, formatos, cronograma, responsabilidades, aceptación, límites y suplementos. La fricción estaba en que la lógica de contratación debía reconstruirse entre varias secciones.

## Solución

Cada oferta incorpora dentro del resumen ejecutivo v5.8 una ficha compacta de contratación con cinco elementos:

1. **Unidad/base de contratación:** qué unidad concreta se dimensiona en la propuesta.
2. **Lógica de honorarios:** cómo se forma el alcance económico sin publicar una tarifa universal inventada.
3. **Tres drivers de dimensionamiento:** variables principales que pueden modificar alcance y honorarios.
4. **Regla de ampliación:** qué ocurre si la necesidad supera el perímetro inicial.
5. **Cierre verificable:** qué evidencia permite considerar ejecutado el alcance contratado.

Los drivers permanecen bajo un `<details>` nativo. La síntesis enlaza al perímetro exacto, a los criterios de aceptación y al contacto canónico.

## Arquitectura preservada

- `catalog-products-v41/` y `catalog-services-v42/` continúan siendo la verdad jurídica principal.
- `offer-commercial-v530.json` es complementario, no un catálogo paralelo.
- No se creó una nueva `<section>` narrativa.
- No se añadió JavaScript funcional.
- v5.30 se ejecuta al final de las extensiones del paso canónico `v5.18+`, después de v5.29.
- El pipeline conserva exactamente 30 pasos.

## Evidencia funcional certificada

- PR funcional: **#134**.
- Release Governance: `31834565612` — PASS.
- Builder canónico: `31834618506` — PASS.
- SHA funcional canónico: `ee88b8ced3347255cf85ee62e3bf4022b7c34a42`.
- Site Quality and Deploy #377: `31834646140` — PASS.
- Segunda pasada / idempotencia: PASS.
- Validaciones estáticas: 37/37 — PASS.
- Cobertura del contrato v5.30 sobre 16/16 ofertas: PASS.
- GitHub Pages: PASS.
- Smoke público: PASS.
- Browser E2E/axe: **100 observados · 98 PASS · 2 SKIP · 0 FAIL · 0 reintentos**.
- axe: PASS en las superficies cubiertas por la suite.
- Lighthouse performance/accesibilidad: PASS con budgets existentes.
- Promoción automática de `stable`: PASS.
- Budgets relajados: no.
- Cobertura reducida: no.

## Qué mejoró para el cliente

### Productos

Las fichas cerradas ahora explican con mayor claridad qué cubre el paquete estándar, qué factores lo pueden ampliar, cuándo procede un suplemento y cómo se verifica la entrega. La cantidad exacta de documentos, sociedades, entrevistas, casos, contratos, activos o permisos sigue proveniendo del catálogo fuente.

### Servicios

Las modalidades variables ahora explican qué unidad se compra —proyecto, negociación, portafolio, capacidad recurrente, casos de uso o flujos— y cuáles factores alteran el esfuerzo. Esto permite hablar de honorarios con transparencia sin fingir que todos los asuntos jurídicos admiten una tarifa fija idéntica.

## Invariantes preservadas

- 46 HTML.
- 16 fichas profundas.
- 1 formulario físico canónico.
- WhatsApp manual.
- Portal real deshabilitado.
- Demo explícitamente ficticia/noindex.
- 30 pasos canónicos.
- Sin clientes, testimonios o resultados inventados.
- Sin importes, monedas, descuentos o tarifas no aprobadas en v5.30.
- Sin cotizador o scoring automático.
- Sin PII, lectura de formulario o persistencia nueva.
- Sin CRM, backend, firma, pagos, agenda, autenticación o carga documental ficticios.
- Sin conversión inferida desde navegación, contacto o handoff.

## Cierre documental

El canal de release es `github-pages-production-offer-commercial-depth-certified`. Para evitar referencias recursivas, este documento conserva el SHA funcional certificado y no incrusta el SHA de su propio cierre. La referencia canónica definitiva debe verificarse en los refs vigentes: una release está cerrada documentalmente cuando el commit que contiene esta nota ha superado builder, idempotencia, Pages/smoke, Browser E2E/axe y Lighthouse, y `main = stable`.

# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **5.30.0 — profundidad comercial de las 16 ofertas**.
- SHA funcional certificado: `ee88b8ced3347255cf85ee62e3bf4022b7c34a42`.
- Site Quality and Deploy funcional: `31834646140` — PASS.
- Browser E2E/axe: **100 observados · 98 PASS · 2 SKIP · 0 FAIL · 0 reintentos**.
- Canal certificado: `github-pages-production-offer-commercial-depth-certified`.
- No hay un ciclo funcional posterior abierto.
- Para la referencia documental definitiva, verificar que los refs actuales `main` y `stable` coincidan; no incrustar un SHA recursivo de cierre en esta nota.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué cambió en v5.30

Las 16 ofertas mantienen su profundidad jurídica original y ahora hacen explícita, dentro del resumen ejecutivo v5.8, la lógica de contratación que antes debía inferirse entre varias secciones. Cada oferta declara:

- unidad/base de contratación;
- cómo se dimensionan los honorarios sin publicar tarifas inventadas;
- exactamente tres variables que pueden modificar alcance y honorarios;
- regla de ampliación o cambio de modalidad;
- criterio de cierre verificable.

La síntesis enlaza a perímetro, aceptación y contacto. Los catálogos fuente siguen siendo la verdad jurídica del alcance, entregables, responsabilidades, límites y cantidades.

## Source-of-truth

- `main`: verdad técnica y documental vigente.
- `stable`: snapshot certificado; debe coincidir con `main` al cierre de una release.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad.
- `offer-commercial-v530.json`: contrato complementario de lógica de contratación; nunca sustituye perímetro o aceptación de los catálogos.
- `professional-authority-v525.json`: hechos profesionales publicables.
- `visual-assets-v526.json`: verdad de activos visuales.
- `funnel-contract-v529.json`: límites semánticos y de privacidad del funnel.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar importes, monedas, descuentos o tarifas no aprobadas;
- no cotizador automático ni scoring de honorarios;
- no PII ni lectura del contenido del formulario;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- no equiparar exposición/contacto/handoff con conversión comercial;
- conservar exactamente 30 pasos canónicos;
- `stable` solo después de gates verdes.

## Graphify

Graphify es memoria derivada y no sustituye a `main`. Solo usar `knowledge/graphify-live` como autoridad auxiliar cuando `graphify-out/BUILD_META.json.source_commit` coincida con el `main` vigente.

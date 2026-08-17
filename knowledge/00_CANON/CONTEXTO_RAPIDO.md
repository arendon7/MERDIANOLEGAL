# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **5.31.0 — compresión decisional mediante divulgación progresiva**.
- SHA funcional certificado: `159be8a9e467a303faa8d302bfac93b33c2e7b29`.
- Builder canónico funcional: `32059316508` — PASS.
- Site Quality and Deploy #383: `32059355395` — PASS.
- Browser E2E/axe: **112 observados · 110 PASS · 2 SKIP · 0 FAIL · 0 reintentos**.
- Lighthouse: PASS con budgets existentes.
- Canal: `github-pages-production-decision-compression-certified`.
- No hay un ciclo funcional posterior abierto.
- Para la referencia documental definitiva, verificar los refs vigentes `main` y `stable`; no incrustar un SHA recursivo de cierre en esta nota.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué cambió en v5.31

La auditoría del recorrido público confirmó que la web ya tenía suficiente profundidad jurídica y comercial. La fricción era de jerarquía: demasiadas capas decisionales válidas permanecían abiertas simultáneamente.

- En 16/16 fichas, v5.8 + v5.30 permanecen como primer grupo abierto y pregunta ejecutiva + resultado como segundo grupo compacto.
- `offer-narrative-v522` se conserva íntegro en el DOM bajo `<details>/<summary>` nativo cerrado por defecto.
- En 6/6 rutas de necesidad permanecen abiertos hero, señales, encaje, decisiones, modalidad, honorarios, resultado, límites y CTA.
- Solo objeciones, FAQ, rutas relacionadas y prueba/contexto pasan a divulgación progresiva.
- No se eliminó copy, perímetro, límites, alternativas, evidencia ni honorarios aprobados.

## Source-of-truth

- `main`: verdad técnica y documental vigente.
- `stable`: snapshot certificado; debe coincidir con `main` al cierre de una release.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad.
- `offer-commercial-v530.json`: lógica de contratación complementaria.
- `decision-compression-v531.json`: contrato de jerarquía/divulgación progresiva.
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

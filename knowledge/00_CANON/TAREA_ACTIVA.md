# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.4.0 — Commercial Evidence Readiness / production-certified closure.**

Rama: `docs/v740-certified-closure`.

La funcionalidad y el candidate ya fueron certificados productivamente.

## Evidencia cerrada

### Funcional #180

- Baseline anterior certificado: v7.3.0 `61790b4bdf0bfe4dd1143a414288559d664826e6`.
- SHA funcional final: `fcd929a63f0cdede944cf1767ec03346711e6ee8`.
- 12/12 workflows aplicables same-SHA: PASS.
- Merge funcional #180: `d781b3296b325d3d4cd6974523b01c27d77ebaf2`.

### Candidate #181

- SHA candidate final: `b30d92c923f3f982190dfba3ce31b353cb170f97`.
- 10/10 workflows aplicables same-SHA: PASS.
- Merge candidate #181: `8a898dd3e791bb4b216815156643396a6f5e7c93`.
- Builder/snapshot candidate: `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- Pages quality/deploy/live smoke + Browser E2E/axe + Lighthouse: PASS.
- `stable` fue promovido automáticamente a `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- Antes de este cierre: `main == stable == 8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- `stable/version.json`: v7.4.0 / `github-pages-commercial-evidence-readiness-candidate`.

## Qué contiene v7.4

Commercial Evidence Readiness prepara atribución comercial local y anónima para Legal AI Transformation, Contract Control, AI Governance 360, Regulatory Control y Meridiano Legal Desk.

Solo admite `offer_view`, `demo_offer_open`, `contact_intent` y `handoff_prepared`, asociados mediante tokens públicos allowlisted `source=li-*`.

## Lifecycle y activation boundary

El cierre cambia el lifecycle del contrato de `release-candidate` a `certified`, pero **no cambia el estado operativo**: v7.4 permanece `readiness-disabled`.

- `site-config.json` continúa con analytics disabled, provider `none`, site_id vacío.
- No se activa Plausible, GA4, Umami ni otro proveedor.
- No hay transporte analytics externo propio, cookies, storage persistente, fingerprinting o identificadores cross-session.
- No se exporta PII, texto libre o contenido del formulario.
- El buffer local permanece limitado a 24 eventos en memoria.
- El payload local sigue limitado a `subject + interaction`.

Una futura activación externa requiere otro frente/release, proveedor/site ID reales, revisión de metadata del proveedor y actualización previa de privacidad.

## Boundary del cierre

El cierre `production-certified` modifica exactamente siete archivos:

1. `version.json`: candidate → `github-pages-production-commercial-evidence-readiness-certified`.
2. `assets/data/v7/commercial-evidence-v74.json`: lifecycle `release-candidate` → `certified`, manteniendo `status: readiness-disabled`.
3. `README.md`.
4. `RELEASE-v7.4.md`.
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`.
7. esta memoria.

No modifica runtime JS, HTML, navegación, formularios, CSS, catálogos, precios, capabilities, `site-config.json`, política de privacidad, materializadores, validators funcionales, E2E ni workflows.

## Gate del cierre

Antes de declarar v7.4 definitivamente cerrada:

1. confirmar boundary exacto de siete archivos;
2. congelar un único SHA final;
3. superar todos los workflows aplicables sobre ese mismo SHA;
4. confirmar V7.4 PASS con lifecycle `certified` y status `readiness-disabled`;
5. mantener Measurement y Browser E2E/axe PASS;
6. fusionar únicamente con `expected_head_sha`;
7. completar Builder → Pages → live smoke → Browser/axe + Lighthouse;
8. permitir únicamente promoción automática de `stable`;
9. terminar con `main == stable`;
10. confirmar `stable/version.json` = v7.4.0 + `github-pages-production-commercial-evidence-readiness-certified`.

`stable` no se mueve manualmente.

## Después de v7.4

Cualquier activación real de analítica será una decisión separada. El próximo frente comercial debe mejorar comprensión, autoridad, descubrimiento y conversión de las ofertas existentes antes de crear nuevas capabilities tecnológicas.

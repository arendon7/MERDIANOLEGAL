# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.4.0 — Commercial Evidence Readiness / release candidate.**

Rama: `release/v740-commercial-evidence-readiness-candidate`.

Baseline estable: **v7.3.0 — Legal Intelligence Demo production-certified**, `stable == 61790b4bdf0bfe4dd1143a414288559d664826e6`.

## Evidencia funcional ya cerrada

La fase funcional v7.4 fue certificada antes de este candidate:

- SHA funcional final: `fcd929a63f0cdede944cf1767ec03346711e6ee8`.
- **12/12 workflows aplicables same-SHA: PASS**.
- Incluidos: V7.4 Commercial Evidence, V7.3 Legal Intelligence Demo, V7.2 Buying Clarity, V6 Candidate Validation, Canonical Builder Equivalence, Engagement Clarity, Fit & Scope, Search Discovery, Measurement, Browser/axe, Release Governance y Graphify.
- PR funcional #180 fusionado.
- Merge funcional: `d781b3296b325d3d4cd6974523b01c27d77ebaf2`.

`stable` no se movió con el merge funcional y continúa representando la release certificada v7.3 hasta que exista un candidate formal v7.4 publicado y validado.

## Qué contiene v7.4

Commercial Evidence Readiness prepara atribución comercial local y anónima para cinco sujetos públicos de Meridiano Legal Intelligence:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Solo admite cuatro interacciones:

- `offer_view`;
- `demo_offer_open`;
- `contact_intent`;
- `handoff_prepared`.

La atribución usa únicamente tokens públicos allowlisted `source=li-*`. Cualquier source libre o manipulado se ignora.

## Separación lifecycle / estado operativo

En v7.4 el lifecycle de release y el estado de analítica son conceptos distintos.

- `prototype`: contrato `7.4.0-prototype*` sobre release pública v7.3 certificada.
- `release-candidate`: contrato y runtime `7.4.0`, versión pública `7.4.0`, canal `github-pages-commercial-evidence-readiness-candidate`.
- `certified`: contrato `7.4.0`, versión pública `7.4.0`, canal `github-pages-production-commercial-evidence-readiness-certified`.

En las tres fases el estado operativo permanece **`readiness-disabled`**.

Esto significa que promover v7.4 a candidate o certified **no activa analítica externa**.

## Privacidad y límites preservados

- `site-config.json`: analytics `enabled=false`, provider `none`, site_id vacío.
- Measurement v6.1 permanece `readiness-disabled` / production-disabled.
- Cero requests propios a Plausible, GA4, Umami u otro proveedor.
- Cero cookies, `localStorage`, `sessionStorage`, IndexedDB o identificadores cross-session.
- Cero fingerprinting.
- Cero PII, contenido de formulario o texto libre en eventos.
- Buffer máximo de 24 eventos, solo en memoria de la pestaña.
- Payload local limitado a `subject + interaction`.
- `contact_intent` no significa mensaje enviado.
- `handoff_prepared` no significa envío, entrega, lectura, aceptación, contratación ni cliente.

Una futura activación externa requiere otra decisión/release, proveedor real, site ID real, revisión de metadata del proveedor y actualización previa de la política de privacidad.

## Boundary del candidate formal

El candidate modifica únicamente seis fuentes de lifecycle/release:

1. `version.json` — 7.3.0 certified → 7.4.0 candidate.
2. `assets/data/v7/commercial-evidence-v74.json` — añade lifecycle `release-candidate` y fija versión 7.4.0, manteniendo status `readiness-disabled`.
3. `assets/js/v7/commercial-evidence-v74.js` — metadata runtime prototype → 7.4.0; comportamiento y límites permanecen iguales.
4. `scripts/apply_commercial_evidence_v74.py` — máquina de estados lifecycle fail-closed.
5. `scripts/validate_commercial_evidence_v74.py` — valida lifecycle + versión/canal + readiness-disabled.
6. esta memoria.

No modifica HTML, navegación, formularios, catálogos, precios, capabilities, `site-config.json`, privacidad, E2E ni workflows.

## Gate del candidate

Antes de fusionar:

1. confirmar boundary exacto del PR;
2. congelar un único SHA final;
3. exigir todos los workflows aplicables verdes sobre ese mismo SHA;
4. preservar `apply_commercial_evidence_v74.py --check` idempotente;
5. mantener v6.1 Measurement PASS con analytics externos deshabilitados;
6. mantener Browser E2E/axe PASS;
7. fusionar únicamente con `expected_head_sha`.

Después del merge candidate:

1. Builder canónico;
2. Pages quality/deploy;
3. live smoke;
4. Browser E2E desplegado;
5. Lighthouse;
6. promoción automática de `stable`;
7. confirmar `main == stable` y `stable/version.json` = 7.4.0 candidate.

Solo después se abrirá un cierre documental separado `candidate → production-certified`. `stable` no se mueve manualmente.

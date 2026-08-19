# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.4 — Commercial Evidence Readiness / prototype.**

Rama: `feat/v740-commercial-evidence-readiness`.

Baseline certificada: **v7.3.0 — Legal Intelligence Demo**, con `main == stable == 61790b4bdf0bfe4dd1143a414288559d664826e6` y canal `github-pages-production-legal-intelligence-demo-certified`.

## Problema que resuelve

v7.0–v7.3 hicieron más clara, comprable y demostrable la capa Meridiano Legal Intelligence, pero Measurement v6.1 solo exportaría etapas agregadas del funnel y deliberadamente descarta `target/event`. Hoy no existe una atribución comercial cerrada para saber qué capacidad Legal Intelligence originó una intención de contacto.

## Hipótesis v7.4

Preparar una capa local y anónima que permita atribuir interacciones a cinco sujetos comerciales sin activar analytics externo ni crear perfiles:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Cada sujeto usa un token público allowlisted `source=li-*`. Cualquier source diferente se ignora.

## Interacciones admitidas

- `offer_view`.
- `demo_offer_open`.
- `contact_intent`.
- `handoff_prepared`.

Ninguna interacción equivale a usuario único, mensaje enviado, entrega, lectura, aceptación, contratación o cliente.

## Boundary funcional

Commercial Evidence v7.4 se carga únicamente en siete superficies:

1. `index.html`.
2. `experiencia.html`.
3. `servicios/legal-operations.html`.
4. `productos/sistema-contractual-empresarial.html`.
5. `productos/programa-gobernanza-ia.html`.
6. `productos/proyecto-regulado-estructurado.html`.
7. `soluciones/ordenar-operacion-juridica.html`.

No cambia navegación, formulario, campos, anchors, catálogos, precios o capabilities.

## Privacidad / capability truth

El prototype permanece `readiness-disabled`:

- analytics externo deshabilitado;
- provider `none`;
- cero network transport propio;
- cero cookies;
- cero local/session storage;
- cero identificadores cross-session;
- cero fingerprinting;
- cero PII;
- cero contenido de formulario o texto libre en eventos;
- buffer máximo de 24 eventos, solo en memoria de la pestaña;
- payload local limitado a `subject + interaction`;
- `site-config.json` y Measurement v6.1 siguen production-disabled.

El `source` permanece visible en URL y el handoff histórico continúa mostrando `pathname+search` en el campo `Origen` del mensaje que el usuario revisa antes de enviar por WhatsApp.

## Estado de materialización

Las siete superficies fueron materializadas desde `scripts/apply_commercial_evidence_v74.py` y Graphify fue restaurado byte-for-byte desde `main` antes del commit generado.

El boundary permanente del PR #180 es de **16 archivos**:

- 9 archivos de source/QA/gobernanza (incluida esta memoria y el hook del normalizador);
- 7 superficies HTML materializadas;
- ningún workflow temporal adicional.

La primera ejecución de Graphify que produjo el commit termina con freshness obsoleta por diseño, porque su propio push mueve el head durante el job. Esa ejecución no cuenta como certificación; la ronda válida debe ejecutarse sobre un SHA posterior normal, sin modificación de workflows.

## Archivos source-driven

- `assets/data/v7/commercial-evidence-v74.json`.
- `assets/js/v7/commercial-evidence-v74.js`.
- `knowledge/20_DESIGN/COMMERCIAL-EVIDENCE-v74.md`.
- `scripts/apply_commercial_evidence_v74.py`.
- `scripts/validate_commercial_evidence_v74.py`.
- `scripts/normalize_experience_compat_v60.py`.
- `tests/e2e/commercial-evidence-v74.spec.mjs`.
- `.github/workflows/v74-commercial-evidence-readiness.yml`.
- siete superficies HTML materializadas.
- esta memoria de tarea.

## Gate del prototype

Antes de considerar la fase funcional lista:

1. materializar exactamente las siete superficies;
2. confirmar idempotencia `apply --check`;
3. mantener Measurement v6.1 PASS y analytics production-disabled;
4. E2E debe probar propagación allowlisted de source, eventos locales, source inválido ignorado y ausencia de requests a proveedores analytics;
5. superar Builder/Candidate, Engagement, Fit & Scope, Buying Clarity, Legal Intelligence Demo, Search, Release Governance, Graphify, Browser/axe y Measurement;
6. congelar un único SHA same-SHA antes de cualquier merge.

## No objetivos

- No activar Plausible, GA4, Umami u otro proveedor.
- No introducir pageviews automáticos.
- No identificar usuarios.
- No afirmar conversiones que la web estática no conoce.
- No cambiar el copy comercial por el solo hecho de instrumentarlo.

Una eventual activación externa será otra decisión y otra release, con proveedor, site ID, política de privacidad, retención y semántica aprobados expresamente.

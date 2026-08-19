# Release v7.4.0 — Commercial Evidence Readiness

Fecha: 2026-08-19.

## Objetivo

Preparar una capa de atribución comercial anónima y verificable para Meridiano Legal Intelligence que permita distinguir qué recorridos públicos generan señales de interés, sin activar analítica externa, cookies, almacenamiento persistente, perfiles de usuario o captura de información jurídica/personales.

v7.4 separa deliberadamente dos conceptos:

- **lifecycle de release**: `prototype → release-candidate → certified`;
- **estado operativo de analítica**: permanece `readiness-disabled` en toda v7.4.

Por tanto, certificar v7.4 no equivale a habilitar Plausible, GA4, Umami u otro proveedor.

## Alcance funcional

La capa cubre cinco sujetos públicos de Legal Intelligence:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Y únicamente cuatro interacciones allowlisted:

- `offer_view`;
- `demo_offer_open`;
- `contact_intent`;
- `handoff_prepared`.

La atribución usa tokens públicos `source=li-*`. Los valores fuera del allowlist se ignoran.

## Semántica de evidencia

Los eventos de v7.4 son señales operativas limitadas:

- `offer_view` no representa una persona única;
- `contact_intent` no demuestra que un mensaje haya sido enviado;
- `handoff_prepared` no demuestra envío, entrega, lectura, aceptación, contratación o conversión a cliente.

El runtime conserva como máximo 24 eventos en memoria de la pestaña y cada evento contiene exclusivamente `subject + interaction`.

## Privacidad y activation boundary

v7.4 certificada mantiene:

- `site-config.json`: `analytics.enabled=false`, provider `none`, site_id vacío;
- Measurement v6.1: `readiness-disabled` / production-disabled;
- cero requests propios a proveedores de analítica;
- cero cookies;
- cero `localStorage`, `sessionStorage` o IndexedDB;
- cero identificadores cross-session;
- cero fingerprinting;
- cero PII;
- cero contenido de formulario;
- cero texto libre en eventos;
- cero URL completa exportada como propiedad;
- cero propiedades custom exportables.

Una futura activación de analítica requiere una decisión/release separada, proveedor y site ID reales, revisión de metadata estándar del proveedor y actualización previa de la política pública de privacidad.

## Fuente de verdad

La implementación está gobernada por:

- `assets/data/v7/commercial-evidence-v74.json`;
- `assets/js/v7/commercial-evidence-v74.js`;
- `scripts/apply_commercial_evidence_v74.py`;
- `scripts/validate_commercial_evidence_v74.py`;
- `tests/e2e/commercial-evidence-v74.spec.mjs`;
- `.github/workflows/v74-commercial-evidence-readiness.yml`;
- integración canónica desde `scripts/normalize_experience_compat_v60.py`.

Las siete superficies públicas instrumentadas son:

1. `index.html`;
2. `experiencia.html`;
3. `servicios/legal-operations.html`;
4. `productos/sistema-contractual-empresarial.html`;
5. `productos/programa-gobernanza-ia.html`;
6. `productos/proyecto-regulado-estructurado.html`;
7. `soluciones/ordenar-operacion-juridica.html`.

## Evidencia funcional

### Fase funcional #180

- Baseline estable: v7.3.0 production-certified `61790b4bdf0bfe4dd1143a414288559d664826e6`.
- SHA funcional final: `fcd929a63f0cdede944cf1767ec03346711e6ee8`.
- 12/12 workflows aplicables same-SHA: PASS.
- Incluidos v7.4, v7.3, v7.2, Candidate Validation, Canonical Builder, Engagement, Fit & Scope, Search, Measurement, Browser/axe, Release Governance y Graphify.
- PR funcional #180 fusionado.
- Merge funcional: `d781b3296b325d3d4cd6974523b01c27d77ebaf2`.

## Candidate formal #181

- SHA candidate final: `b30d92c923f3f982190dfba3ce31b353cb170f97`.
- Boundary: seis archivos de lifecycle/release, sin cambios funcionales nuevos.
- 10/10 workflows aplicables same-SHA: PASS.
- V7.4 Commercial Evidence Readiness: PASS.
- Browser E2E/axe: PASS.
- Measurement/Browser: PASS.
- Candidate Validation, Builder, Fit & Scope, Engagement, Search, Governance y Graphify: PASS.
- Merge candidate #181: `8a898dd3e791bb4b216815156643396a6f5e7c93`.
- Builder canónico: `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- Pages quality → deploy → live smoke → Browser E2E desplegado → Lighthouse → snapshot: PASS, acreditado por la promoción automática de `stable`.
- Antes de este cierre: `main == stable == 8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- `stable/version.json`: v7.4.0 / `github-pages-commercial-evidence-readiness-candidate`.

## Arquitectura y capability truth preservados

v7.4 no crea una nueva oferta, producto, servicio o capability jurídica. Preserva:

- 8 productos + 8 servicios canónicos;
- seis rutas públicas;
- Meridiano Legal como marca madre;
- Meridiano Legal Intelligence como capa transversal;
- v7.3 Legal Intelligence Demo;
- v7.2 Buying Clarity;
- v7.1 Commercial Clarity;
- v7.0 Legal Intelligence;
- v6.4 Fit & Scope Clarity;
- v6.3 Engagement Clarity;
- v6.2 Search Discovery;
- v6.1 Measurement privacy-first;
- v6.0 Experience System.

Contract Control y Regulatory Control continúan sin presentarse como SaaS autónomos; Legal Desk sigue sujeto a propuesta y capacidad pactada; AI Governance 360 no sustituye seguridad/auditoría técnica; Legal Engineering solo incorpora tecnología expresamente pactada; Meridiano Counsel permanece fuera de la oferta pública.

## Cierre production-certified

El cierre final modifica únicamente siete fuentes de metadata/documentación:

1. `version.json` → `github-pages-production-commercial-evidence-readiness-certified`;
2. `assets/data/v7/commercial-evidence-v74.json` → lifecycle `certified`, manteniendo `status: readiness-disabled`;
3. `README.md`;
4. este `RELEASE-v7.4.md`;
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`;
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`;
7. `knowledge/00_CANON/TAREA_ACTIVA.md`.

No modifica runtime JS, HTML, formularios, catálogos, precios, `site-config.json`, privacidad, materializadores, validators funcionales, E2E, workflows ni capabilities.

La release queda definitivamente cerrada cuando este propio PR supere sus gates same-SHA, se fusione con SHA protegido y complete otra vez Builder → Pages → live smoke → Browser/axe + Lighthouse → snapshot, terminando con `main == stable` y el canal production-certified.

## Siguiente frente

Después de v7.4 no debe activarse analítica por intuición. La activación externa requiere una decisión específica sobre proveedor, política de privacidad y gobernanza de datos. En paralelo, la siguiente mejora comercial del sitio debe concentrarse en hacer más visible y persuasivo el valor de las 16 ofertas y de Legal Intelligence, no en ampliar capacidades ficticias.

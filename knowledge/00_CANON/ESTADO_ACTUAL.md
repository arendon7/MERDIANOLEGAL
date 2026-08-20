# Meridiano Legal — Estado canónico

Última verificación funcional: 2026-08-19.

## Estado

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado/publicado: `stable`.
- Release: **v7.4.0 — Commercial Evidence Readiness**.
- Estado operativo de analítica: **`readiness-disabled`**.
- Canal objetivo de cierre: `github-pages-production-commercial-evidence-readiness-certified`.
- 8 productos + 8 servicios canónicos continúan gobernando alcance, entregables, tiempos, responsabilidades y límites.

## Resultado v7.4

Commercial Evidence Readiness prepara atribución comercial local y anónima para cinco sujetos públicos de Meridiano Legal Intelligence:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Solo admite cuatro interacciones allowlisted:

- `offer_view`;
- `demo_offer_open`;
- `contact_intent`;
- `handoff_prepared`.

La atribución utiliza exclusivamente tokens públicos `source=li-*`. Valores libres o alterados fuera del allowlist se ignoran.

## Evidencia

### Fase funcional #180

- Baseline certificado v7.3.0: `61790b4bdf0bfe4dd1143a414288559d664826e6`.
- SHA funcional: `fcd929a63f0cdede944cf1767ec03346711e6ee8`.
- 12/12 workflows aplicables same-SHA: PASS.
- Merge #180: `d781b3296b325d3d4cd6974523b01c27d77ebaf2`.

### Candidate #181

- SHA candidate final: `b30d92c923f3f982190dfba3ce31b353cb170f97`.
- 10/10 workflows aplicables same-SHA: PASS.
- Merge #181: `8a898dd3e791bb4b216815156643396a6f5e7c93`.
- Builder canónico: `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- Pages quality/deploy/live smoke: PASS.
- Browser E2E/axe desplegado: PASS.
- Lighthouse: PASS.
- Snapshot automático: `stable → 8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- Antes del cierre documental: `main == stable == 8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- `stable/version.json`: v7.4.0 / `github-pages-commercial-evidence-readiness-candidate` antes de este cierre.

## Separación lifecycle / estado operativo

El lifecycle de release y la activación de analítica son independientes:

- prototype;
- release-candidate;
- certified.

En las tres fases v7.4 mantiene `status: readiness-disabled`.

La promoción a production-certified no habilita proveedor, transporte, cookies, storage, perfiles o medición externa.

## Privacidad y semántica

- `site-config.json`: analytics `enabled=false`, provider `none`, site_id vacío;
- Measurement v6.1 continúa production-disabled;
- cero transporte analytics externo propio;
- cero cookies, `localStorage`, `sessionStorage`, IndexedDB o identificadores cross-session;
- cero fingerprinting;
- cero PII, texto libre o contenido de formulario en eventos;
- máximo 24 eventos efímeros en memoria;
- payload local limitado a `subject + interaction`;
- `offer_view` no significa usuario único;
- `contact_intent` no significa mensaje enviado;
- `handoff_prepared` no significa envío, entrega, lectura, aceptación, contratación o conversión a cliente.

## Arquitectura preservada

Meridiano Legal sigue siendo marca madre. Meridiano Legal Intelligence continúa como capa transversal:

- Legal AI Diagnostic;
- Legal AI Transformation;
- Meridiano Legal Desk;
- Contract Control;
- Regulatory Control;
- AI Governance 360;
- Legal Engineering Studio.

Meridiano Counsel continúa como concepto futuro/no producto público.

## Capability truth

- Contract Control y Regulatory Control no son SaaS autónomos;
- no CLM productivo implícito;
- Legal Desk está sujeto a propuesta, perímetro, capacidad, canales y SLA pactados;
- AI Governance 360 no sustituye evaluación técnica, seguridad o auditoría;
- Legal Engineering solo incorpora tecnología expresamente pactada;
- no existe monitoreo automático universal ni decisión jurídica autónoma;
- portal real, auth, CRM, pagos, firma, agenda y upload siguen fuera de capability productiva;
- no tarifas nuevas.

## Compatibilidad

- v7.3 Legal Intelligence Demo preservada.
- v7.2 Buying Clarity preservada.
- v7.1 Commercial Clarity preservada.
- v7.0 Legal Intelligence preservada.
- v6.4 Fit & Scope y v6.3 Engagement preservadas.
- v6.2 Search, v6.1 Measurement y v6.0 Experience preservadas.
- Canonical Builder mantiene materialización e idempotencia.

## Cierre documental v7.4

La rama `docs/v740-certified-closure` modifica exactamente siete fuentes de metadata/documentación:

1. `version.json`.
2. `assets/data/v7/commercial-evidence-v74.json`.
3. `README.md`.
4. `RELEASE-v7.4.md`.
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`.
7. `knowledge/00_CANON/TAREA_ACTIVA.md`.

No modifica runtime JS, HTML, formularios, CSS, catálogos, `site-config.json`, privacidad, materializadores, validators funcionales, E2E, workflows ni capabilities.

La certificación queda definitiva cuando este cierre supere sus propios gates same-SHA, se fusione con SHA protegido y complete nuevamente Builder → Pages → live smoke → Browser/axe + Lighthouse → snapshot, terminando con `main == stable` y `stable/version.json` en canal `github-pages-production-commercial-evidence-readiness-certified`.

## Siguiente frente

Después del cierre definitivo, separar cualquier eventual activación de analítica en una release específica. El siguiente trabajo comercial debe priorizar comprensión, autoridad y conversión de la oferta existente con evidencia verificable, sin ampliar capabilities por intuición.

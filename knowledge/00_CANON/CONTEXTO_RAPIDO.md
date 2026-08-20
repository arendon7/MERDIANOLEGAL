# Meridiano Legal — Contexto rápido

Actualizado: 2026-08-19.

Use esta nota para orientarse antes de abrir fuentes. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan ante cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal, static-first sobre GitHub Pages.

Arquitectura pública preservada:

- 46 superficies HTML;
- 16 fichas profundas: 8 productos + 8 servicios;
- seis rutas públicas de solución;
- un único formulario físico canónico;
- Meridiano Legal como marca madre;
- Meridiano Legal Intelligence como capa transversal, no catálogo paralelo.

## Release vigente

**v7.4.0 — Commercial Evidence Readiness**.

Estado antes del cierre documental production-certified:

- baseline certificado anterior v7.3.0: `61790b4bdf0bfe4dd1143a414288559d664826e6`;
- SHA funcional v7.4: `fcd929a63f0cdede944cf1767ec03346711e6ee8` — 12/12 workflows aplicables PASS;
- merge funcional #180: `d781b3296b325d3d4cd6974523b01c27d77ebaf2`;
- SHA candidate formal: `b30d92c923f3f982190dfba3ce31b353cb170f97` — 10/10 workflows aplicables PASS;
- merge candidate #181: `8a898dd3e791bb4b216815156643396a6f5e7c93`;
- Builder/snapshot candidate: `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`;
- Pages quality → deploy → live smoke → Browser E2E/axe + Lighthouse → snapshot: PASS;
- `main == stable == 8f3596a0a23ec264c0fd4c4cdbf701311403f17a` antes de este cierre;
- canal candidate estable: `github-pages-commercial-evidence-readiness-candidate`;
- canal objetivo de cierre: `github-pages-production-commercial-evidence-readiness-certified`.

## Qué añade v7.4

Commercial Evidence Readiness prepara atribución comercial local, anónima y allowlisted para cinco sujetos de Meridiano Legal Intelligence:

1. Legal AI Transformation.
2. Contract Control.
3. AI Governance 360.
4. Regulatory Control.
5. Meridiano Legal Desk.

Solo reconoce cuatro interacciones:

- `offer_view`;
- `demo_offer_open`;
- `contact_intent`;
- `handoff_prepared`.

La atribución utiliza únicamente tokens públicos `source=li-*`; cualquier valor libre o manipulado fuera del allowlist se ignora.

## Release certificada no significa analytics activado

El lifecycle de v7.4 y el estado operativo son independientes. En prototype, candidate y certified, el estado operativo permanece **`readiness-disabled`**.

Por tanto:

- `site-config.json`: analytics deshabilitado, provider `none`, site_id vacío;
- no hay requests propios a Plausible, GA4, Umami u otro proveedor;
- no hay cookies ni almacenamiento persistente;
- no hay identificadores cross-session ni fingerprinting;
- no se exporta PII, texto libre o contenido de formulario;
- el buffer local está limitado a 24 eventos en memoria de la pestaña;
- el payload local se limita a `subject + interaction`.

Una futura activación requiere una decisión/release separada, proveedor y site ID reales, revisión de metadata del proveedor y actualización previa de privacidad.

## Semántica

- `offer_view` no equivale a persona única;
- `contact_intent` no equivale a mensaje enviado;
- `handoff_prepared` no equivale a envío, entrega, lectura, aceptación, contratación o cliente.

## Capas preservadas

- v7.3 Legal Intelligence Demo.
- v7.2 Buying Clarity.
- v7.1 Commercial Clarity.
- v7.0 Legal Intelligence.
- v6.4 Fit & Scope Clarity.
- v6.3 Engagement Clarity.
- v6.2 Search Discovery.
- v6.1 Measurement privacy-first.
- v6.0 Experience System.

## Capability truth

- 8 productos + 8 servicios canónicos continúan gobernando alcance, entregables y límites;
- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk sigue como managed legal service bajo propuesta y capacidad pactadas;
- AI Governance 360 no reemplaza seguridad, auditoría técnica o evaluación científica;
- Legal Engineering incorpora tecnología solo cuando se pacta expresamente;
- Meridiano Counsel continúa como futuro/no oferta pública;
- portal/auth/CRM/pagos/firma/agenda/upload no son capabilities productivas por efecto de v7.4;
- no existe monitoreo automático universal ni decisión jurídica autónoma;
- no hay tarifas nuevas sin pricing truth aprobado.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado/publicado.
- catálogos v4.1/v4.2: verdad jurídica/comercial.
- `assets/data/v7/`: contratos de capas v7.
- `knowledge/00_CANON/`: memoria operativa.

## Frente siguiente

Después del cierre production-certified de v7.4, cualquier activación externa de analítica debe ser un frente separado. Comercialmente, priorizar claridad, autoridad y conversión de las ofertas existentes antes de ampliar capabilities por intuición.

## Invariantes

No inventar clientes, testimonios, resultados, precios, capacidades tecnológicas o certificaciones; no reducir E2E/axe ni relajar Lighthouse; conservar seis rutas, un formulario canónico y `stable` únicamente después de gates productivos verdes.

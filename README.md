# Meridiano Legal · Web canónica v7.4.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v7.4.0 — Commercial Evidence Readiness** sobre la arquitectura de Meridiano Legal Intelligence.

La release prepara atribución comercial anónima y verificable para cinco recorridos de Legal Intelligence sin activar analítica externa ni modificar la verdad jurídica de los catálogos.

### Evidencia de release

- Baseline certificado anterior v7.3.0: `61790b4bdf0bfe4dd1143a414288559d664826e6`.
- SHA funcional v7.4: `fcd929a63f0cdede944cf1767ec03346711e6ee8` — 12/12 workflows aplicables verdes.
- Merge funcional #180: `d781b3296b325d3d4cd6974523b01c27d77ebaf2`.
- Candidate formal 7.4.0: `b30d92c923f3f982190dfba3ce31b353cb170f97` — 10/10 workflows aplicables verdes.
- Merge candidate #181: `8a898dd3e791bb4b216815156643396a6f5e7c93`.
- Builder/snapshot productivo candidate: `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`.
- Pages quality → deploy → live smoke → Browser E2E/axe + Lighthouse → snapshot: PASS.
- `stable` fue promovido automáticamente a `8f3596a0a23ec264c0fd4c4cdbf701311403f17a`; no se movió manualmente.
- Canal de cierre: `github-pages-production-commercial-evidence-readiness-certified`.

## Qué añade Commercial Evidence Readiness

v7.4 instrumenta de forma local y efímera cinco sujetos públicos de Meridiano Legal Intelligence:

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

La atribución usa exclusivamente tokens públicos allowlisted `source=li-*`. Valores libres o manipulados se ignoran.

## Release certificada ≠ analytics activado

El lifecycle de v7.4 y el estado operativo de analítica son independientes.

La release está certificada, pero la analítica externa permanece **`readiness-disabled`**:

- `analytics.enabled=false`;
- provider `none`;
- site_id vacío;
- cero requests propios a Plausible, GA4, Umami u otro proveedor;
- cero cookies o almacenamiento persistente;
- cero fingerprinting o identificadores cross-session;
- cero PII, texto libre o contenido de formulario en eventos;
- máximo 24 eventos en memoria de la pestaña;
- payload local limitado a `subject + interaction`.

Una futura activación requerirá una release separada, proveedor/site ID reales y revisión previa de privacidad y metadata del proveedor.

## Semántica de las señales

- `offer_view` no equivale a visitante único.
- `contact_intent` no equivale a mensaje enviado.
- `handoff_prepared` no equivale a envío, entrega, lectura, aceptación, contratación o conversión a cliente.

La capa sirve para preparar evidencia comercial; no fabrica métricas de negocio que todavía no existen.

## Arquitectura preservada

Meridiano Legal permanece como marca madre y **Meridiano Legal Intelligence** como capa transversal:

- Legal AI Diagnostic;
- Legal AI Transformation;
- Meridiano Legal Desk;
- Contract Control;
- Regulatory Control;
- AI Governance 360;
- Legal Engineering Studio.

v7.4 preserva además:

- v7.3 Legal Intelligence Demo;
- v7.2 Buying Clarity;
- v7.1 Commercial Clarity;
- v7.0 Legal Intelligence;
- v6.4 Fit & Scope Clarity;
- v6.3 Engagement Clarity;
- v6.2 Search Discovery;
- v6.1 Measurement privacy-first;
- v6.0 Experience System.

## Capability truth

- 8 productos + 8 servicios canónicos continúan gobernando alcance, entregables y límites;
- Contract Control y Regulatory Control no son SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada bajo propuesta y perímetro pactados;
- AI Governance 360 no sustituye auditoría técnica, seguridad o evaluación científica;
- Legal Engineering incorpora tecnología solo cuando se pacta expresamente;
- Meridiano Counsel permanece fuera de la oferta pública;
- no existe monitoreo automático universal ni decisión jurídica autónoma;
- portal/auth/CRM/pagos/firma/agenda/upload no se convierten en capabilities productivas por v7.4;
- no se publicaron precios nuevos.

## Release engineering v7.4

- `assets/data/v7/commercial-evidence-v74.json`: contrato de subjects, interactions, privacidad, activation boundary y lifecycle.
- `assets/js/v7/commercial-evidence-v74.js`: runtime local y efímero sin transporte externo.
- `scripts/apply_commercial_evidence_v74.py`: materialización determinista y lifecycle-aware.
- `scripts/validate_commercial_evidence_v74.py`: allowlist, privacidad, versión/canal y readiness fail-closed.
- `tests/e2e/commercial-evidence-v74.spec.mjs`: regresión de atribución comercial y límites.
- `.github/workflows/v74-commercial-evidence-readiness.yml`: gate dedicado.
- `scripts/normalize_experience_compat_v60.py`: recomposición canónica de la capa.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial.
- `assets/data/v7/`: contratos de las capas v7.
- `knowledge/00_CANON/`: memoria operativa actual.

## Siguiente frente

v7.4 deja preparada la infraestructura de evidencia sin activarla. La próxima ola debe decidir por separado si conviene habilitar un proveedor privacy-first y, comercialmente, continuar mejorando descubrimiento, autoridad y conversión de las ofertas existentes antes de crear nuevas capabilities.

Ver `RELEASE-v7.4.md` para evidencia, límites y arquitectura de la release.

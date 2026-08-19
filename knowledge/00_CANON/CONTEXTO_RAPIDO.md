# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **7.0.0 — Meridiano Legal Intelligence**.
- SHA funcional certificado y snapshot productivo: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Merge funcional: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.
- Candidate pre-merge: `50646aadb514611241c0210a6bcfaac8ba7fe2d8` — 9/9 workflows aplicables verdes.
- Canal de cierre: `github-pages-production-legal-intelligence-certified`.
- `main == stable == 291bf23b…` después de la promoción funcional automática.
- Browser E2E + axe y Lighthouse post-deploy: PASS antes de mover `stable`.
- Cobertura reducida: no. Budgets relajados: no.
- Search Console permanece sin configurar; analytics externa permanece deshabilitada.
- Portal, auth, CRM, pagos, firma, agenda y upload continúan fuera de capability productiva.
- WhatsApp continúa como handoff manual.

## Qué cambió en v7

**Meridiano Legal Intelligence** es una capa transversal de la marca Meridiano Legal. No crea un catálogo paralelo: conecta problemas empresariales con las seis rutas públicas y las 16 ofertas canónicas existentes.

La arquitectura organiza:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece como concepto futuro/no producto público.

La capa hace visible cómo combinar criterio jurídico, diseño de procesos, IA, automatización y Legal Engineering para diagnosticar, transformar, controlar y operar trabajo jurídico. Los catálogos canónicos siguen gobernando entregables, tiempos, honorarios, responsabilidades y límites.

## Superficies v7

v7 se materializa sobre 11 URLs existentes, sin crear nuevas rutas:

- `index.html`;
- `soluciones/index.html`;
- `soluciones/ordenar-operacion-juridica.html`;
- `servicios/legal-operations.html`;
- `productos/sistema-contractual-empresarial.html`;
- `soluciones/gobernar-inteligencia-artificial-empresa.html`;
- `productos/programa-gobernanza-ia.html`;
- `servicios/tecnologia-inteligencia-artificial.html`;
- `soluciones/estructurar-proyecto-regulado.html`;
- `productos/proyecto-regulado-estructurado.html`;
- `servicios/proyectos-regulados.html`.

La entrada pública continúa siendo situation-first y conserva exactamente las seis rutas v6.

## Capability truth

- no portal, auth, upload, CRM, firma, pagos o SaaS ficticio;
- Contract Control y Regulatory Control son patrones de implementación/operación, no productos SaaS autónomos;
- no CLM productivo implícito;
- no monitoreo automático universal;
- no certificaciones técnicas no incluidas;
- no garantías sobre licencias, permisos o decisiones de autoridades;
- Legal Desk mantiene SLA, canales y capacidad sujetos a propuesta específica;
- automatizaciones, agentes, integraciones y herramientas solo forman parte de un encargo si se incluyen expresamente;
- Meridiano Counsel permanece fuera de la oferta pública.

## v6.4 y capas previas preservadas

- Fit & Scope v6.4: 16/16 fichas conservan `situations` y `supplements` con `#v6-fit-scope` entre Resultado y Entregables.
- Engagement Clarity v6.3: `requirements` + `responsibilities` preservados.
- Search Discovery v6.2: 43 indexables + 3 `noindex`; sitemap canónico de 43 URLs.
- Measurement v6.1: privacy-first; analytics externa deshabilitada.
- Experience System v6.0: 46/46 superficies.
- 1/1 formulario físico canónico.
- 30/30 pasos históricos del builder.

## Release engineering v7

- `assets/data/v7/legal-intelligence-architecture-v70.json`: contrato arquitectónico phase-aware y certificado.
- `assets/data/v7/legal-intelligence-prototype-v70.json`: Legal Intelligence / operación jurídica.
- `assets/data/v7/legal-intelligence-deep-offers-v70.json`: Legal AI Transformation + Contract Control.
- `assets/data/v7/ai-governance-360-prototype-v70.json`: AI Governance 360.
- `assets/data/v7/regulatory-control-prototype-v70.json`: Regulatory Control.
- `assets/data/v7/legal-intelligence-discovery-v70.json`: Home + hub.
- `scripts/apply_*_v70.py`: materializadores deterministas.
- `scripts/validate_*_v70.py`: validators fail-closed.
- `scripts/normalize_experience_compat_v60.py`: integración en la cadena canónica existente.
- `tests/e2e/legal-intelligence-v70.spec.mjs`: E2E de las 11 superficies, boundaries, seis rutas y ausencia pública de Counsel.

## Evidencia de promoción

- Reconciliación limpia sobre v6.4: `67b097c4e6cb1adf9d252aafb7e6a524b7e0636e` — 9/9 gates verdes.
- Candidate final: `50646aadb514611241c0210a6bcfaac8ba7fe2d8` — 9/9 gates verdes.
- PR funcional: #167.
- Merge: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.
- Builder canónico: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Pages completó quality, deploy, live smoke, Browser/axe y Lighthouse antes del snapshot.
- `stable` fue promovido automáticamente a `291bf23b…`; no se movió manualmente.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial principal.
- `assets/data/v7/`: contratos Legal Intelligence.
- `assets/data/v6/fit-scope-clarity-v64.json`: Fit & Scope.
- `assets/data/v6/engagement-clarity-v63.json`: Engagement Clarity.
- `assets/data/v6/search-discovery-readiness-v62.json`: Search Discovery.
- `assets/data/v6/measurement-readiness-v61.json`: Measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.

## Frente vigente

No hay un ciclo funcional nuevo abierto. El único frente es el **cierre documental v7.0.0 candidate → certified** en `docs/v700-release-closure`.

Ese cierre debe atravesar sus propios gates pre-merge y, después de fusionarse, volver a completar Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot. Queda cerrado cuando `main == stable` en el commit canónico resultante.

## Invariantes

No inventar clientes, testimonios, resultados, precios, capacidades tecnológicas o certificaciones; no PII ni exportación del formulario; no backend/CRM/portal/auth/firma/pagos/agenda/upload ficticios; no reducir E2E/axe ni relajar Lighthouse; conservar un único formulario, seis rutas públicas y 30 pasos históricos; `stable` solo después de gates verdes.

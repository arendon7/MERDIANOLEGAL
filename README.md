# Meridiano Legal · Web canónica v7.0.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v7.0.0 — Meridiano Legal Intelligence**.

- SHA funcional certificado: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Merge funcional: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.
- Candidate pre-merge: `50646aadb514611241c0210a6bcfaac8ba7fe2d8` — 9/9 workflows verdes.
- Canal certificado: `github-pages-production-legal-intelligence-certified`.
- 46 HTML públicos, 16 fichas profundas y 1 formulario físico canónico.
- `main == stable` después de la promoción funcional automática.
- Browser E2E + axe y Lighthouse post-deploy: PASS antes de mover `stable`.
- Cobertura reducida: no. Budgets relajados: no.

## v7 — Meridiano Legal Intelligence

Meridiano Legal permanece como marca madre. **Meridiano Legal Intelligence** es una capa transversal que hace visible cómo Meridiano puede combinar criterio jurídico, diseño de procesos, IA, automatización y Legal Engineering para diagnosticar, transformar, controlar y operar trabajo jurídico.

No es un catálogo paralelo. La navegación continúa entrando por la situación/decisión del cliente y las seis rutas v6; los 8 productos y 8 servicios canónicos siguen gobernando el alcance jurídico y comercial.

La arquitectura organiza:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece como concepto futuro/no producto público.

## Superficies v7

La capa se materializa sobre 11 URLs existentes:

- Home y hub de Soluciones;
- ruta de Legal Operations;
- servicio Legal Operations;
- producto Sistema Contractual Empresarial;
- ruta, producto y servicio de IA;
- ruta, producto y servicio de proyectos regulados.

No se añadió una séptima ruta ni nuevas URLs por nomenclatura v7.

## Capability truth

La release mantiene límites fail-closed:

- portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados;
- Contract Control y Regulatory Control: patrones de implementación/operación, no SaaS autónomos;
- no CLM productivo implícito;
- no monitoreo automático universal;
- no certificaciones técnicas no incluidas;
- no garantía sobre licencias, permisos o decisiones de autoridades;
- Legal Desk: SLA, canales y capacidad sujetos a la propuesta específica;
- Meridiano Counsel: fuera de la oferta pública.

## v6.4 preservada

v7 fue reconciliada sobre la baseline certificada **v6.4.0 — Fit & Scope Clarity**.

- 16/16 fichas conservan `situations` → **Señales de que esta modalidad encaja**.
- 16/16 conservan `supplements` → **Situaciones que amplían el alcance**.
- `#v6-fit-scope` permanece después de Resultado y antes de Entregables.
- Engagement Clarity v6.3 continúa íntegra.
- Search Discovery v6.2 conserva 43 indexables + 3 `noindex`.
- Measurement v6.1 sigue privacy-first y con analytics externa deshabilitada.
- Experience System v6.0 mantiene 46/46 superficies y 30 pasos históricos.

## Verdad jurídica y comercial

La fuente principal continúa en:

- `catalog-products-v41/*.json` para 8 productos;
- `catalog-services-v42/*.json` para 8 servicios.

Legal Intelligence puede reorganizar navegación, recorridos y formas de intervención, pero no puede modificar silenciosamente entregables, honorarios, tiempos, responsabilidades o límites de esos catálogos.

## Release engineering v7

- `assets/data/v7/legal-intelligence-architecture-v70.json`: contrato arquitectónico phase-aware.
- `assets/data/v7/legal-intelligence-prototype-v70.json`: ruta de operación jurídica.
- `assets/data/v7/legal-intelligence-deep-offers-v70.json`: Legal AI Transformation + Contract Control.
- `assets/data/v7/ai-governance-360-prototype-v70.json`: AI Governance 360.
- `assets/data/v7/regulatory-control-prototype-v70.json`: Regulatory Control.
- `assets/data/v7/legal-intelligence-discovery-v70.json`: Home + hub.
- `scripts/apply_*_v70.py`: materializadores deterministas.
- `scripts/validate_*_v70.py`: validators fail-closed.
- `scripts/normalize_experience_compat_v60.py`: integración en la cadena canónica.
- `tests/e2e/legal-intelligence-v70.spec.mjs`: E2E de las 11 superficies y boundaries.

## Evidencia de promoción funcional

- Reconciliación v6.4 + v7: `67b097c4e6cb1adf9d252aafb7e6a524b7e0636e` — 9/9 gates verdes.
- Candidate 7.0.0: `50646aadb514611241c0210a6bcfaac8ba7fe2d8` — 9/9 gates verdes.
- PR #167 fusionado con expected head SHA.
- Merge: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.
- Builder: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Pages quality, deploy, live smoke, Browser/axe y Lighthouse precedieron la promoción automática de `stable`.
- `stable` fue movido por workflow, no manualmente, a `291bf23b…`.

## Discovery, privacidad y capacidades preservadas

- 43 páginas indexables con canonical autorreferencial;
- 3 superficies `noindex` preservadas;
- sitemap canónico de 43 URLs;
- Search Console sigue sin token auténtico/configuración verificada;
- analytics externa sigue apagada;
- no PII ni contenido del formulario exportados;
- un único formulario físico canónico;
- WhatsApp continúa como handoff manual.

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

## Documentación

- `RELEASE-v7.0.md`: alcance, reconciliación, evidencia y cierre v7.
- `RELEASE-v6.4.md`: cierre histórico de Fit & Scope Clarity.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md`: contexto operativo actual.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico y certificación.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: frente vigente.

Este cierre documental queda definitivo cuando su propio SHA atraviese otra vez Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y termine nuevamente con `main == stable`.

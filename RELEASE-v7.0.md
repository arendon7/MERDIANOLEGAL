# Meridiano Legal — Release v7.0.0

Fecha funcional: 2026-08-18.

## Resultado

**v7.0.0 — Meridiano Legal Intelligence** está publicada y certificada funcionalmente sobre la baseline **v6.4.0 — Fit & Scope Clarity**.

Meridiano Legal continúa como marca madre. Meridiano Legal Intelligence funciona como una capa transversal que conecta criterio jurídico, procesos, inteligencia artificial, automatización y Legal Engineering con las seis rutas públicas y las 16 ofertas canónicas existentes. No crea un catálogo paralelo ni modifica silenciosamente el alcance jurídico/comercial.

## Arquitectura publicada

La capa organiza siete capacidades/recorridos:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece expresamente como concepto futuro/no producto público.

## Superficies

v7 se materializa sobre 11 superficies existentes, sin crear nuevas URLs:

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

La navegación principal sigue siendo situation-first y conserva exactamente las seis rutas v6.

## Verdad jurídica y capability boundaries

Los 8 productos y 8 servicios canónicos continúan gobernando entregables, tiempos, honorarios, responsabilidades y límites. La capa v7 no altera esa verdad.

Los validators fail-closed preservan, entre otros, estos límites:

- no portal, auth, upload, CRM, firma, pagos o SaaS ficticio;
- Contract Control y Regulatory Control siguen como patrones de implementación/operación, no SaaS autónomos;
- no CLM productivo implícito;
- no monitoreo automático universal;
- no certificaciones o auditorías técnicas no incluidas;
- no garantías sobre licencias, permisos o decisiones de autoridades;
- no exposición pública de Meridiano Counsel;
- Legal Desk mantiene canales, capacidad y SLA sujetos al alcance pactado.

## Reconciliación con v6.4

El prototipo inicial #163 había nacido sobre v6.3. Cuando `main` avanzó a v6.4, ese PR dejó de ser un vehículo seguro de release.

Se abrió una rama nueva desde v6.4 y se portó únicamente source v7. Luego se rematerializaron las 11 superficies sobre Fit & Scope Clarity y se validaron ambas capas en conjunto.

- SHA de reconciliación limpia: `67b097c4e6cb1adf9d252aafb7e6a524b7e0636e`.
- Resultado: 9/9 workflows aplicables verdes.
- Fit & Scope v6.4: preservado.
- Graphify temporal de reconciliación: restaurado; no quedó en el diff funcional.

## Candidate pre-merge

Candidate final:

`50646aadb514611241c0210a6bcfaac8ba7fe2d8`

Ese mismo SHA superó 9/9 workflows:

1. V6 Candidate Validation.
2. V6 Canonical Builder Equivalence.
3. V6.4 Fit & Scope Clarity.
4. V6.3 Engagement Clarity.
5. V6.2 Search Discovery Readiness.
6. Release Governance.
7. Graphify.
8. V6 Browser Candidate / axe.
9. V6.1 Measurement Readiness / Browser E2E.

No se redujo cobertura, no se relajaron budgets y no se eliminaron tests para aprobar la release.

## Promoción funcional

- PR funcional: **#167**.
- Candidate SHA fijado para merge: `50646aadb514611241c0210a6bcfaac8ba7fe2d8`.
- Merge protegido por expected head SHA: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.
- Builder canónico post-merge: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- El Builder modificó únicamente la sincronización pública esperada de versión/metadata sobre las superficies instrumentadas.
- `main` quedó en `291bf23b…`.
- La cadena oficial Pages completó quality, deploy, live smoke, Browser/axe y Lighthouse antes del snapshot.
- `stable` fue promovido **automáticamente**, no manualmente, a `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Resultado funcional: `main == stable == 291bf23b…`.

La promoción automática de `stable` es la evidencia fail-closed de que los jobs productivos previos exigidos por `pages.yml` terminaron satisfactoriamente.

## Release engineering v7

- `assets/data/v7/legal-intelligence-architecture-v70.json`: contrato arquitectónico phase-aware.
- `assets/data/v7/legal-intelligence-prototype-v70.json`: recorrido Legal Intelligence / operación jurídica.
- `assets/data/v7/legal-intelligence-deep-offers-v70.json`: Legal AI Transformation + Contract Control.
- `assets/data/v7/ai-governance-360-prototype-v70.json`: Readiness → Implementación → Managed Governance.
- `assets/data/v7/regulatory-control-prototype-v70.json`: Estructurar → Controlar → Acompañar.
- `assets/data/v7/legal-intelligence-discovery-v70.json`: descubrimiento público Home + hub.
- `scripts/apply_*_v70.py`: materializadores deterministas.
- `scripts/validate_*_v70.py`: validators fail-closed.
- `scripts/normalize_experience_compat_v60.py`: integración v7 dentro de la cadena canónica existente.
- `tests/e2e/legal-intelligence-v70.spec.mjs`: presencia, boundaries, seis rutas, ausencia de Counsel y navegación por fragmentos.

## Capas anteriores preservadas

- v6.4 Fit & Scope Clarity: 16/16 fichas.
- v6.3 Engagement Clarity: requirements + responsibilities.
- v6.2 Search Discovery: 43 indexables + 3 noindex.
- v6.1 Measurement: privacy-first; analytics externa deshabilitada.
- v6.0 Experience System: 46 superficies.
- 1 formulario físico canónico.
- 30 pasos históricos del builder.
- WhatsApp como handoff manual.

## Cierre documental

Este archivo pertenece al cierre separado `candidate → certified`. El cierre queda definitivo cuando su propio SHA atraviese nuevamente los gates pre-merge, se fusione y vuelva a completar Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot con `main == stable`.

El canal certificado es:

`github-pages-production-legal-intelligence-certified`

El PR #163 debe permanecer sin merge y cerrarse como superseded por #167/reconciliación v6.4.

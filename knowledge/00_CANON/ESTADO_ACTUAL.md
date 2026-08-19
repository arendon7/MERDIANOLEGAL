# Meridiano Legal — Estado canónico

Última verificación funcional: 2026-08-18.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **7.0.0 — Meridiano Legal Intelligence**.
- SHA funcional certificado: `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Merge funcional: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.
- Candidate pre-merge: `50646aadb514611241c0210a6bcfaac8ba7fe2d8`.
- Canal de cierre: `github-pages-production-legal-intelligence-certified`.
- Antes de abrir este cierre documental, `main == stable == 291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.

## Resultado v7.0

v7 hace visible una capacidad transversal que ya existía distribuida entre Diagnóstico, Dirección Jurídica Externa, Contratación, Tecnología/IA, Proyectos Regulados y Legal Operations: diagnosticar, transformar, controlar y operar trabajo jurídico combinando criterio legal, procesos, IA, automatización y Legal Engineering.

### Arquitectura Legal Intelligence

Meridiano Legal permanece como marca madre. **Meridiano Legal Intelligence** no es un catálogo paralelo ni una nueva unidad comercial independiente.

La arquitectura organiza:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece como concepto futuro/no producto público.

### Superficies y navegación

- 11 superficies existentes materializan la capa v7.
- No se crean nuevas URLs por nomenclatura Legal Intelligence.
- Las seis rutas de solución v6 continúan siendo la entrada principal.
- Home explica Diagnosticar → Transformar → Controlar → Operar.
- El hub de Soluciones presenta Legal Intelligence como capa transversal, no como séptima ruta.
- Legal Operations conecta diagnóstico, transformación y operación.
- Sistema Contractual Empresarial explica Contract Control.
- IA organiza Readiness → Implementación → Gobierno recurrente.
- Proyectos regulados organiza Estructurar → Controlar → Acompañar.

## Verdad jurídica y capability boundaries

Los 8 productos y 8 servicios canónicos continúan gobernando entregables, tiempos, honorarios, responsabilidades y límites. v7 no modifica silenciosamente esa verdad.

Invariantes:

- portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados;
- Contract Control y Regulatory Control: patrones de implementación/operación, no SaaS autónomos;
- no CLM productivo implícito;
- no monitoreo automático universal;
- no auditorías técnicas o certificaciones no incluidas;
- no garantía sobre licencias, permisos o decisiones de autoridades;
- Legal Desk mantiene SLA, canales y capacidad sujetos al alcance pactado;
- Meridiano Counsel no es oferta transaccional pública;
- automatizaciones, agentes, integraciones o herramientas solo integran un encargo cuando están expresamente incluidas en su alcance.

## Capas previas preservadas

- **v6.4 Fit & Scope Clarity:** 16/16 fichas con `situations` y `supplements`; `#v6-fit-scope` entre Resultado y Entregables.
- **v6.3 Engagement Clarity:** 16/16 fichas con `requirements` + `responsibilities` y `#v6-engagement`.
- **v6.2 Search Discovery:** 43 indexables + 3 `noindex`; sitemap canónico de 43 URLs.
- **v6.1 Measurement:** privacy-first, sin PII exportada y analytics externa deshabilitada.
- **v6.0 Experience System:** 46/46 superficies estructurales preservadas.
- 1/1 formulario físico canónico.
- WhatsApp manual.
- 30/30 pasos históricos exactos del builder.

## Evidencia funcional v7

### Reconciliación con v6.4

El prototipo original #163 nació sobre v6.3 y dejó de ser un vehículo seguro cuando `main` avanzó a v6.4. Se creó una rama nueva desde v6.4, se portó únicamente source v7 y las 11 superficies se rematerializaron sobre la baseline vigente.

- SHA limpio de reconciliación: `67b097c4e6cb1adf9d252aafb7e6a524b7e0636e`.
- 9/9 workflows aplicables: PASS.
- Fit & Scope v6.4 validado después de aplicar v7.
- Boundary: únicamente las 11 superficies previstas.
- Graphify temporal restaurado; no quedó en el diff funcional.

### Candidate y merge

- Candidate final: `50646aadb514611241c0210a6bcfaac8ba7fe2d8`.
- Nueve workflows aplicables sobre el mismo SHA: PASS:
  - V6 Candidate Validation;
  - V6 Canonical Builder Equivalence;
  - V6.4 Fit & Scope Clarity;
  - V6.3 Engagement Clarity;
  - V6.2 Search Discovery Readiness;
  - Release Governance;
  - Graphify;
  - V6 Browser Candidate / axe;
  - V6.1 Measurement Readiness / Browser E2E.
- PR #167 fusionado con expected head SHA.
- Merge funcional: `6b655fbf502196473a0457fd8e47d0c29e74ab41`.

### Producción

- Builder post-merge produjo `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- El diff del Builder fue la sincronización pública esperada de versión/metadata, sin reescritura sustantiva de la arquitectura jurídica v7.
- GitHub Pages sirve la release v7.0.0.
- Quality, deploy, live smoke, Browser/axe y Lighthouse precedieron el snapshot productivo.
- `stable` fue promovido automáticamente, no manualmente, a `291bf23b6e9cd3d3cfb1743f032a4bc4583f726b`.
- Antes de este cierre documental: `main == stable == 291bf23b…`.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para aprobar la release: no.

## Release engineering v7

1. **Arquitectura source-driven.** La capa se deriva de contratos v7, no de edición HTML manual.
2. **Verdad jurídica no duplicada.** Los catálogos v4.1/v4.2 siguen gobernando las 16 ofertas.
3. **Materializadores deterministas.** `scripts/apply_*_v70.py` produce las superficies previstas.
4. **Validators fail-closed.** `scripts/validate_*_v70.py` exige soporte canónico y boundaries de capability.
5. **Phase-aware architecture contract.** `prototype → release-candidate → certified` sin habilitar capabilities por cambio de fase.
6. **Compatibilidad v6.4.** Fit & Scope se valida después de aplicar v7.
7. **Normalizador canónico.** `normalize_experience_compat_v60.py` reproduce v7 dentro de la cadena existente.
8. **E2E dedicado.** `legal-intelligence-v70.spec.mjs` recorre 11 superficies, boundaries y navegación por fragmentos.
9. **No séptima ruta.** Las seis rutas siguen siendo invariantes públicas.
10. **Stable fail-closed.** Solo se mueve después de los gates productivos oficiales.

## PR principal

- #167 — release funcional v7 reconciliada sobre v6.4: fusionado y publicado.
- #163 — prototipo histórico sobre v6.3: debe cerrarse sin merge como superseded por #167.

## Estado del ciclo

**v7.0.0 está implementada, materializada, publicada y certificada funcionalmente.**

El único frente restante es este cierre documental `candidate → certified` en `docs/v700-release-closure`. Este cierre no cambia producto, HTML público, catálogos ni capabilities. Actualiza canal, estado arquitectónico y memoria de release.

El ciclo v7 quedará totalmente cerrado cuando el commit documental atraviese nuevamente sus gates, se fusione y complete Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot con `main == stable` y `stable/version.json` en `github-pages-production-legal-intelligence-certified`.

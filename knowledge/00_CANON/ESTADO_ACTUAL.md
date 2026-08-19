# Meridiano Legal — Estado canónico

Última verificación funcional: 2026-08-19.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release vigente: **7.1.0 — Commercial Clarity** sobre **Meridiano Legal Intelligence**.
- Canal de cierre: `github-pages-production-commercial-clarity-certified`.
- Antes de abrir el cierre documental: `main == stable == 8b13ff120cceddc9c9913892416046efb7368572`.
- Los 8 productos + 8 servicios canónicos continúan gobernando alcance, entregables, tiempos, honorarios, responsabilidades y límites.

## Resultado v7.1

v7.1 mejora la comprensión comercial de la arquitectura v7.0 sin crear rutas, productos o servicios nuevos.

La Home aplica profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

### Cuatro formas de intervención

1. **Diagnosticar** — Legal AI Diagnostic, auditorías y diagnósticos focales.
2. **Implementar** — productos cerrados, Legal AI Transformation, AI Governance 360, Contract Control y Regulatory Control.
3. **Operar** — Dirección Jurídica Externa, Meridiano Legal Desk y modalidades gestionadas expresamente pactadas.
4. **Construir** — Legal Engineering Studio cuando el caso requiere una solución jurídica-tecnológica específica.

### Capacidades visibles

La Home explica cuatro capacidades que pueden quedar funcionando dentro de alcance contratado:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering permanece visible en **Construir** y no se duplica como quinta capacidad instalada.

### Densidad y diseño

- `v6-outcomes` y `v6-home-method` fueron absorbidos de la lectura principal para evitar redundancia.
- Se preserva el mensaje: **“El trabajo jurídico debe dejar algo que la organización pueda usar, ejecutar y verificar.”**
- La grilla usa 4 columnas desktop, 2×2 tablet y apilado móvil.
- El contraste WCAG de las capacidades sobre superficie clara fue corregido de forma scoped.
- El lenguaje operativo reduce anglicismos no esenciales.
- El hub de Soluciones explica valor y resultado antes que nomenclatura interna.

## Arquitectura v7 preservada

Meridiano Legal permanece como marca madre. **Meridiano Legal Intelligence** continúa como capa transversal y no como catálogo paralelo.

La arquitectura organiza:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece como concepto futuro/no producto público.

Las seis rutas públicas siguen siendo la entrada principal y las 16 ofertas canónicas continúan gobernando la verdad jurídica y comercial.

## Capability truth

Invariantes:

- portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados;
- Contract Control y Regulatory Control: capacidades/patrones de implementación y operación, no SaaS autónomos;
- no CLM productivo implícito;
- no monitoreo automático universal;
- AI Governance 360 no sustituye auditorías técnicas, seguridad o evaluación científica;
- no certificaciones técnicas no incluidas;
- no garantía sobre licencias, permisos o decisiones de autoridades;
- Legal Desk mantiene perímetro, canales, capacidad y niveles de servicio sujetos al alcance pactado;
- Legal Engineering solo incorpora desarrollo, integraciones, interfaces de IA o automatización cuando se pactan expresamente;
- Meridiano Counsel no es oferta transaccional pública;
- no se publicaron nuevas tarifas.

## Capas previas preservadas

- **v6.4 Fit & Scope Clarity:** 16/16 fichas con `situations` y `supplements`.
- **v6.3 Engagement Clarity:** 16/16 fichas con `requirements` + `responsibilities`.
- **v6.2 Search Discovery:** 43 indexables + 3 `noindex`; sitemap canónico de 43 URLs.
- **v6.1 Measurement:** privacy-first, sin PII exportada y analytics externa deshabilitada.
- **v6.0 Experience System:** 46/46 superficies estructurales.
- 1/1 formulario físico canónico.
- WhatsApp manual.
- 30/30 pasos históricos exactos del builder.

## Evidencia v7.1

### Cambio funcional #170

- Baseline: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`.
- Candidate funcional final: `12c8145dc8b6a3901217eb3d5793e210bfe06486`.
- Gates aplicables same-SHA: PASS.
- PR #170 fusionado con `expected_head_sha`.
- Merge funcional: `f01c5163e2c70012218c7d369bfb68180db04ed7`.
- La cadena productiva promovió `stable` automáticamente; no se movió manualmente.

### Release candidate #171

- Candidate formal: `8f0a3c2e016b6bc1aab92922f418965e57cb06c3`.
- 9/9 workflows aplicables: PASS:
  - V6 Candidate Validation;
  - V6 Canonical Builder Equivalence;
  - V6.4 Fit & Scope Clarity;
  - V6.3 Engagement Clarity;
  - V6.2 Search Discovery Readiness;
  - Release Governance;
  - Graphify;
  - V6 Browser Candidate / axe;
  - V6.1 Measurement Readiness / Browser E2E.
- Browser y Measurement fueron reejecutados sobre el mismo SHA después de cancelaciones externas; terminaron en `success` sin cambios de código.
- PR #171 fusionado con `expected_head_sha`.
- Merge candidate: `5185e5c1aed4e3ed23074a41318e446fbb3a741d`.
- Builder canónico: `8b13ff120cceddc9c9913892416046efb7368572`.
- Pages quality, deploy, live smoke, Browser/axe y Lighthouse: PASS.
- Snapshot productivo: `stable → 8b13ff120cceddc9c9913892416046efb7368572`.
- Antes de este cierre: `main == stable == 8b13ff120cceddc9c9913892416046efb7368572`.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para aprobar: no.

## Release engineering v7.1

1. **Source-driven.** `assets/data/v7/home-commercial-clarity-v71.json` gobierna Home + hub.
2. **Materialización determinista.** `apply_legal_intelligence_discovery_v70.py` reproduce la superficie comercial.
3. **Lifecycle phase-aware.** `prototype → release-candidate → certified` sin habilitar capabilities por cambio de estado.
4. **Verdad jurídica no duplicada.** Catálogos v4.1/v4.2 siguen gobernando las 16 ofertas.
5. **Idempotencia.** Segunda pasada canónica sin drift.
6. **E2E release-aware.** La regresión valida la arquitectura consolidada.
7. **Stable fail-closed.** Solo se mueve después de Browser y Lighthouse productivos.

## Cierre certified

El cierre `docs/v710-certified-closure` contiene únicamente siete fuentes de metadata/documentación:

1. `version.json`.
2. `assets/data/v7/home-commercial-clarity-v71.json`.
3. `README.md`.
4. `RELEASE-v7.1.md`.
5. `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
6. `knowledge/00_CANON/ESTADO_ACTUAL.md`.
7. `knowledge/00_CANON/TAREA_ACTIVA.md`.

No modifica HTML, CSS, catálogos, materializadores, validators funcionales, E2E, workflows ni capabilities.

La certificación documental queda definitiva cuando el SHA final de este cierre supere sus propios workflows, se fusione con `expected_head_sha` y complete nuevamente Builder → Pages → live smoke → Browser/axe → Lighthouse → snapshot, terminando con `main == stable` y `stable/version.json` en canal `github-pages-production-commercial-clarity-certified`.

## Siguiente frente

Después del cierre de v7.1, la siguiente ola recomendada es **Buying Clarity** para fichas profundas y Centro Demo, derivando cantidades, entregables, duración, requisitos, continuidad y forma de contratación exclusivamente de los catálogos canónicos. No introducir tarifas hasta contar con pricing truth aprobado.

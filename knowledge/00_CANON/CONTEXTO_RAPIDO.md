# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas, seis rutas públicas y un único formulario físico canónico.

## Estado vigente

- Release: **7.1.0 — Commercial Clarity** sobre **Meridiano Legal Intelligence**.
- Canal de cierre: `github-pages-production-commercial-clarity-certified`.
- Candidate funcional: `12c8145dc8b6a3901217eb3d5793e210bfe06486`.
- Merge funcional #170: `f01c5163e2c70012218c7d369bfb68180db04ed7`.
- Candidate formal 7.1.0: `8f0a3c2e016b6bc1aab92922f418965e57cb06c3` — 9/9 workflows verdes.
- Merge candidate #171: `5185e5c1aed4e3ed23074a41318e446fbb3a741d`.
- Builder/snapshot productivo: `8b13ff120cceddc9c9913892416046efb7368572`.
- Antes del cierre documental: `main == stable == 8b13ff120cceddc9c9913892416046efb7368572`.
- Browser E2E + axe y Lighthouse post-deploy: PASS antes de mover `stable`.
- Cobertura reducida: no. Budgets relajados: no.
- Search Console permanece sin configurar; analytics externa permanece deshabilitada.
- Portal, auth, CRM, pagos, firma, agenda y upload continúan fuera de capability productiva.
- WhatsApp continúa como handoff manual.

## Qué hace v7.1

v7.1 no crea ofertas nuevas. Mejora la comprensión comercial de Legal Intelligence mediante profundidad progresiva:

**situación → forma de intervención → capacidad concreta → resultado → profundidad jurídica de respaldo**.

Cuatro formas de intervención:

1. **Diagnosticar**.
2. **Implementar**.
3. **Operar**.
4. **Construir**.

Capacidades visibles que pueden quedar operando dentro del alcance pactado:

- Contract Control;
- AI Governance 360;
- Regulatory Control;
- Meridiano Legal Desk.

Legal Engineering Studio permanece en **Construir**.

## Arquitectura v7 preservada

Meridiano Legal sigue siendo marca madre y **Meridiano Legal Intelligence** una capa transversal, no un catálogo paralelo.

La arquitectura organiza:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.

`Meridiano Counsel` permanece como concepto futuro/no producto público.

Los 8 productos y 8 servicios canónicos siguen gobernando entregables, tiempos, honorarios, responsabilidades y límites.

## Capability truth

- no portal, auth, upload, CRM, firma, pagos o SaaS ficticio;
- Contract Control y Regulatory Control no son SaaS autónomos;
- no CLM productivo implícito;
- no monitoreo automático universal;
- AI Governance 360 no sustituye seguridad, auditorías técnicas o evaluación científica;
- no certificaciones técnicas no incluidas;
- no garantías sobre licencias, permisos o decisiones de autoridades;
- Legal Desk mantiene perímetro, canales, capacidad y niveles de servicio sujetos a propuesta específica;
- Legal Engineering solo incorpora tecnología expresamente pactada;
- Meridiano Counsel permanece fuera de la oferta pública;
- no se publicaron tarifas nuevas.

## Capas previas preservadas

- Fit & Scope v6.4: 16/16 fichas con `situations` y `supplements`.
- Engagement Clarity v6.3: `requirements` + `responsibilities` preservados.
- Search Discovery v6.2: 43 indexables + 3 `noindex`; sitemap de 43 URLs.
- Measurement v6.1: privacy-first; analytics externa deshabilitada.
- Experience System v6.0: 46/46 superficies.
- 1/1 formulario físico canónico.
- 30/30 pasos históricos del builder.

## Evidencia de promoción v7.1

### Funcional #170

- `12c8145…` — candidate funcional final.
- #170 fusionado con expected head SHA.
- `f01c516…` — merge funcional y primera promoción productiva automática.

### Candidate #171

- `8f0a3c2…` — candidate 7.1.0 con 9/9 workflows PASS.
- #171 fusionado con expected head SHA.
- `5185e5c…` — merge candidate.
- `8b13ff1…` — Builder canónico.
- Pages quality, deploy, live smoke, Browser/axe y Lighthouse: PASS.
- `stable` promovido automáticamente a `8b13ff1…`; no se movió manualmente.

## Source of truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial principal.
- `assets/data/v7/`: Legal Intelligence + Commercial Clarity.
- `assets/data/v6/fit-scope-clarity-v64.json`: Fit & Scope.
- `assets/data/v6/engagement-clarity-v63.json`: Engagement Clarity.
- `assets/data/v6/search-discovery-readiness-v62.json`: Search Discovery.
- `assets/data/v6/measurement-readiness-v61.json`: Measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.

## Frente vigente

Únicamente el cierre documental **v7.1.0 candidate → certified** en `docs/v710-certified-closure`.

El cierre contiene siete fuentes documentales/metadata y no cambia funcionalidad pública. Debe superar sus propios gates, fusionarse con SHA protegido y completar Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot. Queda definitivo cuando `main == stable` y `stable/version.json` declare el canal certificado.

Después se abre una ola independiente de **Buying Clarity** para fichas profundas y Centro Demo, siempre derivada de los catálogos canónicos y sin introducir precios no aprobados.

## Invariantes

No inventar clientes, testimonios, resultados, precios, capacidades tecnológicas o certificaciones; no PII ni exportación del formulario; no backend/CRM/portal/auth/firma/pagos/agenda/upload ficticios; no reducir E2E/axe ni relajar Lighthouse; conservar un único formulario, seis rutas públicas y 30 pasos históricos; `stable` solo después de gates verdes.

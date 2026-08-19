# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance**.
- SHA funcional certificado: `0045588f795f5f0a0b9144786bc61cdf89f34319`.
- Canal de cierre: `github-pages-production-fit-scope-clarity-certified`.
- 16/16 fichas muestran `situations` y `supplements` derivados exactamente de sus catálogos canónicos.
- Cada ficha contiene una única sección `#v6-fit-scope` entre Resultado y Entregables.
- El TOC profundo conserva exactamente los 7 hitos de v6.3; v6.4 no agrega enlace propio.
- Engagement Clarity v6.3 permanece íntegra (`requirements` + `responsibilities`).
- Browser E2E + axe: PASS antes de la promoción automática de `stable`.
- Lighthouse post-deploy: PASS con budgets existentes antes de la promoción automática de `stable`.
- 46/46 HTML, 16/16 fichas, 1/1 formulario físico y 30/30 pasos históricos preservados.
- Search Console permanece sin configurar: no hay token auténtico y runtime publica `searchConsoleConfigured=false`.
- Analítica externa permanece deshabilitada: `analytics.enabled=false`, `provider=none`, `site_id=""`.
- Discovery v6.2 permanece íntegro: 43 indexables + 3 `noindex`, sitemap canónico de 43 URLs.
- Portal real deshabilitado; WhatsApp continúa como handoff manual.

## Qué cambió en v6.4

v6.4 hace visible truth que ya existía en los catálogos jurídicos/comerciales, pero no estaba representado con suficiente claridad en el recorrido ejecutivo de compra.

- `situations` se presenta como **Señales de que esta modalidad encaja**.
- `supplements` se presenta como **Situaciones que amplían el alcance**.
- La información no se reescribe: el validator compara fila por fila la representación pública contra `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.
- La nueva sección se integra después de Resultado y antes de Entregables.
- No se añade un octavo hito al TOC.
- El objetivo es reducir inferencias antes de solicitar propuesta, no crear criterios de elegibilidad ni ampliar contractualmente el servicio desde la capa visual.

## Release engineering v6.4

- Contrato: `assets/data/v6/fit-scope-clarity-v64.json`.
- Materializador: `scripts/apply_fit_scope_clarity_v64.py` con `--check` fail-closed.
- Validator: `scripts/validate_fit_scope_clarity_v64.py` contra los 16 catálogos canónicos.
- Gate v6.4 phase-aware: baseline 0/16 exige materializar exactamente 16; baseline 16/16 exige drift cero; cualquier estado parcial falla.
- Canonical Equivalence exige `measurement ∪ release ∪ discovery ∪ engagement ∪ fit/scope` cuando aplica.
- Builder, Pages y `canonical_pipeline_v524.py` comparten la misma extensión v6, conservando 30 pasos históricos.
- Candidate, Browser y Measurement materializan/validan v6.4 antes de sus suites.
- E2E recorre las 16 fichas, mantiene 7 hitos y comprueba el orden Resultado → Fit/Scope → Entregables.
- `stable` solo se mueve después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Incidencia de certificación

El primer Lighthouse productivo recibió HTTP 503 transitorio únicamente en `demo`; el resto de la cadena ya estaba verde. Un PR diagnóstico temporal (#164) reprodujo smoke, Browser/axe y Lighthouse contra la URL pública sin cambios de producto y se cerró sin merge. El rerun oficial de jobs fallidos pasó y el snapshot promovió `stable` automáticamente. No se relajaron budgets ni cobertura.

## Source-of-truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `assets/data/v6/fit-scope-clarity-v64.json`: contrato de encaje y cambio de alcance.
- `assets/data/v6/engagement-clarity-v63.json`: contrato de claridad precontratación.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `assets/data/v6/search-discovery-readiness-v62.json`: contrato de discovery/search verification.
- `assets/data/v6/measurement-readiness-v61.json`: contrato privacy-first de measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar tarifas o descuentos no aprobados;
- no crear criterios de encaje o ampliaciones distintos de `situations`/`supplements`;
- no PII ni lectura/exportación del contenido del formulario;
- no cotizador automático ni scoring de honorarios;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o upload ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- conservar exactamente 30 pasos históricos;
- analytics externa deshabilitada hasta decisión/revisión expresa;
- Search Console no puede declararse configurado sin token auténtico;
- readiness no equivale a ranking, tráfico ni indexación garantizada;
- `stable` solo después de gates verdes.

## Próximo ciclo

No se abre otra versión por inercia. Una vez este cierre documental quede también promovido a `stable`, no existe un ciclo funcional nuevo abierto. Cualquier siguiente ciclo debe partir de una necesidad observable de negocio, conversión, contenido u operación jurídica y comprobar primero si la verdad necesaria ya existe en los catálogos o contratos actuales.

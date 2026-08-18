# Meridiano Legal — Estado canónico

Última verificación: 2026-08-18.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **6.3.0 — Engagement Clarity / claridad precontratación**.
- SHA funcional certificado: `118cee5030f27689d91172beb525d7d92c751117`.
- Canal de cierre: `github-pages-production-engagement-clarity-certified`.
- La referencia documental definitiva se obtiene por los refs vigentes `main` y `stable`, que deben coincidir tras este cierre.

## Resultado v6.3

v6.3 eleva a primer nivel dos matrices jurídicas/comerciales que ya existían en los 16 catálogos canónicos y eran relevantes para decidir un encargo antes del contacto.

### Claridad precontratación

- 16/16 fichas profundas gobernadas.
- 8/8 productos y 8/8 servicios.
- Cada ficha incorpora exactamente un enlace `Para empezar`.
- Cada ficha incorpora exactamente una sección `#v6-engagement` antes de Límites.
- `requirements` se presenta como **Qué debe estar listo del lado del cliente**.
- `responsibilities` se presenta como **Cómo se distribuyen las responsabilidades**.
- Las filas visibles deben coincidir exactamente y en orden con el catálogo canónico correspondiente.
- No se crean obligaciones jurídicas nuevas ni se alteran entregables, perímetro, método, límites, honorarios o contacto.
- Navegación v6.3: exactamente 7 hitos.

### Discovery, measurement y capability truth preservados

- 46/46 HTML públicos.
- 43 páginas indexables + 3 `noindex` (`404.html`, `demo.html`, `experiencia.html`).
- Sitemap canónico de 43 URLs.
- Search Console: `readiness-not-verified`; token vacío; runtime `searchConsoleConfigured=false`.
- `analytics.enabled=false`, `provider=none`, `site_id=""`.
- 1/1 formulario físico canónico.
- WhatsApp manual.
- Portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados.
- 30/30 pasos históricos exactos del builder.

## Evidencia funcional

- SHA técnico pre-bump: `a7e8b057dc4818365247cd0615c796a233836203` — 7/7 gates técnicos verdes.
- Candidate final 6.3.0: `a90e035b0389344d7a6bc435a0735180a1d37051`.
- Ocho gates aplicables sobre ese SHA: PASS:
  - V6.3 Engagement Clarity;
  - V6.2 Search Discovery Readiness;
  - V6 Candidate Validation;
  - V6 Canonical Builder Equivalence;
  - Release Governance;
  - Graphify;
  - V6 Browser Candidate / axe;
  - V6.1 Measurement Readiness / Browser E2E.
- PR #160 fusionado con expected head SHA.
- Builder post-merge materializó exactamente la nueva superficie y produjo `118cee5030f27689d91172beb525d7d92c751117`.
- `stable` fue promovido automáticamente a `118cee50…` después de la cadena post-deploy.
- Browser/axe y Lighthouse productivos son prerequisitos del job que mueve `stable`; no hubo promoción manual.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para aprobar la release: no.

## Release engineering endurecido durante v6.3

1. **Truth reutilizado, no duplicado.** El renderer consume `requirements` y `responsibilities` directamente de los catálogos v4.1/v4.2.
2. **Validación fila por fila.** La representación HTML debe coincidir exactamente y en orden con su fuente canónica.
3. **Boundary exacto.** La transición inicial modifica exactamente 16 fichas; ningún HTML fuera de productos/servicios forma parte del engagement drift.
4. **Idempotencia real.** Se corrigió la posición de la hoja CSS v6.3 para que el reordenamiento histórico de estilos v6.0 no produzca whitespace drift en una segunda pasada.
5. **Claims heredados.** Un guard lexical inicial rechazaba palabras legítimas presentes en truth canónico; se eliminó ese falso positivo y se mantuvo la comparación exacta contra fuente como control más fuerte.
6. **v4.6 phase-aware.** Baselines sin v6.3 conservan exactamente 6 hitos; con v6.3 deben tener exactamente 7 y uno debe ser `#v6-engagement`.
7. **Equivalencia exacta.** Canonical Equivalence exige `measurement ∪ release ∪ discovery ∪ engagement` cuando aplica, sin permitir rutas por patrón amplio.
8. **Trigger coverage.** Builder, Candidate y Browser observan expresamente los scripts v6.3; `validate_pages_trigger_v511.py` exige cobertura del materializador.
9. **E2E real.** Chromium/WebKit recorren las 16 fichas; dos casos representativos prueban navegación efectiva al bloque.
10. **Gate post-materialización.** El gate v6.3 distingue una baseline `0/16` de una `16/16`: la primera exige 16 drift; la segunda exige 0; cualquier estado parcial falla.

## PR principal

- #160 — Engagement Clarity v6.3: contrato, renderer, validator, navegación, estilos, gates, E2E y release candidate.

## Invariantes preservadas

46 HTML; 16 fichas profundas; 1 formulario físico; WhatsApp manual; portal real deshabilitado; analytics externa deshabilitada; Search Console no verificada sin token real; no PII; no nuevas obligaciones desde la capa de presentación; no tarifas inventadas; exactamente 30 pasos históricos; Browser/axe/Lighthouse sin relajación; `stable` solo después de gates verdes.

## Estado del ciclo

**v6.3.0 está implementada, materializada, publicada y certificada funcionalmente. El único frente activo es cerrar documentalmente la release. Ese cierre queda definitivo cuando el commit que actualiza esta memoria y marca el canal como `certified` atraviese nuevamente Builder, Pages, smoke, Browser/axe, Lighthouse y termine con `main == stable`.**

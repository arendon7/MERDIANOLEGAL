# Meridiano Legal · Web canónica v6.4.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance**.

- SHA funcional certificado: `0045588f795f5f0a0b9144786bc61cdf89f34319`.
- Canal certificado: `github-pages-production-fit-scope-clarity-certified`.
- 46 HTML públicos, 16 fichas profundas y 1 formulario físico canónico.
- Las 16 fichas exponen `situations` y `supplements` derivados exactamente de los catálogos canónicos.
- Cada ficha incorpora una única sección `#v6-fit-scope` entre Resultado y Entregables.
- La navegación ejecutiva conserva exactamente los 7 hitos de v6.3; v6.4 deliberadamente no agrega un octavo enlace.
- Engagement Clarity v6.3 permanece íntegra: `requirements` + `responsibilities` y `#v6-engagement`.
- Search Console continúa sin configurar: `searchConsoleConfigured=false`, sin token auténtico.
- Analítica externa continúa deshabilitada: `analytics.enabled=false`, `provider=none`, `site_id=""`.
- 43 páginas indexables y 3 superficies `noindex` preservadas.
- 30 pasos históricos exactos del builder; sin paso 31.
- Browser E2E + axe: PASS.
- Lighthouse post-deploy: PASS con los budgets existentes antes de la promoción automática de `stable`.
- Cobertura reducida: no. Budgets relajados: no.

## v6.4 — Fit & Scope Clarity

v6.4 reduce fricción de autocalificación antes del contacto comercial sin crear criterios jurídicos nuevos. La mejora usa dos matrices que ya existían en las 16 fuentes de producto/servicio:

- **Señales de que esta modalidad encaja**, derivado de `situations`;
- **Situaciones que amplían el alcance**, derivado de `supplements`.

Ambas aparecen en `#v6-fit-scope`, inmediatamente después de Resultado y antes de Entregables. El objetivo es que el comprador pueda distinguir con mayor precisión si la modalidad corresponde a su situación y qué circunstancias cambian el perímetro base, sin confundir esa orientación con una propuesta o alcance contractual definitivo.

La capa no modifica `perimeter`, `limits`, entregables, método, honorarios, cronogramas, contacto o capability truth.

## Verdad jurídica y comercial

La fuente permanece en:

- `catalog-products-v41/*.json` para 8 productos;
- `catalog-services-v42/*.json` para 8 servicios.

`validate_fit_scope_clarity_v64.py` compara fila por fila las matrices visibles contra `situations` y `supplements` de cada catálogo. No existe una segunda copia editorial intermedia.

Engagement Clarity v6.3 conserva el mismo principio para `requirements` y `responsibilities`.

## Release engineering v6.4

- `assets/data/v6/fit-scope-clarity-v64.json`: contrato de presentación y alcance.
- `scripts/apply_fit_scope_clarity_v64.py`: materializador determinista con `--check` fail-closed.
- `scripts/validate_fit_scope_clarity_v64.py`: validator 16/16 contra truth canónico.
- `.github/workflows/v64-fit-scope-clarity.yml`: gate phase-aware; 0/16 exige 16 drift, 16/16 exige 0 y cualquier estado parcial falla.
- Canonical Equivalence exige `measurement ∪ release ∪ discovery ∪ engagement ∪ fit/scope` cuando aplica.
- Builder, Pages y `canonical_pipeline_v524.py` ejecutan la misma extensión v6; los 30 pasos históricos permanecen intactos.
- Candidate, Browser y Measurement materializan/validan v6.4 antes de sus suites.
- E2E visita las 16 fichas, verifica ambos paneles, conserva 7 hitos y prueba el orden Resultado → Fit/Scope → Entregables.
- `stable` continúa moviéndose únicamente después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Incidencia productiva v6.4

El primer run productivo obtuvo un HTTP 503 transitorio al cargar `demo` durante Lighthouse; quality, deploy, smoke y Browser ya habían pasado. Un diagnóstico temporal contra la misma URL pública reprodujo smoke, Browser/axe y Lighthouse en verde. Se reejecutaron los jobs fallidos del run oficial, sin cambios de código ni relajación de budgets; Lighthouse pasó y el snapshot promovió `stable` automáticamente.

El PR diagnóstico #164 se cerró sin merge.

## Discovery, privacidad y capability truth preservados

- 43 páginas indexables con canonical autorreferencial;
- `404.html`, `demo.html` y `experiencia.html` permanecen `noindex`;
- sitemap canónico de 43 URLs;
- Search Console sigue en readiness, no verificada;
- analytics externa sigue apagada;
- no PII ni contenido del formulario exportados;
- un único formulario físico canónico;
- WhatsApp continúa como handoff manual;
- portal real, auth, CRM, pagos, firma, agenda y upload continúan deshabilitados/no implementados.

## Source of truth

- `assets/data/v6/fit-scope-clarity-v64.json`: contrato v6.4.
- `scripts/apply_fit_scope_clarity_v64.py`: materializador v6.4.
- `scripts/validate_fit_scope_clarity_v64.py`: validator v6.4.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial principal.
- `assets/data/v6/engagement-clarity-v63.json`: contrato v6.3.
- `assets/data/v6/search-discovery-readiness-v62.json`: contrato de discovery.
- `assets/data/v6/measurement-readiness-v61.json`: contrato privacy-first de measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.

## Documentación

- `RELEASE-v6.4.md`: alcance, evidencia, incidencia productiva y cierre v6.4.
- `RELEASE-v6.3.md`: cierre histórico de Engagement Clarity.
- `RELEASE-v6.2.md`: cierre histórico de Search Discovery Readiness.
- `RELEASE-v6.1.md`: cierre histórico de Measurement Readiness.
- `RELEASE-v6.0.md`: cierre histórico del Experience System.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md`: contexto operativo actual.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico y certificación.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: frente vigente.

Este cierre documental queda definitivo cuando el commit de certificación atraviese nuevamente Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y termine con `main == stable`.

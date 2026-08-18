# Meridiano Legal — Estado canónico

Última verificación: 2026-08-18.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **6.0.0 — Experience System**.
- SHA funcional certificado: `a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.
- Canal certificado: `github-pages-production-experience-system-certified`.
- Al cierre funcional: `main == stable == a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.
- No existe un ciclo funcional posterior activo; el frente vigente es el cierre documental v6.0.0.
- El SHA documental definitivo se verifica por los refs vigentes `main` y `stable`, que deben coincidir tras la certificación del cierre.

## Resultado v6.0

v6 consolida la web pública alrededor de una arquitectura de decisión client-first:

**situación → resultado → intervención → evidencia → contacto**.

La migración quedó completada en las seis waves previstas:

- Wave 0: foundations, tokens, shell, materializadores, gates y validators v6.
- Wave 1: Home, Auditoría Jurídica Empresarial Integral, Tecnología e Inteligencia Artificial y contacto/mobile.
- Wave 2: 8 productos + 8 servicios.
- Wave 3: hub de soluciones + 6 rutas por situación.
- Wave 4: 8 sectores.
- Wave 5: hub editorial + 6 perspectivas.
- Wave 6: Firma, Experiencia, Centro Demo, legales y 404.

La release preserva toda la profundidad jurídica/comercial histórica y diferencia semánticamente decisión, resultado, entregable, proceso, perímetro, límite, evidencia y profundidad. No convierte la web en SPA ni introduce capacidades inexistentes.

## Superficies y truth preservados

- 46/46 HTML públicos.
- 8/8 productos.
- 8/8 servicios.
- 7/7 superficies de soluciones.
- 8/8 sectores.
- 6/6 perspectivas internas + hub editorial.
- 16/16 fichas profundas con truth visible y profundidad histórica preservada.
- 1/1 formulario físico canónico.
- 30/30 pasos exactos del builder.
- WhatsApp sigue siendo handoff manual.
- Portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados.
- Funnel y observabilidad: sin PII ni persistencia propia.

## Evidencia funcional

- SHA funcional final certificado: `a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.
- `stable` fue promovido automáticamente a ese mismo SHA después de la cadena post-deploy.
- GitHub Pages sirve `6.0.0` en `site-status.json`.
- Smoke público v5.0→v5.3: PASS sobre la URL servida.
- Diagnóstico independiente post-deploy, run `32145563599`:
  - Browser E2E + axe: PASS;
  - Lighthouse: PASS con budgets existentes;
  - v6 candidate/public probe: PASS.
- Equivalencia canónica pre-merge: PASS.
- Idempotencia de primera pasada sobre baseline v6: PASS.
- Idempotencia de segunda pasada: PASS.
- Validadores Python de Pages: PASS.
- `node --check` y validadores JSON de Pages: PASS.
- Release Governance: PASS en los hotfixes de cierre funcional.
- Graphify sobre el SHA funcional: PASS; 1.007 nodos, 1.887 relaciones, 115 notas wiki y 17 specs E2E detectadas.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para hacer pasar la release: no.

## Incidencias que endurecieron el release system

v6 no se cerró ocultando incompatibilidades; los gates detectaron y obligaron a corregir varias capas históricas:

1. **Equivalencia builder/Pages.** El pipeline necesitaba reconocer una baseline ya materializada en v6 y no volver a ejecutar materializadores legacy v4/v5.
2. **Validator v5.17.** Su comprobación dependía de indentación YAML literal; pasó a verificar orden semántico de composición sin reducir controles funcionales.
3. **Validators históricos de DOM.** `validate_site.py`, `validate_static_catalog.py`, v4.5, v4.6, v4.7 y `validate_page_context.py` conservaban supuestos visuales pre-v6. Se hicieron phase-aware: legacy mantiene sus requisitos; v6 valida los componentes semánticos equivalentes.
4. **Paridad real con Pages.** El gate de equivalencia pasó a ejecutar la cadena estática completa de Pages, incluidos Python, `node --check` y JSON, y a exigir diff cero de primera pasada sobre una baseline v6 canónica.
5. **Cobertura de trigger.** El builder no se disparaba ante algunos cambios de validators. El trigger canónico ahora cubre `scripts/validate_*.py` y su validator de topología exige esa cobertura.
6. **Candidate sobre baseline v6.** El gate candidate asumía que toda primera pasada debía producir cambios; ahora distingue pre-v6 de una baseline v6 ya canónica sin rebajar la segunda pasada ni el boundary de 46 superficies.
7. **Propagación de GitHub Pages.** El smoke live podía recibir HTTP 200 con una versión anterior durante propagación. `validate_live_v50.py` ahora usa cache-busting/no-cache y espera explícitamente la versión declarada antes de validar el resto.

## Invariantes preservadas

46 HTML; 16 fichas profundas; un único formulario físico; WhatsApp manual; portal real deshabilitado; funnel sin PII/persistencia; no inferir conversión; no tarifas inventadas; no ocultar profundidad material; exactamente 30 pasos canónicos; axe/Lighthouse sin relajación; `stable` solo después de gates verdes.

## Estado del ciclo

**v6.0 está implementada, publicada y certificada funcionalmente. No hay una release funcional posterior activa. El cierre documental queda definitivo cuando el commit que actualiza esta memoria y marca el canal como `certified` atraviese nuevamente builder, Pages, smoke, Browser/axe, Lighthouse, release-health y termine con `main == stable`.**

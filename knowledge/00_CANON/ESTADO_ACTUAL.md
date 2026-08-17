# Meridiano Legal — Estado canónico

Última verificación: 2026-08-17.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **5.31.0 — compresión decisional mediante divulgación progresiva**.
- SHA funcional certificado: `159be8a9e467a303faa8d302bfac93b33c2e7b29`.
- Canal: `github-pages-production-decision-compression-certified`.
- No existe un ciclo funcional posterior activo.
- El SHA documental definitivo se verifica por los refs vigentes `main` y `stable`, que deben coincidir tras la certificación del cierre.

## Resultado v5.31

La auditoría posterior a v5.30 determinó que el problema ya no era falta de profundidad, sino carga cognitiva por exposición simultánea de capas decisionales.

En las 16 fichas:
- v5.8 + v5.30 siguen abiertas como primer grupo;
- pregunta ejecutiva + resultado empresarial forman el segundo grupo abierto;
- v5.22 permanece completo en el DOM bajo `<details>/<summary>` nativo cerrado por defecto.

En las 6 rutas de necesidad:
- permanecen abiertos hero, señales, encaje, decisiones, modalidad, honorarios, resultado, límites y CTA;
- solo objeciones, FAQ, rutas relacionadas y prueba/contexto pasan a divulgación progresiva.

No se reescribieron catálogos ni se eliminaron copy, límites, alternativas, evidencia u honorarios aprobados.

## Evidencia funcional

- PRs del ciclo: `#137` a `#141`.
- Builder final #161: `32059316508` — PASS, 30 pasos.
- SHA funcional final: `159be8a9e467a303faa8d302bfac93b33c2e7b29`.
- Site Quality and Deploy #383: `32059355395` — PASS.
- Idempotencia / segunda pasada: PASS.
- Validaciones estáticas: 37/37 — PASS.
- GitHub Pages + smoke: PASS.
- Browser E2E/axe: **112 observados · 110 PASS · 2 SKIP · 0 FAIL · 0 reintentos**; axe sin violaciones serias/críticas en las superficies cubiertas.
- Lighthouse: PASS con budgets existentes.
- Promoción de `stable`: PASS.
- Graphify #314: PASS sobre el mismo SHA funcional; 800 nodos, 1.368 relaciones, 106 notas wiki y 16 specs E2E.
- Budgets relajados: no.
- Tests eliminados: no.

## Gates que endurecieron el sistema

- #379 detectó que el canal candidate degradaba erróneamente la portada a “Web demostrativa”; se corrigió `sync_public_version.py` para separar estado de release de capability pública.
- #380 detectó una contradicción histórica en `validate_visual_assets.py`; se alineó con la verdad v5.0: portada pública, componentes demo demostrativos.
- #381 y #382 detectaron pruebas históricas que asumían visibilidad permanente o selectores ambiguos; se actualizaron para exigir cerrado por defecto, apertura explícita por usuario y conservación posterior del mismo contenido/telemetría. No se redujo cobertura ni se cambió la UX para satisfacer tests.

## Invariantes preservadas

46 HTML; 16 fichas profundas; un único formulario físico; WhatsApp manual; portal real deshabilitado; funnel sin PII/persistencia; no inferir conversión; no tarifas inventadas; no ocultar profundidad con CSS/hidden; exactamente 30 pasos canónicos; axe/Lighthouse sin relajación; `stable` solo después de gates verdes.

## Estado del ciclo

**v5.31 está implementada, publicada y certificada funcionalmente. No hay una release funcional posterior activa. El cierre documental queda definitivo cuando el commit de esta memoria atraviese los mismos gates y `main = stable`.**

# Meridiano Legal — Estado canónico

Última verificación: 2026-08-18.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **6.1.0 — Measurement Readiness / observabilidad privacy-first**.
- SHA funcional certificado: `8ffe0e923fc626281870ca2bd38d6c55a665b31b`.
- Canal de cierre: `github-pages-production-measurement-readiness-certified`.
- La referencia documental definitiva se verifica por los refs vigentes `main` y `stable`, que deben coincidir tras la certificación de este cierre.
- No existe un ciclo funcional posterior activo; el frente vigente es únicamente cerrar documentalmente v6.1.0.

## Resultado v6.1

v6.1 convierte la observabilidad local ya existente en una arquitectura de **measurement readiness** gobernada, sin activar analítica externa.

La release preserva Experience System v6 y añade un firewall de medición:

- fuente externa única: `meridiano:funnel-v529`;
- campo aceptado: `stage`;
- `event` y `target` ignorados;
- raw `adapter.track(name,event)` conservado por compatibilidad pero `no-op`;
- seis etapas allowlisted: need, offer, evidence, decision, contact y handoff;
- payload custom de Meridiano limitado al nombre del evento, sin propiedades custom;
- deduplicación por primera etapa/página;
- Plausible preparado, pero deshabilitado y sin identificador real;
- pageviews automáticos deshabilitados;
- revisión de metadata estándar del proveedor y actualización de política/configuración obligatorias antes de activar.

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
- 43 superficies con telemetría previa reciben el adapter v6.1.
- `404.html`, `demo.html` y `experiencia.html` permanecen sin adapter.
- WhatsApp sigue siendo handoff manual.
- Portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados.
- `analytics.enabled=false`, `provider=none`, `site_id=""`.

## Evidencia funcional

- SHA funcional certificado: `8ffe0e923fc626281870ca2bd38d6c55a665b31b`.
- `stable` fue promovido automáticamente a ese SHA después de la cadena post-deploy.
- GitHub Pages sirve v6.1.0 con measurement adapter materializado y analytics externa deshabilitada.
- Browser E2E + axe: PASS.
- Lighthouse: PASS con budgets existentes.
- V6 Candidate: PASS.
- Measurement Readiness gate: PASS.
- Canonical Equivalence: PASS.
- Release Governance: PASS.
- Graphify: PASS en los SHAs de candidato/hotfix aplicables.
- Primera materialización v6.1: 43 superficies exactas; 3 exclusiones preservadas.
- Segunda pasada canónica: idempotente.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para hacer pasar la release: no.

## Release engineering endurecido durante v6.1

1. **Measurement como migración determinista.** Canonical Equivalence pasó a distinguir una baseline v6.0 de una baseline v6.1 ya materializada y a comprobar el conjunto exacto de superficies esperado.
2. **Sincronización completa de release.** `sync_public_version.py` evolucionó a una fuente única para etiquetas de versión, `runtime-config.js`, `site-status.json`, sitemap y metadata editorial de modificación; `--check` detecta drift sin escribir.
3. **Paridad de versión en gates.** Candidate, Browser, Measurement y Equivalence reproducen la sincronización antes de validar una baseline v6.
4. **Sitemap.** Todos los `lastmod` se sincronizan con `version.json.release_date`, preservando el contrato v4.8.
5. **Perspectivas.** `article:modified_time` y `dateModified` se sincronizan con la fecha de release, sin alterar `datePublished`, preservando v5.3.
6. **Payload de privacidad.** La telemetría raw no se exporta; el adapter escucha solo la etapa saneada y el payload custom queda sin propiedades.
7. **Pageviews automáticos.** Plausible queda preparado con `autoCapturePageviews:false`; cualquier metadata estándar del proveedor queda sujeta a revisión previa.
8. **Carrera de concurrencia de Pages.** Los workflow_run originados por el commit canónico `build:` quedan aislados en `ignored-build-output` para no cancelar una release válida.
9. **YAML de concurrencia.** La primera corrección de concurrencia introdujo un scalar YAML ambiguo por el literal `build:`; se detectó y corrigió envolviendo el valor dinámico completo entre comillas dobles. El validator exige esa forma para impedir regresión.

## PRs principales

- #154 — Measurement Readiness v6.1, privacy firewall, release metadata parity y gates.
- #155 — aislamiento de la carrera de concurrencia Pages/build-output.
- #156 — corrección YAML quoted del `concurrency.group` y guard correspondiente.

## Invariantes preservadas

46 HTML; 16 fichas profundas; un único formulario físico; WhatsApp manual; portal real deshabilitado; analytics externa deshabilitada; no PII ni propiedades custom exportadas; no inferir conversión; no tarifas inventadas; no ocultar profundidad material; exactamente 30 pasos canónicos; axe/Lighthouse sin relajación; `stable` solo después de gates verdes.

## Estado del ciclo

**v6.1.0 está implementada, publicada y certificada funcionalmente. No hay una release funcional posterior activa. El cierre documental queda definitivo cuando el commit que actualiza esta memoria y marca el canal como `certified` atraviese nuevamente Builder, Pages, smoke, Browser/axe, Lighthouse, release-health y termine con `main == stable`.**

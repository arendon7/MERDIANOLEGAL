# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **6.2.0 — Search Discovery Readiness / indexación verificable**.
- SHA funcional certificado: `4027b6a5425a13cdd0134799c88081e08ac80b6f`.
- Canal de cierre: `github-pages-production-search-discovery-readiness-certified`.
- 46/46 HTML clasificados: 43 indexables + 3 `noindex` (`404.html`, `demo.html`, `experiencia.html`).
- Las 43 páginas indexables declaran exactamente un canonical autorreferencial.
- Sitemap: 43 `<loc>`, sin `lastmod`, `priority` ni `changefreq` no sustentados.
- Search Console permanece **sin configurar**: no hay token auténtico y runtime publica `searchConsoleConfigured=false`.
- Analítica externa permanece deshabilitada: `analytics.enabled=false`, `provider=none`, `site_id=""`.
- Browser E2E + axe: PASS en el candidato v6.2.
- Lighthouse post-deploy: PASS con budgets existentes antes de promoción automática de `stable`.
- 16/16 fichas, 1/1 formulario físico y 30/30 pasos históricos preservados.
- Portal real deshabilitado; WhatsApp continúa como handoff manual.
- Para la referencia documental definitiva, verificar `main` y `stable`; deben coincidir después del cierre.

## Qué cambió en v6.2

v6.2 hace que discovery sea una propiedad verificable del repositorio, sin convertir readiness en una afirmación falsa de propiedad o posicionamiento.

- Nuevo contrato: `assets/data/v6/search-discovery-readiness-v62.json`.
- Nuevo normalizador: `scripts/apply_search_discovery_v62.py`.
- Nuevo validator: `scripts/validate_search_discovery_v62.py`.
- El sitemap se deriva de las páginas indexables y sus canonicals reales.
- Cada página indexable debe tener exactamente un canonical autorreferencial.
- Las tres superficies `noindex` quedan fuera del sitemap.
- La configuración de Search Console es fail-closed: token vacío => sin meta Google y runtime `false`.
- Una futura verificación real solo requiere aportar un token auténtico a la configuración gobernada; no exige rehacer la arquitectura.

## Release engineering v6.2

- Discovery se integra mediante `normalize_experience_compat_v60.py`; no existe paso histórico 31.
- `sync_public_version.py` deja de presentar la fecha global de release como `lastmod` cuando el contrato v6.2 existe.
- v4.8 mantiene comportamiento legacy para baselines anteriores y valida sitemap mínimo en v6.2.
- v5.1 conserva las siete URLs de soluciones y deja de depender del marcador físico histórico de sitemap cuando v6.2 gobierna el output.
- Canonical Equivalence exige el conjunto exacto de measurement/release/discovery drift aplicable.
- Search Discovery gate exige boundary exacto e idempotencia.
- Builder vigila el materializador v6.2; Candidate y Browser vigilan `site-config.json`, sitemap, robots y discovery.
- E2E v6.2 valida coherencia runtime/meta de Google y frontera sitemap 43/3.
- `stable` solo se mueve después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Source-of-truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `assets/data/v6/search-discovery-readiness-v62.json`: contrato de discovery/search verification.
- `assets/data/v6/measurement-readiness-v61.json`: contrato privacy-first de measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `growth-solutions-v51.json` y `cro-solutions-v52.json`: truth de rutas por situación.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar tarifas o descuentos no aprobados;
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

No existe un ciclo funcional posterior que deba abrirse por inercia. El siguiente paso de Search Console requiere una propiedad/cuenta Google auténtica y su token de verificación. Sin ese insumo externo, la arquitectura queda preparada y certificada, pero no se afirma verificación real.

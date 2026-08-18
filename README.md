# Meridiano Legal · Web canónica v6.2.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v6.2.0 — Search Discovery Readiness / indexación verificable**.

- SHA funcional certificado: `4027b6a5425a13cdd0134799c88081e08ac80b6f`.
- Canal certificado: `github-pages-production-search-discovery-readiness-certified`.
- 46 HTML públicos, 16 fichas profundas y 1 formulario físico canónico.
- 43 páginas indexables con canonical autorreferencial único.
- 3 superficies `noindex` fuera del sitemap: `404.html`, `demo.html`, `experiencia.html`.
- Sitemap canónico mínimo con 43 `<loc>` y sin `lastmod`, `priority` ni `changefreq` no sustentados.
- Search Console: **readiness únicamente**; `searchConsoleConfigured=false` y no existe token de verificación publicado.
- Analítica externa: **deshabilitada**; `analytics.enabled=false`, `provider=none`, `site_id=""`.
- 30 pasos históricos exactos del builder; sin paso 31.
- Browser E2E + axe sobre el candidato v6.2: PASS.
- Lighthouse post-deploy: PASS con budgets existentes antes de la promoción automática de `stable`.
- Cobertura reducida: no. Budgets relajados: no.
- El SHA documental definitivo se determina por los refs `main` y `stable` al terminar el cierre.

## v6.2 — Search Discovery Readiness

v6.2 convierte la indexación pública en un contrato verificable sin afirmar una propiedad de Google que todavía no existe.

La release:

- clasifica las 46 superficies públicas a partir de sus señales reales de indexación;
- exige exactamente un canonical autorreferencial por página indexable;
- deriva el sitemap de esas páginas indexables, en vez de mantener una lista paralela permisiva;
- deja fuera del sitemap las tres superficies `noindex`;
- elimina `priority` y `changefreq`, que no forman parte del contrato canónico v6.2;
- deja de usar la fecha global de release como `lastmod` de todas las URLs cuando no existe evidencia de modificación material por página;
- prepara verificación de Google Search Console mediante meta HTML gobernada por `site-config.json.search_console_verification`;
- falla de forma cerrada: token vacío significa ausencia de meta y `searchConsoleConfigured=false`;
- no inventa token, cuenta, propiedad, ranking, tráfico ni evidencia de posicionamiento.

## Search Console: preparado, no activado

La configuración productiva conserva `search_console_verification=""`. Por tanto:

- no se publica `google-site-verification`;
- runtime declara `searchConsoleConfigured=false`;
- no se afirma que Google haya verificado la propiedad;
- no se envía el sitemap desde una cuenta de Search Console no conectada;
- una futura activación requerirá un token auténtico emitido para la propiedad correspondiente y otra certificación completa.

## Privacidad y capability truth

v6.2 no modifica el firewall de medición v6.1. Producción mantiene:

- analytics externa deshabilitada;
- sin PII ni contenido del formulario exportados;
- un único formulario físico canónico;
- WhatsApp como handoff manual;
- portal real, auth, CRM, pagos, firma, agenda y upload deshabilitados/no implementados;
- ningún evento equivalente automáticamente a cliente convertido.

## Release engineering v6.2

El ciclo endureció discovery y publicación sin cambiar los 30 pasos históricos:

- `apply_search_discovery_v62.py` materializa sitemap/meta de verificación de forma determinista y ofrece `--check` fail-closed;
- `validate_search_discovery_v62.py` valida 46/43/3, canonicals, sitemap, robots y coherencia del token/runtime;
- la integración ocurre dentro de `normalize_experience_compat_v60.py`, la extensión canónica v6 existente;
- `sync_public_version.py` conserva semántica legacy del sitemap en baselines anteriores y cede su gobierno a v6.2 cuando existe el nuevo contrato;
- v4.8 y v5.1 evolucionan phase-aware sin eliminar sus propiedades históricas sustantivas;
- Canonical Equivalence exige el conjunto exacto `measurement esperado ∪ release drift ∪ discovery drift` cuando aplica;
- el gate v6.2 prueba boundary exacto y segunda pasada idempotente;
- Builder observa cambios del materializador v6.2 y el validator de topología impide perder esa cobertura;
- Candidate y Browser incluyen sitemap/robots/configuración Search Console en sus contratos;
- el E2E v6.2 comprueba dinámicamente que runtime y meta de verificación nunca diverjan y que el sitemap servido conserve la frontera 43/3;
- `stable` sigue moviéndose únicamente después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Source of truth

- `assets/data/v6/search-discovery-readiness-v62.json`: contrato canónico de discovery y verificación.
- `scripts/apply_search_discovery_v62.py`: normalizador determinista.
- `scripts/validate_search_discovery_v62.py`: validator fail-closed.
- `assets/data/v6/measurement-readiness-v61.json`: contrato privacy-first de measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `catalog-products-v41/` y `catalog-services-v42/`: truth jurídica/comercial de las 16 ofertas.
- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.

## Documentación

- `RELEASE-v6.2.md`: alcance, discovery, incidencias y evidencia del cierre v6.2.
- `RELEASE-v6.1.md`: cierre histórico de Measurement Readiness.
- `RELEASE-v6.0.md`: cierre histórico del Experience System.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md`: contexto operativo actual.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico y certificación.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: frente vigente.

El cierre documental v6.2 queda definitivo únicamente cuando este commit de certificación atraviese nuevamente Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y termine con `main == stable`.

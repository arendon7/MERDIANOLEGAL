# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado base certificado

- Release certificada de partida: **v6.1.0 — Measurement Readiness / observabilidad privacy-first**.
- `main == stable == 5a44596e6e44cda44e77bfd60a039bded753e01a` al abrir este ciclo.
- Canal base: `github-pages-production-measurement-readiness-certified`.
- Analytics externa permanece deshabilitada: `enabled=false`, `provider=none`, `site_id=""`.
- Search Console permanece sin configurar: no existe token auténtico en `site-config.json` y runtime publica `searchConsoleConfigured=false`.
- 46 HTML, 16 fichas profundas, un único formulario físico y 30 pasos históricos del builder permanecen como invariantes.

## Ciclo funcional activo

**v6.2.0 — Search Discovery Readiness / indexación verificable.**

Rama: `feat/v62-search-discovery-readiness`.
PR: `#158` (Draft hasta certificación same-SHA).
Release candidate: `version.json = 6.2.0`, fecha `2026-08-18`, canal `github-pages-search-discovery-readiness-candidate`.

### Problema observable

La web ya tenía canonicals, robots y sitemap, pero dos aspectos impedían considerar discovery como un contrato preciso:

1. Google Search Console no está verificado/configurado y no existe un token auténtico que permita afirmarlo.
2. El sitemap heredado sincronizaba `lastmod` de todas las URLs con la fecha global de release y conservaba `priority/changefreq`, aunque una release técnica no demuestra por sí sola una modificación material de cada página.

v6.2 corrige la semántica sin inventar propiedad sobre Google ni alterar contenido jurídico/comercial.

## Alcance v6.2

1. contrato `assets/data/v6/search-discovery-readiness-v62.json`;
2. estado explícito `readiness-not-verified`;
3. proveedor de verificación previsto: Google Search Console, propiedad URL-prefix;
4. método preparado: meta HTML gobernada por `site-config.json.search_console_verification`;
5. token auténtico obligatorio; token vacío implica ausencia total de meta de verificación y `searchConsoleConfigured=false`;
6. clasificación exacta de las 46 superficies públicas;
7. **43 páginas indexables** con exactamente un canonical autorreferencial;
8. **3 páginas `noindex`** fuera del sitemap: `404.html`, `demo.html`, `experiencia.html`;
9. sitemap determinista derivado de los canonicals indexables;
10. sitemap mínimo: solo `<loc>`, sin `priority`, `changefreq` ni `lastmod` global no demostrable;
11. `robots.txt` conserva una única referencia al sitemap canónico y la exclusión explícita de demo;
12. normalizador `scripts/apply_search_discovery_v62.py` con modo `--check` fail-closed;
13. validator `scripts/validate_search_discovery_v62.py` para frontera 43/3, canonicals, sitemap, robots y coherencia de verificación;
14. integración a través de `normalize_experience_compat_v60.py`, sin crear un paso histórico 31;
15. `sync_public_version.py` conserva el comportamiento sitemap legacy cuando v6.2 no existe y deja de poseer el sitemap cuando el contrato v6.2 está presente;
16. v4.8 y v5.1 evolucionan phase-aware sin eliminar sus controles históricos;
17. Canonical Equivalence exige `diff real = measurement esperado ∪ release drift ∪ discovery drift` según corresponda;
18. gate dedicado `.github/workflows/v62-search-discovery-readiness.yml` exige boundary exacto e idempotencia;
19. Builder observa cambios futuros de `scripts/apply_search_discovery_v62.py` y su validator de topología lo exige;
20. Candidate incluye sitemap/robots en la prueba de idempotencia;
21. Browser Candidate observa `site-config.json`, sitemap, robots y scripts v6.2;
22. E2E `search-discovery-v62.spec.mjs` verifica dinámicamente coherencia entre runtime y meta de Search Console, además de la frontera sitemap 43/3.

## Criterios de éxito

- ninguna meta `google-site-verification` mientras el token canónico esté vacío;
- no afirmar Search Console configurado sin token auténtico;
- 46/46 HTML clasificados;
- 43/43 indexables con canonical autorreferencial único;
- 3/3 noindex fuera del sitemap;
- sitemap con exactamente 43 `<loc>` y sin `lastmod`, `priority` o `changefreq` no sustentados;
- `robots.txt` conserva el sitemap canónico;
- la primera materialización modifica únicamente el conjunto exacto declarado por release metadata + discovery;
- segunda pasada idempotente;
- 46 HTML, 16 fichas, un formulario y 30 pasos históricos intactos;
- analytics externa continúa deshabilitada;
- Browser/axe, Measurement, Candidate, Search Discovery, Equivalence, Governance y Graphify verdes sobre el mismo SHA;
- después del merge, Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot debe promover `stable` automáticamente.

## Fuera de alcance de esta fase

- inventar o publicar un token de Google;
- afirmar que la propiedad ya fue verificada en Search Console;
- crear o controlar una cuenta de Google sin credenciales/decisión explícita;
- enviar sitemaps a Search Console desde una cuenta no conectada;
- activar Plausible u otro proveedor de analytics;
- cambiar copy, servicios, productos, precios, layout o funnel por intuición;
- convertir discovery readiness en una promesa de ranking o tráfico.

## Condición para verificación real posterior

Una activación real de Search Console requerirá:

1. propiedad/cuenta Google auténtica;
2. token de verificación generado por Google para la URL-prefix correspondiente;
3. incorporación del token en `site-config.json` sin exponer credenciales adicionales;
4. materialización de una única meta en Home;
5. Browser/Candidate/Search Discovery/Equivalence verdes;
6. despliegue productivo certificado;
7. verificación efectiva en Search Console y, posteriormente, envío/lectura del sitemap desde la propiedad verificada.

Hasta entonces, v6.2 es **Search Discovery Readiness**, no Search Console activa ni evidencia de posicionamiento.

# Meridiano Legal — Estado canónico

Última verificación: 2026-08-18.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot certificado: `stable`.
- Release funcional certificada: **6.2.0 — Search Discovery Readiness / indexación verificable**.
- SHA funcional certificado: `4027b6a5425a13cdd0134799c88081e08ac80b6f`.
- Canal de cierre: `github-pages-production-search-discovery-readiness-certified`.
- La referencia documental definitiva se obtiene por los refs vigentes `main` y `stable`, que deben coincidir tras este cierre.

## Resultado v6.2

v6.2 convierte las señales de discovery en un contrato determinista sin afirmar Search Console activa ni resultados de posicionamiento.

### Frontera de indexación

- 46/46 HTML públicos clasificados.
- 43/43 páginas indexables con exactamente un canonical autorreferencial.
- 3/3 superficies `noindex`: `404.html`, `demo.html`, `experiencia.html`.
- Las tres superficies `noindex` están fuera del sitemap.
- Sitemap canónico con exactamente 43 `<loc>`.
- Sin `priority` ni `changefreq`.
- Sin `lastmod` global derivado simplemente de `version.json.release_date`.
- `robots.txt` conserva una única referencia al sitemap canónico y la exclusión explícita de demo.

### Search Console

- Estado: **readiness-not-verified**.
- Método preparado: meta HTML para propiedad URL-prefix.
- Fuente gobernada: `site-config.json.search_console_verification`.
- Token actual: vacío.
- Meta `google-site-verification`: ausente mientras el token esté vacío.
- Runtime: `searchConsoleConfigured=false`.
- No existe afirmación de propiedad verificada ni envío autenticado de sitemap desde Search Console.

### Measurement/capability truth preservado

- `analytics.enabled=false`.
- `provider=none`.
- `site_id=""`.
- 43 superficies continúan con measurement adapter v6.1; `404`, `demo` y `experiencia` continúan fuera de esa instrumentación.
- 16/16 fichas profundas.
- 1/1 formulario físico canónico.
- WhatsApp manual.
- Portal real, auth, CRM, pagos, firma, agenda y upload: deshabilitados/no implementados.
- 30/30 pasos históricos exactos del builder.

## Evidencia funcional

- Candidate v6.2 same-SHA: `d14b0356aa2733645061f7230b7cc044f09cd42f`.
- Siete gates pre-merge sobre ese SHA: PASS:
  - V6.2 Search Discovery Readiness;
  - V6 Candidate Validation;
  - V6 Canonical Builder Equivalence;
  - Release Governance;
  - Graphify;
  - V6 Browser Candidate / axe;
  - V6.1 Measurement Readiness / Browser E2E.
- PR #158 fusionado sin incluir HTML generado ni sitemap materializado en el diff fuente.
- Builder post-merge materializó el snapshot `4027b6a5425a13cdd0134799c88081e08ac80b6f`.
- `stable` fue promovido automáticamente a `4027b6a5…` tras la cadena post-deploy.
- Browser/axe y Lighthouse productivos son prerequisitos del job que mueve `stable`; no se hizo promoción manual.
- Cobertura reducida: no.
- Budgets relajados: no.
- Tests eliminados para aprobar la release: no.

## Release engineering endurecido durante v6.2

1. **Sitemap derivado del canonical.** El sitemap deja de ser una lista mantenida de forma independiente y se genera desde las páginas realmente indexables y sus canonicals autorreferenciales.
2. **Señales temporales honestas.** `sync_public_version.py` conserva `lastmod` histórico en baselines anteriores, pero cede el gobierno del sitemap a v6.2. Una fecha global de release ya no se presenta como prueba de modificación material de cada URL.
3. **Verification fail-closed.** El token vacío conserva Home byte-stable y prohíbe publicar una meta Google o runtime `true`. Un token futuro debe producir exactamente una meta no vacía.
4. **Boundary real 43/3.** El primer gate reveló que `experiencia.html` también es `noindex`; el contrato se corrigió para reflejar la verdad existente, no para forzar una página al índice.
5. **No drift cosmético.** El normalizador dejó de reescribir espacios/saltos de Home cuando no existe token.
6. **v4.8 phase-aware.** Legacy conserva su contrato de `lastmod`; v6.2 exige sitemap mínimo sin `lastmod`, `priority` ni `changefreq`.
7. **v5.1 phase-aware.** Las siete URLs de soluciones siguen siendo obligatorias, pero el output v6.2 ya no depende del antiguo comentario gestionado `GROWTH-V51-SITEMAP`.
8. **Source vs output.** Governance puede validar una fuente pre-materialización que aún contiene el marcador histórico; el normalizador/validator v6.2 son quienes exigen su eliminación en el output canónico.
9. **Equivalencia exacta.** El conjunto de cambios esperado es measurement aplicable ∪ release drift ∪ discovery drift declarado; cualquier archivo extra falla.
10. **Trigger coverage.** Builder vigila el materializador discovery; Candidate y Browser vigilan configuración, sitemap, robots y scripts v6.2.
11. **E2E dinámico.** La suite no codifica un token: infiere la expectativa desde runtime y comprueba meta Search Console + sitemap servido 43/3.

## PR principal

- #158 — Search Discovery Readiness v6.2: contrato, normalizador, validator, sitemap/canonical topology, Search Console fail-closed, gates y E2E.

## Invariantes preservadas

46 HTML; 16 fichas profundas; 1 formulario físico; WhatsApp manual; portal real deshabilitado; analytics externa deshabilitada; Search Console no verificada sin token real; no PII; no inferir conversión; no inventar rankings ni tráfico; no tarifas inventadas; exactamente 30 pasos históricos; Browser/axe/Lighthouse sin relajación; `stable` solo después de gates verdes.

## Estado del ciclo

**v6.2.0 está implementada, materializada, publicada y certificada funcionalmente. No hay una release funcional posterior activa. El cierre documental queda definitivo cuando el commit que actualiza esta memoria y marca el canal como `certified` atraviese nuevamente Builder, Pages, smoke, Browser/axe, Lighthouse y termine con `main == stable`.**

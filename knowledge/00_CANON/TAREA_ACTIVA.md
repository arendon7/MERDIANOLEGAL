# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Release vigente

**v6.2.0 — Search Discovery Readiness / indexación verificable**.

- SHA funcional certificado: `4027b6a5425a13cdd0134799c88081e08ac80b6f`.
- Canal de cierre: `github-pages-production-search-discovery-readiness-certified`.
- 46 HTML clasificados: 43 indexables + 3 `noindex` (`404.html`, `demo.html`, `experiencia.html`).
- Sitemap canónico: 43 `<loc>`, sin `lastmod`, `priority` ni `changefreq` no sustentados.
- Search Console: no configurado; no existe token auténtico y runtime conserva `searchConsoleConfigured=false`.
- Analytics externa: deshabilitada (`enabled=false`, `provider=none`, `site_id=""`).
- 16 fichas profundas, 1 formulario físico y 30 pasos históricos preservados.

## Estado del ciclo

El frente funcional v6.2 quedó completado y certificado. PR #158 fue fusionado después de **7/7 gates same-SHA verdes** y el builder materializó el snapshot público `4027b6a5…`; `stable` alcanzó automáticamente ese mismo SHA después de Pages/Browser/Lighthouse.

La única tarea vigente es **cerrar documentalmente v6.2**: README, memoria canónica, `RELEASE-v6.2.md` y canal `certified`. Ese cierre también debe atravesar la cadena completa y terminar con `main == stable`.

## Qué quedó preparado

1. contrato `assets/data/v6/search-discovery-readiness-v62.json` en estado `readiness-not-verified`;
2. 43 páginas indexables con canonical autorreferencial único;
3. 3 superficies noindex fuera del sitemap;
4. sitemap determinista derivado de canonicals indexables;
5. ausencia de señales no sustentadas `lastmod`, `priority`, `changefreq`;
6. verificación Search Console gobernada por `site-config.json.search_console_verification`;
7. token vacío => ninguna meta Google + runtime `searchConsoleConfigured=false`;
8. normalizador y validator fail-closed;
9. Builder, Candidate, Browser, Equivalence y gate v6.2 con cobertura de cambios futuros;
10. E2E dinámico de Search Console/sitemap.

## No hacer por inercia

No abrir una v6.3 ni activar servicios externos solo para continuar el versionado. No inventar un token Google, propiedad, cuenta, tráfico, ranking, impresiones o clics. No activar analytics ni cambiar la política de privacidad sin una decisión explícita y evidencia real.

## Próximo paso externo posible

La siguiente acción material de Search Console requiere un **token auténtico emitido por Google para la propiedad correspondiente**. Cuando exista:

1. incorporarlo únicamente en `site-config.json.search_console_verification`;
2. comprobar que se materialice una sola meta `google-site-verification`;
3. exigir runtime `searchConsoleConfigured=true`;
4. ejecutar Search Discovery + Candidate + Browser + Equivalence + Governance;
5. publicar por Builder/Pages y promover `stable` únicamente después de Browser/Lighthouse;
6. completar la verificación en la cuenta Google correspondiente y, solo entonces, tratar Search Console como configurado externamente.

Hasta recibir ese insumo, **no existe un nuevo ciclo funcional activo**.

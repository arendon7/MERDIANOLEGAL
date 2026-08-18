# Meridiano Legal · Web canónica v6.3.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v6.3.0 — Engagement Clarity / claridad precontratación**.

- SHA funcional certificado: `118cee5030f27689d91172beb525d7d92c751117`.
- Canal certificado: `github-pages-production-engagement-clarity-certified`.
- 46 HTML públicos, 16 fichas profundas y 1 formulario físico canónico.
- Las 16 fichas elevan a primer nivel dos matrices jurídicas/comerciales ya aprobadas: `requirements` y `responsibilities`.
- Cada ficha incorpora un único hito `Para empezar` y una única sección `#v6-engagement` antes de Límites.
- La navegación ejecutiva v6.3 conserva exactamente 7 hitos; v4.6 permanece phase-aware y estricto.
- Search Console continúa sin configurar: `searchConsoleConfigured=false`, sin token auténtico.
- Analítica externa continúa deshabilitada: `analytics.enabled=false`, `provider=none`, `site_id=""`.
- 43 páginas indexables y 3 superficies `noindex` preservadas desde v6.2.
- 30 pasos históricos exactos del builder; sin paso 31.
- Browser E2E + axe: PASS.
- Lighthouse post-deploy: PASS con los budgets existentes antes de la promoción automática de `stable`.
- Cobertura reducida: no. Budgets relajados: no.
- El SHA documental definitivo se determina por los refs `main` y `stable` una vez este cierre vuelva a atravesar la cadena productiva.

## v6.3 — Engagement Clarity

v6.3 reduce fricción antes de solicitar una propuesta sin crear obligaciones jurídicas nuevas. La mejora parte de una verdad que ya existía en los 16 catálogos canónicos, pero permanecía relegada a la profundidad histórica de cada ficha.

La release hace visible, para cada producto y servicio:

- **qué debe estar listo del lado del cliente**, derivado exactamente de `requirements`;
- **cómo se distribuyen las responsabilidades**, derivado exactamente de `responsibilities`;
- una entrada ejecutiva `Para empezar` dentro de la navegación de la ficha;
- una sección `#v6-engagement` situada entre Proceso y Límites.

La capa de presentación no modifica entregables, perímetro, método, límites, honorarios, cronogramas, contacto ni capability truth. Si cambia una fila de `requirements` o `responsibilities` en los catálogos canónicos, el validator exige que la representación pública se sincronice exactamente.

## Verdad jurídica y comercial

La fuente permanece en:

- `catalog-products-v41/*.json` para los 8 productos;
- `catalog-services-v42/*.json` para los 8 servicios.

`validate_engagement_clarity_v63.py` compara fila por fila las matrices visibles contra esas fuentes. No existe una segunda copia editorial intermedia que pueda divergir silenciosamente.

Esto permite que una ficha explique no solo **qué recibe** la empresa, sino también **qué necesita aportar** y **quién responde por cada frente**, antes del contacto comercial.

## Release engineering v6.3

El ciclo añadió Engagement Clarity como extensión de la arquitectura v6 existente, sin modificar los 30 pasos históricos:

- `apply_engagement_clarity_v63.py` materializa las 16 fichas de forma determinista y ofrece `--check` fail-closed;
- `validate_engagement_clarity_v63.py` exige 8 productos + 8 servicios, truth exacto, navegación única y orden de secciones;
- `normalize_experience_compat_v60.py` integra la extensión junto a Measurement v6.1 y Search Discovery v6.2;
- el gate dedicado v6.3 distingue de forma estricta una baseline pre-materializada `0/16` de una baseline certificada `16/16`; cualquier estado parcial falla;
- durante la transición inicial exige exactamente 16 HTML de engagement; una baseline ya materializada exige drift cero;
- Canonical Equivalence exige el conjunto exacto `measurement ∪ release ∪ discovery ∪ engagement` cuando aplica;
- v4.6 conserva exactamente 6 hitos sin v6.3 y exige exactamente 7 con v6.3, incluido `#v6-engagement`;
- Builder, Candidate y Browser observan expresamente el materializador/validator v6.3;
- `validate_pages_trigger_v511.py` bloquea la pérdida de cobertura del materializador en Builder;
- E2E visita las 16 fichas y verifica navegación real en una ficha de producto y una de servicio;
- la hoja v6.3 se ubica en una posición estable respecto del bloque CSS v6.0 para preservar idempotencia byte-equivalent;
- `stable` continúa moviéndose únicamente después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Discovery, privacidad y capability truth preservados

v6.3 no altera las garantías de v6.1/v6.2:

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

- `assets/data/v6/engagement-clarity-v63.json`: contrato v6.3.
- `scripts/apply_engagement_clarity_v63.py`: materializador determinista.
- `scripts/validate_engagement_clarity_v63.py`: validator contra truth canónico.
- `catalog-products-v41/` y `catalog-services-v42/`: verdad jurídica/comercial de las 16 ofertas.
- `assets/data/v6/search-discovery-readiness-v62.json`: contrato de discovery.
- `assets/data/v6/measurement-readiness-v61.json`: contrato privacy-first de measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.

## Documentación

- `RELEASE-v6.3.md`: alcance, evidencia e incidencias del cierre v6.3.
- `RELEASE-v6.2.md`: cierre histórico de Search Discovery Readiness.
- `RELEASE-v6.1.md`: cierre histórico de Measurement Readiness.
- `RELEASE-v6.0.md`: cierre histórico del Experience System.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md`: contexto operativo actual.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico y certificación.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: frente vigente.

El cierre documental v6.3 queda definitivo únicamente cuando este commit de certificación atraviese nuevamente Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y termine con `main == stable`.

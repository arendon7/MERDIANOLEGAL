# Meridiano Legal · Web canónica v5.22.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages.

URL pública: `https://arendon7.github.io/MERDIANOLEGAL/`

## Estado actual

La publicación conserva 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico. `stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

Release funcional certificada y cerrada: **v5.22.0**.

- SHA funcional de las mejoras: `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2` — run `31671834728`.
- Snapshot público final `ready`: `dcb5bc9643eff595c0f8614c7cf6acbadc3bb719` — run `31673266141`.
- Canal: `github-pages-public-offer-narrative-ready`.

El primer SHA identifica el cierre funcional de narrativa/productos/servicios. El segundo incorpora el cierre documental/metadata `ready` y volvió a superar todos los gates antes de mover `stable`.

## Capas vigentes

- **v5.8:** claridad de compra;
- **v5.9:** calificación comercial y privacidad;
- **v5.10:** intención contextual, propuesta y cierre;
- **v5.11:** solicitud, propuesta, aceptación e inicio;
- **v5.12:** modalidades y prueba verificable;
- **v5.13:** continuidad hasta formulario/WhatsApp;
- **v5.14:** recomendación explicable sin scoring;
- **v5.15:** recomendación→acción;
- **v5.16:** UX móvil y accesibilidad;
- **v5.17:** continuidad manual del handoff y stale protection;
- **v5.18:** observabilidad verificable del handoff sin PII;
- **v5.19:** progressive disclosure por intención explícita;
- **v5.20:** compresión de la decisión comercial en portada;
- **v5.21:** frontera verificable entre demo y capacidades reales;
- **v5.22:** arquitectura editorial de oferta y narrativa jurídica senior.

## v5.22 · Oferta más clara sin perder profundidad

v5.22 integra las mejores capas históricas de narrativa con el catálogo profundo v4.1/v4.2. No añade ofertas: hace más fácil entender qué decisión compra la empresa, por qué conviene una modalidad y no otra, qué criterio jurídico gobierna el trabajo y qué queda instalado al cierre.

Cada una de las 16 fichas incorpora una capa editorial source-driven con:

1. decisión empresarial;
2. por qué esta modalidad;
3. alternativa cercana;
4. lente jurídica;
5. capacidad instalada.

La diferenciación es explícita en cinco pares: diagnóstico/auditoría, contrato puntual/sistema contractual, PI, IA y proyectos regulados.

La portada conserva una sola arquitectura de decisión v5.20 y refuerza la tesis de Meridiano: el valor no está en producir respuestas aisladas, sino en convertir criterio jurídico en decisiones, instrumentos, responsables y acciones verificables.

## Veracidad de capacidades

La frontera v5.21 continúa vigente. El portal real de clientes está deshabilitado y la demo sigue siendo ficticia, client-side y `noindex`.

Las fuentes v4.1/v4.2 fueron saneadas para que `Meridiano Empresas` solo aparezca condicionado a una habilitación productiva real o como relación explícitamente demostrativa. El compositor v5.22 no reescribe silenciosamente el contrato fuente después del render.

No se añadieron autenticación, cuentas reales, backend, CRM, almacenamiento servidor, PII, email transaccional, firma electrónica, pagos, agenda ni carga documental.

## Evidencia funcional v5.22

Run `31671834728`, SHA funcional `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`:

- builder + segunda pasada/idempotencia: PASS;
- validadores históricos + v5.22: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 49 observados → 47 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.96–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1367 ms, CLS 0, TBT 55 ms;
- CI hasta `stable`: 206 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 26.2%;
- cobertura reducida: no;
- budgets relajados: no.

## Recertificación pública `ready`

Run `31673266141`, SHA `dcb5bc9643eff595c0f8614c7cf6acbadc3bb719`:

- idempotencia + validadores: PASS;
- Pages + smoke: PASS;
- Browser E2E/axe: PASS;
- Lighthouse: PASS;
- release-health: PASS;
- `stable`: promovida;
- tiempo hasta gate: 204 s;
- mejora frente al baseline: 26.9%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos `ready`:

- Lighthouse `9170555585`;
- CI `9170580133`;
- release-health `9170580558`;
- Pages `9170509163`.

## Arquitectura v5.22

Fuentes y controles principales:

- `offer-narrative-v522.json` — contrato editorial de 16 ofertas;
- `offer-v522.css` — presentación trust-first;
- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica/comercial;
- `scripts/apply_offer_narrative_v522.py` — materialización final idempotente;
- `scripts/validate_offer_narrative_v522.py` — contrato anti-drift;
- `tests/e2e/offer-narrative.spec.mjs` — cobertura Browser de portada y fichas.

El runtime conserva el HTML prerenderizado cuando la ficha declara `data-static-catalog="true"`; no rehidrata destructivamente `#detail-page` con el template legado.

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estática/noindex y pipeline de certificación.

Explícitamente deshabilitada: portal real de clientes.

No declarar activas sin configuración real: autenticación/cuentas reales, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.22.md`: narrativa, catálogo, incidencias y evidencia funcional;
- `RELEASE-v5.21.md`: frontera demo/capacidad;
- `RELEASE-v5.20.md`: compresión de decisión;
- `RELEASE-v5.19.md`: foco comercial adaptativo;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No inferir intención comercial que el usuario no haya declarado.
- No convertir acciones locales en afirmaciones sobre envío, lectura, aceptación o conversión.
- Una demo no equivale a una capacidad productiva.
- El contenido contractual se corrige en la fuente, no mediante mutaciones ocultas post-render.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

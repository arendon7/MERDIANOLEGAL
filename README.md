# Meridiano Legal · Web canónica v6.1.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v6.1.0 — Measurement Readiness / observabilidad privacy-first**.

- SHA funcional certificado: `8ffe0e923fc626281870ca2bd38d6c55a665b31b`.
- Canal certificado: `github-pages-production-measurement-readiness-certified`.
- 46 HTML públicos, 16 fichas profundas y 1 formulario físico canónico.
- 30 pasos exactos del builder canónico; sin paso 31.
- Browser E2E + axe sobre la v6.1 pública: PASS.
- Lighthouse sobre la v6.1 pública: PASS con los budgets existentes.
- Cobertura reducida: no. Budgets relajados: no.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.
- Analítica de terceros: **deshabilitada**; `provider=none`, sin site id real y sin tráfico externo del adapter.
- El SHA documental definitivo se verifica por los refs `main` y `stable` tras la certificación del cierre.

## v6.1 — Measurement Readiness

v6.1 prepara una futura observabilidad agregada del funnel sin convertir la web en un sistema de seguimiento de personas ni activar un proveedor externo.

La release:

- consume únicamente la etapa saneada del evento `meridiano:funnel-v529`;
- acepta seis etapas allowlisted: `need`, `offer`, `evidence`, `decision`, `contact`, `handoff`;
- conserva el hook histórico `MeridianoAnalyticsAdapter.track(name,event)` como `no-op` para no exportar telemetría raw;
- limita el payload custom de Meridiano al **nombre del evento**, sin propiedades custom;
- deduplica la primera emisión de cada etapa durante la vida de la página;
- inserta el adapter en exactamente 43 superficies que ya tenían telemetría;
- preserva `404.html`, `demo.html` y `experiencia.html` sin adapter porque no tenían telemetría previa;
- prepara Plausible como adapter posible, pero sin token real y con `autoCapturePageviews:false`;
- exige revisar la metadata estándar del proveedor y actualizar política/configuración antes de cualquier activación real.

## Privacidad y capability truth

v6.1 **no activa analítica**. Producción conserva:

- `analytics.enabled=false`;
- `provider=none`;
- `site_id=""`;
- sin cookies propias del adapter;
- sin `localStorage` o `sessionStorage` introducidos por measurement;
- sin `fetch`, XHR o `sendBeacon` propios en el adapter;
- sin exportar nombre, empresa, correo, mensaje, referencia, presupuesto, urgencia ni contenido del formulario;
- sin equiparar `contact` o `handoff` con mensaje enviado, propuesta aceptada, encargo iniciado o cliente convertido.

## Release engineering v6.1

El ciclo endureció además la publicación canónica:

- `sync_public_version.py` sincroniza y valida etiquetas de versión, `runtime-config.js`, `site-status.json`, `sitemap.xml` y metadata editorial de modificación;
- `sync_public_version.py --check` falla si existe drift de release;
- Canonical Equivalence compara el conjunto exacto esperado de cambios, no una lista permisiva;
- la transición v6.0→v6.1 materializa exactamente 43 superficies de measurement y preserva las 3 exclusiones;
- segunda pasada canónica: idempotente;
- el workflow Pages separa los `workflow_run` del commit canónico `build:` en un grupo de concurrencia `ignored-build-output`, evitando que una ejecución ignorada cancele una release válida;
- el `concurrency.group` dinámico permanece entre comillas dobles para ser YAML inequívoco y su validator bloquea regresiones;
- `stable` continúa moviéndose únicamente después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Source of truth

- `assets/data/v6/measurement-readiness-v61.json`: contrato de readiness, privacidad, proveedor y límites semánticos.
- `assets/js/v6/analytics-adapter-v61.js`: adapter fail-closed.
- `funnel-contract-v529.json`: límites semánticos y de privacidad del funnel.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `catalog-products-v41/` y `catalog-services-v42/`: truth jurídica/comercial de las 16 ofertas.
- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.

## Documentación

- `RELEASE-v6.1.md`: alcance, privacidad, incidencias y evidencia del cierre v6.1.
- `RELEASE-v6.0.md`: cierre histórico del Experience System.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md`: contexto operativo actual.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico y certificación.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: frente vigente.
- `knowledge/HOME.md`: navegación de memoria.

El cierre documental v6.1 queda definitivo únicamente cuando el commit que contiene esta documentación y el canal `certified` atraviese Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y termine con `main == stable`.

# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **6.1.0 — Measurement Readiness / observabilidad privacy-first**.
- SHA funcional certificado: `8ffe0e923fc626281870ca2bd38d6c55a665b31b`.
- Canal de cierre: `github-pages-production-measurement-readiness-certified`.
- Browser E2E + axe sobre la v6.1 pública: PASS.
- Lighthouse sobre la v6.1 pública: PASS con budgets existentes.
- 46/46 superficies, 16/16 fichas, 1/1 formulario físico y 30/30 pasos canónicos preservados.
- Analítica externa sigue deshabilitada: `analytics.enabled=false`, `provider=none`, `site_id=""`.
- 43 superficies con telemetría previa cargan el adapter v6.1; `404.html`, `demo.html` y `experiencia.html` permanecen sin adapter.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.
- Después del cierre documental no existe un ciclo funcional posterior abierto.
- Para la referencia documental definitiva, verificar los refs vigentes `main` y `stable`; no incrustar un SHA recursivo de cierre en esta nota.

## Qué cambió en v6.1

v6.1 prepara medición agregada futura sin activar un tercero ni transportar telemetría raw.

- Fuente única: evento saneado `meridiano:funnel-v529`.
- Campo aceptado: `detail.stage`.
- `event` y `target` se ignoran.
- `adapter.track(name,event)` histórico permanece como `no-op`.
- Etapas allowlisted: `need`, `offer`, `evidence`, `decision`, `contact`, `handoff`.
- Payload custom de Meridiano: solo nombre del evento; cero propiedades custom.
- Deduplicación: primera emisión de cada etapa durante la vida de la página.
- Plausible: adapter preparado pero deshabilitado; sin site id real; `autoCapturePageviews:false`.
- Cualquier futura activación requiere proveedor/identificador auténticos, revisión de metadata estándar, actualización previa de política/configuración y nueva certificación.

## Release engineering v6.1

- `sync_public_version.py` sincroniza versión visible, runtime/status, sitemap y metadata editorial de modificación; `--check` detecta drift sin escribir.
- Candidate, Browser, Measurement y Canonical Equivalence reproducen la sincronización de release en baseline v6.
- Canonical Equivalence compara el set exacto de cambios esperados y mantiene segunda pasada idempotente.
- El builder conserva exactamente 30 pasos históricos; v6.1 no crea un paso 31.
- Pages aísla los workflow_run del commit canónico `build:` en `ignored-build-output` para que una ejecución ignorada no cancele una release válida.
- El `concurrency.group` dinámico está quoted y `validate_pages_trigger_v511.py` exige esa forma.
- `stable` solo se mueve después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Source-of-truth

- `main`: verdad técnica y documental vigente.
- `stable`: snapshot certificado; debe coincidir con `main` al cierre definitivo.
- `assets/data/v6/measurement-readiness-v61.json`: contrato v6.1 de medición/privacy.
- `assets/js/v6/analytics-adapter-v61.js`: adapter de measurement fail-closed.
- `funnel-contract-v529.json`: límites semánticos y de privacidad del funnel.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `growth-solutions-v51.json` y `cro-solutions-v52.json`: truth de rutas por situación.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad.
- `professional-authority-v525.json`: hechos profesionales publicables.
- `visual-assets-v526.json`: verdad de activos visuales.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar importes, monedas, descuentos o tarifas no aprobadas;
- no cotizador automático ni scoring de honorarios;
- no PII ni lectura/exportación del contenido del formulario;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- no equiparar exposición/contacto/handoff con conversión comercial;
- conservar exactamente 30 pasos canónicos;
- analytics permanece deshabilitada hasta decisión y revisión expresa;
- `stable` solo después de gates verdes.

## Próximo ciclo

No se activa automáticamente un proveedor de analytics ni se abre una nueva versión por inercia. El siguiente ciclo debe partir de una necesidad observable o de una decisión explícita de activación, con criterio de éxito y contrato de privacidad verificable.

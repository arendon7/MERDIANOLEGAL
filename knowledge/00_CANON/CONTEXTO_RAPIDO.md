# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **6.0.0 — Experience System**.
- SHA funcional certificado: `a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.
- `main == stable` sobre ese SHA al cierre funcional.
- Canal certificado: `github-pages-production-experience-system-certified`.
- GitHub Pages sirve v6.0.0; smoke público v5.0→v5.3: PASS.
- Browser E2E + axe sobre la v6 pública: PASS.
- Lighthouse: PASS con budgets existentes.
- 46/46 superficies migradas; 16/16 fichas preservan depth/truth; 1/1 formulario físico; 30/30 pasos canónicos.
- No hay un ciclo funcional posterior abierto. La tarea vigente es únicamente el cierre documental v6.0.0.
- Para la referencia documental definitiva, verificar los refs vigentes `main` y `stable`; no incrustar un SHA recursivo de cierre en esta nota.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## Qué cambió en v6.0

v6 reemplaza la primera lectura centrada en taxonomía interna por una arquitectura client-first:

**situación → resultado → intervención → evidencia → contacto**.

- La Home prioriza situaciones y decisiones empresariales antes que nombres internos de servicios/productos.
- Las 16 fichas diferencian producto cerrado y servicio adaptable, con gramática visual/semántica para resultado, entregables, proceso, perímetro, límites y profundidad.
- Las 7 superficies de soluciones, 8 sectores y 6 perspectivas se integran a la misma Experience System sin perder su contenido canónico.
- Firma, experiencia, demo, legales y 404 conservan su función específica dentro del sistema visual consolidado.
- La profundidad histórica v5.x se preserva; v6 reorganiza y jerarquiza, no sustituye truth jurídica por slogans.
- Contacto sigue siendo un único formulario físico con handoff manual por WhatsApp.

## Release engineering v6

- Equivalencia canónica pre-merge reproduce el builder y la calidad estática de Pages.
- Validators históricos incompatibles con el DOM v6 se hicieron phase-aware sin rebajar sus contratos legacy.
- El gate de equivalencia ejecuta Python + `node --check` + JSON antes del merge.
- Cambios en `scripts/validate_*.py` disparan el builder canónico.
- El smoke live usa cache-busting y espera la versión esperada para tolerar propagación de GitHub Pages sin aceptar una release vieja.
- `stable` solo se mueve después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Source-of-truth

- `main`: verdad técnica y documental vigente.
- `stable`: snapshot certificado; debe coincidir con `main` al cierre de una release.
- `experience-system-v60.json` y `experience-content-v60.json`: contratos principales de Experience System v6.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `growth-solutions-v51.json` y `cro-solutions-v52.json`: truth de las rutas por situación.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad preservado.
- `professional-authority-v525.json`: hechos profesionales publicables.
- `visual-assets-v526.json`: verdad de activos visuales.
- `funnel-contract-v529.json`: límites semánticos y de privacidad del funnel.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar importes, monedas, descuentos o tarifas no aprobadas;
- no cotizador automático ni scoring de honorarios;
- no PII ni lectura del contenido del formulario;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o carga documental ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- no ocultar contenido material para aparentar menor densidad;
- no equiparar exposición/contacto/handoff con conversión comercial;
- conservar exactamente 30 pasos canónicos;
- `stable` solo después de gates verdes.

## Graphify

Graphify sobre el SHA funcional certificado `a7940696…` está alineado con `main`: 1.007 nodos, 1.887 relaciones, 115 notas wiki y 17 specs E2E detectadas. Es memoria derivada y no sustituye a `main`; si `source_commit` deja de coincidir con `main`, tratarlo como obsoleto hasta su regeneración.

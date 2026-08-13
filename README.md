# Meridiano Legal · Web canónica v5.23.0

Sitio público static-first de Meridiano Legal, publicado en GitHub Pages: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado actual

**v5.23.0 — compresión del contacto comercial** está implementada, desplegada y certificada.

- SHA funcional y snapshot público certificado: `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`.
- Run final: `31730632791`.
- Al cierre funcional: `main == stable`.
- 46 HTML, 16 fichas profundas y 1 formulario físico canónico.
- Browser E2E + axe: 58 observados → 56 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; accesibilidad 1.00 en las seis superficies.
- Home: performance 1.00, LCP 1304 ms, CLS 0, TBT 11 ms.
- CI hasta `stable`: 264 s; baseline v5.5: 279 s; mejora 5.4%.
- Cobertura reducida: no. Budgets relajados: no.

El `channel` técnico de `version.json` conserva `github-pages-public-contact-compression-candidate`. No se renombra mediante un commit documental porque `version.json` dispara builder/Pages. El estado real de la release lo determinan la certificación, la promoción de `stable` y la memoria canónica.

## Arquitectura comercial vigente

- v5.20: una sola arquitectura de decisión en portada.
- v5.21: frontera verificable entre demo y capacidades reales.
- v5.22: narrativa jurídica senior y 16 ofertas diferenciadas.
- v5.23: una sola síntesis dentro del formulario y un único disclosure de proceso.

v5.23 conserva los contratos v5.9/v5.13/v5.14/v5.15 dentro de la síntesis y v5.10/v5.11 dentro del disclosure. Una intención explícita de propuesta puede abrir el detalle; orientación/alcance lo mantienen cerrado. No hay scoring, inferencia automática ni decisión autónoma.

Se mantienen exactamente los campos físicos del formulario, privacidad, handoff manual v5.17 y observabilidad local sin PII v5.18.

## Evidencia v5.23

Run `31730632791`:

- builder + segunda pasada/idempotencia: PASS;
- validadores históricos + v5.23: PASS;
- Pages + smoke: PASS;
- Browser E2E/axe: PASS;
- Lighthouse: PASS;
- release-health: PASS;
- promoción de `stable`: PASS.

Artefactos:

- Pages `9193089702` — `sha256:31619db18b44ba746eaca07d9d0dd6b73f5ebd87a7893e6c8df27952a0195533`;
- Lighthouse `9193157108` — `sha256:d98a955fdadd8d2ad03f5a0a110e77e5cd5cbb75e5275540dbf6d5d28a674390`;
- CI `9193218997` — `sha256:b98fbbf2b69fb3425526b30a48ddd3db5784f738e08e641d4489e524fbd235d8`;
- release-health `9193219605` — `sha256:7c7c29957dcb6626cb6ffd1b0350cc687e8e519031d9c81471638a9db5f138cc`.

## Controles principales

- `scripts/apply_contact_compression_v523.py`;
- `scripts/normalize_contact_compression_v523.py`;
- `scripts/validate_contact_compression_v523.py`;
- `tests/e2e/contact-compression.spec.mjs`;
- `tests/e2e/contact-integrity-v523.spec.mjs`;
- `tests/e2e/accessibility.spec.mjs`;
- `decision-action-v515.js` y `decision-action-v515.css`.

Builder y Release Governance vigilan directamente los scripts v5.23. El E2E protege la integridad `DIV role=region + message + privacy + submit`; axe verifica siete superficies WCAG 2.1 AA.

## Capacidades externas: verdad operativa

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estática/noindex y pipeline CI.

No declarar activas sin implementación real: autenticación/cuentas reales, portal real, CRM/backend, almacenamiento servidor, email transaccional, firma electrónica, pagos, agenda, carga documental o analítica externa.

## Graphify

Al cierre funcional Graphify `0.9.26` procesó `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`: 675 nodos, 1.126 relaciones, 96 notas, 75 scripts Python, 25 fuentes JS y 9 specs E2E.

Graphify es memoria derivada; `main`, `stable`, Pages, validadores y tests deciden.

## Documentación

- `RELEASE-v5.23.md`: cierre completo, incidencias y evidencia.
- `RELEASE-v5.22.md`: narrativa y catálogo.
- `RELEASE-v5.21.md`: frontera demo/capacidad.
- `RELEASE-v5.20.md`: compresión de decisión.
- `knowledge/HOME.md`: memoria operativa.

## Principios

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No inferir intención comercial no declarada.
- No convertir acciones locales en afirmaciones de envío, lectura, aceptación o conversión.
- Una demo no equivale a capacidad productiva.

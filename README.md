# Meridiano Legal · Web canónica v5.18.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages.

URL pública: `https://arendon7.github.io/MERDIANOLEGAL/`

## Estado actual

La publicación conserva 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico. `stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

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
- **v5.17:** continuidad manual del handoff, borrador efímero y stale protection;
- **v5.18:** observabilidad verificable de seis hechos locales del handoff, sin PII ni inferencias falsas.

La composición canónica termina en `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15 → v5.17 → v5.18`; v5.16 permanece como hardening transversal.

## v5.18 · Observabilidad del handoff manual

La web solo mide acciones que realmente ocurren dentro de la página: borrador preparado, reapertura solicitada, copia exitosa o fallida, edición solicitada y borrador desactualizado.

No registra contenido del formulario, nombre, email, empresa, teléfono, referencia, resumen ni URL de WhatsApp. No usa backend, CRM, proveedor de analítica externa, storage persistente ni transporte de red nuevo. Tampoco declara enviado, entregado, leído, aceptado o convertido algo que la web no puede verificar.

El contrato fuente es `handoff-observability-v518.json`; el runtime es `handoff-observability-v518.js` y su validator es `scripts/validate_handoff_observability_v518.py`.

## Evidencia funcional v5.18

PR #67 → merge fuente `3dd01285bcb28a568e2d5a65e2fa88ad284142cb` → candidato materializado `a082b4d9139ae929367cac0085597365e75dbaaf`.

Run `31631855996`:

- `main == stable == a082b4d9139ae929367cac0085597365e75dbaaf` al cierre funcional;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse 6/6 PASS y accesibilidad 1.00 en las seis superficies;
- performance 0.98–1.00;
- `accessibilityAuditGaps` vacío;
- CI hasta `stable`: 200 s, 28.3% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no.

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.18.md`: alcance, límites y evidencia de v5.18;
- `RELEASE-v5.17.md`: continuidad manual y hardening del handoff;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No convertir acciones locales en afirmaciones sobre envío, lectura, aceptación o conversión.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

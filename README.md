# Meridiano Legal · Web canónica v5.19.0

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
- **v5.18:** observabilidad verificable de seis hechos locales del handoff, sin PII ni inferencias falsas;
- **v5.19:** foco comercial adaptativo mediante progressive disclosure basado solo en intención explícita.

La composición canónica termina en `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15 → v5.17 → v5.18`; v5.16 y v5.19 actúan como hardening transversal de UX/decisión sobre esa composición.

## v5.19 · Foco comercial adaptativo

El tramo final conserva el formulario, la recomendación y todas las salvaguardas jurídicas, pero reduce información secundaria visible cuando el usuario todavía está explorando o definiendo alcance.

- `orientation` y `scope`: detalle secundario inicialmente replegado;
- `proposal` explícito en escritorio: detalle inicialmente expandido;
- móvil conserva el progressive disclosure v5.16;
- abrir/cerrar detalle no modifica etapa, modalidad, recomendación ni handoff.

No hay scoring, inferencia de intención, PII nueva, persistencia nueva, transporte de red nuevo, backend ni CRM. El contenido material permanece disponible mediante `<details>` nativo y accesible.

## Evidencia funcional v5.19

PR #71 → merge fuente `fcf8d868e5b95ab201c8ebb612ffba166f4746f5` → candidato público `9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.

Run `31649425600`:

- `main == stable == 9a91e8d19697142c0d2d0990c1e606f6ff9660ef` al cierre funcional;
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse 6/6 PASS y accesibilidad 1.00 en las seis superficies;
- performance 0.98–1.00;
- LCP máximo 1368 ms, CLS máximo 0.087, TBT máximo 56 ms;
- `accessibilityAuditGaps` vacío;
- CI hasta `stable`: 215 s, 22.9% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no.

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.19.md`: foco comercial adaptativo, límites y evidencia de v5.19;
- `RELEASE-v5.18.md`: observabilidad verificable del handoff;
- `RELEASE-v5.17.md`: continuidad manual y hardening del handoff;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No inferir intención comercial que el usuario no haya declarado.
- No convertir acciones locales en afirmaciones sobre envío, lectura, aceptación o conversión.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

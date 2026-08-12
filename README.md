# Meridiano Legal · Web canónica v5.16.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.16 mejora **UX móvil y accesibilidad verificable** sin recortar profundidad jurídica: corrige targets táctiles y contrastes reales, reduce scroll mediante revelado progresivo nativo y amplía la observabilidad Lighthouse para que los gaps de accesibilidad queden auditables.

## Estado actual

La publicación conserva 46 páginas HTML: 8 servicios profesionales, 8 productos jurídicos de alcance cerrado, 5 planes recurrentes, hub + 6 rutas de decisión, 8 sectores, 6 perspectivas, Firma, Centro Demo y Meridiano Empresas ficticio/noindex.

URL pública: `https://arendon7.github.io/MERDIANOLEGAL/`

`stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

## Capas comerciales y de calidad vigentes

- **v5.8:** claridad de compra;
- **v5.9:** calificación comercial y privacidad;
- **v5.10:** intención contextual, propuesta y cierre;
- **v5.11:** solicitud, propuesta, aceptación e inicio + Pages serializado detrás del builder;
- **v5.12:** 5 modalidades y prueba verificable derivada de fuente;
- **v5.13:** continuidad de modalidad/prueba hasta formulario y WhatsApp;
- **v5.14:** recomendación explicable con encaje, límite y alternativa;
- **v5.15:** consolidación recomendación→acción y rutas proposal/scope/orientation controladas por el usuario;
- **v5.16:** UX móvil, targets táctiles, progressive disclosure, foco/scroll accesible y diagnóstico Lighthouse de auditorías con score < 1.

La composición fuente continúa `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15`; v5.16 es hardening final de runtime/CSS/QA y no añade un applicator de contenido nuevo.

## v5.16 · UX móvil y accesibilidad verificable

v5.16 parte de evidencia, no de supuestos. `scripts/run_quality_v55.mjs` conserva en sus resúmenes las auditorías Lighthouse de accesibilidad con score menor a 1. Ese diagnóstico identificó `target-size` en tres CTA de Perspectivas y posteriormente una deuda móvil de contraste/targets en la ficha Programa de Gobernanza IA.

Implementado:

- tres CTA “Explorar la práctica” con target táctil mínimo de 44 px;
- en móvil, detalle secundario de v5.10 y v5.11 dentro de `<details>` nativos; calificación, contexto, recomendación y ruta permanecen visibles;
- sin JavaScript, el contenido comercial sigue expandido como antes;
- tres regiones horizontalmente desplazables reciben foco, `role=region`, nombre accesible y foco visible en móvil;
- contraste móvil corregido en el primer paso comercial;
- menú profundo, sus cinco enlaces y CTA fijo de fichas profundas con targets/contraste accesibles;
- portada y ficha profunda auditadas por axe en viewport 390×844 dentro de las mismas 37 entradas protegidas;
- ningún cambio de budgets, workers, topología CI, scoring, storage, red propia o PII.

## Evidencia funcional v5.16

Run `31618614227`, SHA funcional certificado `2cd5fb0d2b428187c08cf21e562427f9bc44508c`:

- `main == stable` en el cierre funcional;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe sin violaciones serias/críticas, incluida la ficha profunda en móvil;
- Lighthouse: 6/6 PASS y **accesibilidad 1.00 en las seis superficies**;
- `accessibilityAuditGaps`: vacío en las seis superficies;
- CI hasta `stable`: 187 s, 33.0% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|
| Portada | 1.00 | 1.00 | 1255 ms | 0 | 7 ms |
| Solución IA | 1.00 | 1.00 | 902 ms | 0 | 0 ms |
| Producto IA | 1.00 | 1.00 | 905 ms | 0 | 0 ms |
| Sector tecnología | 0.98 | 1.00 | 905 ms | 0.087 | 0 ms |
| Perspectiva IA | 1.00 | 1.00 | 902 ms | 0 | 0 ms |
| Demo | 1.00 | 1.00 | 905 ms | 0 | 0 ms |

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.16.md`: UX móvil, accesibilidad y evidencia de release;
- `RELEASE-v5.15.md`: eficiencia recomendación→acción;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No usar scoring opaco para decidir la modalidad.
- Compactar móvil no significa ocultar contenido jurídico material.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

## Transición al siguiente ciclo

v5.17 solo puede iniciar cuando el SHA que contiene este cierre formal 5.16.0 haya atravesado nuevamente builder, sincronización visible, Pages, Browser/axe, Lighthouse y termine en `main == stable`.

# Meridiano Legal · Web canónica v5.13.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.13 conserva **modalidad + estándar verificable** desde las fichas profundas hasta el formulario y el brief preparado para WhatsApp, sin backend ni persistencia adicional.

## Estado actual

La publicación conserva 46 páginas HTML:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- hub de soluciones + 6 rutas de decisión;
- 8 sectores;
- 6 perspectivas;
- Firma, Centro Demo y Meridiano Empresas ficticio/noindex.

URL pública: `https://arendon7.github.io/MERDIANOLEGAL/`

`stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

## Capas comerciales vigentes

- **v5.8:** claridad de compra;
- **v5.9:** calificación comercial y privacidad;
- **v5.10:** intención contextual, propuesta y cierre;
- **v5.11:** solicitud, propuesta, aceptación e inicio + Pages serializado detrás del builder;
- **v5.12:** 5 modalidades y prueba verificable derivada de fuente;
- **v5.13:** continuidad de modalidad y estándar verificable hasta formulario/WhatsApp.

Secuencia canónica: `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13`.

## v5.13 · Brief comercial continuo

Las 16 fichas profundas transportan categorías estructuradas al formulario:

- modalidad considerada;
- estándar verificable: método + entregables + formatos + aceptación/cierre.

El brief visible y el mensaje de WhatsApp reutilizan ese contexto. Las categorías orientan la conversación; no constituyen propuesta, aceptación ni inicio automático del encargo.

Implementación: `commercial-brief-v513.css`, `commercial-brief-v513.js`, `scripts/apply_commercial_brief_v513.py` y `scripts/validate_commercial_brief_v513.py`.

No se añadió storage, backend, transporte de red propio de la capa ni PII adicional.

## Evidencia funcional v5.13 previa al cierre documental

Run `31568876368`, SHA `e77a7e824117d3f8f3f67cc3fc71f11f3fc858c3`:

- `main == stable` antes del cierre documental;
- Browser: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7/7 sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 177 s hasta `stable`, 36.6% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger: PASS, sin carrera directa por push;
- Commercial Brief v5.13 validator: PASS.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1319 ms | 0 | 89 ms | 91,193 B |
| Solución IA | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 23,254 B |
| Producto IA | 1.00 | 1.00 | 994 ms | 0 | 0 ms | 37,334 B |
| Sector tecnología | 1.00 | 1.00 | 997 ms | 0 | 0 ms | 24,286 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,908 B |
| Demo | 1.00 | 1.00 | 1033 ms | 0 | 0 ms | 21,932 B |

## Correcciones de composición v5.13

- tipo canónico de fichas de servicio: `Servicio profesional`;
- validator v5.12 ahora conserva las cinco rutas obligatorias por `path + fragment`, permitiendo query params aditivos posteriores.

Ambos ajustes fueron certificados antes de promover `stable`; no reducen cobertura.

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial local/de página, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.13.md`: continuidad comercial y evidencia de release;
- `RELEASE-v5.12.md`: modalidad y prueba verificable;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura para acelerar CI.
- No relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

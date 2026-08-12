# Meridiano Legal · Web canónica v5.14.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.14 añade **recomendación explicable de modalidad**: por qué encaja, límite y alternativa, sin puntajes opacos, backend ni persistencia adicional.

## Estado actual

La publicación conserva 46 páginas HTML: 8 servicios profesionales, 8 productos jurídicos de alcance cerrado, 5 planes recurrentes, hub + 6 rutas de decisión, 8 sectores, 6 perspectivas, Firma, Centro Demo y Meridiano Empresas ficticio/noindex.

URL pública: `https://arendon7.github.io/MERDIANOLEGAL/`

`stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

## Capas comerciales vigentes

- **v5.8:** claridad de compra;
- **v5.9:** calificación comercial y privacidad;
- **v5.10:** intención contextual, propuesta y cierre;
- **v5.11:** solicitud, propuesta, aceptación e inicio + Pages serializado detrás del builder;
- **v5.12:** 5 modalidades y prueba verificable derivada de fuente;
- **v5.13:** continuidad de modalidad/prueba hasta formulario y WhatsApp;
- **v5.14:** recomendación explicable con encaje, límite y alternativa.

Secuencia canónica: `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14`.

## v5.14 · Recomendación explicable

`recommendation-v514.json` define cinco reglas determinísticas con `scoring: false`. La portada permite comparar las modalidades y, cuando existe contexto suficiente, el formulario y WhatsApp reutilizan la explicación. Si no existe contexto, la web no presume una recomendación.

Implementación: `recommendation-v514.json`, `recommendation-v514.css`, `recommendation-v514.js`, `scripts/apply_recommendation_v514.py` y `scripts/validate_recommendation_v514.py`.

No se añadió cuestionario, storage, backend, transporte de red propio de la capa ni PII adicional.

## Evidencia funcional v5.14 previa al cierre documental

Run `31570619885`, SHA `42e482241a818e0c94137810e1224558a58f397d`:

- `main == stable` antes del cierre documental;
- Browser E2E + axe: PASS sobre 37 entradas protegidas y 7 superficies axe;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 264 s hasta `stable`, 5.4% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance + Pages trigger + validator v5.14: PASS.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 0.99 | 0.97 | 1307 ms | 0 | 106 ms | 95,461 B |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,279 B |
| Producto IA | 1.00 | 1.00 | 907 ms | 0 | 0 ms | 37,657 B |
| Sector tecnología | 0.98 | 1.00 | 988 ms | 0.087 | 0 ms | 24,564 B |
| Perspectiva IA | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 25,918 B |
| Demo | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 22,048 B |

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.14.md`: recomendación explicable y evidencia de release;
- `RELEASE-v5.13.md`: continuidad comercial;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No usar scoring opaco para decidir la modalidad.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

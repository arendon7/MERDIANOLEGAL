# Meridiano Legal · Web canónica v5.15.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.15 consolida **recomendación → siguiente acción**: el encaje queda junto al CTA, límites y alternativas pasan a comparación secundaria y la ruta comercial permanece explícita y controlada por el usuario.

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
- **v5.14:** recomendación explicable con encaje, límite y alternativa;
- **v5.15:** consolidación recomendación→acción, comparación secundaria y rutas proposal/scope/orientation controladas por el usuario.

Secuencia canónica: `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15`.

## v5.15 · Recomendación → acción

La capa reutiliza `recommendation-v514.json` como fuente de las cinco modalidades y mantiene `scoring: false`. El encaje se muestra directamente en el selector v5.12; límites y alternativas se conservan en un detalle ampliado colapsado. El formulario muestra una ruta comercial sugerida, pero nunca modifica automáticamente la etapa del usuario.

Rutas canónicas:

- diagnóstico → definición de alcance;
- auditoría → propuesta;
- producto cerrado → propuesta;
- servicio especializado → definición de alcance;
- acompañamiento recurrente → definición de alcance;
- sin contexto suficiente → orientación inicial.

Implementación: `decision-action-v515.css`, `decision-action-v515.js`, `scripts/apply_decision_action_v515.py` y `scripts/validate_decision_action_v515.py`.

No se añadió cuestionario, scoring, storage, backend, transporte de red propio ni PII adicional.

## Evidencia funcional v5.15 previa al cierre documental

Run `31609518536`, SHA `48a0692e8e4f999a85cfd8619fe2e293528945c2`:

- `main == stable` antes del cierre documental;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY; 7 superficies axe limpias;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 209 s hasta `stable`, 25.1% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance + Pages trigger + validator v5.15: PASS.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1322 ms | 0 | 3 ms | 99,735 B |
| Solución IA | 1.00 | 1.00 | 989 ms | 0 | 0 ms | 23,234 B |
| Producto IA | 1.00 | 1.00 | 999 ms | 0 | 0 ms | 37,677 B |
| Sector tecnología | 0.98 | 1.00 | 1006 ms | 0.087 | 0 ms | 24,289 B |
| Perspectiva IA | 1.00 | 1.00 | 1044 ms | 0 | 0 ms | 25,796 B |
| Demo | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 21,994 B |

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.15.md`: eficiencia recomendación→acción y evidencia de release;
- `RELEASE-v5.14.md`: recomendación explicable;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No usar scoring opaco para decidir la modalidad.
- Una ruta sugerida no puede cambiar automáticamente la decisión declarada por el usuario.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

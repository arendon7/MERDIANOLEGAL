# Meridiano Legal · Web canónica v5.12.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.12 añade **prueba comercial verificable derivada de la fuente jurídica** y una guía de **5 modalidades de contratación**, preservando los gates Browser E2E + axe + Lighthouse y la release serializada detrás del builder.

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

`main` es la candidata vigente; `stable` solo se mueve cuando builder, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

## v5.12 · Prueba verificable

La portada distingue 5 modalidades: diagnóstico, auditoría, producto cerrado, servicio especializado y acompañamiento recurrente.

Las 16 fichas profundas muestran un bloque derivado de la fuente canónica con cuatro dimensiones verificables:

- método;
- entregables;
- formatos;
- aceptación/cierre.

No se usan clientes, testimonios, casos de éxito, resultados ni métricas inventadas.

Implementación: `proof-v512.css`, `scripts/apply_proof_v512.py` y `scripts/validate_proof_v512.py`.

## Capas comerciales preservadas

- **v5.8:** claridad de compra;
- **v5.9:** calificación comercial y privacidad;
- **v5.10:** intención contextual, propuesta y cierre;
- **v5.11:** solicitud, propuesta, aceptación e inicio + Pages serializado detrás del builder;
- **v5.12:** modalidad y prueba verificable.

Secuencia canónica: `v5.8 → v5.9 → v5.10 → v5.11 → v5.12`.

## Evidencia funcional v5.12 previa al cierre documental

Run `31562692907`, SHA `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`:

- `main == stable` antes del cierre documental;
- Browser: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7/7 sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 187 s hasta `stable`, 33.0% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance: PASS;
- Pages trigger: PASS, sin carrera directa por push.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1263 ms | 0 | 2 ms | 88,599 B |
| Solución IA | 1.00 | 1.00 | 908 ms | 0 | 0 ms | 23,343 B |
| Producto IA | 1.00 | 1.00 | 908 ms | 0 | 0 ms | 37,309 B |
| Sector tecnología | 0.98 | 1.00 | 960 ms | 0.087 | 0 ms | 24,400 B |
| Perspectiva IA | 0.98 | 1.00 | 906 ms | 0.087 | 0 ms | 26,003 B |
| Demo | 1.00 | 1.00 | 978 ms | 0 | 0 ms | 22,076 B |

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial local/de sesión, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.12.md`: prueba verificable, modalidad y evidencia de release;
- `RELEASE-v5.11.md`: contratación/inicio y topología CI;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura para acelerar CI.
- No relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

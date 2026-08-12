# Meridiano Legal · Web canónica v5.17.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.17 mejora la **continuidad del handoff comercial manual a WhatsApp**: mantiene una referencia utilizable, permite reabrir o copiar de forma explícita, invalida borradores desactualizados y aclara qué puede y qué no puede verificar una web estática, sin convertir el sitio en CRM ni persistir la solicitud.

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
- **v5.16:** UX móvil, targets táctiles, progressive disclosure, foco/scroll accesible y diagnóstico Lighthouse;
- **v5.17:** continuidad post-preparación del handoff manual a WhatsApp, borrador efímero, protección stale e idempotencia/gobernanza reforzadas.

La composición canónica de contenido comercial termina en `v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → v5.13 → v5.14 → v5.15 → v5.17`; v5.16 permanece como hardening transversal de runtime/CSS/QA previo a esta capa.

## v5.17 · Continuidad manual del handoff

La arquitectura real conserva **un único formulario físico** en `index.html`. Las 16 fichas profundas no lo duplican: conservan modalidad, estándar verificable e intención comercial en rutas contextuales hacia `index.html#contacto`.

Después de preparar una solicitud, el usuario dispone de un panel que muestra la referencia y ofrece acciones manuales para:

- reabrir WhatsApp con el mismo borrador;
- copiar el resumen de forma explícita;
- volver a editar la solicitud.

La copia automática silenciosa al portapapeles fue eliminada. El borrador v5.17 vive solo en memoria de la página; no usa `localStorage`, `sessionStorage`, backend ni almacenamiento servidor. Si el formulario cambia después de preparar el handoff, el borrador pasa a estado desactualizado y copiar/reabrir quedan bloqueados hasta volver a prepararlo.

El panel no replica nombre, empresa, email ni mensaje completo en el DOM y declara que la web no conoce entrega, lectura, aceptación contractual, apertura de expediente ni inicio del encargo.

## Hardening de composición v5.17

Los gates de release detectaron defectos reales durante el desarrollo y no se relajaron:

- el primer candidato falló idempotencia porque Pages todavía terminaba en v5.15;
- el segundo candidato reveló un panel residual, ID duplicado y pérdida del cierre canónico del formulario;
- v5.17 pasó a limpiar por identidad semántica `data-handoff-v517`, restaurar el cierre solo si falta y exigir exactamente una instancia válida;
- Pages termina ahora la recomposición en v5.17 y ejecuta su validator explícito;
- Release Governance normaliza outputs materializados v5.17 antes de ejecutar intactos los validators históricos v5.8→v5.15.

## Evidencia funcional v5.17

Run `31628244159`, SHA funcional certificado `56f99a5398b1e0505da5acd601bac3aec8588c1d`:

- `main == stable == 56f99a5398b1e0505da5acd601bac3aec8588c1d` al cierre funcional;
- builder + idempotencia + validadores históricos + v5.17: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- tiempo Browser reporter: 71 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS y **accesibilidad 1.00 en las seis superficies**;
- `accessibilityAuditGaps`: vacío;
- CI hasta `stable`: 181 s, 35.1% mejor que baseline v5.5 de 279 s;
- cobertura reducida: no;
- budgets relajados: no.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT |
|---|---:|---:|---:|---:|---:|
| Portada | 1.00 | 1.00 | 1276 ms | 0 | 1 ms |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms |
| Producto IA | 1.00 | 1.00 | 919 ms | 0 | 0 ms |
| Sector tecnología | 0.98 | 1.00 | 947 ms | 0.087 | 0 ms |
| Perspectiva IA | 0.98 | 1.00 | 906 ms | 0.087 | 0 ms |
| Demo | 1.00 | 1.00 | 948 ms | 0 | 0 ms |

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff manual, contexto comercial client-side, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No declarar activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.17.md`: continuidad manual, privacidad, hardening de composición y evidencia de release;
- `RELEASE-v5.16.md`: UX móvil y accesibilidad verificable;
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura ni relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- No usar scoring opaco para decidir la modalidad.
- No declarar enviado, leído o aceptado algo que la web estática no puede verificar.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

## Transición al siguiente ciclo

v5.18 solo puede iniciar cuando el SHA que contiene este cierre formal 5.17.0 haya atravesado nuevamente builder, sincronización visible, Pages, Browser/axe, Lighthouse, release-health, procedencia Graphify y termine en `main == stable`.

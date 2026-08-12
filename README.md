# Meridiano Legal · Web canónica v5.11.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.11 conserva la arquitectura jurídica/comercial y los gates Browser E2E + axe + Lighthouse, y añade **preparación jurídica del encargo** junto con una **release serializada detrás del builder canónico**.

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

`main` es la candidata vigente; `stable` solo se mueve cuando construcción, idempotencia, Pages, smoke, Browser E2E, axe, Lighthouse y release-health están verdes.

## v5.11 · Contratación e inicio

El recorrido público diferencia cuatro estados:

1. Solicitud preparada.
2. Propuesta emitida.
3. Propuesta aceptada.
4. Encargo iniciado.

Antes del inicio operativo se explican verificaciones de partes/conflictos cuando correspondan, alcance y exclusiones, condiciones económicas, fecha/condición de inicio, interlocutores y canal adecuado para información confidencial.

La web deja claro que **no acepta contratos, no cobra pagos, no reserva agenda, no crea expedientes, no habilita carga documental y no inicia el encargo automáticamente**.

Implementación:

- `engagement-v511.css`;
- `scripts/apply_engagement_v511.py`;
- `scripts/validate_engagement_v511.py`.

## v5.11 · CI sin carrera builder/Pages

`Site Quality and Deploy` ya no tiene trigger directo por `push`. La secuencia protegida es:

```text
push de fuente
  ↓
Build canonical public site
  ↓ workflow_run exitoso
Site Quality and Deploy
  ↓
deploy + smoke
  ├──→ Browser E2E + axe ──┐
  └──→ Lighthouse ─────────┴──→ release-health → stable
```

`scripts/validate_pages_trigger_v511.py` impide reintroducir el `push` directo de Pages.

## Capas comerciales preservadas

- **v5.8:** claridad de compra en portada y 16 fichas profundas;
- **v5.9:** calificación comercial y resumen previo a WhatsApp, sin persistencia servidor;
- **v5.10:** intención contextual, anatomía de propuesta y ruta de cierre;
- **v5.11:** separación entre solicitud, propuesta, aceptación e inicio efectivo.

Secuencia canónica: `v5.8 → v5.9 → v5.10 → v5.11`.

## Cobertura protegida

- 37 entradas Playwright;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- workers Playwright CI = 1;
- budgets: performance >= 0.70, accesibilidad >= 0.90, LCP <= 4000 ms, CLS <= 0.15, TBT <= 350 ms, transferencia <= 1.5 MB.

## Evidencia funcional v5.11 previa al cierre documental

Run `31560805174`, SHA `cf4341eb9ec051a3e583b4675263b228ee5f0839`:

- `main == stable` antes del cierre documental;
- Browser: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7/7 sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 193 s hasta `stable`;
- baseline v5.5: 279 s;
- mejora: 30.8%;
- cobertura reducida: no;
- budgets relajados: no;
- release trigger v5.11: PASS, sin carrera directa por push.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1247 ms | 0 | 74 ms | 86,682 B |
| Solución IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,310 B |
| Producto IA | 1.00 | 1.00 | 907 ms | 0 | 0 ms | 35,468 B |
| Sector tecnología | 0.98 | 1.00 | 922 ms | 0.087 | 0 ms | 24,507 B |
| Perspectiva IA | 0.98 | 1.00 | 902 ms | 0.087 | 0 ms | 25,914 B |
| Demo | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 22,058 B |

## Integraciones externas: estado verdadero

Activas: GitHub Pages, WhatsApp como handoff, contexto comercial local/de sesión, telemetría first-party/local sin PII, sitemap/robots/canonical/Open Graph, demo estático/noindex y pipeline de certificación.

No activas sin configuración real: dominio personalizado/CNAME, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario, email transaccional, firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.11.md`: contratación/inicio, topología CI y evidencia.
- `RELEASE-v5.10.md`: intención comercial y propuesta/cierre.
- `RELEASE-v5.9.md`: calificación comercial y privacidad.
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura para acelerar CI.
- No relajar budgets para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- No transmitir PII en telemetría.
- Graphify orienta; `main`, Pages, validadores y tests deciden.

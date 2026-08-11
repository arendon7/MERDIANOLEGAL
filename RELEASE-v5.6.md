# Meridiano Legal — Release v5.6.0

Fecha de cierre funcional: 2026-08-10.
Canal: `github-pages-public-ci-observability-ready`.

## Objetivo

v5.6 reduce el tiempo de pared de la certificación pública y mejora su observabilidad **sin disminuir cobertura, navegadores, superficies axe/Lighthouse ni presupuestos**.

La hipótesis inicial se midió antes de modificar la topología. El baseline v5.5 mostró que el cuello de botella estaba en el job de navegador serial: Browser E2E/axe y Lighthouse se ejecutaban uno después del otro.

## Baseline

Baseline versionado en `ci-baseline-v56.json`:

- run: `31433199058`;
- SHA: `440c09c235c3826c7b0031fd5ac9ddaed9748379`;
- métrica: inicio de `quality` → inicio del snapshot estable;
- tiempo crítico: **279 s**;
- Browser Quality serial: ~215 s.

Objetivo interno: al menos 20% de mejora, medido como observabilidad y no como threshold frágil de aprobación.

## Arquitectura final

La cadena final queda:

```text
quality → deploy → live_smoke
                    ├─ browser_e2e ──────┐
                    └─ lighthouse_quality ├─ snapshot → stable
                                         ┘
```

Los dos rails empiezan después del mismo deploy y smoke. Ninguno sustituye al otro y `stable` exige ambos.

## Browser E2E + axe

Se conserva:

- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- proyecto `accessibility-chromium`;
- 7 superficies axe;
- worker único en CI;
- retries únicamente según la política Playwright existente;
- traces/screenshots/reportes de fallo.

`tests/e2e/ci-summary-reporter.mjs` añade resumen compacto al Job Summary con tests observados, passed, skipped, fallidos, retries y tiempo de pared.

## Lighthouse

Lighthouse se desacopla del job E2E y usa:

- Node 22;
- `npm ci`;
- caché npm de `actions/setup-node`;
- únicamente Chromium fijado por Playwright;
- seis superficies de `quality-budgets-v55.json`;
- los mismos presupuestos v5.5.

No se cachean binarios Playwright.

### Política de outliers

La política robusta v5.6 no cambia umbrales:

- accesibilidad y peso total son no reintentables;
- solo performance, LCP, CLS y TBT pueden activar verificación;
- solo si todos los fallos iniciales pertenecen a ese conjunto;
- se toman exactamente dos muestras adicionales;
- se requieren tres muestras válidas;
- se decide por mediana de tres;
- nunca se selecciona el mejor valor.

Cada muestra queda registrada en `summary.json`.

## Observabilidad

v5.6 incorpora:

- `ci-baseline-v56.json`;
- `scripts/summarize_ci_v56.py`;
- `scripts/validate_ci_v56.py`;
- reporter Playwright;
- `summary.json` + `summary.md` de Lighthouse;
- artefacto `ci-certification-summary-v56` con tiempos por gate y comparación contra baseline;
- artefactos QA directos mediante `actions/upload-artifact@v7`.

## Reducción de ciclos redundantes

El builder identifica commits automáticos `build: sincroniza sitio público canónico` y evita iniciar una nueva construcción útil sobre esos outputs.

Además, si al reconstruir no existe diff canónico, el builder termina sin crear otro commit.

Durante la propia implementación se verificó este caso: tras materializar los outputs v5.6, cambios posteriores de validators/workflow que no modificaban HTML hicieron que el builder terminara en verde sin generar otro commit de salida.

## Incidentes encontrados durante v5.6

### 1. YAML del builder inválido

La primera versión del filtro de commits incluía el literal `build: ...` dentro de un scalar YAML `if:` sin envolver correctamente todo el valor. GitHub rechazó el workflow antes de crear jobs.

Corrección:

- condición segura basada en `startsWith(..., 'build')`;
- `validate_ci_v56.py` protege esa forma.

### 2. Validator v5.4 incompatible con gate dual

`validate_browser_v54.py` esperaba literalmente `needs: browser_e2e`.

Desde v5.6 el contrato es más fuerte: `stable` depende de `[browser_e2e, lighthouse_quality]`.

El validator se hizo version-aware:

- <=5.5 conserva el contrato original;
- >=5.6 exige ambos gates.

### 3. Validator v5.6 exigía un path redundante

El validator esperaba el reporter E2E como path literal aunque `build-canonical.yml` ya vigila `tests/e2e/**`.

Se alineó con el glob canónico sin reducir cobertura.

### 4. Chrome mutable del runner produjo TBT aislado

El primer experimento paralelo usó el Chrome del runner para Lighthouse. La portada produjo TBT 497 ms frente al budget <=350, con CLS 0 y las demás superficies TBT 0.

La comparación con v5.5 mostró que la release anterior usaba el Chromium fijado por Playwright.

Corrección:

- Lighthouse vuelve al Chromium pinneado;
- instala solo Chromium, sin WebKit y sin `--with-deps`;
- se añadió la política mediana-de-tres descrita arriba.

El siguiente run volvió a TBT 0 en portada y no necesitó muestras adicionales.

### 5. Runtime de upload-artifact

La cadena todavía utilizaba `actions/upload-artifact@v5`, que emitía una advertencia de runtime antiguo en el runner actual.

Se actualizaron las cargas directas de artefactos a `actions/upload-artifact@v7`. `upload-pages-artifact@v4` se mantiene porque pertenece al flujo específico de Pages.

## Certificación funcional final

Run: `31458580456`.

SHA funcional antes del cierre documental:

`c4f48e43a1681cdbd24db4c6308878efeb801700`

Todos los jobs terminaron en `success`:

- Validate current site;
- Deploy GitHub Pages;
- Verify deployed Pages;
- Lighthouse quality on deployed Pages;
- Browser E2E on deployed Pages;
- Update stable snapshot.

La fase estática aprobó idempotencia, catálogo, conversión, UX v4.5-v4.7, calidad v4.8, operación v4.9, producción v5.0, growth v5.1, CRO/search v5.2, autoridad/medición v5.3, Browser v5.4, calidad v5.5, CI v5.6, selector, contexto, editorial, sistema visual, JavaScript y JSON.

## Resultado Browser E2E + axe

- 37 tests observados;
- 35 passed;
- 2 skipped;
- 0 fallos;
- 0 retries;
- 7 superficies axe sin violaciones serias/críticas.

## Resultado Lighthouse final

Todas las superficies usaron `single-sample`; ninguna activó verificación.

| Superficie | Performance | A11y | LCP | CLS | TBT | Bytes |
|---|---:|---:|---:|---:|---:|---:|
| home | 1.00 | 0.97 | 1239 ms | 0 | 0 ms | 73,834 |
| solution-ai | 1.00 | 1.00 | 964 ms | 0 | 0 ms | 23,235 |
| product-ai | 1.00 | 1.00 | 911 ms | 0 | 0 ms | 33,351 |
| sector-tech | 1.00 | 1.00 | 935 ms | 0 | 0 ms | 24,272 |
| perspective-ai | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,985 |
| demo | 1.00 | 1.00 | 944 ms | 0 | 0 ms | 22,003 |

Resultado:

`QUALITY V5.5/V5.6 OK: 6 superficies cumplen Lighthouse y presupuestos sin relajación.`

## Resultado de eficiencia

El resumen de certificación del run final midió:

- baseline v5.5: **279 s**;
- v5.6: **160 s**;
- mejora: **42.7%**;
- cobertura reducida: **no**;
- budgets relajados: **no**.

Duraciones aproximadas observadas:

- Validate current site: 8 s;
- Deploy GitHub Pages: 11 s;
- Verify deployed Pages: 12 s;
- Browser E2E: 115 s;
- Lighthouse: 94 s.

La reducción supera el objetivo del 20% y proviene principalmente del paralelismo y de eliminar esperas/ciclos redundantes, no de quitar controles.

## Política de cierre

La release solo queda cerrada cuando el commit documental final vuelve a atravesar la misma certificación y `main == stable`.

Los SHA escritos aquí documentan evidencia histórica. Para conocer el estado vigente deben consultarse los refs actuales y `knowledge/graphify-live/graphify-out/BUILD_META.json.source_commit`.

## Integraciones externas

Activas únicamente las verificadas: GitHub Pages, WhatsApp, contexto comercial local/session, telemetría local sin PII, SEO técnico y pipeline de publicación.

No están activas sin configuración real: dominio personalizado, Search Console, analítica externa, CRM/backend, almacenamiento servidor del formulario y email transaccional.

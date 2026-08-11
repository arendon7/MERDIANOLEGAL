# Meridiano Legal — Release v5.7.0

Fecha de cierre: 2026-08-11.
Canal: `github-pages-release-governance-ready`.

## Objetivo

v5.7 consolida gobierno de releases, salud operativa y control de dependencias **sin reducir cobertura, navegadores, superficies axe/Lighthouse ni presupuestos**.

La release toma como base v5.6, donde Browser E2E/axe y Lighthouse ya operan como gates paralelos después del mismo deploy + smoke, y añade una capa preventiva para evitar que cambios futuros en Actions, permisos, runtimes o dependencias degraden silenciosamente esa garantía.

## Política versionada

`release-governance-v57.json` registra:

- Actions permitidas, major validado y SHA exacto;
- runtimes QA autorizados;
- versiones exactas de Playwright, axe y Lighthouse;
- workflows requeridos;
- invariantes de cobertura;
- contrato de permisos;
- evidencia funcional del ciclo.

El validator `scripts/validate_release_governance_v57.py` convierte esa policy en un gate ejecutable y produce `release-health.json` + `release-health.md`.

## Supply chain de GitHub Actions

Las Actions oficiales dejan de depender de referencias móviles y quedan fijadas a SHA completo, conservando el major en comentario para legibilidad:

- `actions/checkout` v6;
- `actions/setup-node` v6;
- `actions/setup-python` v7;
- `actions/configure-pages` v5;
- `actions/upload-pages-artifact` v4;
- `actions/deploy-pages` v4;
- `actions/upload-artifact` v7.

El validator bloquea:

- Actions remotas no inventariadas;
- referencias no fijadas a SHA completo;
- SHA distinto al aprobado por policy;
- `pull_request_target`;
- `permissions: write-all`;
- desaparición de los workflows obligatorios o de sus timeouts/concurrency.

## Permisos y credenciales

Los checkouts de jobs de solo lectura usan `persist-credentials: false`.

Las credenciales se conservan únicamente donde la función exige escritura:

- builder canónico, que publica outputs generados;
- Graphify, que publica `knowledge/graphify-live`;
- snapshot, que promueve `stable`.

Los permisos continúan definidos por workflow/job según necesidad y están protegidos por la policy v5.7.

## Dependencias controladas

Dependabot queda configurado para npm y GitHub Actions:

- frecuencia semanal;
- máximo dos PR abiertos por ecosistema;
- actualizaciones minor/patch;
- upgrades major automáticos bloqueados.

Las dependencias QA continúan fijadas exactamente:

- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1;
- Node >=22.

No se realizó una actualización masiva de dependencias en v5.7.

## Health y mantenimiento preventivo

Se añadió `Release governance health`, ejecutable en PR, manualmente y por schedule.

Además, `Actions hygiene` limpia de forma acotada runs canónicos queued huérfanos y se aplaza cuando existe un `Site Quality and Deploy` activo o queued, evitando competir con una certificación pública.

Antes de promover `stable`, el snapshot genera el artefacto `release-governance-health-v57`.

## Compatibilidad histórica

La adopción de SHA pinning reveló dos contratos históricos demasiado literales:

- v5.5 esperaba `actions/setup-node@v6` como texto exacto;
- v5.6 esperaba exactamente cuatro usos literales de `actions/upload-artifact@v7`.

Se corrigieron de forma ascendente:

- v5.5 acepta el major histórico o el SHA v6 exacto declarado por la policy v5.7;
- v5.6 exige como mínimo sus cuatro cargas históricas v7, reconoce el SHA aprobado y permite artefactos adicionales de releases posteriores.

No se debilitó ningún budget, navegador, superficie o gate funcional.

El workflow de governance ahora ejecuta preventivamente v5.5 + v5.6 + v5.7 cuando cambian estos contratos.

## Evidencia funcional de la fundación

Run: `31534382576`.

SHA certificado antes del cierre documental:

`945abb9c4e35c87d4f9a9ecd5ff161707b7d716e`

La cadena aprobó:

- idempotencia canónica;
- validadores v4.4→v5.7;
- JavaScript y JSON;
- GitHub Pages;
- smoke público;
- Lighthouse;
- Browser E2E + axe;
- release-health;
- promoción de `stable`.

Al terminar esa certificación, `main == stable == 945abb9c4e35c87d4f9a9ecd5ff161707b7d716e`.

Los refs actuales siguen siendo la autoridad y deben consultarse dinámicamente.

## Browser E2E + axe

Resultado limpio de la tentativa certificada:

- 37 tests observados;
- 35 passed;
- 2 skipped por diseño;
- 0 fallos;
- 0 retries;
- 7 superficies axe sin violaciones serias/críticas.

### Incidencia de infraestructura

La primera tentativa del job Browser agotó el wrapper `timeout 360s` durante `playwright install --with-deps chromium webkit` por lentitud transitoria del mirror Ubuntu. **Los tests no llegaron a ejecutarse y `stable` no se movió.**

Se reejecutó el job sobre un runner limpio. La instalación terminó dentro del margen y la suite completa aprobó 35/2/0/0.

No se aumentó el timeout ni se retiró WebKit/Chromium porque la evidencia mostró una incidencia transitoria de infraestructura, no una incompatibilidad estructural.

## Lighthouse

Las seis superficies aprobaron con una sola muestra; ninguna activó la verificación mediana-de-tres.

| Superficie | Performance | A11y | LCP | CLS | TBT | Bytes |
|---|---:|---:|---:|---:|---:|---:|
| home | 1.00 | 0.97 | 1484 ms | 0 | 62 ms | 73,826 |
| solution-ai | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,283 |
| product-ai | 1.00 | 1.00 | 1005 ms | 0 | 0 ms | 33,096 |
| sector-tech | 0.98 | 1.00 | 996 ms | 0.087 | 0 ms | 24,292 |
| perspective-ai | 0.98 | 1.00 | 916 ms | 0.087 | 0 ms | 25,874 |
| demo | 1.00 | 1.00 | 986 ms | 0 | 0 ms | 21,931 |

Resultado: 6/6 dentro de `quality-budgets-v55.json`, sin relajación.

## Interpretación de tiempo CI

El resumen del run `31534382576` registró 634 s porque la medición abarca la primera tentativa Browser fallida por el mirror y su reejecución. Ese valor **no es comparable** con el baseline limpio v5.5 ni con el run limpio v5.6 y no se usa como nueva referencia de rendimiento.

Los gates de la tentativa exitosa conservaron la arquitectura paralela de v5.6. No se modificó la topología para ocultar la incidencia.

## Invariantes preservados

v5.7 mantiene obligatoriamente:

- 37 entradas E2E;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- Chromium fijado por Playwright para Lighthouse;
- política mediana-de-tres únicamente para métricas de laboratorio verificables;
- gate dual `browser_e2e` + `lighthouse_quality` antes de `stable`;
- idempotencia canónica;
- prohibición de reducir cobertura o relajar budgets para hacer pasar una candidata.

## Política de cierre

El commit documental que declara `5.7.0` solo constituye el cierre definitivo cuando vuelve a atravesar la certificación pública completa y `main == stable`.

La evidencia histórica de este documento demuestra la fundación funcional; los refs actuales, Pages, gates y `knowledge/graphify-live/graphify-out/BUILD_META.json.source_commit` determinan el estado vigente.

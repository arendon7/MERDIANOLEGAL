# Meridiano Legal · Web canónica v5.6.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.6 conserva íntegra la arquitectura jurídica, comercial, CRO, SEO, privacidad y los gates Browser E2E + axe + Lighthouse de v5.5, y mejora **la eficiencia y la observabilidad del pipeline sin reducir cobertura ni relajar presupuestos**.

## Estado actual

La publicación conserva **46 páginas HTML**:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 1 hub de soluciones y 6 rutas de decisión empresarial;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- página institucional de Firma;
- Centro Demo;
- Meridiano Empresas con datos ficticios y `noindex,nofollow`.

URL pública canónica:

`https://arendon7.github.io/MERDIANOLEGAL/`

Política de release:

- `main`: fuente/candidata vigente;
- `stable`: último commit que aprobó construcción, idempotencia, validadores, Pages, smoke, Browser E2E, axe y Lighthouse.

Una candidata puede estar temporalmente publicada y seguir sin estar certificada. `stable` se mueve únicamente después de todos los gates.

## v5.6 · Eficiencia de CI y observabilidad

La cadena pública conserva todos los controles de v5.5, pero cambia su topología:

```text
quality
  ↓
deploy
  ↓
live_smoke
  ├──→ browser_e2e ───────┐
  └──→ lighthouse_quality ├──→ snapshot / stable
                          ┘
```

Después del smoke, Browser E2E/axe y Lighthouse se ejecutan como **gates paralelos e independientes**. `stable` exige que ambos terminen en `success`.

### Lo que no se redujo

- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- siete superficies axe;
- seis superficies Lighthouse;
- 37 entradas Playwright;
- workers de Playwright en CI: 1;
- presupuestos de performance/accesibilidad de v5.5.

`quality-budgets-v55.json` permanece como contrato vigente:

- performance >= 0.70;
- accesibilidad >= 0.90;
- LCP <= 4000 ms;
- CLS <= 0.15;
- TBT <= 350 ms;
- transferencia <= 1.5 MB.

## Resultado funcional certificado

Run de certificación v5.6: `31458580456`.

Candidata funcional certificada antes del cierre documental:

`c4f48e43a1681cdbd24db4c6308878efeb801700`

### Browser E2E + axe

- 37 tests observados;
- 35 `passed`;
- 2 `skipped` por diseño;
- 0 fallos;
- 0 tests con retry;
- siete auditorías axe sin violaciones serias/críticas.

### Lighthouse

Las seis superficies aprobaron con **una sola muestra**; la verificación mediana-de-tres no tuvo que activarse.

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1239 ms | 0 | 0 ms | 73,834 B |
| Solución IA | 1.00 | 1.00 | 964 ms | 0 | 0 ms | 23,235 B |
| Producto IA | 1.00 | 1.00 | 911 ms | 0 | 0 ms | 33,351 B |
| Sector tecnología | 1.00 | 1.00 | 935 ms | 0 | 0 ms | 24,272 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,985 B |
| Demo | 1.00 | 1.00 | 944 ms | 0 | 0 ms | 22,003 B |

## Mejora de tiempo medida

`ci-baseline-v56.json` fija como baseline el run v5.5 `31433199058` y usa una métrica comparable: desde el inicio de `quality` hasta que quedan habilitados todos los gates previos a `stable`.

- baseline v5.5: **279 s**;
- v5.6 final funcional: **160 s**;
- mejora: **42.7%**;
- objetivo interno v5.6: 20%.

La mejora no se usa como threshold rígido de release: sirve como observabilidad. La seguridad de publicación sigue dependiendo de los gates funcionales.

## Cómo se obtuvo la mejora

### 1. Gates de navegador en paralelo

Antes, Lighthouse esperaba a que terminara Browser E2E. Desde v5.6 ambos arrancan después del mismo smoke y `stable` espera los dos resultados.

### 2. Caché npm segura

`actions/setup-node@v6` reutiliza la caché del package manager con `package-lock.json`. No se cachean `node_modules` ni binarios Playwright.

### 3. Chromium comparable para Lighthouse

Lighthouse usa el Chromium fijado por la misma versión de Playwright del proyecto. Su job instala únicamente Chromium, sin WebKit y sin repetir `--with-deps`.

Esto conserva comparabilidad con la certificación v5.5 y evita depender de la versión mutable de Google Chrome incluida en la imagen del runner.

### 4. Menos ciclos canónicos redundantes

Los commits automáticos `build: sincroniza sitio público canónico` quedan reconocidos por la cadena para no abrir una nueva ronda útil de construcción/certificación cuando el único cambio es el output ya generado.

Si el builder comprueba que los outputs ya están canónicos, termina sin crear un commit adicional.

### 5. Observabilidad compacta

- Playwright publica conteos, retries y tiempo mediante `ci-summary-reporter.mjs`.
- Lighthouse publica `summary.json` y `summary.md`.
- el snapshot publica `ci-certification-summary-v56` con tiempos por gate y comparación contra baseline.
- los artefactos directos de QA usan `actions/upload-artifact@v7`.

## Robustez Lighthouse sin relajar budgets

Durante el desarrollo, una ejecución experimental con el Chrome mutable del runner produjo un TBT aislado de 497 ms en portada. El análisis comparativo mostró que v5.5 usaba el Chromium fijado por Playwright.

La release final restaura ese browser comparable y añade una política acotada contra outliers de laboratorio:

- a11y y peso son fallos no reintentables;
- solo performance, LCP, CLS y TBT pueden activar verificación;
- únicamente si **todos** los fallos iniciales pertenecen a esas métricas;
- se ejecutan exactamente dos muestras adicionales;
- deben existir tres muestras válidas;
- la decisión se toma por mediana de tres, nunca por el mejor resultado;
- los presupuestos permanecen exactamente iguales.

En el run funcional final no fue necesario activar esta verificación.

## Cadena de aprobación vigente

1. construcción canónica;
2. segunda pasada idempotente;
3. validadores v4.4→v5.6;
4. JavaScript y JSON;
5. GitHub Pages;
6. smoke público;
7. Browser E2E + axe;
8. Lighthouse + budgets;
9. resumen de certificación;
10. promoción de `stable`.

## Memoria de ingeniería · Graphify + Obsidian

Meridiano mantiene continuidad estructural mediante:

- `AGENTS.md`;
- `knowledge/HOME.md`;
- `knowledge/00_CANON/`;
- `knowledge/10_DECISIONES/`;
- `knowledge/20_ARQUITECTURA/`;
- `knowledge/30_RUNBOOKS/`;
- `knowledge/99_HANDOFF/`;
- rama regenerable `knowledge/graphify-live` con `BUILD_META.json`, snapshot, reporte y wiki.

Graphify se utiliza para reducir el conjunto de impacto; `main` y los tests siguen siendo la autoridad funcional. Los cambios exclusivamente de memoria regeneran Graphify sin desplegar de nuevo la web.

## Integraciones externas: estado verdadero

Activas:

- GitHub Pages;
- WhatsApp como canal real de contacto;
- contexto comercial de navegación;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- pipeline canónico, smoke, Browser E2E, axe, Lighthouse y `stable`.

Preparadas pero **no activas** sin configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor externo de analítica;
- CRM/backend de leads;
- almacenamiento servidor del formulario;
- email transaccional.

## Documentación

- `RELEASE-v5.6.md`: cierre técnico de esta release.
- `RELEASE-v5.5.md`: performance y accesibilidad.
- `RELEASE-v5.4.md`: Browser E2E.
- `CHANGELOG.md`: historial de capas anteriores.
- `knowledge/HOME.md`: entrada a la memoria operativa.

## Principios vigentes

- No reducir cobertura para acelerar CI.
- No relajar presupuestos para hacer pasar una candidata.
- No tomar el mejor resultado de una serie de métricas volátiles.
- No mover `stable` con un gate rojo.
- No inventar integraciones, clientes, testimonios ni resultados.
- Usar Graphify para navegar; usar `main`, Pages y pruebas para decidir.

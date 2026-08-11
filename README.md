# Meridiano Legal · Web canónica v5.8.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. La v5.8 conserva la arquitectura jurídica, comercial, CRO, SEO, privacidad y los gates Browser E2E + axe + Lighthouse, y añade **arquitectura de decisión y claridad de compra derivada de las fuentes jurídicas, sin reducir cobertura ni relajar presupuestos**.

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
- `stable`: último commit que aprobó construcción, idempotencia, validadores, Pages, smoke, Browser E2E, axe, Lighthouse y release-health.

Una candidata puede estar temporalmente publicada y seguir sin estar certificada. `stable` se mueve únicamente después de todos los gates.

## v5.8 · Arquitectura de decisión y claridad de compra

v5.8 reduce el esfuerzo necesario para responder “¿esto es para mí?” y “¿qué compro exactamente?” sin crear una segunda fuente de marketing.

### Cuatro formas de contratar

La portada incorpora un selector que diferencia:

- entender primero el problema;
- contratar un resultado cerrado;
- obtener dirección jurídica recurrente;
- abordar una decisión o proyecto especializado.

Cada ruta apunta a superficies existentes y conserva la regla de que el visitante puede empezar por su situación empresarial, no por el nombre técnico de un servicio.

### Lectura ejecutiva de las 16 fichas

Servicios y productos muestran cinco bloques antes del detalle técnico:

1. `ENCAJA SI`;
2. `QUÉ COMPRA`;
3. `QUÉ RECIBE`;
4. `QUÉ APORTA`;
5. `QUÉ NO ASUMIR`.

Los bloques se generan directamente desde `situations`, `perimeter`, `deliverables`, `requirements` y `limits` de `catalog-services-v42/` y `catalog-products-v41/`. Duración, modalidad y audiencia también provienen de esas fuentes.

`scripts/validate_decision_v58.py` comprueba la correspondencia fuente→resumen en las 16 fichas y exige que la capa quede fuera del contenedor mutable `#detail-page`, de modo que sobreviva al render JavaScript y siga disponible sin JavaScript.

## v5.7 · Release governance preservada

`release-governance-v57.json` sigue siendo el contrato versionado de:

- Actions oficiales permitidas y sus SHA exactos;
- majors validados de cada Action;
- runtimes Node/Python/uv/Graphify;
- dependencias QA exactas;
- workflows requeridos;
- permisos esperados;
- invariantes de Browser, axe, Lighthouse y `stable`.

`scripts/validate_release_governance_v57.py` aplica ese contrato dentro del quality gate y genera un reporte reutilizable `release-health`.

### Supply chain

Las Actions oficiales se fijan a SHA completo y conservan su major documentado. El validator bloquea referencias móviles, Actions no inventariadas, SHA fuera de policy, `pull_request_target` y `permissions: write-all`.

Los checkouts de solo lectura usan `persist-credentials: false`; únicamente conservan credenciales los jobs que realmente deben publicar outputs o promover `stable`.

### Dependencias

Dependabot revisa semanalmente npm y GitHub Actions, con máximo dos PR abiertos por ecosistema y upgrades automáticos limitados a minor/patch. Los cambios major requieren decisión y certificación independiente.

La suite QA continúa fijada en:

- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1;
- Node >=22.

El `package.json` conserva su versión interna QA 5.5.0 porque identifica el contrato de herramientas, no la release pública del sitio.

### Mantenimiento preventivo

`Release governance health` se ejecuta por PR, schedule y manualmente. `Actions hygiene` limpia de forma acotada runs queued huérfanos y se aplaza cuando existe una certificación pública activa o queued.

Antes de mover `stable`, el snapshot genera `release-governance-health-v57`.

## Arquitectura de certificación

```text
quality + contrato v5.8
  ↓
deploy
  ↓
live_smoke
  ├──→ browser_e2e ──────┐
  └──→ lighthouse_quality ├──→ release-health → snapshot / stable
                          ┘
```

Después del smoke, Browser E2E/axe y Lighthouse son gates paralelos e independientes. Ninguno sustituye al otro.

### Cobertura protegida

- 37 entradas Playwright;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- workers de Playwright en CI: 1;
- budgets de `quality-budgets-v55.json` sin relajación.

Presupuestos vigentes:

- performance >= 0.70;
- accesibilidad >= 0.90;
- LCP <= 4000 ms;
- CLS <= 0.15;
- TBT <= 350 ms;
- transferencia <= 1.5 MB.

## Evidencia funcional v5.8

Certificación funcional final: run `31541197197`, SHA `681c252f09a50447af0557a2039b34b8a79faed9`.

### Browser E2E + axe

- 37 tests observados;
- 35 `passed`;
- 2 `skipped` por diseño;
- 0 fallos;
- 0 retries;
- 7 superficies axe sin violaciones serias/críticas.

La nueva arquitectura se prueba dentro de la cobertura existente: el navegador verifica el selector de cuatro modalidades en portada y las cinco tarjetas ejecutivas de una ficha profunda después del render JavaScript.

### Lighthouse

Las seis superficies aprobaron con una sola muestra y sin activar mediana-de-tres:

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1425 ms | 0 | 0 ms | 76,009 B |
| Solución IA | 1.00 | 1.00 | 978 ms | 0 | 0 ms | 23,234 B |
| Producto IA | 1.00 | 1.00 | 909 ms | 0 | 0 ms | 35,406 B |
| Sector tecnología | 1.00 | 1.00 | 938 ms | 0 | 0 ms | 24,260 B |
| Perspectiva IA | 1.00 | 1.00 | 1003 ms | 0 | 0 ms | 25,728 B |
| Demo | 1.00 | 1.00 | 970 ms | 0 | 0 ms | 22,045 B |

### Eficiencia

- baseline v5.5: 279 s;
- certificación funcional v5.8: 232 s hasta gate de `stable`;
- mejora frente al baseline: 16.8%;
- cobertura reducida: no;
- budgets relajados: no.

## Regresiones que los gates bloquearon durante v5.8

Antes de la certificación final se detectaron y corrigieron dos incompatibilidades:

- un parser histórico v4.5 asumía indentación exacta y rompía la segunda pasada idempotente;
- el primer bloque ejecutivo estaba dentro de `#detail-page` y el runtime de producto lo reemplazaba después de cargar JavaScript.

En ambos casos `stable` permaneció inmóvil. Se corrigieron los generadores y se reforzó el validator; no se debilitó ninguna prueba.

## v5.6 · Eficiencia y observabilidad preservadas

v5.8 conserva la topología paralela introducida en v5.6. Lighthouse continúa usando Chromium fijado por Playwright. Para performance/LCP/CLS/TBT, un fallo exclusivamente de métricas de laboratorio puede activar exactamente dos muestras adicionales y decisión por mediana de tres; accesibilidad y peso no se reintentan.

## Cadena de aprobación vigente

1. construcción canónica;
2. segunda pasada idempotente;
3. validadores históricos v4.4→v5.7 + contrato fuente/runtime v5.8;
4. JavaScript y JSON;
5. GitHub Pages;
6. smoke público;
7. Browser E2E + axe;
8. Lighthouse + budgets;
9. resumen CI;
10. release-health v5.7;
11. promoción de `stable`.

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

Graphify reduce el conjunto de impacto; `main`, Pages, validadores y tests siguen siendo la autoridad funcional.

## Integraciones externas: estado verdadero

Activas:

- GitHub Pages;
- WhatsApp como canal real de contacto;
- contexto comercial de navegación;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- pipeline canónico, smoke, Browser E2E, axe, Lighthouse, governance health y `stable`.

Preparadas pero **no activas** sin configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor externo de analítica;
- CRM/backend de leads;
- almacenamiento servidor del formulario;
- email transaccional.

## Documentación

- `RELEASE-v5.8.md`: arquitectura de decisión, claridad de compra y evidencia de certificación.
- `RELEASE-v5.7.md`: gobierno de releases, dependencias y salud operativa.
- `RELEASE-v5.6.md`: eficiencia y observabilidad de CI.
- `RELEASE-v5.5.md`: performance y accesibilidad.
- `RELEASE-v5.4.md`: Browser E2E.
- `CHANGELOG.md`: historial de capas anteriores.
- `knowledge/HOME.md`: entrada a la memoria operativa.

## Principios vigentes

- No reducir cobertura para acelerar CI.
- No relajar presupuestos para hacer pasar una candidata.
- No tomar el mejor resultado de una serie de métricas volátiles.
- No mover `stable` con un gate rojo.
- No aceptar Actions nuevas o cambios de SHA fuera de la policy de governance.
- No automatizar upgrades major sin validación específica.
- No inventar integraciones, clientes, testimonios ni resultados.
- No duplicar como marketing una fuente jurídica que ya puede derivarse de forma determinista.
- Usar Graphify para navegar; usar `main`, Pages y pruebas para decidir.
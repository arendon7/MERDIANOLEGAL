# Meridiano Legal · Web canónica v5.9.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.9 conserva la arquitectura jurídica, comercial, CRO, SEO, privacidad y los gates Browser E2E + axe + Lighthouse, y añade **calificación comercial y preparación de propuesta sin CRM/backend ni almacenamiento servidor inventados**.

## Estado actual

La publicación conserva 46 páginas HTML:

- 8 servicios profesionales;
- 8 productos jurídicos de alcance cerrado;
- 5 planes recurrentes;
- 1 hub de soluciones y 6 rutas de decisión empresarial;
- 8 lecturas sectoriales;
- 6 perspectivas jurídicas;
- Firma, Centro Demo y Meridiano Empresas ficticio/noindex.

URL pública canónica:

`https://arendon7.github.io/MERDIANOLEGAL/`

Política de release:

- `main`: fuente/candidata vigente;
- `stable`: último commit que aprobó construcción, idempotencia, validadores, Pages, smoke, Browser E2E, axe, Lighthouse y release-health.

Una candidata puede estar temporalmente publicada sin estar certificada. `stable` solo se mueve al final de todos los gates.

## v5.9 · Calificación comercial y preparación de propuesta

El formulario público incorpora tres datos comerciales estructurados:

- momento de decisión;
- horizonte para decidir o iniciar;
- rango de inversión jurídica previsto, opcional.

Antes del handoff, el usuario ve un resumen con contexto, necesidad, momento, horizonte e inversión. La web sugiere un siguiente paso operativo —`Orientación inicial`, `Llamada de alcance` o `Propuesta estructurada`— sin aplicar scoring de valor ni rechazar leads automáticamente.

La clasificación no constituye asesoría jurídica, cotización, aceptación del encargo, reserva de disponibilidad ni promesa de resultado.

### Privacidad y handoff

La web sigue siendo estática:

- no almacena el formulario en servidor;
- no existe CRM/backend de leads activo;
- las respuestas de calificación se incorporan únicamente al mensaje que el usuario decide abrir en WhatsApp;
- el envío no es automático;
- la telemetría no debe contener nombre, correo, empresa ni texto libre del caso.

La capa se implementa mediante:

- `commercial-intake-v59.css`;
- `commercial-intake-v59.js`;
- `scripts/apply_commercial_intake_v59.py`;
- `scripts/validate_commercial_intake_v59.py`.

## v5.8 · Claridad de compra preservada

La portada mantiene cuatro formas de contratación y las 16 fichas profundas conservan los bloques `ENCAJA SI`, `QUÉ COMPRA`, `QUÉ RECIBE`, `QUÉ APORTA` y `QUÉ NO ASUMIR`, derivados directamente de las fuentes jurídicas existentes.

La cadena canónica debe terminar siempre en `v5.8 → v5.9`.

## v5.7 · Release governance preservada

`release-governance-v57.json` protege:

- Actions oficiales y SHA exactos;
- majors validados;
- runtimes Node/Python/uv/Graphify;
- dependencias QA exactas;
- workflows y permisos;
- 37 entradas Browser;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets y gate dual antes de `stable`.

Dependabot revisa npm y GitHub Actions semanalmente, con máximo dos PR abiertos por ecosistema y upgrades automáticos limitados a minor/patch. Los major requieren revisión explícita.

QA fijada:

- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1;
- Node >=22.

## Arquitectura de certificación

```text
quality + v5.8 + v5.9
  ↓
deploy
  ↓
live_smoke
  ├──→ browser_e2e ──────┐
  └──→ lighthouse_quality ├──→ release-health → snapshot / stable
                          ┘
```

Cobertura protegida:

- 37 entradas Playwright;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- workers Playwright CI = 1;
- budgets sin relajación: performance >= 0.70, accesibilidad >= 0.90, LCP <= 4000 ms, CLS <= 0.15, TBT <= 350 ms, transferencia <= 1.5 MB.

## Evidencia funcional v5.9 previa al cierre documental

Run `31547313170`, SHA `a64d2d957e3ca6c96fec855be85019680ebe6a03`.

Antes del cierre documental:

- `main == stable`;
- Browser: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 196 s hasta gate de `stable`;
- baseline v5.5: 279 s;
- mejora: 29.7%;
- cobertura reducida: no;
- budgets relajados: no.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1286 ms | 0 | 0 ms | 80,365 B |
| Solución IA | 1.00 | 1.00 | 1011 ms | 0 | 0 ms | 23,195 B |
| Producto IA | 1.00 | 1.00 | 1005 ms | 0 | 0 ms | 35,409 B |
| Sector tecnología | 0.98 | 1.00 | 1005 ms | 0.087 | 0 ms | 24,220 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,814 B |
| Demo | 1.00 | 1.00 | 1095 ms | 0 | 0 ms | 22,073 B |

## Regresiones bloqueadas durante v5.9

Los gates impidieron promover `stable` hasta corregir dos incompatibilidades de composición:

1. el generador histórico v4.9 esperaba una firma exacta del formulario y rechazaba el nuevo atributo v5.9; se hizo extensible sin debilitar su contrato;
2. el builder volvía a ejecutar v5.8 después de v5.9; se corrigió para terminar siempre en `v5.8 → v5.9`.

Governance ahora vigila el generador v4.9 y prueba explícitamente `v4.9 → v5.9`.

## Cadena de aprobación vigente

1. construcción canónica;
2. segunda pasada idempotente;
3. validadores históricos + v5.8 + v5.9;
4. JavaScript y JSON;
5. GitHub Pages;
6. smoke público;
7. Browser E2E + axe;
8. Lighthouse + budgets;
9. resumen CI;
10. release-health;
11. promoción de `stable`.

## Memoria de ingeniería · Graphify + Obsidian

La continuidad se apoya en `AGENTS.md`, `knowledge/HOME.md`, `knowledge/00_CANON/`, ADR, arquitectura, runbooks, handoff y la rama regenerable `knowledge/graphify-live`.

Graphify reduce el conjunto de impacto; `main`, Pages, validadores y tests siguen siendo la autoridad funcional.

## Integraciones externas: estado verdadero

Activas:

- GitHub Pages;
- WhatsApp como canal real de contacto;
- contexto comercial local/de sesión;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estático/noindex;
- pipeline canónico, smoke, Browser E2E, axe, Lighthouse, governance health y `stable`.

No activas sin configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor externo de analítica;
- CRM/backend de leads;
- almacenamiento servidor del formulario;
- email transaccional.

## Documentación

- `RELEASE-v5.9.md`: calificación comercial, handoff, privacidad y evidencia.
- `RELEASE-v5.8.md`: arquitectura de decisión y claridad de compra.
- `RELEASE-v5.7.md`: gobierno de releases y dependencias.
- `CHANGELOG.md`: historial de capas anteriores.
- `knowledge/HOME.md`: entrada a memoria operativa.

## Principios vigentes

- No reducir cobertura para acelerar CI.
- No relajar presupuestos para hacer pasar una candidata.
- No mover `stable` con un gate rojo.
- No aceptar Actions nuevas o SHA fuera de policy.
- No automatizar upgrades major sin validación específica.
- No inventar integraciones, clientes, testimonios ni resultados.
- No duplicar como marketing una fuente jurídica derivable de forma determinista.
- No transmitir PII en telemetría.
- Usar Graphify para navegar; usar `main`, Pages y pruebas para decidir.

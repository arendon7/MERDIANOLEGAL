# Meridiano Legal · Web canónica v5.10.0

Sitio público, responsive, static-first y autocontenido de Meridiano Legal, publicado mediante GitHub Pages. v5.10 conserva la arquitectura jurídica, comercial, CRO, SEO, privacidad y los gates Browser E2E + axe + Lighthouse, y añade **intención comercial contextual y una ruta explícita desde interés hasta propuesta, aceptación e inicio, sin CRM/backend inventado**.

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

## v5.10 · Conversión, propuesta y cierre

Las 16 fichas profundas transportan intención comercial al formulario:

- productos → solicitud de propuesta;
- servicios → definición de alcance.

El usuario puede cambiar la intención. El formulario mantiene la calificación v5.9 y presenta una ruta realista de cuatro etapas: `calificación → alcance/propuesta → aceptación → inicio`.

La web también explica la anatomía esperada de una propuesta —objetivo, perímetro, entregables, cronograma y supuestos/exclusiones— y deja claro que preparar una solicitud o abrir WhatsApp no equivale a contratación, aceptación del encargo, disponibilidad reservada ni promesa de resultado.

La capa se implementa mediante:

- `conversion-close-v510.css`;
- `scripts/apply_conversion_v510.py`;
- `scripts/validate_conversion_v510.py`.

## v5.9 · Calificación comercial preservada

El formulario mantiene momento de decisión, horizonte y rango de inversión jurídica opcional, más un resumen previo al handoff. No existe scoring de valor ni rechazo automático de leads.

La web sigue siendo estática:

- no almacena el formulario en servidor;
- no existe CRM/backend de leads activo;
- el envío a WhatsApp no es automático;
- la telemetría no contiene nombre, correo, empresa ni texto libre del caso.

## v5.8 · Claridad de compra preservada

La portada mantiene cuatro formas de contratación y las 16 fichas profundas conservan `ENCAJA SI`, `QUÉ COMPRA`, `QUÉ RECIBE`, `QUÉ APORTA` y `QUÉ NO ASUMIR`, derivados de las fuentes jurídicas existentes.

La secuencia comercial/canónica termina en `v5.8 → v5.9 → v5.10`. Los generadores históricos deben preservar atributos de capas posteriores.

## v5.7 · Release governance preservada

`release-governance-v57.json` protege Actions oficiales con SHA exactos, runtimes, dependencias, permisos, 37 entradas Browser, 7 superficies axe, 6 superficies Lighthouse, budgets y gate dual antes de `stable`.

QA fijada:

- `@playwright/test` 1.62.0;
- `@axe-core/playwright` 4.12.1;
- `lighthouse` 13.4.1;
- Node >=22.

## Arquitectura de certificación

```text
quality + v5.8 + v5.9 + v5.10
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
- budgets: performance >= 0.70, accesibilidad >= 0.90, LCP <= 4000 ms, CLS <= 0.15, TBT <= 350 ms, transferencia <= 1.5 MB.

## Evidencia funcional v5.10 previa al cierre documental

Run `31558953560`, SHA `f8b47f2ec2885cc39ff64a2448792f352619f9c3`:

- `main == stable` antes del cierre documental;
- Browser: 37 observados, 35 passed, 2 skipped, 0 failed, 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 dentro de presupuesto;
- CI: 173 s hasta gate de `stable`;
- baseline v5.5: 279 s;
- mejora: 38.0%;
- cobertura reducida: no;
- budgets relajados: no.

### Lighthouse

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Portada | 1.00 | 0.97 | 1250 ms | 0 | 0 ms | 84,524 B |
| Solución IA | 1.00 | 1.00 | 955 ms | 0 | 0 ms | 23,213 B |
| Producto IA | 1.00 | 1.00 | 905 ms | 0 | 0 ms | 35,506 B |
| Sector tecnología | 0.98 | 1.00 | 945 ms | 0.087 | 0 ms | 24,226 B |
| Perspectiva IA | 0.98 | 1.00 | 904 ms | 0.087 | 0 ms | 25,867 B |
| Demo | 1.00 | 1.00 | 903 ms | 0 | 0 ms | 22,040 B |

## Regresiones bloqueadas durante v5.10

Los gates impidieron promover `stable` hasta corregir:

1. una incompatibilidad de composición porque v5.9 no preservaba atributos posteriores del formulario;
2. un contraste WCAG insuficiente en `.close-legal-v510`.

Ambos problemas quedaron corregidos sin debilitar pruebas. El builder posterior confirmó `Canonical public files are current.` y Browser/axe terminó 35/2/0/0.

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
- email transaccional;
- firma electrónica, pagos, agenda o carga documental.

## Documentación

- `RELEASE-v5.10.md`: intención comercial, propuesta/cierre y evidencia.
- `RELEASE-v5.9.md`: calificación comercial y privacidad.
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

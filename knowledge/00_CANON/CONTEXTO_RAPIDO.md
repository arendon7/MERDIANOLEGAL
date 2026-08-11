# Meridiano Legal — Contexto rápido

Use esta nota para orientarse en menos de dos minutos antes de abrir archivos fuente.

## Qué es el proyecto

Sitio público y centro demostrativo de Meridiano Legal. La propuesta combina servicios jurídicos especializados, productos de alcance cerrado, planes recurrentes, rutas por necesidad, sectores, perspectivas y una experiencia demo estática.

## Arquitectura comercial vigente

- 8 servicios especializados.
- 8 productos de alcance cerrado.
- 5 planes recurrentes.
- 6 rutas de decisión en `soluciones/` más su hub.
- 8 sectores.
- 6 perspectivas desarrolladas más biblioteca.
- Firma/método y Centro Demo como superficies de autoridad y prueba pública.
- 4 formas de contratación en portada para orientar al usuario por tipo de necesidad.
- 5 bloques ejecutivos de compra en cada una de las 16 fichas profundas.

Principio comercial: el usuario puede empezar por su situación empresarial y no necesita conocer el nombre del servicio correcto.

## Diferenciaciones que no deben perderse

- Diagnóstico jurídico ≠ Auditoría Jurídica Empresarial Integral.
- Dirección Jurídica Externa ≠ disponibilidad jurídica ilimitada.
- Contratación Estratégica ≠ Sistema Contractual Empresarial.
- Sociedades/Gobierno/Inversión ≠ Empresa Lista para Inversión.
- Propiedad Intelectual como servicio ≠ paquete cerrado de activos protegidos.
- Gobernanza jurídica de IA como servicio ≠ programa cerrado de gobernanza.
- Proyecto regulado como servicio ≠ producto estructurado de alcance cerrado.
- Legal Operations ≠ Dirección Jurídica Externa: el primero transforma modelo operativo, procesos, documentos, datos y herramientas; el segundo aporta capacidad jurídica recurrente y gobierno de la agenda.

## Fuentes principales

- `catalog-products-v41/` — fuente de productos.
- `catalog-services-v42/` — fuente de servicios.
- `growth-solutions-v51.json` — rutas por necesidad.
- `cro-solutions-v52.json` — CRO, objeciones, FAQ e intención de búsqueda.
- `authority-v53.json` — autoridad, interlinking y semántica editorial.
- `measurement-contract-v53.json` — contrato de eventos sin PII.
- `commercial-v43.css` / `commercial-conversion-v44.js` — planes y conversión.
- `site-v3.js` + `catalog-home-v32.js` + `decision-flow.js` — runtime principal de portada.
- `decision-v58.css` — presentación de selector de contratación y claridad ejecutiva.
- `scripts/apply_decision_v58.py` — deriva la capa de compra directamente de las 16 fuentes jurídicas.
- `scripts/validate_decision_v58.py` — valida fuente→resumen y persistencia frente al runtime.
- `release-governance-v57.json` — policy versionada de Actions, runtimes, dependencias QA, permisos e invariantes.
- `scripts/validate_release_governance_v57.py` — validator y generador del release-health v5.7.
- `scripts/` — construcción, normalización y validación canónica.
- `tests/e2e/` — contrato funcional de navegador.

## Secuencia de release

El orden conceptual es:

fuentes → generadores/aplicadores históricos → capa de decisión v5.8 → normalizadores/validadores → idempotencia → Pages → smoke live → Playwright/axe/Lighthouse → release-health → `stable`.

Nunca promover `stable` antes de que todos los gates aplicables estén verdes.

## Estado actual resumido

- Versión declarada en cierre: v5.8.0.
- La implementación funcional v5.8 quedó certificada en el run `31541197197` sobre `681c252f09a50447af0557a2039b34b8a79faed9`.
- En esa certificación `main == stable`.
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries sobre 37 entradas.
- axe: 7 superficies sin violaciones serias/críticas.
- Lighthouse: 6/6 superficies dentro de budget; portada 1.00 performance / 0.97 a11y y producto IA 1.00 / 1.00.
- CI funcional: 232 s hasta el gate de `stable`, 16.8% mejor que baseline v5.5 de 279 s.
- v5.8 añade cuatro formas de contratación y cinco bloques ejecutivos derivados de fuente en las 16 fichas.
- El validator v5.8 protege que esos bloques sobrevivan al render JavaScript y funcionen también static-first.
- v5.7 continúa protegiendo SHA pinning de Actions, permisos, dependencias QA, Dependabot controlado, higiene de runs y reporte `release-health`.
- Invariantes: 37 entradas E2E, 7 superficies axe, 6 superficies Lighthouse, budgets v5.5 y gate dual Browser + Lighthouse.
- El commit documental de cierre 5.8.0 solo es definitivo después de repetir la certificación y terminar nuevamente con `main == stable`.

## Cómo usar Graphify

Graphify no decide qué es correcto: reduce el espacio de búsqueda. Úselo para localizar módulos, llamadas, imports y comunidades; confirme después en `main` las fuentes relevantes.

La rama `knowledge/graphify-live` contiene:

- `graphify-out/BUILD_META.json` — frescura y métricas del snapshot;
- `graphify-out/PROJECT_SNAPSHOT.md` — resumen automático;
- `graphify-out/GRAPH_REPORT.md` — reporte estructural;
- `graphify-out/wiki/` — navegación por comunidades/módulos.

## Regla para respuestas rápidas y coherentes

Antes de explorar masivamente el repositorio, construir un conjunto mínimo de impacto a partir de esta nota + tarea activa + Graphify. Solo ampliar la lectura cuando exista una dependencia concreta o una validación que lo exija.
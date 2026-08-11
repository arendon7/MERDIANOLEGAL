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
- `release-governance-v57.json` — policy versionada de Actions, runtimes, dependencias QA, permisos e invariantes.
- `scripts/validate_release_governance_v57.py` — validator y generador del release-health v5.7.
- `scripts/` — construcción, normalización y validación canónica.
- `tests/e2e/` — contrato funcional de navegador.

## Secuencia de release

El orden conceptual es:

fuentes → generadores/aplicadores históricos → normalizadores → validadores → idempotencia → Pages → smoke live → Playwright/axe/Lighthouse → release-health → `stable`.

Nunca promover `stable` antes de que todos los gates aplicables estén verdes.

## Estado actual resumido

- Versión declarada: v5.7.0.
- La fundación funcional v5.7 quedó certificada en el run `31534382576` sobre `945abb9c4e35c87d4f9a9ecd5ff161707b7d716e` antes del cierre documental.
- El commit documental de cierre solo es definitivo después de atravesar la misma certificación pública y terminar con `main == stable`.
- Browser E2E/axe y Lighthouse continúan en paralelo tras deploy+smoke.
- v5.7 protege SHA pinning de Actions, permisos, dependencias QA, Dependabot controlado, higiene de runs y reporte `release-health`.
- Invariantes: 37 entradas E2E, 7 superficies axe, 6 superficies Lighthouse, budgets v5.5 y gate dual Browser + Lighthouse.
- La referencia temporal limpia continúa siendo v5.6: 160 s frente a baseline v5.5 de 279 s. El run v5.7 con reintento de infraestructura no se usa como benchmark comparable.
- `main` y `stable` deben verificarse dinámicamente antes de actuar.

## Cómo usar Graphify

Graphify no decide qué es correcto: reduce el espacio de búsqueda. Úselo para localizar módulos, llamadas, imports y comunidades; confirme después en `main` las fuentes relevantes.

La rama `knowledge/graphify-live` contiene:

- `graphify-out/BUILD_META.json` — frescura y métricas del snapshot;
- `graphify-out/PROJECT_SNAPSHOT.md` — resumen automático;
- `graphify-out/GRAPH_REPORT.md` — reporte estructural;
- `graphify-out/wiki/` — navegación por comunidades/módulos.

## Regla para respuestas rápidas y coherentes

Antes de explorar masivamente el repositorio, construir un conjunto mínimo de impacto a partir de esta nota + tarea activa + Graphify. Solo ampliar la lectura cuando exista una dependencia concreta o una validación que lo exija.

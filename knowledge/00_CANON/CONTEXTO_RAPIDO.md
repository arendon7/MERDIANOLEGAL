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
- `scripts/` — construcción, normalización y validación canónica.
- `tests/e2e/` — contrato funcional de navegador.

## Secuencia de release

El orden conceptual es:

fuentes → generadores/aplicadores históricos → normalizadores → validadores → idempotencia → Pages → smoke live → Playwright/axe/Lighthouse → `stable`.

Nunca promover `stable` antes de que todos los gates aplicables estén verdes.

## Estado actual resumido

- v5.4: última base certificada en `stable`.
- v5.5: candidata de Performance + Accessibility QA.
- Playwright + axe ya están verdes.
- Único bloqueo conocido: CLS de portada causado por `.hero-art`; Lighthouse observó ~0.304 frente a presupuesto <=0.15.

## Cómo usar Graphify

Graphify no decide qué es correcto: reduce el espacio de búsqueda. Úselo para localizar módulos, llamadas, imports y comunidades; confirme después en `main` las fuentes relevantes.

La rama `knowledge/graphify-live` contiene:

- `graphify-out/BUILD_META.json` — frescura y métricas del snapshot;
- `graphify-out/PROJECT_SNAPSHOT.md` — resumen automático;
- `graphify-out/GRAPH_REPORT.md` — reporte estructural;
- `graphify-out/wiki/` — navegación por comunidades/módulos.

## Regla para respuestas rápidas y coherentes

Antes de explorar masivamente el repositorio, construir un conjunto mínimo de impacto a partir de esta nota + tarea activa + Graphify. Solo ampliar la lectura cuando exista una dependencia concreta o una validación que lo exija.
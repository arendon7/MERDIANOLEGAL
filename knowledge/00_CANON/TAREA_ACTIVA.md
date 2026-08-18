# Meridiano Legal — Tarea activa

Actualizado: 2026-08-17.

## Estado

**Ciclo funcional activo: v6.0.0 — Experience System.**

Rama de implementación: `feat/v6-experience-system`.
Baseline técnico/documental: `main@56b6d179345966fd4fbb99159d9d1d12652c31d6`.
Snapshot funcional estable: v5.31.0 en `stable`; **stable no se mueve hasta certificación total de v6**.

## Problema observable

v5.31 resolvió la exposición simultánea de profundidad secundaria, pero la auditoría post-v5.31 confirmó una deuda distinta:

1. la primera lectura todavía exige comprender demasiada taxonomía interna —servicios, productos, planes y modalidades— antes de reconocer el problema empresarial;
2. contenidos con funciones distintas —decisión, entregable, proceso, perímetro, límite y evidencia— reciben tratamientos visuales demasiado equivalentes;
3. la presentación se ha sedimentado por releases incrementales: la Home carga 23 CSS y 13 JS, y las fichas profundas combinan múltiples generaciones de shell/visual/detail/decision/proof/offer/commercial/compression;
4. mobile evita overflow, pero parte de la densidad se traslada a stacks/carruseles en lugar de diseñarse específicamente;
5. `Centro demo` y otras acciones secundarias compiten con el siguiente paso comercial principal.

## Objetivo v6

Convertir Meridiano Legal en una interfaz jurídica de decisión coherente y client-first, preservando toda la profundidad y truth actual, mediante:

- arquitectura `situación → resultado → intervención → evidencia → contacto`;
- gramática semántica diferenciada para decisión, resultado, entregable, proceso, perímetro, límite, evidencia y profundidad;
- design system consolidado en lugar de nuevas capas versionadas de CSS;
- templates diferenciados para producto cerrado y servicio adaptable;
- mobile diseñado de forma específica;
- contacto perceptualmente simple con el mismo formulario físico y handoff manual;
- racionalización de CSS/JS de presentación sin perder contratos funcionales.

## Pilotos obligatorios

Wave 1:
1. Home desktop/mobile.
2. Auditoría Jurídica Empresarial Integral desktop/mobile.
3. Tecnología e Inteligencia Artificial desktop/mobile.
4. Contacto/handoff.

Solo después de su aceptación se propaga a las demás familias.

## Invariantes

- 46 HTML públicos salvo ADR explícito posterior; objetivo actual: conservar 46.
- 8 productos + 8 servicios.
- 7 superficies de soluciones —6 rutas + índice—.
- 8 sectores.
- 6 perspectivas internas.
- Un único formulario físico.
- WhatsApp manual.
- Sin portal real, auth, pagos, firma, upload o CRM ficticios.
- Funnel sin PII ni persistencia.
- Contacto/handoff no equivale a conversión, aceptación ni inicio.
- Profundidad jurídica completa preservada en DOM.
- 30 pasos exactos del builder; **no paso 31**.
- Idempotencia obligatoria.
- Release Governance, Graphify, Pages/smoke, Playwright, axe y Lighthouse sin relajación.
- `stable` solo después de gates verdes.

## No objetivos

v6 no pretende:
- convertir la web en SPA o adoptar framework por moda;
- crear backend/CRM/cuentas/pagos/carga documental;
- inventar precios, clientes, testimonios, métricas o resultados;
- sustituir profundidad jurídica por slogans;
- aprobar una nueva tipografía solo porque Figma usó Source Serif 4 como proxy;
- introducir motion decorativo antes de estabilizar IA/copy/layout;
- eliminar contratos de funnel/handoff/capability truth;
- migrar las 46 superficies en un único cambio no aislable.

## Acceptance bar

v6 solo puede certificarse si:
- truth parity de cantidades, límites, entregables y cierres: PASS;
- 46/46 superficies migradas al final del ciclo;
- 16/16 fichas profundas preservan depth y truth;
- 1/1 formulario físico;
- 30/30 pasos builder;
- idempotencia PASS;
- static validations PASS;
- Browser E2E PASS;
- axe serious/critical 0 en cobertura vigente;
- Lighthouse budgets PASS sin relajación;
- Pages + smoke PASS;
- Graphify alineado con `main`;
- stable se promueve únicamente al SHA final certificado.

## Plan de waves

### Wave 0 — Foundations
Tokens, shell, componentes semánticos, renderer/materializer v6, version gates y validators.

### Wave 1 — Pilotos
Home + Auditoría + IA + contacto/mobile.

### Wave 2 — 16 fichas
8 productos + 8 servicios.

### Wave 3 — Soluciones
6 rutas + índice.

### Wave 4 — Sectores
8 superficies sectoriales.

### Wave 5 — Perspectivas
6 internas + hub editorial.

### Wave 6 — Resto público
Firma, experiencia/demo, legales y 404, preservando su función específica.

## Fuente de diseño

El discovery aprobado está en `knowledge/20_DESIGN/` y el prototipo editable en Figma `Meridiano Legal — Rediseño post-v5.31`.

El design orchestrator y skills curados deben aplicarse contextual y secuencialmente: truth → UX/IA/a11y → visual/taste → motion/polish → QA.
# Inventario de presentación actual — baseline v5.31

Fecha: 2026-08-17
Baseline inspeccionado: `main@5fdca20b3837eab9ea2b2341b3d239660f48562f`.
Propósito: medir sedimentación antes de diseñar consolidación vNext.

## 1. Home — CSS cargado

`index.html` carga actualmente **23 hojas CSS**:

1. `site-v3.css`
2. `clarity-v31.css`
3. `commercial-v43.css`
4. `visual-v39.css`
5. `ux-v45.css`
6. `page-context.css`
7. `quality-v48.css`
8. `operations-v49.css`
9. `growth-v51.css`
10. `decision-v58.css`
11. `commercial-intake-v59.css`
12. `conversion-close-v510.css`
13. `engagement-v511.css`
14. `proof-v512.css`
15. `commercial-brief-v513.css`
16. `recommendation-v514.css`
17. `decision-action-v515.css`
18. `handoff-continuity-v517.css`
19. `offer-v522.css`
20. `professional-authority-v525.css`
21. `integral-v526.css`
22. `conversion-path-v528.css`
23. `funnel-trust-v529.css`

### Lectura

No todas son redundantes; varias codifican contratos reales. El problema es que **responsabilidad semántica y responsabilidad visual están mezcladas** y la cascada histórica funciona como arquitectura de composición.

vNext debe separar:
- truth/contract;
- behavior;
- presentation.

## 2. Home — JS cargado

El cierre actual de `index.html` carga **13 scripts JS**:

1. `site-v3.js`
2. `commercial-conversion-v44.js`
3. `commercial-intake-v59.js`
4. `commercial-brief-v513.js`
5. `recommendation-v514.js`
6. `decision-action-v515.js`
7. `handoff-continuity-v517.js`
8. `visual-v39.js`
9. `runtime-config.js`
10. `telemetry-v50.js`
11. `handoff-observability-v518.js`
12. `funnel-observability-v529.js`
13. `conversion-close-v510.js`

### Clasificación preliminar

#### Behavior/capability que puede seguir siendo necesario
- menu/navigation y modal/interaction base;
- form → WhatsApp manual;
- runtime config;
- observabilidad no PII;
- handoff continuity;
- funnel contract;
- close semantics.

#### Candidato a consolidación
Scripts cuyo papel principal sea:
- insertar markup ya materializable en build;
- duplicar decisiones de presentación;
- mantener compatibilidad de releases históricas;
- reconfigurar visualmente superficies después del HTML canónico.

No se eliminará ningún script solo por antigüedad. Cada retiro requiere contract parity + E2E.

## 3. Fichas profundas — ejemplo representativo

Una ficha v5.31 puede cargar conjuntamente:
- `catalog-v32.css`;
- `page-context.css`;
- `visual-v39.css`;
- `detail-v46.css`;
- `decision-v58.css`;
- `proof-v512.css`;
- `offer-v522.css`;
- `offer-commercial-v530.css`;
- `decision-compression-v531.css`.

La última capa v5.31 no reescribe la verdad; envuelve bloques históricos ya materializados. Esto fue correcto como release incremental, pero no debe convertirse en el patrón arquitectónico permanente.

## 4. Builder — 30 pasos exactos

El workflow `Build canonical public site` mantiene **30 pasos exactos** contando:
- setup/checkout;
- lockfile;
- shell/catalog renderers;
- enrichment/materializers históricos;
- commit final.

vNext no debe crear el paso 31.

La estrategia será:
- integrar renderer/design-system v6 dentro de un paso existente;
- version-gate materializadores históricos de presentación;
- conservar validators equivalentes o más estrictos;
- mantener idempotencia.

## 5. Sedimentación en markup

Ejemplo Home/contacto actual conserva simultáneamente:
- intake;
- recommendation;
- conversion-to-close;
- engagement readiness;
- contact compression;
- handoff continuity;
- post-contact depth.

Cada capa tiene una razón histórica válida. El rediseño debe **preservar sus contratos** sin exigir que todas sean bloques visuales autónomos permanentemente visibles.

## 6. Clasificación objetivo de dependencias v6

### A. Canon/truth
Permanecen como datos/documentación y no necesariamente como CSS/JS.

### B. Build-time render
Absorbe inserción de markup predecible y estructura semántica.

### C. Runtime essential
Solo interacción que requiere estado en navegador:
- navegación;
- formulario/handoff;
- observabilidad permitida;
- disclosures si necesitan enhancement, nunca en sustitución de HTML nativo.

### D. Presentation
Familia CSS consolidada.

## 7. Métricas de consolidación propuestas

Además de Lighthouse/axe:

- número de CSS requests Home;
- número de CSS requests fichas;
- bytes CSS transferidos;
- número de JS requests Home;
- bytes JS transferidos;
- count de clases/selectores v3–v5 cargados en output v6;
- count de exception mappings temporales;
- count de transformaciones regex activas sobre una ficha v6;
- DOM nodes por first-layer de Home/ficha;
- headings/landmarks;
- cantidad de CTAs visibles simultáneamente en first viewport.

No fijar budgets numéricos de reducción hasta medir artefactos actuales en CI; no inventar baseline.

## 8. Definition of success

La consolidación es exitosa cuando:
- la experiencia target puede renderizarse sin cadena histórica de overrides;
- contract truth se conserva;
- runtime JS disminuye o se racionaliza sin perder behavior;
- los validators detectan drift;
- dos builds consecutivos son idempotentes;
- browser/axe/Lighthouse continúan verdes;
- un cambio de componente semántico no obliga a conocer veinte generaciones de CSS.
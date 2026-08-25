# Meridiano Legal — Tarea activa

Actualizado: 2026-08-25.

## Baseline certificado

- `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
- Release productiva: **v7.4.0 — Commercial Evidence Readiness**.
- Capability truth v7.4 continúa vigente.
- `stable` no se modifica manualmente.

## Stack v8

### W4.1 — Client Architecture & Taxonomy
- PR draft #183.
- 46/46 superficies mapeadas.
- 6 prácticas + 8 soluciones + servicios continuos.

### W4.2 — Route Compatibility & SEO
- PR draft #184.
- route contract 46/46 + sitemap 43/43.
- CI PASS: run `32904478022`.
- `experiencia.html` modelada correctamente como `noindex`, coherente con v7.4.

### W4.3 — Renderer & Design-System Pilot Infrastructure
- PR draft #185.
- renderer source-driven sin escritura pública.
- truth parity en memoria para SO07 + PR02 + RC01.
- CSS v8 consolidado.
- gate de no activación: 46 HTML, 0 targets físicos, 0 HTML cargando CSS v8.
- CI PASS completo: run `32904520736`.

## Frente vigente

**W4.4 — Pilot Materialization Candidate.**

Rama: `design/v8-pilot-materialization-w44`.
Base lógica: W4.3.

Objetivo: probar targets HTML reales sin publicarlos ni comprometerlos todavía en el árbol canónico.

## Estrategia

CI materializa efímeramente tres targets dentro del checkout desechable:

1. `/soluciones/sistema-contractual-empresarial.html` — SO07.
2. `/practicas/corporativo-societario-gobierno.html` — PR02.
3. `/servicios-continuos/direccion-juridica-externa.html` — RC01.

Durante el job:

- topología temporal = 49 HTML (46 legacy + 3 targets);
- targets = `noindex,follow`;
- legacy pilots permanecen sin cambios;
- no se modifica sitemap;
- no hay canonical handoff;
- no hay deploy.

## Evidencia W4.4

### Materializador
`scripts/materialize_v8_pilot.py`

- requiere raíz explícita;
- escribir en checkout exige `--allow-working-tree`;
- materializa solo tres targets;
- no sobrescribe targets existentes;
- genera `.v8-pilot-materialization.json`.

### Validator materializado
`scripts/validate_v8_pilot_materialized.py`

Exige:

- manifest efímero;
- 3 targets exactos;
- 49 HTML temporales;
- canonical target;
- `noindex,follow`;
- 4 CSS v8;
- un H1;
- cero forms;
- cero internal links a `/productos/` o `/servicios/` desde targets;
- tres legacy pilots todavía disponibles.

### Browser E2E
`tests/e2e/v8-pilot-materialization.spec.mjs`

Comprueba en los tres targets:

- HTTP 200;
- semántica de familia;
- fuente canónica declarada;
- metadata/candidate boundary;
- CTA al formulario canónico;
- relacionados target;
- disclosure por teclado;
- no horizontal overflow;
- axe WCAG 2.1 AA sin serious/critical.

También comprueba 200 en los tres legacy pilots.

### CI
`.github/workflows/v80-pilot-materialization-candidate.yml`

Orden:

1. compile;
2. revalidar W4.2/W4.3 sobre 46 páginas;
3. materializar 3 targets efímeros;
4. validar topología temporal 49;
5. probar que los legacy no fueron reescritos;
6. npm locked dependencies;
7. Chromium + WebKit;
8. server local;
9. Playwright desktop/mobile/WebKit + axe.

## Boundary

W4.4 todavía NO:

- commitea target HTML;
- cambia `version.json`;
- cambia sitemap/robots;
- cambia Home/navigation;
- cambia canonical legacy;
- cambia Builder/Pages;
- despliega;
- habilita RC02 Meridiano Contratos;
- mueve `stable`.

## Siguiente decisión

Solo si W4.4 CI es PASS:

**W4.5 — Pilot Public-Tree Candidate** podrá evaluar comprometer los tres targets `noindex` en rama candidate, incorporar version-gating estructural y probar el builder sobre la topología nueva.

Si browser/axe falla, corregir primero renderer/design system y repetir W4.4.

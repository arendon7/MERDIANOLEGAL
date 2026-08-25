# Meridiano Legal — Tarea activa

Actualizado: 2026-08-25.

## Baseline certificado

- Repositorio: `arendon7/MERDIANOLEGAL`.
- `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
- Release productiva: **v7.4.0 — Commercial Evidence Readiness**.
- Analytics: `readiness-disabled`.
- Capability truth v7.4 permanece vigente mientras v8 está en diseño.
- `stable` no se modifica manualmente.

## Frente vigente

**W4.2 — v8 Route Compatibility & SEO Contract.**

Rama: `design/v8-route-compat-w42`.
Base lógica: `design/v8-client-architecture-w41`.

W4.2 convierte la arquitectura W4.1 en un contrato técnico verificable. No activa todavía nuevas rutas públicas ni mueve páginas históricas.

## W4.1 — estado

PR draft #183 contra `main`:

- ADR-008 de arquitectura/taxonomía;
- matriz 46/46;
- canon de 6 prácticas, 8 soluciones y servicios continuos;
- Meridiano Contratos bloqueado hasta capability contract verificable.

## Evidencia W4.2 materializada

### 1. Route contract estructurado

`assets/data/v8/route-contract-v80.json`

Declara:

- baseline v7.4;
- 46 legacy routes;
- 43 URLs del sitemap baseline;
- current → target;
- acción KEEP/RENAME/MOVE/MERGE;
- familia;
- indexación;
- sitemap;
- prioridad;
- 6 prácticas target;
- 8 soluciones target;
- 2 recurrentes target;
- RC02 Meridiano Contratos `publishable=false`.

### 2. Validator

`scripts/validate_route_contract_v80.py`

Debe demostrar:

- 46/46 rutas legacy cubiertas;
- árbol físico == contrato;
- 43/43 sitemap URLs == contrato baseline;
- self-canonical baseline para indexables;
- demo/404 noindex;
- 6 prácticas;
- 8 soluciones;
- 2 recurrentes;
- RC02 bloqueado;
- legacy removal prohibido antes de certificación;
- no asumir redirects de servidor en GitHub Pages.

### 3. Contrato técnico SEO/compatibilidad

`knowledge/20_DESIGN/V8-ROUTE-COMPATIBILITY-SEO.md`

Define:

- estrategia dual-route → canonical handoff → legacy alias;
- canonical policy;
- sitemap generado desde route contract al activar v8;
- breadcrumbs/schema por familia;
- internal linking a target routes;
- inventario de materializadores/validators afectados;
- nuevos invariantes v8;
- rollback a v7.4.

### 4. Gate CI

`.github/workflows/v80-route-contract-candidate.yml`

Ejecuta únicamente:

1. compilación del validator;
2. `validate_route_contract_v80.py`;
3. `canonical_pipeline_v524.py validate`.

No construye, despliega ni promueve `stable`.

## Hallazgos técnicos W4.2

### H1 — `validate_site.py`

Hardcodea topología v7: 16 fichas, 6 perspectivas, 8 sectores y rutas históricas.

### H2 — materializadores de catálogo

`build_catalog_shells.py` y `render_services_v42.mjs` dependen de `/productos/` y `/servicios/`.

### H3 — `/soluciones/`

Experience v6 trata esa carpeta como exactamente seis rutas de necesidad + hub. v8 la redefine como ocho soluciones canónicas, por lo que requiere version-gating y renderer v8.

### H4 — producción/SEO

`apply_production_v50.py` no recorre `soluciones/` ni futuras `practicas/` o `servicios-continuos/`; además no genera el sitemap, solo normaliza base URL.

### H5 — E2E

`public-site.spec.mjs` fija 16 fichas y old routes. No debe silenciarse: v8 necesita nuevos contratos y smoke legacy paralelo.

### H6 — pipeline

El pipeline conserva 30 pasos históricos y una extensión v6. W4.3 debe incorporar v8 mediante version-gating/extensión compartida Builder == Pages, sin inventar un paso histórico 31.

## Piloto definido para W4.3

Tres superficies representativas:

1. **SO07 — Sistema Contractual Empresarial**
   - legacy: `/productos/sistema-contractual-empresarial.html`;
   - target: `/soluciones/sistema-contractual-empresarial.html`.

2. **PR02 — Corporativo, Societario y Gobierno**
   - legacy: `/servicios/sociedades-gobierno-inversion.html`;
   - target: `/practicas/corporativo-societario-gobierno.html`.

3. **RC01 — Dirección Jurídica Externa**
   - legacy: `/servicios/direccion-juridica-externa.html`;
   - target: `/servicios-continuos/direccion-juridica-externa.html`.

RC02 Meridiano Contratos queda fuera del piloto.

## Siguiente frente — W4.3

**v8 Renderer & Design-System Pilot Infrastructure.**

Debe crear, antes de mover producción:

1. experience model v8 para las tres familias;
2. renderer v8 source-driven;
3. design tokens/componentes consolidados;
4. version gate en pipeline/materializadores históricos;
5. validator de truth parity para los tres pilotos;
6. target pages en candidate;
7. E2E target + smoke legacy;
8. desktop/mobile/keyboard/axe;
9. idempotencia;
10. rollback completo a v7.4.

## Definition of Done W4.2

- route contract estructurado;
- 46/46 legacy routes clasificadas y verificables;
- 43/43 sitemap baseline modelado;
- canonical/alias policy definida;
- sitemap target policy definida;
- validators/materializadores afectados inventariados;
- nuevos invariantes definidos;
- gate CI dedicado creado;
- piloto W4.3 seleccionado;
- RC02 bloqueado;
- `stable` intacta.

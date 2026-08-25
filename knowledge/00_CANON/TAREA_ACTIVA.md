# Meridiano Legal — Tarea activa

Actualizado: 2026-08-25.

## Baseline certificado

- Repositorio: `arendon7/MERDIANOLEGAL`.
- `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
- Release productiva: **v7.4.0 — Commercial Evidence Readiness**.
- Analytics: `readiness-disabled`.
- Capability truth v7.4 permanece vigente.
- `stable` no se modifica manualmente.

## Stack v8 abierto

### W4.1 — Client Architecture & Taxonomy

- rama: `design/v8-client-architecture-w41`;
- PR draft: #183;
- 46/46 superficies clasificadas;
- 6 prácticas + 8 soluciones + servicios continuos;
- ADR-008;
- RC02 Meridiano Contratos bloqueado hasta capability contract verificable.

### W4.2 — Route Compatibility & SEO Contract

- rama: `design/v8-route-compat-w42`;
- PR draft: #184, apilado sobre W4.1;
- `assets/data/v8/route-contract-v80.json`;
- 46 legacy routes + 43 sitemap URLs modeladas;
- canonical/alias/sitemap policy;
- `scripts/validate_route_contract_v80.py`;
- workflow candidate dedicado.

El workflow W4.2 aún no registra una ejecución en el SHA del PR apilado; no se declara PASS sin evidencia.

## Frente vigente

**W4.3 — v8 Renderer & Design-System Pilot Infrastructure.**

Rama: `design/v8-pilot-infrastructure-w43`.
Base lógica: W4.2.

W4.3 prepara el renderer y sistema visual sin activar nuevas superficies públicas.

## Pilotos exactos

1. **SO07 — Sistema Contractual Empresarial**
   - fuente: `catalog-products-v41/p07-contractual.json`;
   - legacy: `/productos/sistema-contractual-empresarial.html`;
   - target futuro: `/soluciones/sistema-contractual-empresarial.html`.

2. **PR02 — Corporativo, Societario y Gobierno**
   - fuente: `catalog-services-v42/s04-societario.json`;
   - legacy: `/servicios/sociedades-gobierno-inversion.html`;
   - target futuro: `/practicas/corporativo-societario-gobierno.html`.

3. **RC01 — Dirección Jurídica Externa**
   - fuente: `catalog-services-v42/s02-direccion.json`;
   - legacy: `/servicios/direccion-juridica-externa.html`;
   - target futuro: `/servicios-continuos/direccion-juridica-externa.html`.

RC02 Meridiano Contratos está fuera de W4.3.

## Evidencia W4.3 materializada

### Experience model

`assets/data/v8/experience-model-v80.json`

- referencia fuentes canónicas, no duplica contenido;
- diferencia `solution`, `practice`, `recurring`;
- preserva commercial intent/modality histórico de los tres pilotos;
- `commit_target_html=false`;
- `candidate_indexing=noindex`;
- `legacy_routes_unchanged=true`.

### Renderer

`scripts/render_v8_pilot.py`

- `--check`: render doble determinista + truth parity completa en memoria;
- `--preview SO07|PR02|RC01`: HTML a stdout;
- no tiene modo de escritura pública;
- traduce relacionados legacy usando el route contract;
- no crea segundo formulario;
- mantiene targets como `noindex` durante piloto.

### Design system

`assets/css/v8/`:

- `tokens.css`;
- `base.css`;
- `components.css`;
- `surfaces.css`.

Consolida identidad v6 en una gramática semántica y distingue solución/práctica/recurrente sin crear marcas separadas.

### Gate de no activación

`scripts/validate_v8_pilot_infra.py`

Exige:

- tres pilotos exactos;
- cuatro CSS v8;
- 46 HTML legacy intactos;
- targets v8 físicamente ausentes;
- cero HTML actual cargando CSS v8;
- renderer compilable;
- renderer `--check` PASS cuando CI pueda ejecutarlo.

### CI

`.github/workflows/v80-pilot-infra-candidate.yml`

Valida:

1. compile;
2. W4.2 route contract;
3. W4.3 pilot infra;
4. canonical pipeline manifest.

No construye ni despliega.

## Boundary W4.3

No se modifica:

- ningún HTML público;
- `index.html`;
- sitemap/robots/version;
- catálogos;
- CSS v6/v7;
- runtime JS;
- formulario;
- analítica/privacidad;
- Builder/Pages;
- `stable`.

## Siguiente frente — W4.4

**Pilot Materialization Candidate**, condicionado a evidencia CI real de W4.2/W4.3.

W4.4 deberá:

1. introducir version-gate v8 controlado;
2. materializar solo SO07, PR02 y RC01;
3. mantener los tres legacy completos;
4. targets `noindex` durante comparación;
5. añadir E2E target + smoke legacy;
6. validar desktop/mobile/keyboard/axe;
7. probar truth parity DOM;
8. probar dos pasadas idempotentes;
9. ejecutar crítica independiente;
10. solo después decidir canonical handoff.

## Definition of Done W4.3

- experience model source-driven;
- renderer no destructivo;
- truth parity en memoria como contrato;
- 4 CSS v8 consolidados;
- gate de no activación;
- CI candidate dedicado;
- 46 HTML productivos intactos;
- 0 targets físicos;
- RC02 fuera de scope;
- `stable` intacta;
- PR draft apilado abierto para revisión.

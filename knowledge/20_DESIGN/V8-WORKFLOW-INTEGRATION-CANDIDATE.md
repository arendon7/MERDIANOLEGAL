# W4.8 — v8 Workflow Integration Candidate

Fecha: 2026-08-25
Dependencia: W4.7 Pipeline Adapter Integration PASS (`32908858494`).
Estado inicial: committed candidate; sin deploy.

## Objetivo

Committear en una rama apilada exactamente los workflows Builder/Pages certificados por W4.7 y demostrar que los bytes, la regeneración desde base y toda la gobernanza siguen siendo equivalentes.

## Fuente de bytes

Artefacto W4.7:

- id `9585803169`;
- digest `sha256:05b5fffb77a40b9726c23536dfad28e5ea3b2151fed870c2746f31424ce18dd1`;
- Builder SHA-256 `6a002a1e6f9049bc9c98ad767c6aca9083c92f6847af3bc8ec78af534b5345ea`;
- Pages SHA-256 `3e3ab999ead2f094d7a0b26b2d430dd1bf5e414b224f9e6275f961000e25be01`.

## Doble prueba de identidad

W4.8 exige:

1. hash exacto de los dos archivos committeados contra el artefacto W4.7;
2. checkout del base SHA W4.7 en worktree temporal;
3. regeneración con `materialize_v8_pipeline_integration_candidate.py`;
4. `cmp` byte-for-byte entre la regeneración y los workflows W4.8.

## Gobernanza

Después de la paridad se ejecutan sobre los workflows realmente committeados:

- `canonical_pipeline_v524.py validate`;
- `validate_pages_trigger_v511.py`;
- `validate_ci_v56.py`;
- `apply_v8_builder_compat.py --check`;
- Pages Quality dual-view.

## Boundary

Aunque `build-canonical.yml` y `pages.yml` ya cambian en esta rama:

- Builder solo se dispara por push a `main`;
- Pages solo por dispatch o completion del Builder canónico;
- el PR W4.8 no ejecuta ninguno de los deploy jobs productivos;
- no cambia main/stable;
- no cambia versión, sitemap, robots, Home ni canonical legacy;
- no activa RC02.

## Gate de salida

- artifact hash parity PASS;
- base regeneration parity PASS;
- YAML PASS;
- governance PASS;
- Builder adapter PASS;
- Pages dual-view PASS;
- checkout idempotente;
- artefacto W4.8 publicado;
- main/stable intactos.

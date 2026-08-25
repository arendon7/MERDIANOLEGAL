# W4.7 — v8 Pipeline Adapter Integration Candidate

Fecha: 2026-08-25
Dependencia: W4.6 Pipeline Compatibility PASS (`32908333460`).
Estado final: **PASS**; producción intacta.
Run final: `32908858494`.
Job final: `97998709785`.

## Objetivo

Demostrar la forma exacta en que el adapter dual-view certificado en W4.6 puede integrarse en Builder y Pages reales sin modificar todavía los workflows productivos del branch ni ejecutar deploy.

## Builder adapter

`scripts/apply_v8_builder_compat.py`

Opera en dos modos:

- `apply`: materializa la extensión canónica legacy en una proyección de 46 HTML y sincroniza al árbol real únicamente outputs legacy allowlisted;
- `--check`: ejecuta la misma proyección y falla si existe cualquier output legacy pendiente.

Siempre preserva por hash los tres targets v8 aditivos.

## Integración derivada certificada

`scripts/materialize_v8_pipeline_integration_candidate.py`

Solo puede escribir en una raíz desechable distinta del checkout activo.

Builder candidate:

- mantiene exactamente 30 pasos nombrados;
- detecta contrato + 3 targets dentro del paso existente de lockfile;
- invoca el adapter `apply`;
- evita repetir `sync_public_version` y extensión v6 directa cuando el adapter está activo;
- conserva textualmente la secuencia histórica como fallback;
- conserva byte-identical la sección final de commit/push.

Pages candidate:

- integra `apply_v8_builder_compat.py --check` dentro del paso de idempotencia;
- conserva textualmente la secuencia histórica como fallback;
- Growth v5.1 usa el strict projection cuando v8 candidate está activo;
- conserva byte-identical toda la sección `deploy:` y release posterior.

## Gobernanza certificada

Sobre las copias integradas pasaron sin modificación los validators históricos:

- `canonical_pipeline_v524.py validate`;
- `validate_pages_trigger_v511.py`;
- `validate_ci_v56.py`;
- W4.6 compatibility;
- Builder adapter `--check`;
- Pages Quality dual-view.

También pasó el parse YAML de ambos workflows candidate.

## Resultado definitivo

Run `32908858494`, job `97998709785`: **SUCCESS**.

- W4.6 revalidation: PASS.
- Workflows productivos sin diff: PASS.
- Materialización integrada en `/tmp`: PASS.
- YAML parse: PASS.
- End-to-end governance: PASS.
- Checkout fuente sin diff: PASS.
- Artefacto `w47-v8-pipeline-integration-candidate`: publicado.
- Artifact id: `9585803169`.
- Artifact digest: `sha256:05b5fffb77a40b9726c23536dfad28e5ea3b2151fed870c2746f31424ce18dd1`.

## Boundary

W4.7 no modifica:

- `.github/workflows/build-canonical.yml`;
- `.github/workflows/pages.yml`;
- main;
- stable;
- version;
- sitemap/robots/Home;
- canonical legacy;
- deploy;
- RC02.

## Siguiente frente

W4.8 puede aplicar **exactamente el diff integrado certificado en W4.7** a Builder y Pages dentro de una nueva rama candidate. W4.8 deberá regenerar el W4.7 expected workflow desde su base y exigir byte parity con los workflows realmente committeados antes de cualquier consideración de merge o deploy.

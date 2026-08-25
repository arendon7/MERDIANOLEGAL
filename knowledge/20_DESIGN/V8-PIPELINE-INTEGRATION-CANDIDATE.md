# W4.7 — v8 Pipeline Adapter Integration Candidate

Fecha: 2026-08-25
Dependencia: W4.6 Pipeline Compatibility PASS (`32908333460`).
Estado inicial: candidate derivado; producción intacta.

## Objetivo

Demostrar la forma exacta en que el adapter dual-view certificado en W4.6 puede integrarse en Builder y Pages reales sin modificar todavía los workflows productivos del branch ni ejecutar deploy.

## Builder adapter

`scripts/apply_v8_builder_compat.py`

Opera en dos modos:

- `apply`: materializa la extensión canónica legacy en una proyección de 46 HTML y sincroniza al árbol real únicamente outputs legacy allowlisted;
- `--check`: ejecuta la misma proyección y falla si existe cualquier output legacy pendiente.

Siempre preserva por hash los tres targets v8 aditivos.

## Integración derivada

`scripts/materialize_v8_pipeline_integration_candidate.py`

Solo puede escribir en una raíz desechable distinta del checkout activo.

En Builder candidate:

- conserva exactamente 30 pasos nombrados;
- detecta contrato + 3 targets dentro del paso existente de lockfile;
- ejecuta `apply_v8_builder_compat.py` en modo candidate;
- evita repetir `sync_public_version` y extensión v6 directa cuando el adapter está activo;
- conserva textualmente la secuencia histórica como fallback;
- conserva intacta la sección final de commit/push.

En Pages candidate:

- integra `apply_v8_builder_compat.py --check` dentro del paso existente de idempotencia;
- conserva textualmente toda la secuencia histórica como fallback;
- Growth v5.1 pasa por `validate_v8_pipeline_compat.py` cuando candidate está activo;
- conserva intacta toda la sección `deploy:` y release posterior.

## Gobernanza

El candidate debe seguir pasando, sin modificar los validators históricos:

- `canonical_pipeline_v524.py validate`;
- `validate_pages_trigger_v511.py`;
- `validate_ci_v56.py`;
- W4.6 compatibility;
- Builder adapter `--check`;
- Pages Quality dual-view.

## Boundary

W4.7 no modifica todavía:

- `.github/workflows/build-canonical.yml`;
- `.github/workflows/pages.yml`;
- main;
- stable;
- version;
- sitemap/robots/Home;
- canonical legacy;
- deploy;
- RC02.

Las dos versiones integradas se generan en `/tmp`, se validan y se publican únicamente como artefacto de revisión.

## Gate de salida

1. W4.6 PASS.
2. Workflows productivos sin diff contra base.
3. Materialización candidate PASS.
4. YAML parse PASS.
5. Builder mantiene 30 pasos.
6. Manifiesto canónico Builder==Pages PASS.
7. Trigger Pages PASS.
8. CI v5.6 PASS.
9. Adapter `--check` PASS.
10. Pages Quality dual-view PASS.
11. Builder commit/push y Pages deploy byte-identical respecto a producción.
12. Artefacto candidate publicado.

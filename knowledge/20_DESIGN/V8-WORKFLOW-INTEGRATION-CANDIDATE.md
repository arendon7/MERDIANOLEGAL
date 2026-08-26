# W4.8 — v8 Workflow Integration Candidate

Fecha: 2026-08-25
Dependencia: W4.7 Pipeline Adapter Integration PASS (`32908858494`).
Estado final: **PASS**; workflows integrados en branch candidate, sin deploy.
Run final: `32909238315`.
Job final: `97999828834`.

## Objetivo

Committear en una rama apilada exactamente los workflows Builder/Pages certificados por W4.7 y demostrar que los bytes, la regeneración desde base y toda la gobernanza siguen siendo equivalentes.

## Fuente de bytes

Artefacto W4.7:

- id `9585803169`;
- digest `sha256:05b5fffb77a40b9726c23536dfad28e5ea3b2151fed870c2746f31424ce18dd1`;
- Builder SHA-256 `6a002a1e6f9049bc9c98ad767c6aca9083c92f6847af3bc8ec78af534b5345ea`;
- Pages SHA-256 `3e3ab999ead2f094d7a0b26b2d430dd1bf5e414b224f9e6275f961000e25be01`.

## Doble prueba de identidad certificada

1. Hash exacto de ambos workflows contra el artefacto W4.7: PASS.
2. Checkout detached del base W4.7: PASS.
3. Regeneración con el patcher certificado: PASS.
4. `cmp` byte-for-byte regenerado vs committeado: PASS.
5. Parse YAML de los dos workflows reales: PASS.

## Gobernanza certificada

Sobre los workflows committeados pasaron:

- `canonical_pipeline_v524.py validate`;
- `validate_pages_trigger_v511.py`;
- `validate_ci_v56.py`;
- `apply_v8_builder_compat.py --check`;
- Pages Quality dual-view.

El checkout terminó sin diff.

## Resultado definitivo

Run `32909238315`, job `97999828834`: **SUCCESS**.

Artefacto W4.8:

- id `9585929386`;
- digest `sha256:53125e3daea2c2e6d7e6163a2c9236c7467ccc7d3fd7dbb8c1d4aca7d566b806`.

## Boundary

Aunque `build-canonical.yml` y `pages.yml` están integrados en esta rama:

- Builder continúa disparándose solo por push a `main`;
- Pages continúa por dispatch o completion del Builder canónico;
- W4.8 no ejecutó deploy;
- no cambió main/stable;
- no cambió versión, sitemap, robots, Home ni canonical legacy;
- RC02 continúa fuera de alcance.

## Siguiente frente

W4.9 debe ejecutar una **shadow run operacional** de la lógica integrada Builder → Pages Quality → artifact, sustituyendo commit/push y deploy por comprobaciones y artefactos. El objetivo es demostrar el comportamiento efectivo del pipeline integrado antes de cualquier merge a `main`.

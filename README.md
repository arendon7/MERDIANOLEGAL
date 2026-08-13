# Meridiano Legal · Web canónica v5.24.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v5.24.0 — orquestación canónica verificable**.

- SHA funcional certificado: `73ba88fda16545cc3a257594b2a91d67a9c848b6`.
- Run final: `31739813251`.
- 46 HTML, 16 fichas profundas y 1 formulario físico canónico.
- Browser E2E + axe: 58 observados → 56 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; performance y accesibilidad 1.00 en las seis superficies.
- Home: LCP 1421 ms, CLS 0, TBT 42 ms.
- CI hasta `stable`: 196 s; mejora 29.7% frente al baseline de 279 s.
- Cobertura reducida: no. Budgets relajados: no.

## v5.24

`scripts/canonical_pipeline_v524.py` declara 30 pasos de composición y exige que las dos rutas canónicas ejecuten los mismos comandos en el mismo orden.

`builder == segunda pasada == manifiesto`

No se rediseñó la web ni se añadieron capacidades externas. Los contratos comerciales v5.20–v5.23, el handoff manual, la telemetría local sin PII y la frontera demo/capacidad permanecen vigentes.

## Documentación

- `RELEASE-v5.24.md`: contrato, incidencias, métricas, artefactos y digests.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: tarea vigente/cierre.
- `knowledge/HOME.md`: navegación de memoria.

Graphify es memoria derivada; `main`, `stable`, Pages, validadores y tests deciden.

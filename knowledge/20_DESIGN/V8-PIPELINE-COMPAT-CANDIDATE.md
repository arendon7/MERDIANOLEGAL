# W4.6 — v8 Pipeline Compatibility Candidate

Fecha: 2026-08-25
Dependencia: W4.5 Public-Tree Candidate PASS (`32907133921`).
Estado final: **PASS**; sin deploy.
Run final: `32908333460`.
Job final: `97997137990`.

## Objetivo

Demostrar que el árbol físico W4.5 de `49 HTML = 46 legacy + 3 targets v8` puede coexistir con Builder y Pages vigentes sin debilitar invariantes históricas y sin activar v8 públicamente.

## Hallazgos reales

Durante W4.6 se identificaron tres contratos históricos de topología cerrada:

1. `validate_experience_v60.py`: exige baseline de 46 HTML públicos.
2. `validate_experience_solutions_v60.py`: exige exactamente las seis rutas v6 de `/soluciones/`.
3. `validate_growth_v51.py`: exige exactamente las seis rutas Growth + hub en `/soluciones/`.

No se modificó ninguno para ignorar el target nuevo.

`validate_site.py`, CRO v5.2 y el resto de la batería Pages demostraron ser compatibles con el árbol ampliado cuando se ejecutan bajo el adapter W4.6.

## Estrategia certificada

W4.6 mantiene dos vistas explícitas:

1. **Árbol candidate real**: 49 HTML.
2. **Proyección legacy temporal**: 46 HTML, obtenida retirando únicamente los tres targets allowlisted en un workspace efímero.

Los validadores históricos de topología cerrada siguen ejecutándose, sin cambios, sobre la proyección de 46 páginas. Los validadores additive-safe se ejecutan directamente sobre los 49 HTML reales.

## Contrato

`assets/data/v8/pipeline-compat-v80.json`

Fija:

- baseline pública `7.4.0`;
- 46 HTML legacy;
- 49 HTML candidate;
- exactamente tres targets aditivos;
- allowlist de validadores históricos estrictos;
- Builder v6 ejecutado en proyección;
- targets `noindex,follow`;
- targets fuera de sitemap y Home/navigation;
- legacy self-canonical;
- cero version bump;
- cero canonical handoff;
- cero deploy;
- cero movimiento de stable;
- RC02 fuera de alcance.

## Gate de compatibilidad

`scripts/validate_v8_pipeline_compat.py`

Prueba simultáneamente:

- árbol real de 49 HTML;
- W4.5 public-tree PASS;
- renderer truth PASS;
- contraste AA PASS;
- tres targets presentes y noindex;
- sitemap/Home sin activación;
- proyección temporal de 46 HTML;
- Experience v6, Solutions v6 y Growth v5.1 estrictos PASS en la proyección;
- hashes de targets reales invariantes.

## Builder projection

`scripts/simulate_v8_builder_projection.py`

La cadena canónica v6 se ejecuta únicamente dentro de la proyección de 46 páginas:

- sync de versión visible;
- Experience general;
- Solutions;
- Sectors;
- Perspectives;
- Experience final;
- Funnel trust;
- normalización de compatibilidad;
- Fit/Scope cuando existe;
- validators canónicos posteriores.

Resultado certificado:

- cadena Builder completa PASS;
- validators históricos PASS;
- salida legacy proyectada = árbol legacy real byte por byte;
- tres targets v8 intactos;
- checkout real sin diff.

## Pages quality dual-view

`scripts/run_v8_pages_quality_compat.py`

Ejecuta:

- validadores de topología cerrada dentro de la proyección;
- validadores additive-safe directamente sobre los 49 HTML;
- revalidación W4.6 al final para demostrar ausencia de mutaciones.

Resultado:

- `validate_site.py`: PASS con 49 páginas;
- catálogo, UX, calidad, operación, producción, CRO, autoridad, CI, gobernanza, conversión, handoff, narrativa, contexto y visuales: PASS;
- JavaScript Pages: PASS;
- Pages artifact simulation: PASS.

## Pages artifact simulation

El artefacto simulado contiene los tres targets físicos y comprueba que continúan:

- `noindex,follow`;
- fuera del sitemap;
- fuera de activación pública.

No se invocó `upload-pages-artifact` ni `deploy-pages`.

## Resultado definitivo

Run `32908333460`, job `97997137990`: **SUCCESS**.

Secuencia final:

1. W4.5 + strict projection: PASS.
2. Builder projection: PASS.
3. Real checkout untouched: PASS.
4. Pages Quality dual-view: PASS.
5. JavaScript: PASS.
6. Pages artifact simulation: PASS.

## Boundary

W4.6 no modifica:

- `main`;
- `stable`;
- `version.json`;
- sitemap;
- robots;
- Home/navigation;
- canonical legacy;
- producción;
- RC02.

Tampoco modifica todavía los workflows productivos `build-canonical.yml` o `pages.yml`; demuestra primero el adapter en un workflow candidate aislado.

## Siguiente frente

W4.7 debe integrar de forma controlada este adapter dual-view en el **contrato candidate de Builder/Pages**, manteniendo deploy deshabilitado hasta demostrar equivalencia entre el pipeline integrado y W4.6.

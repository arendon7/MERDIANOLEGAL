# W4.6 — v8 Pipeline Compatibility Candidate

Fecha: 2026-08-25
Dependencia: W4.5 Public-Tree Candidate PASS (`32907133921`).
Estado inicial: candidate; sin deploy.

## Objetivo

Demostrar que el árbol físico W4.5 de 49 HTML puede coexistir con el pipeline v6 vigente sin debilitar sus invariantes históricas y sin activar v8 públicamente.

## Problema observado

El pipeline v6 contiene validadores con topologías cerradas. En particular, `validate_experience_solutions_v60.py` exige que `/soluciones/` contenga exactamente los seis slugs Growth/CRO históricos. La presencia aditiva de `/soluciones/sistema-contractual-empresarial.html` hace fallar correctamente ese contrato v6.

Ese fallo no se corrige ignorando archivos nuevos ni ampliando silenciosamente v6.

## Estrategia

W4.6 mantiene dos vistas:

1. **Árbol candidate real**: 49 HTML = 46 legacy + 3 targets v8.
2. **Proyección legacy temporal**: 46 HTML, obtenida retirando únicamente los tres targets allowlisted dentro de un workspace efímero.

El validador v6 original corre sin modificaciones sobre la proyección legacy. Los contratos v8 validan simultáneamente el árbol real.

## Contrato

`assets/data/v8/pipeline-compat-v80.json`

Declara:

- baseline pública v7.4.0;
- 46 HTML legacy;
- 49 HTML candidate;
- exactamente tres targets aditivos;
- validators legacy que deben permanecer estrictos;
- ausencia de version bump;
- ausencia de sitemap/Home activation;
- ausencia de canonical handoff;
- no deploy;
- no movimiento de stable;
- RC02 fuera de alcance.

## Gate principal

`scripts/validate_v8_pipeline_compat.py`

Prueba:

- contrato W4.6 exacto;
- 49 HTML reales;
- tres targets presentes y `noindex,follow`;
- sitemap/Home sin targets;
- W4.5 public-tree validator PASS;
- renderer truth PASS;
- contraste PASS;
- proyección temporal 46 HTML;
- `validate_experience_solutions_v60.py` PASS sin modificarlo;
- hashes de targets reales invariantes durante la proyección.

## Builder simulation

W4.6 ejecuta sobre el árbol de 49 páginas la cadena canónica de extensiones v6 que el Builder aplica a una baseline v6:

- sync de versión visible;
- Experience general;
- Solutions;
- Sectors;
- Perspectives;
- Experience final;
- Funnel trust;
- normalización de compatibilidad;
- Fit/Scope cuando existe.

Después exige:

- hashes de los tres targets v8 idénticos;
- `git diff --exit-code`;
- validators Builder PASS usando la proyección estricta únicamente donde la topología v6 es cerrada.

## Pages quality simulation

Se ejecuta la batería de validators estáticos de Pages sobre el árbol real de 49 HTML y sintaxis JavaScript. Finalmente se construye una copia equivalente al artefacto Pages, pero no se invoca `upload-pages-artifact` ni `deploy-pages`.

El artefacto simulado debe contener los tres targets y mantenerlos `noindex`, fuera de sitemap.

## No objetivos

W4.6 no:

- modifica `main`;
- modifica `stable`;
- cambia `version.json`;
- cambia sitemap/robots/Home;
- cambia canonical legacy;
- indexa targets;
- cambia producción;
- ejecuta Pages deploy;
- publica RC02;
- realiza todavía el canonical handoff.

## Gate de salida

W4.6 termina únicamente si:

1. W4.5 sigue PASS;
2. strict legacy projection PASS;
3. Builder simulation idempotente PASS;
4. Builder no modifica los tres targets v8;
5. Pages quality suite PASS sobre 49 HTML;
6. Pages artifact simulation PASS;
7. main/stable continúan en baseline productiva.

La siguiente wave podrá decidir la integración controlada de este adapter en Builder/Pages reales o avanzar a un candidate deployment aislado, pero W4.6 por sí sola no despliega.

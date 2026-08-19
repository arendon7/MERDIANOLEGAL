# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado funcional certificado

- Release: **v6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance**.
- SHA funcional certificado: `0045588f795f5f0a0b9144786bc61cdf89f34319`.
- Canal objetivo de cierre: `github-pages-production-fit-scope-clarity-certified`.
- PR funcional: #162 fusionado.
- Builder materializó las 16 fichas y produjo el snapshot funcional certificado.
- `stable` fue promovido automáticamente a `0045588f…` después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.
- Search Console permanece sin configurar: `searchConsoleConfigured=false` y sin token auténtico.
- Analytics externa permanece deshabilitada: `enabled=false`, `provider=none`, `site_id=""`.
- 46 HTML, 16 fichas profundas, un único formulario físico y 30 pasos históricos permanecen intactos.

## Frente vigente

**No existe un ciclo funcional nuevo abierto.**

Este documento acompaña únicamente el **cierre documental v6.4.0**:

1. cambiar el canal `candidate → certified`;
2. actualizar README y memoria canónica;
3. publicar `RELEASE-v6.4.md`;
4. someter el cierre a los gates pre-merge aplicables;
5. fusionar únicamente con same-SHA verde;
6. exigir nuevamente Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot;
7. cerrar cuando `main == stable` y `stable/version.json` declare v6.4.0 con canal certified.

Si esta nota se lee desde `stable` y `version.json.channel` ya es `github-pages-production-fit-scope-clarity-certified`, el cierre documental está completado y **no hay tarea funcional activa**.

## Resultado que queda cerrado

v6.4 hace visible en las 16 fichas verdad ya contenida en los catálogos jurídicos:

- `situations` → **Señales de que esta modalidad encaja**;
- `supplements` → **Situaciones que amplían el alcance**;
- una única sección `#v6-fit-scope` entre Resultado y Entregables;
- TOC v6.3 preservado en exactamente 7 hitos, sin enlace v6.4 adicional.

La representación visible no redefine esos datos. El validator compara fila por fila contra `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.

## Release engineering cerrado

- materializador v6.4 fail-closed + `--check`;
- validator 16/16 contra truth canónico;
- gate v6.4 phase-aware desde el inicio: 0/16 → 16 drift; 16/16 → 0; parcial → fallo;
- Canonical Equivalence `measurement ∪ release ∪ discovery ∪ engagement ∪ fit/scope`;
- CSS v6.4 estabilizado frente a v6.3/tokens para segunda pasada byte-equivalent;
- Builder == Pages == `canonical_pipeline_v524.py` con 30 pasos históricos intactos;
- Builder/Candidate/Browser/Measurement con cobertura explícita de v6.4;
- E2E en las 16 fichas y orden DOM representativo;
- candidate final `38c140f5…` con 9/9 workflows aplicables verdes;
- producción certificada en `0045588f…`.

## Incidencia productiva documentada

El primer Lighthouse productivo recibió HTTP 503 transitorio únicamente en `demo`; quality, deploy, smoke y Browser habían pasado y snapshot quedó skipped.

- #164 reprodujo smoke, Browser/axe y Lighthouse en verde contra producción y se cerró sin merge.
- Se reejecutaron los jobs fallidos del run oficial, sin cambios de código ni budgets.
- Lighthouse pasó en el rerun.
- Snapshot y `Move stable to deployed commit` terminaron success.
- No hubo promoción manual de `stable`.

## Fuera de alcance después del cierre

No hacer automáticamente:

- reescribir `situations`, `supplements`, `requirements` o `responsibilities` por intuición;
- añadir obligaciones, tarifas, descuentos o cronogramas no aprobados;
- activar Search Console sin token auténtico;
- activar Plausible, Umami u otra analítica;
- crear backend, CRM, portal, auth, pagos, firma, agenda o upload ficticios;
- abrir v6.5 solo por continuidad de versionado;
- reducir cobertura E2E/axe o relajar Lighthouse.

## Próximo ciclo

Después de este cierre documental, el proyecto queda en estado estable. El próximo ciclo debe partir de una necesidad observable de negocio, conversión, contenido u operación jurídica. Antes de añadir otra capa, debe comprobarse si la verdad necesaria ya existe en los catálogos o contratos actuales y puede presentarse mejor.

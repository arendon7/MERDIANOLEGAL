# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado base certificado

- Release de partida: **v6.3.0 — Engagement Clarity / claridad precontratación**.
- Base certificada al abrir este ciclo: `main == stable == 9fe408ca59da7c32db8de32baa5d7515282e411d`.
- Snapshot funcional v6.3 materializado por Builder: `118cee5030f27689d91172beb525d7d92c751117`.
- Canal certificado: `github-pages-production-engagement-clarity-certified`.
- Search Console permanece sin configurar: `searchConsoleConfigured=false` y sin token auténtico.
- Analytics externa permanece deshabilitada: `enabled=false`, `provider=none`, `site_id=""`.
- 46 HTML, 16 fichas profundas, un único formulario físico y 30 pasos históricos permanecen como invariantes.

## Ciclo funcional activo

**v6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance.**

Rama: `feat/v64-fit-scope-clarity`.
PR: `#162` (Draft hasta certificación same-SHA).
Release candidate: `version.json = 6.4.0`, fecha `2026-08-18`, canal `github-pages-fit-scope-clarity-candidate`.

### Problema observable

Las 16 fichas profundas ya elevan a primer nivel resultado/aceptación, entregables, perímetro, proceso, límites y, desde v6.3, requisitos y responsabilidades. Sin embargo, dos piezas de truth comercial seguían incompletamente expuestas:

- `situations`: describe las situaciones empresariales concretas en las que una modalidad encaja, pero permanecía en la profundidad histórica;
- `supplements`: v6 mostraba sus títulos como una frase resumida, pero no la explicación canónica de qué ampliación representa cada suplemento.

La consecuencia era una fricción de autocalificación: el comprador podía entender qué hace Meridiano, pero todavía debía inferir si esa modalidad correspondía a su situación y qué circunstancias hacían crecer el perímetro base.

v6.4 corrige esa fricción **sin crear contenido jurídico nuevo**. La representación visible se deriva literalmente de `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.

## Alcance v6.4

1. contrato `assets/data/v6/fit-scope-clarity-v64.json`;
2. exactamente 16 fichas gobernadas = 8 productos + 8 servicios;
3. sección `#v6-fit-scope` inmediatamente después de Resultado y antes de Entregables;
4. panel **Señales de que esta modalidad encaja**, derivado fila por fila de `situations`;
5. panel **Situaciones que amplían el alcance**, derivado fila por fila de `supplements`;
6. **sin añadir un octavo hito al TOC**: la navegación ejecutiva v6.3 permanece con siete hitos;
7. estilos responsivos aislados en `assets/css/v6/fit-scope-clarity-v64.css`;
8. materializador `scripts/apply_fit_scope_clarity_v64.py` fail-closed, con `--check` e inserción CSS estable frente a v6.0/v6.3;
9. validator `scripts/validate_fit_scope_clarity_v64.py` que compara las matrices visibles contra los catálogos y exige orden Resultado → Fit/Scope → Entregables;
10. E2E sobre las 16 fichas, sin ampliar el TOC, con verificación de orden DOM en producto y servicio representativos;
11. gate v6.4 phase-aware: 0/16 exige exactamente 16 drift; 16/16 exige 0; cualquier estado parcial falla;
12. primera pasada exacta `release drift ∪ fit/scope drift`;
13. Canonical Equivalence incorpora explícitamente `fit/scope drift` al conjunto exacto esperado;
14. Builder, Pages y `canonical_pipeline_v524.py` comparten exactamente la misma extensión v6, con 30 pasos históricos intactos;
15. Builder, Candidate y Browser observan/materializan/validan v6.4;
16. `validate_pages_trigger_v511.py` exige cobertura del nuevo materializador;
17. no se crea un paso histórico 31: v6.4 se ejecuta dentro de las extensiones canónicas existentes.

## Evidencia técnica previa al bump

SHA técnico certificado: `ecc90b17f0784f53fb4a035c3d91d2ff2938e627`.

Sobre ese SHA quedaron verdes los **6/6 gates aplicables** de la fase técnica:

- V6.4 Fit & Scope Clarity;
- V6 Candidate Validation;
- V6 Canonical Builder Equivalence;
- Release Governance;
- Graphify;
- V6 Browser Candidate / axe.

El gate v6.4 demostró boundary exacto de 16 fichas y segunda pasada byte-equivalent. Equivalence aceptó el conjunto exacto `measurement ∪ release ∪ discovery ∪ engagement ∪ fit/scope`. Governance confirmó Builder == Pages == manifiesto con los 30 pasos históricos intactos. Browser/axe ejecutó la nueva spec sobre las 16 fichas.

## Invariantes

- no modificar `situations` ni `supplements` de los catálogos por intuición;
- no inventar criterios de encaje, exclusiones, precios, tiempos o garantías;
- no sustituir `perimeter` ni `limits`;
- no alterar los siete hitos v6.3 de navegación;
- no activar Search Console o analytics;
- no modificar el formulario ni el handoff manual por WhatsApp;
- no crear backend, CRM, portal, auth, pagos, firma, agenda o upload ficticios;
- no reducir cobertura E2E/axe ni relajar Lighthouse;
- `stable` solo después de gates productivos verdes.

## Criterios de éxito del candidate 6.4.0

El HEAD final con `version.json = 6.4.0` debe demostrar nuevamente:

- 16/16 fichas reproducen literalmente `situations` y `supplements` canónicos;
- ninguna ficha fuera de productos/servicios recibe la sección;
- el TOC permanece en siete hitos y no contiene `#v6-fit-scope`;
- primera materialización = release drift + fit/scope drift declarado, sin rutas inesperadas;
- segunda pasada idempotente;
- 46 HTML, 16 fichas, 1 formulario y 30 pasos históricos intactos;
- Search Console continúa sin afirmaciones ficticias;
- analytics externa continúa deshabilitada;
- Fit & Scope Clarity, Search Discovery, Candidate, Equivalence, Governance, Graphify, Browser/axe y Measurement deben quedar verdes sobre el **mismo SHA 6.4.0** cuando resulten aplicables;
- después del merge: Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot debe promover `stable` automáticamente.

## Fuera de alcance

- reescribir `situations` o `supplements` por intuición;
- cambiar entregables, perímetro, método, límites u honorarios;
- añadir precios o cronogramas no aprobados;
- activar Search Console o analytics;
- alterar el formulario o el handoff manual por WhatsApp;
- crear un paso canónico 31;
- reducir cobertura E2E/axe o relajar Lighthouse.

## Condición de cierre

v6.4.0 queda funcionalmente cerrada únicamente cuando el candidate same-SHA sea verde, #162 se fusione, Builder materialice la versión y las 16 fichas, Pages complete smoke + Browser/axe + Lighthouse + snapshot y `stable` alcance automáticamente el snapshot canónico de v6.4. Después se realiza el cierre documental `candidate → certified` y se exige nuevamente `main == stable`.

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

**v6.4 — Fit & Scope Clarity / encaje y cambio de alcance.**

Rama: `feat/v64-fit-scope-clarity`.
Estado: **fase técnica pre-bump**. `version.json` continúa en v6.3.0 certified hasta que el cambio técnico demuestre same-SHA verde.

### Problema observable

Las 16 fichas profundas ya elevan a primer nivel resultado/aceptación, entregables, perímetro, proceso, límites y, desde v6.3, requisitos y responsabilidades. Sin embargo, dos piezas de truth comercial siguen incompletamente expuestas:

- `situations`: describe las situaciones empresariales concretas en las que una modalidad encaja, pero permanece en la profundidad histórica;
- `supplements`: v6 muestra sus títulos como una frase resumida, pero no expone la explicación canónica de qué ampliación representa cada suplemento.

La consecuencia es una fricción de autocalificación: el comprador entiende qué hace Meridiano, pero todavía debe inferir si esa modalidad corresponde a su situación y qué circunstancias hacen crecer el perímetro base.

v6.4 corrige esa fricción **sin crear contenido jurídico nuevo**. La representación visible se deriva literalmente de `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.

## Alcance técnico v6.4

1. contrato `assets/data/v6/fit-scope-clarity-v64.json`;
2. exactamente 16 fichas gobernadas = 8 productos + 8 servicios;
3. nueva sección `#v6-fit-scope` inmediatamente después de Resultado y antes de Entregables;
4. panel **Señales de que esta modalidad encaja**, derivado fila por fila de `situations`;
5. panel **Situaciones que amplían el alcance**, derivado fila por fila de `supplements`;
6. **sin añadir un octavo hito al TOC**: la navegación ejecutiva v6.3 permanece con sus siete hitos;
7. estilos responsivos aislados en `assets/css/v6/fit-scope-clarity-v64.css`;
8. materializador `scripts/apply_fit_scope_clarity_v64.py` fail-closed, con `--check` e inserción CSS estable frente a v6.0/v6.3;
9. validator `scripts/validate_fit_scope_clarity_v64.py` que compara las matrices visibles contra los catálogos y exige orden Resultado → Fit/Scope → Entregables;
10. E2E sobre las 16 fichas, sin ampliar el TOC, con verificación de orden DOM en producto y servicio representativos;
11. gate dedicado v6.4 phase-aware: 0/16 exige exactamente 16 drift; 16/16 exige 0; cualquier estado parcial falla;
12. primera pasada exacta `release drift ∪ fit/scope drift`;
13. Canonical Equivalence incorpora explícitamente `fit/scope drift` al conjunto exacto esperado;
14. Builder, Candidate y Browser observan/materializan/validan v6.4;
15. `validate_pages_trigger_v511.py` exige cobertura del nuevo materializador en Builder;
16. no se crea un paso histórico 31: v6.4 se ejecuta dentro de las extensiones canónicas existentes.

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

## Criterio para autorizar el bump 6.4.0

Antes de cambiar `version.json`, el SHA técnico debe demostrar:

- exactamente 16 fichas pendientes desde la base v6.3;
- truth visible `situations + supplements` idéntico a los catálogos;
- cero páginas fuera de productos/servicios afectadas por v6.4;
- TOC v6.3 preservado sin `#v6-fit-scope`;
- segunda pasada byte-equivalent;
- contratos históricos v4/v5/v6 preservados;
- Candidate, Fit & Scope Clarity, Canonical Equivalence, Governance, Graphify y suites Browser/axe/Measurement aplicables verdes sobre el mismo SHA.

Solo después de esa evidencia se crea el candidate formal **6.4.0** y se repite la matriz completa antes del merge.

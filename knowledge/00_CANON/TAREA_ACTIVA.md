# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado base certificado

- Release de partida: **v6.2.0 — Search Discovery Readiness**.
- Base certificada al abrir el ciclo: `main == stable == 992efa56ecdb3d393cd584eccc35a958a5fb0ea6`.
- Search Console continúa sin configurar; no existe token auténtico y runtime conserva `searchConsoleConfigured=false`.
- Analytics externa continúa deshabilitada (`enabled=false`, `provider=none`, `site_id=""`).
- 46 HTML, 16 fichas profundas, un único formulario físico y 30 pasos históricos del builder permanecen como invariantes.

## Ciclo funcional activo

**v6.3.0 — Engagement Clarity / claridad precontratación.**

Rama: `feat/v63-engagement-clarity`.
PR: `#160` (Draft hasta certificación same-SHA).
Release candidate: `version.json = 6.3.0`, fecha `2026-08-18`, canal `github-pages-engagement-clarity-candidate`.

### Problema observable

Las 16 fichas profundas ya explicaban resultado, entregables, perímetro, proceso y límites, pero dos matrices jurídicas/comerciales aprobadas permanecían relegadas a la profundidad histórica:

- `requirements`: qué debe estar listo del lado del cliente;
- `responsibilities`: cómo se distribuyen las responsabilidades del encargo.

La consecuencia era una asimetría de decisión: el comprador podía entender qué haría Meridiano, pero no veía con igual claridad qué debía aportar su organización ni quién respondería por qué antes de solicitar una propuesta.

v6.3 corrige esa fricción **sin inventar contenido jurídico nuevo**. La verdad visible se deriva literalmente de `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.

## Alcance v6.3

1. contrato `assets/data/v6/engagement-clarity-v63.json`;
2. exactamente **16 fichas** gobernadas = 8 productos + 8 servicios;
3. nueva ancla ejecutiva `Para empezar` en las 16 fichas;
4. nueva sección `#v6-engagement` antes de Límites;
5. panel `Qué debe estar listo del lado del cliente` derivado exactamente de `requirements`;
6. panel `Cómo se distribuyen las responsabilidades` derivado exactamente de `responsibilities`;
7. estilos responsivos aislados en `assets/css/v6/engagement-clarity-v63.css`;
8. materializador `scripts/apply_engagement_clarity_v63.py` fail-closed e idempotente;
9. validator `scripts/validate_engagement_clarity_v63.py` que compara fila por fila HTML visible contra los catálogos canónicos;
10. integración transversal por `normalize_experience_compat_v60.py`, sin crear un paso histórico 31;
11. gate dedicado v6.3 con boundary exacto de 16 HTML y segunda pasada idempotente;
12. Canonical Equivalence exige `measurement ∪ release ∪ discovery ∪ engagement`;
13. v4.6 permanece estricto: seis hitos sin Engagement Clarity, exactamente siete cuando v6.3 está materializada y el séptimo debe ser `#v6-engagement`;
14. Builder, Candidate y Browser observan expresamente los scripts v6.3;
15. `validate_pages_trigger_v511.py` exige cobertura del nuevo materializador en Builder;
16. E2E recorre las 16 fichas y comprueba navegación real en una ficha de producto y una de servicio.

## Evidencia técnica previa al bump

SHA técnico previo al bump: `a7e8b057dc4818365247cd0615c796a233836203`.

Sobre ese mismo SHA quedaron verdes:

- V6.3 Engagement Clarity;
- V6 Candidate Validation;
- V6 Canonical Builder Equivalence;
- Release Governance;
- Graphify;
- V6 Browser Candidate / axe;
- V6.1 Measurement Readiness / Browser E2E.

El gate v6.3 demostró exactamente 16 HTML modificados y segunda pasada idempotente. Equivalence volvió a pasar todos los contratos históricos después de hacer v4.6 phase-aware.

## Criterios de éxito del candidate 6.3.0

- 16/16 fichas reproducen literalmente `requirements` y `responsibilities` canónicos;
- ninguna ficha fuera de productos/servicios recibe la sección;
- un único enlace `Para empezar` y una única sección `#v6-engagement` por ficha;
- navegación ejecutiva exacta de siete hitos en v6.3;
- primera materialización = release drift + engagement drift declarado, sin rutas inesperadas;
- segunda pasada idempotente;
- 46 HTML, 16 fichas, 1 formulario y 30 pasos históricos intactos;
- Search Console continúa sin afirmaciones ficticias;
- analytics externa continúa deshabilitada;
- Candidate, Engagement Clarity, Equivalence, Governance, Graphify, Browser/axe y Measurement deben quedar verdes nuevamente sobre el **mismo SHA 6.3.0**;
- después del merge: Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot debe promover `stable` automáticamente.

## Fuera de alcance

- reescribir o ampliar `requirements`/`responsibilities` por intuición;
- cambiar entregables, perímetro, método, límites u honorarios;
- añadir precios o cronogramas no aprobados;
- crear nuevas obligaciones contractuales desde la capa de presentación;
- activar Search Console o analytics;
- alterar el formulario o el handoff manual por WhatsApp;
- crear un paso canónico 31;
- reducir cobertura E2E/axe o relajar Lighthouse.

## Condición de cierre

v6.3.0 queda funcionalmente cerrada únicamente cuando el candidate same-SHA sea verde, #160 se fusione, el builder materialice las 16 fichas, Pages complete smoke + Browser/axe + Lighthouse + snapshot y `stable` alcance automáticamente el snapshot canónico de v6.3. Después se realiza el cierre documental `candidate → certified` y se exige nuevamente `main == stable`.

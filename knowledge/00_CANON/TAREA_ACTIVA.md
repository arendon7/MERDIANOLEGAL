# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado base certificado

- Release de partida: **v6.4.0 — Fit & Scope Clarity / encaje y cambio de alcance**.
- Base certificada al abrir este ciclo: `main == stable == 704d61b9f56e58b4ac135fd66aeee89033e22f24`.
- Canal certificado: `github-pages-production-fit-scope-clarity-certified`.
- Search Console permanece sin configurar: `searchConsoleConfigured=false` y sin token auténtico.
- Analytics externa permanece deshabilitada: `enabled=false`, `provider=none`, `site_id=""`.
- 46 HTML, 16 fichas profundas, un único formulario físico, TOC de 7 hitos y 30 pasos históricos permanecen como invariantes.

## Ciclo funcional activo

**v6.5 — Delivery Plan Clarity / claridad de entrega y ritmo de trabajo.**

Rama: `feat/v65-delivery-plan-clarity`.
Estado: fase técnica pre-bump; `version.json` permanece en 6.4.0 hasta que el renderer y su boundary queden certificados.

## Problema observable

Las 16 fichas ya exponen en lectura ejecutiva:

- resultado y criterios de cierre;
- encaje y situaciones que amplían el alcance (v6.4);
- entregables y perímetro;
- proceso;
- requisitos y responsabilidades (v6.3);
- límites.

Sin embargo, dos campos canónicos siguen relegados a la profundidad histórica cerrada por defecto:

- `formats`: archivos, matrices, dashboards, repositorio y trazabilidad en que queda documentada la entrega;
- `timeline`: semanas, hitos o cadencias que explican cómo transcurre el trabajo.

La consecuencia es una fricción distinta de v6.3/v6.4: el comprador puede entender qué recibe y si la modalidad encaja, pero debe abrir la profundidad para saber **cómo recibirá materialmente el trabajo y cómo se distribuye en el tiempo**.

## Alcance propuesto v6.5

1. contrato `assets/data/v6/delivery-plan-clarity-v65.json`;
2. exactamente 16 fichas = 8 productos + 8 servicios;
3. bloque `#v6-delivery-plan` inmediatamente después de Entregables y antes de Perímetro;
4. panel `Cómo queda documentado y administrable` derivado literalmente de `formats`;
5. panel `Cómo transcurre el trabajo` derivado literalmente de `timeline`;
6. sin octavo hito en la navegación: el TOC permanece exactamente en 7;
7. ninguna plataforma, archivo, plazo, frecuencia, SLA o repositorio se inventa desde presentación;
8. las advertencias existentes sobre Meridiano Empresas solo cuando esté habilitado productivamente se preservan literalmente desde catálogo;
9. materializador fail-closed + `--check` e idempotencia;
10. validator fila por fila contra truth canónico;
11. E2E 16/16 y orden Entregables → Delivery Plan → Perímetro;
12. gate dedicado phase-aware: 0/16 → 16 drift; 16/16 → 0; parcial → fallo.

## Fuera de alcance

- reescribir `formats` o `timeline` por intuición;
- prometer plataforma Meridiano Empresas si no existe habilitación productiva real;
- añadir cronogramas, tiempos de respuesta o SLA no aprobados;
- añadir precios, descuentos, garantías o nuevas obligaciones;
- alterar el formulario o WhatsApp manual;
- activar Search Console o analytics;
- crear un paso histórico 31;
- reducir Browser/axe o relajar Lighthouse.

## Condición para autorizar bump 6.5.0

La fase técnica debe demostrar, sobre un mismo SHA:

- exactamente 16 fichas pendientes en baseline v6.4;
- truth visible idéntico a `formats` + `timeline` de cada catálogo;
- ninguna ruta fuera de `productos/` y `servicios/`;
- TOC exacto de 7 hitos;
- segunda pasada byte-equivalent.

Solo después se integrará v6.5 en Builder, Pages, Candidate, Equivalence, Browser y Measurement y se realizará el bump formal a 6.5.0 candidate.

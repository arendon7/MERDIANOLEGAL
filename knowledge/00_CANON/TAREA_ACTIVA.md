# Meridiano Legal — Tarea activa

Actualizado: 2026-08-25.

## Baseline certificado

- Repositorio: `arendon7/MERDIANOLEGAL`.
- `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
- Release productiva: **v7.4.0 — Commercial Evidence Readiness**.
- Analytics: `readiness-disabled`.
- Capability truth v7.4 permanece vigente mientras v8 está en diseño.

## Frente vigente

**W4.1 — v8 Client Architecture & Taxonomy.**

Rama: `design/v8-client-architecture-w41`.

Este frente es exclusivamente de arquitectura, truth mapping y migración. No modifica todavía HTML público, CSS, JS, sitemap, formularios, precios, analítica ni `stable`.

## Problema observable

La oferta certificada expone simultáneamente `productos`, `servicios` y `soluciones/necesidades`. Existen intenciones de compra solapadas entre estas familias y el visitante debe comprender la taxonomía interna antes de reconocer la intervención adecuada.

La profundidad jurídica/comercial de catálogos v4.1/v4.2 se preserva; el problema a resolver es descubrimiento, jerarquía y arquitectura de compra.

## Decisión v8 propuesta

Tres familias públicas:

1. **Prácticas** — 6 dominios de expertise.
2. **Soluciones** — 8 intervenciones de alcance definido.
3. **Servicios continuos** — Dirección Jurídica Externa y, solo tras capability contract, Meridiano Contratos.

La cifra de 46 HTML pasa de invariante de producto a baseline histórico de migración. Ninguna URL legacy se elimina sin mapping, compatibilidad y gates.

## Evidencia W4.1 ya materializada

1. `knowledge/10_DECISIONES/ADR-008-v8-client-architecture-taxonomy.md`
   - define la nueva taxonomía;
   - cambia el tratamiento del invariante 46 HTML;
   - fija capability boundary de Meridiano Contratos;
   - define rollout y no objetivos.

2. `knowledge/20_DESIGN/V8-ROUTE-MIGRATION-MATRIX.md`
   - top-level 9/9;
   - productos 8/8;
   - servicios 8/8;
   - soluciones/necesidades 7/7;
   - sectores 8/8;
   - perspectivas 6/6;
   - cobertura total 46/46.

3. `knowledge/20_DESIGN/V8-OFFER-CANON.md`
   - 6 prácticas con fuentes;
   - 8 soluciones con fuentes;
   - Dirección Jurídica Externa preservada;
   - Meridiano Contratos mantenido como hipótesis pendiente de contrato verificable;
   - relación práctica → solución → continuidad.

## Riesgos abiertos

### R1 — P01/S01

Diagnóstico Jurídico Empresarial existe hoy como producto y servicio. Antes del merge semántico debe construirse una parity matrix de alcance, entregables, perímetro, tiempos y límites.

### R2 — GitHub Pages / aliases

No asumir redirects de servidor. W4.2 debe definir y probar estrategia real de aliases/canonical para rutas legacy.

### R3 — validators estructurales

Los validators actuales esperan 46 HTML y 8 productos + 8 servicios. No se cambian hasta existir contrato técnico v8 y pruebas equivalentes o más estrictas.

### R4 — Meridiano Contratos

No publicar como plataforma/portal/producto cerrado hasta documentar:

- unidad comercial;
- intake y workflow;
- revisión humana;
- tecnología real;
- autenticación/almacenamiento si existen;
- seguridad;
- versionado;
- mantenimiento;
- SLA/soporte si se prometen;
- límites y suplementos.

## Siguiente subfrente — W4.2

**Route Compatibility & SEO Contract.**

Debe producir:

1. estrategia GitHub Pages para legacy routes;
2. canonical policy;
3. sitemap target;
4. breadcrumb target;
5. aliases vs intent landings;
6. inventario de validators/tests afectados;
7. diseño de nuevos invariantes estructurales;
8. plan de rollback a v7.4;
9. smoke contract para legacy URLs;
10. candidate de migración sin tocar `stable`.

## Definition of Done W4.1

- ADR-008 escrito;
- matriz 46/46 completa;
- canon 6 prácticas / 8 soluciones / recurrentes documentado;
- fuentes de verdad identificadas;
- nuevos claims bloqueados donde no existe evidencia;
- `stable` intacta;
- PR de planificación abierto contra `main` para revisión.

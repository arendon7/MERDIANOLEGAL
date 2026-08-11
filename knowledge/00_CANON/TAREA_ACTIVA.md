# Meridiano Legal — Tarea activa

Actualizado: 2026-08-11.

## Ciclo en cierre

**v5.7 — Release governance, dependencias y salud operativa del pipeline.**

La implementación funcional está certificada. Este commit documental declara `5.7.0` y solo constituye el cierre definitivo cuando atraviesa la certificación pública completa y `main == stable`.

## Implementado

1. `release-governance-v57.json` como policy versionada de Actions, runtimes, dependencias QA, permisos e invariantes;
2. `scripts/validate_release_governance_v57.py` como validator obligatorio y generador de release-health;
3. Actions oficiales fijadas por SHA completo y major documentado;
4. checkouts read-only sin credenciales persistentes;
5. Dependabot semanal limitado a minor/patch y máximo dos PR por ecosistema;
6. workflow `Release governance health` para PR, schedule y ejecución manual;
7. validator v5.7 integrado al quality gate público;
8. artefacto `release-governance-health-v57` generado antes de promover `stable`;
9. `Actions hygiene` para runs queued huérfanos, aplazado si Site Quality está activo o queued;
10. validators históricos v5.5/v5.6 compatibles con el pinning SHA reforzado, sin reducir sus contratos;
11. `RELEASE-v5.7.md`, README y memoria canónica alineados con la release.

## Evidencia funcional previa al cierre documental

Run `31534382576`, SHA `945abb9c4e35c87d4f9a9ecd5ff161707b7d716e`:

- validadores v4.4→v5.7: success;
- Pages + smoke: success;
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- release governance: 5 workflows / 22 usos de Actions, SHA pinning + permisos + dependencias + gates protegidos;
- `stable` promovido correctamente.

La primera tentativa Browser agotó el timeout durante instalación por lentitud transitoria del mirror Ubuntu antes de ejecutar tests. El runner limpio posterior instaló correctamente y aprobó la suite completa. No se redujo cobertura, no se relajaron budgets y no se amplió el timeout para ocultar la incidencia.

## Contratos preservados

- 37 entradas E2E;
- Chromium desktop/mobile;
- WebKit desktop;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5;
- workers Playwright CI = 1;
- gate dual Browser + Lighthouse;
- idempotencia;
- Actions inventariadas y fijadas a SHA;
- permisos controlados;
- no upgrades major automáticos;
- full public certification antes de `stable`.

## Condición de cierre

La v5.7 queda cerrada cuando el commit que contiene esta declaración cumple simultáneamente:

1. builder/idempotencia verdes;
2. validadores v4.4→v5.7 verdes;
3. Pages + smoke verdes;
4. Browser E2E/axe verde;
5. Lighthouse verde;
6. release-health verde;
7. `main == stable`;
8. Graphify regenerado con `BUILD_META.json.source_commit == main`.

## Próximo ciclo después del cierre

No iniciar otra actualización de infraestructura por inercia. El siguiente ciclo debe volver a priorizar producto/web y crecimiento verificable, usando la nueva governance como red de seguridad y manteniendo cambios de dependencias pequeños, independientes y medibles.

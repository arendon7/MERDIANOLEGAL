# Meridiano Legal — Tarea activa

Actualizado: 2026-08-11.

## Ciclo activo

**v5.7 — Release governance, dependencias y salud operativa del pipeline.**

Base certificada de partida:

- v5.6 funcionalmente certificada;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- gate dual Browser + Lighthouse;
- baseline v5.5: 279 s;
- v5.6: 160 s, mejora 42.7%.

## Implementación v5.7 en curso

Candidata inicial: PR `#26` / rama `release/v57-governance-foundation`.

La fundación implementada incluye:

1. `release-governance-v57.json` como policy versionada de Actions, runtimes, dependencias QA e invariantes;
2. `scripts/validate_release_governance_v57.py` como validator obligatorio y generador de release-health;
3. Actions oficiales fijadas por SHA completo, conservando el major documentado;
4. checkouts read-only sin credenciales persistentes;
5. Dependabot semanal limitado a minor/patch y máximo dos PR por ecosistema;
6. workflow `Release governance health` para PR, schedule y ejecución manual;
7. validator v5.7 integrado al job `quality` de la certificación pública;
8. artefacto `release-governance-health-v57` generado antes de promover `stable`;
9. `Actions hygiene` semanal para runs queued huérfanos, aplazado si Site Quality está activo o queued.

## Evidencia de la candidata

Sobre el primer head del PR #26 (`107f5aece5c3ad8a050e7ffe0dd9d684546e5e26`):

- `Release governance health`: success;
- `Graphify — memoria estructural Meridiano Legal`: success.

La candidata todavía debe atravesar la certificación pública completa después del merge antes de declarar v5.7 cerrada.

## Contratos que v5.7 protege

- ningún Action remoto fuera del inventario;
- Actions remotos fijados a SHA completo;
- majors documentados y policy explícita para cualquier cambio;
- ausencia de `pull_request_target`;
- prohibición de `permissions: write-all`;
- permisos mínimos conocidos por workflow/job;
- runtimes Node/Python y herramientas Graphify fijados;
- dependencias Playwright/axe/Lighthouse exactas;
- no upgrades mayores automáticos;
- gate `stable` dependiente de Browser E2E + Lighthouse;
- 37 E2E, 7 axe, 6 Lighthouse y budgets v5.5 preservados.

## Próximos pasos del ciclo

1. terminar QA del PR #26;
2. mergear únicamente con governance + Graphify verdes;
3. observar builder, Pages, smoke, Browser E2E/axe, Lighthouse y release-health en `main`;
4. corregir cualquier regresión sin relajar contratos;
5. promover/corroborar `stable` solo desde la cadena automática;
6. cerrar versión/documentación v5.7 y actualizar `ESTADO_ACTUAL.md`;
7. limpiar ramas temporales únicamente después del cierre certificado.

## Regla para v5.7

No convertir mantenimiento en una actualización masiva. Cada cambio de runtime, Action o dependencia debe demostrar compatibilidad con el pipeline actual y conservar cobertura, presupuestos, idempotencia y el gate dual antes de `stable`.

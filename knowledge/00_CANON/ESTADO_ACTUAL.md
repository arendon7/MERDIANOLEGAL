# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release vigente: `5.20.0`.
- PR funcional: `#74`.
- Merge funcional inicial: `745723c0de896e9d0a7f613dd1b83e5efcaa4878`.
- Hotfix idempotencia: PR `#75`, merge `5ba9053c0e995c77bff555cbd9c37c2909814d81`.
- Hotfix contrato global: PR `#76`.
- SHA funcional final certificado: `85bdcfc9b52172e085dfa9b1df8e8d081b136233`.
- Run final de certificación pública: `31651473515`.
- Snapshot público certificado: `stable = 85bdcfc9b52172e085dfa9b1df8e8d081b136233`.
- PR de cierre documental: `#77`.
- Merge de cierre documental: `62f2f9b5069682ed1fbd8b72865bec267f6c6ac3`.

Refs, Pages, validators y tests son la autoridad para el estado productivo. `stable` conserva el snapshot funcional certificado; `main` puede avanzar con documentación/memoria sin que ello implique una nueva release funcional.

## Estado funcional

**v5.20.0 está implementada, desplegada, certificada y formalmente cerrada. No existe una v5.21 abierta.**

### Compresión de decisión v5.20

La portada ya no superpone varios mecanismos que piden resolver repetidamente cómo contratar.

La arquitectura final contiene dos pasos:

1. seis rutas por situación empresarial;
2. una única superficie con cinco modalidades de contratación.

El estándar verificable de propuesta v5.12 permanece visible. Los límites y alternativas v5.14 siguen disponibles mediante `<details>`. Las 16 fichas profundas conservan perímetro, entregables, formatos, responsabilidades, aceptación, límites y CTA.

Desde v5.20 la salida final no materializa el bloque separado de “Forma de contratar” v5.8 ni la sección histórica `#elegir`. Los contratos históricos permanecen protegidos mediante selectores semánticos y validadores version-aware.

No hay scoring, inferencia adicional, cambio automático de etapa, PII nueva, storage persistente nuevo, transporte de red nuevo, backend ni CRM.

## Evidencia funcional final v5.20

Run `31651473515`, SHA certificado `85bdcfc9b52172e085dfa9b1df8e8d081b136233`:

- builder e idempotencia: PASS;
- validadores históricos y contratos v5.8→v5.19: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- reporter Browser: 85 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.98–1.00;
- portada: performance 1.00, accesibilidad 1.00, LCP 1421 ms, CLS 0, TBT 83 ms;
- máximo global: LCP 1421 ms, CLS 0.087, TBT 83 ms;
- CI hasta `stable`: 191 s;
- baseline v5.5: 279 s;
- mejora: 31.5%;
- cobertura reducida: no;
- budgets relajados: no;
- release-health: PASS;
- promoción de `stable`: PASS.

Artefactos finales del run `31651473515`:

- Lighthouse `9162821238`, `sha256:681cd883c725e44c26b65c2f9b0c6a276c8668096266618dfe36c75567a3b3c0`;
- CI `9162836693`, `sha256:1862dea240db5ea3c491afc0d8505d51d5bed74dff6cf081a255a8ab1f6564af`;
- release-health `9162837264`, `sha256:00c1e747dc887dc37d4daae63fd4fdd5a279d2e813745312802277931b60c323`;
- Pages `9162779134`, `sha256:31cea6e7fd74a2bdb73543660c6a49ec6d9838341f6fb98bfd604f8abc5d852a`.

## Incidencias de compatibilidad resueltas

### v4.5 / idempotencia

La segunda pasada inicial del builder falló porque `apply_ux_v45.py` aún exigía `#elegir`. PR #75 hizo generador y validator version-aware. No se omitió el gate: idempotencia se reejecutó y pasó.

### validate_site / marcador histórico

Después, el validador global todavía exigía literalmente “CÓMO ELEGIR”. PR #76 mantuvo ese requisito hasta v5.19 y desde v5.20 exige la nueva superficie, además de fallar si reaparece la sección histórica. El gate volvió a ejecutarse y pasó.

## Contratos vigentes

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- telemetría sin PII;
- analítica externa apagada (`provider:none`);
- WhatsApp manual;
- sin CRM/backend, almacenamiento servidor, firma, pagos, agenda o portal documental ficticios;
- `stable` solo después de gates verdes para cambios funcionales/publicables.

## Graphify / procedencia

Tras el PR documental #77, Graphify validó `version = 5.20.0` y `source_commit = 62f2f9b5069682ed1fbd8b72865bec267f6c6ac3`, con 588 nodos, 948 relaciones y 94 notas wiki.

La rama `knowledge/graphify-live` es memoria derivada. La comprobación correcta de frescura es leer `graphify-out/BUILD_META.json` y contrastar su `source_commit` con el último run exitoso que produjo ese snapshot; no fijar un SHA derivado como regla permanente.

## Estado del ciclo

El gate de cierre formal de v5.20 está satisfecho. Cualquier trabajo funcional posterior debe abrir una tarea/release nueva y no modificar retrospectivamente el contrato certificado de v5.20. **No existe una v5.21 activa.**

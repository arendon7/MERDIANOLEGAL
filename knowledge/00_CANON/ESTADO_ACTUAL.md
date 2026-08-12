# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release vigente: `5.19.0`.
- PR funcional: `#71`.
- Merge fuente funcional: `fcf8d868e5b95ab201c8ebb612ffba166f4746f5`.
- SHA público final generado por builder: `9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.
- Run final de certificación pública: `31649425600`.
- Snapshot certificado al cierre funcional: `stable = 9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.

Refs, Pages, validators y tests son la autoridad para el estado productivo. `main` puede avanzar posteriormente con documentación/memoria sin que ello implique una nueva release funcional ni una modificación del snapshot público certificado.

## Estado funcional

**v5.19.0 está implementada, desplegada y funcionalmente certificada. Este ciclo solo tiene pendiente su cierre documental.**

### Foco comercial adaptativo v5.19

La capa extiende el progressive disclosure sobre los bloques secundarios de v5.10 y v5.11 usando exclusivamente `commercial_intent` explícito ya existente:

- `orientation` y `scope`: detalle secundario inicialmente replegado;
- `proposal` explícito en escritorio: detalle inicialmente expandido;
- móvil conserva el comportamiento v5.16;
- el contenido material permanece disponible mediante `<details>` nativo;
- abrir/cerrar detalle no altera `decision_stage`, modalidad, recomendación ni handoff.

No hay scoring, inferencia adicional, PII nueva, storage persistente nuevo, transporte de red nuevo, backend ni CRM.

## Evidencia funcional final v5.19

Run `31649425600`, SHA público certificado `9a91e8d19697142c0d2d0990c1e606f6ff9660ef`:

- builder/idempotencia + validators históricos + hardening v5.19: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- reporter Browser: 85 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.98–1.00;
- LCP máximo observado: 1368 ms;
- CLS máximo observado: 0.087;
- TBT máximo observado: 56 ms;
- `accessibilityAuditGaps`: vacío;
- CI hasta `stable`: 215 s;
- baseline v5.5: 279 s;
- mejora: 22.9%;
- cobertura reducida: no;
- budgets relajados: no;
- release-health: PASS;
- promoción de `stable`: PASS.

Artefactos finales del run `31649425600`:

- Lighthouse `9162048825`, `sha256:82bec745b16796e574f516b22de27d023c258a5ab1b827075eeb80a3da35670e`;
- CI `9162074790`, `sha256:4ed4f8c2d330354fababe3389e3542974f0427a55230df6f0e9bd8b57128a7bb`;
- release-health `9162075114`, `sha256:681f567ade20a27df2df8ad1645cda53d68260d127e5d43a90700c85bdc1c0d1`.

## Incidencia de compatibilidad resuelta

El primer Release Governance bloqueó la candidata porque el validator histórico v5.5 esperaba el símbolo contractual `enhanceMobileDisclosureV516`. El gate no se relajó: v5.19 preservó ese punto de entrada mediante un alias real hacia la implementación ampliada. El segundo Release Governance pasó completo.

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

La rama `knowledge/graphify-live` es memoria derivada. El snapshot observado antes del cierre documental reporta `version = 5.19.0` y `source_commit = fcf8d868e5b95ab201c8ebb612ffba166f4746f5`, que corresponde al merge fuente funcional. El commit `9a91e8d…` posterior es la materialización canónica generada por el builder y no una divergencia funcional.

No fijar como regla permanente un `source_commit` que quede obsoleto por la regeneración de Graphify. La comprobación correcta es leer `graphify-out/BUILD_META.json` y contrastarlo con el último run exitoso que produjo ese snapshot.

## Estado del ciclo

v5.19 está funcionalmente certificada. Tras integrar este cierre documental y verificar Graphify, la tarea queda cerrada. No se abre v5.20 dentro de este ciclo.

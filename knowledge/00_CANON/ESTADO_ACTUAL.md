# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-12.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release vigente: `5.18.0`.
- Merge fuente funcional: `3dd01285bcb28a568e2d5a65e2fa88ad284142cb`.
- SHA funcional certificado: `a082b4d9139ae929367cac0085597365e75dbaaf`.
- Merge de cierre documental: `b816d52979a5382c658c4589d91db853b799c932`.
- SHA público final generado por builder: `8dc462d072d4a419fc2329e60051b1cfb1044794`.
- Run final de certificación pública: `31644281459`.
- Snapshot certificado: `stable = 8dc462d072d4a419fc2329e60051b1cfb1044794`.

Refs, Pages, validators y tests son la autoridad para el estado productivo. `main` puede avanzar posteriormente con documentación/memoria sin que ello implique una nueva release funcional ni una modificación del snapshot público certificado.

## Estado funcional

**v5.18.0 está implementada, desplegada, certificada y formalmente cerrada. No hay una v5.19 abierta.**

### Observabilidad v5.18

El contrato `handoff-observability-v518.json` define exactamente seis hechos observables: `handoff_prepared`, `handoff_reopen_requested`, `handoff_copy_succeeded`, `handoff_copy_failed`, `handoff_edit_requested` y `handoff_draft_stale`.

El runtime usa únicamente `stage` y `target` sobre la cola local existente. Permanecen en `false`: PII permitida, transporte nuevo, storage persistente, identificador cross-session y contenido del formulario.

No son hechos conocidos por la web y están expresamente prohibidos como eventos: envío, entrega, lectura, aceptación de propuesta, inicio del encargo y conversión completada.

v5.17 sigue siendo la capa que gestiona el borrador manual/efímero, reabrir, copiar, editar y stale protection. v5.18 solo observa acciones verificables de esa superficie.

## Evidencia final

Run `31644281459`, SHA público certificado `8dc462d072d4a419fc2329e60051b1cfb1044794`:

- builder/idempotencia + validators históricos + v5.17 + v5.18: PASS;
- GitHub Pages + smoke: PASS;
- Browser E2E + axe: PASS;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance Lighthouse: 0.98–1.00;
- LCP máximo observado: 1239 ms;
- CLS máximo observado: 0.087;
- TBT máximo observado: 13 ms;
- budgets relajados: no;
- release-health: PASS;
- promoción de `stable`: PASS.

Artefactos finales del run `31644281459`:

- Lighthouse `9160152671`, `sha256:949516998c51089c1e4351ae4fdbb980c4599c4743ecfe35074737c96edc80bb`;
- CI `9160179743`, `sha256:9fea7d8cc080eec221c2f6f8dfa29ac6bc50a9c273020676ce544c820d8bdadd`;
- release-health `9160180092`, `sha256:bb351a20950606ec5459a9abe757cd8afd456cf671678db89176e9aed93d0d9d`.

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

La rama `knowledge/graphify-live` es memoria derivada y se regenera automáticamente desde `main`. La procedencia correcta se verifica leyendo `graphify-out/BUILD_META.json`: su `source_commit` debe coincidir con el commit procesado por el último run exitoso de Graphify y su versión debe permanecer en `5.18.0` mientras no exista una release posterior.

No fijar en esta nota un `source_commit` de Graphify que quede obsoleto por la propia regeneración del grafo.

## Estado del ciclo

El gate de cierre formal de v5.18 se considera satisfecho. Cualquier trabajo posterior debe abrir una tarea/release nueva y no modificar retrospectivamente el contrato certificado de v5.18.

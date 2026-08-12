# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**No hay una release funcional abierta. v5.18.0 quedó cerrada y certificada.**

El ciclo de observabilidad verificable del handoff manual terminó sin abrir v5.19 ni introducir nuevas integraciones.

## Cierre v5.18.0

- PR funcional: #67.
- Merge funcional: `3dd01285bcb28a568e2d5a65e2fa88ad284142cb`.
- SHA funcional certificado: `a082b4d9139ae929367cac0085597365e75dbaaf`.
- PR de cierre documental: #68.
- Merge documental: `b816d52979a5382c658c4589d91db853b799c932`.
- Commit generado por builder para sincronizar la versión pública: `8dc462d072d4a419fc2329e60051b1cfb1044794`.
- Run final de certificación: `31644281459`.
- Snapshot público certificado: `stable = 8dc462d072d4a419fc2329e60051b1cfb1044794`.
- Idempotencia + validators históricos + v5.17 + v5.18: PASS.
- Pages + smoke: PASS.
- Browser E2E + axe: PASS.
- Lighthouse: 6/6 PASS; accesibilidad 1.00 en las seis superficies; performance 0.98–1.00.
- Release-health: PASS.
- Budgets relajados: no.
- Cobertura reducida: no.

Los commits documentales posteriores al SHA público certificado pueden avanzar `main` sin alterar el runtime o el contenido desplegado certificado en `stable`.

## Procedencia Graphify

La rama `knowledge/graphify-live` se regenera automáticamente después de cambios en `main`. Su `graphify-out/BUILD_META.json` debe conservar como `source_commit` el commit exacto desde el cual fue construido el snapshot vigente.

No fijar aquí un SHA de Graphify que se vuelva obsoleto al regenerar la memoria. La regla de cierre es: comprobar que `source_commit` coincide con el `main` procesado por el último run exitoso de Graphify y que la versión reportada sigue siendo `5.18.0`.

## Contrato que permanece vigente

Se observan únicamente seis acciones locales verificables: preparado, reapertura solicitada, copia exitosa, copia fallida, editar y borrador stale.

No se transmite ni almacena PII, contenido del formulario, referencia, resumen o URL WhatsApp. No se introducen red nueva, storage persistente, cookies, identificador cross-session, CRM/backend ni analítica externa.

Nunca inferir ni registrar como hechos: mensaje enviado/entregado/leído, propuesta aceptada, encargo iniciado o conversión completada.

## Próximo ciclo

No iniciar v5.19 por arrastre. El siguiente frente debe abrirse como una tarea nueva, con objetivo, contrato, no-objetivos y criterio de cierre propios.

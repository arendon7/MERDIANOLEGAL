# Meridiano Legal — Tarea activa

Actualizado: 2026-08-13.

## Estado

**No existe una release funcional activa.**

v5.23.0 — compresión del contacto comercial — está implementada, desplegada, certificada, documentada y formalmente cerrada.

- SHA funcional certificado y `stable`: `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`.
- Run público final: `31730632791`.
- Browser E2E/axe: 58 observados → 56 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS.
- Cobertura reducida: no.
- Budgets relajados: no.

## Memoria de cierre

- `RELEASE-v5.23.md` contiene contrato, incidencias, métricas, artefactos y trazabilidad.
- README y `ESTADO_ACTUAL.md` reflejan v5.23.
- Graphify post-PR #100 procesó `main = 6a468a16f3a9590eab49c67e6796635aaf474fe7` con 675 nodos, 1.126 relaciones y 96 notas.
- Este último cierre documental debe volver a actualizar el `source_commit` de Graphify al `main` final.
- `stable` debe permanecer en el SHA funcional certificado durante los commits exclusivamente documentales.

## Próximo ciclo

**No existe una v5.24 abierta.**

Antes de crear una nueva release se debe:

1. auditar el estado público y técnico vigente;
2. identificar un problema observable y material;
3. definir objetivo, contrato y no-objetivos;
4. fijar criterios de cierre y gates;
5. abrir rama/PR solo después de esa definición.

No modificar retrospectivamente v5.23 para abrir nuevas funcionalidades.

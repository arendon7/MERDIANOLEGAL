# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**No hay una release funcional abierta. v5.19.0 quedó cerrada y certificada.**

El ciclo de foco comercial adaptativo terminó sin abrir v5.20 ni introducir integraciones, automatismos o deuda funcional nueva.

## Cierre v5.19.0

- PR funcional: #71.
- Merge fuente: `fcf8d868e5b95ab201c8ebb612ffba166f4746f5`.
- SHA público materializado y certificado: `9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.
- Run final de certificación: `31649425600`.
- PR de cierre documental: #72.
- Merge documental: `44feaf5e0bda3a2741dafca1c4ed91d9adec1b1d`.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; accesibilidad 1.00; performance 0.98–1.00.
- LCP máximo: 1368 ms; CLS máximo: 0.087; TBT máximo: 56 ms.
- CI hasta `stable`: 215 s, 22.9% mejor que baseline 279 s.
- cobertura reducida: no.
- budgets relajados: no.

`stable` conserva el snapshot público funcional certificado. Los commits documentales posteriores pueden avanzar `main` sin implicar una nueva release funcional.

## Contrato que permanece vigente

- `orientation` y `scope`: detalle secundario replegado inicialmente;
- `proposal` explícito en escritorio: detalle inicialmente expandido;
- móvil conserva v5.16;
- sin scoring o inferencia adicional;
- sin cambio automático de etapa;
- sin PII, persistencia, transporte, backend o CRM nuevos;
- contenido material siempre disponible mediante `<details>`.

## Graphify

La rama `knowledge/graphify-live` se regenera desde `main`. La verificación correcta no consiste en fijar aquí un SHA autocambiante: el último snapshot exitoso debe reportar versión `5.19.0` y un `source_commit` igual al commit de `main` que ese run procesó.

## Próximo ciclo

No iniciar v5.20 por arrastre. El siguiente frente debe abrirse como una tarea nueva, con objetivo, contrato, no-objetivos y criterio de cierre propios.

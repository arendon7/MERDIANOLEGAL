# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**v5.19.0 — foco comercial adaptativo — funcionalmente certificada; cierre documental en curso.**

No hay desarrollo funcional pendiente dentro de v5.19. El runtime público ya superó builder, idempotencia, validadores, Pages, smoke, Browser E2E, axe, Lighthouse y release-health y fue promovido a `stable`.

## Evidencia funcional

- PR funcional: #71.
- Merge fuente: `fcf8d868e5b95ab201c8ebb612ffba166f4746f5`.
- SHA público materializado: `9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.
- Run final: `31649425600`.
- Snapshot certificado al cierre funcional: `main == stable == 9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; accesibilidad 1.00; performance 0.98–1.00.
- LCP máximo: 1368 ms; CLS máximo: 0.087; TBT máximo: 56 ms.
- CI hasta `stable`: 215 s, 22.9% mejor que baseline 279 s.
- cobertura reducida: no.
- budgets relajados: no.

## Contrato v5.19

- `orientation` y `scope`: detalle secundario replegado inicialmente;
- `proposal` explícito en escritorio: detalle inicialmente expandido;
- móvil conserva v5.16;
- sin scoring o inferencia adicional;
- sin cambio automático de etapa;
- sin PII, persistencia, transporte, backend o CRM nuevos;
- contenido material siempre disponible mediante `<details>`.

## Condición de finalización

1. integrar `RELEASE-v5.19.md`;
2. alinear README y memoria canónica;
3. comprobar que el delta de cierre sea exclusivamente documental;
4. mergear el cierre documental;
5. verificar el run Graphify posterior y su frescura/versionado;
6. dejar explícito que no existe una v5.20 abierta.

No es necesario volver a modificar el snapshot público certificado salvo que un cambio funcional/publicable posterior lo requiera.

## No objetivos

- no nuevas features;
- no nuevas preguntas;
- no backend/CRM;
- no automatización externa de WhatsApp;
- no nueva analítica externa;
- no modificar el contrato certificado v5.19;
- no abrir v5.20 dentro de este cierre.

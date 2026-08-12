# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Estado

**v5.20.0 — compresión de decisión en portada — funcionalmente certificada; cierre documental en curso.**

No hay desarrollo funcional pendiente dentro de v5.20. El runtime público ya superó builder, idempotencia, validadores, Pages, smoke, Browser E2E, axe, Lighthouse y release-health y fue promovido a `stable`.

## Evidencia funcional

- PR funcional: #74.
- Hotfixes de compatibilidad: #75 y #76.
- SHA funcional final: `85bdcfc9b52172e085dfa9b1df8e8d081b136233`.
- Run final: `31651473515`.
- Snapshot certificado: `main == stable == 85bdcfc9b52172e085dfa9b1df8e8d081b136233` al cierre funcional.
- Browser E2E + axe: 37 → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- Lighthouse: 6/6 PASS; accesibilidad 1.00; performance 0.98–1.00.
- Portada: performance 1.00, accesibilidad 1.00, LCP 1421 ms, CLS 0, TBT 83 ms.
- CI hasta `stable`: 191 s, 31.5% mejor que baseline 279 s.
- cobertura reducida: no.
- budgets relajados: no.

## Contrato v5.20

- seis rutas por situación empresarial como primer paso;
- una sola superficie con cinco modalidades como segundo paso;
- estándar verificable v5.12 visible;
- límites y alternativas v5.14 disponibles mediante `<details>`;
- sin bloque separado v5.8 ni `#elegir` en la salida final;
- 16 fichas profundas intactas;
- sin scoring, inferencia adicional, cambio automático de etapa, PII, persistencia, transporte, backend o CRM nuevos.

## Cierre pendiente

1. integrar `RELEASE-v5.20.md`;
2. alinear README y memoria canónica;
3. confirmar que el diff es exclusivamente documental;
4. mergear el cierre documental;
5. verificar Graphify posterior y su frescura/versionado;
6. marcar el ciclo como formalmente cerrado y dejar explícito que no existe v5.21 abierta.

No es necesario modificar de nuevo el snapshot público `stable` salvo que exista un cambio funcional/publicable posterior.

## No objetivos

- no nuevas features;
- no ampliar catálogo;
- no reescribir fichas profundas;
- no backend/CRM;
- no automatización externa de WhatsApp;
- no nueva analítica externa;
- no modificar el contrato certificado v5.20;
- no abrir v5.21 dentro de este cierre.

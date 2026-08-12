# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release activa

**v5.20.0 — compresión de decisión en portada.**

La auditoría posterior a v5.19 confirmó que las 16 fichas profundas ya tienen suficiente detalle jurídico y comercial. El principal problema actual está en la portada: antes de llegar a la oferta, el prospecto encuentra varios mecanismos que vuelven a preguntarle cómo elegir o contratar.

## Objetivo

Reducir la arquitectura pública de decisión a dos capas claras:

1. **Situación empresarial:** conservar las seis rutas por necesidad de v5.1 como primer punto de entrada.
2. **Modalidad de contratación:** ofrecer después un único selector compacto con las cinco modalidades canónicas de v5.12/v5.14.

La comparación de límites y alternativas permanece disponible como información secundaria desplegable. Las 16 fichas profundas conservan íntegramente alcance, perímetro, entregables, formatos, responsabilidades, aceptación, límites y CTA.

## Qué se elimina de la portada

- el bloque separado de “Forma de contratar” v5.8;
- la repetición independiente de recomendación v5.14;
- la sección histórica “Cómo elegir”;
- cualquier duplicación que obligue a elegir varias veces entre producto, servicio, diagnóstico o capacidad recurrente.

No se oculta esa redundancia con CSS: la salida HTML final deja de materializar los bloques duplicados.

## Contrato v5.20

- las seis rutas por necesidad permanecen intactas;
- existen exactamente cinco modalidades de contratación en una sola superficie;
- el estándar verificable de propuesta v5.12 permanece visible;
- límites y alternativas v5.14 permanecen disponibles mediante `<details>`;
- v5.8, v5.12, v5.14 y v5.15 conservan continuidad contractual mediante validadores version-aware;
- las 16 fichas profundas no reducen contenido ni controles;
- no scoring;
- no inferencia automática de intención;
- no cambio automático de `decision_stage`;
- no PII, storage persistente, transporte de red, backend o CRM nuevos;
- v5.16, v5.17, v5.18 y v5.19 permanecen intactas en formulario/handoff;
- no reducción de 37 E2E, 7 superficies axe o 6 superficies Lighthouse;
- no relajación de budgets v5.5.

## Implementación

- `version.json`: `5.20.0`;
- `scripts/apply_decision_action_v515.py`: composición version-aware y eliminación real de redundancia en home;
- `decision-action-v515.css`: layout compacto v5.20 dentro de la capa ya gobernada;
- `scripts/validate_decision_v58.py`: continuidad v5.8 sin exigir el bloque visual histórico;
- `scripts/validate_proof_v512.py`: prueba/modalidad v5.12 dentro de la superficie unificada.

## Criterio de cierre

1. Release Governance: PASS sin relajar gates;
2. builder canónico e idempotencia: PASS;
3. todos los validadores históricos: PASS;
4. Pages + smoke público: PASS;
5. Browser E2E + axe: sin regresiones ni reducción de cobertura;
6. Lighthouse: 6/6 dentro de budgets vigentes;
7. release-health: PASS;
8. promoción de `stable` al SHA funcional certificado;
9. Graphify fresco y versionado en `5.20.0`;
10. documentación final de release y cierre de la tarea.

## No objetivos

- no ampliar catálogo;
- no reescribir las 16 fichas jurídicas;
- no añadir nuevas preguntas al formulario;
- no activar CRM/backend, firma, pagos, agenda o carga documental;
- no automatizar WhatsApp;
- no abrir v5.21 dentro de este ciclo.

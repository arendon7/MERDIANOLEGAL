# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release activa

**v5.19.0 — foco comercial adaptativo.**

La auditoría posterior al cierre de v5.18 detectó que la oferta profunda y el contrato jurídico están bien estructurados, pero el tramo final de contacto acumula demasiada información visible antes del handoff. El problema no requiere otra capa de calificación: requiere reducir carga cognitiva sin perder trazabilidad, límites ni control del usuario.

## Objetivo

Aplicar progressive disclosure también en escritorio sobre los bloques secundarios de v5.10 y v5.11, usando únicamente la intención comercial explícita ya existente:

- `orientation` y `scope`: detalle secundario inicialmente replegado;
- `proposal` explícito en escritorio: detalle inicialmente expandido;
- móvil: conservar el comportamiento v5.16 ya certificado;
- el encabezado, la ruta recomendada, el formulario y el material jurídico permanecen disponibles;
- abrir/cerrar información no cambia etapa, modalidad, recomendación ni contenido del handoff.

## Contrato v5.19

- no scoring;
- no inferencia de intención distinta del parámetro explícito existente;
- no cambio automático de `decision_stage`;
- no PII adicional;
- no `localStorage`/`sessionStorage` nuevo;
- no fetch/XHR/sendBeacon nuevo;
- no backend/CRM;
- no reducción de los 37 E2E, 7 superficies axe o 6 superficies Lighthouse;
- no relajación de budgets v5.5;
- no supresión de información material: se reordena mediante `<details>` nativo y accesible.

## Implementación fuente

- `decision-action-v515.js`: extensión `COMMERCIAL-FOCUS-V519` sobre el disclosure existente;
- `decision-action-v515.css`: estilos adaptativos escritorio/móvil;
- `scripts/validate_decision_action_v515.py`: hardening contractual v5.19 sin romper v5.15;
- `version.json`: `5.19.0`.

## Criterio de cierre

1. validator v5.15/v5.19: PASS;
2. builder canónico e idempotencia: PASS;
3. validators históricos: PASS;
4. Pages + smoke: PASS;
5. Browser E2E + axe: sin regresiones;
6. Lighthouse 6/6 dentro de budgets;
7. release-health: PASS;
8. promoción de `stable` al SHA público final;
9. Graphify fresco respecto del `main` procesado;
10. documentar evidencia final y cerrar la tarea.

## No objetivos

- no nuevas preguntas de formulario;
- no automatización de WhatsApp;
- no nueva analítica externa;
- no backend, CRM, firma, pagos, agenda o carga documental;
- no rediseño general de la oferta;
- no v5.20 dentro de este ciclo.

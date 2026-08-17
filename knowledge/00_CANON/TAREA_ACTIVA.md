# Meridiano Legal — Tarea activa

Actualizado: 2026-08-17.

## Estado

**v5.31.0 — compresión decisional del recorrido público: candidata activa.**

Baseline certificado:

`main = stable = 48b4deb97087f651d07628467be148807873f6fa` · v5.30.0.

La candidata se desarrolla en `feat/v531-decision-compression`. `stable` no debe moverse hasta superar Release Governance, builder canónico, idempotencia, Pages/smoke, Browser E2E/axe y Lighthouse.

## Problema observable

La auditoría posterior a v5.30 confirmó que la web ya tiene profundidad jurídica y comercial suficiente. La fricción está en la acumulación de capas válidas que permanecen abiertas a la vez.

- 16/16 fichas encadenan v5.8/v5.30, pregunta ejecutiva, resultado empresarial y v5.22 antes del núcleo técnico.
- 6/6 rutas de necesidad mantienen abiertas cuatro capas secundarias —objeciones, FAQ, rutas relacionadas y prueba/contexto— además de la ruta primaria.
- La portada también es extensa, pero ya ofrece accesos directos por necesidad y contacto y concentra referencias públicas de honorarios aprobadas; no se modifica estructuralmente en este ciclo.

Baseline detallado: `knowledge/30_RUNBOOKS/AUDIT-RECORRIDO-v5.31.md`.

## Contrato v5.31

1. Conservar íntegros catálogos, copy jurídico/comercial, límites, alternativas y honorarios aprobados.
2. Mantener en las 16 fichas exactamente dos grupos decisionales siempre abiertos antes del núcleo:
   - `buying-clarity-v58` + v5.30;
   - pregunta ejecutiva + resultado empresarial, agrupados visualmente.
3. Conservar `offer-narrative-v522` completo dentro de `<details>` nativo cerrado por defecto.
4. En las 6 rutas mantener abiertos hero, señales, encaje, decisiones, modalidad, honorarios, resultado, límites y CTA.
5. Pasar únicamente objeciones, FAQ, rutas relacionadas y prueba/contexto a `<details>` nativos.
6. No usar `display:none`, `visibility:hidden`, `hidden`, carga diferida o JavaScript para fingir menor densidad.
7. Mantener un único formulario físico, WhatsApp manual y semántica de funnel/handoff existente.
8. Conservar exactamente 30 pasos canónicos: v5.31 corre después de v5.30 dentro de `apply_handoff_observability_v518.py`.
9. Añadir validator y E2E específicos; conservar sin relajación todos los contratos históricos, axe y Lighthouse.

## No objetivos

No reescribir las 16 ofertas, no eliminar profundidad técnica, no modificar precios, no crear cotizador/CRM/backend, no rediseñar marca, no añadir dependencias de acordeón, no alterar contacto/handoff ni inferir conversión.

## Criterio de cierre

v5.31 solo se considera cerrada cuando la salida materializada sea idempotente, los contratos históricos y el validator v5.31 estén verdes, el recorrido E2E confirme divulgación progresiva y teclado/móvil, Lighthouse conserve budgets, Pages esté pública y `main = stable` en el SHA certificado.

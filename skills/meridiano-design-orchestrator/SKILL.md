---
name: meridiano-design-orchestrator
description: Orquesta auditoría, rediseño, UX, UI, motion, contenido y QA visual de Meridiano Legal usando el canon del proyecto y lentes especialistas externos sin permitir que la estética contradiga verdad jurídica, accesibilidad o gobernanza.
---

# Meridiano Design Orchestrator

## Propósito

Usar este skill para cualquier tarea que cambie o evalúe una superficie pública de Meridiano Legal: portada, fichas de servicio/producto, rutas de necesidad, contacto, sectores, perspectivas, firma, demo, navegación, responsive, componentes, motion o sistema visual.

Este skill no reemplaza `AGENTS.md`, el canon, los catálogos ni los validadores. Los coordina con lentes de diseño externos.

## Orden obligatorio de trabajo

1. Confirmar `main` y `stable` y leer el canon conforme a `AGENTS.md`.
2. Definir el problema observable de usuario antes de proponer una nueva versión.
3. Identificar la superficie, audiencia, tarea principal y estado responsive afectados.
4. Preservar verdad jurídica/comercial y capability truth antes de editar copy o UI.
5. Ejecutar las lentes de diseño aplicables del registro `design-skills.lock.json`.
6. Resolver contradicciones por precedencia, nunca por promedio entre skills.
7. Prototipar primero la menor superficie representativa posible.
8. Revisar desktop + mobile + teclado + reduced motion + estados de foco antes de propagar.
9. Implementar mediante las fuentes/generadores canónicos; evitar parches manuales divergentes.
10. Someter el cambio a los validadores y gates existentes; no debilitar contratos.

## Precedencia

Cuando dos reglas entren en conflicto, usar este orden:

1. Verdad legal, de producto y de evidencia de Meridiano.
2. Privacidad, seguridad, accesibilidad, semántica y performance.
3. Contratos UX y decisiones canónicas de Meridiano.
4. Sistema de diseño de Meridiano.
5. Skills externos especialistas.
6. Preferencia estética puntual.

Un skill externo nunca autoriza inventar clientes, resultados, precios, capacidades, portales, automatizaciones, evidencia o claims.

## Routing de skills

### Rediseño mayor / nueva dirección visual
Usar conjuntamente:
- `impeccable`
- `design-taste-frontend`
- `frontend-design-review`
- `web-design-guidelines`

Objetivo: dirección estética clara, jerarquía, IA, responsive, accesibilidad y criterio independiente.

### Arquitectura de información / carga cognitiva / journey
Priorizar:
- `impeccable`
- `frontend-design-review`
- `design-taste-frontend` en modo redesign/audit

La salida debe distinguir contenido primario, secundario y de respaldo; no ocultar profundidad material ni crear dark patterns.

### Motion y microinteracciones
Priorizar:
- `emil-design-eng`
- `make-interfaces-feel-better`
- `web-design-guidelines`

Motion debe explicar estado, continuidad o causalidad. No animar por decoración. Respetar `prefers-reduced-motion` y no degradar interacción en Safari/mobile.

### Sistema visual / tokens / consolidación CSS
Priorizar:
- `ui-craft`
- `impeccable`
- `frontend-design-review`

Objetivo: tokens coherentes, menos excepciones acumuladas, componentes distinguibles por función y ausencia de raw values arbitrarios cuando exista token equivalente.

### Accesibilidad y formularios
Priorizar:
- `web-design-guidelines`
- QA actual de Playwright/axe
- `frontend-design-review`

Axe es un gate, no una prueba completa de UX accesible. Revisar también teclado, nombres accesibles, foco, touch targets, orden de lectura y reduced motion.

### Pase de polish final
Priorizar:
- `make-interfaces-feel-better`
- `emil-design-eng`
- `gpt-taste`
- `ui-craft`

Este pase ocurre después de resolver arquitectura, copy y accesibilidad; nunca antes.

## Formato de una iteración de diseño

Cada iteración significativa debe dejar explícitos:

- `Problema observable`
- `Hipótesis`
- `Superficies afectadas`
- `No objetivos`
- `Lentes/skills usados`
- `Decisiones de diseño`
- `Riesgos jurídicos/UX`
- `Desktop/mobile/keyboard/reduced-motion`
- `Criterios de aceptación`
- `Resultado de crítica independiente`

## Reglas anti-sedimentación

- No crear automáticamente `vXXX.css` para cada corrección.
- Preferir consolidación de tokens/componentes cuando el cambio atraviese varias superficies.
- No multiplicar tarjetas cuando una composición editorial, tabla, timeline, lista o diagrama comunique mejor.
- No usar motion para compensar jerarquía pobre.
- No usar progressive disclosure para esconder información material necesaria para decidir.
- No introducir una nueva taxonomía de navegación sin demostrar qué problema resuelve.
- No cambiar URLs, anchors, nombres de campos o contratos E2E silenciosamente.

## Regla de copy

Editar primero para comprensión y decisión, luego para precisión y finalmente para tono.

Una superficie comercial debe permitir responder, en este orden:
1. ¿Qué problema resuelve?
2. ¿Para quién encaja/no encaja?
3. ¿Qué recibe el cliente?
4. ¿Cómo ocurre el trabajo?
5. ¿Qué límites tiene?
6. ¿Cuál es el siguiente paso?

La profundidad jurídica permanece disponible como soporte de la decisión, no como barrera de entrada.

## Cierre de diseño

No declarar una superficie lista solo porque “se ve mejor”. Debe demostrar mejora frente al problema inicial y conservar:
- semántica;
- accesibilidad;
- responsive;
- capability truth;
- evidencia/claims;
- contratos históricos aplicables;
- performance budgets;
- integridad del funnel/contacto.

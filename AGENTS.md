# AGENTS.md — Meridiano Legal

Este repositorio usa una memoria de ingeniería en capas. Estas reglas aplican a ChatGPT y a cualquier otro agente que trabaje sobre el proyecto.

## Orden obligatorio al iniciar una tarea

1. Confirmar los SHA actuales de `main` y `stable`.
2. Leer `knowledge/00_CANON/CONTEXTO_RAPIDO.md`.
3. Leer `knowledge/00_CANON/ESTADO_ACTUAL.md` y `knowledge/00_CANON/TAREA_ACTIVA.md`.
4. Consultar `graphify-out/BUILD_META.json`, `graphify-out/PROJECT_SNAPSHOT.md` y `graphify-out/wiki/` desde la rama `knowledge/graphify-live`.
5. Si `source_commit` no coincide con el `main` actual, tratar Graphify como obsoleto y usar `main` como autoridad.
6. Abrir solamente las fuentes, generadores, validadores y tests afectados por la tarea.
7. Consultar CHANGELOG, PRs o conversaciones antiguas solo cuando sea necesario reconstruir el motivo de una decisión.

## Autoridad

- `main`: verdad técnica y ejecutable.
- `stable`: último snapshot que superó la certificación pública aplicable.
- `knowledge/`: memoria humana de decisiones, arquitectura y handoff.
- `knowledge/graphify-live`: memoria estructural regenerable; nunca sustituye el código fuente.
- GitHub Actions + Playwright + axe + Lighthouse + validadores: autoridad de certificación.

## Reglas de trabajo

- No reconstruir el proyecto principalmente desde una conversación si el repositorio contiene información más reciente.
- No modificar `stable` antes de que todos los gates de la release correspondiente estén verdes.
- No rebajar validadores ni presupuestos para hacer pasar una release; corregir primero la causa.
- Una relación Graphify `INFERRED` es una hipótesis y debe verificarse contra fuente.
- Mantener separadas la memoria humana y los artefactos regenerables.
- Las notas de `knowledge/00_CANON` deben actualizarse cuando cambie materialmente el estado del proyecto o la tarea activa.
- Los cambios de arquitectura o de contrato que puedan volver a discutirse deben registrar un ADR en `knowledge/10_DECISIONES/`.

## Trabajo de diseño, UX y frontend

Para cualquier tarea que cambie o evalúe una superficie pública, leer además:

1. `skills/meridiano-design-orchestrator/SKILL.md`.
2. `design-skills.lock.json`.

El orquestador define qué lentes especialistas aplicar para rediseño, UX, UI, motion, accesibilidad, responsive, copy y polish. Los skills externos son lentes de trabajo, no autoridad sobre el canon.

Reglas adicionales:

- No abrir una nueva versión solo para aplicar una preferencia estética; primero definir un problema observable de usuario y criterio de éxito.
- No agregar otra capa CSS versionada por inercia cuando el problema sea sedimentación del sistema visual; considerar consolidación de tokens/componentes.
- Antes de propagar un rediseño a las 46 superficies HTML, validar una muestra representativa: portada, una ficha de producto, una ficha de servicio y mobile.
- Toda nueva animación debe justificar propósito, respetar `prefers-reduced-motion` y pasar revisión de accesibilidad/performance.
- Una mejora visual nunca puede inventar evidencia, clientes, resultados, precios, capacidades, portales ni automatizaciones.
- Para cambios mayores, exigir al menos una crítica independiente posterior a la implementación y anterior al freeze visual.

## Principio de velocidad

Antes de leer archivos masivamente, usar el contexto rápido y el mapa Graphify para construir el conjunto mínimo de impacto. El objetivo es reducir exploración repetida sin sacrificar verificación.

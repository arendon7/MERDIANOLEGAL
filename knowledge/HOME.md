---
type: home
project: Meridiano Legal
status: active
---

# Meridiano Legal — Home de conocimiento

Esta es la puerta de entrada recomendada al abrir el repositorio como vault de Obsidian.

## Empezar aquí

- [[00_CANON/CONTEXTO_RAPIDO|Contexto rápido]] — qué es el proyecto, oferta, fuentes y reglas que no deben reconstruirse.
- [[00_CANON/ESTADO_ACTUAL|Estado actual]] — versión, refs, integraciones y certificación observada.
- [[00_CANON/TAREA_ACTIVA|Tarea activa]] — frente en curso, bloqueo, evidencia y próximo paso verificable.
- [[20_ARQUITECTURA/MAPA_PROYECTO|Mapa del proyecto]] — fuentes, generadores, runtime, validadores y mapa de impacto.
- [[30_RUNBOOKS/FLUJO_DE_TRABAJO|Flujo de trabajo]] — cómo iniciar, implementar, validar y cerrar un ciclo.
- [[99_HANDOFF/COMO_RETOMAR|Cómo retomar]] — protocolo para chat/agente nuevo.

## Decisiones

- [[10_DECISIONES/ADR-001-graphify-obsidian|ADR-001 · Graphify + Obsidian]]

Crear nuevas decisiones desde [[98_TEMPLATES/ADR|plantilla ADR]].

## Graphify vivo

La memoria estructural no vive en `main`. Consultar en la rama `knowledge/graphify-live`:

- `graphify-out/BUILD_META.json` — comprobar primero `source_commit`;
- `graphify-out/PROJECT_SNAPSHOT.md` — fotografía compacta;
- `graphify-out/GRAPH_REPORT.md` — reporte arquitectónico;
- `graphify-out/wiki/index.md` — índice de comunidades y nodos.

Si el vault local contiene un `graphify-out/` recién generado, Obsidian puede navegarlo directamente junto con estas notas.

## Ciclo mental

**Estado → impacto → fuente → cambio → prueba → decisión → handoff.**

No usar el grafo para sustituir la lectura del código. No usar una conversación antigua para sustituir el estado canónico. No usar una nota humana para sustituir un gate de CI.

## Plantillas

- [[98_TEMPLATES/ADR|ADR]]
- [[98_TEMPLATES/HANDOFF_TAREA|Handoff de tarea]]
- [[98_TEMPLATES/CIERRE_RELEASE|Cierre de release]]

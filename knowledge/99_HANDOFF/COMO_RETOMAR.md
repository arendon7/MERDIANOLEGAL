# Cómo retomar Meridiano Legal en un chat nuevo

Mensaje recomendado:

> Retoma Meridiano Legal desde su memoria canónica. Confirma primero los SHA actuales de `main` y `stable`. Lee `knowledge/00_CANON/CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md`. Luego consulta `graphify-out/BUILD_META.json`, `PROJECT_SNAPSHOT.md`, `GRAPH_REPORT.md` y la wiki en la rama `knowledge/graphify-live`, verificando que `source_commit` corresponda al `main` actual. Usa después únicamente los archivos fuente, generadores, validadores y tests relevantes de `main`. No reconstruyas el proyecto desde conversaciones antiguas si el repositorio ya contiene información más reciente.

## Orden de recuperación

1. refs `main` y `stable`;
2. contexto rápido;
3. estado canónico y tarea activa;
4. Graphify vivo y verificación de frescura;
5. fuentes/tests afectados;
6. CHANGELOG/PRs/historial solo si hace falta explicar una decisión.

## Qué evita este protocolo

- releer decenas de archivos sin mapa de impacto;
- confundir outputs generados con fuentes;
- retomar una release desde un SHA intermedio;
- tratar una conversación antigua como fuente de verdad;
- volver a discutir decisiones ya registradas;
- mover `stable` con gates pendientes;
- confiar en relaciones Graphify inferidas sin confirmación.

## Cierre de una tarea

Cuando cambie materialmente el proyecto:

1. actualizar `knowledge/00_CANON/TAREA_ACTIVA.md`;
2. actualizar `ESTADO_ACTUAL.md` si cambia la versión, `stable`, una integración o un gate material;
3. crear/actualizar ADR si cambió una decisión arquitectónica o de contrato;
4. dejar que el workflow regenere `knowledge/graphify-live` desde el nuevo `main`;
5. comprobar que `BUILD_META.json.source_commit` coincida con `main`.

Las relaciones Graphify `INFERRED` nunca sustituyen la verificación del código fuente.
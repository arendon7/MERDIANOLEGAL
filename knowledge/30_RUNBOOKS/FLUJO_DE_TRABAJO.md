---
type: runbook
project: Meridiano Legal
---

# Flujo de trabajo con memoria de ingeniería

## 1. Inicio de una tarea

1. Confirmar `main` y `stable`.
2. Leer [[../00_CANON/CONTEXTO_RAPIDO|Contexto rápido]].
3. Leer [[../00_CANON/TAREA_ACTIVA|Tarea activa]].
4. Confirmar frescura de Graphify mediante `graphify-out/BUILD_META.json.source_commit`.
5. Usar la wiki Graphify para construir un conjunto mínimo de impacto.
6. Abrir en `main` únicamente fuentes, generadores, tests y validadores de ese conjunto.

El objetivo no es leer menos a cualquier costo; es evitar lectura repetida que no cambia la decisión.

## 2. Antes de modificar

Definir explícitamente:

- fuente de verdad que se modificará;
- outputs generados afectados;
- contratos históricos que deben preservarse;
- gates que pueden detectar una regresión;
- ref que no debe moverse todavía (`stable` durante una candidata no certificada).

Si la decisión cambia arquitectura o política persistente, preparar un ADR.

## 3. Implementación

- Preferir cambios atómicos.
- No editar outputs generados si existe una fuente/aplicador canónico que los produce.
- No debilitar un validator para ocultar un defecto real.
- Verificar relaciones Graphify `INFERRED` contra código antes de usarlas como fundamento.
- Releer `main` antes de actualizar refs si la implementación tomó varios pasos.

## 4. Validación proporcional

### Solo memoria

Cambios en `knowledge/**`, `AGENTS.md` o infraestructura Graphify:

- Graphify debe regenerarse y validar frescura.
- No debe desplegarse la web pública por ese cambio aislado.

### Fuente funcional/canónica

Ejecutar la cadena correspondiente:

- builder;
- idempotencia;
- validadores históricos + actuales;
- Pages;
- smoke live;
- Playwright/axe/Lighthouse cuando aplique;
- `stable` únicamente después de todos los gates verdes.

## 5. Cierre

Actualizar solo lo que cambió materialmente:

- [[../00_CANON/ESTADO_ACTUAL|ESTADO_ACTUAL]] — versión, refs, integraciones, gates o hechos persistentes;
- [[../00_CANON/TAREA_ACTIVA|TAREA_ACTIVA]] — siguiente frente o cierre del actual;
- `10_DECISIONES/` — decisiones arquitectónicas/contractuales;
- CHANGELOG/README/release docs — según disciplina de release, no como sustituto de la memoria operativa.

Después confirmar que `knowledge/graphify-live` se construyó desde el `main` final.

## 6. Handoff

Un chat nuevo no debería necesitar el chat anterior para ser productivo. Debe poder reconstruir el estado con:

1. refs;
2. contexto rápido;
3. tarea activa;
4. Graphify fresco;
5. fuentes/tests afectados.

Si no puede hacerlo, falta conocimiento persistente y debe corregirse la memoria, no ampliar indefinidamente el prompt de conversación.
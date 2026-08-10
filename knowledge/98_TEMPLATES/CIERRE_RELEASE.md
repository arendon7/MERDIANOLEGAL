---
type: template
template: release-close
---

# Cierre de release — vX.Y.Z

Fecha: YYYY-MM-DD.

## Resultado

Qué cambió materialmente y qué problema resuelve.

## Autoridad final

- `main`: `<SHA>`
- `stable`: `<SHA>`
- confirmar `main == stable`: sí/no
- URL pública: `<URL>`

## Gates

- builder: success
- idempotencia: success
- validadores estáticos: success
- deploy Pages: success
- smoke live: success
- Playwright: success
- axe: success/no aplica
- Lighthouse: success/no aplica

## Métricas o evidencia relevante

- ...

## Incidentes y aprendizaje

- Qué falló durante el ciclo.
- Cómo se corrigió.
- Qué regla o validator quedó para evitar repetición.

## Estado externo verdadero

Activos:
- ...

Preparados/no activos:
- ...

## Próximo ciclo

Hipótesis y objetivos, sin declarar trabajo futuro como ya ejecutado.

## Memoria

- actualizar `ESTADO_ACTUAL.md`;
- actualizar `TAREA_ACTIVA.md`;
- actualizar ADR si cambió arquitectura;
- verificar `knowledge/graphify-live` contra `main` final.
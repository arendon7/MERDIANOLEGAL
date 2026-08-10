# Meridiano Legal — Knowledge

Esta carpeta es la memoria humana persistente del proyecto. Su función es reducir reconstrucción de contexto, mantener coherencia entre conversaciones y separar claramente hechos, decisiones y estructura técnica.

## Capas de memoria

1. **GitHub `main`** — verdad técnica y ejecutable.
2. **GitHub `stable`** — último snapshot certificado por los gates públicos aplicables.
3. **`knowledge/00_CANON/`** — contexto humano compacto: estado, tarea activa y reglas que no deberían reconstruirse desde cero.
4. **`knowledge/10_DECISIONES/`** — ADR y razonamiento detrás de decisiones arquitectónicas o de proceso.
5. **`knowledge/20_ARQUITECTURA/`** — mapa humano de capas, fuentes, generadores, validadores y runtime.
6. **Rama `knowledge/graphify-live`** — grafo, reporte, snapshot y wiki estructural regenerables desde `main`.
7. **`knowledge/90_GRAPHIFY_AUTO/`** — export Obsidian detallado opcional y local; nunca se versiona.
8. **`knowledge/99_HANDOFF/`** — protocolo de reanudación cuando cambia el chat o el agente.

## Protocolo corto para ChatGPT

1. Confirmar `main` y `stable`.
2. Leer `00_CANON/CONTEXTO_RAPIDO.md`, `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md`.
3. Leer `graphify-out/BUILD_META.json` y `PROJECT_SNAPSHOT.md` desde `knowledge/graphify-live`.
4. Verificar que `source_commit` coincida con el `main` actual.
5. Consultar la wiki Graphify del módulo implicado.
6. Abrir en `main` solamente las fuentes y tests del conjunto de impacto.
7. Si Graphify marca una relación como inferida, confirmarla contra fuente antes de actuar.
8. Al cerrar un ciclo, actualizar la memoria humana si cambió el estado, el contrato o el siguiente paso.

## Obsidian en Mac

Abrir la raíz local de `MERDIANOLEGAL/` como vault. No es necesario versionar `.obsidian/`.

Para regenerar Graphify localmente:

```bash
./scripts/refresh_graphify_knowledge.sh
```

Obsidian podrá navegar simultáneamente:

- `knowledge/` — memoria humana;
- `graphify-out/wiki/` — mapa estructural compacto;
- `graphify-out/PROJECT_SNAPSHOT.md` — fotografía técnica del checkout actual.

Para generar además el export detallado por nodo:

```bash
GRAPHIFY_FULL_OBSIDIAN=1 ./scripts/refresh_graphify_knowledge.sh
```

Ese export se crea en `knowledge/90_GRAPHIFY_AUTO/`, está ignorado por Git y puede eliminarse sin pérdida.

## Regla de autoridad

Si una nota contradice a `main`, gana `main` y la nota debe corregirse. Si Graphify fue construido desde otro SHA, se considera obsoleto hasta su regeneración. GitHub Actions, Playwright, axe, Lighthouse y los validadores del repositorio siguen siendo la autoridad de certificación funcional.
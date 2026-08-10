# ADR-001 — Graphify + Obsidian como memoria de ingeniería

Estado: adopción propuesta mediante PR de infraestructura.
Fecha: 2026-08-10.

## Contexto

Meridiano Legal ya contiene múltiples generaciones de fuentes, renderizadores, normalizadores, validadores, workflows, rutas comerciales y contratos históricos. Cuando una conversación se agota o una tarea cambia de frente, se pierde tiempo reconstruyendo qué archivo es fuente, qué salida es generada, qué validator protege cada contrato y qué estado quedó certificado.

La experiencia validada en ELERRANTE demostró que separar memoria humana y memoria estructural reduce esa reconstrucción sin sustituir las pruebas funcionales.

## Decisión

Adoptar cuatro capas complementarias:

1. GitHub `main` como autoridad técnica.
2. GitHub `stable` como último snapshot certificado.
3. Graphify como grafo estructural regenerable, publicado fuera de `main`.
4. Obsidian/Markdown como memoria humana persistente y superficie de exploración local.

ChatGPT continúa como agente principal. Codex no es requisito.

## Mejoras específicas respecto del piloto de ELERRANTE

- Añadir `AGENTS.md` como puerta de entrada tool-agnostic para agentes.
- Separar `CONTEXTO_RAPIDO.md` de `ESTADO_ACTUAL.md` para reducir lectura inicial.
- Mantener `TAREA_ACTIVA.md` como handoff explícito del ciclo en curso.
- Generar `graphify-out/BUILD_META.json` con el SHA fuente y métricas, evitando inferir frescura desde el texto del reporte.
- Generar `graphify-out/PROJECT_SNAPSHOT.md` con versión, canal, conteos de superficies y tamaño del grafo.
- Excluir del corpus Graphify las salidas HTML y assets generados para concentrar el análisis en código fuente, generadores, runtime y tests.

## Reglas

1. La memoria estructural generada no se versiona en `main`; se publica en `knowledge/graphify-live`.
2. `knowledge/90_GRAPHIFY_AUTO/` es un export local opcional y nunca se versiona.
3. La superficie automática persistente principal es la wiki compacta `graphify-out/wiki/` más `BUILD_META.json` y `PROJECT_SNAPSHOT.md`.
4. Las notas humanas deben poder entenderse sin Graphify.
5. Graphify se ejecuta en modo `--code-only`; la extracción es AST local y no envía el código a un LLM.
6. Una relación `EXTRACTED` orienta navegación. Una relación `INFERRED` debe verificarse contra fuente antes de justificar una modificación.
7. La rama Graphify es regenerable y puede sobrescribirse; nunca contiene decisiones humanas exclusivas.
8. GitHub Actions, Playwright, axe, Lighthouse, validadores e idempotencia siguen siendo la autoridad de certificación.
9. La memoria no debe modificar el runtime público ni alterar el contenido legal/comercial por sí sola.
10. Cuando una decisión cambie arquitectura, contrato de build, definición comercial o política de release, debe registrarse o actualizarse un ADR.

## Resultado esperado

Al iniciar trabajo, ChatGPT obtiene primero una fotografía compacta del estado y un mapa de impacto. En lugar de releer decenas de archivos y largos historiales, puede dirigirse a las fuentes y tests relevantes, conservando a la vez la obligación de verificar el código real.

Al cerrar trabajo, `main` conserva decisiones humanas y la rama Graphify conserva una fotografía estructural del mismo `main`. Esto mejora continuidad, coherencia y velocidad sin convertir memoria o inferencias en una nueva fuente de verdad.
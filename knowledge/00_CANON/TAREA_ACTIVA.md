# Meridiano Legal — Tarea activa

Actualizado: 2026-08-10.

## Ciclo

v5.5 — Performance + Accessibility QA.

## Objetivo de release

Cerrar la candidata con presupuestos Lighthouse reproducibles, accesibilidad axe sin violaciones serias/críticas, E2E funcional y `stable` promovido únicamente después de la certificación pública completa.

## Memoria de ingeniería ya integrada

Antes de retomar el defecto funcional se cerró la mejora de continuidad del proyecto:

- PR #10 integró Graphify + Obsidian como memoria de ingeniería.
- `knowledge/` conserva contexto humano, estado, decisiones, arquitectura y handoff.
- `knowledge/graphify-live` publica el grafo regenerable desde `main`.
- `BUILD_META.json` permite validar frescura mediante `source_commit`.
- El corpus Graphify optimizado produjo en el piloto 341 nodos, 520 relaciones, 56 comunidades y 67 notas wiki.
- PR #11 separó cambios exclusivamente de memoria/Graphify del despliegue público para evitar ejecutar Pages, Playwright, axe y Lighthouse cuando el sitio no cambió.

Al iniciar o retomar trabajo usar primero `CONTEXTO_RAPIDO.md`, esta nota y Graphify; después abrir solamente las fuentes/tests afectadas.

## Estado funcional v5.5

- `stable` continúa en `6d95d96d00e1ce15ad0c110ca7511e1d0873e933` mientras exista un gate rojo.
- Playwright + axe: verde.
- 5/6 superficies Lighthouse: dentro de presupuesto.
- Portada: performance 0.85; accessibility 0.97; LCP ~1206 ms; TBT 0 ms; transferencia ~73.9 KB.
- Bloqueo único: CLS ~0.304, presupuesto <=0.15.
- Nodo responsable reportado por Lighthouse: `main#contenido > section.hero > div.container > div.hero-art`.

## Hipótesis técnica prioritaria

La imagen del hero ya tiene dimensiones HTML, pero su comportamiento visual puede cambiar después del primer layout cuando el runtime/capa visual aplica clases o posicionamiento. La corrección debe estabilizar el espacio del hero desde el primer render CSS y eliminar cualquier cambio de flujo posterior causado por JavaScript o reglas tardías.

## Próximo paso verificable

1. confirmar los refs actuales de `main` y `stable`;
2. consultar la comunidad Graphify de `visual-v39.js`/runtime de portada y luego verificar en fuente `visual-v39.css`, `site-v3.css`, `ux-v45.css` y cualquier regla de `.hero-art` / `.visual-home-hero`;
3. aplicar una corrección fuente mínima que reserve el layout definitivo desde el primer render;
4. no tocar el presupuesto CLS;
5. reconstruir;
6. exigir idempotencia + validadores + Pages + smoke + Playwright/axe + seis Lighthouse;
7. mover `stable` solo si toda la cadena queda verde;
8. documentar el cierre y actualizar esta nota.

## Regla de separación

La memoria de ingeniería está ya operativa. A partir de aquí los cambios de `knowledge/**` deben regenerar Graphify sin desplegar el sitio; los cambios funcionales de v5.5 sí deben recorrer la certificación pública completa.
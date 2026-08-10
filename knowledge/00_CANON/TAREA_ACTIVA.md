# Meridiano Legal — Tarea activa

Actualizado: 2026-08-10.

## Ciclo

v5.5 — Performance + Accessibility QA.

## Objetivo de release

Cerrar la candidata con presupuestos Lighthouse reproducibles, accesibilidad axe sin violaciones serias/críticas, E2E funcional y `stable` promovido únicamente después de la certificación pública completa.

## Estado verificado antes de pausar para integrar memoria de ingeniería

- `main` base: `a6559ea0e5288c0e2b86e189ce6856acedcbac57`.
- `stable`: `6d95d96d00e1ce15ad0c110ca7511e1d0873e933`.
- Playwright + axe: verde.
- 5/6 superficies Lighthouse: dentro de presupuesto.
- Portada: performance 0.85; accessibility 0.97; LCP ~1206 ms; TBT 0 ms; transferencia ~73.9 KB.
- Bloqueo único: CLS ~0.304, presupuesto <=0.15.
- Nodo responsable reportado por Lighthouse: `main#contenido > section.hero > div.container > div.hero-art`.

## Hipótesis técnica prioritaria

La imagen del hero ya tiene dimensiones HTML, pero su comportamiento visual puede cambiar después del primer layout cuando el runtime/capa visual aplica clases o posicionamiento. La corrección debe estabilizar el espacio del hero desde el primer render CSS y eliminar cualquier cambio de flujo posterior causado por JavaScript o reglas tardías.

## Próximo paso verificable

1. inspeccionar `visual-v39.css`, `site-v3.css`, `ux-v45.css` y cualquier regla de `.hero-art` / `.visual-home-hero`;
2. aplicar una corrección fuente mínima que reserve el layout definitivo desde el primer render;
3. no tocar el presupuesto CLS;
4. reconstruir;
5. exigir idempotencia + validadores + Pages + smoke + Playwright/axe + seis Lighthouse;
6. mover `stable` solo si toda la cadena queda verde;
7. documentar el cierre y actualizar esta nota.

## No mezclar

La integración Graphify + Obsidian es infraestructura/memoria y no debe confundirse con la corrección funcional del CLS. Si cambia `main` por esta infraestructura, volver a confirmar el SHA antes de retomar v5.5.
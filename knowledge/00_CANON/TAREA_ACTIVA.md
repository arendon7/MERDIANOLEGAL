# Meridiano Legal — Tarea activa

Actualizado: 2026-08-10.

## Ciclo cerrado

**v5.5 — Performance + Accessibility QA: funcionalmente certificado.**

Evidencia principal:

- run `31431923694`;
- candidata funcional `bd310076bbc098771dffd8fde03cabee9e16bc6f` antes del cierre documental;
- idempotencia y validadores: verdes;
- Pages: verde;
- smoke público: verde;
- Browser E2E: 35 passed / 2 skipped / 0 failed;
- axe: 7 superficies sin violaciones serias/críticas;
- Lighthouse: 6/6 superficies dentro de presupuesto;
- CLS portada: ~0.304 → 0;
- performance portada: ~0.85 → 1.00;
- `stable` fue promovido después de la certificación funcional.

## Aprendizaje consolidado

El bloqueo CLS no era peso ni dimensión de imagen. Era una mutación tardía de estado de layout: `visual-v39.js` añadía `visual-home-hero` después del primer render y la imagen pasaba a `position:absolute`.

La corrección definitiva se distribuye entre:

- `scripts/apply_visual_assets.py` — estado visual desde HTML inicial;
- `visual-v39.js` — sin adición tardía de clase;
- `scripts/normalize_quality_v48.py` — compatibilidad con la capa histórica que reconstruye el hero;
- `scripts/validate_visual_assets.py` — contrato v5.5;
- `scripts/validate_quality_v48.py` — requisito histórico semántico, no dependiente del orden de atributos.

No se modificó el presupuesto CLS.

## Memoria de ingeniería

Graphify + Obsidian está integrado y debe usarse en el siguiente ciclo:

1. refs actuales;
2. contexto/estado/tarea;
3. `BUILD_META.json` y wiki Graphify;
4. conjunto mínimo de impacto;
5. fuente + tests;
6. implementación;
7. gates;
8. actualización de memoria.

Los cambios solo de `knowledge/**` ya no disparan la certificación pública completa.

## Próximo ciclo propuesto

**v5.6 — Eficiencia de CI y observabilidad de calidad, sin pérdida de cobertura.**

Objetivo: reducir tiempo y costo de validación ahora que los gates de navegador ya son confiables, manteniendo exactamente el mismo estándar de aprobación.

Frentes a evaluar:

- distinguir qué cambios requieren Browser E2E/Lighthouse completo y cuáles pueden usar un subconjunto seguro antes del cierre final;
- reutilización/caché reproducible de dependencias y navegadores si GitHub Actions lo permite sin introducir fragilidad;
- evitar ejecuciones duplicadas entre builder y Pages;
- conservar un pipeline completo obligatorio antes de mover `stable`;
- producir un resumen de calidad compacto que Graphify/Obsidian pueda enlazar para evitar leer logs extensos;
- revisar tiempos reales de cada job antes de optimizar, no asumir el cuello de botella.

## Regla para v5.6

No reducir navegadores, tests, axe, superficies Lighthouse ni presupuestos simplemente para acelerar CI. La optimización debe eliminar trabajo redundante o mejorar reutilización, no bajar el estándar de release.

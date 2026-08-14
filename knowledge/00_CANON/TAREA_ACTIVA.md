# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**v5.26.0 — simplificación editorial e integración visual: activa.**

Baseline funcional certificado:

`stable = b5a23e0ac1b675cade3ad69d197bbf86d5b998d8` (v5.25.0).

## Problema observable

La web ya tiene profundidad jurídica, 16 ofertas diferenciadas, autoridad profesional y un funnel comercial certificado, pero la auditoría post-v5.25 detectó una brecha visual y de densidad:

- `assets/images/` contiene un solo raster (`home-hero.webp`);
- los mockups e imágenes aprobadas previamente no fueron incorporados físicamente al repositorio;
- la portada materializa consecutivamente métricas de oferta, audiencias, seis rutas de necesidad, modalidad, prueba, servicios, productos, sectores, firma y contacto;
- dos bandas tempranas (`principles` y `audience-strip`) repiten contexto antes de que el usuario llegue al verdadero punto de entrada por necesidad.

## Contrato v5.26

1. `visual-assets-v526.json` clasifica activos como presentes, recuperados del historial o referencias pendientes de binario.
2. Ningún archivo externo pendiente puede producir una URL pública rota.
3. Se recupera `assets/decision-map-v526.svg` desde la rama histórica v3.1.
4. Las bandas históricas de métricas y audiencias se consolidan en una sola superficie editorial/visual antes de `#necesidades`.
5. La jerarquía visible superior queda: hero → señal editorial → necesidad → modalidad.
6. El hero mantiene el contenido jurídico canónico v5.22, pero la imagen adquiere mayor peso estructural.
7. Se preservan las seis rutas de necesidad, las cinco modalidades, la prueba verificable, servicios, productos, sectores, autoridad y contacto.
8. No se oculta contenido material mediante trucos de CSS; la consolidación se materializa en DOM mediante compositor final.
9. v5.26 se integra dentro del paso canónico v5.18+ y no altera los 30 pasos de v5.24.
10. No se reducen validators, E2E, axe, Lighthouse ni budgets.

## Dirección de diseño

Criterios aplicados: jerarquía y UX writing tipo Impeccable, baja densidad y ausencia de patrones genéricos tipo Taste, e interacción sobria y funcional en línea con Emil Kowalski. La identidad se apoya en navy, blue, ivory y gold; menos tarjetas, más tipografía, espacio y visuales con función.

## No objetivos

No se inventan imágenes, clientes, testimonios o casos; no se migra a Wix u otro builder; no se incorpora backend, CRM, portal real, storage, pagos, firma, PII ni nueva analítica; no se reescriben a ciegas las 16 fichas profundas.

## Cierre

Compositor y validator v5.26, E2E responsive, builder/idempotencia, validadores históricos, Pages/smoke, Browser/axe, Lighthouse 6/6 y release-health deben permanecer verdes antes de mover `stable`. Después se cerrará documentación y Graphify.

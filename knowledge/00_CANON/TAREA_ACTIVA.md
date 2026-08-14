# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**v5.28.0 — compresión de la ruta de conversión: activa.**

Baseline funcional certificado:

`stable = 26c90ec3a0e1ea08ae251673cba0a7fc56b4e0b2` (v5.27.0).

## Problema observable

v5.27 resolvió la densidad de las colecciones comerciales en móvil, pero el recorrido lineal mantiene una fricción de conversión:

- `#contratacion` ya explica necesidad → calificación → propuesta → inicio;
- después de ese cierre comercial aparecen sectores, perspectivas, autoridad/firma y FAQ antes del único `#contacto`;
- el formulario vuelve a abrir con un preámbulo de tres tarjetas que repite el mismo proceso;
- dentro del formulario, las rejillas de síntesis comercial vuelven a crecer verticalmente en móvil aunque el proceso detallado v5.23 ya está correctamente colapsado.

## Contrato v5.28

1. `#contacto` se materializa inmediatamente después de `#contratacion`.
2. Sectores, perspectivas, firma y FAQ permanecen íntegros en DOM y pasan a ser profundidad opcional posterior al punto de contacto.
3. El preámbulo de tres tarjetas se sustituye por una única franja de preparación con tres datos mínimos: decisión/problema, plazo/urgencia y resultado esperado.
4. No se modifica el único formulario físico ni sus campos obligatorios.
5. Se preservan v5.9 calificación, v5.10 propuesta/cierre, v5.11 engagement, v5.13 brief, v5.14 recomendación, v5.23 síntesis/proceso y v5.17–v5.18 handoff manual/observabilidad.
6. En <=620 px, `contact-synthesis-grid-v523` y `contact-brief-grid-v523` usan scroll horizontal local contenido; no se permite overflow global.
7. Después de `#contacto` se ofrece navegación breve a sectores, perspectivas, firma y FAQ para quien necesite más evidencia antes de decidir.
8. v5.28 se ejecuta después de v5.26 dentro de la extensión canónica `v5.18+`; el manifiesto v5.24 permanece en 30 pasos.
9. `scripts/validate_conversion_path_v528.py` y `tests/e2e/conversion-path-v528.spec.mjs` protegen orden, unicidad, profundidad preservada y responsive.
10. No se reducen validators, E2E, axe, Lighthouse ni budgets.

## No objetivos

No crear backend, CRM, agenda, pagos, firma, autenticación, carga documental o portal real; no inventar clientes, resultados o pruebas sociales; no reescribir las 16 fichas; no eliminar sectores, perspectivas, firma o FAQ; no convertir el contacto en aceptación automática del encargo.

## Decisión registrada

`knowledge/10_DECISIONES/ADR-002-conversion-path-v528.md` documenta la reubicación del contacto y sus consecuencias.

## Cierre requerido

Compositor + validator v5.28, idempotencia, validadores históricos, Release Governance, Pages/smoke, Browser E2E/axe, Lighthouse y release-health deben permanecer verdes antes de mover `stable`. Después se cerrarán `ESTADO_ACTUAL.md`, `CONTEXTO_RAPIDO.md`, release note y Graphify.

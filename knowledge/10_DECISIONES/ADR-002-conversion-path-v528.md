# ADR-002 — Acercar el contacto al cierre comercial sin retirar profundidad

Fecha: 2026-08-14
Estado: propuesta para v5.28

## Contexto

Después de v5.27 la portada conserva profundidad jurídica y mejoró sustancialmente su densidad móvil, pero el orden natural todavía obliga a atravesar sectores, perspectivas, autoridad profesional y FAQ después del bloque comercial antes de llegar al único formulario canónico. Al mismo tiempo, `#contacto` repite una secuencia de tres tarjetas que ya fue explicada en `#contratacion`.

La web ya dispone de CTAs directos a `#contacto`, pero la arquitectura editorial debe funcionar también para quien recorre la página de manera lineal. El objetivo no es ocultar información ni reducir controles jurídicos, sino separar el punto de acción de la profundidad opcional.

## Decisión

1. Mantener un único formulario físico canónico y el handoff manual a WhatsApp.
2. Mantener intactos calificación v5.9, cierre v5.10, engagement v5.11, síntesis/recomendación v5.23 y límites de capacidad real.
3. Reubicar `#contacto` inmediatamente después de `#contratacion` y antes de sectores, perspectivas, firma y FAQ.
4. Consolidar el preámbulo de tres tarjetas de contacto en una única franja operativa con tres datos mínimos: decisión/problema, plazo/urgencia y resultado esperado.
5. Mantener sectores, perspectivas, firma y FAQ en DOM y acceso público; después del contacto se ofrece una navegación corta para continuar profundizando.
6. En móvil, convertir únicamente las rejillas de síntesis comercial en scroll horizontal contenido, sin introducir overflow global ni ocultar información.
7. Materializar v5.28 mediante compositor y validator dentro de la extensión canónica `v5.18+`, después de v5.26, manteniendo los 30 pasos de v5.24.
8. No mover `stable` hasta que idempotencia, validadores históricos, Release Governance, Pages/smoke, Browser E2E/axe y Lighthouse permanezcan verdes.

## Consecuencias

### Positivas

- Reduce la distancia editorial entre comprensión de honorarios/contratación y presentación de la necesidad.
- Mantiene la profundidad disponible para compradores que necesitan más evidencia antes de avanzar.
- Elimina una repetición visible sin retirar condiciones jurídicas materiales.
- Conserva el contrato histórico de un solo formulario y WhatsApp manual.

### Riesgos

- Reordenar `#contacto` puede afectar selectores o tests que asuman que el formulario es el último bloque de la portada.
- El scroll horizontal de síntesis debe quedar contenido para no repetir la regresión móvil de v5.26.
- La nueva ubicación no puede interpretarse como aceptación automática del encargo; el copy y los bloques v5.9–v5.23 mantienen expresamente esa frontera.

## Verificación

- `scripts/validate_conversion_path_v528.py` comprueba orden, unicidad, profundidad preservada y contrato CSS.
- `tests/e2e/conversion-path-v528.spec.mjs` comprueba secuencia DOM, único formulario, navegación posterior, síntesis móvil y ausencia de overflow global.
- Los validators históricos siguen siendo obligatorios.

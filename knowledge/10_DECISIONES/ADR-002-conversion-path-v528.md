# ADR-002 — Acercar el contacto al cierre comercial sin retirar profundidad

Fecha: 2026-08-14
Estado: **aceptada e implementada en v5.28.0**

## Contexto

Después de v5.27 la portada conservaba profundidad jurídica y había mejorado sustancialmente su densidad móvil, pero el orden natural obligaba a atravesar sectores, perspectivas, autoridad profesional y FAQ después del bloque comercial antes de llegar al único formulario canónico. Al mismo tiempo, `#contacto` repetía una secuencia de tres tarjetas ya explicada en `#contratacion`.

La web ya disponía de CTAs directos a `#contacto`, pero la arquitectura editorial debía funcionar también para quien recorre la página de manera lineal. El objetivo no era ocultar información ni reducir controles jurídicos, sino separar el punto de acción de la profundidad opcional.

## Decisión

1. Mantener un único formulario físico canónico y el handoff manual a WhatsApp.
2. Mantener intactos calificación v5.9, cierre v5.10, engagement v5.11, síntesis/recomendación v5.23 y límites de capacidad real.
3. Reubicar `#contacto` inmediatamente después de `#contratacion` y antes de sectores, perspectivas, firma y FAQ.
4. Consolidar el preámbulo de tres tarjetas de contacto en una única franja operativa con tres datos mínimos: decisión/problema, plazo/urgencia y resultado esperado.
5. Mantener sectores, perspectivas, firma y FAQ en DOM y acceso público; después del contacto se ofrece una navegación corta para continuar profundizando.
6. En móvil, convertir únicamente las rejillas de síntesis comercial en scroll horizontal contenido, sin introducir overflow global ni ocultar información.
7. Hacer focables las regiones horizontalmente desplazables. En elementos `<dl>`, preservar la semántica nativa y añadir `tabindex`/`aria-label` sin sustituirla mediante `role="region"`.
8. Materializar v5.28 mediante compositor y validator dentro de la extensión canónica `v5.18+`, después de v5.26, manteniendo los 30 pasos de v5.24.
9. No mover `stable` hasta que idempotencia, validadores históricos, Release Governance, Pages/smoke, Browser E2E/axe y Lighthouse permanezcan verdes.

## Consecuencias

### Positivas

- Reduce la distancia editorial entre comprensión de honorarios/contratación y presentación de la necesidad.
- Mantiene la profundidad disponible para compradores que necesitan más evidencia antes de avanzar.
- Elimina una repetición visible sin retirar condiciones jurídicas materiales.
- Conserva el contrato histórico de un solo formulario y WhatsApp manual.
- Los decks móviles siguen siendo operables por teclado sin degradar la semántica HTML.

### Riesgos verificados durante implementación

- Reordenar `#contacto` rompió una expectativa histórica del validator UX v4.5. Se resolvió haciéndolo version-aware, sin retirar el contrato antiguo para versiones previas.
- El compositor introdujo diferencias de whitespace entre pasadas. Se normalizó el formato para conservar idempotencia estricta.
- El primer tratamiento de accesibilidad añadió `role="region"` a `<dl>`, lo que rompió la relación semántica `dt/dd`. Se corrigió preservando la semántica nativa.
- El acento inicial de la franja de preparación no alcanzaba contraste AA; se oscureció sin modificar la identidad visual general.

## Verificación final

- `scripts/validate_conversion_path_v528.py`: PASS.
- `tests/e2e/conversion-path-v528.spec.mjs`: PASS en Chromium desktop, Chromium mobile y WebKit.
- Browser E2E/axe final: 79 observados · 77 PASS · 2 SKIP · 0 FAIL · 0 retries.
- Lighthouse: PASS contra budgets existentes.
- Release Governance: PASS.
- Idempotencia canónica: PASS.
- Pages/smoke: PASS.
- `stable`: promovido únicamente después de gates verdes.

## Resultado

La decisión queda implementada y certificada en v5.28.0. La baseline funcional certificada previa al cierre documental es `786bd9d4dc720f027f64067c9dd83d583e7e934c`.

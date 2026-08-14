# Meridiano Legal v5.28.0 — Ruta de conversión compacta

Fecha de cierre: 2026-08-14
Estado: certificada

## Objetivo

Reducir la fricción entre la comprensión de contratación/honorarios y la presentación de una necesidad, sin retirar profundidad jurídica, evidencia profesional ni controles de capacidad real.

## Cambios funcionales

- `#contacto` pasa inmediatamente después de `#contratacion`.
- Sectores, perspectivas, firma y FAQ permanecen íntegros después del contacto como profundidad opcional.
- El preámbulo repetido de tres tarjetas se consolida en una sola franja operativa con:
  1. decisión o problema;
  2. plazo o urgencia;
  3. resultado esperado.
- Se conserva un único formulario físico canónico.
- Se preservan calificación v5.9, propuesta/cierre v5.10, engagement v5.11, brief v5.13, recomendación v5.14, síntesis/proceso v5.23 y handoff manual/observabilidad v5.17–v5.18.
- En móvil, las rejillas de síntesis y modalidad se convierten en decks horizontales contenidos.
- Las regiones desplazables son accesibles por teclado.
- Los decks `<dl>` conservan semántica nativa `dt/dd`; no se sobrescribe mediante `role="region"`.
- La navegación posterior al contacto permite volver a sectores, perspectivas, firma y FAQ.

## Gobierno y arquitectura

- v5.28 se ejecuta después de v5.26 dentro de la extensión final `v5.18+`.
- El pipeline canónico permanece en exactamente 30 pasos.
- Se añadió `scripts/apply_conversion_path_v528.py`.
- Se añadió `scripts/validate_conversion_path_v528.py`.
- Se añadió `tests/e2e/conversion-path-v528.spec.mjs`.
- Se añadió `conversion-path-v528.css`.
- ADR: `knowledge/10_DECISIONES/ADR-002-conversion-path-v528.md`.
- `validate_ux_v45.py` quedó version-aware: mantiene el orden histórico hasta v5.27 y exige la nueva secuencia desde v5.28.

## Incidencias detectadas y corregidas por CI

### 1. Idempotencia

La primera materialización v5.28 produjo tres diferencias de whitespace en segunda pasada. Se corrigió el compositor para normalizar separadores de forma determinista. `git diff --exit-code` permanece estricto.

### 2. Orden narrativo histórico

El validator v4.5 codificaba el contacto como último bloque. Se mantuvo esa regla para versiones previas y se introdujo el contrato v5.28 `contratación → contacto → sectores → perspectivas → firma → FAQ`.

### 3. Contraste y foco

Axe detectó contraste insuficiente en la etiqueta de preparación y regiones horizontalmente desplazables no focables. El color se ajustó a `#725431` sobre el fondo crema y los decks recibieron foco de teclado.

### 4. Semántica de listas de definición

El primer ajuste de foco usó `role="region"` sobre `<dl>`, provocando `dlitem` en axe. Se eliminó ese override, conservando `tabindex="0"` y `aria-label`; los `<dt>/<dd>` recuperaron su semántica nativa.

## Certificación final

Baseline funcional certificada: `786bd9d4dc720f027f64067c9dd83d583e7e934c`.

- Builder final: `31819573869` — PASS.
- Site Quality and Deploy: `31819606409` — PASS.
- Release Governance final relevante: `31819530202` — PASS.
- 30 pasos canónicos: PASS.
- 37 validaciones estáticas: PASS.
- GitHub Pages: PASS.
- Smoke público: PASS.
- Browser E2E/axe: **79 observados · 77 PASS · 2 SKIP · 0 FAIL · 0 retries**.
- Lighthouse: PASS contra budgets existentes.
- Artefactos de fallo finales: ninguno.
- Promoción automática de `stable`: PASS.
- Budgets relajados: no.
- Cobertura reducida: no.

## Estado de memoria

Graphify v0.9.26 dispone de un snapshot verde v5.28 con 740 nodos, 1.256 aristas y 100 notas wiki, construido desde `7f9caa0a77923b79da6b1d5e2054680dfce0f63d`. Al ser anterior al commit canónico final, `main` continúa siendo autoridad hasta la siguiente regeneración.

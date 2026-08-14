# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**Sin tarea funcional activa. v5.28.0 está cerrada y certificada.**

Baseline funcional certificada previa al commit documental de cierre:

`main = stable = 786bd9d4dc720f027f64067c9dd83d583e7e934c` (v5.28.0).

## Último ciclo cerrado

v5.28 comprimió la ruta de conversión sin retirar profundidad:

1. `#contacto` quedó inmediatamente después de `#contratacion`.
2. Sectores, perspectivas, firma y FAQ permanecen íntegros como profundidad opcional posterior.
3. El preámbulo repetido se consolidó en una franja operativa de tres datos mínimos.
4. El único formulario físico, la calificación, la recomendación, el proceso y el handoff manual a WhatsApp permanecen intactos.
5. Los decks móviles de síntesis usan scroll local contenido y son focables.
6. Los `<dl>` preservan su semántica nativa; no usan `role="region"`.
7. El pipeline canónico continúa en exactamente 30 pasos.

## Evidencia de cierre

- Builder: `31819573869` — PASS.
- Site Quality & Deploy: `31819606409` — PASS.
- Release Governance final: `31819530202` — PASS.
- Browser E2E/axe: 79 observados · 77 PASS · 2 SKIP · 0 FAIL · 0 retries.
- Lighthouse: PASS.
- Pages/smoke: PASS.
- `stable` promovido automáticamente: PASS.

## Qué no debe asumirse

No existe todavía un alcance v5.29 aprobado. Cualquier nuevo ciclo debe partir de la release v5.28 certificada, registrar su problema observable, contrato y gates antes de modificar la arquitectura pública.

## Decisión registrada

`knowledge/10_DECISIONES/ADR-002-conversion-path-v528.md` queda aceptada e implementada con v5.28.

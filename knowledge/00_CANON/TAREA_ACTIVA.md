# Meridiano Legal — Tarea activa

Actualizado: 2026-08-13.

## Estado

**No hay una release funcional activa.**

v5.22.0 — arquitectura editorial de oferta y narrativa jurídica senior — está implementada, desplegada, certificada y funcionalmente cerrada.

Snapshot funcional certificado:

`5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`

Run público final:

`31671834728`

Al cierre funcional:

`main == stable == 5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`.

El trabajo actual es exclusivamente de cierre documental y sincronización de memoria. Los commits documentales pueden hacer avanzar `main` sin mover `stable` si el runtime certificado no cambia.

## Qué quedó resuelto en v5.22

1. Las 16 ofertas tienen contrato editorial único y source-driven.
2. Productos y servicios se distinguen por lógica de contratación y no solo por nombre.
3. Cinco pares solapados tienen alternativa recíproca y diferencia verificable.
4. Cada ficha explica decisión empresarial, modalidad, capacidad instalada y lente jurídica.
5. La portada conserva una sola superficie de decisión v5.20.
6. El seniority se demuestra con criterio, método, fuentes, responsables, límites y cierre; no con claims no verificables.
7. Capability truth vive en los JSON fuente v4.1/v4.2.
8. `Meridiano Empresas` solo puede aparecer con condición productiva real o como demostración explícita.
9. El runtime preserva el HTML prerenderizado static-first y no rehidrata destructivamente `#detail-page`.
10. El último contraste AA pendiente de las fichas profundas quedó corregido sin relajar axe ni budgets.

## Evidencia de cierre

- Release Governance: PASS.
- Builder canónico: PASS.
- Segunda pasada/idempotencia: PASS.
- Validadores históricos + v5.22: PASS.
- Pages + smoke: PASS.
- Browser E2E + axe: 49 observados → 47 PASS / 2 SKIP / 0 FAIL / 0 RETRY.
- 7 superficies axe WCAG 2.1 AA limpias de violaciones serias/críticas.
- Lighthouse: 6/6 PASS.
- Accesibilidad Lighthouse: 1.00 en las seis superficies.
- CI hasta `stable`: 206 s frente a baseline 279 s; mejora 26.2%.
- Cobertura reducida: no.
- Budgets relajados: no.
- `stable`: promovida correctamente al SHA funcional final.

## Archivos canónicos de referencia

- `RELEASE-v5.22.md` — evidencia y decisiones completas de la release.
- `offer-narrative-v522.json` — contrato editorial de las 16 ofertas.
- `offer-v522.css` — capa visual trust-first.
- `scripts/apply_offer_narrative_v522.py` — materialización final.
- `scripts/validate_offer_narrative_v522.py` — contrato anti-drift.
- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica/comercial.
- `tests/e2e/offer-narrative.spec.mjs` — cobertura Browser específica.
- `knowledge/00_CANON/ESTADO_ACTUAL.md` — estado canónico.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md` — orientación rápida.

## Invariantes que siguen vigentes

- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- static-first;
- 49 E2E observados como piso certificado;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- sin scoring o inferencia automática nueva;
- sin PII, storage persistente o transporte nuevo;
- WhatsApp manual;
- portal real deshabilitado;
- no CRM/backend, autenticación real, firma, pagos, agenda o carga documental ficticios;
- no testimonios, clientes, premios, cifras de experiencia o resultados no verificables;
- no mutar contratos fuente silenciosamente después del render.

## Siguiente ciclo

**No abrir v5.23 por inercia.**

Antes de cualquier release funcional posterior:

1. releer `ESTADO_ACTUAL.md`, `TAREA_ACTIVA.md`, `version.json`, `site-config.json` y Graphify fresco;
2. auditar la experiencia pública ya certificada;
3. identificar un problema observable y medible;
4. definir objetivo, contrato, no-objetivos y criterios de cierre;
5. abrir rama funcional únicamente cuando exista evidencia suficiente.

Hasta entonces, el estado correcto es: **v5.22 cerrada; sin release funcional activa.**

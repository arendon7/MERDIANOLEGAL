# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**v5.29.0 — funnel observable y confianza contextual: activa.**

Baseline funcional certificada:

`main = stable = 92edb1aac33ed83cbab49175f212546941dfaa5d` (v5.28.0).

## Problema observable

v5.28 cerró la compresión de la ruta de conversión, pero quedaron dos brechas:

- la telemetría v5.0, medición v5.3 y observabilidad de handoff v5.18 existen como capas separadas y no permiten leer un funnel semántico único;
- la autoridad profesional v5.25 es verificable, pero queda lejos del punto inmediatamente anterior a `#contacto` para quien ya recorrió honorarios y contratación.

## Contrato v5.29

1. Unificar el funnel observable en siete etapas: `awareness → need → offer → evidence → decision → contact → handoff`.
2. Mantener la cola v5.29 únicamente en memoria y limitada a 48 eventos.
3. No leer valores del formulario, no introducir PII, persistencia, identificador cross-session, fingerprinting ni transporte de red propio.
4. Reutilizar `MeridianoTelemetry` sin activar el proveedor público, que continúa deshabilitado.
5. Instrumentar checkpoints de exposición en portada y reconocer las 16 fichas profundas mediante su `data-catalog-id`.
6. No llamar “conversión” a un hecho que el navegador no conoce: envío, entrega, lectura, propuesta aceptada, encargo iniciado y cliente convertido permanecen `unknown`.
7. Insertar un `<aside>` compacto de confianza entre `#contratacion` y `#contacto`, derivado exclusivamente de `professional-authority-v525.json`.
8. Preservar la invariante v5.28: `#contacto` sigue siendo la siguiente `<section>` después de `#contratacion`; el nuevo bloque es contextual, no una nueva sección narrativa.
9. Mantener intactos el único formulario físico, privacidad, calificación, propuesta, límites y WhatsApp manual.
10. Ejecutar v5.29 al final de la extensión canónica `v5.18+`, después de v5.28, conservando exactamente 30 pasos.
11. Añadir validator y E2E específicos y mantener todos los gates históricos, axe, Lighthouse, Pages y Release Governance.

## Fuentes y archivos del ciclo

- `funnel-contract-v529.json`: taxonomía, privacidad y límites semánticos.
- `funnel-observability-v529.js`: agregador de eventos y checkpoints en memoria.
- `funnel-trust-v529.css`: presentación compacta de confianza.
- `scripts/apply_funnel_trust_v529.py`: compositor final.
- `scripts/validate_funnel_trust_v529.py`: contrato estático.
- `tests/e2e/funnel-trust-v529.spec.mjs`: comportamiento real.
- `knowledge/10_DECISIONES/ADR-003-funnel-trust-v529.md`: decisión de arquitectura.

## No objetivos

No habilitar Google Analytics, CRM, backend, cookies, píxeles, persistencia local, identificación de usuario, scoring automático, atribución de clientes, testimonios, resultados, aceptación de propuesta o inicio automático del encargo.

## Cierre requerido

Composición v5.29, idempotencia, 16 fichas instrumentadas, validators históricos, Release Governance, Pages/smoke, Browser E2E/axe, Lighthouse, promoción de `stable` y regeneración de Graphify deben quedar verdes antes de declarar la release cerrada.

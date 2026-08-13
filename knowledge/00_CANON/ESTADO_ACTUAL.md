# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-13.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot público certificado: `stable`.
- Release funcional certificada y cerrada: **5.23.0 — compresión del contacto comercial**.
- SHA funcional: `8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`.
- Run final: `31730632791`.
- Snapshot público: `stable = 8d749ab286e8ecbec4d4bd7a083b03dc2b47e5ca`.
- Cierre documental principal: `main = 6a468a16f3a9590eab49c67e6796635aaf474fe7` antes de este cierre final.
- No existe una release funcional posterior activa.

`version.json` conserva el channel técnico `github-pages-public-contact-compression-candidate`. No se renombra durante un cierre exclusivamente documental porque esa entrada dispara builder/Pages. El estado certificado lo determinan los gates, `stable` y esta memoria.

## Qué dejó v5.23

El formulario conserva los mismos campos y la misma lógica comercial, pero reduce superficies visibles:

1. datos de contacto y necesidad;
2. momento, horizonte y presupuesto opcional;
3. una única síntesis dinámica con v5.9/v5.13/v5.14/v5.15;
4. un único disclosure con v5.10/v5.11;
5. contexto general, privacidad y CTA;
6. handoff manual v5.17/v5.18.

La síntesis final es `div[role="region"]`. Una intención explícita `proposal` puede abrir el disclosure; orientación/alcance permanecen colapsados. No hay scoring, inferencia, storage, PII nueva ni transporte automático.

## Evidencia certificada

Run `31730632791`:

- builder + segunda pasada/idempotencia: PASS;
- validadores históricos + v5.23: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: **58 observados → 56 PASS / 2 SKIP / 0 FAIL / 0 RETRY**;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas;
- Lighthouse: **6/6 PASS**;
- Home: performance 1.00, accesibilidad 1.00, LCP 1304 ms, CLS 0, TBT 11 ms;
- CI hasta `stable`: 264 s frente a baseline 279 s;
- cobertura reducida: no;
- budgets relajados: no;
- promoción de `stable`: PASS.

Artefactos: Pages `9193089702`; Lighthouse `9193157108`; CI `9193218997`; release-health `9193219605`. Digests completos: `RELEASE-v5.23.md`.

## Incidencias cerradas

- compatibilidad version-aware v4.9/v5.10 para controles existentes con serialización no literal;
- corrección raíz v4.5: wrapper v5.23 como `DIV`, evitando truncado de `#contacto`;
- E2E de integridad protege `DIV + message + privacy + submit`;
- accesibilidad version-aware exige un disclosure único v5.23 con v5.10/v5.11 completos y target ≥44 px;
- cuatro fallos reales de contraste axe corregidos, sin exclusiones;
- builder y Release Governance vigilan directamente los tres scripts v5.23 y existe un gate nominal de validación final.

## Invariantes

- static-first;
- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- piso v5.23: 58 tests observados, 7 superficies axe y 6 Lighthouse;
- budgets v5.5 intactos;
- telemetría sin PII;
- WhatsApp manual;
- analítica externa apagada (`provider:none`);
- portal real deshabilitado;
- sin CRM/backend, storage servidor, autenticación real, firma, pagos, agenda o carga documental ficticios;
- sin claims no verificables;
- `stable` solo se mueve tras gates verdes.

## Graphify

Después del PR documental #100, Graphify 0.9.26 procesó exactamente `main = 6a468a16f3a9590eab49c67e6796635aaf474fe7` y registró 675 nodos, 1.126 relaciones y 96 notas. La memoria derivada estaba fresca antes de este cierre final; el último commit documental debe volver a actualizar `source_commit` sin mover `stable`.

## Trazabilidad

PRs principales v5.23: #92, #93, #95, #97, #98 y #99. PR #100: release note, README y memoria de cierre. Detalle completo en `RELEASE-v5.23.md`.

## Estado del ciclo

**v5.23 está implementada, desplegada, certificada, documentada y formalmente cerrada. No existe una v5.24 activa ni una tarea funcional abierta.**

Cualquier ciclo posterior debe empezar con auditoría independiente, problema observable, objetivo, contrato, no-objetivos y criterios de cierre.

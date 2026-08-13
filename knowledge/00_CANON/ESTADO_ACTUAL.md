# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-13.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release funcional certificada: **5.24.0 — orquestación canónica verificable**.
- SHA funcional: `73ba88fda16545cc3a257594b2a91d67a9c848b6`.
- Run final: `31739813251`.
- Snapshot certificado: `stable = 73ba88fda16545cc3a257594b2a91d67a9c848b6`.
- No existe una release funcional posterior activa.

## Qué dejó v5.24

v5.24 incorpora `scripts/canonical_pipeline_v524.py` como manifiesto explícito de 30 pasos y exige que las dos rutas de composición existentes ejecuten exactamente los mismos comandos y en el mismo orden.

Contrato:

`builder == segunda pasada == manifiesto`

El guard se integra en la cadena canónica ya existente. Los scripts históricos permanecen, no se redujo cobertura y no se relajaron budgets.

No hubo rediseño intencional ni cambio de productos, servicios, precios, firma, formulario o capacidades externas. La release es un hardening de reproducibilidad y mantenimiento.

## Evidencia certificada

Run `31739813251`:

- builder y manifiesto de 30 pasos: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: **58 observados → 56 PASS / 2 SKIP / 0 FAIL / 0 RETRY**;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas;
- Lighthouse: **6/6 PASS**, performance 1.00 y accesibilidad 1.00 en las seis superficies;
- Home: LCP 1421 ms, CLS 0, TBT 42 ms;
- CI hasta `stable`: 196 s frente a baseline 279 s, mejora 29.7%;
- cobertura reducida: no;
- budgets relajados: no;
- promoción de `stable`: PASS.

Artefactos: Pages `9196603570`; Lighthouse `9196671033`; CI `9196701543`; release-health `9196701995`. Digests completos en `RELEASE-v5.24.md`.

## Incidencias cerradas

- el parser inicial del manifiesto solo reconocía comandos YAML multiline; se corrigió para normalizar formas inline y multiline sin cambiar las rutas reales;
- el canal inicial no se identificaba como superficie pública; el validator de producción bloqueó correctamente y la metadata se corrigió antes de recertificar desde cero;
- ningún validator histórico se debilitó para resolver estas incidencias.

## Invariantes

- static-first;
- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- piso de cobertura: 58 tests observados, 7 superficies axe y 6 Lighthouse;
- budgets v5.5 intactos;
- telemetría sin PII;
- WhatsApp manual;
- analítica externa apagada;
- portal real deshabilitado;
- sin CRM/backend, storage servidor, autenticación real, firma, pagos, agenda o carga documental ficticios;
- sin claims no verificables;
- `stable` solo se mueve tras gates verdes;
- el orden canónico debe permanecer explícito y verificable.

## Graphify

Al cierre funcional Graphify 0.9.26 ya reconoce v5.24 con 685 nodos, 1.147 relaciones, 96 notas, 76 scripts Python, 25 fuentes JavaScript y 9 specs E2E. El cierre documental debe producir una corrida cuyo `source_commit` coincida exactamente con el `main` documental definitivo, sin mover `stable`.

## Trazabilidad

PR #102: orquestación canónica verificable. PR #103: corrección de metadata del canal. Builder final `31739786763`; certificación final `31739813251`. Detalle completo en `RELEASE-v5.24.md`.

## Estado del ciclo

**v5.24 está implementada, desplegada y funcionalmente certificada. El cierre documental/Graphify está en curso. No existe una v5.25 activa.**

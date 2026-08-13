# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-13.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release certificada y cerrada: **5.24.0 — orquestación canónica verificable**.
- SHA funcional: `73ba88fda16545cc3a257594b2a91d67a9c848b6`.
- Run final: `31739813251`.
- `stable = 73ba88fda16545cc3a257594b2a91d67a9c848b6`.

## Contrato v5.24

`scripts/canonical_pipeline_v524.py` declara 30 pasos únicos y verifica que las dos rutas de composición ejecuten los mismos comandos en el mismo orden:

`builder == segunda pasada == manifiesto`

No hubo rediseño funcional intencional. Los contratos previos permanecen vigentes y no se redujo cobertura ni se relajaron budgets.

## Evidencia

- segunda pasada/idempotencia: PASS;
- validadores históricos: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 58 observados → 56 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS, performance 1.00 y accesibilidad 1.00;
- Home: LCP 1421 ms, CLS 0, TBT 42 ms;
- CI hasta `stable`: 196 s, 29.7% mejor que el baseline de 279 s;
- promoción de `stable`: PASS.

Artefactos y digests: `RELEASE-v5.24.md`.

## Invariantes

- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 58 tests observados, 7 superficies axe y 6 Lighthouse como piso certificado;
- WhatsApp manual y telemetría local sin PII;
- portal real deshabilitado;
- `stable` solo se mueve tras gates verdes;
- el orden canónico debe permanecer explícito y verificable.

## Graphify

Graphify 0.9.26 registra v5.24 con 685 nodos, 1.147 relaciones, 96 notas, 76 scripts Python, 25 fuentes JavaScript y 9 specs E2E. La frescura se comprueba comparando `BUILD_META.source_commit` con el último `main` procesado exitosamente. Los commits exclusivamente documentales no mueven `stable`.

## Trazabilidad

PR #102: orquestación. PR #103: metadata de canal. PR #104: documentación de cierre. Detalle completo en `RELEASE-v5.24.md`.

## Estado del ciclo

**v5.24 está implementada, desplegada, certificada, documentada y formalmente cerrada. No existe una v5.25 activa ni una tarea funcional abierta.**

Cualquier ciclo posterior debe comenzar con una auditoría independiente.

# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release certificada y cerrada: **5.25.0 — autoridad profesional verificable**.
- SHA funcional: `b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`.
- Builder autoritativo: `31772373318`.
- Run público final: `31772394136`.
- `stable = b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`.

## Contrato v5.25

`professional-authority-v525.json` es la fuente de verdad de la capa profesional publicada. La portada incorpora prueba profesional breve y `firma.html#trayectoria` materializa formación, cinco entradas cronológicas y cuatro grupos de asuntos representativos.

Las organizaciones citadas corresponden a trayectoria del director, no a una lista de clientes de Meridiano Legal. No se publican testimonios inventados, logos como social proof, métricas de éxito, garantías de resultado ni claims de liderazgo no sustentados. UNIR se mantiene como formación de posgrado y el centro demo continúa ficticio/noindex.

El compositor se integra dentro del paso v5.18+; el manifiesto protegido v5.24 continúa con 30 pasos. Builder y Release Governance vigilan explícitamente JSON, CSS, compositor y validator v5.25. Release Governance ejecuta además `Validate professional authority v5.25`.

## Evidencia

- builder canónico de 30 pasos: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos y v5.25: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 64 observados → 62 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- Home: performance 1.00, accesibilidad 1.00, LCP 1387 ms, CLS 0, TBT 72 ms;
- CI hasta `stable`: 240 s, 14.0% mejor que el baseline de 279 s;
- cobertura reducida: no;
- budgets relajados: no;
- promoción de `stable`: PASS.

Artefactos, digests e incidencias: `RELEASE-v5.25.md`.

## Invariantes

- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 64 tests observados, 7 superficies axe y 6 Lighthouse como piso certificado;
- 30 pasos del pipeline canónico, con `builder == segunda pasada == manifiesto`;
- WhatsApp manual y telemetría local sin PII;
- portal real deshabilitado;
- demo explícitamente ficticia;
- `stable` solo se mueve tras gates verdes;
- ningún hecho profesional nuevo debe publicarse fuera de la fuente v5.25 sin actualizar su contrato y validación.

## Graphify

Graphify es memoria derivada. Su frescura se comprueba comparando `graphify-out/BUILD_META.json.source_commit` con el último `main` procesado exitosamente. Los commits exclusivamente documentales pueden hacer que `main` avance sin mover `stable`.

## Trazabilidad

PR #106: implementación principal. PR #107: idempotencia. PRs #108–#111: precisión del contrato E2E responsive/accesible. PR #113: hardening de workflows. Detalle completo en `RELEASE-v5.25.md`.

## Estado del ciclo

**v5.25 está implementada, desplegada, certificada y funcionalmente cerrada. No existe una v5.26 activa ni una tarea funcional abierta.**

El cierre documental puede hacer avanzar `main` exclusivamente por memoria/documentación; `stable` debe conservar el SHA funcional certificado. Cualquier ciclo posterior debe comenzar con una auditoría independiente.
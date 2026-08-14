# Meridiano Legal — Tarea activa

Actualizado: 2026-08-14.

## Estado

**No existe una release funcional activa. v5.25.0 está cerrada.**

Snapshot funcional certificado:

`stable = b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`.

## Cierre v5.25

La release de autoridad profesional verificable cumplió su contrato:

- fuente canónica `professional-authority-v525.json`;
- prueba profesional breve en portada;
- `firma.html#trayectoria` con formación, cinco entradas cronológicas y cuatro grupos de asuntos;
- Organization ↔ Person coherente;
- frontera explícita entre trayectoria del director, clientes de Meridiano Legal y experiencia demo;
- UNIR presentada como formación de posgrado, no como título completado;
- demo ficticia/noindex preservada;
- sin testimonios, logos de terceros, métricas de éxito, garantías o claims de liderazgo no sustentados;
- integración dentro del paso v5.18+ sin alterar el manifiesto canónico de 30 pasos;
- vigilancia explícita de los cuatro archivos v5.25 en Builder y Release Governance.

## Gates finales

Run público `31772394136`:

- builder e idempotencia: PASS;
- validadores históricos y v5.25: PASS;
- Pages + smoke: PASS;
- Browser/axe: 64 → 62 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- Lighthouse: 6/6 PASS;
- release-health: PASS;
- cobertura reducida: no;
- budgets relajados: no;
- `stable`: promovida a `b5a23e0ac1b675cade3ad69d197bbf86d5b998d8`.

Detalle y artefactos: `RELEASE-v5.25.md`.

## Siguiente movimiento permitido

No abrir v5.26 por continuidad numérica. El siguiente ciclo solo debe comenzar después de una auditoría nueva que identifique un problema material y verificable.

Los commits exclusivamente documentales pueden avanzar `main` después de este cierre sin mover `stable`. Graphify debe considerarse fresco cuando su `BUILD_META.source_commit` coincida con el último `main` procesado exitosamente.
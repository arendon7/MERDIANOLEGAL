# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release certificada y cerrada: **5.27.0 — densidad comercial móvil**.
- SHA público/canónico certificado: `26c90ec3a0e1ea08ae251673cba0a7fc56b4e0b2`.
- Builder autoritativo: `31813283560`.
- Run público final: `31813319651`.
- `main = stable = 26c90ec3a0e1ea08ae251673cba0a7fc56b4e0b2` al cierre.

## Contrato v5.27

La portada conserva las 8 opciones de servicios, 8 productos, 5 planes, 4 grupos de referencias de honorarios y 8 sectores. En viewport móvil esas colecciones se presentan como decks horizontales contenidos con `scroll-snap`, sin alterar escritorio, sin ocultar opciones y sin generar overflow horizontal global.

La capa está materializada en `integral-v526.css` como extensión responsive v5.27 y protegida por `tests/e2e/mobile-density-v527.spec.mjs`.

## Evidencia

- generación canónica: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: PASS;
- Lighthouse: PASS;
- promoción de `stable`: PASS;
- budgets relajados: no;
- cobertura reducida: no.

## Invariantes

- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- WhatsApp manual y telemetría local sin PII;
- portal real deshabilitado;
- demo explícitamente ficticia;
- `stable` solo se mueve tras gates verdes;
- ningún hecho profesional nuevo debe publicarse fuera de la fuente v5.25 sin actualizar su contrato y validación;
- la densidad móvil no puede resolverse ocultando contenido material.

## Graphify

Graphify es memoria derivada. El snapshot disponible declara v5.27 y `source_commit = 75d18b45d7273ae10a3722617bfc3808350a3f0f`, mientras el `main` canónico certificado terminó en `26c90ec3…`. Hasta la siguiente regeneración, `main` es la autoridad.

## Estado del ciclo

**v5.27 está implementada, desplegada, certificada y funcionalmente cerrada. v5.28 está activa en `TAREA_ACTIVA.md`; `stable` debe permanecer en v5.27 hasta la certificación completa de ese ciclo.**

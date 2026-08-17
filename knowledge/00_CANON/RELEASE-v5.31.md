# Meridiano Legal — Release v5.31

Estado: cerrada funcionalmente; cierre documental sujeto a recertificación del commit de memoria.
Fecha: 2026-08-17.
Versión: `5.31.0`.
Canal objetivo: `github-pages-production-decision-compression-certified`.

## Problema resuelto

La auditoría posterior a v5.30 confirmó que Meridiano Legal ya contaba con suficiente profundidad jurídica y comercial, pero el recorrido público acumulaba demasiadas capas válidas abiertas simultáneamente. La fricción era de jerarquía y carga cognitiva, no de ausencia de contenido.

## Solución

v5.31 introduce divulgación progresiva nativa sin eliminar contenido material:

- 16/16 fichas mantienen dos grupos decisionales abiertos y conservan v5.22 completo bajo `<details>/<summary>` cerrado por defecto;
- 6/6 rutas de necesidad mantienen abierto el recorrido principal y pliegan únicamente objeciones, FAQ, rutas relacionadas y prueba/contexto;
- no se eliminan catálogos, copy jurídico/comercial, perímetro, límites, alternativas, evidencia ni honorarios aprobados;
- no se usa JavaScript de acordeón, carga diferida, `display:none`, `visibility:hidden` ni atributo `hidden` para aparentar menor densidad.

## Implementación

- contrato: `decision-compression-v531.json`;
- estilos: `decision-compression-v531.css`;
- compositor: `scripts/apply_decision_compression_v531.py`;
- validator: `scripts/validate_decision_compression_v531.py`;
- E2E: `tests/e2e/decision-compression-v531.spec.mjs`;
- auditoría: `knowledge/30_RUNBOOKS/AUDIT-RECORRIDO-v5.31.md`;
- decisión: `knowledge/10_DECISIONES/ADR-005-decision-compression-v531.md`.

v5.31 corre después de v5.30 dentro del orquestador existente y conserva exactamente 30 pasos canónicos.

## Evidencia funcional certificada

- SHA funcional: `159be8a9e467a303faa8d302bfac93b33c2e7b29`.
- PRs del ciclo: #137 a #141.
- Builder final #161: `32059316508` — PASS.
- Site Quality and Deploy #383: `32059355395` — PASS.
- Idempotencia / segunda pasada: PASS.
- Validaciones estáticas: 37/37 — PASS.
- GitHub Pages + smoke: PASS.
- Browser E2E/axe: 112 observados · 110 PASS · 2 SKIP · 0 FAIL · 0 reintentos; reporter 194 s.
- Lighthouse: PASS con budgets existentes.
- Promoción de `stable`: PASS.
- Graphify #314: PASS sobre el SHA funcional; 800 nodos, 1.368 relaciones y 106 notas wiki.

## Gates que mejoraron la gobernanza

Durante la certificación, los gates bloquearon correctamente la promoción hasta resolver incompatibilidades históricas:

- #379 detectó que un canal candidate podía degradar erróneamente la portada a “Web demostrativa”; se separó la capability pública del estado de release.
- #380 detectó una contradicción del validator visual histórico; quedó alineado con la verdad de producción: portada pública y componentes demo demostrativos.
- #381 y #382 detectaron supuestos E2E incompatibles con la nueva divulgación progresiva; las pruebas se actualizaron para exigir cerrado por defecto, apertura explícita y conservación posterior del mismo contenido/telemetría, incluida activación por teclado en WebKit.

No se cambió la UX para complacer tests, no se eliminaron pruebas y no se relajaron budgets.

## Invariantes preservadas

- 46 HTML y 16 fichas profundas;
- un único formulario físico canónico;
- WhatsApp manual;
- portal real deshabilitado y demo explícitamente demostrativa/noindex;
- funnel en memoria sin PII ni persistencia;
- no equiparar navegación, contacto o handoff con conversión comercial;
- no clientes, testimonios, resultados ni tarifas inventadas;
- no cotizador/CRM/backend/firma/pagos/agenda/autenticación/carga documental ficticios;
- exactamente 30 pasos canónicos;
- `stable` únicamente después de gates verdes.

## Autoridad del cierre

Este registro fija el SHA funcional certificado, pero no incrusta recursivamente el SHA del commit documental de cierre. El estado final autoritativo debe comprobarse leyendo los refs vigentes y exige simultáneamente:

1. `main == stable`;
2. `version.json.channel == github-pages-production-decision-compression-certified`;
3. Site Quality and Deploy verde sobre el commit documental final;
4. Graphify con `source_commit == main`.

No se abre v5.32 como consecuencia automática de este cierre.

# Meridiano Legal v5.19.0 — foco comercial adaptativo

Fecha: 2026-08-12.

## Objetivo

Reducir carga cognitiva en el tramo final de conversión sin eliminar información jurídica, alterar la decisión del usuario ni introducir scoring, inferencias o integraciones nuevas.

## Alcance

v5.19 extiende el progressive disclosure ya existente sobre los bloques secundarios de cierre y contratación:

- `orientation` y `scope`: el detalle secundario inicia replegado;
- `proposal` explícito en escritorio: el detalle inicia expandido;
- móvil conserva el comportamiento v5.16;
- el material permanece disponible mediante `<details>` nativo y accesible;
- abrir o cerrar detalle no cambia etapa, modalidad, recomendación ni handoff.

La capa reutiliza únicamente `commercial_intent`, un dato explícito que ya forma parte de las rutas comerciales anteriores. No crea un perfil ni deduce intención distinta de la declarada por el usuario.

## Contratos y privacidad

v5.19 mantiene:

- `scoring: false`;
- sin cambio automático de `decision_stage`;
- sin PII nueva;
- sin `localStorage` o `sessionStorage` nuevo;
- sin `fetch`, XHR o `sendBeacon` nuevo;
- sin backend o CRM;
- sin supresión de contenido material;
- sin reducción de cobertura ni relajación de budgets.

El runtime sigue siendo `decision-action-v515.js`; v5.19 añade allí el bloque auditable `COMMERCIAL-FOCUS-V519` y conserva el punto de entrada contractual v5.16 mediante alias real, en vez de romper validadores históricos.

## Incidencia detectada durante certificación

El primer Release Governance de la candidata bloqueó correctamente el cambio porque el validator histórico v5.5 esperaba el símbolo contractual `enhanceMobileDisclosureV516`.

No se relajó el gate. La implementación se corrigió preservando ese punto de entrada y delegándolo a la función ampliada v5.19. El segundo Release Governance pasó todos los contratos históricos y la nueva extensión.

## Evidencia funcional certificada

PR funcional: #71.

Merge fuente: `fcf8d868e5b95ab201c8ebb612ffba166f4746f5`.

SHA público materializado y promovido a `stable`: `9a91e8d19697142c0d2d0990c1e606f6ff9660ef`.

Run final Pages/certificación: `31649425600`.

- `main == stable == 9a91e8d19697142c0d2d0990c1e606f6ff9660ef` al cierre funcional;
- builder e idempotencia: PASS;
- validadores históricos + hardening v5.19: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- reporter Browser: 85 s;
- 7 superficies axe sin violaciones serias/críticas;
- Lighthouse: 6/6 PASS;
- accesibilidad Lighthouse: 1.00 en las seis superficies;
- performance: 1.00 en portada, solución IA, producto IA y demo; 0.98 en sector tecnología y perspectiva IA;
- LCP máximo observado: 1368 ms;
- CLS máximo observado: 0.087;
- TBT máximo observado: 56 ms;
- `accessibilityAuditGaps`: vacío;
- CI hasta `stable`: 215 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 22.9%;
- cobertura reducida: no;
- budgets relajados: no.

Artefactos del run `31649425600`:

- Lighthouse `9162048825`, digest `sha256:82bec745b16796e574f516b22de27d023c258a5ab1b827075eeb80a3da35670e`;
- CI `9162074790`, digest `sha256:4ed4f8c2d330354fababe3389e3542974f0427a55230df6f0e9bd8b57128a7bb`;
- release-health `9162075114`, digest `sha256:681f567ade20a27df2df8ad1645cda53d68260d127e5d43a90700c85bdc1c0d1`.

## Contratos preservados

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- 37 entradas E2E;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- WhatsApp como handoff manual;
- telemetría sin PII;
- analítica externa desactivada;
- `stable` solo después de gates verdes.

## Graphify / procedencia

Graphify se regenera desde `main` y debe conservar como `source_commit` el commit realmente procesado. El snapshot observado antes de este cierre documental reporta versión `5.19.0` sobre el merge fuente `fcf8d868e5b95ab201c8ebb612ffba166f4746f5`; el commit posterior `9a91e8d…` corresponde a materialización canónica del builder.

No se fija como regla permanente un SHA de Graphify que pueda quedar obsoleto al regenerarse. La verificación correcta es comparar `BUILD_META.json` con el último run exitoso de Graphify.

## Estado

v5.19.0 queda funcionalmente certificada. Este documento formaliza el cierre; no abre v5.20 ni modifica retrospectivamente el contrato certificado.

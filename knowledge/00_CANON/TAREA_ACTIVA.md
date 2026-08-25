# Meridiano Legal — Tarea activa

Actualizado: 2026-08-25.

## Baseline certificado

- Repositorio: `arendon7/MERDIANOLEGAL`.
- `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
- Release productiva: **v7.4.0 — Commercial Evidence Readiness**.
- Analytics: `readiness-disabled`.
- Capability truth v7.4 permanece vigente mientras v8 está en candidate.
- `stable` no se modifica manualmente.

## Programa v8 — estado acumulado

### W4.1 — Client Architecture & Taxonomy

PR draft #183.

- taxonomía `Prácticas / Soluciones / Servicios continuos`;
- matriz 46/46;
- 6 prácticas;
- 8 soluciones;
- Dirección Jurídica Externa como servicio continuo;
- RC02 Meridiano Contratos bloqueado hasta capability contract verificable.

### W4.2 — Route Compatibility & SEO Contract

PR draft #184.

- route contract estructurado;
- 46/46 legacy routes;
- 43/43 sitemap baseline;
- canonical/alias/sitemap policy;
- CI run `32904478022`: **PASS**.

### W4.3 — Renderer & Design-System Pilot Infrastructure

PR draft #185.

- experience model source-driven;
- renderer no destructivo;
- design system v8 consolidado;
- truth parity;
- no-activation gate;
- CI run `32904520736`: **PASS**.

### W4.4 — Ephemeral Pilot Materialization

PR draft #186.

Pilotos:

1. SO07 `/soluciones/sistema-contractual-empresarial.html`.
2. PR02 `/practicas/corporativo-societario-gobierno.html`.
3. RC01 `/servicios-continuos/direccion-juridica-externa.html`.

Resultado definitivo:

- 46 legacy antes del materializado: PASS;
- materialización efímera: PASS;
- topología temporal 49 = 46 + 3: PASS;
- legacy pilots sin reescritura: PASS;
- contraste determinista WCAG AA: PASS;
- Chromium desktop: PASS;
- Chromium mobile: PASS;
- WebKit desktop: PASS;
- axe WCAG 2.1 A/AA serious/critical: PASS;
- run final `32905639585`, job `97989006324`: **success**.

La incidencia previa de contraste se corrigió en el sistema de tokens, sin rebajar axe:

- `--ml-muted` → `#52606a`;
- `--ml-gold-ink` → `#765b38` para texto dorado;
- `--ml-gold` se conserva para acento no textual;
- `validate_v8_contrast_tokens.py` impide regresión.

## Frente vigente

**W4.5 — v8 Public-Tree Candidate.**

Objetivo: persistir exactamente los tres targets ya certificados por W4.4 como páginas `noindex`, manteniendo el sitio productivo v7.4 sin handoff canónico.

### Estrategia de bootstrap reproducible

No se copiará HTML manualmente desde conversación ni se recreará fuera del renderer.

1. crear branch W4.5 sobre W4.4;
2. CI genera los tres targets desde `render_v8_pilot.py` + fuentes canónicas en un checkout temporal;
3. CI publica un artefacto con los tres HTML exactos;
4. esos bytes se incorporan al branch W4.5;
5. un segundo run vuelve a renderizar y exige byte parity con los tres archivos persistidos;
6. después ejecuta validación estructural + Browser/Axe sobre el árbol persistente.

## Invariantes W4.5

Durante esta wave:

- los tres targets permanecen `noindex,follow`;
- no se añaden al sitemap;
- Home/navigation no los enlaza todavía;
- los 46 legacy permanecen físicamente presentes;
- los legacy conservan self-canonical;
- no se cambia `version.json`;
- no se integra aún v8 al Builder/Pages productivo;
- no se cambia robots productivo;
- no se crea otro formulario;
- no se activa analytics;
- RC02 Meridiano Contratos sigue `publishable=false`;
- `stable` permanece intacta.

## Crítica visual abierta

Screenshots reales W4.4 muestran una mejora de polish no bloqueante:

- en mobile, el summary `Profundidad jurídica y operativa / Ver alcance completo` tiene demasiado peso visual.

Se tratará después de asegurar byte parity y Public-Tree Candidate, sin esconder profundidad material ni romper `<details>` nativo.

## Definition of Done W4.5

- tres target HTML persistidos;
- generated == persisted byte-for-byte;
- 49 HTML en candidate = 46 legacy + 3 targets;
- targets `noindex` y fuera del sitemap;
- legacy canonical intacto;
- Home/navigation sin activación v8;
- route contract y truth parity PASS;
- Chromium desktop/mobile + WebKit + axe PASS sobre archivos persistidos;
- no cambio en `stable`;
- handoff preparado para W4.6, sin activarlo.

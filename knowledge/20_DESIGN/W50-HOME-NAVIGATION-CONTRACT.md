# W5.0 — Home + Navigation Expansion Contract

Status: IMPLEMENTATION CONTRACT
Base release: `619d11ce829ce251f02314a96201f5d0e7eb120e`
Branch: `design/v8-expansion-w50`

## 1. Objective

Move Meridiano from the additive v8 pilot state to a coherent v8 public shell by redesigning the Home and global navigation before activating any individual v8 offer route.

W5.0 is deliberately shell-first. The three deployed v8 pilot surfaces remain `noindex,follow` and outside public discovery until Home/navigation, route taxonomy and activation gates are ready together.

## 2. Product thesis

Meridiano must read as a contemporary business law firm built around legal judgment, business understanding and technology-enabled execution.

The public architecture must teach three different ways of engaging the firm:

1. **Prácticas** — expertise and legal capability.
2. **Soluciones** — structured projects with defined outcomes and deliverables.
3. **Servicios continuos** — recurring operating relationships: Dirección Jurídica Externa and Meridiano Contratos.

LegalAIZ remains infrastructure/Legal Intelligence, not the primary public brand.

## 3. Current-state problems to remove

The current Home is strong but still carries accumulated v3/v4/v5/v6 layers and historical taxonomy. W5.0 must remove the following user-facing ambiguities without weakening the certified legacy truth:

- navigation mixes situation-led and catalogue-led labels (`Cómo podemos ayudar`, `Soluciones`, `Oferta completa`);
- public taxonomy does not yet expose the canonical distinction practice / solution / recurring service;
- Home does not yet present Meridiano Contratos as a central recurring capability;
- Dirección Jurídica Externa must remain framed by coverage, complexity, priority and service level, never a public bag of hours;
- the public shell does not yet provide the canonical v8 navigation structure;
- accumulated CSS/JS layers must not be copied into the new v8 shell as another override stack.

## 4. Canonical global navigation

Desktop primary navigation:

- Qué hacemos
- Sectores
- Firma
- Insights
- Contacto

Primary action:

- Hablar con Meridiano

Secondary/utility actions:

- Solicitar diagnóstico
- Portal clientes (discreet, only where the real destination/capability is verified)

### Qué hacemos mega-menu

Three semantic groups only:

**Prácticas**
- Corporativo, Societario y Gobierno
- Contratación y Negocios
- Regulación, Infraestructura y Proyectos
- Tecnología, Datos e Inteligencia Artificial
- Propiedad Intelectual y Activos Intangibles
- Legal Operations y Transformación Jurídica

**Soluciones**
- Diagnóstico Jurídico Empresarial
- Empresa Jurídicamente Organizada
- Sistema Contractual Empresarial
- Empresa Lista para Inversión
- Sistema de Protección de Activos Intangibles
- Programa de Gobernanza de Inteligencia Artificial
- Programa de Cumplimiento Digital
- Proyecto Regulado Estructurado

**Servicios continuos**
- Dirección Jurídica Externa
- Meridiano Contratos

No top-level menu item for Products, Plans, Documents or LegalAIZ.

## 5. Home narrative — canonical order

### H01 — Hero
Eyebrow: `FIRMA JURÍDICA EMPRESARIAL`

Target headline:

> Derecho empresarial para decisiones que necesitan avanzar.

Support copy must communicate legal judgment + business + technology without generic AI/startup language.

Primary CTA: `Hablar con Meridiano`
Secondary CTA: `Explorar soluciones →`

Visual language: structural M / legal-operating diagram, not court imagery or generic stock legal photography.

### H02 — Situation-led entry
Headline concept:

> Empiece por lo que está pasando en su empresa.

Six canonical problem routes:
- Mi empresa creció y jurídicamente está desorganizada.
- Necesito controlar mejor nuestros contratos.
- Estamos preparando inversión.
- Tenemos un proyecto regulado.
- Estamos utilizando IA.
- Necesitamos apoyo jurídico permanente.

These are discovery prompts, not separate competing product taxonomies.

### H03 — Featured solutions
Prioritize structured outcomes, not a flat catalogue.

Initial editorial emphasis:
- Diagnóstico Jurídico Empresarial
- Sistema Contractual Empresarial
- Empresa Lista para Inversión
- Proyecto Regulado Estructurado

All eight solutions remain reachable through the solutions hub.

### H04 — Meridiano Contratos
This is mandatory and central.

Core message:

> Configure sus contratos con Meridiano y genérelos después desde su biblioteca jurídica, sobre modelos versionados y mantenidos jurídicamente.

Explain the operating loop:

`configurar → parametrizar → generar → registrar → actualizar → escalar excepciones`

Clarify that updates apply to master models for future generation; executed agreements do not change automatically.

Do not present this as generic template software or unrestricted automated legal advice.

### H05 — Practices
Editorial numbered list, not card grid.

Six canonical practices.

### H06 — Method
Dark section.

Canonical conceptual method:

`Entender → Estructurar → Ejecutar → Controlar`

Individual solution methodologies may differ deeper in the site.

### H07 — Experience / evidence
Use anonymized/verifiable case structures only.
No fabricated metrics.

### H08 — Dirección Jurídica Externa
Position as an integrated recurring legal function.

Public commercial dimensions:
- coverage;
- complexity;
- priority;
- SLA / service level;
- governance and reporting.

Forbidden public commercial framing:
- bolsa de horas;
- X horas al mes;
- hourly retainer as the principal value proposition.

### H09 — Sectors
Canonical visible clusters:
- Empresas y grupos empresariales
- Tecnología y economía digital
- Servicios públicos e infraestructura
- Ambiente, residuos y economía circular
- Salud y ciencias de la vida
- Startups e inversión

Existing deeper sector authority may remain as subsectors/experience without overloading the Home.

### H10 — Legal Intelligence
Subtle technology layer.
Meridiano is the public brand; LegalAIZ may be referenced only as supporting infrastructure where truth and capability permit.

### H11 — Insights
Featured editorial content with contextual internal links.

### H12 — Final CTA
Primary: `Hablar con Meridiano`
Secondary where appropriate: `Solicitar diagnóstico`

## 6. Mobile behavior

Mobile is not a stacked desktop clone.

Required sequence:
- compact header;
- hero;
- situations;
- featured solutions;
- Meridiano Contratos;
- practices accordion/list;
- method;
- Dirección Jurídica Externa;
- evidence;
- sectors;
- Legal Intelligence;
- insights;
- final CTA.

Sticky CTA permitted after hero; must disappear while a form/menu is active and near the final CTA.

Minimum interactive target: 44px.
No horizontal overflow.
Respect `prefers-reduced-motion`.

## 7. Design-system boundary

W5.0 must use `assets/css/v8/*` and semantic v8 primitives. It must not add a new numbered historical CSS patch layer.

Target v8 shell should consolidate rather than inherit the full historical Home stylesheet stack.

No new component may be introduced unless:
1. an existing v8 primitive cannot express the requirement;
2. its mobile behavior is defined;
3. keyboard/focus behavior is defined where interactive;
4. it is reusable or strategically necessary.

## 8. SEO and activation boundary

During W5.0 candidate work:
- current production Home canonical remains unchanged until the candidate is certified;
- the three additive v8 routes remain `noindex,follow`;
- they remain outside sitemap until activation wave;
- legacy route canonical handoff is not performed in W5.0;
- no public version bump merely for visual implementation.

Activation requires a separate gate proving Home/navigation and intended target destinations are all physically available and valid.

## 9. Analytics contract

Use normalized event names rather than per-button event proliferation:
- `cta_click`
- `solution_view`
- `practice_view`
- `diagnosis_start`
- `contact_submit`
- `portal_click`

Properties may identify source/page/solution/CTA type. No PII in analytics payloads.

## 10. Accessibility / performance acceptance

Mandatory:
- WCAG 2.1 AA for production surfaces;
- visible keyboard focus;
- semantic headings and landmarks;
- accessible mega-menu/mobile navigation;
- reduced motion support;
- images and decorative M treatment do not carry sole semantic meaning;
- no small-text use of non-AA brand gold;
- no layout shift introduced by navigation/hero assets.

Target budgets remain governed by existing production Lighthouse gates; W5.0 may not weaken them.

## 11. Implementation sequence

### W5.0A — Home experience model
Create a source-driven Home model that references canonical offer/practice contracts rather than duplicating legal scope.

### W5.0B — Global navigation shell
Implement Header, MegaMenu, MobileMenu and Footer using v8 primitives.

### W5.0C — Home renderer
Render Home from the v8 model into an ephemeral candidate first.

### W5.0D — Browser candidate
Desktop Chromium + mobile Chromium + WebKit + axe + keyboard + overflow + link-integrity.

### W5.0E — Persisted Home candidate
Only after browser PASS; maintain SEO/activation boundary until the coordinated activation wave.

## 12. W5.0 exit criteria

W5.0 is complete only when:
- Home v8 source model is deterministic and source-driven;
- global navigation expresses the canonical taxonomy;
- Meridiano Contratos has a central Home surface;
- Dirección Jurídica Externa has no hourly-bag framing;
- Home desktop/mobile pass browser, axe, keyboard and overflow checks;
- all visible navigation destinations return valid local targets or use an explicit legacy fallback;
- Builder remains idempotent;
- Pages Quality remains green;
- production is not modified from this branch.

## 13. Explicit non-goals

W5.0 does not yet:
- activate all v8 SEO routes;
- redirect all legacy URLs;
- implement the interactive diagnostic;
- migrate every sector/insight page;
- expose a client portal destination unless the real private capability/destination is verified;
- change executed-contract semantics of Meridiano Contratos;
- sell Dirección Jurídica Externa by hours.

The objective is to establish the coherent public v8 shell from which the remaining propagation can proceed safely.
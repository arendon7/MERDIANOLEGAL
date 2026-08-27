# W5.0E — Persisted Home Candidate

Status: **candidate / non-public**.

## Objective

Certify the exact HTML, CSS and JavaScript that can replace the current root `index.html` in a later E2 commit, without changing production during E1.

## SEO boundary

The future Home is indexable and canonical to the repository root, but it **does not hand off internal links to the three noindex v8 pilots yet**. PR02, SO07 and RC01 retain their certified legacy/indexable URLs until a coordinated route/indexing/sitemap wave. RC02 Meridiano Contratos remains an owner-confirmed capability without a public route.

## Runtime boundary

The future Home loads only:

1. the four canonical v8 design-system styles;
2. one candidate-only Home/contact stylesheet;
3. `runtime-config.js`;
4. the privacy-preserving v6.1 analytics adapter;
5. a v8 stage-only measurement adapter;
6. v8 navigation;
7. v8 contact/handoff.

It does not load the historical v3-v6 visual/commercial JS/CSS stack.

## Contact contract

There is exactly one intake form. It collects only first-contact context, never silently sends it to a backend, never uses local/session storage or cookies, and only prepares a WhatsApp handoff after explicit submit. The user must confirm sending in WhatsApp. A prepared draft is invalidated if the form changes, preventing stale handoff content.

Measurement receives stage names only; no field content, email, name, company, message, budget or handoff text is exported.

## E1 gate

GitHub Actions renders `.w5-persisted/index.html` in a disposable checkout and runs:

- fail-closed static contract validation;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- WCAG 2.1 A/AA axe serious/critical gate;
- keyboard/menu behavior;
- no horizontal overflow;
- explicit WhatsApp-only handoff behavior;
- stale-draft protection;
- zero persistent browser storage;
- no external network request while analytics is disabled;
- final `git diff --exit-code` proving `index.html` was not changed.

Only after E1 is green may E2 replace root `index.html` and adapt historical Builder/validators through a strict projection.

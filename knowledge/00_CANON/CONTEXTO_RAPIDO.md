# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente. `ESTADO_ACTUAL.md` y `TAREA_ACTIVA.md` mandan si existe cualquier diferencia.

## Proyecto

Sitio público y centro demostrativo de Meridiano Legal. Arquitectura static-first publicada en GitHub Pages, con 46 páginas HTML, 16 fichas profundas y un único formulario físico canónico.

## Estado funcional

- Release funcional certificada: **6.3.0 — Engagement Clarity / claridad precontratación**.
- SHA funcional certificado: `118cee5030f27689d91172beb525d7d92c751117`.
- Canal de cierre: `github-pages-production-engagement-clarity-certified`.
- 16/16 fichas profundas muestran `requirements` y `responsibilities` derivados exactamente de sus catálogos canónicos.
- Cada ficha tiene un único hito `Para empezar` y una única sección `#v6-engagement` antes de Límites.
- Navegación ejecutiva v6.3: exactamente 7 hitos.
- Browser E2E + axe: PASS antes de la promoción automática de `stable`.
- Lighthouse post-deploy: PASS con budgets existentes antes de la promoción automática de `stable`.
- 46/46 HTML, 16/16 fichas, 1/1 formulario físico y 30/30 pasos históricos preservados.
- Search Console permanece sin configurar: no hay token auténtico y runtime publica `searchConsoleConfigured=false`.
- Analítica externa permanece deshabilitada: `analytics.enabled=false`, `provider=none`, `site_id=""`.
- Discovery v6.2 permanece íntegro: 43 indexables + 3 `noindex`, sitemap canónico de 43 URLs.
- Portal real deshabilitado; WhatsApp continúa como handoff manual.
- Para la referencia documental definitiva, verificar `main` y `stable`; deben coincidir después del cierre documental.

## Qué cambió en v6.3

v6.3 hace visible información precontractual que ya existía en los catálogos jurídicos de productos y servicios, pero estaba relegada a la profundidad histórica de las fichas.

- `requirements` se presenta como **Qué debe estar listo del lado del cliente**.
- `responsibilities` se presenta como **Cómo se distribuyen las responsabilidades**.
- La información no se reescribe: el validator compara fila por fila la representación pública contra `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.
- La nueva sección se integra entre Proceso y Límites.
- El objetivo es reducir ambigüedad antes de solicitar una propuesta, no crear nuevas obligaciones desde la capa de presentación.

## Release engineering v6.3

- Contrato: `assets/data/v6/engagement-clarity-v63.json`.
- Materializador: `scripts/apply_engagement_clarity_v63.py` con `--check` fail-closed.
- Validator: `scripts/validate_engagement_clarity_v63.py` contra los 16 catálogos canónicos.
- Integración: `normalize_experience_compat_v60.py`; no existe paso histórico 31.
- Gate v6.3 phase-aware: baseline 0/16 exige materializar exactamente 16; baseline 16/16 exige drift cero; cualquier estado parcial falla.
- Canonical Equivalence exige `measurement ∪ release ∪ discovery ∪ engagement` cuando aplica.
- v4.6 mantiene 6 hitos en baselines sin v6.3 y exactamente 7 cuando Engagement Clarity está materializada.
- Builder/Candidate/Browser observan expresamente los scripts v6.3.
- E2E recorre las 16 fichas y comprueba navegación real en un producto y un servicio.
- `stable` solo se mueve después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Source-of-truth

- `main`: verdad técnica/documental vigente.
- `stable`: snapshot certificado.
- `assets/data/v6/engagement-clarity-v63.json`: contrato de claridad precontratación.
- `catalog-products-v41/` y `catalog-services-v42/`: fuente jurídica/comercial principal de las 16 ofertas.
- `assets/data/v6/search-discovery-readiness-v62.json`: contrato de discovery/search verification.
- `assets/data/v6/measurement-readiness-v61.json`: contrato privacy-first de measurement.
- `experience-system-v60.json` y `experience-content-v60.json`: Experience System base.
- `growth-solutions-v51.json` y `cro-solutions-v52.json`: truth de rutas por situación.
- `offer-narrative-v522.json`: contrato editorial de decisión y modalidad.

## Invariantes

- no inventar clientes, testimonios, premios, antigüedad o resultados;
- no publicar tarifas o descuentos no aprobados;
- no crear nuevas obligaciones desde la presentación de `requirements`/`responsibilities`;
- no PII ni lectura/exportación del contenido del formulario;
- no cotizador automático ni scoring de honorarios;
- WhatsApp manual;
- portal real deshabilitado mientras no exista implementación auténtica;
- no CRM/backend, firma, pagos, agenda, autenticación o upload ficticios;
- no reducir cobertura ni relajar budgets;
- conservar un solo formulario físico canónico;
- conservar exactamente 30 pasos históricos;
- analytics externa deshabilitada hasta decisión/revisión expresa;
- Search Console no puede declararse configurado sin token auténtico;
- readiness no equivale a ranking, tráfico ni indexación garantizada;
- `stable` solo después de gates verdes.

## Próximo ciclo

No se abre otra versión por inercia. Search Console continúa requiriendo un token auténtico externo. Cualquier nuevo ciclo funcional debe partir de una necesidad observable de negocio, conversión, contenido o operación jurídica y demostrar su valor sin duplicar la profundidad ya existente.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado funcional certificado

- Release: **v6.1.0 — Measurement Readiness / observabilidad privacy-first**.
- SHA funcional certificado: `8ffe0e923fc626281870ca2bd38d6c55a665b31b`.
- Canal de cierre: `github-pages-production-measurement-readiness-certified`.
- GitHub Pages sirve v6.1.0.
- Browser E2E/axe público: PASS.
- Lighthouse público: PASS con budgets existentes.
- 46 HTML, 16 fichas profundas, 1 formulario físico y 30 pasos canónicos preservados.
- Analytics externa permanece deshabilitada: `enabled=false`, `provider=none`, sin site id real.

## Frente vigente

**No existe un ciclo funcional nuevo abierto.**

La única tarea activa es el **cierre documental v6.1.0**:

1. marcar el canal como `certified`;
2. actualizar README y memoria canónica;
3. publicar `RELEASE-v6.1.md`;
4. someter este cierre a los gates pre-merge aplicables;
5. fusionar únicamente con same-SHA verde;
6. exigir Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot;
7. cerrar solo cuando `main == stable` y `stable/version.json` declare v6.1.0 certified.

## Resultado que queda cerrado

v6.1 dejó preparada una futura medición agregada sin activar un tercero:

- fuente única `meridiano:funnel-v529`;
- solo `detail.stage` es elegible para exportación;
- raw `adapter.track(name,event)` es `no-op`;
- seis etapas allowlisted: need, offer, evidence, decision, contact, handoff;
- payload custom de Meridiano: solo nombre del evento, cero propiedades custom;
- 43 superficies instrumentadas;
- `404.html`, `demo.html` y `experiencia.html` excluidas por ausencia previa de telemetría;
- Plausible adapter-ready pero deshabilitado;
- `autoCapturePageviews:false`;
- revisión de metadata estándar + actualización de política/configuración obligatorias antes de activar.

## Release engineering cerrado

- `sync_public_version.py` sincroniza versión visible, runtime/status, sitemap y metadata editorial de modificación.
- `--check` bloquea drift de release.
- Canonical Equivalence compara el conjunto exacto esperado y prueba segunda pasada idempotente.
- Candidate/Browser/Measurement reproducen la sincronización en baseline v6.
- Pages aísla los workflow_run del commit canónico `build:` en `ignored-build-output`.
- El `concurrency.group` dinámico queda quoted para YAML inequívoco.
- `validate_pages_trigger_v511.py` bloquea una regresión a grupo fijo o expresión no quoted.

## Fuera de alcance después del cierre

No hacer automáticamente:

- activar Plausible, Umami u otro tercero;
- crear cuentas/proyectos de analytics;
- introducir un site id ficticio;
- cambiar la política como si existiera un tercero activo;
- añadir propiedades custom o UTMs al payload;
- convertir `contact`/`handoff` en una métrica de cliente convertido;
- abrir otro ciclo de UI/CRO/performance sin evidencia observable.

## Condición para futura activación de analytics

Una futura activación requiere como mínimo:

1. decisión explícita de proveedor;
2. identificador/snippet auténtico;
3. revisión técnica de metadata estándar y tráfico saliente;
4. actualización previa de política y configuración;
5. pageviews automáticos deshabilitados salvo decisión expresa distinta;
6. nueva suite de privacy/network E2E;
7. nueva certificación y promoción automática de `stable`.

## Próximo ciclo

Después de cerrar esta documentación, el proyecto queda en estado estable. El siguiente ciclo debe arrancar únicamente desde una necesidad observable o una decisión explícita de negocio/medición, con criterio de éxito verificable. No se añade una nueva capa versionada por inercia.

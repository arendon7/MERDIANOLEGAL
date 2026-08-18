# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Estado funcional certificado

- Release: **v6.3.0 — Engagement Clarity / claridad precontratación**.
- SHA funcional certificado: `118cee5030f27689d91172beb525d7d92c751117`.
- Canal: `github-pages-production-engagement-clarity-certified`.
- PR funcional: `#160` fusionado.
- Builder materializó las 16 fichas y produjo el snapshot funcional certificado.
- `stable` fue promovido automáticamente a `118cee50…` después de Pages, smoke, Browser/axe, Lighthouse y snapshot.
- Search Console permanece sin configurar: `searchConsoleConfigured=false` y sin token auténtico.
- Analytics externa permanece deshabilitada: `enabled=false`, `provider=none`, `site_id=""`.
- 46 HTML, 16 fichas profundas, un único formulario físico y 30 pasos históricos permanecen intactos.

## Frente vigente

**No existe un ciclo funcional nuevo abierto.**

La única tarea activa es el **cierre documental v6.3.0**:

1. marcar el canal como `certified`;
2. actualizar README y memoria canónica;
3. publicar `RELEASE-v6.3.md`;
4. hacer phase-aware el gate v6.3 para una baseline ya materializada, sin aceptar estados parciales;
5. someter el cierre a los gates pre-merge aplicables;
6. fusionar únicamente con same-SHA verde;
7. exigir nuevamente Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot;
8. cerrar solo cuando `main == stable` y `stable/version.json` declare v6.3.0 certified.

## Resultado que queda cerrado

v6.3 hace visible en las 16 fichas una capa de precontratación ya contenida en los catálogos jurídicos:

- `requirements` → **Qué debe estar listo del lado del cliente**;
- `responsibilities` → **Cómo se distribuyen las responsabilidades**;
- un único hito `Para empezar`;
- una única sección `#v6-engagement` antes de Límites;
- exactamente 7 hitos de navegación en una ficha v6.3.

La representación visible no redefine esos datos. El validator compara fila por fila contra `catalog-products-v41/*.json` y `catalog-services-v42/*.json`.

## Release engineering cerrado

- materializador v6.3 fail-closed + `--check`;
- validator 16/16 contra truth canónico;
- integración mediante `normalize_experience_compat_v60.py`, sin paso 31;
- first-pass exacto `release drift ∪ engagement drift`;
- Canonical Equivalence `measurement ∪ release ∪ discovery ∪ engagement`;
- v4.6 estricto: 6 hitos sin v6.3 / exactamente 7 con v6.3;
- CSS v6.3 estabilizado para segunda pasada byte-equivalent;
- Builder/Candidate/Browser con cobertura explícita del nuevo materializador;
- E2E en las 16 fichas y navegación real representativa;
- gate v6.3 de cierre: 0/16 materializadas exige 16 drift; 16/16 exige 0; cualquier estado parcial falla.

## Fuera de alcance después del cierre

No hacer automáticamente:

- reescribir `requirements` o `responsibilities` por intuición;
- añadir obligaciones, tarifas, descuentos o cronogramas no aprobados;
- activar Search Console sin token auténtico;
- activar Plausible, Umami u otra analítica;
- crear backend, CRM, portal, auth, pagos, firma, agenda o upload ficticios;
- abrir v6.4 solo por continuidad de versionado;
- reducir cobertura E2E/axe o relajar Lighthouse.

## Próximo ciclo

Después de cerrar esta documentación, el proyecto queda en estado estable. El próximo ciclo debe partir de una necesidad observable de negocio, conversión, contenido o operación jurídica. Antes de añadir otra capa, debe comprobarse si la verdad necesaria ya existe en los catálogos o contratos actuales y puede presentarse mejor, como ocurrió en v6.3.

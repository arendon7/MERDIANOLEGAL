# Meridiano Legal · Web canónica v6.0.0

Sitio público static-first de Meridiano Legal: `https://arendon7.github.io/MERDIANOLEGAL/`.

## Estado certificado

**v6.0.0 — Experience System**.

- SHA funcional certificado: `a7940696cb358fcd4ace50e32f4a1463b76fdaa5`.
- `main == stable` sobre ese SHA al cierre funcional.
- Canal certificado: `github-pages-production-experience-system-certified`.
- 46 HTML públicos, 16 fichas profundas y 1 formulario físico canónico.
- 30 pasos exactos del builder canónico; sin paso 31.
- GitHub Pages sirve v6.0.0 y el smoke público v5.0→v5.3 pasa.
- Browser E2E + axe sobre la v6 pública: PASS.
- Lighthouse sobre la v6 pública: PASS con los budgets existentes.
- Cobertura reducida: no. Budgets relajados: no.
- Portal real de clientes: deshabilitado; `demo.html` continúa siendo demostrativo/noindex.

## v6.0 — Experience System

v6 consolida la experiencia pública alrededor de la secuencia **situación → resultado → intervención → evidencia → contacto** y reduce la dependencia de taxonomía interna para la primera lectura.

La release:

- preserva la profundidad jurídica y comercial histórica en el DOM;
- diferencia semánticamente decisión, resultado, entregable, proceso, perímetro, límite, evidencia y profundidad;
- usa templates distintos para producto cerrado y servicio adaptable;
- migra las 46 superficies públicas sin alterar las cantidades canónicas de productos, servicios, soluciones, sectores o perspectivas;
- mantiene un único formulario físico y handoff manual por WhatsApp;
- conserva capability truth: sin portal real, auth, CRM, pagos, firma, agenda, upload ni automatizaciones ficticias;
- mantiene funnel/telemetría sin PII, sin persistencia propia y sin equiparar contacto con conversión.

## Release engineering

El ciclo v6 también endureció el sistema de publicación:

- equivalencia canónica pre-merge frente al builder de producción;
- validación phase-aware para baselines legacy y Experience System v6;
- la cadena de equivalencia ejecuta la misma calidad estática Python, JavaScript y JSON que Pages;
- los cambios en `scripts/validate_*.py` disparan el builder canónico;
- el smoke live usa cache-busting y espera explícitamente la versión esperada antes de validar el resto de la superficie;
- `stable` solo se mueve después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Memoria estructural

Graphify sobre el SHA funcional certificado registra 1.007 nodos, 1.887 relaciones, 115 notas wiki y detecta 46 HTML, 8 productos, 8 servicios, 7 superficies de soluciones, 8 sectores, 6 perspectivas y 17 specs E2E.

Graphify es memoria derivada; `main`, `stable`, Pages, validadores y tests deciden.

## Documentación

- `RELEASE-v6.0.md`: contrato, waves, incidencias y evidencia del cierre.
- `knowledge/00_CANON/CONTEXTO_RAPIDO.md`: contexto operativo actual.
- `knowledge/00_CANON/ESTADO_ACTUAL.md`: estado canónico y certificación.
- `knowledge/00_CANON/TAREA_ACTIVA.md`: frente vigente.
- `knowledge/HOME.md`: navegación de memoria.

El commit documental de cierre debe atravesar nuevamente el pipeline y terminar con `main == stable` para que el cierre quede definitivo.

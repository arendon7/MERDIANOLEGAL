# Meridiano Legal v6.0.0 — Experience System

Fecha de release funcional: 2026-08-18

## Objetivo

v6.0 transforma la web pública de Meridiano Legal en una interfaz jurídica de decisión coherente y client-first, sin recortar la profundidad construida en v5.x.

La arquitectura principal pasa a ser:

**situación → resultado → intervención → evidencia → contacto**.

El objetivo no fue añadir otra capa visual versionada, sino consolidar la experiencia existente, reducir la dependencia de taxonomía interna en la primera lectura y diferenciar semánticamente el papel de cada bloque jurídico/comercial.

## Alcance completado

La migración se cerró en las seis waves previstas más foundations:

### Wave 0 — Foundations

- Experience System v6, tokens y shell consolidado.
- `experience-system-v60.json` y `experience-content-v60.json` como contratos de experiencia/contenido.
- materializadores y validators v6.
- detección phase-aware para distinguir baseline legacy de baseline ya materializada en v6.

### Wave 1 — Pilotos

- Home desktop/mobile.
- Auditoría Jurídica Empresarial Integral.
- Tecnología e Inteligencia Artificial.
- Contacto/handoff.

### Wave 2 — 16 fichas

- 8/8 productos.
- 8/8 servicios.
- templates diferenciados para producto cerrado y servicio adaptable.
- truth, entregables, proceso, perímetro, límites y profundidad preservados.

### Wave 3 — Soluciones

- hub de soluciones.
- 6/6 rutas por situación empresarial.
- continuidad Growth/CRO preservada.

### Wave 4 — Sectores

- 8/8 superficies sectoriales integradas al sistema v6.
- SEO, authority y contexto editorial preservados.

### Wave 5 — Perspectivas

- hub editorial.
- 6/6 perspectivas completas.
- guía de lectura v6 preservando profundidad editorial y navegación equivalente.

### Wave 6 — Resto público

- Firma.
- Experiencia.
- Centro Demo.
- aviso legal, privacidad y términos.
- 404.

## Contratos preservados

v6 mantiene:

- 46 páginas HTML públicas;
- 8 productos + 8 servicios;
- 7 superficies de soluciones;
- 8 sectores;
- 6 perspectivas internas + hub editorial;
- 16 fichas profundas;
- un único formulario físico canónico;
- WhatsApp como handoff manual;
- 30 pasos exactos del builder canónico;
- profundidad jurídica completa en DOM;
- capability truth: portal real, auth, CRM, pagos, firma, agenda y upload no implementados/deshabilitados;
- funnel/observabilidad sin PII ni persistencia propia;
- contacto/handoff no equivale a conversión, aceptación ni inicio;
- budgets, axe, Browser y Lighthouse sin relajación.

## Release engineering endurecido durante v6

La release no se cerró desactivando gates. Los fallos encontrados se usaron para fortalecer la arquitectura de publicación.

### 1. Equivalencia builder/Pages

La cadena de producción necesitaba distinguir una baseline pre-v6 de una baseline ya materializada en v6. Builder y Pages pasaron a saltar materializadores HTML legacy cuando detectan `data-experience-system="v6"`, manteniendo sincronización de versión, applicators v6 y validadores.

Se creó un gate de **V6 canonical builder equivalence** que reproduce el builder antes del merge y demuestra idempotencia.

### 2. Validator v5.17

`validate_handoff_v517.py` dependía de una secuencia YAML con indentación literal. Se sustituyó por validación semántica del orden v5.15 → v5.17 → v5.18 → diff, preservando los checks de continuidad, seguridad e integridad.

### 3. Validators históricos de DOM

Pages reveló que varios validators legacy describían selectores pre-v6 aunque la función correspondiente seguía preservada:

- `validate_site.py`;
- `validate_static_catalog.py`;
- `validate_ux_v45.py`;
- `validate_detail_ux_v46.py`;
- `validate_editorial_ux_v47.py`;
- `validate_page_context.py`.

Se hicieron phase-aware: una baseline legacy continúa exigiendo sus contratos históricos; v6 exige los componentes semánticos equivalentes (`v6-detail-hero`, navegación v6, guía editorial v6, journeys/contexto), sin reducir cobertura.

### 4. Paridad real del gate pre-merge con Pages

El gate de equivalencia se amplió para ejecutar antes del merge:

- toda la cadena Python de calidad estática de Pages;
- todos los `node --check` productivos;
- todos los validadores JSON de Pages;
- diff cero de primera pasada cuando la baseline ya es v6;
- idempotencia de segunda pasada.

Esto evita volver a descubrir después del merge incompatibilidades que podían detectarse antes.

### 5. Cobertura del trigger canónico

Se detectó que algunos cambios en validators podían llegar a `main` sin disparar el builder. El trigger canónico pasó a cubrir `scripts/validate_*.py`, y el validator de topología exige esa cobertura.

### 6. Candidate sobre baseline ya v6

El gate V6 Candidate asumía inicialmente que toda primera materialización debía producir un diff no vacío. Se hizo phase-aware: pre-v6 sigue exigiendo materialización; una baseline ya v6 puede producir cero cambios, pero continúa obligada a superar validators, boundary de 46 superficies e idempotencia de segunda pasada.

### 7. Propagación de GitHub Pages

El smoke live reintentaba errores de red, pero aceptaba inmediatamente cualquier HTTP 200. Durante propagación podía recibir temporalmente `site-status.json` de la versión anterior y bloquear el release aunque el deploy estuviera completándose correctamente.

`validate_live_v50.py` pasó a:

- usar cache-busting por petición;
- enviar headers `no-cache`;
- esperar explícitamente la versión declarada en `version.json`;
- reintentar propagación antes de validar el resto de la superficie.

Los checks históricos v5.0→v5.3 permanecen intactos.

## Evidencia funcional certificada

SHA funcional certificado:

`a7940696cb358fcd4ace50e32f4a1463b76fdaa5`

Estado observado al cierre funcional:

- `main == stable == a7940696cb358fcd4ace50e32f4a1463b76fdaa5`;
- GitHub Pages sirve `6.0.0` en `site-status.json`;
- smoke público v5.0→v5.3: PASS;
- 46/46 superficies v6: PASS;
- 16/16 fichas con truth/depth: PASS;
- 1/1 formulario físico: PASS;
- 30/30 pasos canónicos: preservados;
- primera pasada sobre baseline v6: diff cero;
- segunda pasada: idempotente;
- validadores Python de Pages: PASS;
- JavaScript syntax checks: PASS;
- JSON metadata/catalogs: PASS;
- Release Governance: PASS en los hotfixes funcionales aplicables;
- cobertura reducida: no;
- budgets relajados: no;
- tests eliminados para hacer pasar la release: no.

### Verificación independiente de la superficie pública

Run diagnóstico: `32145563599`.

- Candidate/public probe: PASS.
- `site-status.json` cache-busted respondió `version: 6.0.0`.
- Smoke v5.0: PASS.
- Smoke v5.1: PASS.
- Smoke v5.2: PASS.
- Smoke v5.3: PASS.
- Browser E2E/axe job `95738350273`: PASS.
- Lighthouse job `95738350295`: PASS con budgets existentes.

El diagnóstico fue temporal y se retiró antes del hotfix final; el diff funcional de PR #152 quedó limitado a `scripts/validate_live_v50.py`.

## PRs de estabilización/cierre funcional

- #147 — candidato v6 y gates finales.
- #148 — equivalencia del builder canónico y compatibilidad release phase-aware.
- #149 — evolución de validators legacy iniciales.
- #150 — paridad completa de calidad estática de Pages y validators phase-aware restantes.
- #151 — cobertura del trigger canónico y Candidate phase-aware.
- #152 — smoke live resiliente a propagación de GitHub Pages.

## Graphify

Sobre el SHA funcional certificado, `knowledge/graphify-live` quedó alineado con:

- `source_commit = a7940696cb358fcd4ace50e32f4a1463b76fdaa5`;
- versión `6.0.0`;
- 1.007 nodos;
- 1.887 relaciones;
- 115 notas wiki;
- 46 HTML;
- 8 fuentes de producto;
- 8 fuentes de servicio;
- 7 superficies de soluciones;
- 8 sectores;
- 6 perspectivas;
- 17 specs E2E.

Graphify continúa siendo memoria derivada; `main`, `stable`, Pages, validadores y tests mandan.

## Canal definitivo

El cierre documental cambia el canal de:

`github-pages-experience-system-candidate`

A:

`github-pages-production-experience-system-certified`

El cambio describe el estado de certificación; no modifica la capability pública ni convierte el Centro Demo en un portal real.

## Condición de cierre definitivo

Este documento y la memoria canónica forman parte del cierre. v6.0.0 queda documentalmente cerrada solo cuando el commit que contiene:

- `RELEASE-v6.0.md`;
- README v6;
- `CONTEXTO_RAPIDO.md`;
- `ESTADO_ACTUAL.md`;
- `TAREA_ACTIVA.md`;
- canal `certified` en `version.json`;

atraviese nuevamente los gates aplicables, Builder → Pages → smoke → Browser/axe → Lighthouse → release-health/snapshot y termine con `main == stable`.

## Próximo ciclo

No se abre automáticamente una v6.1.

El siguiente ciclo deberá partir de evidencia real de uso de la v6 publicada y de un problema observable con criterio de éxito verificable. No se añadirá otra capa CSS/JS versionada por inercia ni se reabrirá la taxonomía sin una necesidad concreta de usuario, conversión, accesibilidad, performance u operación.

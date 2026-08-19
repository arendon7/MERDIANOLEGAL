# Meridiano Legal v6.4.0 — Fit & Scope Clarity

Fecha de release funcional: 2026-08-18

## Objetivo

v6.4 reduce una fricción concreta de autocalificación comercial: las 16 fichas profundas ya explicaban resultado, entregables, perímetro, proceso, límites y condiciones del encargo, pero dos piezas de verdad canónica seguían insuficientemente expuestas:

- `situations`: situaciones empresariales concretas en las que la modalidad encaja;
- `supplements`: circunstancias previstas que amplían el alcance base.

La release eleva ambas matrices a primer nivel sin crear contenido jurídico nuevo.

## Resultado funcional certificado

SHA funcional certificado:

`0045588f795f5f0a0b9144786bc61cdf89f34319`

Ese SHA fue producido por el builder canónico después del merge de #162 y promovido automáticamente a `stable` únicamente después de quality, deploy, smoke, Browser/axe, Lighthouse y snapshot.

## Alcance completado

### 1. Truth reutilizado desde los catálogos

Las fuentes permanecen en:

- `catalog-products-v41/*.json` — 8 productos;
- `catalog-services-v42/*.json` — 8 servicios.

v6.4 consume exclusivamente:

- `situations`;
- `supplements`.

No existe una segunda copia editorial con criterios de encaje o ampliaciones resumidas que pueda divergir silenciosamente.

### 2. Nueva capa visible de encaje y alcance

Cada una de las 16 fichas incorpora una única sección `#v6-fit-scope`, situada inmediatamente después de Resultado y antes de Entregables, con dos paneles:

- **Señales de que esta modalidad encaja** — derivado fila por fila de `situations`;
- **Situaciones que amplían el alcance** — derivado fila por fila de `supplements`.

La navegación ejecutiva conserva exactamente los siete hitos de v6.3. `#v6-fit-scope` deliberadamente no añade un octavo hito al TOC.

### 3. Exactitud jurídica de la representación

`scripts/validate_fit_scope_clarity_v64.py` vuelve a abrir los 16 catálogos canónicos y exige igualdad exacta, en orden, entre las matrices visibles y sus fuentes.

El control bloquea, entre otros:

- fuentes faltantes o duplicadas;
- matrices vacías o mal formadas;
- desalineación entre `catalog_id` y ficha HTML;
- sección duplicada;
- `situations` o `supplements` visibles divergentes;
- inserción en páginas fuera de productos/servicios;
- incorporación accidental de `#v6-fit-scope` al TOC;
- orden distinto de Resultado → Fit/Scope → Entregables.

La capa no cambia `perimeter`, `limits`, entregables, método, honorarios, cronogramas, contacto o capability truth.

### 4. Materialización determinista

`scripts/apply_fit_scope_clarity_v64.py`:

- descubre exactamente 8 productos + 8 servicios mediante `data-catalog-id`;
- exige correspondencia 1:1 entre fuente y HTML;
- inserta una sección gestionada después de Resultado;
- carga una hoja CSS aislada;
- ofrece `--check` para detectar drift sin escribir;
- falla de forma cerrada ante truth incompleto;
- conserva idempotencia dentro de la composición completa v6.

La hoja `fit-scope-clarity-v64.css` se ubica en una posición estable antes de `engagement-clarity-v63.css` para evitar drift de orden/whitespace durante materializaciones sucesivas.

### 5. Sin paso histórico 31

La cadena histórica permanece en exactamente 30 pasos.

v6.4 se integra como extensión posterior de Experience v6. `canonical_pipeline_v524.py`, Builder y Pages comparten la misma extensión v6 y ahora incluyen los comandos apply/validate de Fit & Scope Clarity.

### 6. E2E

`tests/e2e/fit-scope-clarity-v64.spec.mjs`:

- visita las 16 fichas profundas;
- exige una única sección v6.4;
- exige ambos paneles y filas visibles;
- comprueba que el TOC siga teniendo siete hitos y no enlace `#v6-fit-scope`;
- verifica el orden DOM Resultado → Fit/Scope → Entregables en producto y servicio representativos.

La spec corre dentro de la suite global Chromium/WebKit y convive con axe y los controles privacy-first de measurement.

## Release engineering

### Gate dedicado v6.4

`.github/workflows/v64-fit-scope-clarity.yml` distingue estrictamente dos estados válidos:

- baseline pre-v6.4: `0/16` materializadas → exige exactamente 16 páginas de fit/scope drift;
- baseline v6.4: `16/16` materializadas → exige exactamente 0 páginas de fit/scope drift;
- cualquier estado parcial entre 1 y 15 falla.

El gate compone además el release drift de `sync_public_version.py` y exige igualdad exacta con el diff observado.

### Canonical Equivalence

La frontera v6 queda expresada como:

`measurement aplicable ∪ release drift ∪ discovery drift ∪ engagement drift ∪ fit/scope drift`

No se amplió a un patrón abierto de HTML permitido.

### Builder, Pages y manifiesto

v6.4 endureció la simetría del pipeline:

- Builder aplica y valida v6.4 después de reconstruir la base v6/v6.3;
- Pages ejecuta la misma extensión durante la comprobación de idempotencia;
- `canonical_pipeline_v524.py` registra exactamente los mismos comandos;
- `validate_pages_trigger_v511.py` exige que cambios del materializador v6.4 disparen Builder.

Los 30 pasos históricos no se modificaron; solo la extensión v6 pasó a incorporar apply/validate v6.4.

### Measurement Browser

Durante la fase candidate se detectó una integración incompleta: Measurement materializaba v6.0/v6.3/v6.2 pero no v6.4 antes de ejecutar la suite global. El efecto eran fallos E2E por ausencia del nuevo bloque, no una regresión de privacidad.

Se corrigió el workflow para materializar y validar v6.4 antes del navegador. No se modificó ninguna expectativa, no se eliminó ninguna prueba y no se relajó cobertura.

## Evidencia pre-merge

### SHA técnico previo al bump

`ecc90b17f0784f53fb4a035c3d91d2ff2938e627`

Seis gates técnicos aplicables verdes:

- V6.4 Fit & Scope Clarity;
- V6 Candidate Validation;
- V6 Canonical Builder Equivalence;
- Release Governance;
- Graphify;
- V6 Browser Candidate / axe.

### Candidate final 6.4.0

`38c140f5ec943f6a527f88278e78d2e9a7cb0bd1`

Nueve workflows aplicables verdes sobre el mismo SHA:

- V6.4 Fit & Scope Clarity;
- V6.3 Engagement Clarity;
- V6.2 Search Discovery Readiness;
- V6.1 Measurement Readiness / Browser E2E;
- V6 Candidate Validation;
- V6 Canonical Builder Equivalence;
- Release Governance;
- Graphify;
- V6 Browser Candidate / axe.

No hubo reviews ni hilos bloqueantes. #162 se fusionó con `expected_head_sha` fijado al candidate certificado.

## Evidencia post-merge

- PR funcional: #162.
- Merge funcional: `8937a985c94e9f29f6dafbc6a53ab8ff5cb24ee0`.
- Builder canónico: `0045588f795f5f0a0b9144786bc61cdf89f34319`.
- GitHub Pages público sirvió v6.4.0 y superó smoke v5.0–v5.3.
- Browser E2E/axe público: PASS.
- Lighthouse público: PASS con budgets existentes.
- `stable` alcanzó automáticamente `0045588f…` después del snapshot oficial.
- No hubo force-push manual de `stable`.
- Cobertura reducida: no.
- Budgets relajados: no.

## Incidencia productiva y recuperación

El primer run productivo de Pages (`32203459870`) completó:

- quality: success;
- deploy: success;
- smoke: success;
- Browser E2E: success;
- Lighthouse: failure;
- snapshot: skipped.

La causa registrada por Lighthouse fue un **HTTP 503 transitorio al cargar únicamente `demo`**. Las demás superficies auditadas obtuvieron performance entre 0.98 y 1.00 y accessibility 1.00.

Para distinguir una regresión real de un incidente transitorio se abrió el PR diagnóstico temporal #164, sin despliegue y sin posibilidad de mover `stable`. Contra la misma URL pública se reprodujeron con éxito:

- smoke v6.4;
- Browser E2E/axe completo;
- Lighthouse con los budgets vigentes.

El PR #164 se cerró sin merge.

Después se reejecutaron **los jobs fallidos del mismo run oficial**, sin cambiar código. El Lighthouse oficial pasó, el snapshot se ejecutó, generó los reportes CI/gobernanza y movió `stable` al SHA canónico.

La recuperación no introdujo retries laxos, no alteró budgets y no redujo cobertura.

## Garantías preservadas

v6.4 no altera:

- 46 HTML públicos;
- 16 fichas profundas;
- 43 páginas indexables + 3 `noindex`;
- sitemap canónico de 43 URLs;
- Search Console `readiness-not-verified` y sin token auténtico;
- analytics externa deshabilitada;
- ausencia de PII exportada;
- un único formulario físico;
- WhatsApp manual;
- portal/auth/CRM/pagos/firma/agenda/upload deshabilitados;
- exactamente 30 pasos históricos;
- ausencia de precios, descuentos, clientes, testimonios o resultados inventados.

## Estado final

v6.4.0 queda funcionalmente certificada como **Fit & Scope Clarity**. La release mejora la comprabilidad de las 16 ofertas mostrando, desde truth jurídico ya aprobado, cuándo una modalidad encaja y qué circunstancias amplían el alcance base.

El cierre documental queda definitivo cuando el commit que marca el canal como `certified` atraviese nuevamente Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y `main == stable`.

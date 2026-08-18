# Meridiano Legal v6.3.0 — Engagement Clarity

Fecha de release funcional: 2026-08-18

## Objetivo

v6.3 reduce una fricción concreta de decisión comercial: las 16 fichas profundas ya explicaban resultado, entregables, perímetro, proceso y límites, pero la información sobre **qué debía aportar el cliente** y **cómo se distribuían las responsabilidades** permanecía relegada a la profundidad histórica.

La release hace visible esa información sin crear truth jurídico nuevo.

## Resultado funcional

SHA funcional certificado:

`118cee5030f27689d91172beb525d7d92c751117`

Ese SHA fue producido por el builder canónico después del merge de #160 y promovido automáticamente a `stable` únicamente después de la cadena post-deploy.

## Alcance completado

### 1. Truth reutilizado desde los catálogos

Las fuentes continúan siendo:

- `catalog-products-v41/*.json` — 8 productos;
- `catalog-services-v42/*.json` — 8 servicios.

v6.3 consume únicamente dos campos ya aprobados:

- `requirements`;
- `responsibilities`.

No se creó un archivo paralelo con versiones resumidas de esas matrices.

### 2. Nueva capa visible de precontratación

Cada una de las 16 fichas incorpora:

- un enlace `Para empezar` en la navegación ejecutiva;
- una sección `#v6-engagement` situada después de Proceso y antes de Límites;
- un panel **Qué debe estar listo del lado del cliente**;
- un panel **Cómo se distribuyen las responsabilidades**.

La navegación v6.3 contiene exactamente 7 hitos.

### 3. Exactitud jurídica de la representación

`scripts/validate_engagement_clarity_v63.py` vuelve a abrir los 16 catálogos canónicos y compara fila por fila, en orden, la representación HTML contra `requirements` y `responsibilities`.

El control bloquea:

- fuentes faltantes;
- matrices vacías;
- filas mal formadas;
- `catalog_id` sin ficha o ficha sin fuente;
- secciones duplicadas;
- enlaces duplicados;
- matrices visibles divergentes;
- ubicación incorrecta respecto de Límites y cierre.

Por diseño, la capa v6.3 no modifica entregables, perímetro, proceso, límites, honorarios, contacto o capability truth.

### 4. Materialización determinista

`scripts/apply_engagement_clarity_v63.py`:

- descubre exactamente 16 fichas por `data-catalog-id`;
- exige correspondencia 1:1 entre HTML y catálogo;
- inserta estilos, navegación y sección gestionada;
- ofrece `--check` para detectar drift sin escribir;
- falla de forma cerrada si la verdad canónica está incompleta;
- es idempotente dentro de la cadena completa v6.

### 5. Integración sin paso 31

Engagement Clarity se ejecuta desde `normalize_experience_compat_v60.py`.

El builder conserva exactamente los 30 pasos históricos. v6.3 no añadió una etapa numerada independiente.

### 6. E2E

`tests/e2e/engagement-clarity-v63.spec.mjs`:

- visita las 16 fichas profundas;
- exige una sección v6.3 y un enlace de navegación por ficha;
- exige filas visibles en requirements y responsibilities;
- prueba navegación real a `#v6-engagement` en una ficha de producto y una de servicio.

La spec corre dentro de la suite global Chromium/WebKit y convive con axe y el firewall de measurement.

## Release engineering

### Gate dedicado v6.3

`.github/workflows/v63-engagement-clarity.yml` certifica dos fases sin convertirlas en una tolerancia abierta:

- baseline pre-v6.3: `0/16` fichas materializadas → exige exactamente 16 páginas de engagement drift;
- baseline v6.3: `16/16` fichas materializadas → exige exactamente 0 páginas de engagement drift;
- cualquier estado parcial entre 1 y 15 falla.

El gate compone además el release drift declarado por `sync_public_version.py` y exige igualdad exacta con el diff real.

### Canonical Equivalence

La frontera v6 pasa a ser:

`measurement aplicable ∪ release drift ∪ discovery drift ∪ engagement drift`

No se permite una expresión amplia como “cualquier HTML de productos/servicios”.

### Compatibilidad histórica v4.6

El validator histórico de navegación profunda exigía exactamente seis hitos en Experience v6. La incorporación deliberada de `Para empezar` hizo necesario evolucionarlo sin perder precisión:

- sin Engagement Clarity: exactamente 6 hitos;
- con Engagement Clarity: exactamente 7;
- el nuevo hito debe apuntar a `#v6-engagement` y llevar el atributo gobernado v6.3.

### Trigger coverage

- Builder observa expresamente `scripts/apply_engagement_clarity_v63.py`.
- Candidate observa apply/validate v6.3.
- Browser observa apply/validate v6.3 y los E2E.
- `validate_pages_trigger_v511.py` exige que Builder conserve esa cobertura.

## Incidencias que mejoraron el diseño

### 1. Claim lexical vs truth canónico

La primera versión del validator prohibía por texto ciertas palabras como `garantiza`. El gate reveló que algunas aparecían legítimamente dentro de matrices ya aprobadas en los catálogos.

La solución no fue cambiar el catálogo ni introducir excepciones por frase. Se eliminó el veto lexical redundante y se mantuvo un control más fuerte: **el HTML visible debe coincidir exactamente con la fuente canónica**.

### 2. Idempotencia de la hoja CSS

La primera ubicación del stylesheet v6.3 al final de `<head>` interactuaba con el normalizador histórico de estilos v6.0, que retira y repone sus cuatro hojas gestionadas. La segunda pasada producía únicamente whitespace/order drift.

La hoja v6.3 pasó a insertarse en una posición estable antes de `tokens.css`, y su regex de limpieza dejó de consumir saltos de línea vecinos. El gate volvió a demostrar segunda pasada byte-equivalent.

### 3. Navegación histórica exacta

Canonical Equivalence detectó que v4.6 seguía exigiendo exactamente seis enlaces. En vez de relajar a `>=6`, el validator evolucionó de manera phase-aware para exigir seis o siete según exista o no la sección v6.3.

### 4. Gate de cierre post-materialización

La transición inicial exigía 16 fichas pendientes, condición correcta antes del primer builder. Tras la certificación funcional, esa misma regla habría convertido cualquier cierre documental en un falso fallo.

El gate evolucionó para detectar la fase por el output materializado: 0/16 → 16 drift; 16/16 → 0 drift; parcial → fallo.

## Evidencia pre-merge

### SHA técnico previo al bump

`a7e8b057dc4818365247cd0615c796a233836203`

Siete gates técnicos verdes antes de cambiar `version.json`:

- V6.3 Engagement Clarity;
- V6 Candidate Validation;
- V6 Canonical Builder Equivalence;
- Release Governance;
- Graphify;
- V6 Browser Candidate / axe;
- V6.1 Measurement Readiness / Browser E2E.

### Candidate final 6.3.0

`a90e035b0389344d7a6bc435a0735180a1d37051`

Ocho gates aplicables verdes sobre el mismo SHA:

- V6.3 Engagement Clarity;
- V6.2 Search Discovery Readiness;
- V6 Candidate Validation;
- V6 Canonical Builder Equivalence;
- Release Governance;
- Graphify;
- V6 Browser Candidate / axe;
- V6.1 Measurement Readiness / Browser E2E.

El gate Search Discovery fue aplicable por el bump de versión y confirmó que v6.3 no reintrodujo drift en sitemap/canonicals.

## Evidencia post-merge

- PR funcional: #160.
- Merge funcional: `8f53385979658de68cf2c51a8ed9853db3dd911f`.
- Builder canónico: `118cee5030f27689d91172beb525d7d92c751117`.
- `stable` alcanzó automáticamente ese SHA después de la cadena productiva.
- No hubo force-push manual de `stable`.
- Browser/axe productivo: prerequisito satisfecho antes de la promoción.
- Lighthouse productivo: prerequisito satisfecho antes de la promoción.
- Budgets relajados: no.
- Cobertura reducida: no.

## Garantías preservadas

v6.3 no altera:

- 46 HTML públicos;
- 43 indexables + 3 `noindex`;
- sitemap de 43 URLs;
- Search Console `readiness-not-verified`;
- analytics externa deshabilitada;
- ausencia de PII exportada;
- un único formulario físico;
- WhatsApp manual;
- portal/auth/CRM/pagos/firma/agenda/upload deshabilitados;
- 30 pasos históricos del builder;
- ausencia de precios, descuentos, clientes, testimonios o resultados inventados.

## Estado final

v6.3.0 queda funcionalmente certificada como **Engagement Clarity**. La release mejora la comprabilidad de las 16 ofertas haciendo visible verdad jurídica ya aprobada, sin convertir la capa comercial en una fuente independiente de obligaciones.

El cierre documental queda definitivo cuando el commit `certified` vuelva a atravesar Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y `main == stable`.

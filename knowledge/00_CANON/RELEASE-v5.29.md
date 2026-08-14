# Meridiano Legal — Release v5.29.0

Fecha de cierre funcional: 2026-08-14.

## Alcance

v5.29 introduce un funnel observable y una señal contextual de confianza sin alterar la naturaleza static-first del sitio ni habilitar capacidades inexistentes.

### Funnel observable

Etapas contractuales:

`awareness → need → offer → evidence → decision → contact → handoff`

La capa:

- mantiene un máximo de 48 eventos únicamente en memoria;
- reutiliza `MeridianoTelemetry` sin habilitar transporte público;
- no lee valores del formulario;
- no usa persistencia local, cookies, IndexedDB, identificadores cross-session, fingerprinting ni UUID;
- no introduce `fetch`, XHR ni `sendBeacon`;
- observa checkpoints de portada y las 16 fichas profundas por `data-catalog-id`;
- fija 5% de superficie visible como umbral contractual de exposición para soportar secciones más altas que el viewport móvil.

`contact` y `handoff` no son sinónimos de conversión: el navegador no conoce envío, entrega, lectura, aceptación de propuesta, inicio de encargo ni conversión a cliente.

### Confianza contextual

Entre `#contratacion` y `#contacto` se materializa un `<aside>` compacto derivado exclusivamente de `professional-authority-v525.json`. Presenta formación, práctica actual y tipos de asuntos documentados, conservando la frontera expresa de que esa trayectoria no constituye lista de clientes ni prueba de resultados específicos.

El bloque no es una nueva `<section>`, por lo que la secuencia narrativa v5.28 permanece intacta.

## Evidencia funcional certificada

- SHA funcional: `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`.
- Builder final: `31823965908`.
- Site Quality and Deploy #374: `31823985048`.
- Release Governance final relevante: `31823922160`.
- Pipeline canónico: 30 pasos — PASS.
- Segunda pasada / `git diff --exit-code`: PASS.
- Validaciones estáticas: 37/37 — PASS.
- Cobertura de 16 fichas profundas: PASS.
- GitHub Pages: PASS.
- Smoke público: PASS.
- Browser E2E/axe: **88 observados · 86 PASS · 2 SKIP · 0 FAIL · 0 retries**.
- axe: 0 violaciones serias/críticas en las superficies cubiertas.
- Lighthouse performance/accesibilidad: PASS contra budgets existentes.
- Promoción automática de `stable`: PASS.
- Budgets relajados: no.
- Cobertura reducida: no.
- PII/persistencia/transporte nuevo: no.

## Hallazgos detectados y corregidos por CI

### 1. Guardias PII demasiado amplios

Las primeras reglas estáticas prohibían los literales `name:` y `contact-form`. Ambos podían aparecer legítimamente como estructura de evento o etiqueta semántica de destino sin implicar lectura de datos personales.

Se corrigió el validator para prohibir acceso real a controles y valores (`FormData`, textarea/input/select, `.value`, `.elements`, selectores de formulario), manteniendo las etiquetas semánticas necesarias. No se debilitó la protección de PII.

### 2. Deriva de idempotencia en el `<head>`

La primera salida canónica alternaba whitespace alrededor de `commercial-v43.css` y `visual-v39.css` durante la segunda pasada.

Se hizo determinista `scripts/apply_funnel_trust_v529.py`, restringiendo la eliminación de links a whitespace horizontal y normalizando el separador final. `git diff --exit-code` permaneció obligatorio y terminó verde.

### 3. Checkpoint de contacto incompatible con geometría móvil

El runtime inicial exigía `intersectionRatio >= 0.25`. En Chromium móvil, `#contacto` es más alto que el viewport, por lo que podía estar efectivamente alcanzado sin que 25% de su superficie fuese visible simultáneamente.

El contrato se corrigió a 5% de exposición visible y el E2E dejó de usar pausas fijas: ahora espera explícitamente la aparición de cada milestone real. El fallo móvil quedó cerrado sin cambiar la semántica de `contact`.

## Invariantes preservadas

- 46 HTML.
- 16 fichas profundas.
- 1 formulario físico canónico.
- WhatsApp manual.
- Portal real deshabilitado.
- Demo explícitamente ficticia/noindex.
- 30 pasos canónicos.
- Profundidad jurídica/comercial preservada.
- Sin clientes, testimonios o resultados inventados.
- Sin conversión inferida desde navegación.
- `stable` únicamente después de todos los gates verdes.

## Cierre documental

El canal pasa de `github-pages-production-funnel-trust-candidate` a `github-pages-production-funnel-trust-certified`. Este cambio documental debe volver a atravesar builder, idempotencia, validaciones, Pages/smoke, Browser E2E/axe, Lighthouse, promoción de `stable` y Graphify. El SHA resultante de ese último ciclo será la referencia definitiva de v5.29.

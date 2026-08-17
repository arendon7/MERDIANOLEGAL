# Baseline de aceptación vNext — antes de abrir candidato v6

Fecha: 2026-08-17
Estado: contrato de comparación; no modifica producción.

## 1. Baseline funcional certificado

Release: **v5.31.0**.

Estado canónico documentado:
- 46 HTML públicos;
- 16 fichas profundas;
- 6 rutas de necesidad + índice;
- un único formulario físico;
- WhatsApp manual;
- portal real deshabilitado;
- funnel sin PII/persistencia;
- no inferir conversión;
- no tarifas inventadas;
- profundidad no ocultada con CSS/hidden;
- exactamente 30 pasos canónicos.

## 2. Evidencia de QA v5.31

Última certificación funcional conocida del ciclo:
- builder: PASS, 30 pasos;
- segunda pasada/idempotencia: PASS;
- validaciones estáticas: 37/37 PASS;
- Pages + smoke: PASS;
- Browser E2E/axe: 112 observados, 110 PASS, 2 SKIP, 0 FAIL, 0 retries;
- axe: sin violaciones serious/critical en superficies cubiertas;
- Lighthouse: PASS con budgets existentes;
- stable promotion: PASS;
- Graphify: 800 nodos, 1.368 relaciones, 106 notas wiki, 16 specs E2E.

Este baseline es un **piso**, no una meta para relajar.

## 3. Baseline estructural actual

Graphify post Design Skills Foundation sobre `main@5fdca20b3837eab9ea2b2341b3d239660f48562f` mantiene:
- `html_total`: 46;
- `products_source`: 8;
- `services_source`: 8;
- `solutions_html`: 7;
- `sectors_html`: 8;
- `perspectives_html`: 6;
- `python_scripts`: 88;
- `javascript_sources`: 26;
- `e2e_specs`: 16.

La incorporación de tooling/design docs no cambió la release funcional v5.31.

## 4. Baseline de presentación

Home:
- 23 CSS cargados;
- 13 JS cargados.

Fichas profundas:
- cadena representativa de 9 CSS entre shell/context/visual/detail/decision/proof/offer/commercial/compression.

Estos números son inventario técnico, **no budgets todavía**.

## 5. Acceptance bar del candidato v6

### No regresión obligatoria
- 46 HTML o cambio explícito aprobado con ADR; por defecto 46;
- 16 fichas;
- 8 productos + 8 servicios;
- 7 soluciones;
- 8 sectores;
- 6 perspectivas internas;
- 1 formulario;
- 30 pasos builder;
- 0 PII persistida;
- 0 fake capabilities;
- 0 pérdida de profundidad jurídica;
- 0 serious/critical axe en cobertura vigente;
- Lighthouse dentro de budgets vigentes;
- idempotencia PASS;
- Pages/smoke PASS;
- Graphify source_commit == main al cierre;
- stable solo después de todo lo anterior.

### Mejora observable esperada
Sin fijar todavía umbrales artificiales, v6 debe demostrar:
- menos CSS/JS de presentación cargado;
- menos dependencia de overrides históricos;
- menos capas comerciales simultáneamente visibles;
- un CTA primario claramente dominante por estado;
- menor cardification;
- diferenciación visual de decisión/entregable/proceso/perímetro/límite/evidencia;
- mobile sin depender de carrusel para contenido esencial;
- contacto perceptualmente más simple sin perder truth/handoff.

## 6. Superficies críticas de regresión

Obligatorias en piloto:
1. Home desktop.
2. Home mobile.
3. Auditoría Jurídica Empresarial Integral desktop/mobile.
4. Tecnología e Inteligencia Artificial desktop/mobile.
5. Contacto/handoff.
6. navegación/header/mobile menu.
7. disclosure profundo.

Antes de propagación global añadir muestras representativas de:
- solution;
- sector;
- perspective;
- firma;
- experiencia/demo;
- legal notice.

## 7. Pruebas específicas nuevas a diseñar

### IA/jerarquía
- first-layer contiene problema/resultado/CTA esperado;
- taxonomía secundaria sigue accesible;
- demo no compite como CTA primario.

### Truth parity
- cantidades/perímetros/entregables por `data-catalog-id`;
- límites obligatorios presentes;
- cierre verificable presente;
- profundidad accesible después de expandir.

### CSS migration
- páginas v6 solo cargan allowlist v6 + excepciones declaradas;
- exception list no crece silenciosamente.

### Contact
- un único `<form>`;
- no upload;
- privacy required;
- WhatsApp manual;
- no fetch/XHR/sendBeacon para contenido del formulario;
- no local/session storage, cookie o IndexedDB con funnel/form;
- handoff no afirma delivered/read/accepted/started.

### Motion
- reduced motion elimina/reduce enhancement no esencial;
- keyboard/focus no depende de animación.

## 8. Regla de comparación

Una mejora visual no compensa:
- pérdida de contenido;
- pérdida de semántica;
- deterioro Lighthouse;
- deterioro a11y;
- falsedad comercial;
- aumento de capability ficticia;
- ruptura de idempotencia.

Si ocurre cualquiera, la wave no pasa.

## 9. Condición para abrir formalmente v6.0

Se considera cumplida cuando en `main` exista el paquete de discovery con:
- audit post-v5.31;
- design brief;
- IA target;
- Home target;
- detail pilots target;
- prototype critique;
- technical architecture;
- migration matrix;
- presentation inventory;
- acceptance baseline;
- skills operating layer.

Entonces puede crearse `TAREA_ACTIVA`/ADR/release contract de v6.0 y comenzar implementación en rama funcional separada.
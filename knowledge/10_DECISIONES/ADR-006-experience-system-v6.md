# ADR-006 — Experience System v6

Fecha: 2026-08-17
Estado: propuesto durante implementación; se acepta únicamente con certificación final.

## Contexto

v5.31 cerró correctamente el problema de profundidad simultáneamente visible mediante divulgación progresiva nativa. La auditoría posterior mostró que el siguiente cuello de botella no es más contenido, sino coherencia sistémica de IA, jerarquía, componentes y presentación.

La Home carga 23 CSS y 13 JS; las fichas profundas combinan múltiples generaciones de presentación. Esta sedimentación es resultado de evolución incremental válida, pero aumenta costo de cambio y hace que funciones semánticas distintas terminen con tratamientos visuales similares.

## Decisión

Adoptar para v6 un **Experience System semántico, source-driven y static-first** que:

1. mantenga las fuentes jurídicas/comerciales existentes como truth layer;
2. introduzca un modelo semántico de experiencia separado de la presentación;
3. produzca HTML final desde renderer/materializer v6 en vez de seguir acumulando overrides;
4. consolide CSS en una familia pequeña de responsabilidades estables;
5. racionalice JS, conservando solo behavior/capability real;
6. diferencie templates de producto cerrado y servicio adaptable;
7. preserve profundidad bajo disclosure nativo cuando sea secundaria;
8. migre por waves y no en un big-bang;
9. preserve exactamente 30 pasos del builder sin añadir paso 31.

## Gramática semántica

Componentes conceptuales autorizados:
- decision statement;
- situation index;
- outcome ledger;
- deliverable ledger;
- process timeline;
- perimeter matrix;
- responsibility note;
- boundary band;
- evidence block;
- commercial matrix;
- scope drivers disclosure;
- deep disclosure;
- contextual CTA;
- canonical contact form / WhatsApp handoff.

La elección visual depende de la función. No existe un `Card` universal como solución por defecto.

## Integración con builder

v6 no agrega un paso canónico nuevo. El renderer v6 se integrará dentro de uno de los pasos existentes de presentación. Los materializadores históricos que ya no deban alterar markup/CSS quedan `semver`-gated como no-op/delegación para `>=6.0.0`.

El punto exacto de integración se fija y valida durante Wave 0; debe garantizar que ningún paso posterior reintroduzca markup/CSS legacy absorbido.

## CSS

Objetivo conceptual:
- tokens;
- base;
- layout;
- components;
- surfaces;
- print.

Los nombres/particiones exactos pueden cambiar durante Wave 0, pero está prohibido resolver v6 mediante una nueva cadena de overrides tipo `v600.css` encima de todas las generaciones anteriores.

## JS

No migrar a SPA/framework.

Mantener runtime solo cuando existe estado real en navegador:
- navegación;
- formulario/handoff manual;
- observabilidad permitida;
- feedback/accesibilidad necesaria.

Mover a build-time la inserción de markup determinista cuando sea seguro.

## Navegación e IA

La primera lectura se orienta a situación/decisión del cliente. Servicios/productos/planes/modalidades continúan disponibles como oferta/SEO y profundidad, pero dejan de gobernar la entrada principal.

`Centro demo` se reencuadra como evidencia de método/experiencia y no compite con `Presentar necesidad` como CTA primario.

## Product vs Service

### Producto cerrado
Prioridad:
`problema/resultado → entregables → perímetro → proceso → cierre/límites → profundidad`.

### Servicio adaptable
Prioridad:
`decisión/pregunta → resultado → capas/intervención → perímetro → gobierno/cierre/límites → profundidad`.

## Contacto

Se conserva un único formulario físico. La simplificación es perceptual, no funcional: contratos de privacidad, capability truth, estados comerciales y handoff manual siguen vigentes.

## Motion

Motion entra después de IA/layout estable. Se aplicará design engineering sobrio, causal, compatible con reduced motion; no scroll-jacking, parallax pesado ni animación de texto decorativa.

## Consecuencias positivas

- menor costo cognitivo para visitante;
- mejor diferenciación de tipos de información;
- menor deuda de cascada;
- cambios transversales más predecibles;
- mejor testabilidad semántica;
- mobile diseñado como superficie propia;
- posibilidad de reducir requests/bytes sin sacrificar depth.

## Costos/riesgos

- migración de 46 superficies;
- riesgo de drift entre truth y nuevo renderer;
- transición compleja con scripts históricos;
- mayor tamaño inicial del cambio arquitectónico;
- necesidad de tests de parity adicionales.

Mitigación: waves, stable congelado, truth parity validators, idempotencia, Browser/axe/Lighthouse y rollback simple a v5.31.

## Alternativas descartadas

### Añadir v5.32/v532.css
Descartado: corrige síntomas y profundiza sedimentación.

### Reescribir en React/Next u otro framework
Descartado: no existe necesidad de capability que justifique abandonar static-first.

### Eliminar profundidad para simplificar
Descartado: la profundidad jurídica es una fortaleza y parte del producto.

### Mantener un único layout de cards y variar copy
Descartado: perpetúa equivalencia visual entre funciones distintas.

## Criterio de aceptación del ADR

ADR-006 se marca aceptado solo si la release v6 completa supera:
- 46/46 migración final;
- truth parity;
- 30 pasos;
- idempotencia;
- static validations;
- Browser E2E/axe;
- Lighthouse;
- Pages/smoke;
- Graphify;
- promoción stable.
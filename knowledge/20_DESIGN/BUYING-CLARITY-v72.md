# Meridiano Legal v7.2 — Buying Clarity

## Problema observable

La v7.1 resolvió la comprensión comercial de Home y hub, pero las fichas profundas todavía obligan al visitante a recorrer varias secciones antes de poder responder una pregunta básica: **¿qué estoy contratando exactamente?**

La información ya existe en los catálogos canónicos v4.1/v4.2: modalidad, duración, perímetro, entregables, requisitos, aceptación, límites y suplementos. v7.2 no reescribe la oferta; mejora su compresión y descubrimiento.

## Regla v7.2

**Una ficha comprable debe permitir entender el contrato operativo antes de leer toda la profundidad jurídica.**

Inmediatamente después del hero, cada ficha debe mostrar un resumen que responda:

1. ¿Qué modalidad estoy contratando?
2. ¿Cuánto dura o con qué cadencia opera?
3. ¿Cuál es el perímetro base?
4. ¿Qué entregables/resultados concretos recibo?
5. ¿Qué debe aportar el cliente para empezar?
6. ¿Cómo se verifica el cierre o continuidad?
7. ¿Qué ocurre si la necesidad excede el perímetro?

## Fuente de verdad

Exclusivamente:

- `catalog-products-v41/*.json`;
- `catalog-services-v42/*.json`.

Campos consumidos:

- `type`;
- `title`;
- `duration`;
- `modality`;
- `audience`;
- `perimeter`;
- `deliverables`;
- `requirements`;
- `acceptance`;
- `supplements`;
- `limits` cuando sea necesario para boundary.

No introducir cifras, precios, alcances, SLA, integraciones o capacidades que no estén en estas fuentes.

## Nuevo bloque: Resumen de contratación

Ubicación: inmediatamente después del hero de cada una de las 16 fichas y antes de Resultado/Pregunta de gobierno.

### Cabecera

Eyebrow: `RESUMEN DE CONTRATACIÓN`

Título: **Antes de entrar al detalle, esto es lo que está contratando.**

Lead: **Una lectura ejecutiva del alcance estándar. La propuesta final confirma perímetro, responsables, exclusiones y cualquier ampliación.**

### Banda principal

- **Modalidad** → `modality`.
- **Horizonte** → `duration`.
- **Dirigido a** → `audience`.

### Perímetro base

Mostrar hasta los primeros cuatro ítems de `perimeter`, respetando orden canónico. No resumir cifras ni alterar límites.

CTA contextual: `Ver perímetro completo → #v6-perimeter`.

### Entregables clave

Mostrar hasta los primeros cuatro títulos de `deliverables`, con su cantidad exacta (`1`, `Hasta 6`, etc.). El detalle descriptivo continúa en la sección completa.

CTA contextual: `Ver todos los entregables → #v6-deliverables`.

### Para empezar

Mostrar los primeros dos requisitos de `requirements` como condiciones de inicio.

CTA contextual: `Ver condiciones para empezar → #v6-engagement` cuando la sección exista.

### Cierre / verificación

Mostrar los primeros dos criterios de `acceptance`.

En productos, lenguaje de cierre: `Cómo sabemos que el producto terminó correctamente`.

En servicios, lenguaje de operación: `Cómo verificamos que la prestación está funcionando dentro del alcance`.

### Si la necesidad crece

Mostrar hasta dos `supplements` como rutas naturales de ampliación o continuidad.

No presentarlos como incluidos en el alcance base.

## UX

### Desktop

- resumen editorial de dos columnas;
- banda superior de 3 metadatos;
- perímetro y entregables como bloques principales;
- requisitos/cierre/ampliación en una franja secundaria;
- sin tarjetas SaaS ni mosaicos excesivos.

### Mobile

- apilado en orden de decisión: modalidad → perímetro → entregables → inicio → cierre → ampliación;
- sin scroll horizontal;
- cantidades y límites visibles antes del CTA.

## Navegación

Añadir `Qué contrata` como primer enlace del nav sticky de ficha, apuntando a `#v72-buying-summary`.

El resto de la ficha permanece disponible y no se elimina:

- Resultado/Decisión;
- Entregables;
- Perímetro;
- Proceso;
- Para empezar;
- Límites;
- Profundidad.

## Hero

La CTA secundaria debe priorizar la comprensión de compra:

`Ver qué incluye → #v72-buying-summary`.

La CTA primaria sigue usando el handoff comercial canónico existente.

## Centro Demo — fase 2 de v7.2

Después de certificar el resumen de contratación en las 16 fichas, integrar una capa de demostración estrictamente demostrativa:

- mostrar cómo podría verse un tablero, expediente, matriz o flujo cuando exista artefacto demo correspondiente;
- etiquetar siempre `DEMO` / `EJEMPLO ILUSTRATIVO`;
- nunca presentar Meridiano Empresas como capability productiva si no está habilitada;
- no convertir el demo en requisito para entender alcance o contratar.

## No objetivos

- no modificar los 8 productos + 8 servicios canónicos en esta primera fase;
- no crear nuevas tarifas;
- no cambiar precios existentes de Home;
- no prometer software, portal, CLM, CRM, firma, pagos, agenda, upload o monitoreo automático;
- no añadir nuevas capacidades a Legal Intelligence;
- no ocultar límites materiales en disclosure;
- no eliminar profundidad jurídica existente;
- no degradar accesibilidad, responsive, SEO, funnel o trazabilidad.

## Criterio de aceptación

Sin hacer scroll por toda la ficha, un visitante debe poder explicar:

1. qué modalidad está contratando;
2. cuánto dura;
3. las principales cantidades del perímetro;
4. los entregables principales;
5. qué debe aportar para empezar;
6. cómo se valida cierre/operación;
7. cómo se amplía la necesidad;
8. dónde consultar el detalle completo.

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

Ubicación: inmediatamente después del hero de cada una de las 16 fichas y antes del nav sticky y del contenido profundo.

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

**No se añade un segundo enlace a `#v6-engagement`.** El resumen hace visibles los requisitos y el nav sticky conserva la única ruta canónica a la sección completa “Para empezar”.

### Cierre / verificación

Mostrar los primeros dos criterios de `acceptance`.

En productos: `Cómo se verifica el cierre`.

En servicios: `Cómo se verifica la prestación`.

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
- cantidades y límites visibles antes del siguiente paso.

## Compatibilidad de navegación y hero

En la **fase 1 certificable** se preservan el hero y el nav sticky existentes. El resumen vive entre ambos y fuera del `<main>` reconstruido por el materializador v6.

Esto permite que:

- el builder histórico vuelva a materializar la ficha sin borrar Buying Clarity;
- no se duplique la navegación a `#v6-engagement`;
- la CTA primaria conserve el handoff comercial canónico;
- las CTAs secundarias históricas sigan apuntando a perímetro o límites según la oferta.

Una modificación futura del hero/nav solo se considerará después de certificar esta capa y si mejora la decisión sin romper contratos históricos.

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

Sin recorrer toda la ficha, un visitante debe poder explicar:

1. qué modalidad está contratando;
2. cuánto dura;
3. las principales cantidades del perímetro;
4. los entregables principales;
5. qué debe aportar para empezar;
6. cómo se valida cierre/operación;
7. cómo se amplía la necesidad;
8. dónde consultar el detalle completo.

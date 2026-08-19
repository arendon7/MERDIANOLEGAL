# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.2 — Buying Clarity / fichas profundas y Centro Demo.**

Rama: `feat/v720-buying-clarity`.

Baseline certificado: **v7.1.0 — Commercial Clarity**, con `main == stable == 0a01942c9a2b7868768e0b454af5a600c65ad01a` al abrir esta ola.

## Problema observable

La v7.1 permite entender mejor desde Home dónde encaja una necesidad y cómo puede intervenir Meridiano. Sin embargo, las 16 fichas profundas todavía distribuyen la información de compra entre Resultado/Decisión, Encaje, Entregables, Perímetro, Proceso, Condiciones, Límites y Profundidad.

La información material existe y es sólida en los catálogos canónicos; el problema es de compresión y descubrimiento.

## Hipótesis v7.2

Una ficha debe permitir comprender **qué se contrata exactamente** antes de recorrer toda la profundidad jurídica.

Añadir inmediatamente después del hero un **Resumen de contratación** construido exclusivamente desde los catálogos v4.1/v4.2.

Debe responder de forma visible:

1. modalidad;
2. duración/cadencia;
3. destinatario;
4. principales cantidades del perímetro;
5. principales entregables;
6. requisitos para empezar;
7. criterios de cierre o verificación de prestación;
8. rutas de ampliación/continuidad.

## Fuente de verdad

- `catalog-products-v41/*.json`;
- `catalog-services-v42/*.json`;
- `knowledge/20_DESIGN/BUYING-CLARITY-v72.md`;
- `assets/data/v7/buying-clarity-v72.json`.

No modificar inicialmente el contenido canónico de los 8 productos + 8 servicios.

## Implementación fase 1

- integrar el resumen en las 16 fichas mediante el materializador canónico, no parches manuales;
- añadir `Qué contrata` como primer enlace del nav sticky;
- orientar la CTA secundaria del hero a `#v72-buying-summary`;
- mantener intactas las secciones profundas existentes;
- preservar el handoff comercial canónico de la CTA primaria;
- validar idempotencia, responsive, axe y capability truth.

## Implementación fase 2

Una vez certificada la fase 1, mejorar el **Centro Demo** para conectar artefactos demostrativos con resultados/entregables de las fichas, siempre con etiquetado explícito `DEMO` y sin presentar Meridiano Empresas como capability productiva no habilitada.

## Capability truth preservado

- Meridiano Legal permanece como marca madre;
- Legal Intelligence continúa como capa transversal;
- seis rutas públicas permanecen intactas;
- 8 productos + 8 servicios permanecen como verdad contractual;
- no crear SaaS, CLM, CRM, portal, firma, pagos, agenda, upload o monitoreo automático implícito;
- Meridiano Counsel permanece fuera de oferta pública;
- no introducir tarifas nuevas sin pricing truth aprobado.

## Criterio de aceptación fase 1

En la parte superior de cualquiera de las 16 fichas, sin recorrer toda la página, el visitante debe poder explicar:

1. qué modalidad contrata;
2. cuánto dura;
3. qué cantidades principales cubre;
4. qué entregables principales recibe;
5. qué debe aportar para empezar;
6. cómo se valida cierre/operación;
7. cómo puede ampliarse el alcance;
8. dónde consultar el detalle completo.

## Estado

- baseline v7.1 certificado y `main == stable` confirmado;
- rama v7.2 creada desde baseline certificado;
- brief Buying Clarity creado;
- contrato source-driven v7.2 creado;
- pendiente: materializador, CSS, validator, materialización 16/16, E2E/axe y PR draft.

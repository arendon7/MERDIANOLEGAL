# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.2 — Buying Clarity / fichas profundas y Centro Demo.**

Rama: `feat/v720-buying-clarity`.

PR: `#174` — temporalmente cerrado durante rematerialización; reabrir sobre SHA limpio para regresión final.

Baseline certificado: **v7.1.0 — Commercial Clarity**, con `main == stable == 0a01942c9a2b7868768e0b454af5a600c65ad01a` al abrir esta ola.

## Problema observable

La v7.1 permite entender mejor desde Home dónde encaja una necesidad y cómo puede intervenir Meridiano. Sin embargo, las 16 fichas profundas todavía distribuían la información de compra entre Resultado/Decisión, Encaje, Entregables, Perímetro, Proceso, Condiciones, Límites y Profundidad.

La información material ya existía en los catálogos canónicos; el problema era de compresión y descubrimiento.

## Solución fase 1

Cada una de las 16 fichas incorpora inmediatamente después del hero un **Resumen de contratación** construido exclusivamente desde los catálogos v4.1/v4.2.

Hace visible:

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

No se modifica el contenido canónico de los 8 productos + 8 servicios.

## Decisión de compatibilidad

La fase 1 **preserva hero y nav sticky históricos**.

El resumen se materializa entre hero y nav y fuera del `<main>` reconstruido por v6. Esta ubicación permite que el builder histórico vuelva a materializar las fichas sin borrar Buying Clarity.

Además:

- no se añade un segundo enlace a `#v6-engagement`;
- el nav sticky conserva la única navegación canónica a “Para empezar”;
- la CTA primaria conserva el handoff existente;
- las CTAs secundarias históricas permanecen intactas;
- el resumen enlaza únicamente a Perímetro y Entregables para profundización directa.

## Implementación fase 1

- materializador idempotente: `scripts/apply_buying_clarity_v72.py`;
- validador source-truth: `scripts/validate_buying_clarity_v72.py`;
- superficie visual: `assets/css/v7/buying-clarity-v72.css`;
- gate dedicado: `.github/workflows/v72-buying-clarity-candidate.yml`;
- E2E: `tests/e2e/buying-clarity-v72.spec.mjs`;
- materialización: 16/16 fichas;
- contraste de superficie clara ajustado mediante token tipográfico oscuro;
- supplements visibles pero expresamente fuera del alcance base salvo pacto.

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
- brief y contrato source-driven implementados;
- CSS/materializador/validator/E2E/gate implementados;
- 16/16 fichas materializadas;
- primer ciclo detectó dos incompatibilidades: duplicación de `#v6-engagement` y gobernanza incompleta del workflow;
- ambas fuentes corregidas sin relajar validadores históricos;
- rematerialización posterior completada y workflow temporal eliminado;
- pendiente: reabrir PR #174 y cerrar toda la regresión sobre un único SHA final antes de merge.

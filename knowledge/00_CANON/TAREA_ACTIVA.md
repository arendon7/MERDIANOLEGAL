# Meridiano Legal — Tarea activa

Actualizado: 2026-08-19.

## Frente vigente

**v7.2 — Buying Clarity / fichas profundas y Centro Demo.**

Rama: `feat/v720-buying-clarity`.

PR: `#174` — draft; en regresión final same-SHA.

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

El resumen se materializa entre hero y nav y fuera del `<main>` reconstruido por v6. `scripts/normalize_experience_compat_v60.py` reaplica y valida Buying Clarity después de las normalizaciones históricas.

Además:

- `apply_buying_clarity_v72.py` no consume saltos de línea vecinos al normalizar su stylesheet;
- `apply_engagement_clarity_v63.py` preserva una hoja v6.3 ya correctamente situada antes de `tokens.css`, evitando drift cosmético frente a capas posteriores;
- no se añade un segundo enlace a `#v6-engagement`;
- el nav sticky conserva la única navegación canónica a “Para empezar”;
- la CTA primaria conserva el handoff existente;
- las CTAs secundarias históricas permanecen intactas;
- el resumen enlaza únicamente a Perímetro y Entregables para profundización directa.

## Implementación fase 1

- materializador idempotente: `scripts/apply_buying_clarity_v72.py`;
- validador source-truth: `scripts/validate_buying_clarity_v72.py`;
- integración con normalizador canónico: `scripts/normalize_experience_compat_v60.py`;
- compatibilidad de composición v6.3: `scripts/apply_engagement_clarity_v63.py`;
- superficie visual: `assets/css/v7/buying-clarity-v72.css`;
- gate dedicado: `.github/workflows/v72-buying-clarity-candidate.yml`;
- E2E: `tests/e2e/buying-clarity-v72.spec.mjs`;
- materialización: 16/16 fichas;
- supplements visibles pero expresamente fuera del alcance base salvo pacto.

## Boundary final fase 1

Comparado contra el baseline certificado, la ola queda limitada a **26 archivos permanentes**:

- 16 fichas HTML materializadas;
- contrato y brief v7.2;
- CSS v7.2;
- materializador y validador v7.2;
- integración del normalizador canónico;
- compatibilidad de composición en el materializador v6.3, sin alterar truth jurídico;
- E2E;
- workflow candidato;
- tarea activa.

No quedan workflows temporales ni cambios en Home, hub de Soluciones, precios o catálogos canónicos.

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
- brief y contrato source-driven implementados;
- CSS/materializador/validator/E2E/gate implementados;
- 16/16 fichas materializadas;
- duplicación inicial de `#v6-engagement` corregida;
- Buying Clarity integrado al normalizador canónico;
- composición de stylesheets v6.3/v6.4/v7.2 endurecida sin cambiar contenido jurídico;
- canonicalización fuerte validó simultáneamente Engagement, Fit & Scope y Buying Clarity;
- boundary final limpio: 26 archivos permanentes, cero workflows temporales;
- pendiente: cerrar todos los workflows aplicables sobre un único SHA normal de contenido, marcar PR #174 ready y promover v7.2 siguiendo Builder → Pages → snapshot `stable`.

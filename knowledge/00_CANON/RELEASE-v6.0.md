# Release v6.0 — Experience System

Fecha de apertura: 2026-08-17
Estado: **candidate / implementación activa**.

## Problema

v5.31 redujo correctamente la profundidad visible de forma simultánea, pero el sistema público conserva una arquitectura de presentación sedimentada y una primera lectura excesivamente orientada a la taxonomía interna de Meridiano.

El problema observable se resume en cuatro frentes:
1. costo cognitivo de entrada;
2. equivalencia visual de funciones semánticas distintas;
3. deuda de cascada/materializadores históricos;
4. mobile/contacto todavía más complejos de lo necesario a nivel perceptual.

## Resultado esperado

Una experiencia jurídica client-first en la que un visitante pueda identificar rápidamente:
- qué tipo de decisión ayuda a resolver Meridiano;
- qué resultado jurídico/operativo puede recibir;
- cómo se estructura el trabajo;
- qué evidencia/perímetro/límites puede verificar;
- qué debe hacer para avanzar.

Y pueda profundizar sin pérdida en:
- fundamento jurídico;
- método;
- responsabilidades;
- aceptación/cierre;
- drivers de alcance;
- alternativas;
- evidencia y contexto.

## Scope

### Wave 0 — Foundations
- tokens normalizados;
- shell/header/footer;
- primitives y componentes semánticos;
- renderer/materializer v6;
- version gates legacy;
- validators v6.

### Wave 1 — Pilotos
- Home desktop/mobile;
- Auditoría Jurídica Empresarial Integral desktop/mobile;
- Tecnología e Inteligencia Artificial desktop/mobile;
- contacto/handoff.

### Wave 2 — Fichas
- 8 productos;
- 8 servicios.

### Wave 3 — Soluciones
- índice + 6 rutas.

### Wave 4 — Sectores
- 8 superficies.

### Wave 5 — Perspectivas
- 6 perspectivas + hub.

### Wave 6 — Resto
- firma;
- experiencia/demo;
- legales;
- 404;
- shell final global.

## Non-goals

- backend;
- cuentas/auth;
- CRM;
- pagos;
- e-signature;
- upload;
- portal real;
- SPA/framework migration;
- precios nuevos no aprobados;
- claims/clientes/resultados no verificables;
- eliminación de profundidad jurídica;
- nueva fuente production sin evaluación expresa;
- motion decorativo como sustituto de IA.

## Truth boundaries

Fuentes v5.x siguen siendo autoridad para:
- catálogos;
- offer narrative;
- offer commercial;
- capability truth;
- funnel/handoff;
- profesional authority;
- límites, cantidades, entregables, cierres y alternativas.

v6 puede cambiar su **jerarquía y representación**, no su significado sin una decisión jurídica/comercial explícita.

## Structural contract

Final de release:
- 46 HTML;
- 16 fichas profundas;
- 8 productos + 8 servicios;
- 7 soluciones;
- 8 sectores;
- 6 perspectivas internas;
- 1 formulario físico;
- WhatsApp manual;
- 30 pasos builder;
- static-first.

## Design contract

- una función semántica = un tratamiento visual reconocible;
- menos cardification;
- un CTA primario por estado;
- mobile diseñado, no solo apilado;
- demo como evidencia secundaria;
- profundidad bajo disclosure nativo cuando sea secundaria;
- límites visibles y sobrios;
- typography/space/rules/indexes como gramática principal.

## Technical contract

- no sumar hoja `v600.css` encima de todo el legacy como arquitectura final;
- renderer source-driven;
- CSS consolidado por responsabilidad;
- JS runtime solo donde exista estado real;
- legacy materializers version-gated/no-op/delegation cuando sean absorbidos;
- no paso 31;
- idempotencia dos pasadas.

## QA contract

Piso mínimo heredado de v5.31:
- static validations sin regresión;
- Browser E2E/axe sin regresión;
- serious/critical axe 0 en cobertura;
- Lighthouse budgets vigentes;
- Pages + smoke;
- Graphify alineado;
- stable solo al final.

Nuevas validaciones:
- truth parity;
- CSS allowlist/legacy exceptions;
- único formulario;
- no PII/persistencia;
- no fake capability;
- first-layer hierarchy;
- reduced motion cuando motion se incorpore.

## Rollback

`stable` permanece en v5.31 hasta cierre completo. Ninguna wave parcial se promueve a stable.

## Evidencia de diseño

Discovery y prototipos aprobados para implementación se encuentran en `knowledge/20_DESIGN/` y en Figma `Meridiano Legal — Rediseño post-v5.31`.

## Estado de ADR

ADR-006 permanece propuesto durante implementación y solo se acepta en cierre certificado.
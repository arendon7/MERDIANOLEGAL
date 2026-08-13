# Meridiano Legal — Tarea activa

Actualizado: 2026-08-13.

## Release candidata

**v5.23.0 — compresión del contacto comercial.**

Rama: `feature/v523-contact-compression`.

`stable` permanece en el snapshot público certificado v5.22: `dcb5bc9643eff595c0f8614c7cf6acbadc3bb719`.

## Problema observable

La auditoría posterior a v5.22 confirma que la profundidad de oferta y la veracidad de capacidades ya están resueltas. El principal cuello de botella visible está en el tramo final de conversión de la portada.

Antes del formulario, la página ya explica la secuencia necesidad → calificación → propuesta → aceptación/inicio. Dentro del mismo formulario vuelven a aparecer superficies separadas para:

1. calificación comercial y resumen;
2. brief de modalidad/prueba;
3. recomendación y siguiente paso;
4. ruta de solicitud a propuesta;
5. condiciones de aceptación e inicio;
6. handoff manual a WhatsApp.

v5.19 repliega la ruta completa y las condiciones de inicio para ciertas intenciones, pero la calificación, el resumen, el brief y la recomendación siguen compitiendo visualmente con los campos que el usuario debe completar.

La lógica subyacente no necesita ampliarse: los scripts v5.9, v5.10, v5.13, v5.14 y v5.15 ya calculan necesidad, momento, horizonte, modalidad, encaje, ruta y CTA sin scoring, persistencia ni transporte adicional.

## Objetivo

Reducir la carga cognitiva del contacto sin perder información jurídica material, continuidad comercial ni capacidad de auditoría.

La experiencia visible debe quedar en una secuencia corta:

1. datos de contacto y necesidad;
2. tres datos de contexto comercial: momento, horizonte y presupuesto opcional;
3. una única síntesis dinámica con necesidad, modalidad cuando exista, siguiente paso y estándar verificable;
4. un único disclosure opcional con límites, ruta a propuesta y condiciones de aceptación/inicio;
5. contexto general, privacidad y CTA a WhatsApp;
6. handoff manual posterior, solo cuando el usuario lo prepara.

## Contrato v5.23

- Una sola superficie visible de síntesis comercial dentro del formulario.
- Una sola superficie opcional para proceso, límites y condiciones de inicio.
- No duplicar visualmente el proceso que ya aparece en `#contratacion`.
- Mantener los mismos campos físicos del formulario; no añadir PII ni preguntas nuevas.
- Mantener `decision_stage`, `urgency`, `budget`, `need`, modalidad, proof standard, recommendation y close route como estado verificable.
- Reutilizar los `data-*` históricos cuando sea posible para conservar comportamiento y trazabilidad.
- No ocultar contenido material mediante CSS: la compresión debe expresarse en HTML semántico y progressive disclosure accesible.
- La intención explícita `proposal` puede abrir más detalle, pero no debe desplegar múltiples paneles redundantes.
- En móvil y escritorio debe existir la misma jerarquía conceptual.

## No objetivos

- no cambiar productos, servicios, planes, precios u honorarios;
- no construir CRM, backend, agenda, firma, pagos o portal real;
- no introducir scoring, inferencia automática ni IA de recomendación;
- no almacenar PII ni respuestas del formulario;
- no automatizar el envío de WhatsApp;
- no modificar retrospectivamente v5.22;
- no reducir cobertura ni relajar budgets;
- no hacer una refactorización general de los 72 scripts Python o 25 fuentes JS dentro de este ciclo.

## Criterios de cierre

1. el formulario conserva una única instancia física;
2. los campos actuales siguen funcionando y la privacidad no se degrada;
3. calificación + brief + recomendación se presentan como una sola síntesis visible;
4. ruta a propuesta + aceptación/inicio se presentan dentro de un único disclosure opcional;
5. el CTA continúa adaptándose a la ruta existente sin automatizar la decisión;
6. el handoff v5.17 y observabilidad v5.18 permanecen intactos;
7. contratos v5.8→v5.22: PASS;
8. validator nuevo v5.23: PASS;
9. builder + segunda pasada/idempotencia: PASS;
10. Pages + smoke: PASS;
11. Browser E2E + axe: al menos 49 pruebas observadas, sin reducir cobertura y con las 7 superficies axe;
12. Lighthouse: 6/6 dentro de budgets vigentes;
13. release-health: PASS;
14. `stable` solo se mueve después de todos los gates verdes;
15. Graphify fresco antes del cierre documental.

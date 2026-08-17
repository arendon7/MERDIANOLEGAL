# Meridiano Legal — Initial Post-v5.31 Redesign Backlog

Estado: discovery backlog, no release abierta
Fecha: 2026-08-17

Este backlog no autoriza implementación automática. Cada ítem debe pasar por auditoría, evidencia y contrato antes de convertirse en una release.

## P0 — arquitectura y sistema

### R01 — navegación client-first
Problema a verificar: la navegación pública expone la taxonomía interna (necesidades, servicios, productos, planes, sectores, demo) antes de que el cliente formule claramente su problema.

Hipótesis: priorizar problemas/decisiones y reducir opciones de primer nivel puede disminuir carga cognitiva sin perder profundidad.

### R02 — consolidación del sistema visual
Problema a verificar: la portada y fichas cargan múltiples generaciones de CSS/componentes, señal de sedimentación y riesgo de incoherencia visual/mantenimiento.

Hipótesis: consolidar tokens, tipografía, spacing, components y states puede mejorar consistencia sin alterar truth/content.

### R03 — jerarquía editorial vs. cardification
Problema a verificar: varias superficies recurren repetidamente a grids de cards con peso visual similar para contenidos de distinta importancia.

Hipótesis: una gramática más editorial —texto, diagramas, timelines, tablas, pull quotes, listas y cards solo cuando aporten— puede aumentar jerarquía y percepción premium.

## P1 — recorridos comerciales

### R04 — hero y above-the-fold
Problema a verificar: el hero comunica posicionamiento con solvencia, pero puede condensar más claramente problema, resultado y diferenciador antes de presentar el ecosistema completo.

### R05 — demo como CTA secundario
Problema a verificar: `Centro demo`/`Demo de cliente` tienen presencia fuerte en header/mobile y podrían competir con el objetivo de presentar una necesidad.

Hipótesis: reencuadrar demo como prueba de método / cómo trabajamos, en un nivel secundario, puede mejorar el foco comercial.

### R06 — formulario y contacto
Problema a verificar: la arquitectura jurídica/comercial alrededor del formulario es rigurosa pero puede seguir siendo demasiado visible para una tarea simple de contacto.

Hipótesis: mantener todas las garantías y estados en el sistema, mostrando solo la información necesaria en cada momento.

## P1 — fichas profundas

### R07 — primera pantalla de ficha
Problema a verificar: la primera pantalla tiene título, summary, meta y CTA correctos, pero el recorrido inmediatamente posterior todavía expone varias taxonomías comerciales antes de entregables y método.

Hipótesis: ordenar `problema/resultado → encaje → qué recibe → cómo trabajamos → límites/contratación → fundamento` puede mejorar comprensión.

### R08 — copy client-language
Problema a verificar: parte del copy explica la arquitectura de modalidades de Meridiano en vez de comenzar desde situaciones que el cliente reconoce.

Hipótesis: reescribir la primera capa en lenguaje de problema/decisión manteniendo intacta la profundidad jurídica mejora relevancia y conversion intent.

## P1 — mobile

### R09 — mobile density
Problema a verificar: aunque no existe overflow global y hay scroll decks, mobile puede conservar demasiada densidad, secuencias largas de cards y navegación secundaria.

Hipótesis: diseñar la jerarquía específicamente para mobile, en vez de solo apilar desktop, mejora scanning y decisión.

## P2 — confianza y autoridad

### R10 — seniority verificable
Problema a verificar: la web es prudente con claims, pero puede mostrar seniority de manera más fuerte con metodología, artefactos, experiencia profesional verificable y muestras de trabajo sin inventar clientes/resultados.

### R11 — sectores y perspectivas
Problema a verificar: hoy funcionan principalmente como profundidad posterior al contacto. Pueden evolucionar a activos editoriales de autoridad y SEO sin competir con el funnel principal.

## P2 — interacción

### R12 — motion con significado
Problema a verificar: la experiencia es funcional pero tiene margen para microinteracciones de estado, continuity y feedback.

Restricción: motion solo si explica causalidad/estado y siempre con reduced-motion, performance y accesibilidad.

## Muestra piloto propuesta

Antes de propagar cualquier rediseño:
1. `index.html` / Home.
2. `productos/diagnostico-juridico-empresarial.html`.
3. `servicios/tecnologia-inteligencia-artificial.html` o `servicios/contratacion-estrategica.html`.
4. contacto en Home.
5. mobile de esas superficies.

## Skills/lentes para la auditoría inicial

- Impeccable: auditoría holística.
- Taste Skill: dirección visual / anti-generic / density.
- Microsoft Frontend Design Review: crítica independiente.
- Vercel Web Design Guidelines: web/accessibility constraints.
- UI Craft: tokens / anti-slop / acceptance.
- Emil + Make Interfaces Feel Better: solo después de resolver IA/copy/layout.

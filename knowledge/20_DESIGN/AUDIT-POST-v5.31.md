# Auditoría de Experiencia post-v5.31 — Meridiano Legal

Fecha: 2026-08-17
Rama de trabajo: `audit/post-v531-experience`
Baseline técnico: `5fdca20b3837eab9ea2b2341b3d239660f48562f`
Baseline público certificado: v5.31.0 (`stable` permanece en el snapshot público certificado previo al tooling de diseño)
Estado: discovery / auditoría. **No abre v5.32 ni v6.0.**

## 1. Propósito

Evaluar Meridiano Legal como producto y experiencia de decisión, no como suma de releases históricas. El objetivo es identificar fricciones observables en arquitectura de información, copy, jerarquía visual, responsive, contacto y mantenimiento del sistema visual antes de aprobar una nueva release funcional.

## 2. Lentes aplicadas

### Lente primaria — Impeccable
Jerarquía, arquitectura de información, carga cognitiva, responsive, formularios, estados y claridad del recorrido.

### Dirección / anti-generic — Taste Skill
Cardification, densidad, monotonía de composición, predictibilidad de layouts y diferenciación visual apropiada para una firma jurídica premium.

### Restricciones — Web Design Guidelines
Semántica, accesibilidad, keyboard, responsive, forms, foco y prácticas web.

### Crítica independiente — Microsoft Frontend Design Review
Confianza, craft, frictionless UI y coherencia sistémica.

### Reservadas para fase posterior
- Emil Design Engineering: motion y microinteracciones, solo después de resolver IA/copy/layout.
- Make Interfaces Feel Better: polish tardío.
- UI Craft: consolidación de tokens/componentes y acceptance bar.

## 3. Lo que ya está bien y debe preservarse

1. **Profundidad jurídica real.** Las fichas no son marketing vacío: muestran decisión, perímetro, entregables, método, responsabilidades, límites y criterios de cierre.
2. **Truthfulness.** Se diferencia demo de portal real; no se inventan clientes, resultados o capacidades.
3. **Contratación explícita.** v5.30 dejó claras unidad de contratación, variables de alcance y cierre verificable.
4. **Compresión decisional válida.** v5.31 usa `<details>/<summary>` nativo para profundidad secundaria sin eliminar contenido del DOM.
5. **Accesibilidad y QA maduros.** Playwright/axe/Lighthouse y contratos históricos funcionan como gates, no como decoración.
6. **Mobile sin overflow global.** Existen soluciones específicas como scroll-snap y CTA móvil.
7. **Identidad reconocible.** Navy, marfil, dorado, serif/sans y tono editorial ya forman una base coherente con el posicionamiento.

El rediseño no debe destruir estas fortalezas para obtener novedad visual.

## 4. Hallazgos prioritarios

### P0 — H1. Sedimentación del sistema visual

**Evidencia:** la portada carga múltiples generaciones de CSS —desde `site-v3.css` y `clarity-v31.css` hasta `funnel-trust-v529.css`— y las fichas profundas combinan `catalog-v32`, `detail-v46`, `decision-v58`, `proof-v512`, `offer-v522`, `offer-commercial-v530` y `decision-compression-v531`, entre otras.

**Problema observable:** aunque los gates están verdes, la coherencia visual depende de una cascada histórica de parches y capas. Esto aumenta costo de cambio, riesgo de especificidad y probabilidad de que dos componentes con funciones distintas terminen pareciéndose demasiado.

**Hipótesis:** consolidar tokens, patrones y componentes en una gramática visual única reducirá deuda y mejorará consistencia sin alterar contenido ni contratos.

**No solución:** crear `v532.css` para tapar el problema.

### P0 — H2. Cardification y equivalencia visual excesiva

**Evidencia:** `situation`, `scope`, `deliverable`, `requirement`, `related`, buying clarity, engagement router, servicios, productos y otros bloques recurren a tarjetas, grids, borders, radius o sombras. En las fichas, cinco cards de buying clarity son seguidas por tres cards de contratación antes de llegar a la profundidad técnica.

**Problema observable:** contenidos con jerarquía y función distintas reciben tratamientos visuales similares. El usuario debe leer etiquetas para entender la diferencia entre “qué compra”, “qué recibe”, “cómo se dimensiona”, “resultado”, “método” y “evidencia”.

**Hipótesis:** una gramática editorial con más variación semántica —listas indexadas, tablas, timelines, diagramas, extractos documentales, bandas, columnas y cards solo cuando aporten— hará más evidente qué es decisión, qué es evidencia y qué es profundidad.

### P0 — H3. Arquitectura todavía demasiado orientada a nuestra taxonomía

**Evidencia:** la navegación principal expone Necesidades, Servicios, Productos, Planes, Sectores y Firma; además aparecen modalidades (diagnóstico, auditoría, producto, especialista, recurrente), Centro demo y Demo de cliente.

**Problema observable:** un visitante puede verse obligado a comprender cómo Meridiano clasifica su trabajo antes de reconocer cómo resolver su propia situación.

**Hipótesis:** la primera navegación comercial debe partir de situaciones/decisiones del cliente; la taxonomía de servicios/productos puede seguir existiendo como estructura secundaria y SEO.

### P0 — H4. Profundidad conseguida, edición insuficiente

**Evidencia:** cada ficha ya contiene suficiente sustancia. La Auditoría Jurídica Empresarial, por ejemplo, comunica horizonte, perímetro, documentos, entrevistas, entregables, límites, unidad de contratación y cierre.

**Problema observable:** el usuario todavía procesa varias capas comerciales/taxonómicas antes de llegar al núcleo “qué me resuelven, qué recibo y cómo ocurre”.

**Hipótesis:** editar la primera capa al orden `problema → resultado → encaje → entregables → proceso → límites → siguiente paso` permitirá reconocer valor antes de consumir fundamento.

## 5. Hallazgos de prioridad alta

### P1 — H5. Demo compite con el objetivo comercial

`Centro demo` aparece como acción destacada en header y `Demo de cliente` también tiene protagonismo móvil. Es una prueba valiosa de método, pero no debería competir en el primer nivel con “Presentar necesidad”.

**Dirección:** reencuadrar como “Cómo trabajamos” / “Ver una experiencia de trabajo” o situarlo como evidencia secundaria.

### P1 — H6. Contacto jurídicamente riguroso pero perceptualmente pesado

La arquitectura preserva síntesis, modalidad, recomendación, proceso, estados de propuesta/aceptación/inicio y handoff manual. Esto es correcto en términos de capability truth, pero parte de esa complejidad puede sentirse como una tarea adicional antes de simplemente contactar.

**Dirección:** mantener todas las salvaguardas y estados, pero revelar solo lo necesario en el momento adecuado. El formulario debe sentirse corto incluso si el sistema alrededor es sofisticado.

### P1 — H7. Mobile resuelve overflow, no necesariamente densidad

Los decks horizontales de servicios/productos/sectores/planes evitan páginas interminables, pero siguen trasladando múltiples cards a un carrusel manual. En fichas, el patrón responsive convierte grids en largas secuencias verticales.

**Dirección:** diseñar una jerarquía mobile específica: menos elementos equivalentes por pantalla, resúmenes más decisionales, acceso explícito a “ver todos” cuando corresponda y no convertir cada desktop grid en carrusel o stack por defecto.

### P1 — H8. Jerarquía CTA susceptible de simplificación

En algunas superficies conviven Presentar necesidad, Ver cómo podemos ayudar, Centro demo, Demo de cliente, Volver al portafolio, Solicitar propuesta/Definir alcance, enlaces de TOC y WhatsApp.

**Dirección:** un CTA primario por estado de decisión; secundarios coherentes; WhatsApp como salida directa, no competencia constante.

## 6. Hallazgos de prioridad media

### P2 — H9. Seniority verificable puede comunicarse mejor

La firma ya presenta trayectoria y aclara que no es lista de clientes. Podemos elevar percepción de seniority mediante artefactos verificables: método, ejemplos de matrices/documentos ficticios claramente etiquetados, publicaciones, sectores, decisiones tipo y muestras de trabajo, sin inventar resultados.

### P2 — H10. Sectores y perspectivas pueden ser una capa editorial de autoridad

Hoy funcionan bien como profundidad posterior. Deben evolucionar hacia una biblioteca editorial con lenguaje visual propio, no más cards equivalentes al catálogo comercial.

### P2 — H11. Motion está subutilizado, pero no es prioridad actual

Hay espacio para feedback y continuidad en nav, filtros, disclosures y handoff. Sin embargo, añadir motion antes de resolver IA y jerarquía solo embellecería la sedimentación.

## 7. Auditoría por superficie

### Home

**Fortalezas:** hero claro, positioning serio, CTA a necesidad, señal de alcance, oferta profunda, autoridad, sectores y contacto.

**Fricciones:** demasiadas familias de contenido tienen peso similar; la secuencia obliga a navegar por varias taxonomías; el catálogo ocupa mucho espacio; el demo aparece demasiado pronto; el visitante puede perder el hilo “qué decisión vine a resolver”.

### Ficha de producto — Auditoría Jurídica Empresarial Integral

**Fortalezas:** perímetro y outputs concretos; horizonte visible; límites serios; cierre verificable; producto verdaderamente comprensible.

**Fricciones:** 5 cards de claridad + 3 cards de contratación + drivers + pregunta/resultado antes del detalle profundo. Hay claridad local, pero mucha estructura acumulada globalmente.

### Ficha de servicio — Tecnología e IA

**Fortalezas:** copy técnicamente sobrio; alcance adaptable; límites correctos frente a auditoría técnica/pentesting/certificación; buen TOC.

**Fricciones:** el servicio se presenta inicialmente a través de categorías de modalidad y contratación antes de hacer tangible la situación empresarial y la intervención. Mismo patrón visual de cards del producto pese a naturaleza distinta.

### Contacto

**Fortalezas:** un formulario, privacidad, sin upload, WhatsApp manual, no se presume aceptación o contratación.

**Fricciones:** el modelo de estados comerciales puede ocupar más atención que la tarea principal. Conviene diseñar “complejidad interna, simplicidad externa”.

### Mobile

**Fortalezas:** CTA fijo, no overflow, breakpoints y reduced motion.

**Fricciones:** muchas cards se transforman en scroll horizontal o stack; el volumen total sigue existiendo y exige navegación manual prolongada.

## 8. Arquitectura objetivo de experiencia

### Capa A — reconocer
1. Situación / problema.
2. Resultado que Meridiano puede ayudar a instalar.
3. Evidencia mínima de por qué confiar.
4. CTA único contextual.

### Capa B — decidir
1. Encaje / no encaje.
2. Qué recibe.
3. Cómo ocurre.
4. Tiempo / modalidad cuando sea relevante.
5. Límites principales.

### Capa C — verificar
1. Perímetro exacto.
2. Método.
3. Responsabilidades.
4. Criterios de aceptación/cierre.
5. Fundamento jurídico y evidencia.
6. Alternativas y FAQ.

### Capa D — profundizar
Sectores, perspectivas, firma, demo/metodología y material educativo.

## 9. Contrato de diseño para prototipo

El piloto debe demostrar, sin cambiar todavía producción:

1. Menos categorías simultáneamente visibles en first viewport.
2. Un único CTA primario por superficie/estado.
3. Diferencia visual inequívoca entre decisión, entregable, proceso y profundidad.
4. Reducción de cardification sin pérdida de información.
5. Mobile diseñado específicamente, no solo apilado.
6. Toda profundidad jurídica preservada y accesible.
7. Keyboard, focus, contrast y reduced motion desde prototipo.
8. Ningún claim nuevo sin fuente.
9. Ningún backend/capability ficticio.
10. No crear una nueva capa CSS versionada como estrategia principal.

## 10. Muestra piloto

- Home.
- Auditoría Jurídica Empresarial Integral.
- Tecnología e Inteligencia Artificial.
- Contacto de Home.
- Mobile de las cuatro superficies.

## 11. Decisión de versión

Aún no se decide entre v5.32 y v6.0.

**Criterio:** si la solución puede implementarse como edición de IA/copy/componentes conservando la gramática visual esencial, podría ser v5.32. Si exige consolidar el design system, cambiar navegación de primer nivel y reemplazar patrones transversales de las 46 superficies, debe evaluarse como v6.0 por cambio arquitectónico.

## 12. Próximo paso

Crear Design Brief objetivo + mapa IA actual/objetivo + prototipo editable de Home/producto/servicio/mobile. Someter el prototipo a crítica independiente antes de definir release funcional.

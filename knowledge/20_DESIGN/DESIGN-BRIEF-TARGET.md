# Design Brief objetivo — Meridiano Legal next experience

Fecha: 2026-08-17
Estado: target brief para prototipado; no es release.

## 1. Posicionamiento visual

**Firma jurídica estratégica, editorial y tecnológica.**

Meridiano debe sentirse senior, preciso y contemporáneo sin adoptar el lenguaje visual de un SaaS genérico ni el de una firma tradicional excesivamente solemne.

Referencias conceptuales, no imitativas:
- publicación jurídica/financiera de alta calidad;
- consultoría estratégica;
- design engineering sobrio;
- materialidad documental y evidencia;
- tecnología integrada como método, no como estética futurista.

## 2. Personalidad

- Precisa.
- Serena.
- Ejecutiva.
- Editorial.
- Técnica sin ser críptica.
- Premium sin ornamentación ostentosa.
- Digital sin estética “AI startup”.

## 3. Lo que se conserva

- Navy profundo como base de autoridad.
- Marfil como superficie editorial.
- Dorado cálido como acento escaso y funcional.
- Contraste serif/sans.
- Fotografía/territorio cuando aporte contexto.
- Líneas, índices, numeración y estructura documental.

## 4. Lo que debe reducirse

- Cards como contenedor universal.
- Pills/chips usados para metadata no esencial.
- Sombras repetidas.
- Radius aplicado indiscriminadamente.
- Grids con 4–5 columnas de igual peso.
- CTAs simultáneos con jerarquía comparable.
- Textos que explican nuestro sistema antes del problema del cliente.
- Componentes que parecen dashboard en una página editorial.

## 5. Gramática de composición

### Jerarquía editorial
Usar espacio, escala tipográfica, columnas, reglas, numeración y contraste de superficie para organizar la lectura.

### Componentes con semántica visual distinta

**Decisión:** statement amplio, alto contraste y poca ornamentación.

**Resultado/entregable:** lista estructurada o tabla clara, con cantidades cuando sean fuente canónica.

**Proceso:** timeline o secuencia indexada.

**Perímetro:** tabla/matriz legible, no necesariamente card.

**Límite:** banda o callout sobrio con alto contraste semántico.

**Evidencia:** documento, matriz, artefacto, cita metodológica o referencia verificable.

**Profundidad:** disclosure nativo cuando es secundaria.

**CTA:** acción única dominante y alternativa textual.

## 6. Densidad y varianza

- Densidad objetivo: media.
- Varianza visual: 5–6/10; suficiente para diferenciar capas, sin eclecticismo.
- Motion: 2–3/10 inicialmente.
- Radius: bajo y contextual; no convertir toda superficie en “soft cards”.
- Shadows: excepcionalmente, para capas flotantes o continuidad espacial; no como decoración de catálogo.

## 7. Tipografía

La tipografía debe hacer gran parte del trabajo visual.

- Display/heading serif: autoridad editorial y contraste.
- Sans: legibilidad, navegación, metadata y UI.
- Evitar incorporar nuevas fuentes externas hasta evaluar licencias, performance, fallback y coherencia.
- Aumentar contraste de escala entre título, deck, copy y metadata; reducir dependencia de cajas para jerarquía.

## 8. Home objetivo

### Above the fold
- Logo/navigation simplificada.
- Eyebrow breve.
- H1 orientado a decisión/resultado.
- Lead máximo 2–3 líneas desktop.
- CTA primario: presentar necesidad.
- CTA secundario: explorar cómo ayudamos.
- Evidencia compacta, no cuatro chips equivalentes si puede integrarse editorialmente.
- Visual/artefacto que comunique método, no imagen decorativa aislada.

### Situaciones
4–6 entradas redactadas desde problemas reconocibles, no desde nombres internos de servicios.

### Qué instala Meridiano
3–4 resultados/arquetipos de trabajo que hagan tangible la oferta.

### Cómo trabaja
Secuencia breve: comprender → delimitar → estructurar → implementar/acompañar → cerrar/recordar.

### Evidencia y autoridad
Método, alcance verificable, trayectoria, sectores, perspectivas y demo reencuadrada.

### Oferta completa
Servicios/productos/plans siguen disponibles, pero después de que el usuario comprenda la lógica.

### Contacto
Simple a primera vista; profundidad legal/comercial progresiva.

## 9. Ficha objetivo

### Hero
- Qué problema resuelve.
- Qué resultado instala.
- Horizonte/modalidad solo si ayudan a decidir.
- CTA contextual.

### “Encaja si”
2–4 señales reales, en formato editorial/diagnóstico.

### “Qué recibe”
Entregables visibles antes de la taxonomía comercial extensa.

### “Cómo trabajamos”
Timeline o secuencia.

### “Qué debe aportar el cliente”
Compacto y operativo.

### “Perímetro y cierre”
Tabla o matriz; precisión sin ocho cards.

### “Límites y alternativas”
Visible y sobrio.

### “Fundamento y profundidad”
Disclosure accesible con v5.22/v5.30 preservado cuando sea pertinente.

## 10. Mobile objetivo

- First viewport resuelve identidad, problema y CTA.
- Evitar más de una interacción horizontal principal por bloque.
- No depender de carruseles para descubrir contenido esencial.
- “Ver todos” cuando una biblioteca supera la capacidad de scanning.
- Toc compacto, con todas las rutas esenciales accesibles; no esconder enlaces arbitrariamente por `nth-child` sin alternativa.
- CTA fijo solo cuando no tape contenido ni compita con acciones de contexto.

## 11. Motion — guía inicial basada en design engineering

Aplazar motion decorativo. Cuando se incorpore:
- 120–220 ms para microfeedback;
- easing natural y consistente;
- animar transform/opacity preferentemente;
- entrada/salida con relación causal;
- focus/keyboard sin depender de animación;
- `prefers-reduced-motion` obligatorio;
- no scroll-jacking, parallax pesado ni storytelling que retrase la tarea.

## 12. Anti-patterns explícitos

No usar:
- gradientes púrpura/azul “AI”.
- glassmorphism generalizado.
- bento grids por moda.
- iconos genéricos para cada párrafo.
- números de métricas sin evidencia.
- testimonials ficticios.
- enormes titulares vacíos que sustituyan sustancia.
- animaciones de texto por letra.
- cards redondeadas con sombra como lenguaje dominante.

## 13. Criterio de éxito

El nuevo sistema debe lograr que un visitante pueda responder en segundos:
1. Qué tipo de problema resuelve Meridiano.
2. Qué resultado puede esperar comprar.
3. Qué diferencia su método.
4. Qué debe hacer para avanzar.

Y, si quiere profundizar, encontrar sin pérdida:
5. perímetro;
6. entregables;
7. método;
8. límites;
9. evidencia;
10. condiciones de contratación.

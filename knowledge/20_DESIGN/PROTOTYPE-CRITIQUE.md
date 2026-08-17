# Crítica del prototipo post-v5.31

Fecha: 2026-08-17
Estado: discovery. No abre release funcional.
Artefacto visual: Figma `Meridiano Legal — Rediseño post-v5.31`.

## 1. Resultado general

La dirección objetivo supera el problema principal identificado en v5.31: la profundidad jurídica sigue disponible, pero la primera lectura deja de parecer una acumulación de capas comerciales equivalentes.

Se valida provisionalmente una gramática común capaz de diferenciar:

- situación/decisión;
- resultado;
- entregable;
- proceso;
- perímetro;
- límite;
- evidencia;
- profundidad.

## 2. Home — hallazgos del render

### Validado

1. El hero comunica una sola promesa y una sola acción dominante.
2. La pieza de método a la derecha funciona mejor que una imagen decorativa como explicación del modelo de trabajo.
3. Las seis situaciones se leen como índice editorial, no como seis productos competidores.
4. Los cuatro resultados se distinguen de las situaciones y del proceso sin recurrir a cards con sombra.
5. El timeline de cinco pasos introduce método sin obligar a comprender modalidades comerciales.
6. La evidencia tiene un bloque de alto contraste y no se confunde con catálogo.
7. Las familias de oferta aparecen solo después de que el usuario ya reconoce necesidad y resultado.
8. El contacto funciona como cierre natural del recorrido.

### Ajustes pendientes

1. Revisar el H1 final para preservar contundencia sin exceder longitud en algunos anchos intermedios.
2. Evaluar si `Cómo podemos ayudar` y `Soluciones` son semánticamente redundantes en navegación.
3. El artefacto de método puede evolucionar desde lista tipográfica a diagrama/documento propio de Meridiano, sin volverlo ornamental.
4. La sección de evidencia debe usar únicamente elementos demostrables; no convertir conteos técnicos del sitio en claim comercial central si no aportan valor al comprador.
5. El formulario del prototipo es una simplificación visual. La implementación deberá conservar el único formulario canónico y sus contratos de privacidad/handoff.

## 3. Home mobile — hallazgos

### Validado

1. El primer viewport contiene identidad, decisión, lead y CTA.
2. No se necesita carrusel para descubrir contenido esencial.
3. Las situaciones se escanean naturalmente como lista.
4. Resultados, método y evidencia tienen tratamientos distintos.
5. El CTA final no compite permanentemente con múltiples acciones.

### Ajustes pendientes

1. Verificar tamaño real de targets y spacing con browser render, no solo Figma.
2. Resolver navegación móvil completa sin esconder arbitrariamente elementos por posición.
3. Decidir si el CTA fijo existente se conserva; la nueva jerarquía puede reducir su necesidad.

## 4. Auditoría Jurídica Empresarial — hallazgos

### Validado

1. El producto se percibe como producto cerrado antes de explicar su modalidad.
2. Los tres entregables funcionan mejor como expediente de salida que como tres cards.
3. La matriz de perímetro hace inmediatamente comprensibles 1 sociedad / hasta 8 entrevistas / hasta 60 documentos / 5–6 semanas.
4. Resultado y perímetro son visualmente distintos.
5. La banda de límites aporta confianza sin competir con el valor.
6. La profundidad jurídica/contractual queda accesible como segunda capa.

### Ajustes pendientes

1. El timeline del prototipo usa descriptores estructurales provisionales. Antes de implementación debe materializar exclusivamente el método canónico de la ficha.
2. La aceptación/cierre y drivers v5.30 deben mapearse a tabla/disclosure sin pérdida semántica.
3. El CTA final debe transportar contexto al formulario canónico sin afirmar aceptación ni contratación.

## 5. Tecnología e IA — hallazgos

### Validado

1. La ficha se siente distinta a Auditoría aunque comparte tokens y tipografía.
2. La pregunta ejecutiva funciona como eje conceptual y evita un segundo “inicio” de página posterior al hero.
3. `Inventario → clasificación → gobierno` crea una narrativa de sistema clara.
4. El perímetro `hasta 20 casos / hasta 8 proveedores / 1 matriz` es escaneable.
5. El cierre verificable aparece como estado operativo, no como promesa de cumplimiento absoluto.
6. La banda de límites técnicos es especialmente importante para capability truth.

### Ajustes pendientes

1. Incorporar en profundidad el régimen jurídico y fuentes sin hacer que compitan con la decisión inicial.
2. Evaluar cómo representar evaluaciones de impacto y gobierno recurrente cuando sean drivers, sin inventar una cuarta capa de producto.
3. Mantener explícito que alto impacto puede exigir especialistas adicionales.

## 6. Tipografía

El prototipo utiliza `Source Serif 4` como proxy editorial porque Figma no ofrece Georgia/Times en el entorno conectado.

Esto **no aprueba una nueva fuente para producción**. Antes de cualquier cambio tipográfico real se debe evaluar:
- licenciamiento;
- carga/performance;
- disponibilidad;
- fallback;
- CLS;
- coherencia con la marca actual.

Georgia/Times continúa siendo baseline técnico hasta una decisión explícita.

## 7. Motion

Todavía no se justifica animar el prototipo completo.

Aplicación posterior de lente Emil Design Engineering:
- feedback de hover/focus;
- expansión de disclosures;
- indicador de navegación/TOC;
- transición discreta de estados;
- posible progresión del artefacto de método.

No usar motion para compensar jerarquía o copy insuficientes.

## 8. Señal de alcance de release

Los prototipos no proponen un parche visual aislado. La dirección afecta:

- navegación de primer nivel;
- arquitectura de Home;
- orden de fichas profundas;
- semántica de componentes;
- sistema de tokens/componentes;
- responsive/mobile;
- tratamiento de contacto;
- posicionamiento del demo;
- consolidación de CSS histórica.

Por amplitud, el cambio **se parece más a una revisión arquitectónica de experiencia que a una v5.32 incremental**.

Recomendación provisional: tratar el siguiente ciclo como **candidato v6.0**, pero no abrir formalmente v6.0 hasta cerrar:
1. inventario de componentes/tokens actuales;
2. estrategia de consolidación CSS;
3. contrato de migración de las 46 superficies;
4. plan de pruebas/regresión;
5. baseline Lighthouse/axe/Playwright para comparar antes/después.

## 9. Go / no-go del prototipo

**GO para avanzar a arquitectura técnica de vNext.**

No se aprueba todavía publicación ni release. El siguiente paso es diseñar cómo implementar el sistema sin añadir otra capa `v532.css`, preservar materializadores/canon y mantener todos los gates existentes.
# Meridiano Legal — Design Skills Operating Model

Fecha: 2026-08-17
Estado: foundation / no functional release opened

## Objetivo

Incorporar criterio especializado de diseño, UX, design engineering, motion, accesibilidad y frontend craft al proceso de evolución de Meridiano Legal sin convertir skills externos en una nueva fuente de verdad del producto.

La meta no es producir más estilos. Es elevar la calidad de decisión de diseño y reducir la sedimentación de soluciones acumuladas.

## Lentes principales

### 1. Impeccable — auditoría UX/UI integral

Se usa como primera lente en rediseños mayores para revisar jerarquía, información, densidad, layout, responsive, formularios, estados, typography, spacing, motion y edge cases.

Meridiano lo usa para diagnosticar y criticar, no para sustituir el canon.

### 2. Taste Skill — dirección visual y disciplina anti-genérica

Se usa para leer el brief, definir dirección estética, calibrar varianza/motion/densidad y evitar patrones genéricos de frontend generado por IA.

En Meridiano su función principal es cuestionar composiciones previsibles y exceso de tarjetas, no imponer una estética ajena a una firma jurídica premium.

### 3. Emil Kowalski / Design Engineering — interacción y motion

Se usa cuando una interacción realmente necesita movimiento: entrada/salida, continuidad espacial, feedback, estado o causalidad.

No se usa para agregar motion ornamental a páginas editoriales.

### 4. Vercel Web Design Guidelines — revisión web y accesibilidad

Se usa en todo cambio visible para revisar semántica, navegación, formularios, estados, keyboard, responsive y buenas prácticas de interfaz web.

Su resultado complementa, pero no sustituye, Playwright + axe + Lighthouse.

### 5. Microsoft Frontend Design Review — crítica independiente

Se usa como lente posterior a implementación en cambios mayores. Debe revisar si el resultado es frictionless, crafted y trustworthy, además de coherente con el design system.

### 6. Make Interfaces Feel Better — polish

Se usa tarde, cuando arquitectura y copy ya están resueltos. Atiende detalles de tipografía, superficies, iconos, microinteracciones y performance-aware polish.

### 7. UI Craft — sistema y acceptance bar

Se usa especialmente durante consolidación del design system y como crítica determinista/estructurada de anti-slop, tokens y acabado.

No se convierte automáticamente en un gate de CI hasta fijar versión, validar ruido y acordar qué reglas corresponden al lenguaje Meridiano.

## Matriz de uso por fase

| Fase | Skills/lentes | Resultado esperado |
|---|---|---|
| Discovery | Impeccable + Taste | problemas, jerarquía, dirección visual |
| IA / journey | Impeccable + Microsoft review | arquitectura client-first y fricción reducida |
| Visual system | UI Craft + Taste + Impeccable | tokens, composición, gramática de componentes |
| Prototype | Taste + Impeccable | Home + producto + servicio + mobile |
| Motion | Emil + Make Interfaces Feel Better | motion justificado y sutil |
| Accessibility | Vercel guidelines + axe/Playwright | teclado, semántica, foco, forms, reduced motion |
| Critique | Microsoft + GPT Taste/UI Craft | crítica independiente antes del freeze |
| Release | contratos existentes | cero regresiones y certificación pública |

## Reglas de combinación

No mezclar todos los skills en una misma decisión sin propósito.

Cada iteración selecciona:
- una lente primaria;
- una lente de restricciones;
- opcionalmente una lente de crítica independiente.

Ejemplo — rediseño del hero:
- primaria: Taste;
- restricciones: Impeccable + canon Meridiano;
- motion, solo si aplica: Emil;
- verificación: Web Design Guidelines + E2E/a11y.

Ejemplo — formulario de contacto:
- primaria: Impeccable;
- restricciones: Web Design Guidelines + invariantes de privacidad/handoff;
- polish: Make Interfaces Feel Better;
- crítica: Microsoft Frontend Design Review.

## Principios específicos para Meridiano

### Editorial antes que dashboard

La web pública es una experiencia jurídica/comercial, no un panel operativo. Cards, chips, matrices y estados se usan cuando mejoran comprensión; no como contenedor por defecto.

### Jerarquía antes que disclosure

Progressive disclosure es válido para profundidad secundaria. No debe usarse para corregir una jerarquía que sigue siendo confusa cuando el usuario abre el contenido.

### Copy visible vs. fundamento

La primera capa habla desde el problema y resultado del cliente. La segunda demuestra método y entregables. La tercera conserva fundamento jurídico, supuestos, límites y evidencia.

### Motion como significado

Animar solo para explicar:
- aparición/desaparición;
- relación origen-destino;
- cambio de estado;
- feedback de interacción;
- continuidad de navegación.

### Mobile como superficie primaria

No aceptar un desktop elegante que se convierta en una lista interminable de cajas en mobile. La jerarquía debe rediseñarse, no únicamente apilarse.

## Protocolo de rediseño inicial

Antes de tocar masivamente las 46 páginas:

1. Auditar portada certificada v5.31.
2. Auditar una ficha de producto compleja: Auditoría Jurídica Empresarial Integral.
3. Auditar una ficha de servicio adaptable: Tecnología e Inteligencia Artificial o Contratación Estratégica.
4. Auditar el contacto en desktop y mobile.
5. Definir arquitectura objetivo.
6. Definir design tokens y gramática visual objetivo.
7. Crear prototipo de las superficies piloto.
8. Ejecutar crítica independiente.
9. Probar responsive, keyboard, reduced motion y axe.
10. Solo entonces definir el contrato de una eventual release funcional.

## Condición para abrir una nueva release

No basta con decir “el diseño se ve viejo” o “queremos modernizarlo”. Debe existir un problema observable y un contrato verificable, por ejemplo:

- navegación exige comprender taxonomía interna antes de formular una necesidad;
- exceso de componentes equivalentes reduce jerarquía visual;
- demasiadas hojas de estilo versionadas dificultan coherencia y mantenimiento;
- CTA demo compite con el objetivo comercial principal;
- mobile conserva demasiada densidad aunque no tenga overflow;
- las fichas profundas obligan a procesar más categorías de las necesarias antes de reconocer qué se compra.

Solo después de medir y documentar esos problemas se decide si corresponde v5.32 o una v6.0 de sistema visual/IA.

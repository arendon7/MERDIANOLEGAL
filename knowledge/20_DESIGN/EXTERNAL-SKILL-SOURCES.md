# Meridiano Legal — External Design Skill Sources

Fecha de evaluación inicial: 2026-08-17

Este documento registra procedencia y función de los skills externos considerados por el Design Skills Layer. No convierte repositorios externos en autoridad del producto ni autoriza actualización automática desde ramas mutables.

## Núcleo

- **Emil Kowalski — Design Engineering**  
  Fuente declarada: `emilkowalski/skill` / skill `emil-design-eng`.  
  Función en Meridiano: motion, interacción, polish y criterio de design engineering.

- **Impeccable**  
  Fuente declarada: `pbakaus/impeccable`.  
  Función en Meridiano: auditoría amplia de UX/UI, information architecture, visual hierarchy, responsive, typography, spacing, forms, edge cases y polish.

- **Taste Skill**  
  Fuente declarada: `Leonxlnx/taste-skill`; skills `design-taste-frontend` y `gpt-taste`.  
  Función en Meridiano: lectura del brief, dirección visual, varianza/densidad/motion y disciplina anti-genérica.

- **Vercel Agent Skills — Web Design Guidelines**  
  Fuente declarada: `vercel-labs/agent-skills`; skill `web-design-guidelines`.  
  Función en Meridiano: interfaz web, semántica, accesibilidad, forms y buenas prácticas. La fuente de reglas externa debe fijarse antes de convertirse en gate reproducible.

- **Microsoft Skills — Frontend Design Review**  
  Fuente declarada: `microsoft/skills`; skill `frontend-design-review`.  
  Función en Meridiano: crítica independiente de production design, design-system compliance, responsive y trustworthy UI.

- **Make Interfaces Feel Better**  
  Fuente declarada: `jakubkrehel/make-interfaces-feel-better`.  
  Función en Meridiano: pase tardío de polish en tipografía, superficies, iconos, motion y performance.

- **UI Craft**  
  Fuente declarada: `educlopez/ui-craft`.  
  Función en Meridiano: design engineering system, anti-slop, tokens, review, accessibility audit y acceptance bar. No se convierte en gate de CI sin evaluación previa de señal/ruido y versionado.

## Política de actualización

1. No consumir instrucciones remotas mutables como autoridad silenciosa durante una release.
2. Antes de CI/enforcement, registrar versión o commit upstream y revisar licencia/procedencia.
3. Las actualizaciones de skills se revisan como cambios de tooling, no se autoaceptan.
4. Toda contradicción con Meridiano se resuelve con la precedencia del orquestador.
5. Un skill puede ser retirado si produce recomendaciones repetidamente incompatibles con el contexto jurídico, accesibilidad o performance.

## Herramientas complementarias

Figma se considera la superficie preferida para prototipos visuales editables cuando un rediseño necesita validar composición antes de propagarse en HTML/CSS. Playwright, axe y Lighthouse siguen siendo la evidencia ejecutable para browser QA; ninguna crítica visual los reemplaza.

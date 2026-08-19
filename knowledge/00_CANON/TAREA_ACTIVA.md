# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Frente vigente

**v7.1 — Commercial Clarity / profundidad progresiva de Home y hub de Soluciones.**

Rama:

`feat/v710-commercial-clarity`

## Baseline

- `main`: v7.0.0 certificada;
- baseline de apertura: `e5dc22e33c46a1b4fc2ebc9a01ab33444b935eb6`;
- Meridiano Legal sigue siendo la marca madre;
- Meridiano Legal Intelligence sigue siendo una capa transversal;
- se conservan las seis rutas públicas y los 8 productos + 8 servicios canónicos;
- `Meridiano Counsel` continúa fuera de la oferta pública.

## Problema observable

La v7.0 mejoró la arquitectura y redujo carga cognitiva, pero la Home quedó demasiado condensada para comprensión comercial. Un visitante entiende Diagnosticar → Transformar → Controlar → Operar, pero debe navegar demasiado para saber:

1. qué modalidad puede contratar;
2. qué capacidades concretas existen detrás de cada verbo;
3. qué puede recibir o dejar funcionando;
4. cómo se diferencian intervención puntual, transformación, capacidad recurrente e ingeniería jurídica;
5. por qué la experiencia de Meridiano es pertinente para ese trabajo.

## Hipótesis

Aplicar profundidad progresiva: problema primero, modalidad después, capacidad concreta luego y profundidad jurídica como respaldo. La Home debe recuperar sustancia sin regresar a una acumulación de tarjetas, taxonomías o claims tecnológicos.

## Alcance de esta iteración

1. Definir arquitectura comercial v7.1 de Home y hub.
2. Hacer visibles cinco modalidades de intervención:
   - diagnóstico;
   - proyecto cerrado;
   - transformación/implementación;
   - capacidad jurídica recurrente;
   - Legal Engineering.
3. Mantener el modelo Diagnosticar → Transformar → Controlar → Operar, revelando detrás:
   - Legal AI Diagnostic;
   - Legal AI Transformation;
   - Meridiano Legal Desk;
   - Contract Control;
   - Regulatory Control;
   - AI Governance 360;
   - Legal Engineering Studio.
4. Hacer visibles resultados operativos de alto valor sin crear un segundo catálogo.
5. Reforzar autoridad y especialización en una iteración posterior del mismo frente, usando únicamente evidencia documentada en `firma.html` y fuentes canónicas.
6. Mantener source-driven materialization, validación fail-closed y compatibilidad con la capa v7.0.

## Fuentes nuevas

- `knowledge/20_DESIGN/HOME-COMMERCIAL-CLARITY-v71.md`;
- `assets/data/v7/home-commercial-clarity-v71.json`.

El materializador y validador públicos de Legal Intelligence deben preferir el contrato v7.1 cuando exista y conservar fallback v7.0 cuando no exista.

## No objetivos

- no crear una séptima ruta;
- no crear un segundo catálogo;
- no modificar todavía los catálogos jurídicos de 8 productos y 8 servicios;
- no publicar nuevas tarifas;
- no prometer portal, CLM/SaaS, CRM, pagos, firma, agenda o upload;
- no prometer monitoreo automático universal;
- no garantizar permisos o decisiones de autoridades;
- no publicar Meridiano Counsel;
- no crear un framework frontend nuevo;
- no degradar accesibilidad, responsive, performance o el funnel de contacto.

## Capability truth

- Contract Control y Regulatory Control siguen siendo patrones de implementación/operación, no SaaS autónomos;
- Legal Desk es capacidad jurídica gestionada dentro de perímetro, canales, QA, capacidad y SLA pactados;
- AI Governance 360 no sustituye auditorías técnicas, seguridad o evaluación científica del modelo;
- Legal Engineering solo incluye desarrollo, integraciones, agentes, interfaces o automatización cuando el alcance técnico y jurídico lo establece expresamente.

## Criterio de aceptación del prototipo

Sin abrir fichas profundas, un usuario debe poder responder:

1. qué problemas atiende Meridiano;
2. qué tipo de intervención puede contratar;
3. qué es Legal Intelligence;
4. qué diferencia existe entre Legal Desk y una bolsa de horas;
5. qué diferencia existe entre Contract Control y un CLM/repositorio;
6. cómo funciona la escalera de AI Governance;
7. qué significa Regulatory Control y qué no promete;
8. cuándo puede intervenir Legal Engineering;
9. qué puede quedar funcionando después del proyecto;
10. cuál es el siguiente paso aunque el usuario no conozca el nombre del producto.

## Secuencia de trabajo

1. contrato de contenido y arquitectura;
2. materialización source-driven en Home + hub;
3. validación de enlaces, seis rutas y capability truth;
4. crítica de densidad desktop/mobile;
5. ajuste de autoridad y consolidación de resultados/método si mejora comprensión;
6. E2E/axe/performance;
7. PR permanece draft hasta que todos los gates del mismo SHA estén verdes.

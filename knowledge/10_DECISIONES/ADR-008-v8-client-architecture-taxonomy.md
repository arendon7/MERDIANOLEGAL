# ADR-008 — v8 Client Architecture & Taxonomy

Fecha: 2026-08-25
Estado: **propuesto para revisión; no modifica todavía producción ni capability truth**.
Baseline: `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b` — v7.4.0 production-certified.

## 1. Problema observable

La arquitectura pública certificada es técnicamente sólida, pero expone simultáneamente tres taxonomías comerciales que se solapan: `productos`, `servicios` y `soluciones/necesidades`.

Ejemplos:

- `productos/diagnostico-juridico-empresarial.html`;
- `servicios/diagnostico-juridico-empresarial.html`;
- `soluciones/ordenar-riesgo-juridico-empresa.html`.

Las tres superficies pueden responder a una intención de compra muy similar. El visitante debe comprender primero la taxonomía interna de Meridiano antes de identificar qué intervención necesita.

El problema no es falta de profundidad jurídica. Los catálogos v4.1/v4.2 contienen perímetro, entregables, límites, responsabilidades, tiempos y criterios de aceptación suficientemente estructurados. El problema es la arquitectura de descubrimiento y la carga cognitiva producida por categorías comerciales paralelas.

## 2. Decisión

v8 adoptará una arquitectura pública orientada a la decisión del cliente con tres familias de oferta:

1. **Prácticas** — dominios de expertise y capacidad profesional.
2. **Soluciones** — intervenciones con resultado, perímetro y entregables definidos.
3. **Servicios continuos** — relaciones recurrentes de capacidad jurídica y continuidad.

Las antiguas etiquetas `producto` y `servicio` continúan existiendo en las fuentes históricas mientras se migra el truth layer, pero dejan de gobernar la primera lectura del sitio.

## 3. Arquitectura objetivo

### Prácticas

1. Contratación y Negocios.
2. Corporativo, Societario y Gobierno.
3. Propiedad Intelectual y Activos Intangibles.
4. Tecnología, Datos e Inteligencia Artificial.
5. Regulación, Infraestructura y Proyectos.
6. Legal Operations y Transformación Jurídica.

### Soluciones

1. Diagnóstico Jurídico Empresarial.
2. Empresa Jurídicamente Organizada.
3. Sistema de Protección de Activos Intangibles.
4. Empresa Lista para Inversión.
5. Programa de Gobernanza de IA.
6. Proyecto Regulado Estructurado.
7. Sistema Contractual Empresarial.
8. Programa de Cumplimiento Digital.

### Servicios continuos

1. Dirección Jurídica Externa.
2. Meridiano Contratos — sujeto a capability contract específico antes de publicación.

## 4. Regla de capability truth para Meridiano Contratos

Meridiano Contratos podrá presentarse como una oferta recurrente de continuidad contractual únicamente en la medida en que su contrato comercial describa capacidades realmente disponibles.

La web pública **no** puede inferir por el nombre:

- portal productivo dentro de este repositorio;
- autenticación;
- firma electrónica;
- pagos;
- CRM;
- agenda;
- upload;
- CLM autónomo;
- monitoreo universal;
- decisión jurídica autónoma.

Si existe un workspace privado real en infraestructura separada, su alcance, disponibilidad, autenticación, soporte, datos, seguridad y límites deben quedar expresamente documentados antes de usarlo como claim público.

Hasta entonces, v7.4 capability truth permanece vigente.

## 5. Cambio del invariante “46 HTML”

La cifra de **46 superficies HTML** pasa de ser un objetivo de producto permanente a ser un **baseline histórico de migración**.

Justificación:

- conservar una cantidad física de páginas no es un objetivo de usuario;
- varias rutas actuales contienen intención semántica solapada;
- v8 debe poder consolidar superficies sin perder SEO, enlaces ni verdad jurídica;
- cualquier retiro requiere mapping explícito, canonical/alias compatible y validación de enlaces.

Durante transición puede existir un número físico mayor de HTML por aliases de compatibilidad. La métrica relevante será:

- destinos canónicos identificados;
- legacy URLs resueltas;
- cero enlaces rotos;
- sitemap coherente;
- canonical correcto;
- truth parity.

## 6. Estrategia de rutas

No se eliminarán URLs antiguas de forma abrupta.

Cada superficie recibe uno de estos estados:

- `KEEP` — permanece canónica;
- `RENAME` — cambia naming público sin necesariamente cambiar URL en la primera wave;
- `MOVE` — nueva ruta canónica con alias legacy;
- `MERGE` — contenido/intent se absorbe en otra superficie canónica;
- `ALIAS` — superficie legacy mínima para compatibilidad;
- `REVIEW` — destino pendiente de evidencia o prototipo.

GitHub Pages no debe tratarse como si ofreciera redirects de servidor configurables. La estrategia concreta de alias/redirect se definirá antes de ejecutar W4.2 y se validará en navegadores y SEO.

## 7. Sectores

La navegación primaria de sectores se simplifica hacia seis clusters:

1. Tecnología y economía digital.
2. Startups e inversión.
3. Servicios públicos, infraestructura y proyectos públicos.
4. Ambiente, residuos y economía circular.
5. Salud y ciencias de la vida.
6. Empresas, comercio y grupos empresariales.

`Agroindustria, fertilizantes y sostenibilidad` permanece como especialidad/subsector con autoridad propia, pero no necesita competir necesariamente como séptimo cluster primario.

`Operaciones jurídicas` deja de tratarse como sector y migra hacia la práctica Legal Operations.

## 8. Perspectivas / Insights

Los seis artículos actuales se preservan. La decisión de naming visible `Perspectivas` vs `Insights / Perspectivas` es de copy/IA y no exige cambio de URL en esta ADR.

## 9. No objetivos de W4.1

Este ADR no:

- cambia HTML público;
- cambia navegación productiva;
- cambia sitemap;
- habilita analítica;
- crea nuevas capabilities tecnológicas;
- cambia precios;
- modifica `stable`;
- elimina catálogos v4.1/v4.2;
- reduce validadores o gates;
- abre un portal dentro de GitHub Pages.

## 10. Impacto técnico esperado

La implementación v8 deberá actualizar de manera controlada:

- truth/experience model;
- renderer/materializadores;
- navegación;
- breadcrumbs;
- sitemap/canonical;
- E2E de rutas;
- validators que hoy fijan 46 HTML y 8+8 fichas;
- documentación canónica;
- Graphify después del merge.

Los gates existentes se mantienen o endurecen; no se relajan para acomodar la nueva arquitectura.

## 11. Rollout

1. W4.1 — contrato canónico y matriz de migración.
2. W4.2 — contrato técnico de aliases/canonical/SEO.
3. W4.3 — design system v8 y renderer piloto.
4. W4.4 — Home piloto desktop/mobile.
5. W4.5 — tres superficies representativas: solución, práctica, recurrente.
6. W4.6 — Meridiano Contratos, solo tras capability contract verificable.
7. W4.7 — propagación de oferta.
8. W4.8 — sectores, perspectivas y firma.
9. W4.9 — diagnóstico interactivo como frente separado.
10. W4.10/W4.11 — migración SEO, hardening y certificación.

## 12. Criterio de aceptación de la ADR

La ADR puede pasar a `accepted` cuando:

- la matriz de las 46 superficies esté completa;
- cada legacy URL tenga destino/estado;
- las 8 soluciones preserven truth parity con catálogos;
- las 6 prácticas tengan fuente jurídica identificable;
- Dirección Jurídica Externa conserve su contrato vigente;
- Meridiano Contratos tenga capability boundary documentado o permanezca no publicado;
- exista estrategia técnica de compatibilidad para GitHub Pages;
- se valide una muestra Home + solución + práctica + recurrente antes de propagación.

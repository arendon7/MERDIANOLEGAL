# Meridiano Legal — Tarea activa

Actualizado: 2026-08-13.

## Estado

**v5.25.0 — autoridad profesional verificable: activa.**

Baseline certificado: `stable = 73ba88fda16545cc3a257594b2a91d67a9c848b6` (v5.24.0).

## Problema

La oferta y la autoridad temática ya tienen contratos verificables, pero la web muestra poca trayectoria profesional concreta. La portada describe método; `firma.html` enumera formación y sectores; `experiencia.html` es correctamente ficticia y noindex. Falta distinguir con claridad conocimiento temático, demostración y experiencia profesional real del director.

## Contrato

1. `professional-authority-v525.json` es la fuente canónica de hechos publicados por v5.25.
2. La portada muestra una síntesis breve de formación y trayectoria.
3. `firma.html` incorpora `#trayectoria` con formación, cinco entradas cronológicas y cuatro grupos de asuntos representativos.
4. Las organizaciones citadas son trayectoria del director, no una lista de clientes de Meridiano Legal.
5. La formación de UNIR se publica como formación de posgrado, no como título completado.
6. Portada y firma mantienen un grafo Organization ↔ Person coherente.
7. El centro demo conserva su naturaleza ficticia y noindex.
8. No se publican testimonios, logos de terceros, métricas de éxito, garantías ni claims de liderazgo no sustentados.
9. v5.25 se integra dentro del paso canónico v5.18+ sin alterar los 30 pasos de v5.24.
10. No se reduce ningún validator, E2E, axe gate, budget ni requisito de promoción a stable.

## No objetivos

No hay rediseño general, cambio de precios/oferta, nuevas capacidades externas, backend, CRM, portal real, almacenamiento, PII ni reescritura retrospectiva de v5.24.

## Cierre

Fuente, compositor, validator y E2E v5.25 deben pasar; builder e idempotencia deben pasar; validadores históricos, Pages, smoke, Browser/axe, Lighthouse y release-health deben permanecer verdes. `stable` solo se mueve después de la certificación completa y del cierre documental/Graphify.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release activa

**v5.22.0 — arquitectura editorial de oferta y narrativa jurídica senior.**

`stable` permanece congelada en el snapshot funcional v5.21 certificado: `b2a6d4d4d2608362e86b53ea4cc197cd7ce33cc1`.

## Problema observable

La auditoría posterior a v5.21 confirma que las 16 fichas profundas ya tienen buen perímetro, cantidades, entregables, responsabilidades, aceptación y límites. La debilidad está en la lectura comercial/editorial:

1. productos y servicios comparten una estructura visual y narrativa casi idéntica;
2. varios pares se perciben solapados aunque su lógica de contratación sea distinta —diagnóstico/auditoría, contrato puntual/sistema contractual, PI, IA y proyectos regulados—;
3. capas anteriores con buena tesis comercial y jurídica quedaron diluidas al superponer versiones posteriores;
4. el criterio jurídico y el seniority se deducen del detalle, pero no se explicitan de forma compacta como estándar de análisis;
5. algunas referencias a `Meridiano Empresas` deben seguir la frontera de capacidades v5.21 y no sugerir un portal productivo no habilitado;
6. `knowledge/00_CANON/CONTEXTO_RAPIDO.md` quedó desactualizado respecto de v5.21.

## Objetivo

Integrar las mejores decisiones de contenido ya construidas en el proyecto y elevar la comprensión del portafolio sin aumentar ruido ni inventar autoridad.

La narrativa canónica debe expresar que Meridiano no vende horas aisladas como propuesta principal: vende reducción de incertidumbre, estructuras implementables, decisiones mejor informadas, continuidad jurídica, capacidad de ejecución y organización empresarial. La unidad comercial visible es el resultado y el alcance verificable.

## Arquitectura editorial v5.22

### Portada

Conservar la secuencia certificada de v5.20:

1. situación empresarial;
2. modalidad;
3. servicios;
4. productos;
5. evidencia;
6. planes/precios;
7. contratación.

Mejorar dentro de esa secuencia, sin abrir nuevos selectores:

- tesis de marca y hero;
- diferencia entre servicio especializado, producto cerrado, diagnóstico y acompañamiento recurrente;
- copy de transición y CTAs;
- prueba de rigor basada en alcance, método, fuentes, responsables y cierre, no en claims no verificables.

### 16 fichas profundas

Mantener toda la estructura v4.1/v4.2 y añadir una sola capa editorial compacta por oferta que responda:

1. **Decisión empresarial:** qué debe poder decidir la dirección;
2. **Por qué esta modalidad:** por qué conviene producto, servicio, diagnóstico o acompañamiento;
3. **Alternativa cercana:** cuándo elegir la oferta vecina en lugar de esta;
4. **Lente jurídica:** regímenes/preguntas de control que gobiernan el análisis;
5. **Capacidad instalada:** qué queda administrable al cierre o en operación.

El marco jurídico evitará listas normativas decorativas. Las normas concretas solo se incorporan cuando sean materialmente útiles y su estado haya sido verificado. En IA se distingue expresamente política pública de legislación vigente.

## Pares que deben quedar inequívocamente diferenciados

- Diagnóstico Jurídico Empresarial ↔ Auditoría Jurídica Empresarial Integral.
- Contratación Estratégica ↔ Sistema Contractual Empresarial.
- Propiedad Intelectual y Activos Intangibles ↔ Marca, Software y Activos Intangibles Protegidos.
- Tecnología e Inteligencia Artificial ↔ Programa de Gobernanza Jurídica y Uso Responsable de IA.
- Estructuración Jurídica de Proyectos Regulados ↔ Proyecto Regulado Jurídicamente Estructurado.

## Criterio de diseño

Aplicar un enfoque trust-first y regulado:

- baja variación visual;
- movimiento mínimo y funcional;
- densidad media;
- jerarquía tipográfica y espacial antes que decoración;
- no gradientes/efectos genéricos de IA;
- no nuevas librerías de motion salvo necesidad demostrable;
- responsive y accesibilidad sin regresión.

Marcos de trabajo: Impeccable para jerarquía/UX writing/refine; Taste Skill para auditoría anti-slop y control de densidad/variación; Emil Kowalski Design Engineering para detalle funcional e interacción con propósito.

## Contratos que no pueden degradarse

- 46 páginas HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- static-first;
- 43 E2E observados como piso de cobertura;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- v5.8→v5.21 preservados;
- sin scoring ni inferencia automática nueva;
- sin PII, storage persistente o transporte nuevo;
- WhatsApp manual;
- portal real deshabilitado;
- no CRM/backend, autenticación real, firma, pagos, agenda o carga documental ficticios;
- no testimonios, clientes, premios, cifras de experiencia o resultados no verificables.

## Alcance técnico previsto

- `offer-narrative-v522.json`: contrato editorial por oferta;
- renderers v4.1/v4.2: integración de la capa narrativa en las 16 fichas;
- `offer-v522.css`: presentación compacta trust-first;
- `scripts/apply_offer_narrative_v522.py`: narrativa de portada y normalización final;
- `scripts/validate_offer_narrative_v522.py`: integridad de 16 ofertas, diferenciación y capability truth;
- E2E mínimo adicional para verificar estructura y accesibilidad de la nueva capa;
- actualización de `CONTEXTO_RAPIDO.md` al cierre.

## Criterio de cierre

1. las 16 ofertas poseen contrato editorial completo y único;
2. los cinco pares solapados muestran una diferencia de modalidad verificable;
3. ninguna ficha sugiere que la demo es un portal productivo;
4. la portada conserva la arquitectura v5.20 sin nuevos selectores redundantes;
5. Release Governance: PASS;
6. builder + segunda pasada/idempotencia: PASS;
7. validadores históricos + v5.22: PASS;
8. Pages + smoke: PASS;
9. Browser E2E + axe: PASS, sin reducción de cobertura;
10. Lighthouse 6/6 dentro de budgets vigentes;
11. release-health: PASS;
12. `stable` solo se promueve después de todos los gates verdes;
13. Graphify fresco en 5.22.0;
14. cierre documental y memoria canónica actualizada.

## No objetivos

- no crear productos o servicios nuevos;
- no cambiar precios por intuición;
- no construir portal real;
- no rediseñar visualmente toda la marca desde cero;
- no introducir animación decorativa;
- no convertir fichas jurídicas en artículos doctrinales extensos;
- no abrir v5.23 dentro de este ciclo.

# Meridiano Legal — Tarea activa

Actualizado: 2026-08-12.

## Release en cierre formal

**v5.15.0 — Eficiencia recomendación→acción.**

La funcionalidad ya está certificada. Antes de este cierre documental:

- SHA funcional: `48a0692e8e4f999a85cfd8619fe2e293528945c2`;
- run funcional: `31609518536`;
- `main == stable` en ese SHA;
- builder/idempotencia y validadores históricos + composición v5.8→v5.15: PASS;
- Pages + smoke: PASS;
- Browser E2E + axe: 37 observados → 35 PASS / 2 SKIP / 0 FAIL / 0 RETRY;
- 7 superficies axe limpias;
- Lighthouse: 6/6 PASS;
- CI hasta `stable`: 209 s;
- baseline v5.5: 279 s;
- mejora: 25.1%;
- cobertura reducida: no;
- budgets relajados: no;
- Release Governance + trigger builder→Pages + validator v5.15: PASS.

Graphify del cierre funcional apunta exactamente a `source_commit = 48a0692e8e4f999a85cfd8619fe2e293528945c2`, con 544 nodos, 877 relaciones y 88 notas wiki. El campo declarativo de versión aún refleja 5.14.0 porque fue construido antes de elevar `version.json`.

## Qué cerró v5.15

1. el encaje canónico de cada modalidad se muestra junto al CTA del selector v5.12;
2. límites y alternativas v5.14 se conservan como comparación ampliada secundaria y colapsada;
3. el brief del formulario prioriza razón visible + ruta comercial, manteniendo límite/alternativa disponibles;
4. rutas canónicas: diagnóstico→`scope`, auditoría→`proposal`, producto→`proposal`, servicio especializado→`scope`, recurrente→`scope`, sin contexto→`orientation`;
5. un `commercial_intent` explícito siempre tiene prioridad;
6. la web nunca cambia automáticamente la etapa de decisión; aplicar una sugerencia requiere acción del usuario;
7. las 16 fichas conservan modalidad, prueba verificable, explicación y siguiente paso hasta formulario/WhatsApp;
8. no se añadió scoring, storage, backend, fetch/XHR propio ni PII adicional.

Tres gates detectaron incompatibilidades durante la certificación y se corrigieron sin relajarlos: forma CTA v5.10, contrato JSON embebido v5.14 y validación E2E del orden de query. La cobertura permanece intacta.

## Condición pendiente para declarar v5.15 definitivamente cerrada

El cierre documental/versionado debe atravesar nuevamente:

1. builder canónico y sincronización visible a 5.15.0;
2. idempotencia + validadores v5.8→v5.15;
3. Pages + smoke;
4. Browser E2E/axe;
5. Lighthouse;
6. release-health y trigger guard;
7. promoción de `stable`;
8. verificación `main == stable`;
9. procedencia Graphify sin falsificar `source_commit`.

**No iniciar una feature pública v5.16 antes de que esos nueve puntos estén verdes sobre el SHA final de release.**

## Próximo ciclo después del cierre

**v5.16 — UX móvil y accesibilidad del recorrido comercial.**

### Objetivo

Reducir fricción y scroll en pantallas pequeñas y cerrar mejoras legítimas de accesibilidad/escaneabilidad del recorrido comercial, sin ocultar profundidad jurídica ni alterar el modelo de decisión controlado por el usuario.

### Prioridades

1. medir y reducir repetición visible/scroll móvil entre selector, recomendación, brief y estados comerciales;
2. investigar por qué la portada obtiene Lighthouse Accessibility 0.97 aunque axe no reporte violaciones serias/críticas, y corregir únicamente causas reales identificadas;
3. revisar foco visible, orden de teclado, estados `details`, navegación por anclas y devolución de foco;
4. revisar targets táctiles, espaciado, densidad y legibilidad en viewports pequeños;
5. preservar el acceso a límites, exclusiones, prueba verificable y condiciones de inicio; compactar no significa ocultar información material;
6. mantener rutas proposal/scope/orientation y ausencia de cambios automáticos;
7. ampliar assertions dentro de las 37 entradas protegidas antes de crear tests independientes nuevos.

### No objetivos

- no nuevo cuestionario;
- no scoring/ranking opaco;
- no `localStorage`/`sessionStorage` para decisión comercial;
- no backend/CRM;
- no fetch/XHR propio;
- no PII adicional;
- no testimonios/clientes/resultados fabricados;
- no firma, pagos, agenda, expediente o carga documental ficticios;
- no esconder contenido jurídico para mejorar métricas.

## Contratos que v5.16 deberá preservar

- static-first;
- 46 páginas HTML;
- 16 fichas profundas;
- 37 entradas E2E salvo necesidad independiente demostrada;
- 7 superficies axe;
- 6 superficies Lighthouse;
- budgets v5.5 sin relajación;
- fuente jurídica única;
- WhatsApp manual;
- telemetría sin PII;
- builder idempotente;
- `stable` solo después de todos los gates verdes.

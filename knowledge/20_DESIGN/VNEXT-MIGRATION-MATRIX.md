# Matriz de migración vNext — 46 superficies públicas

Fecha: 2026-08-17
Estado: planning/discovery. No es una release.

## 1. Cobertura total

El contrato canónico mantiene **46 HTML públicos**. La migración se organiza por familias para evitar rediseños archivo por archivo sin sistema.

| Familia | Cantidad | Estrategia vNext |
|---|---:|---|
| Home | 1 | Client-first + gramática editorial completa |
| Fichas de servicios | 8 | Template servicio adaptable |
| Fichas de productos | 8 | Template producto cerrado |
| Soluciones/necesidades | 7 | 6 rutas + índice |
| Sectores | 8 | Lectura sectorial, no catálogo |
| Perspectivas internas | 6 | Biblioteca editorial |
| Superficies top-level restantes | 8 | Firma, hub de perspectivas, experiencia/demo y legales/404 según función |
| **Total** | **46** | |

Nota: el grupo top-level debe validarse contra el árbol final antes del PR funcional; la suma contractual permanece en 46.

## 2. Orden de migración

### Wave 0 — infraestructura
- tokens;
- base/reset;
- shell/header/footer;
- primitives editoriales;
- componentes semánticos;
- validators vNext;
- version gates en materializadores históricos.

No cambia todavía contenido público canónico.

### Wave 1 — pilotos
1. Home.
2. Producto: Auditoría Jurídica Empresarial Integral.
3. Servicio: Tecnología e Inteligencia Artificial.
4. Contacto de Home.
5. Estados mobile de los anteriores.

Objetivo: probar todo el sistema con tres tipos de superficie antes de propagación.

### Wave 2 — 16 fichas profundas
- 8 productos usando template cerrado;
- 8 servicios usando template adaptable.

Acceptance:
- truth parity;
- mismas cantidades/límites/cierres;
- profundidad preservada;
- no CSS legacy en output v6;
- E2E de una muestra por familia + invariantes globales.

### Wave 3 — 7 soluciones
Migrar las 6 rutas + índice.
Orden:
`situación → señales → decisión → resultado → intervención → honorarios/modalidad → límites → CTA → profundidad`.

### Wave 4 — 8 sectores
Diseño editorial sectorial:
- contexto;
- decisiones/riesgos;
- actores/regulación cuando la fuente lo soporte;
- oferta relacionada;
- perspectivas.

### Wave 5 — 6 perspectivas internas + hub
Biblioteca editorial con:
- título/deck;
- metadata;
- lectura;
- relacionados;
- CTA contextual no invasivo.

### Wave 6 — Firma / experiencia / demo / legales / 404
Aplicar shell y tokens, pero respetar función de cada superficie.

`experiencia/demo` debe permanecer claramente demostrativa; no debe parecer portal real.

Privacidad, términos y aviso legal priorizan legibilidad y estabilidad sobre expresividad visual.

404 prioriza recuperación/navigation.

## 3. Mapping de componentes por familia

| Componente | Home | Producto | Servicio | Solución | Sector | Perspectiva | Legal |
|---|---|---|---|---|---|---|---|
| SiteHeader/Footer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| DecisionStatement | ✓ | ✓ | ✓ | ✓ | opc. | opc. | — |
| SituationIndex | ✓ | — | — | señales | opc. | — | — |
| OutcomeLedger | ✓ | ✓ | ✓ | ✓ | opc. | — | — |
| DeliverableLedger | — | ✓ | según fuente | opc. | — | — | — |
| ProcessTimeline | ✓ | ✓ | ✓ | opc. | — | — | — |
| PerimeterMatrix | — | ✓ | ✓ | modalidad | — | — | — |
| BoundaryBand | — | ✓ | ✓ | ✓ | según fuente | — | — |
| EvidenceBlock | ✓ | ✓ | ✓ | ✓ | ✓ | fuentes | — |
| CommercialMatrix | profundidad | ✓ | ✓ | ✓ | — | — | — |
| DeepDisclosure | opc. | ✓ | ✓ | ✓ | opc. | opc. | — |
| CanonicalContactForm | 1 único | enlaza | enlaza | enlaza | enlaza | enlaza | — |

## 4. CSS legacy — plan de retirada

### No retirar de golpe
Las hojas históricas siguen siendo necesarias para reproducir el baseline v5.x y pueden ser requeridas durante transición.

### En v6 output
Una superficie marcada `migrated-v6` no debe cargar hojas legacy de presentación que hayan sido absorbidas por el nuevo sistema.

Validator propuesto:
- lista permitida de CSS v6;
- lista prohibida en superficies v6 para hojas absorbidas;
- exception list temporal explícita por wave;
- exception count debe disminuir, nunca crecer sin ADR.

### Meta de final de ciclo
Todas las 46 superficies usan la familia consolidada y ninguna depende de overrides históricos de presentación v3.x–v5.x.

Los archivos históricos pueden permanecer en repo para reproducibilidad/documentación, pero no cargarse en producción v6 salvo dependencia deliberada documentada.

## 5. JS legacy

Separar:

### Mantener por capability real
- navegación/menu;
- único form/handoff;
- observabilidad no PII;
- runtime config;
- comportamiento accesible necesario.

### Evaluar consolidación
JS de releases históricas que solo inserta/ajusta markup ya materializable desde fuente.

Regla: no migrar a SPA/framework solo para consolidar. Static-first sigue vigente.

## 6. Contratos de contenido

Cada migración debe comprobar:
- title/meta/schema/canonical intactos salvo cambio aprobado;
- fuente de verdad identificable;
- cantidades idénticas;
- límites idénticos en significado;
- no omisión de exclusiones;
- no convertir procedimiento en garantía;
- no convertir experiencia del director en cliente/case study de Meridiano;
- no convertir demo en capability real.

## 7. Contacto/handoff

La única superficie con formulario físico sigue siendo Home/contacto.

Las demás:
- CTA con parámetros de contexto permitidos;
- enlace al mismo formulario;
- WhatsApp manual según contrato vigente.

Prohibido crear formularios embebidos por ficha durante migración.

## 8. Mobile

Cada wave debe tener aceptación mobile propia. No aceptar automáticamente:
- desktop grid → horizontal carousel;
- desktop grid → stack infinito.

Patrones preferidos:
- índice lineal;
- disclosure;
- tabla responsive;
- ledger;
- “ver todos” para bibliotecas no esenciales;
- CTA contextual.

## 9. Rollout técnico

Por wave:
1. source/contract;
2. renderer/materializer;
3. validators;
4. unit/static checks;
5. browser desktop/mobile;
6. axe;
7. Lighthouse si impacta superficie cargada;
8. segunda pasada idempotente;
9. solo entonces propagación a siguiente familia.

No mezclar migración de todas las familias en un único cambio imposible de aislar.

## 10. Rollback

Mientras v6 no esté certificado:
- `stable` conserva v5.31 certificada;
- cualquier fallo permite descartar/revertir rama v6 sin alterar snapshot estable;
- no promover stable parcialmente por waves.

## 11. Definition of Done global

La migración completa termina cuando:
- 46/46 superficies declaradas v6;
- 16/16 fichas truth-parity;
- 7/7 soluciones migradas;
- 8/8 sectores migrados;
- biblioteca editorial migrada;
- 1/1 formulario físico;
- 0 dependencias de CSS legacy absorbido en output v6;
- 30 pasos builder exactos;
- idempotencia PASS;
- static validation PASS;
- Browser E2E/axe PASS;
- Lighthouse budgets PASS;
- Graphify alineado;
- Pages + smoke PASS;
- stable promovido solo al SHA certificado.
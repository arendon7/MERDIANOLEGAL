# Meridiano Legal v5.22.0 — Arquitectura editorial de oferta y narrativa jurídica

Fecha de cierre funcional: 2026-08-13.

## Propósito

v5.22 reconcilia las mejores capas históricas de narrativa comercial y profundidad jurídica con el catálogo profundo v4.1/v4.2 y con la arquitectura de compra certificada en v5.20–v5.21.

La release no crea productos o servicios nuevos. Su objetivo es hacer más evidente qué compra la empresa, por qué conviene una modalidad y no otra, qué criterio jurídico gobierna el trabajo y qué capacidad queda instalada al cierre.

La tesis comercial se desplaza de “horas de abogado” hacia resultado, perímetro, método, evidencia, implementación y cierre verificable.

## Resultado funcional

### Portada

La portada conserva una sola secuencia de decisión:

1. situación empresarial;
2. modalidad;
3. servicios;
4. productos;
5. evidencia;
6. planes/precios;
7. contratación.

v5.22 mejora la tesis sin reintroducir selectores redundantes:

- H1: `Dirección jurídica para decisiones que deben avanzar.`;
- el lead integra criterio jurídico, comprensión empresarial y tecnología aplicada;
- la prueba pública se formula como evidencia de criterio senior, no como claim de autoridad;
- servicios se presentan como intervenciones adaptables a hechos, negociación, regulación y terceros;
- productos se presentan como resultados con perímetro, entregables y cierre definidos desde el inicio.

### 16 fichas profundas

Cada ficha conserva el alcance jurídico/comercial v4.1/v4.2 y añade una única capa editorial source-driven por `catalog-id` con cinco respuestas:

1. **Decisión empresarial:** qué debe poder decidir la dirección;
2. **Por qué esta modalidad:** por qué conviene ese tipo de intervención;
3. **Alternativa cercana:** cuándo elegir una oferta vecina;
4. **Lente jurídica:** regímenes y preguntas de control que gobiernan el análisis;
5. **Capacidad instalada:** qué queda administrable al cierre o durante la operación.

El contrato fuente es `offer-narrative-v522.json` y cubre exactamente 16 ofertas.

## Diferenciación de ofertas cercanas

El validator exige diferenciación verificable en cinco pares que antes podían percibirse como solapados:

- Diagnóstico Jurídico Empresarial ↔ Auditoría Jurídica Empresarial Integral;
- Contratación Estratégica y Gestión Contractual ↔ Sistema Contractual Empresarial;
- Propiedad Intelectual y Activos Intangibles ↔ Marca, Software y Activos Intangibles Protegidos;
- Tecnología e Inteligencia Artificial ↔ Programa de Gobernanza Jurídica y Uso Responsable de IA;
- Estructuración Jurídica de Proyectos Regulados ↔ Proyecto Regulado Jurídicamente Estructurado.

La diferencia no descansa solo en el nombre: cada par debe explicar decisión, modalidad, perímetro, alternativa y resultado instalado.

## Lente jurídica y criterio senior

v5.22 recupera una capa de razonamiento jurídico que versiones anteriores expresaban mejor y la integra sin convertir las fichas en artículos doctrinales.

El seniority se demuestra mediante:

- preguntas de control;
- régimen y fuentes relevantes;
- supuestos;
- materialidad y riesgo;
- responsables;
- perímetro y exclusiones;
- entregables;
- criterios de aceptación y cierre.

No se publican claims no verificables sobre clientes, premios, antigüedad, liderazgo de mercado o resultados garantizados.

### IA

La narrativa de IA distingue expresamente:

- obligaciones vigentes por materia —datos, consumidor, propiedad intelectual, contratación, trabajo, competencia, derechos fundamentales y regulación sectorial—;
- gobierno basado en riesgo;
- política pública y evolución normativa.

`CONPES 4144 de 2025` se presenta como Política Nacional de Inteligencia Artificial y no como una supuesta ley general integral de IA ya vigente.

### Referencias legales estables incorporadas cuando son materiales

Entre otras:

- Ley 1581 de 2012 para protección de datos;
- Ley 1480 de 2011 para protección del consumidor;
- Ley 1258 de 2008 cuando aplica al régimen SAS.

Las referencias normativas no se usan como decoración ni como lista exhaustiva fuera de contexto.

## Capability truth desde la fuente

Una de las correcciones más importantes de v5.22 fue trasladar la veracidad de capacidades al catálogo fuente.

La primera implementación intentó neutralizar después del render cualquier mención de `Meridiano Empresas`. El validator v5.12 detectó que esa estrategia hacía divergir el HTML materializado del contrato v4.1/v4.2.

La solución definitiva fue source-driven:

- el compositor v5.22 dejó de reescribir silenciosamente el contenido contractual;
- las fuentes ambiguas se corrigieron en `catalog-products-v41/` y `catalog-services-v42/`;
- `Meridiano Empresas` solo puede aparecer condicionado a una habilitación productiva real o como relación explícitamente demostrativa hacia `demo.html`;
- formulaciones ambiguas como `Meridiano Empresas o Microsoft 365` sin condición productiva son bloqueadas por CI.

Fuentes corregidas durante la release:

- `catalog-services-v42/s01-diagnostico.json`;
- `catalog-services-v42/s02-direccion.json`;
- `catalog-services-v42/s08-legal-ops.json`;
- `catalog-products-v41/p03-intangibles.json`;
- `catalog-products-v41/p05-ia.json`;
- `catalog-products-v41/p08-datos-consumidor.json`.

La frontera v5.21 continúa vigente: el portal real permanece deshabilitado y `demo.html` sigue siendo demostrativo/noindex.

## Arquitectura técnica

### Fuentes

- `offer-narrative-v522.json` — contrato editorial de 16 ofertas;
- `catalog-products-v41/` — productos fuente;
- `catalog-services-v42/` — servicios fuente.

### Materialización

`scripts/apply_offer_narrative_v522.py` se ejecuta después de capability truth v5.21 y:

1. identifica cada ficha mediante `data-catalog-id`;
2. preserva el cuerpo contractual generado por v4.1/v4.2;
3. inserta una única capa editorial v5.22 antes de situaciones de uso;
4. carga `offer-v522.css` exactamente una vez;
5. actualiza la narrativa de portada de forma idempotente;
6. falla si detecta copy de plataforma ambiguo que debería corregirse en la fuente.

### Validator

`scripts/validate_offer_narrative_v522.py` protege:

- 16/16 contratos editoriales;
- cinco pares de modalidad recíprocos y diferenciados;
- tres criterios de lente jurídica por ficha;
- enlaces locales de alternativa existentes;
- frontera semántica IA entre política pública, proyectos legislativos y derecho vigente;
- referencias jurídicas mínimas verificadas donde corresponde;
- capability truth desde catálogo fuente;
- una sola capa v5.22 por ficha;
- una sola superficie de modalidad v5.20 en portada;
- ausencia de claims comerciales no verificables.

### Presentación

`offer-v522.css` aplica un lenguaje visual trust-first:

- baja variación;
- densidad media;
- jerarquía espacial y tipográfica antes que decoración;
- disclosure nativo para la lente jurídica;
- foco visible;
- responsive sin overflow;
- sin librerías de motion ni efectos decorativos nuevos.

Los criterios de trabajo usados fueron Impeccable para jerarquía y UX writing, Taste Skill para auditoría anti-slop/densidad y Emil Kowalski Design Engineering para detalle funcional e interacción con propósito.

## Incidencias resueltas sin debilitar gates

### 1. Compatibilidad histórica del validator growth

PR #85 hizo `validate_growth_v51.py` version-aware. Hasta v5.21 mantiene el contrato histórico; desde v5.22 exige la nueva evidencia de criterio senior.

No se revirtió el nuevo copy ni se eliminó la prueba.

### 2. Divergencia fuente/render por `Meridiano Empresas`

PR #86 corrigió el enfoque: capability truth pasó a las fuentes v4.1/v4.2 y el compositor dejó de mutar contenido contractual después del render.

El validator v5.12 se conservó intacto como defensa de source-of-truth.

### 3. Smoke público v5.1

PR #87 hizo `validate_live_v51.py` version-aware para comprobar en la URL pública la narrativa v5.22 sin perder canonical, hub, rutas e interlinking v5.1.

### 4. Runtime que destruía el prerender static-first

PR #88 encontró una deuda real de arquitectura: `catalog-page.js` volvía a hacer fetch del JSON y reemplazaba `#detail-page` con un template legado, borrando en navegador la capa editorial que sí estaba correcta en el HTML estático.

La corrección preserva el HTML prerenderizado cuando `#detail-page` declara `data-static-catalog="true"`; el renderer dinámico queda únicamente como fallback legado. El validator v5.22 protege este guard.

### 5. Contraste WCAG AA en ficha profunda

PR #89 resolvió el último gate Browser/axe rojo. El texto descriptivo heredado tenía aproximadamente 4.44:1 sobre fondo marfil, apenas bajo AA para texto normal. Se ajustó a `#53606b`, aproximadamente 5.73:1, sin cambiar copy, layout, cobertura ni budgets.

## Trazabilidad de implementación

- PR funcional #84 — arquitectura editorial de oferta;
- PR #85 — compatibilidad growth validator;
- PR #86 — capability truth desde catálogo fuente;
- PR #87 — smoke público version-aware;
- PR #88 — preservación static-first en runtime;
- PR #89 — contraste AA de ficha profunda;
- SHA funcional final certificado: `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`;
- run público final: `31671834728`.

Al cierre funcional:

`main == stable == 5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`.

## Evidencia final

### Builder, validación y despliegue

- builder canónico: PASS;
- segunda pasada/idempotencia: PASS;
- validadores históricos: PASS;
- validator v5.22: PASS;
- Pages: PASS;
- smoke público: PASS;
- release-health: PASS;
- promoción de `stable`: PASS.

El release-health final registra:

`OFFER NARRATIVE V5.22 OK: 16/16 ofertas, 5 pares diferenciados, lente jurídica x3, capability truth source-driven, #detail-page canónico y runtime sin rehidratación destructiva.`

### Browser E2E + axe

- 49 pruebas observadas;
- 47 PASS;
- 2 SKIP;
- 0 FAIL;
- 0 RETRY;
- reporter wall time: 90 s;
- Chromium desktop;
- Chromium mobile;
- WebKit desktop;
- 7 superficies axe WCAG 2.1 AA sin violaciones serias/críticas.

La suite aumentó de 43 pruebas observadas en v5.21 a 49 en v5.22.

### Lighthouse

6/6 superficies PASS, sin relajación de budgets:

| Superficie | Performance | Accesibilidad | LCP | CLS | TBT | Transferencia |
|---|---:|---:|---:|---:|---:|---:|
| Home | 1.00 | 1.00 | 1367 ms | 0 | 55 ms | 106,908 B |
| Solution IA | 1.00 | 1.00 | 904 ms | 0 | 0 ms | 23,324 B |
| Product IA | 0.96 | 1.00 | 1245 ms | 0 | 210 ms | 37,208 B |
| Sector tecnología | 0.98 | 1.00 | 938 ms | 0.087 | 0 ms | 24,385 B |
| Perspective IA | 1.00 | 1.00 | 941 ms | 0 | 0 ms | 26,146 B |
| Demo | 1.00 | 1.00 | 906 ms | 0 | 0 ms | 22,008 B |

Todos los audits de accesibilidad Lighthouse puntuaron 1.00.

### CI

- tiempo hasta gate de `stable`: 206 s;
- baseline v5.5: 279 s;
- mejora frente al baseline: 26.2%;
- cobertura reducida: no;
- budgets relajados: no.

### Artefactos del run `31671834728`

- Lighthouse: `9170023458`, `sha256:1184af3788a4cf82a017c59e301bdc30f72bfa0291efd27fb6fd17387168457c`;
- CI: `9170051799`, `sha256:d4bcc4135c9e3f5047f00d6e29e398fb30434a62711bfe779cc7cda65ae76365`;
- release-health: `9170052414`, `sha256:c947f7b9c4b98b03bc63059d317c6c35f9da8b3dfa43fe0a28156ebab3d42dce`;
- Pages: `9169986924`, `sha256:247be73a2e8077eef40f4080f900bab98b0ba528f28a8473221d85a6c7eef3c8`.

## Capacidades externas

Activas y verificables:

- GitHub Pages;
- WhatsApp como handoff manual;
- contexto comercial client-side;
- telemetría first-party/local sin PII;
- sitemap, robots, canonical y Open Graph;
- demo estática/noindex;
- pipeline CI de certificación.

Deshabilitada explícitamente:

- portal real de clientes.

No declarar activas sin configuración e implementación real:

- autenticación o cuentas reales;
- CRM/backend;
- almacenamiento servidor del formulario;
- email transaccional;
- firma electrónica;
- pagos;
- agenda;
- carga documental;
- analítica externa.

## No objetivos cumplidos

v5.22 no creó nuevas ofertas, no cambió precios por intuición, no construyó un portal real, no añadió PII/storage/transporte, no introdujo motion decorativo y no convirtió las fichas en tratados doctrinales.

## Cierre

v5.22 deja el portafolio más claro sin sacrificar profundidad. La diferencia entre modalidades ya no depende de interpretación del visitante: está modelada en fuente, materializada en las 16 fichas, verificada por validator y probada en navegador real.

La release funcional queda cerrada en `5c3f3194b45afb9ac21a8def27afdc3d2157b3e2`. Cualquier ciclo posterior debe partir de una nueva auditoría y un objetivo independiente; v5.23 no se abre por continuidad automática.

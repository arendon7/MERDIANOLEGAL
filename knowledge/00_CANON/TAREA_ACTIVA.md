# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Baseline pública certificada

- Release pública: **v6.3.0 — Engagement Clarity / claridad precontratación**.
- `main` y `stable` permanecen fuera del ciclo v7 y no han sido promovidos por este trabajo.
- 46 HTML públicos, 16 fichas profundas, un único formulario físico y 30 pasos históricos siguen siendo la baseline certificada.
- Portal real, auth, CRM, pagos, firma, agenda y upload continúan deshabilitados/no implementados.
- Search Console continúa sin token auténtico y analytics externa permanece deshabilitada.

## Ciclo abierto

**v7.0 — Legal Intelligence Architecture / prototipo integrado, todavía no release pública.**

Rama de trabajo:

`feat/v700-legal-intelligence-architecture`

PR de arquitectura:

`#163 — feat(v7): define Legal Intelligence architecture`

Motivo observable de negocio:

Meridiano necesita hacer visible de forma ordenada una capacidad hoy distribuida entre Diagnóstico, Dirección Jurídica Externa, Contratación, Tecnología/IA, Proyectos Regulados y Legal Operations: diagnosticar, transformar, controlar y operar trabajo jurídico utilizando criterio legal, procesos, IA, automatización y Legal Engineering.

El objetivo **no es añadir otro catálogo**. Meridiano Legal Intelligence funciona como capa transversal que conecta problemas concretos con las 16 ofertas canónicas existentes y explica cuándo la intervención debe ser diagnóstica, de implementación, de control o recurrente.

## Arquitectura vigente del prototipo

Bajo la marca madre **Meridiano Legal**, la familia **Meridiano Legal Intelligence** organiza:

1. **Legal AI Diagnostic** — servicio vendible de diagnóstico y priorización.
2. **Legal AI Transformation** — servicio vendible de rediseño e implementación.
3. **Meridiano Legal Desk** — servicio gestionado recurrente; capacidad, materias, canales y SLA se pactan por alcance.
4. **Contract Control** — patrón de implementación/operación derivado del sistema contractual; no SaaS/CLM autónomo.
5. **Regulatory Control** — patrón de implementación/seguimiento regulatorio; no monitoreo automático universal.
6. **AI Governance 360** — familia Readiness → Implementación → Managed Governance.
7. **Legal Engineering Studio** — servicio custom para workflows, automatizaciones, integraciones y herramientas expresamente delimitadas.
8. **Meridiano Counsel** — concepto futuro; permanece fuera de la oferta pública y transaccional.

Fuentes de arquitectura:

- `knowledge/10_DECISIONES/ADR-007-legal-intelligence-architecture-v7.md`;
- `knowledge/20_ARQUITECTURA/LEGAL-INTELLIGENCE-MAP-v7.md`;
- `knowledge/20_ARQUITECTURA/LEGAL-INTELLIGENCE-CONTENT-v7.md`;
- `knowledge/20_DESIGN/LEGAL-INTELLIGENCE-v7-BRIEF.md`;
- `assets/data/v7/legal-intelligence-architecture-v70.json`.

## Cinco capas source-driven materializadas

El prototipo ya no se limita a una única superficie. Se materializan **11 superficies públicas existentes**, sin crear nuevas URLs:

### 1. Entrada Legal Intelligence en Legal Operations

- `soluciones/ordenar-operacion-juridica.html`.

Hace visible **Diagnosticar → Transformar → Operar** y Legal Engineering, con boundary tecnológico explícito.

### 2. Ofertas profundas de operación y contratos

- `servicios/legal-operations.html` — Legal AI Transformation;
- `productos/sistema-contractual-empresarial.html` — Contract Control.

La capa explica evolución y continuidad sin modificar entregables, tiempos, honorarios ni límites canónicos.

### 3. AI Governance 360

- `soluciones/gobernar-inteligencia-artificial-empresa.html`;
- `productos/programa-gobernanza-ia.html`;
- `servicios/tecnologia-inteligencia-artificial.html`.

Arquitectura: **Readiness → Implementación → Managed Governance**.

### 4. Regulatory Control

- `soluciones/estructurar-proyecto-regulado.html`;
- `productos/proyecto-regulado-estructurado.html`;
- `servicios/proyectos-regulados.html`.

Arquitectura: **Estructurar → Controlar → Acompañar**.

### 5. Descubrimiento público

- `index.html`;
- `soluciones/index.html`.

Home explica **Diagnosticar → Transformar → Controlar → Operar**. El hub mantiene las **seis rutas de decisión** y presenta Legal Intelligence únicamente como capa transversal en operación/contratos, IA y regulados. No se añade una séptima ruta ni un segundo catálogo.

## Contratos y reproducción canónica

Truth y contratos v7:

- `assets/data/v7/legal-intelligence-prototype-v70.json`;
- `assets/data/v7/legal-intelligence-deep-offers-v70.json`;
- `assets/data/v7/ai-governance-360-prototype-v70.json`;
- `assets/data/v7/regulatory-control-prototype-v70.json`;
- `assets/data/v7/legal-intelligence-discovery-v70.json`.

Materializadores y validators fail-closed viven en `scripts/apply_*_v70.py` y `scripts/validate_*_v70.py`.

`scripts/normalize_experience_compat_v60.py` reproduce y valida todas las capas v7 cuando existen sus contratos. **No existe un workflow v7 paralelo permanente**: la implementación usa la cadena canónica v6 y preserva sus gates.

## Evidencia comprobada

Sobre el prototipo integrado se ha comprobado:

- `v7 Legal Intelligence architecture contract: PASS`;
- route prototype + deep offers: **PASS**;
- AI Governance 360: **PASS**;
- Regulatory Control: **PASS**;
- public discovery Home + hub: **PASS**;
- seis rutas de solución preservadas;
- Meridiano Counsel ausente de discovery público;
- portal productivo continúa `disabled`;
- 46 HTML / 43 indexables / 3 noindex preservados;
- un único formulario físico preservado;
- primera pasada canónica: **0 drift**;
- segunda pasada: **idempotente**;
- Candidate, Builder Equivalence, Engagement Clarity, Search Discovery, Release Governance y Graphify han superado el head integrado.

## Reglas que siguen vigentes

- no duplicar ni reescribir por intuición `catalog-products-v41/*.json` o `catalog-services-v42/*.json`;
- no publicar tarifas nuevas dentro de la capa v7;
- no prometer portal, SaaS, CLM, monitoreo universal, certificaciones o capabilities tecnológicas inexistentes;
- no convertir Contract Control o Regulatory Control en productos de software sin capability certificada;
- no publicar Meridiano Counsel como producto;
- no alterar sitemap ni crear URLs solo para alojar nombres comerciales;
- preservar navegación situation-first y las seis rutas v6;
- conservar un único formulario físico;
- no relajar validators, E2E, axe, privacidad ni budgets.

## Frente activo inmediato

Cerrar el prototipo v7 antes de cualquier decisión de release:

1. añadir E2E específico para las 11 superficies Legal Intelligence;
2. validar presencia, navegación por fragmentos, boundaries y preservación de las seis rutas en Browser/axe;
3. completar la ronda same-SHA de Candidate, Builder, Engagement, Search, Release Governance, Graphify, Browser y Measurement;
4. hacer crítica final de claridad, nomenclatura y densidad de Home/hub y superficies profundas;
5. mantener el PR #163 en borrador hasta cerrar esa crítica.

## Criterio para una futura release v7

No cambiar `version.json` desde 6.3.0 ni fusionar automáticamente hasta demostrar que la arquitectura:

- reduce confusión en lugar de añadir nomenclatura;
- preserva profundidad jurídica y truth de las 16 ofertas;
- hace evidente qué compra el cliente y qué cambia después;
- no duplica ofertas ni inventa capabilities;
- mantiene navegabilidad y legibilidad en desktop/mobile/teclado/reduced motion;
- supera gates estructurales, E2E/axe y privacidad en el mismo SHA;
- supera crítica independiente sobre confianza, claridad comercial y densidad.

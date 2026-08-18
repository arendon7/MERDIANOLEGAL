# Meridiano Legal — Tarea activa

Actualizado: 2026-08-18.

## Baseline pública certificada

- Release pública: **v6.3.0 — Engagement Clarity / claridad precontratación**.
- `main` y `stable` coinciden antes de abrir este ciclo.
- 46 HTML públicos, 16 fichas profundas, un único formulario físico y 30 pasos históricos permanecen como baseline certificada.
- Portal real, auth, CRM, pagos, firma, agenda y upload continúan deshabilitados/no implementados.
- Search Console continúa sin token auténtico y analytics externa permanece deshabilitada.

## Nuevo ciclo abierto

**v7.0 — Legal Intelligence Architecture / fase de prototipo.**

Rama de trabajo:

`feat/v700-legal-intelligence-architecture`

Motivo observable de negocio:

Meridiano necesita hacer visible de forma ordenada una capacidad que hoy está distribuida entre Diagnóstico, Dirección Jurídica Externa, Contratación, Tecnología/IA, Proyectos Regulados y Legal Operations: diagnosticar, transformar y operar trabajo jurídico utilizando criterio legal, procesos, IA, automatización y Legal Engineering.

El objetivo no es añadir más productos al catálogo. Es crear una capa comercial integrada que permita comprender esa capacidad y conectarla con las 16 ofertas canónicas existentes.

## Decisión arquitectónica

Ver:

- `knowledge/10_DECISIONES/ADR-007-legal-intelligence-architecture-v7.md`;
- `knowledge/20_ARQUITECTURA/LEGAL-INTELLIGENCE-MAP-v7.md`;
- `knowledge/20_ARQUITECTURA/LEGAL-INTELLIGENCE-CONTENT-v7.md`;
- `knowledge/20_DESIGN/LEGAL-INTELLIGENCE-v7-BRIEF.md`;
- `assets/data/v7/legal-intelligence-architecture-v70.json`.

La familia se denomina **Meridiano Legal Intelligence** bajo la marca madre Meridiano Legal.

Arquitectura inicial:

1. Legal AI Diagnostic.
2. Legal AI Transformation.
3. Meridiano Legal Desk.
4. Contract Control.
5. Regulatory Control.
6. AI Governance 360.
7. Legal Engineering Studio.
8. Meridiano Counsel como concepto futuro/no producto público todavía.

## Reglas del ciclo

- no duplicar `catalog-products-v41/*.json` ni `catalog-services-v42/*.json`;
- no modificar masivamente las 46 superficies antes de probar una superficie representativa;
- no publicar tarifas nuevas;
- no prometer portal/SaaS/capabilities tecnológicas inexistentes;
- Contract Control y Regulatory Control permanecen como patrones de implementación/operación hasta que exista producto verificable;
- Meridiano Counsel no se comercializa todavía como producto;
- Legal Desk se presenta como managed legal service y sus SLA/canales/capacidad se definen por alcance;
- preservar navegación situation-first del Experience System v6;
- conservar un único formulario físico;
- no relajar validators, E2E, axe o budgets.

## Gate nuevo

`scripts/validate_legal_intelligence_v70.py`

Contrato:

`assets/data/v7/legal-intelligence-architecture-v70.json`

Workflow dedicado:

`.github/workflows/v70-legal-intelligence-architecture.yml`

El gate v7 inicial valida arquitectura y capability truth; todavía no materializa HTML público ni cambia la versión visible.

## Próxima iteración

Prototipar la nueva capa comercial en superficies representativas, no en toda la web:

1. `soluciones/ordenar-operacion-juridica.html` como entrada natural a Legal Intelligence;
2. `servicios/legal-operations.html` para transición hacia Legal Desk;
3. `productos/sistema-contractual-empresarial.html` para explicar Implementar → Contract Control → Contract Desk;
4. P05/S06 para explicar AI Governance Readiness → 360 → Managed.

La iteración debe ser source-driven, reversible y revisar desktop, mobile, teclado, reduced motion y capability truth antes de propagarse.

## Criterio para pasar de prototipo a release pública

No cambiar `version.json` desde 6.3.0 hasta demostrar que la nueva arquitectura:

- reduce confusión en lugar de añadir nomenclatura;
- preserva la profundidad jurídica existente;
- hace evidente qué compra el cliente y qué cambia después;
- no duplica ofertas ni inventa capabilities;
- supera los gates actuales y los nuevos controles v7;
- obtiene crítica independiente sobre claridad, confianza y densidad móvil.

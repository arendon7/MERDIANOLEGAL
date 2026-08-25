# v8 — Canon de oferta pública

Fecha: 2026-08-25
Estado: W4.1 — contrato de arquitectura comercial. No modifica todavía HTML productivo.
Baseline: v7.4.0 certified.

## 1. Objetivo

Definir qué representa cada familia v8 y qué fuentes existentes la soportan, evitando que el rediseño invente capacidad, alcance o evidencia.

La primera lectura pública se organiza en:

- **Prácticas** — expertise y capacidad profesional.
- **Soluciones** — intervenciones con alcance/resultados definidos.
- **Servicios continuos** — capacidad recurrente.

Los catálogos v4.1/v4.2 siguen siendo truth layer durante la migración.

---

## 2. Prácticas — contrato común

Una práctica no es un paquete cerrado ni una promesa de disponibilidad ilimitada.

Cada práctica debe responder:

1. qué decisiones jurídicas cubre;
2. en qué situaciones participa Meridiano;
3. qué tipos de trabajo puede estructurar;
4. cómo se relaciona con negocio/operación;
5. qué soluciones cerradas se apoyan en esa práctica;
6. qué límites o especialidades externas pueden ser necesarias;
7. cómo presentar una necesidad.

Una práctica no debe copiar todos los perímetros cuantificados de las soluciones. Su función es demostrar expertise, campo de intervención y capacidad de estructuración.

### PR01 — Contratación y Negocios

Fuente primaria: `catalog-services-v42/s03-contratos.json`.

Capacidades soportadas:

- estructuración contractual;
- revisión;
- negociación;
- asignación de riesgos;
- anexos relacionados;
- administración/transferencia de obligaciones;
- incumplimiento, renegociación y salida dentro del alcance pactado.

Relacionados principales:

- Sistema Contractual Empresarial;
- Dirección Jurídica Externa;
- Legal Operations.

No convertir en claim de CLM autónomo o negociación ilimitada.

### PR02 — Corporativo, Societario y Gobierno

Fuente primaria: `catalog-services-v42/s04-societario.json`.

Debe cubrir, según la fuente vigente:

- estructura societaria;
- gobierno;
- decisiones corporativas;
- socios;
- inversión;
- instrumentos/documentación relacionada;
- coordinación de decisiones y aprobaciones.

Relacionado principal: Empresa Lista para Inversión.

No inventar capacidad financiera, tributaria o de banca de inversión.

### PR03 — Propiedad Intelectual y Activos Intangibles

Fuente primaria: `catalog-services-v42/s05-intangibles.json`.

Debe presentar protección y organización jurídica de:

- marcas;
- software;
- contenidos;
- know-how;
- derechos/cesiones/licencias;
- cadenas de titularidad;
- confidencialidad y activos intangibles cuando la fuente lo soporte.

Relacionado principal: Sistema de Protección de Activos Intangibles.

No convertir experiencia jurídica en promesa de registro/concesión por autoridad.

### PR04 — Tecnología, Datos e Inteligencia Artificial

Fuente primaria: `catalog-services-v42/s06-tecnologia-ia.json`.
Capas complementarias: contratos v7 de Legal Intelligence cuando sean compatibles con capability truth.

Debe distinguir claramente:

- asesoría jurídica sobre tecnología/IA;
- gobierno y controles;
- contratos/licencias/datos;
- Legal Engineering cuando se pacta;
- demo/diagnóstico vs capability productiva.

Relacionado principal: Programa de Gobernanza de IA y Programa de Cumplimiento Digital.

No prometer auditoría técnica, ciberseguridad, monitoreo universal o decisión jurídica autónoma.

### PR05 — Regulación, Infraestructura y Proyectos

Fuente primaria: `catalog-services-v42/s07-regulados.json`.
Apoyo editorial/sectorial: perspectivas y sectores regulados existentes.

Debe explicar intervención en:

- secuencia regulatoria;
- permisos/autoridades cuando corresponda;
- arquitectura contractual y de riesgo del proyecto;
- decisiones de viabilidad jurídica;
- relación entre regulación, operación y cronograma.

Relacionado principal: Proyecto Regulado Estructurado.

No garantizar licencia, permiso, aprobación o resultado administrativo.

### PR06 — Legal Operations y Transformación Jurídica

Fuente primaria: `catalog-services-v42/s08-legal-ops.json`.
Capas complementarias: v6/v7 de experiencia/Legal Intelligence únicamente en su boundary vigente.

Debe cubrir:

- procesos jurídicos;
- intake;
- priorización;
- roles;
- métricas permitidas;
- repositorios/controles;
- automatización o tecnología solo cuando exista y se pacte;
- mejora del modelo operativo jurídico.

Relacionados principales:

- Sistema Contractual Empresarial;
- Dirección Jurídica Externa;
- Legal Engineering cuando corresponda.

No convertir Legal Operations en software autónomo por defecto.

---

## 3. Soluciones — contrato común

Una solución v8 es una intervención con resultado y perímetro entendibles antes de contratar.

Template conceptual obligatorio:

1. problema/decisión;
2. para quién encaja/no encaja;
3. resultado;
4. entregables;
5. perímetro;
6. proceso;
7. participación del cliente;
8. tiempos;
9. criterios de aceptación;
10. límites;
11. variables de alcance/suplementos;
12. siguiente paso;
13. profundidad jurídica y relacionados.

### SO01 — Diagnóstico Jurídico Empresarial

Fuentes: `p01-auditoria.json` + reconciliación explícita con `s01-diagnostico.json`.

Estado: requiere parity matrix P01/S01 antes del renderer final.

### SO02 — Empresa Jurídicamente Organizada

Fuente: `p02-organizada.json`.

### SO03 — Sistema de Protección de Activos Intangibles

Fuente: `p03-intangibles.json`.
Naming v8 describe el resultado/sistema y no altera el perímetro de fuente.

### SO04 — Empresa Lista para Inversión

Fuente: `p04-inversion.json`.

### SO05 — Programa de Gobernanza de IA

Fuente: `p05-ia.json`.
Debe preservar límites frente a seguridad, auditoría técnica y evaluación científica.

### SO06 — Proyecto Regulado Estructurado

Fuente: `p06-regulado.json`.

### SO07 — Sistema Contractual Empresarial

Fuente: `p07-contractual.json`.

Esta solución instala capacidad institucional contractual: taxonomía, modelos, módulos, playbook, atribuciones, procedimiento, inventario, obligaciones, fichas, piloto y capacitaciones según perímetro vigente.

No debe confundirse con Meridiano Contratos: SO07 es **implementación de sistema**; Meridiano Contratos sería **continuidad recurrente** si y cuando su contract truth sea aprobado.

### SO08 — Programa de Cumplimiento Digital

Fuente: `p08-datos-consumidor.json`.
El naming v8 puede agrupar datos/consumidor/canales digitales solo si el contenido de fuente soporta cada claim visible.

---

## 4. Servicios continuos

### RC01 — Dirección Jurídica Externa

Fuente: `catalog-services-v42/s02-direccion.json`.

Debe explicarse como capacidad jurídica recurrente pactada, con:

- gobierno/priorización;
- alcance;
- roles;
- capacidad y canales;
- tiempos/SLA únicamente si están definidos;
- exclusiones;
- escalamiento de asuntos extraordinarios.

No describirla como disponibilidad jurídica ilimitada.

### RC02 — Meridiano Contratos

Estado: **nuevo contrato pendiente; no publicable todavía como capability cerrada**.

Hipótesis comercial a validar:

> continuidad contractual para empresas que necesitan generar, mantener y revisar contratos recurrentes sobre modelos gobernados, con actualización y escalamiento de excepciones bajo revisión jurídica humana.

Antes de pasar de hipótesis a oferta se debe definir:

#### Unidad económica

- número de contratos/documentos incluidos;
- periodicidad;
- rollover o no;
- anexos;
- rondas;
- excepciones;
- negociaciones extraordinarias;
- actualización de modelos.

#### Operación

- intake;
- variables requeridas;
- generación;
- revisión;
- aprobación;
- entrega;
- versionado;
- archivo;
- mantenimiento.

#### Tecnología

- qué interfaz real usa el cliente;
- autenticación real;
- dónde se almacenan datos/documentos;
- permisos;
- disponibilidad;
- seguridad;
- logging;
- soporte;
- límites.

#### Boundary jurídico

- documento automatizado no equivale a asesoría ilimitada;
- cambios materiales/excepciones requieren revisión;
- negociación con contraparte puede ser suplemento;
- no garantizar aceptación/ejecución;
- no asumir firma, pago o cumplimiento por defecto.

Hasta cerrar estos puntos, el sitio puede hablar de **continuidad contractual como dirección de producto**, pero no de una plataforma productiva específica ni de unidades comerciales inventadas.

---

## 5. Relación entre familias

```text
PRÁCTICA
expertise y capacidad
      │
      ├── estructura SOLUCIONES cerradas
      │
      └── soporta SERVICIOS CONTINUOS

SOLUCIÓN
instala sistema / resuelve intervención definida
      │
      └── puede continuar en servicio recurrente

SERVICIO CONTINUO
mantiene capacidad / opera excepciones / continuidad
```

Ejemplo contractual:

```text
Contratación y Negocios
        ↓
Sistema Contractual Empresarial
        ↓
Meridiano Contratos / Dirección Jurídica Externa
```

La secuencia es una posibilidad comercial, no una obligación ni un funnel automático.

---

## 6. Reglas de copy v8

Toda oferta debe permitir responder rápidamente:

1. ¿Qué problema resuelve?
2. ¿Qué obtiene la empresa?
3. ¿Qué está incluido?
4. ¿Qué queda por fuera?
5. ¿Qué necesita Meridiano del cliente?
6. ¿Cómo se cierra/acepta el trabajo?
7. ¿Cuál es el siguiente paso?

Evitar:

- lenguaje genérico de “acompañamiento integral” sin perímetro;
- claims de IA sin función concreta;
- términos de software para servicios humanos;
- listas de áreas jurídicas sin resultado;
- “360” como sustituto de alcance verificable;
- verbos que impliquen garantía regulatoria o comercial.

---

## 7. Definition of Done W4.1 para oferta

- 6/6 prácticas con fuente identificada;
- 8/8 soluciones con fuente identificada;
- 1/1 servicio continuo existente con fuente identificada;
- Meridiano Contratos marcado explícitamente como contract pendiente;
- P01/S01 identificado como conflicto de consolidación a resolver;
- 46/46 rutas clasificadas en matriz;
- ninguna capability nueva activada;
- `stable` intacta.

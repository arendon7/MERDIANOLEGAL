# v8 — Matriz canónica de migración de rutas

Fecha: 2026-08-25
Estado: W4.1 — arquitectura/migración. **No es release ni cambia producción.**
Baseline: v7.4.0 / `main == stable == 86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
ADR relacionada: `knowledge/10_DECISIONES/ADR-008-v8-client-architecture-taxonomy.md`.

## 1. Regla de lectura

Esta matriz cubre las **46 superficies HTML** detectadas por Graphify y el árbol de `main`.

Estados:

- `KEEP`: misma función y, por defecto, misma ruta.
- `RENAME`: cambia naming/posición, no obliga a mover la URL en la primera wave.
- `MOVE`: se propone nueva ruta canónica; la URL legacy debe sobrevivir como alias compatible hasta cierre SEO.
- `MERGE`: intención/contenido se absorbe en otro destino canónico.
- `ALIAS`: la ruta deja de ser experiencia primaria pero debe resolver correctamente.
- `REVIEW`: no ejecutar hasta cerrar capability/SEO/UX correspondiente.

**Principio de rollout:** ninguna URL legacy se elimina en la misma wave en que nace su nuevo destino.

---

## 2. Top-level — 9 superficies

| ID | Ruta actual | Función v7.4 | Destino v8 | Acción | SEO/compatibilidad | Template v8 | Prioridad |
|---|---|---|---|---|---|---|---|
| T01 | `/` | Home | `/` | KEEP + REDESIGN | canonical actual | Home client-first | P0 |
| T02 | `/firma.html` | Firma/autoridad | `/firma.html` | KEEP | canonical actual | Firma editorial | P2 |
| T03 | `/experiencia.html` | Experiencia/cómo trabajamos | `/experiencia.html` inicialmente; naming visible `Cómo trabajamos` | RENAME | mantener URL en v8.0; revisar move posterior | Evidence/Method | P2 |
| T04 | `/demo.html` | Centro demostrativo | `/demo.html` como evidencia secundaria | KEEP + REFRAME | no indexarlo como portal; preservar capability disclaimer | Demo explícita | P2 |
| T05 | `/perspectivas.html` | Hub editorial | `/perspectivas.html` | KEEP + RENAME opcional a `Insights / Perspectivas` | canonical actual | Editorial hub | P2 |
| T06 | `/aviso-legal.html` | Aviso legal | igual | KEEP | canonical actual | Legal | P3 |
| T07 | `/privacidad.html` | Privacidad | igual | KEEP | canonical actual; actualizar solo si cambia tratamiento | Legal | P3 |
| T08 | `/terminos.html` | Términos | igual | KEEP | canonical actual | Legal | P3 |
| T09 | `/404.html` | Recuperación | igual | KEEP + REDESIGN | no sitemap; enlaces de recuperación v8 | 404 | P3 |

---

## 3. Productos actuales → Soluciones — 8 superficies

Las fuentes `catalog-products-v41` siguen siendo truth layer hasta que exista un reemplazo v8 con parity demostrada.

| ID | Ruta actual | Nombre actual | Familia v8 | Destino canónico propuesto | Acción | Fuente | Prioridad |
|---|---|---|---|---|---|---|---|
| P01 | `/productos/diagnostico-juridico-empresarial.html` | Diagnóstico Jurídico Empresarial Integral | Solución | `/soluciones/diagnostico-juridico-empresarial.html` | MOVE + ALIAS | `p01-auditoria.json` | P0 |
| P02 | `/productos/empresa-juridicamente-organizada.html` | Empresa Jurídicamente Organizada | Solución | `/soluciones/empresa-juridicamente-organizada.html` | MOVE + ALIAS | `p02-organizada.json` | P1 |
| P03 | `/productos/activos-intangibles-protegidos.html` | Activos Intangibles Protegidos | Solución | `/soluciones/sistema-proteccion-activos-intangibles.html` | MOVE + RENAME + ALIAS | `p03-intangibles.json` | P1 |
| P04 | `/productos/empresa-lista-para-inversion.html` | Empresa Lista para Inversión | Solución | `/soluciones/empresa-lista-para-inversion.html` | MOVE + ALIAS | `p04-inversion.json` | P1 |
| P05 | `/productos/programa-gobernanza-ia.html` | Programa de Gobernanza de IA | Solución | `/soluciones/programa-gobernanza-ia.html` | MOVE + ALIAS | `p05-ia.json` | P1 |
| P06 | `/productos/proyecto-regulado-estructurado.html` | Proyecto Regulado Estructurado | Solución | `/soluciones/proyecto-regulado-estructurado.html` | MOVE + ALIAS | `p06-regulado.json` | P1 |
| P07 | `/productos/sistema-contractual-empresarial.html` | Sistema Contractual Empresarial | Solución | `/soluciones/sistema-contractual-empresarial.html` | MOVE + ALIAS | `p07-contractual.json` | P0 |
| P08 | `/productos/proteccion-datos-consumidor.html` | Protección de Datos y Consumidor | Solución | `/soluciones/programa-cumplimiento-digital.html` | MOVE + RENAME + ALIAS | `p08-datos-consumidor.json` | P1 |

### Regla de parity para las 8 soluciones

Cada nuevo destino debe conservar en significado:

- problema/pregunta;
- resultado;
- situaciones de encaje;
- alcance;
- perímetro cuantificado;
- método;
- entregables;
- formatos;
- timeline;
- requisitos;
- responsabilidades;
- aceptación;
- límites;
- suplementos/relacionados.

No se permite simplificar el DOM eliminando profundidad material.

---

## 4. Servicios actuales → Prácticas / recurrentes / merge — 8 superficies

| ID | Ruta actual | Nombre actual | Familia v8 | Destino canónico propuesto | Acción | Fuente | Prioridad |
|---|---|---|---|---|---|---|---|
| S01 | `/servicios/diagnostico-juridico-empresarial.html` | Diagnóstico Jurídico Empresarial | Solución | `/soluciones/diagnostico-juridico-empresarial.html` | MERGE + ALIAS | `s01-diagnostico.json` + P01 | P0 |
| S02 | `/servicios/direccion-juridica-externa.html` | Dirección Jurídica Externa | Servicio continuo | `/servicios-continuos/direccion-juridica-externa.html` | MOVE + ALIAS | `s02-direccion.json` | P0 |
| S03 | `/servicios/contratacion-estrategica.html` | Contratación Estratégica y Gestión Contractual | Práctica | `/practicas/contratacion-negocios.html` | MOVE + RENAME + ALIAS | `s03-contratos.json` | P0 |
| S04 | `/servicios/sociedades-gobierno-inversion.html` | Sociedades, Gobierno e Inversión | Práctica | `/practicas/corporativo-societario-gobierno.html` | MOVE + RENAME + ALIAS | `s04-societario.json` | P0 |
| S05 | `/servicios/propiedad-intelectual.html` | Propiedad Intelectual | Práctica | `/practicas/propiedad-intelectual-activos-intangibles.html` | MOVE + RENAME + ALIAS | `s05-intangibles.json` | P1 |
| S06 | `/servicios/tecnologia-inteligencia-artificial.html` | Tecnología e Inteligencia Artificial | Práctica | `/practicas/tecnologia-datos-inteligencia-artificial.html` | MOVE + EXPAND NAMING + ALIAS | `s06-tecnologia-ia.json` | P0 |
| S07 | `/servicios/proyectos-regulados.html` | Proyectos Regulados | Práctica | `/practicas/regulacion-infraestructura-proyectos.html` | MOVE + EXPAND NAMING + ALIAS | `s07-regulados.json` | P1 |
| S08 | `/servicios/legal-operations.html` | Legal Operations | Práctica | `/practicas/legal-operations-transformacion-juridica.html` | MOVE + EXPAND NAMING + ALIAS | `s08-legal-ops.json` | P0 |

### Nota S01

El servicio de diagnóstico no se borra sin reconciliar diferencias de alcance frente a P01. La nueva solución deberá definir qué elementos de S01 son:

- intake/diagnóstico previo;
- componente incluido en P01;
- servicio extraordinario separado;
- o contenido duplicado a consolidar.

Hasta esa reconciliación, ambas fuentes siguen siendo autoridad histórica.

---

## 5. Soluciones/necesidades actuales — 7 superficies

| ID | Ruta actual | Intención v7.4 | Destino v8 | Acción | Compatibilidad | Prioridad |
|---|---|---|---|---|---|---|
| N00 | `/soluciones/` | Hub de necesidades | `/soluciones/` | KEEP + REDESIGN | se convierte en hub de las 8 soluciones | P0 |
| N01 | `/soluciones/ordenar-riesgo-juridico-empresa.html` | Ordenar riesgo jurídico | `/soluciones/diagnostico-juridico-empresarial.html` | MERGE + ALIAS | preservar copy/SEO útil como intent landing o alias | P1 |
| N02 | `/soluciones/direccion-juridica-externa-empresa.html` | Obtener capacidad jurídica recurrente | `/servicios-continuos/direccion-juridica-externa.html` | MERGE + ALIAS | preservar intención de búsqueda | P1 |
| N03 | `/soluciones/preparar-empresa-para-inversion.html` | Preparar inversión | `/soluciones/empresa-lista-para-inversion.html` | MERGE + ALIAS | preservar intención de búsqueda | P1 |
| N04 | `/soluciones/gobernar-inteligencia-artificial-empresa.html` | Gobernar IA | `/soluciones/programa-gobernanza-ia.html` | MERGE + ALIAS | preservar intención de búsqueda | P1 |
| N05 | `/soluciones/estructurar-proyecto-regulado.html` | Estructurar proyecto regulado | `/soluciones/proyecto-regulado-estructurado.html` | MERGE + ALIAS | preservar intención de búsqueda | P1 |
| N06 | `/soluciones/ordenar-operacion-juridica.html` | Ordenar operación jurídica | `/practicas/legal-operations-transformacion-juridica.html` | MERGE + ALIAS | puede mantenerse como intent landing si aporta SEO distinto | P1 |

### Regla para intent landings

`MERGE` no significa necesariamente borrar el archivo. W4.2 debe decidir por evidencia si una ruta legacy funciona mejor como:

1. alias técnico mínimo;
2. intent landing útil con canonical propio;
3. intent landing con canonical al destino principal;
4. redirección compatible.

No decidir por intuición ni duplicar contenido sustancial sin propósito.

---

## 6. Sectores — 8 superficies

| ID | Ruta actual | Rol v8 | Destino propuesto | Acción | Cluster | Prioridad |
|---|---|---|---|---|---|---|
| C01 | `/sectores/agroindustria-fertilizantes-sostenibilidad.html` | Especialidad/subsector | misma ruta inicialmente | KEEP + REPOSITION | Ambiente / Empresas según contexto | P2 |
| C02 | `/sectores/comercio-distribucion.html` | Sector | `/sectores/empresas-comercio-grupos-empresariales.html` | MOVE + EXPAND + ALIAS | Empresas, comercio y grupos empresariales | P2 |
| C03 | `/sectores/operaciones-juridicas.html` | No es sector primario | `/practicas/legal-operations-transformacion-juridica.html` | MERGE + ALIAS | Legal Operations | P2 |
| C04 | `/sectores/proyectos-publicos-territoriales.html` | Sector | `/sectores/servicios-publicos-infraestructura-proyectos.html` | MERGE/PARTIAL + ALIAS | Servicios públicos, infraestructura y proyectos públicos | P2 |
| C05 | `/sectores/salud-negocios-regulados.html` | Sector | `/sectores/salud-ciencias-vida.html` | MOVE + EXPAND + ALIAS | Salud y ciencias de la vida | P2 |
| C06 | `/sectores/servicios-publicos-aseo-economia-circular.html` | Sector/especialidad | `/sectores/ambiente-residuos-economia-circular.html` | MOVE + REFOCUS + ALIAS | Ambiente, residuos y economía circular | P2 |
| C07 | `/sectores/startups-inversion.html` | Sector | misma ruta | KEEP | Startups e inversión | P2 |
| C08 | `/sectores/tecnologia-software-ia.html` | Sector | `/sectores/tecnologia-economia-digital.html` | MOVE + EXPAND + ALIAS | Tecnología y economía digital | P2 |

### Riesgo sectorial a resolver

C04 y C06 hoy contienen material que puede cruzarse entre servicios públicos, proyectos públicos, ambiente, aseo y economía circular. Antes de mover contenido debe hacerse un inventario párrafo/claim → nuevo cluster para evitar perder autoridad sectorial real.

---

## 7. Perspectivas internas — 6 superficies

Los artículos se preservan; la migración es principalmente visual, de metadata, categorías e internal linking.

| ID | Ruta actual | Acción | Categoría v8 sugerida | Template | Prioridad |
|---|---|---|---|---|---|
| I01 | `/perspectivas/contratos-administrables.html` | KEEP | Contratos | Editorial article | P2 |
| I02 | `/perspectivas/gobierno-juridico-inteligencia-artificial.html` | KEEP | IA / Gobierno | Editorial article | P2 |
| I03 | `/perspectivas/legal-operations-modelo-operativo.html` | KEEP | Legal Operations | Editorial article | P2 |
| I04 | `/perspectivas/propiedad-intelectual-cadena-titularidad.html` | KEEP | PI / Intangibles | Editorial article | P2 |
| I05 | `/perspectivas/proyectos-regulados-secuencia-viabilidad.html` | KEEP | Regulación / Proyectos | Editorial article | P2 |
| I06 | `/perspectivas/socios-inversion-gobierno.html` | KEEP | Corporativo / Inversión | Editorial article | P2 |

---

## 8. Resultado de cobertura

Cobertura W4.1:

- top-level: **9/9**;
- productos: **8/8**;
- servicios: **8/8**;
- soluciones/necesidades: **7/7**;
- sectores: **8/8**;
- perspectivas internas: **6/6**;
- total: **46/46**.

No existe ninguna superficie legacy sin clasificación.

---

## 9. Nuevas superficies v8 fuera del baseline 46

Estas rutas **no existen todavía** y no deben añadirse hasta cambiar conscientemente el contrato estructural y sus validators.

### N1 — Meridiano Contratos

Destino propuesto:

`/servicios-continuos/meridiano-contratos.html`

Estado: `REVIEW / capability contract required`.

Debe definir antes de implementación:

- qué recibe el cliente;
- frecuencia y unidades incluidas;
- biblioteca/modelos disponibles;
- quién solicita y quién aprueba;
- dónde ocurre la generación;
- revisión humana;
- versionado;
- mantenimiento normativo;
- excepciones y negociación extraordinaria;
- seguridad y tratamiento de documentos;
- disponibilidad/SLA si se promete;
- límites tecnológicos reales.

### N2 — Hubs opcionales

Posibles hubs:

- `/practicas/`;
- `/servicios-continuos/`;
- `/sectores/`.

No se aprueban automáticamente. Si el header/dropdown resuelve descubrimiento sin añadir thin pages, pueden omitirse.

---

## 10. Navegación objetivo provisional

Primer nivel candidato:

1. `Cómo podemos ayudar` — entrada por decisión/situación.
2. `Soluciones` — 8 soluciones.
3. `Prácticas` — 6 prácticas.
4. `Sectores` — clusters.
5. `Perspectivas` — conocimiento.
6. `Firma`.
7. CTA: `Presentar necesidad`.

`Servicios continuos` puede vivir dentro de `Cómo podemos ayudar` o `Soluciones` hasta que el prototipo demuestre si merece primer nivel propio.

No crear una navegación más larga que la actual solamente porque existen más categorías internas.

---

## 11. Orden de ejecución derivado

### Wave A — P0 pilotos

- Home.
- P07 → Sistema Contractual Empresarial.
- S04 → Corporativo, Societario y Gobierno.
- S02 → Dirección Jurídica Externa.
- S03/S06/S08 como fuentes de prueba de prácticas.

### Wave B — soluciones restantes

P01–P06/P08 con truth parity.

### Wave C — prácticas restantes

S03–S08, excluyendo S01 ya consolidado y S02 recurrente.

### Wave D — intent landings y aliases

N01–N06 + legacy `/productos/` y `/servicios/`.

### Wave E — sectores/perspectivas/firma

C01–C08, I01–I06, T02–T05.

### Wave F — legales/404

T06–T09.

---

## 12. Gates antes de ejecutar rutas nuevas

W4.2 debe producir y probar:

1. estrategia de alias/redirect compatible con GitHub Pages;
2. canonical policy por tipo de legacy URL;
3. sitemap target;
4. breadcrumb target;
5. política para intent landings;
6. actualización segura del validator de 46 HTML;
7. actualización de E2E de rutas sin silenciar checks;
8. smoke de URLs legacy;
9. noindex/canonical rules de demo/aliases si aplican;
10. rollback a v7.4 certificado.

Hasta que W4.2 cierre, **no se borran ni mueven archivos productivos**.

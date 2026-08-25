# W4.3 — v8 Renderer & Design-System Pilot Infrastructure

Fecha: 2026-08-25
Estado: infraestructura no pública.
Baseline productivo: v7.4.0 / `86813813e29dd6b47105ba7fb6259630fcd9cb5b`.
Dependencias: W4.1 + W4.2.

## 1. Problema que resuelve W4.3

La arquitectura v8 ya define nuevas familias y rutas, pero materializar páginas directamente sobre los generadores históricos produciría dos riesgos:

1. duplicar la verdad jurídica en nuevas fuentes de contenido;
2. activar parcialmente una arquitectura que todavía no ha probado renderer, design system, truth parity y compatibilidad.

W4.3 resuelve primero la infraestructura sin tocar las 46 superficies productivas.

---

## 2. Decisión de arquitectura

La cadena v8 piloto es:

```text
catálogo canónico v4.1 / v4.2
          │
          ▼
experience-model-v80.json
(solo semántica, familia y rutas)
          │
          ▼
render_v8_pilot.py
          │
          ├── --check  → truth parity en memoria
          └── --preview → HTML candidato a stdout

route-contract-v80.json
          │
          └── traduce enlaces legacy → target v8

assets/css/v8/
          └── tokens + base + components + surfaces
```

No existe en W4.3 una segunda copia de `summary`, `scope`, `perimeter`, `deliverables`, `limits`, etc.

---

## 3. Experience model

Archivo:

`assets/data/v8/experience-model-v80.json`

### Contiene

- definición semántica de las familias `solution`, `practice`, `recurring`;
- orden de primera capa y profundidad;
- referencias a las fuentes canónicas;
- legacy route;
- target route;
- commercial contract histórico que debe preservarse durante piloto;
- política de no activación.

### No contiene

- texto jurídico duplicado;
- precios;
- claims tecnológicos nuevos;
- portal/auth;
- HTML;
- estilos.

---

## 4. Pilotos

### SO07 — Sistema Contractual Empresarial

Fuente:

`catalog-products-v41/p07-contractual.json`

Familia:

`solution`

Razón de selección:

- perímetro cuantificado;
- entregables numerosos;
- playbook/modelos/obligaciones;
- diferencia clara entre implementar un sistema y prestar capacidad recurrente;
- superficie crítica para la futura continuidad contractual.

### PR02 — Corporativo, Societario y Gobierno

Fuente:

`catalog-services-v42/s04-societario.json`

Familia:

`practice`

Razón:

- trabajo adaptable/transaccional;
- no debe parecer paquete cerrado;
- permite probar scope, decisiones y coordinación con otros asesores.

### RC01 — Dirección Jurídica Externa

Fuente:

`catalog-services-v42/s02-direccion.json`

Familia:

`recurring`

Razón:

- gobierno recurrente;
- bolsa/capacidad;
- usuarios;
- comité;
- SLA pactado;
- tablero vivo;
- límites explícitos de disponibilidad.

RC02 Meridiano Contratos permanece fuera de alcance.

---

## 5. Renderer

Archivo:

`scripts/render_v8_pilot.py`

### `--check`

Debe:

1. cargar experience model y route contract;
2. comprobar que solo existen SO07, PR02 y RC01;
3. comprobar una familia de cada tipo;
4. cargar directamente la fuente canónica;
5. verificar `productV41` / `serviceV42` según corresponda;
6. exigir todos los campos materiales;
7. renderizar dos veces y exigir igualdad exacta;
8. exigir `noindex,follow`;
9. impedir segundo formulario;
10. impedir claims prohibidos;
11. comprobar que todos los textos materiales están presentes en el DOM generado;
12. resolver relacionados hacia target routes v8;
13. mantener CTA hacia el único formulario de Home usando el commercial contract histórico.

### `--preview ID`

Genera HTML únicamente por stdout.

No escribe al repositorio.

### Decisión deliberada

No existe `--write` en W4.3.

La materialización física será otra wave y requerirá un contrato explícito.

---

## 6. Truth parity

Campos que deben preservarse:

- summary;
- duration;
- modality;
- audience;
- question;
- result;
- situations;
- scope;
- perimeter;
- method;
- deliverables;
- formats;
- timeline;
- requirements;
- responsibilities;
- acceptance;
- limits;
- supplements;
- related.

El renderer puede cambiar:

- orden visual;
- heading visible;
- composición;
- disclosure;
- naming de familia;
- rutas relacionadas.

No puede cambiar silenciosamente:

- cantidades;
- límites;
- resultado material;
- condiciones de aceptación;
- responsabilidades;
- exclusiones;
- horizonte;
- modalidad contractual.

---

## 7. Design system v8

Carpeta:

`assets/css/v8/`

### `tokens.css`

Preserva la identidad cromática ya certificada:

- navy `#13263a`;
- navy deep `#091725`;
- blue `#2c5878`;
- ivory `#f5f1e8`;
- gold `#a88454`;
- gold light `#d9bc8b`.

Normaliza:

- typography scale;
- spacing;
- widths;
- radius;
- shadows;
- focus;
- motion;
- z-index.

### `base.css`

Contiene:

- reset mínimo;
- tipografía;
- lectura;
- focus visible;
- skip link;
- containers;
- responsive base;
- reduced motion.

### `components.css`

Componentes semánticos:

- eyebrow;
- actions/buttons;
- meta ledger;
- index rows;
- outcome;
- deliverable/perimeter ledger;
- timeline;
- boundary;
- disclosure;
- related links.

### `surfaces.css`

Diferencia visualmente:

- solution;
- practice;
- recurring.

No crea tres marcas diferentes. Comparte la misma gramática y utiliza énfasis funcional distinto.

---

## 8. Principios visuales

### Menos cardification

No convertir cada concepto en tarjeta.

Usar:

- líneas editoriales;
- ledgers;
- índices;
- timelines;
- bandas de límites;
- disclosure nativo.

### Jerarquía jurídica, no decorativa

Primera lectura:

1. decisión;
2. resultado;
3. encaje;
4. qué recibe;
5. perímetro;
6. método;
7. participación;
8. aceptación;
9. límites;
10. siguiente paso.

### Profundidad disponible

La primera capa no elimina profundidad. Scope detallado, formatos, responsabilidades, extensiones y relacionados permanecen en DOM dentro de disclosure accesible.

### Mobile

No convertir automáticamente grids desktop en carrusel horizontal.

El sistema colapsa a:

- una columna;
- índices lineales;
- ledgers apilados;
- botones full-width cuando corresponde.

---

## 9. Gate de no activación

Archivo:

`scripts/validate_v8_pilot_infra.py`

Comprueba:

- experience model existe;
- cuatro CSS v8 existen;
- exactamente tres pilotos;
- targets v8 aún no existen físicamente;
- legacy pilots sí existen;
- total HTML sigue en 46;
- ningún HTML actual referencia `assets/css/v8/`;
- renderer compila;
- renderer `--check` supera truth parity.

Este gate convierte “todavía no lo publicamos” en una condición verificable.

---

## 10. CI

Workflow:

`.github/workflows/v80-pilot-infra-candidate.yml`

Ejecuta:

1. compile;
2. route contract W4.2;
3. pilot infrastructure W4.3;
4. canonical pipeline manifest.

No:

- materializa páginas;
- ejecuta deploy;
- modifica sitemap;
- modifica version.json;
- mueve stable.

---

## 11. Qué no se toca en W4.3

- 46 HTML productivos;
- `index.html`;
- `sitemap.xml`;
- `robots.txt`;
- `version.json`;
- catálogos v4.1/v4.2;
- CSS v6/v7;
- JS productivo;
- formulario;
- analítica;
- privacidad;
- pipeline Builder/Pages;
- stable.

---

## 12. Siguiente wave — W4.4

**Pilot Materialization Candidate.**

Solo cuando W4.3 esté revisada/gated:

1. añadir version-gate v8 al pipeline;
2. habilitar materialización de SO07, PR02 y RC01 en candidate;
3. mantener legacy pages completas;
4. target pages `noindex` durante comparación;
5. crear E2E target;
6. crear legacy smoke;
7. screenshots/visual QA desktop + mobile;
8. keyboard + axe;
9. truth parity DOM;
10. dos pasadas idempotentes;
11. crítica independiente;
12. decidir canonical handoff solo después.

---

## 13. Definition of Done W4.3

- experience model source-driven;
- tres pilotos exactos;
- renderer no destructivo;
- truth parity completa en memoria;
- related links traducidos por route contract;
- cuatro CSS v8 consolidados;
- reduced motion/focus/mobile incorporados;
- gate de no activación;
- CI candidate dedicado;
- 46 HTML actuales intactos;
- target HTML = 0;
- RC02 fuera de scope;
- stable intacta.

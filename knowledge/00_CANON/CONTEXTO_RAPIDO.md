# Meridiano Legal — Contexto rápido

Use esta nota para orientarse antes de abrir archivos fuente.

## Qué es el proyecto

Sitio público y centro demostrativo de Meridiano Legal. Combina servicios jurídicos especializados, productos de alcance cerrado, planes recurrentes, rutas por necesidad, sectores, perspectivas y una experiencia demo estática.

## Arquitectura comercial vigente

- 8 servicios especializados;
- 8 productos de alcance cerrado;
- 5 planes recurrentes;
- 6 rutas de decisión en `soluciones/` más su hub;
- 8 sectores;
- 6 perspectivas más biblioteca;
- Firma/método y Centro Demo;
- v5.8 aporta claridad de compra;
- v5.9 califica momento, horizonte e inversión sin persistencia servidor;
- v5.10 transmite intención contextual y explica propuesta/cierre;
- v5.11 diferencia solicitud, propuesta, aceptación e inicio real;
- v5.12 presenta 5 modalidades y prueba verificable en las 16 fichas profundas.

Principio comercial: el usuario puede empezar por su situación empresarial y no necesita conocer el nombre técnico del servicio correcto.

## Diferenciaciones que no deben perderse

- Diagnóstico jurídico ≠ Auditoría Jurídica Empresarial Integral.
- Dirección Jurídica Externa ≠ disponibilidad jurídica ilimitada.
- Contratación Estratégica ≠ Sistema Contractual Empresarial.
- Sociedades/Gobierno/Inversión ≠ Empresa Lista para Inversión.
- Propiedad Intelectual como servicio ≠ paquete cerrado de activos protegidos.
- Gobernanza jurídica de IA como servicio ≠ programa cerrado de gobernanza.
- Proyecto regulado como servicio ≠ producto estructurado de alcance cerrado.
- Legal Operations ≠ Dirección Jurídica Externa.

## Fuentes principales

- `catalog-products-v41/` y `catalog-services-v42/` — fuente jurídica de productos/servicios;
- `growth-solutions-v51.json`, `cro-solutions-v52.json`, `authority-v53.json`;
- `measurement-contract-v53.json` — eventos sin PII;
- capas `decision-v58`, `commercial-intake-v59`, `conversion-close-v510`, `engagement-v511`;
- `proof-v512.css` + `scripts/apply_proof_v512.py` + `scripts/validate_proof_v512.py` — modalidad y prueba derivada de método, entregables, formatos y aceptación;
- `scripts/validate_pages_trigger_v511.py` — topología builder→Pages sin carrera directa por push;
- `release-governance-v57.json`;
- `tests/e2e/`.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → v5.12 → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

## Estado actual resumido

- Versión declarada en este cierre: v5.12.0.
- Funcionalidad v5.12 certificada en run `31562692907`, SHA `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`.
- Antes del cierre documental: `main == stable` en ese SHA.
- Browser: 35 passed / 2 skipped / 0 failed / 0 retries sobre 37 entradas.
- axe: 7 superficies sin violaciones serias/críticas.
- Lighthouse: 6/6 dentro de budget.
- CI: 187 s hasta `stable`, 33.0% mejor que baseline v5.5 de 279 s.
- Release Governance y trigger builder→Pages: PASS.
- La web no almacena el formulario en servidor y no existe CRM/backend activo.
- No hay aceptación contractual, pagos, agenda, expediente, carga documental ni inicio automático desde la web pública.
- La telemetría no debe contener nombre, correo, empresa ni texto libre del caso.

## Graphify

Antes de este cierre, Graphify está estructuralmente alineado exactamente con `f8c4d1abc38929040f1ce67b04a2c2c4193c3690`: 463 nodos, 725 relaciones y 79 notas. Tras el cierre documental debe verificarse `BUILD_META.source_commit` contra el SHA final; cualquier desfase exclusivamente generado/versionado debe documentarse con comparación verificable.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

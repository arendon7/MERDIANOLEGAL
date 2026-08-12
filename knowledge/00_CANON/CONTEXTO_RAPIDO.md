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
- 4 formas de contratación en portada;
- 5 bloques ejecutivos de compra en cada una de las 16 fichas profundas;
- v5.9 califica momento, horizonte e inversión sin persistencia servidor;
- v5.10 transmite intención contextual y explica propuesta/cierre;
- v5.11 diferencia solicitud preparada, propuesta emitida, propuesta aceptada y encargo iniciado.

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

- `catalog-products-v41/` — productos.
- `catalog-services-v42/` — servicios.
- `growth-solutions-v51.json` — rutas por necesidad.
- `cro-solutions-v52.json` — CRO, objeciones, FAQ e intención de búsqueda.
- `authority-v53.json` — autoridad, interlinking y semántica editorial.
- `measurement-contract-v53.json` — eventos sin PII.
- `decision-v58.css` + applicator/validator — claridad de compra.
- `commercial-intake-v59.*` + applicator/validator — calificación y privacidad.
- `conversion-close-v510.*` + applicator/validator — intención, propuesta y cierre.
- `engagement-v511.css` + `scripts/apply_engagement_v511.py` + `scripts/validate_engagement_v511.py` — aceptación e inicio real del encargo.
- `scripts/validate_pages_trigger_v511.py` — topología builder→Pages sin carrera directa por push.
- `release-governance-v57.json` — Actions, runtimes, dependencias, permisos e invariantes.
- `tests/e2e/` — contrato funcional de navegador.

## Secuencia de release

fuentes → builder canónico → v5.8 → v5.9 → v5.10 → v5.11 → idempotencia/validadores → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

Pages se dispara por `workflow_run` exitoso del builder, no directamente por `push`. Los generadores históricos deben preservar atributos/capas posteriores y la segunda pasada debe quedar sin drift.

## Estado actual resumido

- Versión declarada en este cierre: v5.11.0.
- Funcionalidad v5.11 certificada en run `31560805174`, SHA `cf4341eb9ec051a3e583b4675263b228ee5f0839`.
- Antes del cierre documental: `main == stable` en ese SHA.
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries sobre 37 entradas.
- axe: 7 superficies sin violaciones serias/críticas.
- Lighthouse: 6/6 dentro de budget.
- CI: 193 s hasta `stable`, 30.8% mejor que baseline v5.5 de 279 s.
- `PAGES TRIGGER V5.11 OK`: Pages espera al builder canónico, sin carrera directa por push.
- La web no almacena el formulario en servidor y no existe CRM/backend activo.
- No hay aceptación contractual, pagos, agenda, expediente, carga documental ni inicio automático desde la web pública.
- La telemetría no debe contener nombre, correo, empresa ni texto libre del caso.

## Graphify

Graphify reduce el espacio de búsqueda, no decide la verdad. Confirmar siempre `BUILD_META.source_commit` contra `main` y luego verificar en fuente/tests. Un desfase puramente generado debe quedar documentado con equivalencia verificable.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

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
- calificación comercial v5.9 en el formulario público, con resumen y siguiente paso antes del handoff a WhatsApp.

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
- `decision-v58.css` + `scripts/apply_decision_v58.py` — claridad de compra.
- `commercial-intake-v59.json` — contrato de calificación comercial y privacidad.
- `commercial-intake-v59.css` / `commercial-intake-v59.js` — presentación y runtime de handoff comercial.
- `scripts/apply_commercial_v59.py` — materialización canónica v5.9.
- `scripts/validate_commercial_v59.py` — contrato v5.9 y privacidad.
- `release-governance-v57.json` — policy de Actions, runtimes, dependencias, permisos e invariantes.
- `tests/e2e/` — contrato funcional de navegador.

## Secuencia de release

fuentes → generadores históricos → v5.8 → v5.9 → validadores → idempotencia → Pages → smoke → Browser/axe + Lighthouse → release-health → `stable`.

El builder debe terminar en `v5.8 → v5.9`. El generador v4.9 debe tolerar extensiones posteriores del formulario.

## Estado actual resumido

- Versión declarada en cierre: v5.9.0.
- Fundación funcional v5.9 certificada en run `31547313170`, SHA `a64d2d957e3ca6c96fec855be85019680ebe6a03`.
- Antes del cierre documental: `main == stable` en ese SHA.
- Browser E2E: 35 passed / 2 skipped / 0 failed / 0 retries sobre 37 entradas.
- axe: 7 superficies sin violaciones serias/críticas.
- Lighthouse: 6/6 dentro de budget.
- CI: 196 s hasta `stable`, 29.7% mejor que baseline v5.5 de 279 s.
- v5.9 añade momento de decisión, horizonte e inversión opcional; genera un resumen y sugiere orientación, llamada de alcance o propuesta estructurada.
- No existe scoring de valor del lead ni exclusión automática.
- La web sigue sin almacenar el formulario en servidor y sin CRM/backend.
- La telemetría no debe contener nombre, correo, empresa ni texto libre del caso.
- El cierre documental 5.9.0 solo es definitivo después de repetir la certificación pública y terminar nuevamente con `main == stable`.

## Graphify

Graphify reduce el espacio de búsqueda, no decide la verdad. La rama `knowledge/graphify-live` contiene `BUILD_META.json`, snapshot, reporte y wiki. Confirmar siempre su `source_commit` contra `main` y luego verificar en fuente/tests.

## Regla de continuidad

Antes de explorar masivamente: confirmar refs, leer esta nota + `ESTADO_ACTUAL.md` + `TAREA_ACTIVA.md`, revisar Graphify y abrir únicamente el conjunto mínimo de archivos afectados.

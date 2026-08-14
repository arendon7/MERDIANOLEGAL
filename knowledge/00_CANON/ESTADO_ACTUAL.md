# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release certificada y cerrada: **5.29.0 — funnel observable y confianza contextual**.
- Canal: `github-pages-production-funnel-trust-certified`.
- Builder de cierre documental: `31824748343` — PASS.
- Site Quality and Deploy #375: `31824770838` — PASS.
- Graphify de cierre: `31824748359` — PASS.
- El SHA exacto vigente se lee de `main` y `stable`; al cierre ambos refs deben estar alineados.

## Contrato v5.29

La capa v5.29 materializa un funnel observable de siete etapas (`awareness`, `need`, `offer`, `evidence`, `decision`, `contact`, `handoff`) sobre la telemetría local ya existente. La cola está limitada a 48 eventos en memoria y no introduce persistencia, identificación entre sesiones, fingerprinting ni transporte de red.

Los checkpoints de portada usan un umbral contractual de 5% de superficie visible, compatible con secciones más altas que el viewport móvil. Las 16 fichas profundas se integran al mismo modelo mediante `data-catalog-id`.

La capa no inspecciona valores de formulario. Ninguna señal permite afirmar que un mensaje fue enviado, entregado o leído, que una propuesta fue aceptada, que comenzó un encargo o que existe una conversión a cliente.

Antes de `#contacto` se presenta un `<aside>` compacto de confianza derivado exclusivamente de `professional-authority-v525.json`. El bloque declara expresamente los límites de esa evidencia y preserva la secuencia de `<section>` establecida por v5.28.

## Evidencia de cierre

- generación canónica de 30 pasos: PASS;
- segunda pasada/idempotencia: PASS;
- 37 validaciones estáticas: PASS;
- Release Governance: PASS;
- 16 fichas profundas instrumentadas: PASS;
- GitHub Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: PASS;
- Lighthouse performance/accesibilidad: PASS contra budgets existentes;
- promoción automática de `stable`: PASS;
- budgets relajados: no;
- cobertura reducida: no;
- PII/persistencia/transporte nuevo: no.

La certificación funcional previa al cierre registró **88 tests observados · 86 PASS · 2 SKIP · 0 FAIL · 0 retries**, con 0 violaciones axe serias/críticas en las superficies cubiertas. El ciclo documental `certified` volvió a ejecutar Browser E2E/axe y Lighthouse con resultado PASS.

## Hallazgos corregidos durante v5.29

1. Dos guardias PII inicialmente demasiado amplios (`name:` y `contact-form`) se estrecharon a acceso real de controles/valores, manteniendo las etiquetas semánticas legítimas.
2. Una deriva de whitespace en el `<head>` rompía `git diff --exit-code`; el compositor final quedó byte-determinista sin relajar idempotencia.
3. El checkpoint móvil de `#contacto` usaba un 25% de `intersectionRatio`, geométricamente inalcanzable para una sección más alta que el viewport. El contrato fija 5% como exposición observable y el E2E espera milestones reales, sin sleeps fijos.

## Invariantes

- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- WhatsApp manual;
- portal real deshabilitado;
- demo explícitamente ficticia;
- funnel v5.29 solo en memoria y sin PII;
- no inferir conversión comercial desde navegación, contacto o handoff;
- `stable` solo se mueve tras gates verdes;
- ningún hecho profesional nuevo se publica fuera del contrato verificable correspondiente;
- no se oculta contenido material ni se relajan budgets o cobertura.

## Graphify

Graphify es memoria derivada. El cierre documental v5.29 fue regenerado correctamente con versión `5.29.0`, canal `github-pages-production-funnel-trust-certified` y el `source_commit` correspondiente al `main` que produjo ese snapshot. Al retomar el proyecto debe verificarse nuevamente la igualdad con `main`.

## Estado del ciclo

**v5.29 está implementada, desplegada, certificada, documentada y cerrada. No existe un ciclo funcional posterior abierto.**

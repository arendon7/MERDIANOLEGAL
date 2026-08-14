# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release certificada y cerrada: **5.29.0 — funnel observable y confianza contextual**.
- SHA funcional certificado previo al cierre documental: `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`.
- Builder funcional final: `31823965908`.
- Run público funcional final: `31823985048`.
- Release Governance final relevante: `31823922160`.
- Al cierre funcional: `main = stable = 8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`.

## Contrato v5.29

La capa v5.29 materializa un funnel observable de siete etapas (`awareness`, `need`, `offer`, `evidence`, `decision`, `contact`, `handoff`) sobre la telemetría local ya existente. La cola está limitada a 48 eventos en memoria y no introduce persistencia, identificación entre sesiones, fingerprinting ni transporte de red.

Los checkpoints de portada usan un umbral contractual de 5% de superficie visible, compatible con secciones más altas que el viewport móvil. Las 16 fichas profundas se integran al mismo modelo mediante `data-catalog-id`.

La capa no inspecciona valores de formulario. Ninguna señal permite afirmar que un mensaje fue enviado, entregado o leído, que una propuesta fue aceptada, que comenzó un encargo o que existe una conversión a cliente.

Antes de `#contacto` se presenta un `<aside>` compacto de confianza derivado exclusivamente de `professional-authority-v525.json`. El bloque declara expresamente los límites de esa evidencia y preserva la secuencia de `<section>` establecida por v5.28.

## Evidencia funcional final

- generación canónica de 30 pasos: PASS;
- segunda pasada/idempotencia: PASS;
- 37 validaciones estáticas: PASS;
- Release Governance: PASS;
- 16 fichas profundas instrumentadas: PASS;
- GitHub Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: **88 observados · 86 PASS · 2 SKIP · 0 FAIL · 0 retries**;
- axe: 0 violaciones serias/críticas en las superficies cubiertas;
- Lighthouse performance/accesibilidad: PASS contra budgets existentes;
- promoción automática de `stable`: PASS;
- budgets relajados: no;
- cobertura reducida: no;
- PII/persistencia/transporte nuevo: no.

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

Graphify funcional v5.29 fue regenerado correctamente sobre `8a8d3bfe473dd5b0ca931c05fbb73b60afaa1f70`. El commit documental de cierre debe volver a regenerarlo con versión `5.29.0`, canal `github-pages-production-funnel-trust-certified` y `source_commit` idéntico al `main` final.

## Estado del ciclo

**v5.29 está implementada, desplegada y funcionalmente certificada. El cierre documental cambia el canal a `certified` y debe recorrer nuevamente todos los gates antes de declarar el SHA documental definitivo.**

# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-14.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Fuente técnica/documental: `main`.
- Snapshot funcional certificado: `stable`.
- Release certificada y cerrada: **5.28.0 — ruta de conversión compacta**.
- SHA público/canónico certificado previo al commit documental de cierre: `786bd9d4dc720f027f64067c9dd83d583e7e934c`.
- Builder autoritativo final: `31819573869`.
- Run público final: `31819606409`.
- Release Governance final relevante: `31819530202`.
- Al cierre funcional: `main = stable = 786bd9d4dc720f027f64067c9dd83d583e7e934c`.

## Contrato v5.28

La portada materializa `#contacto` inmediatamente después de `#contratacion`. Sectores, perspectivas, firma y FAQ permanecen íntegros después del contacto como profundidad opcional. El preámbulo redundante de tres tarjetas fue reemplazado por una franja de preparación con decisión/problema, plazo/urgencia y resultado esperado.

Se conserva un único formulario físico canónico y todas las capas de calificación, propuesta, engagement, brief, recomendación, síntesis, proceso y handoff manual. En móvil, las rejillas de síntesis usan overflow horizontal local contenido. Son focables por teclado y mantienen la semántica nativa de `<dl>`.

## Evidencia final

- generación canónica de 30 pasos: PASS;
- segunda pasada/idempotencia: PASS;
- 37 validaciones estáticas: PASS;
- Release Governance: PASS;
- GitHub Pages: PASS;
- smoke público: PASS;
- Browser E2E/axe: **79 observados · 77 PASS · 2 SKIP · 0 FAIL · 0 retries**;
- axe portada y superficies cubiertas: 0 violaciones serias/críticas;
- Lighthouse performance/accesibilidad: PASS contra budgets existentes;
- promoción automática de `stable`: PASS;
- budgets relajados: no;
- cobertura reducida: no.

## Hallazgos corregidos durante la certificación

1. Whitespace no determinista del compositor: corregido sin relajar `git diff --exit-code`.
2. Validator UX v4.5 con orden narrativo histórico: hecho version-aware; conserva el contrato antiguo hasta v5.27 y exige el nuevo desde v5.28.
3. Contraste y foco de regiones desplazables: corregidos; el acento de preparación supera AA y los decks son alcanzables por teclado.
4. Semántica `<dl>`: se retiró `role="region"` de las listas de definición para preservar `dt/dd`, manteniendo `tabindex` y `aria-label`.

## Invariantes

- 46 HTML;
- 16 fichas profundas;
- 1 formulario físico canónico;
- WhatsApp manual y telemetría local sin PII;
- portal real deshabilitado;
- demo explícitamente ficticia;
- `stable` solo se mueve tras gates verdes;
- ningún hecho profesional nuevo se publica fuera del contrato verificable correspondiente;
- no se oculta contenido material para mejorar densidad;
- la accesibilidad no puede implementarse sustituyendo semántica HTML nativa sin necesidad.

## Graphify

El snapshot derivado verde disponible declara v5.28, `graphify_version = 0.9.26`, 740 nodos, 1.256 aristas y 100 notas wiki, con `source_commit = 7f9caa0a77923b79da6b1d5e2054680dfce0f63d`. Es anterior al SHA canónico certificado `786bd9d4…`; `main` continúa siendo la autoridad hasta la siguiente regeneración.

## Estado del ciclo

**v5.28 está implementada, desplegada, certificada y funcionalmente cerrada. No existe un ciclo posterior activo.**

# Meridiano Legal v6.2.0 — Search Discovery Readiness

Fecha de release funcional: 2026-08-18

## Objetivo

v6.2 convierte Search Discovery en una propiedad verificable del sitio sin afirmar que Google Search Console esté configurado, sin inventar un token de propiedad y sin confundir una preparación técnica con ranking, tráfico o indexación garantizada.

La decisión central fue **hacer verificable la superficie indexable antes de conectar una herramienta externa**.

## Resultado funcional

SHA funcional certificado:

`4027b6a5425a13cdd0134799c88081e08ac80b6f`

Ese SHA fue producido por el builder canónico después del merge de #158 y promovido automáticamente a `stable` únicamente después de la cadena post-deploy.

## Alcance completado

### 1. Contrato Search Discovery v6.2

Se incorporó `assets/data/v6/search-discovery-readiness-v62.json` con estado:

`readiness-not-verified`

El contrato define:

- proveedor de verificación previsto: Google Search Console;
- tipo de propiedad preparado: URL-prefix;
- método: meta HTML;
- fuente gobernada del token: `site-config.json.search_console_verification`;
- requisito de token auténtico;
- comportamiento fail-closed cuando el token está vacío;
- frontera canónica/indexable;
- reglas del sitemap;
- prohibición de afirmar configuración sin evidencia.

### 2. Frontera exacta 43/3

La inspección programática de las 46 superficies públicas determinó:

- **43 páginas indexables**;
- **3 superficies `noindex`**: `404.html`, `demo.html`, `experiencia.html`.

Cada página indexable debe declarar exactamente un canonical y ese canonical debe ser autorreferencial.

Las tres superficies `noindex` permanecen fuera del sitemap.

### 3. Sitemap determinista

`scripts/apply_search_discovery_v62.py` genera `sitemap.xml` desde las páginas realmente indexables y sus canonicals.

El sitemap v6.2 contiene:

- exactamente 43 `<loc>`;
- cero duplicados;
- cero páginas noindex;
- sin `priority`;
- sin `changefreq`;
- sin un `lastmod` global derivado simplemente de la fecha de release.

La ausencia de `lastmod` en esta fase es deliberada: el sistema no afirma una modificación material por URL cuando no dispone de una fuente per-page que pueda demostrarla.

### 4. Search Console fail-closed

Producción mantiene:

- `search_console_verification=""`;
- ninguna meta `google-site-verification`;
- `searchConsoleConfigured=false` en runtime.

El normalizador está preparado para una futura activación auténtica:

- token vacío + meta ausente => Home byte-stable;
- token vacío + meta residual => se elimina;
- token real => exactamente una meta de verificación con el valor gobernado.

El validator impide que runtime y meta diverjan.

### 5. Robots y canonicals

El validator exige:

- una única referencia canónica al sitemap en `robots.txt`;
- exclusión explícita de demo;
- clasificación de las 46 superficies;
- canonical autorreferencial único en cada página indexable;
- exclusión del sitemap de las tres superficies noindex.

## Release engineering v6.2

### 1. Integración sin paso 31

Search Discovery se integra a través de `normalize_experience_compat_v60.py`, el punto transversal de extensiones v6 que ya incorpora Measurement Readiness v6.1.

Los 30 pasos históricos del builder permanecen intactos.

### 2. Separación entre release metadata y sitemap

`sync_public_version.py` conserva su contrato histórico para baselines anteriores a v6.2. Cuando existe el nuevo contrato, deja de ser propietario del sitemap y este pasa a `apply_search_discovery_v62.py`.

Así una fecha global de versión no se reutiliza automáticamente como señal de modificación de cada URL.

### 3. v4.8 phase-aware

`validate_quality_v48.py` conserva el comportamiento legacy cuando v6.2 no existe.

Con v6.2:

- mantiene los controles de calidad/SEO históricos;
- ya no exige `lastmod=release_date`;
- prohíbe `lastmod`, `priority` y `changefreq` en el sitemap canónico v6.2.

### 4. v5.1 phase-aware

`validate_growth_v51.py` continúa exigiendo:

- las seis rutas por situación;
- el hub de soluciones;
- las siete URLs correspondientes en sitemap;
- canonicals e interlinking;
- evidencia y profundidad del contrato Growth.

Solo deja de depender del comentario físico histórico `GROWTH-V51-SITEMAP:START` cuando v6.2 gobierna discovery.

### 5. Source pre-materialización vs output canónico

Durante el ciclo se detectó que Release Governance valida el source antes de que el builder materialice v6.2. Por ello, una fuente puede contener transitoriamente el marcador histórico de v5.1.

La responsabilidad quedó separada correctamente:

- Growth valida la propiedad semántica histórica;
- Search Discovery normaliza el output;
- el validator v6.2 exige la representación canónica final.

### 6. Boundary exacto

`.github/workflows/v62-search-discovery-readiness.yml` captura dos fuentes de drift antes de escribir:

- `sync_public_version.py --check`;
- `apply_search_discovery_v62.py --check`.

Luego exige:

**diff real = release drift ∪ discovery drift**

Canonical Equivalence extiende esa misma lógica a:

**measurement esperado ∪ release drift ∪ discovery drift**.

No existe una whitelist abierta de cambios.

### 7. Idempotencia

Tanto el gate v6.2 como Canonical Equivalence prueban una segunda pasada completa.

La segunda pasada debe conservar exactamente el mismo diff y ambos `--check` deben terminar limpios.

### 8. Trigger coverage

El Builder observa cambios futuros en `scripts/apply_search_discovery_v62.py`, y `validate_pages_trigger_v511.py` exige esa cobertura.

Candidate y Browser observan además:

- `site-config.json`;
- `sitemap.xml`;
- `robots.txt`;
- scripts y contrato v6.2.

Así una futura incorporación de token real no puede saltarse los gates principales.

### 9. E2E dinámico

`tests/e2e/search-discovery-v62.spec.mjs` no contiene ningún token hardcoded.

Prueba:

- runtime false => ninguna meta Google;
- runtime true => exactamente una meta no vacía;
- sitemap servido sin `lastmod`, `priority` ni `changefreq`;
- 43 `<loc>`;
- exclusión de 404, demo y experiencia.

La spec corrió dentro de la suite Browser completa Chromium/WebKit del candidate v6.2.

## Incidencias detectadas y resueltas

### 1. La frontera real era 43/3, no 44/2

El primer gate reveló que `experiencia.html` ya era `noindex`. No se cambió esa política para cuadrar un supuesto; se corrigió el contrato para representar la verdad del sitio.

### 2. Drift innecesario en Home

La primera versión del normalizador compactaba saltos de línea aun cuando no había token de verificación. Se corrigió para que Home permanezca byte-for-byte igual cuando token y meta están ausentes.

### 3. Contrato histórico v5.1

Canonical Equivalence detectó la dependencia del marcador físico de sitemap. Se evolucionó el validator sin eliminar las siete URLs ni el resto del Growth contract.

### 4. Governance y fase de materialización

Una primera corrección v5.1 era demasiado estricta y prohibía el marcador incluso en source pre-materialización. Governance lo detectó. Se separaron source y output en vez de desactivar el gate.

### 5. Boundary durante bump de versión

El gate v6.2 inicialmente observaba solo discovery drift. Antes del bump 6.2 se endureció para incluir también release drift exacto, evitando falsos positivos sin ampliar permisos.

### 6. Cobertura futura de triggers

Se detectó que un cambio aislado al materializador v6.2 o a `site-config.json` podía no activar todos los gates relevantes. Builder, Candidate y Browser quedaron endurecidos y el validator de topología protege esa cobertura.

## Evidencia pre-merge

Candidate final:

`d14b0356aa2733645061f7230b7cc044f09cd42f`

Sobre ese mismo SHA quedaron verdes:

1. V6.2 Search Discovery Readiness;
2. V6 Candidate Validation;
3. V6 Canonical Builder Equivalence;
4. Release Governance Health;
5. Graphify;
6. V6 Browser Candidate / axe;
7. V6.1 Measurement Readiness / Browser E2E.

No se redujo cobertura, no se relajaron budgets y no se eliminaron tests para aprobar la release.

## Evidencia post-merge

- PR #158 fusionado como `b5ec91e950f1ee6fa82f88ac4fcebdcfd4b12200`.
- Builder generó `4027b6a5425a13cdd0134799c88081e08ac80b6f` con mensaje `build: sincroniza sitio público canónico`.
- El snapshot contiene v6.2.0, runtime con analytics deshabilitada, Search Console false y sitemap mínimo 43/3.
- `stable` alcanzó automáticamente `4027b6a5…` después de la cadena post-deploy.

## Capability truth preservado

v6.2 no introduce:

- Search Console ficticia;
- token inventado;
- ranking, tráfico, impresiones o clics ficticios;
- analytics activa;
- cookies/storage/fingerprinting nuevos;
- backend/CRM/auth/pagos/firma/agenda/upload ficticios;
- PII exportada;
- modificación de productos, servicios, precios o claims comerciales.

## Condición para activar Search Console realmente

Una activación posterior requiere, como mínimo:

1. propiedad/cuenta Google auténtica;
2. token emitido por Google para la propiedad URL-prefix correspondiente;
3. incorporación del token únicamente en la configuración gobernada;
4. materialización de una sola meta de verificación;
5. gates v6.2/Candidate/Browser/Equivalence/Governance verdes;
6. despliegue productivo certificado;
7. verificación efectiva en Google y gestión del sitemap desde la propiedad real.

Hasta entonces, el estado correcto es **Search Discovery Readiness certificada, Search Console no configurada**.

## Canal definitivo

El cierre documental cambia el canal de:

`github-pages-search-discovery-readiness-candidate`

A:

`github-pages-production-search-discovery-readiness-certified`

Este cambio describe certificación de la arquitectura. No activa ni verifica Search Console.

## Cierre definitivo

La release queda documentalmente cerrada cuando este paquete —`version.json`, README, memoria canónica y `RELEASE-v6.2.md`— atraviese nuevamente los gates, Builder → Pages → smoke → Browser/axe → Lighthouse → snapshot y termine con `main == stable`.

# Meridiano Legal — Estado canónico

Última verificación humana: 2026-08-10.

## Fuente canónica

- Repositorio: `arendon7/MERDIANOLEGAL`.
- Rama técnica/productiva: `main`.
- Snapshot certificado: `stable`.
- Base técnica sobre la que se inicializa esta memoria: `a6559ea0e5288c0e2b86e189ce6856acedcbac57`.
- `stable` al inicializar esta memoria: `6d95d96d00e1ce15ad0c110ca7511e1d0873e933`.
- Versión declarada en `version.json`: `5.5.0`.

El SHA de `main` cambiará al integrar esta infraestructura. Por eso, al retomar trabajo siempre debe confirmarse el ref real antes de usar cualquier SHA escrito en una nota.

## Estado funcional

La última base completamente certificada y promovida sigue siendo v5.4 en `stable`.

v5.5 está en fase de Performance + Accessibility QA. Ya quedaron incorporados:

- Node 22 para Browser QA;
- dependencias QA fijadas mediante `package-lock.json` y `npm ci`;
- Playwright 1.62.0;
- axe-core 4.12.1;
- Lighthouse 13.4.1;
- siete superficies axe representativas;
- presupuestos Lighthouse versionados;
- correcciones transversales de contraste accesible.

## Evidencia v5.5 más reciente

Sobre la candidata previa a esta memoria:

- Playwright/axe: 35 pruebas pasaron y 2 quedaron skipped; ninguna falló.
- Las 7 auditorías axe quedaron sin violaciones serias/críticas.
- Cinco de seis superficies Lighthouse cumplen los presupuestos.
- La portada cumple performance score, accesibilidad, LCP, TBT y peso.
- Único bloqueo conocido: CLS de portada `0.303806...`, presupuesto `<= 0.15`.
- Lighthouse identificó como responsable del desplazamiento a `main#contenido > section.hero > div.container > div.hero-art`.
- LCP observado en portada: ~1206 ms.
- TBT observado: 0 ms.
- Transferencia observada: ~73.9 KB.
- Performance score observado: 0.85.
- Accessibility score observado: 0.97.

`stable` no debe avanzar hasta que CLS quede dentro del presupuesto y toda la cadena vuelva a estar verde.

## Estado de integraciones externas

Activas:

- GitHub Pages;
- WhatsApp como handoff de contacto;
- contexto comercial en sesión/local según contratos vigentes;
- telemetría local en memoria y semántica de eventos preparada;
- sitemap, robots, canonical, Open Graph y estado público;
- demo estático/noindex;
- build canónico, validación, Pages, smoke y snapshot estable.

No deben declararse activas sin evidencia/configuración real:

- dominio personalizado/CNAME;
- Search Console;
- proveedor de analítica externo;
- CRM/backend de leads;
- formulario con almacenamiento servidor;
- email transaccional.

## Memoria de ingeniería

A partir de esta integración:

- `knowledge/` conserva memoria humana y handoff;
- Graphify conserva la fotografía estructural regenerable en `knowledge/graphify-live`;
- Obsidian puede abrir la raíz del repositorio como vault;
- ChatGPT continúa como agente principal y no requiere Codex;
- GitHub Actions y validadores continúan siendo la autoridad funcional.

## Regla de continuidad

No reconstruir Meridiano desde conversaciones largas si `main`, `knowledge/` y Graphify contienen un estado más reciente. Empezar por el contexto canónico, verificar frescura del grafo y abrir solo el conjunto mínimo de fuentes/tests afectados.
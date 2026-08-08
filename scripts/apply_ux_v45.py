#!/usr/bin/env python3
"""Aplica la arquitectura UX/UI canónica v4.5 a la portada pública."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
CATALOG_HOME = ROOT / "catalog-home-v32.js"
DECISION_FLOW = ROOT / "decision-flow.js"
STYLE = '<link rel="stylesheet" href="ux-v45.css">'
MOBILE_START = "<!-- UX-V45-MOBILE:START -->"
MOBILE_END = "<!-- UX-V45-MOBILE:END -->"

HEADER_NAV = '''<nav id="main-nav" class="main-nav" aria-label="Navegación principal"><a href="#necesidades">Necesidades</a><a href="#servicios">Servicios</a><a href="#productos">Productos</a><a href="#planes">Planes y precios</a><a href="#sectores">Sectores</a><a href="#firma">Firma</a><span class="mobile-nav-actions"><a href="experiencia.html">Centro demo</a><a href="demo.html">Área de clientes</a><a href="#contacto">Presentar necesidad</a></span></nav>'''
HEADER_ACTIONS = '''<div class="header-actions"><a class="btn btn-outline-dark" href="experiencia.html">Centro demo</a><a class="btn btn-navy" href="#contacto">Presentar necesidad</a></div>'''

PRINCIPLES = '''    <section class="principles" aria-label="Oferta pública de Meridiano Legal"><div class="container principles-grid"><article><svg><use href="#i-compass"/></svg><div><strong>8 servicios</strong><span>especializados</span></div></article><article><svg><use href="#i-contract"/></svg><div><strong>8 productos</strong><span>de alcance cerrado</span></div></article><article><svg><use href="#i-building"/></svg><div><strong>5 planes</strong><span>recurrentes</span></div></article><article><svg><use href="#i-chart"/></svg><div><strong>8 sectores</strong><span>con lectura operativa</span></div></article><article><svg><use href="#i-network"/></svg><div><strong>Centro demo</strong><span>y portal demostrativo</span></div></article></div></section>'''

OUTCOMES = '''    <section class="section outcomes-section" id="entregables"><div class="container"><div class="section-heading heading-row"><div><p class="eyebrow dark">QUÉ RECIBE LA EMPRESA</p><h2>Entregables diseñados para decidir, ejecutar y controlar.</h2></div><p>La forma cambia según el asunto, pero el trabajo debe poder comprenderse, aprobarse, implementarse y revisarse. Las fichas profundas detallan cantidades, formatos, responsables, límites y criterios de cierre.</p></div><div class="outcomes-grid"><article class="outcome-card"><span>01 · DECISIÓN</span><h3>Concepto o informe ejecutivo</h3><p>Hechos, supuestos, régimen aplicable, riesgos, alternativas, conclusión y condiciones para decidir.</p><small>Criterio sustentado</small></article><article class="outcome-card"><span>02 · ESTRUCTURA</span><h3>Instrumento jurídico</h3><p>Contrato, política, acta, acuerdo, protocolo o paquete documental conectado con la operación.</p><small>Reglas que pueden ejecutarse</small></article><article class="outcome-card"><span>03 · EJECUCIÓN</span><h3>Hoja de ruta</h3><p>Hitos, dependencias, responsables, evidencia, fechas, aprobaciones y condiciones de cierre.</p><small>Del análisis a la acción</small></article><article class="outcome-card"><span>04 · CONTROL</span><h3>Matriz o tablero</h3><p>Riesgos, obligaciones, decisiones, vencimientos, responsables, estado y evidencia de seguimiento.</p><small>Memoria y trazabilidad</small></article></div></div></section>'''

EXPERIENCE = '''    <section class="section experience-section experience-v45" id="experiencia"><div class="container experience-layout"><div class="experience-copy"><p class="eyebrow">MERIDIANO EMPRESAS · DEMOSTRACIÓN</p><h2>Vea cómo se organiza el trabajo jurídico después del concepto o del documento.</h2><p>La propuesta no termina en archivos sueltos. El entorno demostrativo muestra cómo un asunto puede conectar contexto, riesgos, decisiones, obligaciones, documentos, responsables y próximos hitos.</p><div class="hero-actions"><a class="btn btn-gold" href="experiencia.html">Recorrer el centro demo</a><a class="btn btn-outline-light" href="demo.html">Abrir Meridiano Empresas</a></div><small>Interfaz ilustrativa y datos ficticios. La web pública no recibe expedientes ni información confidencial.</small></div><div class="platform-mockup-v45" aria-label="Vista ilustrativa de Meridiano Empresas"><div class="mockup-top-v45"><strong>Meridiano Empresas</strong><span>Entorno demostrativo</span></div><div class="mockup-body-v45"><div class="mockup-nav-v45"><span class="active">Resumen</span><span>Expediente</span><span>Riesgos</span><span>Obligaciones</span><span>Documentos</span><span>Decisiones</span></div><div class="mockup-main-v45"><span>ASUNTO DEMOSTRATIVO</span><h3>Proyecto de expansión empresarial</h3><div class="mockup-status-v45"><article><small>Estado</small><strong>En estructuración</strong></article><article><small>Próximo hito</small><strong>Validación documental</strong></article><article><small>Gobierno</small><strong>Dirección + responsable interno</strong></article></div><div class="mockup-flow-v45"><article><b>1</b><strong>Contexto y hechos</strong><span>Fuente identificada</span></article><article><b>2</b><strong>Riesgos y dependencias</strong><span>Priorizados</span></article><article><b>3</b><strong>Decisiones y responsables</strong><span>Asignados</span></article><article><b>4</b><strong>Evidencia y cierre</strong><span>Trazables</span></article></div></div></div><small class="mockup-note-v45">Ejemplo visual: no corresponde a un cliente ni a un expediente real.</small></div></div></section>'''

FOOTER = '''  <footer class="site-footer"><div class="container footer-grid"><div class="footer-brand"><img src="assets/brand/meridiano-logo-horizontal-light.svg" alt="Meridiano Legal"><p>Dirección jurídica para empresas, innovación y proyectos regulados.</p></div><div><strong>Oferta</strong><a href="#servicios">Servicios</a><a href="#productos">Productos</a><a href="#planes">Planes y honorarios</a><a href="demo.html#documentos">Documentos guiados</a></div><div><strong>Explorar</strong><a href="#sectores">Sectores</a><a href="perspectivas.html">Perspectivas</a><a href="experiencia.html">Centro demo</a><a href="demo.html">Área de clientes</a></div><div><strong>Información</strong><a href="#firma">Firma</a><a href="#preguntas">Preguntas frecuentes</a><a href="privacidad.html">Privacidad</a><a href="terminos.html">Términos de uso</a><a href="aviso-legal.html">Aviso legal</a></div></div><div class="container footer-principles"><span>DIRECCIÓN<small>Orientamos decisiones</small></span><span>ESTRATEGIA<small>Convertimos riesgos en planes</small></span><span>ESTRUCTURA<small>Diseñamos soluciones ejecutables</small></span><span>TECNOLOGÍA<small>Integramos herramientas</small></span><span>ACOMPAÑAMIENTO<small>Seguimos todo el ciclo</small></span></div><div class="container footer-bottom"><span>© <span id="year"></span> Meridiano Legal · Medellín, Colombia</span><span>Material general · No constituye asesoría jurídica</span><span>Web demostrativa v4.5.0</span></div></footer>'''

MOBILE_CTA = '''<!-- UX-V45-MOBILE:START -->
  <div class="mobile-conversion-v45" aria-label="Acciones rápidas"><a href="#contacto">Presentar necesidad</a><a href="demo.html">Área de clientes</a></div>
<!-- UX-V45-MOBILE:END -->'''


def replace_tag_block(text: str, pattern: str, replacement: str) -> str:
    updated, count = re.subn(pattern, lambda _match: replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"No se pudo aplicar bloque UX: {pattern}")
    return updated


def section(text: str, section_id: str) -> str:
    match = re.search(rf'    <section\b(?=[^>]*\bid="{re.escape(section_id)}")[^>]*>[\s\S]*?</section>', text)
    if not match:
        raise RuntimeError(f"No se encontró la sección #{section_id}")
    return match.group(0)


def main() -> int:
    text = INDEX.read_text(encoding="utf-8")

    text = replace_tag_block(text, r'<nav id="main-nav" class="main-nav" aria-label="Navegación principal">[\s\S]*?</nav>', HEADER_NAV)
    text = replace_tag_block(text, r'<div class="header-actions">[\s\S]*?</div>', HEADER_ACTIONS)
    text = text.replace(
        '<p class="lead">Ayudamos a gerencias, socios y equipos a convertir decisiones jurídicas complejas en estructuras, documentos, responsables y rutas de implementación que puedan administrarse.</p>',
        '<p class="lead">Integramos criterio jurídico, lectura empresarial y seguimiento para convertir decisiones complejas en estructuras, documentos, responsables y rutas de implementación administrables.</p>',
        1,
    )
    text = text.replace('<a class="btn btn-outline-light btn-lg" href="#elegir">Encontrar el punto de entrada</a>', '<a class="btn btn-outline-light btn-lg" href="#necesidades">Ver cómo podemos ayudar</a>', 1)
    text = replace_tag_block(text, r'    <section class="principles"[\s\S]*?</section>', PRINCIPLES)
    text = text.replace('Cuatro formas de empezar, según la decisión y el nivel de acompañamiento.', 'Cuatro formas de empezar. Elija por resultado, no por nombre del servicio.', 1)
    text = replace_tag_block(text, r'    <section class="section outcomes-section" id="entregables">[\s\S]*?</section>', OUTCOMES)
    text = replace_tag_block(text, r'    <section class="section experience-section(?: experience-v45)?" id="experiencia">[\s\S]*?</section>', EXPERIENCE)

    contracting = section(text, "contratacion")
    contracting = re.sub(r'<div class="contracting-route-v45">[\s\S]*?</div>', '', contracting, count=1)
    contracting = contracting.replace(
        '<div class="contracting-grid-v44">',
        '<div class="contracting-route-v45"><img src="assets/route-meridiano-v3.svg" alt="Ruta Meridiano: comprender, calificar, estructurar, proponer e iniciar"></div><div class="contracting-grid-v44">',
        1,
    )
    text = replace_tag_block(text, r'    <section class="section contracting-v44" id="contratacion">[\s\S]*?</section>', contracting)

    audience = re.search(r'    <section class="audience-strip"[\s\S]*?</section>', text)
    if not audience:
        raise RuntimeError("No se encontró audience-strip")
    main_end = text.find('  </main>')
    if main_end < 0:
        raise RuntimeError("No se encontró cierre de main")

    blocks = {
        key: section(text, key)
        for key in (
            "necesidades", "elegir", "servicios", "productos", "entregables", "experiencia",
            "planes", "honorarios", "contratacion", "sectores", "perspectivas", "firma", "preguntas", "contacto"
        )
    }
    commercial = '\n'.join([
        '    <!-- COMMERCIAL-V43:START -->',
        blocks["planes"], '', blocks["honorarios"], '', blocks["contratacion"],
        '    <!-- COMMERCIAL-V43:END -->',
    ])
    sequence = [
        blocks["necesidades"], blocks["elegir"], blocks["servicios"], blocks["productos"],
        blocks["entregables"], blocks["experiencia"], commercial, blocks["sectores"],
        blocks["perspectivas"], blocks["firma"], blocks["preguntas"], blocks["contacto"],
    ]
    text = text[:audience.end()] + '\n\n' + '\n\n'.join(sequence) + '\n' + text[main_end:]

    text = replace_tag_block(text, r'  <footer class="site-footer">[\s\S]*?</footer>', FOOTER)
    text = re.sub(re.escape(MOBILE_START) + r'[\s\S]*?' + re.escape(MOBILE_END), '', text, count=1)
    mobile_pattern = re.compile(r'</footer>[\s\n\r\t ]*<dialog class="modal"', re.S)
    text, mobile_count = mobile_pattern.subn(lambda _match: f'</footer>\n\n{MOBILE_CTA}\n\n  <dialog class="modal"', text, count=1)
    if mobile_count != 1:
        raise RuntimeError("No se pudo normalizar la posición del CTA móvil v4.5")

    for candidate in (f'  {STYLE}\n', f'{STYLE}\n', f'  {STYLE}', STYLE):
        text = text.replace(candidate, '')
    text = text.replace('</head>', f'  {STYLE}\n</head>', 1)
    INDEX.write_text(text, encoding="utf-8")

    if CATALOG_HOME.exists():
        js = CATALOG_HOME.read_text(encoding="utf-8")
        nav_pattern = re.compile(
            r"\n  const mainNav=document\.querySelector\('\.main-nav'\); if\(mainNav&&!mainNav\.querySelector\('\.nav-perspectives'\)\)\{[\s\S]*?mainNav\.insertBefore\(link,contactLink\|\|null\);\}\n  const modalContent=",
            re.S,
        )
        js, count = nav_pattern.subn("\n  const modalContent=", js, count=1)
        if count == 0 and "nav-perspectives" in js:
            raise RuntimeError("No se pudo retirar la inyección legada de Perspectivas del menú")
        CATALOG_HOME.write_text(js, encoding="utf-8")

    if DECISION_FLOW.exists():
        js = DECISION_FLOW.read_text(encoding="utf-8")
        navigation_pattern = re.compile(
            r"\n  const mainNav = document\.querySelector\('\.main-nav'\);[\s\S]*?\n  const menuButton = document\.querySelector\('\.menu-toggle'\);",
            re.S,
        )
        js, count = navigation_pattern.subn("\n  const menuButton = document.querySelector('.menu-toggle');", js, count=1)
        if count == 0 and ("nav-selector" in js or "nav-mobile-utility" in js):
            raise RuntimeError("No se pudieron retirar las inyecciones legadas del flujo guiado")
        DECISION_FLOW.write_text(js, encoding="utf-8")

    print("UX/UI v4.5 aplicada: narrativa, densidad, mockup, navegación y móvil optimizados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

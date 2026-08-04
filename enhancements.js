(() => {
  const VERSION = '2.31.0';
  const WHATSAPP_NUMBER = '573008507813';

  function ensureStylesheet(href) {
    if (document.querySelector(`link[href="${href}"]`)) return;
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    document.head.append(link);
  }

  function ensureManifest() {
    if (document.querySelector('link[rel="manifest"]')) return;
    const link = document.createElement('link');
    link.rel = 'manifest';
    link.href = 'manifest.webmanifest';
    document.head.append(link);
  }

  function ensureCanonical() {
    if (document.querySelector('link[rel="canonical"]')) return;
    const canonical = document.createElement('link');
    canonical.rel = 'canonical';
    canonical.href = `https://arendon7.github.io/MERDIANOLEGAL/${location.pathname.endsWith('/') ? '' : location.pathname.split('/').pop()}`;
    document.head.append(canonical);
  }

  function addLegalLinks() {
    const footerColumns = document.querySelectorAll('.footer-grid > div');
    const target = footerColumns[2];
    if (!target || target.querySelector('.legal-links')) return;

    const links = document.createElement('div');
    links.className = 'legal-links';
    links.innerHTML = `
      <a href="privacidad.html">Privacidad</a>
      <a href="terminos.html">Términos de uso</a>
      <a href="aviso-legal.html">Aviso legal</a>
    `;
    target.append(links);
  }

  function addFloatingActions() {
    if (document.querySelector('.floating-actions')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'floating-actions';
    wrapper.innerHTML = `
      <a class="floating-action floating-whatsapp" href="https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent('Hola, quiero conocer las soluciones de Meridiano Legal.')}" target="_blank" rel="noopener noreferrer" aria-label="Contactar por WhatsApp" title="Contactar por WhatsApp">W</a>
      <button class="floating-action floating-top" type="button" aria-label="Volver arriba" title="Volver arriba">↑</button>
    `;
    document.body.append(wrapper);

    const topButton = wrapper.querySelector('.floating-top');
    topButton.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    const updateVisibility = () => topButton.classList.toggle('visible', window.scrollY > 600);
    window.addEventListener('scroll', updateVisibility, { passive: true });
    updateVisibility();
  }

  function addTrustNote() {
    const form = document.getElementById('contact-form');
    if (!form || form.querySelector('.trust-note')) return;
    const note = document.createElement('div');
    note.className = 'trust-note full';
    note.innerHTML = '<span aria-hidden="true">✓</span><div><strong>Canal directo y sin registro.</strong> La solicitud se prepara en su navegador y se abre en WhatsApp. La web no almacena el contenido del formulario.</div>';
    const submit = form.querySelector('button[type="submit"]');
    form.insertBefore(note, submit);
  }

  function addDemoNavigation() {
    const privateDemo = document.querySelector('.header-actions a[href="demo.html"]');
    if (privateDemo) {
      privateDemo.href = 'experiencia.html';
      privateDemo.textContent = 'Centro demo';
      privateDemo.classList.add('demo-center-link');
    }

    const navigation = document.querySelector('.main-nav');
    if (!navigation || navigation.querySelector('.nav-demo')) return;
    const contact = navigation.querySelector('a[href="#contacto"]');
    const demoLink = document.createElement('a');
    demoLink.href = 'experiencia.html';
    demoLink.className = 'nav-demo';
    demoLink.textContent = 'Demo';
    navigation.insertBefore(demoLink, contact);
  }

  function addWorkModes() {
    if (document.getElementById('modalidades')) return;
    const sectors = document.getElementById('sectores');
    if (!sectors) return;

    const section = document.createElement('section');
    section.className = 'section work-modes-section';
    section.id = 'modalidades';
    section.innerHTML = `
      <div class="container">
        <div class="section-heading heading-row">
          <div><p class="eyebrow dark">MODALIDADES DE TRABAJO</p><h2>El alcance debe corresponder a la decisión, la recurrencia y el nivel de gobierno requerido.</h2></div>
          <p>No toda necesidad exige el mismo nivel de intervención. La modalidad se define por el resultado esperado, la evidencia, la urgencia y la continuidad necesaria.</p>
        </div>
        <div class="work-modes-grid">
          <article class="work-mode"><span>01</span><h3>Orientación focal</h3><dl><dt>Mejor para</dt><dd>Pregunta concreta</dd><dt>Duración</dt><dd>Sesión o alcance breve</dd><dt>Resultado</dt><dd>Definir el siguiente paso</dd></dl></article>
          <article class="work-mode"><span>02</span><h3>Diagnóstico</h3><dl><dt>Mejor para</dt><dd>Varios frentes conectados</dd><dt>Duración</dt><dd>2 a 4 semanas</dd><dt>Resultado</dt><dd>Mapa y ruta de 90 días</dd></dl></article>
          <article class="work-mode"><span>03</span><h3>Proyecto jurídico</h3><dl><dt>Mejor para</dt><dd>Resultado definido</dd><dt>Duración</dt><dd>4 a 12 semanas</dd><dt>Resultado</dt><dd>Entregables e implementación</dd></dl></article>
          <article class="work-mode"><span>04</span><h3>Dirección externa</h3><dl><dt>Mejor para</dt><dd>Necesidad recurrente</dd><dt>Duración</dt><dd>Cadencia mensual</dd><dt>Resultado</dt><dd>Gobierno y memoria continua</dd></dl></article>
        </div>
        <p class="proposal-formula"><strong>Cómo se forma una propuesta:</strong> contexto, resultado esperado, alcance y exclusiones, entregables, cronograma, responsables, honorarios, impuestos, forma de pago, vigencia y aceptación.</p>
      </div>
    `;
    sectors.before(section);
  }

  function addDemoCenter() {
    if (document.getElementById('centro-demo')) return;
    const contact = document.getElementById('contacto');
    if (!contact) return;

    const section = document.createElement('section');
    section.className = 'section demo-center-section';
    section.id = 'centro-demo';
    section.innerHTML = `
      <div class="container demo-center-layout">
        <div class="demo-center-copy">
          <p class="eyebrow">EXPERIENCIA AUTOCONTENIDA</p>
          <h2>Explore cómo funciona Meridiano antes de presentar información.</h2>
          <p>El centro de demostración reúne el recorrido ejecutivo, los entregables, un caso integral ficticio, el simulador privado de alcance y el acceso a Meridiano Empresas.</p>
          <div class="architecture-proof" aria-label="Arquitectura canónica"><span><b>8</b>servicios</span><span><b>8</b>productos</span><span><b>5</b>planes</span><span><b>6</b>documentos</span></div>
          <div class="hero-actions"><a class="btn btn-gold" href="experiencia.html">Abrir centro de demostración</a><a class="btn btn-outline-light" href="demo.html">Entrar al portal</a></div>
        </div>
        <div class="demo-center-grid">
          <a class="demo-center-card" href="experiencia.html#recorrido"><span>01</span><strong>Recorrido ejecutivo</strong><small>Versión de 10 o 20 minutos para gerencia, operación y aliados.</small></a>
          <a class="demo-center-card" href="experiencia.html#entregables"><span>02</span><strong>Entregables</strong><small>Mapas, matrices, contratos, políticas, hojas de ruta y tableros.</small></a>
          <a class="demo-center-card" href="experiencia.html#caso"><span>03</span><strong>Caso integral</strong><small>Escenario ficticio desde el diagnóstico hasta el seguimiento.</small></a>
          <a class="demo-center-card" href="experiencia.html#simulador"><span>04</span><strong>Simulador de alcance</strong><small>Hipótesis privada sin precios vinculantes ni envío de información.</small></a>
          <a class="demo-center-card" href="demo.html"><span>05</span><strong>Meridiano Empresas</strong><small>Solicitudes, expedientes, documentos, obligaciones, riesgos y analítica.</small></a>
          <a class="demo-center-card" href="#contacto"><span>06</span><strong>Presentar necesidad</strong><small>Un canal directo para definir contexto, disponibilidad y siguiente paso.</small></a>
        </div>
      </div>
    `;
    contact.before(section);
  }

  function activateNavigation() {
    const links = [...document.querySelectorAll('.main-nav a[href^="#"]')];
    const sections = links
      .map((link) => document.querySelector(link.getAttribute('href')))
      .filter(Boolean);
    if (!links.length || !sections.length || !('IntersectionObserver' in window)) return;

    const byId = new Map(links.map((link) => [link.getAttribute('href').slice(1), link]));
    const observer = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (!visible) return;
      links.forEach((link) => link.classList.remove('active'));
      byId.get(visible.target.id)?.classList.add('active');
    }, { rootMargin: '-25% 0px -60% 0px', threshold: [0.05, 0.25, 0.5] });
    sections.forEach((section) => observer.observe(section));
  }

  function syncVersion() {
    const label = [...document.querySelectorAll('.footer-bottom span')]
      .find((element) => element.textContent.includes('Versión web GitHub Pages'));
    if (label) label.textContent = `Versión web GitHub Pages · v${VERSION}`;
  }

  ensureStylesheet('enhancements.css');
  ensureStylesheet('autocontenida.css');
  ensureManifest();
  ensureCanonical();
  addLegalLinks();
  addFloatingActions();
  addTrustNote();
  addDemoNavigation();
  addWorkModes();
  addDemoCenter();
  activateNavigation();
  syncVersion();
})();

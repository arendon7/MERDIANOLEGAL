(() => {
  const VERSION = '2.30.0';
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
  ensureManifest();
  ensureCanonical();
  addLegalLinks();
  addFloatingActions();
  addTrustNote();
  activateNavigation();
  syncVersion();
})();

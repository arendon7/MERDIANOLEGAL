(() => {
  const CONTEXT_KEY = 'meridiano.contactContext';
  const ROOT_PATH = '/MERDIANOLEGAL/';
  const body = document.body;

  const safeStorage = {
    get() {
      try {
        const raw = sessionStorage.getItem(CONTEXT_KEY);
        return raw ? JSON.parse(raw) : null;
      } catch {
        return null;
      }
    },
    set(value) {
      try {
        sessionStorage.setItem(CONTEXT_KEY, JSON.stringify(value));
      } catch {
        // El contexto es una mejora de navegación, no un requisito funcional.
      }
    },
    clear() {
      try {
        sessionStorage.removeItem(CONTEXT_KEY);
      } catch {
        // Sin efecto sobre la navegación principal.
      }
    },
  };

  const normalizeNeed = (value = '') => value.trim();
  const normalizeLabel = (value = '') => value.trim().replace(/\s+/g, ' ');

  const contextualUrl = (href, label, need = '') => {
    const url = new URL(href, window.location.href);
    url.searchParams.set('context', normalizeLabel(label));
    if (need) url.searchParams.set('need', normalizeNeed(need));
    return `${url.pathname}${url.search}${url.hash}`;
  };

  const storeContext = (label, need = '') => {
    const context = { label: normalizeLabel(label), need: normalizeNeed(need), savedAt: Date.now() };
    if (context.label) safeStorage.set(context);
    return context;
  };

  const restoreContextIntoLocation = () => {
    const isHome = window.location.pathname.endsWith(ROOT_PATH) || window.location.pathname.endsWith(`${ROOT_PATH}index.html`);
    if (!isHome || new URLSearchParams(window.location.search).has('context')) return;
    const stored = safeStorage.get();
    if (!stored?.label) return;
    const url = new URL(window.location.href);
    url.searchParams.set('context', stored.label);
    if (stored.need) url.searchParams.set('need', stored.need);
    history.replaceState(null, '', `${url.pathname}${url.search}${url.hash}`);
  };

  restoreContextIntoLocation();

  const addJsonLd = (id, data) => {
    if (document.getElementById(id)) return;
    const script = document.createElement('script');
    script.id = id;
    script.type = 'application/ld+json';
    script.textContent = JSON.stringify(data);
    document.head.append(script);
  };

  const isHome = window.location.pathname.endsWith(ROOT_PATH) || window.location.pathname.endsWith(`${ROOT_PATH}index.html`);
  if (isHome) {
    addJsonLd('meridiano-legalservice-schema', {
      '@context': 'https://schema.org',
      '@type': 'LegalService',
      name: 'Meridiano Legal',
      url: 'https://arendon7.github.io/MERDIANOLEGAL/',
      logo: 'https://arendon7.github.io/MERDIANOLEGAL/assets/logo-meridiano-v3.svg',
      image: 'https://arendon7.github.io/MERDIANOLEGAL/assets/hero-meridiano-v3.svg',
      description: 'Dirección jurídica, servicios profesionales y productos jurídicos para empresas, innovación y proyectos regulados.',
      areaServed: { '@type': 'Country', name: 'Colombia' },
      address: { '@type': 'PostalAddress', addressLocality: 'Medellín', addressCountry: 'CO' },
      founder: { '@type': 'Person', name: 'Agustín Rendón Calle' },
      telephone: '+57 300 850 7813',
      serviceType: [
        'Dirección jurídica externa',
        'Contratación estratégica',
        'Sociedades, gobierno e inversión',
        'Propiedad intelectual',
        'Gobernanza jurídica de inteligencia artificial',
        'Proyectos regulados',
        'Legal Operations',
      ],
    });
  }

  const pageTitle = normalizeLabel(body.dataset.pageTitle || document.querySelector('h1')?.textContent || document.title.split('|')[0]);
  const pageType = normalizeLabel(body.dataset.pageType || '');
  const pageNeed = normalizeNeed(body.dataset.pageNeed || '');
  const ownContext = pageTitle ? `${pageType || 'Página'}: ${pageTitle}` : '';

  const addVisibleEditorialMetadata = () => {
    if (!['Perspectiva', 'Sector', 'La firma'].includes(pageType)) return;
    const main = document.querySelector('main');
    const journey = document.querySelector('.editorial-journey');
    if (!main || !journey || document.querySelector('.editorial-meta-strip')) return;
    const strip = document.createElement('div');
    strip.className = 'editorial-meta-strip';
    const content = document.createElement('div');
    content.className = 'container';
    if (pageType === 'Perspectiva') {
      content.innerHTML = '<span>Autor</span><strong>Agustín Rendón Calle</strong><span>Revisión editorial</span><strong>5 de agosto de 2026</strong><small>Contenido general y educativo</small>';
    } else if (pageType === 'Sector') {
      content.innerHTML = '<span>Enfoque sectorial</span><strong>Meridiano Legal</strong><span>Revisión editorial</span><strong>5 de agosto de 2026</strong><small>El régimen aplicable debe validarse para cada caso</small>';
    } else {
      content.innerHTML = '<span>Dirección</span><strong>Agustín Rendón Calle</strong><span>Base</span><strong>Medellín, Colombia</strong><small>Información institucional revisada el 5 de agosto de 2026</small>';
    }
    strip.append(content);
    main.before(strip);
  };

  addVisibleEditorialMetadata();
  if (ownContext) storeContext(ownContext, pageNeed);

  const rewriteContactLinks = () => {
    if (!ownContext) return;
    document.querySelectorAll('a[href*="#contacto"]').forEach((link) => {
      if (link.dataset.contextualized === 'true') return;
      const href = link.getAttribute('href');
      if (!href) return;
      link.href = contextualUrl(href, ownContext, pageNeed);
      link.dataset.contextualized = 'true';
      link.addEventListener('click', () => storeContext(ownContext, pageNeed));
    });
  };

  const rewriteGeneratedActions = () => {
    if (!ownContext) return;
    document.querySelectorAll('.detail-contact-panel a, .detail-cta-row a').forEach((link) => {
      const href = link.getAttribute('href') || '';
      if (href.includes('index.html#contacto') || href.includes('index.html?')) {
        link.href = contextualUrl(href, ownContext, pageNeed);
        link.addEventListener('click', () => storeContext(ownContext, pageNeed), { once: true });
      }
      if (href.startsWith('https://wa.me/') && !href.includes('text=')) {
        const message = `Hola, revisé ${ownContext} en Meridiano Legal y quiero presentar una necesidad relacionada.`;
        link.href = `${href}?text=${encodeURIComponent(message)}`;
      }
    });
  };

  rewriteContactLinks();
  rewriteGeneratedActions();

  const contentTarget = document.getElementById('detail-page');
  if (contentTarget) {
    new MutationObserver(() => {
      rewriteContactLinks();
      rewriteGeneratedActions();
    }).observe(contentTarget, { childList: true, subtree: true });
  }

  document.querySelectorAll('[data-context-label]').forEach((link) => {
    const label = link.dataset.contextLabel || link.textContent;
    const need = link.dataset.contextNeed || '';
    link.addEventListener('click', () => storeContext(label, need));
  });

  const menu = document.querySelector('.detail-menu');
  const nav = document.querySelector('.detail-nav');
  if (menu && nav) {
    const syncMenu = () => {
      const open = menu.getAttribute('aria-expanded') === 'true';
      body.classList.toggle('detail-menu-open', open);
      menu.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    };
    new MutationObserver(syncMenu).observe(menu, { attributes: true, attributeFilter: ['aria-expanded'] });
    nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
      menu.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
    }));
    syncMenu();
  }

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape' || !menu || !nav?.classList.contains('open')) return;
    menu.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
    menu.focus();
  });

  window.MeridianoContext = {
    store: storeContext,
    clear: safeStorage.clear,
    contextualUrl,
  };
})();

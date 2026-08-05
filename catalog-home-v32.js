(() => {
  const CONTEXT_KEY = 'meridiano.contactContext';

  const serviceUrls = {
    diagnostic: { url: 'servicios/diagnostico-juridico-empresarial.html', label: 'Servicio: Diagnóstico Jurídico Empresarial', need: 'Diagnóstico jurídico' },
    direction: { url: 'servicios/direccion-juridica-externa.html', label: 'Servicio: Dirección Jurídica Externa', need: 'Dirección jurídica externa' },
    contracts: { url: 'servicios/contratacion-estrategica.html', label: 'Servicio: Contratación Estratégica y Gestión Contractual', need: 'Contratos y negociaciones' },
    corporate: { url: 'servicios/sociedades-gobierno-inversion.html', label: 'Servicio: Sociedades, Gobierno e Inversión', need: 'Socios, gobierno o inversión' },
    ip: { url: 'servicios/propiedad-intelectual.html', label: 'Servicio: Propiedad Intelectual y Activos Intangibles', need: 'Marca, software o intangibles' },
    ai: { url: 'servicios/tecnologia-inteligencia-artificial.html', label: 'Servicio: Gobernanza Jurídica de Tecnología e Inteligencia Artificial', need: 'Gobernanza de IA' },
    regulated: { url: 'servicios/proyectos-regulados.html', label: 'Servicio: Estructuración Jurídica de Proyectos Regulados', need: 'Proyecto regulado' },
    ops: { url: 'servicios/legal-operations.html', label: 'Servicio: Legal Operations y Transformación de la Función Jurídica', need: 'Legal Operations' },
  };

  const productUrls = {
    'Diagnóstico Jurídico Empresarial': { url: 'productos/diagnostico-juridico-empresarial.html', need: 'Diagnóstico jurídico' },
    'Empresa Jurídicamente Organizada': { url: 'productos/empresa-juridicamente-organizada.html', need: 'Diagnóstico jurídico' },
    'Marca, Software y Activos Intangibles Protegidos': { url: 'productos/activos-intangibles-protegidos.html', need: 'Marca, software o intangibles' },
    'Empresa Lista para Inversión': { url: 'productos/empresa-lista-para-inversion.html', need: 'Socios, gobierno o inversión' },
    'Programa de Gobernanza de IA': { url: 'productos/programa-gobernanza-ia.html', need: 'Gobernanza de IA' },
    'Proyecto Regulado Estructurado': { url: 'productos/proyecto-regulado-estructurado.html', need: 'Proyecto regulado' },
    'Sistema Contractual Empresarial': { url: 'productos/sistema-contractual-empresarial.html', need: 'Contratos y negociaciones' },
    'Programa de Protección de Datos y Consumidor': { url: 'productos/proteccion-datos-consumidor.html', need: 'Legal Operations' },
  };

  const serviceTitleKeys = {
    'Diagnóstico Jurídico Empresarial': 'diagnostic',
    'Dirección Jurídica Externa': 'direction',
    'Contratación Estratégica y Gestión Contractual': 'contracts',
    'Sociedades, Gobierno e Inversión': 'corporate',
    'Propiedad Intelectual y Activos Intangibles': 'ip',
    'Gobernanza Jurídica de Tecnología e Inteligencia Artificial': 'ai',
    'Estructuración Jurídica de Proyectos Regulados': 'regulated',
    'Legal Operations y Transformación de la Función Jurídica': 'ops',
  };

  const perspectiveUrls = {
    ai: { url: 'perspectivas/gobierno-juridico-inteligencia-artificial.html', label: 'Perspectiva: Gobierno jurídico de inteligencia artificial', need: 'Gobernanza de IA' },
    contracts: { url: 'perspectivas/contratos-administrables.html', label: 'Perspectiva: Contratos administrables', need: 'Contratos y negociaciones' },
    regulated: { url: 'perspectivas/proyectos-regulados-secuencia-viabilidad.html', label: 'Perspectiva: Secuencia de viabilidad en proyectos regulados', need: 'Proyecto regulado' },
  };

  const sectorUrls = {
    'Tecnología, software e IA': { url: 'sectores/tecnologia-software-ia.html', need: 'Gobernanza de IA' },
    'Servicios públicos, aseo y economía circular': { url: 'sectores/servicios-publicos-aseo-economia-circular.html', need: 'Proyecto regulado' },
    'Agroindustria y fertilizantes': { url: 'sectores/agroindustria-fertilizantes-sostenibilidad.html', need: 'Proyecto regulado' },
    'Salud y negocios regulados': { url: 'sectores/salud-negocios-regulados.html', need: 'Proyecto regulado' },
    'Proyectos públicos': { url: 'sectores/proyectos-publicos-territoriales.html', need: 'Proyecto regulado' },
    'Comercio y distribución': { url: 'sectores/comercio-distribucion.html', need: 'Contratos y negociaciones' },
    'Startups e inversión': { url: 'sectores/startups-inversion.html', need: 'Socios, gobierno o inversión' },
    'Transformación de operaciones jurídicas': { url: 'sectores/operaciones-juridicas.html', need: 'Legal Operations' },
  };

  const ensureStylesheet = () => {
    if (document.querySelector('link[href="page-context.css"]')) return;
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'page-context.css';
    document.head.append(link);
  };
  ensureStylesheet();

  const storeContext = (label, need = '') => {
    try {
      sessionStorage.setItem(CONTEXT_KEY, JSON.stringify({ label, need, savedAt: Date.now() }));
    } catch {
      // La navegación sigue funcionando sin almacenamiento de sesión.
    }
  };

  const contextualHref = (url, label, need = '') => {
    const params = new URLSearchParams({ context: label });
    if (need) params.set('need', need);
    return `${url}?${params.toString()}`;
  };

  const attachContext = (link, label, need = '') => {
    link.dataset.contextLabel = label;
    link.dataset.contextNeed = need;
    link.addEventListener('click', () => storeContext(label, need));
  };

  const addLink = (card, config, text = 'Ver ficha completa') => {
    if (!card || !config?.url || card.querySelector('.full-detail-link')) return;
    const label = config.label || `Producto: ${card.querySelector('h3')?.textContent.trim() || text}`;
    const link = document.createElement('a');
    link.className = 'full-detail-link';
    link.href = contextualHref(config.url, label, config.need);
    link.textContent = text;
    attachContext(link, label, config.need);
    card.append(link);
  };

  document.querySelectorAll('.service-card [data-service]').forEach((button) => {
    addLink(button.closest('.service-card'), serviceUrls[button.dataset.service]);
  });

  document.querySelectorAll('.product-card [data-product]').forEach((button) => {
    const title = button.dataset.product;
    const config = productUrls[title];
    if (config) addLink(button.closest('.product-card'), { ...config, label: `Producto: ${title}` });
  });

  const firmCopy = document.querySelector('#firma .editorial-copy');
  if (firmCopy && !firmCopy.querySelector('.firm-deep-link')) {
    const label = 'Página institucional: La firma y su método';
    const link = document.createElement('a');
    link.className = 'firm-deep-link';
    link.href = contextualHref('firma.html', label);
    link.textContent = 'Conocer la firma y su método';
    attachContext(link, label);
    firmCopy.append(link);
  }

  document.querySelectorAll('.perspectives-grid article').forEach((card) => {
    const button = card.querySelector('[data-service]');
    const config = perspectiveUrls[button?.dataset.service];
    if (!config || card.querySelector('.perspective-read-link')) return;
    const link = document.createElement('a');
    link.className = 'perspective-read-link';
    link.href = contextualHref(config.url, config.label, config.need);
    link.textContent = 'Leer perspectiva completa';
    attachContext(link, config.label, config.need);
    card.append(link);
  });

  const perspectivesHeading = document.querySelector('#perspectivas .section-heading');
  if (perspectivesHeading && !perspectivesHeading.querySelector('.library-deep-link')) {
    const label = 'Biblioteca: Perspectivas Meridiano';
    const action = document.createElement('div');
    action.className = 'perspective-library-action';
    const link = document.createElement('a');
    link.className = 'library-deep-link';
    link.href = contextualHref('perspectivas.html', label);
    link.textContent = 'Abrir biblioteca de perspectivas';
    attachContext(link, label);
    action.append(link);
    perspectivesHeading.append(action);
  }

  const sectorCards = [...document.querySelectorAll('.sectors-grid article')];
  const publicServicesCard = sectorCards.find((card) => card.querySelector('strong')?.textContent.trim() === 'Servicios públicos');
  if (publicServicesCard) {
    publicServicesCard.querySelector('strong').textContent = 'Servicios públicos, aseo y economía circular';
    const description = publicServicesCard.querySelector('p');
    if (description) description.textContent = 'Modelos operativos, actores territoriales, habilitaciones, contratos, obligaciones y aprovechamiento.';
  }

  const circularCard = sectorCards.find((card) => card.querySelector('strong')?.textContent.trim() === 'Economía circular y aseo');
  if (circularCard) {
    circularCard.querySelector('strong').textContent = 'Transformación de operaciones jurídicas';
    const description = circularCard.querySelector('p');
    if (description) description.textContent = 'Solicitudes, procesos, documentos, obligaciones, métricas, automatización y gestión del cambio.';
  }

  sectorCards.forEach((card) => {
    const title = card.querySelector('strong')?.textContent.trim();
    const config = sectorUrls[title];
    if (!config || card.querySelector('.sector-deep-link')) return;
    const label = `Sector: ${title}`;
    const link = document.createElement('a');
    link.className = 'sector-deep-link';
    link.href = contextualHref(config.url, label, config.need);
    link.textContent = 'Explorar sector';
    attachContext(link, label, config.need);
    card.append(link);
  });

  const mainNav = document.querySelector('.main-nav');
  if (mainNav && !mainNav.querySelector('.nav-perspectives')) {
    const link = document.createElement('a');
    link.className = 'nav-perspectives';
    link.href = 'perspectivas.html';
    link.textContent = 'Perspectivas';
    const contactLink = [...mainNav.querySelectorAll('a')].find((item) => item.getAttribute('href') === '#contacto');
    mainNav.insertBefore(link, contactLink || null);
  }

  const modalContent = document.getElementById('modal-content');
  if (modalContent) {
    const syncModalLink = () => {
      const title = modalContent.querySelector('h2')?.textContent?.trim();
      const code = modalContent.querySelector('.modal-aside span')?.textContent?.trim() || '';
      const actions = modalContent.querySelector('.modal-actions');
      const productMode = code.includes('PRODUCTO') || code.includes('PUNTO DE ENTRADA');
      const config = productMode
        ? productUrls[title] && { ...productUrls[title], label: `Producto: ${title}` }
        : serviceUrls[serviceTitleKeys[title]];
      if (!actions || !config?.url || actions.querySelector('.full-detail-link')) return;
      const link = document.createElement('a');
      link.className = 'full-detail-link';
      link.href = contextualHref(config.url, config.label, config.need);
      link.textContent = 'Abrir ficha completa';
      attachContext(link, config.label, config.need);
      actions.append(link);
    };
    new MutationObserver(syncModalLink).observe(modalContent, { childList: true, subtree: true });
  }

  const loadScript = (src, marker, onload) => {
    const current = document.querySelector(`script[${marker}]`);
    if (current) {
      if (onload) onload();
      return;
    }
    const script = document.createElement('script');
    script.src = src;
    script.setAttribute(marker, '');
    if (onload) script.addEventListener('load', onload, { once: true });
    document.body.append(script);
  };

  const setVersion = () => {
    const versionLabel = [...document.querySelectorAll('.footer-bottom span')].find((item) => item.textContent.includes('Web demostrativa'));
    if (versionLabel) versionLabel.textContent = 'Web demostrativa v3.6.0';
  };

  loadScript('page-context.js', 'data-page-context', () => {
    loadScript('decision-flow.js', 'data-decision-flow', setVersion);
  });
  setVersion();
})();

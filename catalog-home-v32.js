(() => {
  const serviceUrls = {
    diagnostic: 'servicios/diagnostico-juridico-empresarial.html',
    direction: 'servicios/direccion-juridica-externa.html',
    contracts: 'servicios/contratacion-estrategica.html',
    corporate: 'servicios/sociedades-gobierno-inversion.html',
    ip: 'servicios/propiedad-intelectual.html',
    ai: 'servicios/tecnologia-inteligencia-artificial.html',
    regulated: 'servicios/proyectos-regulados.html',
    ops: 'servicios/legal-operations.html',
  };
  const productUrls = {
    'Diagnóstico Jurídico Empresarial': 'productos/diagnostico-juridico-empresarial.html',
    'Empresa Jurídicamente Organizada': 'productos/empresa-juridicamente-organizada.html',
    'Marca, Software y Activos Intangibles Protegidos': 'productos/activos-intangibles-protegidos.html',
    'Empresa Lista para Inversión': 'productos/empresa-lista-para-inversion.html',
    'Programa de Gobernanza de IA': 'productos/programa-gobernanza-ia.html',
    'Proyecto Regulado Estructurado': 'productos/proyecto-regulado-estructurado.html',
    'Sistema Contractual Empresarial': 'productos/sistema-contractual-empresarial.html',
    'Programa de Protección de Datos y Consumidor': 'productos/proteccion-datos-consumidor.html',
  };
  const serviceTitleUrls = {
    'Diagnóstico Jurídico Empresarial': serviceUrls.diagnostic,
    'Dirección Jurídica Externa': serviceUrls.direction,
    'Contratación Estratégica y Gestión Contractual': serviceUrls.contracts,
    'Sociedades, Gobierno e Inversión': serviceUrls.corporate,
    'Propiedad Intelectual y Activos Intangibles': serviceUrls.ip,
    'Gobernanza Jurídica de Tecnología e Inteligencia Artificial': serviceUrls.ai,
    'Estructuración Jurídica de Proyectos Regulados': serviceUrls.regulated,
    'Legal Operations y Transformación de la Función Jurídica': serviceUrls.ops,
  };
  const perspectiveUrls = {
    ai: 'perspectivas/gobierno-juridico-inteligencia-artificial.html',
    contracts: 'perspectivas/contratos-administrables.html',
    regulated: 'perspectivas/proyectos-regulados-secuencia-viabilidad.html',
  };
  const sectorUrls = {
    'Tecnología, software e IA': 'sectores/tecnologia-software-ia.html',
    'Servicios públicos, aseo y economía circular': 'sectores/servicios-publicos-aseo-economia-circular.html',
    'Agroindustria y fertilizantes': 'sectores/agroindustria-fertilizantes-sostenibilidad.html',
    'Salud y negocios regulados': 'sectores/salud-negocios-regulados.html',
    'Proyectos públicos': 'sectores/proyectos-publicos-territoriales.html',
    'Comercio y distribución': 'sectores/comercio-distribucion.html',
    'Startups e inversión': 'sectores/startups-inversion.html',
    'Transformación de operaciones jurídicas': 'sectores/operaciones-juridicas.html',
  };

  const style = document.createElement('style');
  style.textContent = `
    .full-detail-link{display:inline-flex;align-items:center;gap:7px;margin-top:10px;color:#2c5878!important;font-size:.69rem!important;font-weight:900!important;text-transform:uppercase;letter-spacing:.055em;text-decoration:none}
    .full-detail-link:after{content:'→';color:#a88454}.service-card .full-detail-link,.product-card .full-detail-link{margin-top:9px}.product-card .full-detail-link{color:#d9bc8b!important}.modal-actions .full-detail-link{margin-top:0;padding:12px 18px;border:1px solid rgba(19,38,58,.28);color:#13263a!important;background:#fff}.modal-actions .full-detail-link:after{display:none}
    .firm-deep-link,.library-deep-link,.perspective-read-link,.sector-deep-link{display:inline-flex;align-items:center;gap:9px;margin-top:22px;padding:12px 17px;border:1px solid rgba(19,38,58,.28);color:#13263a;font-size:.71rem;font-weight:900;letter-spacing:.06em;text-transform:uppercase;text-decoration:none}.firm-deep-link:after,.library-deep-link:after,.perspective-read-link:after,.sector-deep-link:after{content:'→';color:#a88454}.firm-deep-link:hover,.library-deep-link:hover,.perspective-read-link:hover,.sector-deep-link:hover{border-color:#a88454;color:#a88454}
    .perspectives-grid article,.sectors-grid article{display:flex;flex-direction:column}.perspectives-grid article .perspective-read-link{margin-top:auto;align-self:flex-start;color:#13263a!important}.sectors-grid article .sector-deep-link{margin-top:auto;align-self:flex-start;padding:0;border:0;color:#2c5878!important;font-size:.67rem}.perspective-library-action{margin-top:8px}.main-nav .nav-perspectives{color:#a88454}
  `;
  document.head.append(style);

  const addLink = (card, url) => {
    if (!card || !url || card.querySelector('.full-detail-link')) return;
    const link = document.createElement('a');
    link.className = 'full-detail-link';
    link.href = url;
    link.textContent = 'Ver ficha completa';
    card.append(link);
  };

  document.querySelectorAll('.service-card [data-service]').forEach((button) => addLink(button.closest('.service-card'), serviceUrls[button.dataset.service]));
  document.querySelectorAll('.product-card [data-product]').forEach((button) => addLink(button.closest('.product-card'), productUrls[button.dataset.product]));

  const firmCopy = document.querySelector('#firma .editorial-copy');
  if (firmCopy && !firmCopy.querySelector('.firm-deep-link')) {
    const link = document.createElement('a');
    link.className = 'firm-deep-link';
    link.href = 'firma.html';
    link.textContent = 'Conocer la firma y su método';
    firmCopy.append(link);
  }

  document.querySelectorAll('.perspectives-grid article').forEach((card) => {
    const button = card.querySelector('[data-service]');
    const url = perspectiveUrls[button?.dataset.service];
    if (!url || card.querySelector('.perspective-read-link')) return;
    const link = document.createElement('a');
    link.className = 'perspective-read-link';
    link.href = url;
    link.textContent = 'Leer perspectiva completa';
    card.append(link);
  });

  const perspectivesHeading = document.querySelector('#perspectivas .section-heading');
  if (perspectivesHeading && !perspectivesHeading.querySelector('.library-deep-link')) {
    const action = document.createElement('div');
    action.className = 'perspective-library-action';
    const link = document.createElement('a');
    link.className = 'library-deep-link';
    link.href = 'perspectivas.html';
    link.textContent = 'Abrir biblioteca de perspectivas';
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
    const url = sectorUrls[title];
    if (!url || card.querySelector('.sector-deep-link')) return;
    const link = document.createElement('a');
    link.className = 'sector-deep-link';
    link.href = url;
    link.textContent = 'Explorar sector';
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
      const url = productMode ? productUrls[title] : serviceTitleUrls[title];
      if (!actions || !url || actions.querySelector('.full-detail-link')) return;
      const link = document.createElement('a');
      link.className = 'full-detail-link';
      link.href = url;
      link.textContent = 'Abrir ficha completa';
      actions.append(link);
    };
    new MutationObserver(syncModalLink).observe(modalContent, { childList: true, subtree: true });
  }

  const versionLabel = [...document.querySelectorAll('.footer-bottom span')].find((item) => item.textContent.includes('Web demostrativa'));
  if (versionLabel) versionLabel.textContent = 'Web demostrativa v3.4.0';
})();

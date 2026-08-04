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
  const titleUrls = {
    'Diagnóstico Jurídico Empresarial': productUrls['Diagnóstico Jurídico Empresarial'],
    'Dirección Jurídica Externa': serviceUrls.direction,
    'Contratación Estratégica y Gestión Contractual': serviceUrls.contracts,
    'Sociedades, Gobierno e Inversión': serviceUrls.corporate,
    'Propiedad Intelectual y Activos Intangibles': serviceUrls.ip,
    'Gobernanza Jurídica de Tecnología e Inteligencia Artificial': serviceUrls.ai,
    'Estructuración Jurídica de Proyectos Regulados': serviceUrls.regulated,
    'Legal Operations y Transformación de la Función Jurídica': serviceUrls.ops,
    ...productUrls,
  };

  const style = document.createElement('style');
  style.textContent = `
    .full-detail-link{display:inline-flex;align-items:center;gap:7px;margin-top:10px;color:#2c5878!important;font-size:.69rem!important;font-weight:900!important;text-transform:uppercase;letter-spacing:.055em;text-decoration:none}
    .full-detail-link:after{content:'→';color:#a88454}.service-card .full-detail-link,.product-card .full-detail-link{margin-top:9px}.product-card .full-detail-link{color:#d9bc8b!important}.modal-actions .full-detail-link{margin-top:0;padding:12px 18px;border:1px solid rgba(19,38,58,.28);color:#13263a!important;background:#fff}.modal-actions .full-detail-link:after{display:none}
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

  const modalContent = document.getElementById('modal-content');
  if (modalContent) {
    const syncModalLink = () => {
      const title = modalContent.querySelector('h2')?.textContent?.trim();
      const actions = modalContent.querySelector('.modal-actions');
      const url = titleUrls[title];
      if (!actions || !url || actions.querySelector('.full-detail-link')) return;
      const link = document.createElement('a');
      link.className = 'full-detail-link';
      link.href = url;
      link.textContent = 'Abrir ficha completa';
      actions.append(link);
    };
    new MutationObserver(syncModalLink).observe(modalContent, { childList: true, subtree: true });
  }
})();

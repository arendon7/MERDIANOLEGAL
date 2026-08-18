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
    'Auditoría Jurídica Empresarial Integral': { url: 'productos/diagnostico-juridico-empresarial.html', need: 'Diagnóstico jurídico' },
    'Empresa Jurídicamente Organizada': { url: 'productos/empresa-juridicamente-organizada.html', need: 'Diagnóstico jurídico' },
    'Marca, Software y Activos Intangibles Protegidos': { url: 'productos/activos-intangibles-protegidos.html', need: 'Marca, software o intangibles' },
    'Empresa Lista para Inversión': { url: 'productos/empresa-lista-para-inversion.html', need: 'Socios, gobierno o inversión' },
    'Programa de Gobernanza Jurídica y Uso Responsable de IA': { url: 'productos/programa-gobernanza-ia.html', need: 'Gobernanza de IA' },
    'Proyecto Regulado Jurídicamente Estructurado': { url: 'productos/proyecto-regulado-estructurado.html', need: 'Proyecto regulado' },
    'Sistema Contractual Empresarial': { url: 'productos/sistema-contractual-empresarial.html', need: 'Contratos y negociaciones' },
    'Programa de Datos, Consumidor y Canales Digitales': { url: 'productos/proteccion-datos-consumidor.html', need: 'Legal Operations' },
  };

  const productCardUpgrades = {
    'Diagnóstico Jurídico Empresarial': { title: 'Auditoría Jurídica Empresarial Integral', duration: '5 a 6 semanas', summary: 'Revisión transversal con hasta 80 hallazgos, cinco instrumentos correctivos y plan jurídico de 90 días.', config: productUrls['Auditoría Jurídica Empresarial Integral'] },
    'Empresa Jurídicamente Organizada': { title: 'Empresa Jurídicamente Organizada', duration: '6 a 10 semanas', summary: 'Gobierno, atribuciones, contratos, obligaciones y expediente jurídico organizados como sistema operativo.', config: productUrls['Empresa Jurídicamente Organizada'] },
    'Marca, Software y Activos Intangibles Protegidos': { title: 'Marca, Software y Activos Intangibles Protegidos', duration: '6 a 8 semanas', summary: 'Inventario, titularidad, protección, licencias y evidencia para hasta 40 activos intangibles priorizados.', config: productUrls['Marca, Software y Activos Intangibles Protegidos'] },
    'Empresa Lista para Inversión': { title: 'Empresa Lista para Inversión', duration: '8 a 10 semanas', summary: 'Red flags, cap table, contratos materiales, regularizaciones y data room jurídico antes de una inversión.', config: productUrls['Empresa Lista para Inversión'] },
    'Programa de Gobernanza de IA': { title: 'Programa de Gobernanza Jurídica y Uso Responsable de IA', duration: '8 a 10 semanas', summary: 'Hasta 25 casos de uso, clasificación de riesgo, reglas de uso, proveedores, controles, incidentes y capacitación.', config: productUrls['Programa de Gobernanza Jurídica y Uso Responsable de IA'] },
    'Proyecto Regulado Estructurado': { title: 'Proyecto Regulado Jurídicamente Estructurado', duration: '8 a 10 semanas', summary: 'Autoridades, permisos, predios, contratos, condiciones precedentes y ruta habilitante del proyecto.', config: productUrls['Proyecto Regulado Jurídicamente Estructurado'] },
    'Sistema Contractual Empresarial': { title: 'Sistema Contractual Empresarial', duration: '8 a 10 semanas', summary: 'Seis modelos, biblioteca de cláusulas, playbook, aprobaciones, hasta 100 obligaciones y repositorio contractual.', config: productUrls['Sistema Contractual Empresarial'] },
    'Programa de Protección de Datos y Consumidor': { title: 'Programa de Datos, Consumidor y Canales Digitales', duration: '8 a 10 semanas', summary: 'Tratamientos, bases, términos, PQR, incidentes, proveedores y evidencia operativa para datos y consumidor.', config: productUrls['Programa de Datos, Consumidor y Canales Digitales'] },
  };

  const storeContext = (label, need = '') => {
    try { sessionStorage.setItem(CONTEXT_KEY, JSON.stringify({ label, need, savedAt: Date.now() })); } catch {}
  };
  const contextualHref = (url, label, need = '') => {
    const params = new URLSearchParams({ context: label });
    if (need) params.set('need', need);
    return `${url}?${params.toString()}`;
  };

  Object.entries(productCardUpgrades).forEach(([legacyTitle, upgrade]) => {
    const button = document.querySelector(`.product-card [data-product="${legacyTitle}"]`);
    const card = button?.closest('.product-card');
    if (!card) return;
    const title = card.querySelector('h3');
    const duration = card.querySelector('small');
    const description = card.querySelector('p');
    if (title) title.textContent = upgrade.title;
    if (duration) duration.textContent = upgrade.duration;
    if (description) description.textContent = upgrade.summary;
    button.textContent = 'Ver ficha →';
    button.addEventListener('click', (event) => {
      event.preventDefault(); event.stopImmediatePropagation();
      const label = `Producto: ${upgrade.title}`;
      storeContext(label, upgrade.config.need);
      location.href = contextualHref(upgrade.config.url, label, upgrade.config.need);
    }, true);
  });

  const serviceTitleKeys = {
    'Diagnóstico Jurídico Empresarial': 'diagnostic', 'Dirección Jurídica Externa': 'direction', 'Contratación Estratégica y Gestión Contractual': 'contracts', 'Sociedades, Gobierno e Inversión': 'corporate', 'Propiedad Intelectual y Activos Intangibles': 'ip', 'Gobernanza Jurídica de Tecnología e Inteligencia Artificial': 'ai', 'Estructuración Jurídica de Proyectos Regulados': 'regulated', 'Legal Operations y Transformación de la Función Jurídica': 'ops',
  };
  const perspectiveUrls = {
    ai: { url: 'perspectivas/gobierno-juridico-inteligencia-artificial.html', label: 'Perspectiva: Gobierno jurídico de inteligencia artificial', need: 'Gobernanza de IA' }, contracts: { url: 'perspectivas/contratos-administrables.html', label: 'Perspectiva: Contratos administrables', need: 'Contratos y negociaciones' }, regulated: { url: 'perspectivas/proyectos-regulados-secuencia-viabilidad.html', label: 'Perspectiva: Secuencia de viabilidad en proyectos regulados', need: 'Proyecto regulado' },
  };
  const sectorUrls = {
    'Tecnología, software e IA': { url: 'sectores/tecnologia-software-ia.html', need: 'Gobernanza de IA' }, 'Servicios públicos, aseo y economía circular': { url: 'sectores/servicios-publicos-aseo-economia-circular.html', need: 'Proyecto regulado' }, 'Agroindustria y fertilizantes': { url: 'sectores/agroindustria-fertilizantes-sostenibilidad.html', need: 'Proyecto regulado' }, 'Salud y negocios regulados': { url: 'sectores/salud-negocios-regulados.html', need: 'Proyecto regulado' }, 'Proyectos públicos': { url: 'sectores/proyectos-publicos-territoriales.html', need: 'Proyecto regulado' }, 'Comercio y distribución': { url: 'sectores/comercio-distribucion.html', need: 'Contratos y negociaciones' }, 'Startups e inversión': { url: 'sectores/startups-inversion.html', need: 'Socios, gobierno o inversión' }, 'Transformación de operaciones jurídicas': { url: 'sectores/operaciones-juridicas.html', need: 'Legal Operations' },
  };
  if (!document.querySelector('link[href="page-context.css"]')) { const link=document.createElement('link'); link.rel='stylesheet'; link.href='page-context.css'; document.head.append(link); }
  const attachContext = (link,label,need='') => { link.dataset.contextLabel=label; link.dataset.contextNeed=need; link.addEventListener('click',()=>storeContext(label,need)); };
  const addLink = (card,config,text='Ver ficha completa') => { if(!card||!config?.url||card.querySelector('.full-detail-link')) return; const label=config.label||`Producto: ${card.querySelector('h3')?.textContent.trim()||text}`; const link=document.createElement('a'); link.className='full-detail-link'; link.href=contextualHref(config.url,label,config.need); link.textContent=text; attachContext(link,label,config.need); card.append(link); };
  document.querySelectorAll('.service-card [data-service]').forEach((button)=>addLink(button.closest('.service-card'),serviceUrls[button.dataset.service]));
  document.querySelectorAll('.product-card [data-product]').forEach((button)=>{ const legacyTitle=button.dataset.product; const upgrade=productCardUpgrades[legacyTitle]; const displayTitle=upgrade?.title||legacyTitle; const config=upgrade?.config||productUrls[legacyTitle]; if(config) addLink(button.closest('.product-card'),{...config,label:`Producto: ${displayTitle}`}); });
  const firmCopy=document.querySelector('#firma .editorial-copy'); if(firmCopy&&!firmCopy.querySelector('.firm-deep-link')){const label='Página institucional: La firma y su método'; const link=document.createElement('a'); link.className='firm-deep-link'; link.href=contextualHref('firma.html',label); link.textContent='Conocer la firma y su método'; attachContext(link,label); firmCopy.append(link);}
  document.querySelectorAll('.perspectives-grid article').forEach((card)=>{const button=card.querySelector('[data-service]'); const config=perspectiveUrls[button?.dataset.service]; if(!config||card.querySelector('.perspective-read-link'))return; const link=document.createElement('a'); link.className='perspective-read-link'; link.href=contextualHref(config.url,config.label,config.need); link.textContent='Leer perspectiva completa'; attachContext(link,config.label,config.need); card.append(link);});
  const perspectivesHeading=document.querySelector('#perspectivas .section-heading'); if(perspectivesHeading&&!perspectivesHeading.querySelector('.library-deep-link')){const label='Biblioteca: Perspectivas Meridiano'; const action=document.createElement('div'); action.className='perspective-library-action'; const link=document.createElement('a'); link.className='library-deep-link'; link.href=contextualHref('perspectivas.html',label); link.textContent='Abrir biblioteca de perspectivas'; attachContext(link,label); action.append(link); perspectivesHeading.append(action);}
  const sectorCards=[...document.querySelectorAll('.sectors-grid article')]; const publicServicesCard=sectorCards.find((card)=>card.querySelector('strong')?.textContent.trim()==='Servicios públicos'); if(publicServicesCard){publicServicesCard.querySelector('strong').textContent='Servicios públicos, aseo y economía circular'; const description=publicServicesCard.querySelector('p'); if(description)description.textContent='Modelos operativos, actores territoriales, habilitaciones, contratos, obligaciones y aprovechamiento.';} const circularCard=sectorCards.find((card)=>card.querySelector('strong')?.textContent.trim()==='Economía circular y aseo'); if(circularCard){circularCard.querySelector('strong').textContent='Transformación de operaciones jurídicas'; const description=circularCard.querySelector('p'); if(description)description.textContent='Solicitudes, procesos, documentos, obligaciones, métricas, automatización y gestión del cambio.';}
  sectorCards.forEach((card)=>{const title=card.querySelector('strong')?.textContent.trim(); const config=sectorUrls[title]; if(!config||card.querySelector('.sector-deep-link'))return; const label=`Sector: ${title}`; const link=document.createElement('a'); link.className='sector-deep-link'; link.href=contextualHref(config.url,label,config.need); link.textContent='Explorar sector'; attachContext(link,label,config.need); card.append(link);});
  const modalContent=document.getElementById('modal-content'); if(modalContent){const syncModalLink=()=>{const title=modalContent.querySelector('h2')?.textContent?.trim(); const code=modalContent.querySelector('.modal-aside span')?.textContent?.trim()||''; const actions=modalContent.querySelector('.modal-actions'); const productMode=code.includes('PRODUCTO')||code.includes('PUNTO DE ENTRADA'); const config=productMode?productUrls[title]&&{...productUrls[title],label:`Producto: ${title}`}:serviceUrls[serviceTitleKeys[title]]; if(!actions||!config?.url||actions.querySelector('.full-detail-link'))return; const link=document.createElement('a'); link.className='full-detail-link'; link.href=contextualHref(config.url,config.label,config.need); link.textContent='Abrir ficha completa'; attachContext(link,config.label,config.need); actions.append(link);}; new MutationObserver(syncModalLink).observe(modalContent,{childList:true,subtree:true});}
  const loadScript=(src,marker,onload)=>{const current=document.querySelector(`script[${marker}]`); if(current){if(onload)onload(); return;} const script=document.createElement('script'); script.src=src; script.setAttribute(marker,''); if(onload)script.addEventListener('load',onload,{once:true}); document.body.append(script);};
  const setVersion=()=>{const versionLabel=[...document.querySelectorAll('.footer-bottom span')].find((item)=>item.textContent.includes('Web demostrativa')); if(versionLabel)versionLabel.textContent='Web demostrativa v6.1.0';};
  loadScript('page-context.js','data-page-context',()=>{loadScript('decision-flow.js','data-decision-flow',setVersion);}); setVersion();
})();

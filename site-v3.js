(() => {
  const WHATSAPP_NUMBER = '573008507813';

  const services = {
    diagnostic: {
      title: 'Diagnóstico Jurídico Empresarial', code: 'DIAGNOSTIC', horizon: '2 a 4 semanas', icon: 'i-compass',
      question: '¿Qué exposiciones pueden afectar la continuidad, el patrimonio, la capacidad de contratar o la posibilidad de crecer?',
      scope: ['Existencia, representación, atribuciones y documentación societaria.', 'Contratos materiales, obligaciones, renovaciones, garantías y terminación.', 'Relaciones laborales y de servicios, propiedad intelectual, datos y consumidor.', 'Permisos, registros, autoridades y dependencias regulatorias relevantes.'],
      outputs: ['Informe jurídico ejecutivo', 'Matriz priorizada de riesgos', 'Plan jurídico de 90 días', 'Comité ejecutivo de cierre'],
      limits: ['No es auditoría de aseguramiento absoluto.', 'No cubre información no revelada.', 'Litigios, opiniones tributarias y auditorías técnicas se separan.'],
    },
    direction: {
      title: 'Dirección Jurídica Externa', code: 'LEGAL_DIRECTION', horizon: 'Plan recurrente', icon: 'i-building',
      question: '¿Quién integra jurídicamente las decisiones y asegura que las recomendaciones se ejecuten?',
      scope: ['Comité jurídico con gerencia.', 'Triage y atención preventiva dentro del volumen acordado.', 'Registro de riesgos, obligaciones, decisiones y vencimientos.', 'Coordinación de especialistas externos cuando corresponda.'],
      outputs: ['Tablero jurídico ejecutivo', 'Agenda de decisiones', 'Conceptos y revisiones dentro del alcance', 'Informe periódico y memoria institucional'],
      limits: ['No implica disponibilidad ilimitada.', 'Representación judicial y proyectos extraordinarios se separan.', 'Capacidad, SLA, canales y escalamiento se pactan.'],
    },
    contracts: {
      title: 'Contratación Estratégica y Gestión Contractual', code: 'CONTRACTS', horizon: 'Proyecto o negociación', icon: 'i-contract',
      question: '¿El contrato traduce el acuerdo comercial, distribuye riesgos y conserva opciones razonables ante cambio o incumplimiento?',
      scope: ['Etapa precontractual, autoridad y formación del consentimiento.', 'Objeto, alcance, precio, hitos, aceptación, cambios y pagos.', 'Garantías, indemnidad, responsabilidad, seguros y fuerza mayor.', 'Datos, propiedad intelectual, confidencialidad, cumplimiento y salida.'],
      outputs: ['Documento o control de cambios', 'Matriz ejecutiva de posiciones', 'Soporte de negociación', 'Ficha de obligaciones, preavisos y evidencias'],
      limits: ['No sustituye validaciones técnicas, financieras, tributarias o de seguros.', 'La empresa debe definir posiciones comerciales y autoridad para negociar.'],
    },
    corporate: {
      title: 'Sociedades, Gobierno e Inversión', code: 'CORPORATE', horizon: 'Proyecto societario', icon: 'i-partners',
      question: '¿Las reglas reflejan quién aporta, quién decide, cómo se controla y qué ocurre ante conflicto o salida?',
      scope: ['Capital, clases de acciones y derechos económicos y políticos.', 'Órganos, representación, mayorías, vetos y conflictos de interés.', 'Acuerdos de accionistas, permanencia, transferencia, salida y bloqueos.', 'Rondas, autorizaciones, actas, libros, registros y obligaciones posteriores.'],
      outputs: ['Arquitectura societaria', 'Estatutos, acuerdos o instrumentos de inversión', 'Matriz de materias reservadas y atribuciones', 'Plan de formalización'],
      limits: ['Valoración, tributación y asesoría de inversión requieren especialistas.', 'La eficacia depende de aprobación, firma, registro y libros.'],
    },
    ip: {
      title: 'Propiedad Intelectual y Activos Intangibles', code: 'IP', horizon: 'Proyecto por activo o portafolio', icon: 'i-shield',
      question: '¿La empresa puede probar quién creó sus activos, quién es titular y bajo qué condiciones se explotan?',
      scope: ['Marcas, estrategia de solicitud, titularidad, clases, uso y vigilancia.', 'Software, contenidos, contratos de creación, cesión y licencia.', 'Secretos empresariales, acceso y medidas razonables de reserva.', 'Dominios, componentes de terceros, licencias abiertas y activos digitales.'],
      outputs: ['Inventario y cadena de titularidad', 'Estrategia de protección', 'Contratos, cesiones o licencias prioritarias', 'Calendario de registros, renovaciones y vigilancia'],
      limits: ['No garantiza concesión ni ausencia de oposición.', 'Patentes, litigios y estrategias multijurisdiccionales pueden exigir especialistas.'],
    },
    ai: {
      title: 'Gobernanza Jurídica de Tecnología e Inteligencia Artificial', code: 'AI', horizon: 'Programa e implementación', icon: 'i-ai',
      question: '¿La organización sabe dónde usa IA, qué datos intervienen, quién supervisa y cómo corrige un resultado?',
      scope: ['Inventario de sistemas, casos de uso, proveedores, datos y grupos afectados.', 'Clasificación de riesgo y reglas para usos permitidos o condicionados.', 'Debida diligencia contractual y asignación de responsabilidades.', 'Supervisión humana, transparencia, incidentes, capacitación y revisión.'],
      outputs: ['Inventario y matriz de riesgo', 'Política y procedimiento de aprobación', 'Checklist de proveedores', 'Registro de controles, incidentes y revisiones'],
      limits: ['No es auditoría técnica, certificación algorítmica ni pentesting.', 'Casos de alto impacto requieren evaluación ampliada.'],
    },
    regulated: {
      title: 'Estructuración Jurídica de Proyectos Regulados', code: 'REGULATED', horizon: 'Proyecto de viabilidad', icon: 'i-regulated',
      question: '¿El proyecto debe avanzar, rediseñarse o detenerse antes de comprometer recursos?',
      scope: ['Actividad, localización, regulación y autoridad competente.', 'Permisos, registros, habilitaciones y secuencia de decisiones.', 'Actores públicos y privados, funciones, contraprestaciones y responsabilidades.', 'Vehículo, contratos, alianzas, condiciones precedentes y control.'],
      outputs: ['Concepto ejecutivo de viabilidad', 'Mapa de autoridades y actores', 'Matriz de permisos, contratos y responsabilidades', 'Hoja de ruta de estructuración'],
      limits: ['No sustituye estudios técnicos, ambientales, tarifarios, sanitarios o de ingeniería.', 'No garantiza permisos, financiación ni decisiones de terceros.'],
    },
    ops: {
      title: 'Legal Operations y Transformación de la Función Jurídica', code: 'LEGAL_OPS', horizon: 'Proyecto de transformación', icon: 'i-ops',
      question: '¿La organización puede administrar solicitudes, documentos, obligaciones y decisiones sin depender de canales informales?',
      scope: ['Diagnóstico de demanda, usuarios, canales, documentos y fricción.', 'Catálogo de servicios, taxonomía, triage, flujos y matriz RACI.', 'Banco documental, versiones, permisos, aprobaciones y evidencia.', 'Indicadores, expedientes, obligaciones, capacitación y gestión del cambio.'],
      outputs: ['Modelo operativo y catálogo de servicios', 'Flujos y matriz de roles', 'Banco documental gobernado', 'Tablero de indicadores y plan de mejora'],
      limits: ['La tecnología no corrige falta de capacidad o decisiones indefinidas.', 'Integraciones, migraciones masivas y seguridad técnica se dimensionan aparte.'],
    },
  };

  const products = {
    'Diagnóstico Jurídico Empresarial': { service: 'diagnostic', duration: '2 a 4 semanas', question: '¿Dónde está hoy la mayor exposición jurídica y qué decisiones no deberían seguir aplazándose?', deliverables: ['Informe ejecutivo con alcance y supuestos', 'Matriz de riesgos, tratamiento y riesgo residual', 'Plan jurídico de 90 días', 'Calendario de decisiones y evidencias'], limits: ['Revisión focal, no auditoría exhaustiva', 'La profundidad depende del perímetro y la evidencia', 'Remediaciones y especialidades se contratan separadamente'] },
    'Empresa Jurídicamente Organizada': { service: 'corporate', duration: '6 a 10 semanas', question: '¿La empresa puede crecer y contratar sin depender de memoria, improvisación o acuerdos verbales?', deliverables: ['Mapa societario y de atribuciones', 'Matriz contractual y de obligaciones', 'Paquete de documentos esenciales', 'Calendario de formalización'], limits: ['No cubre saneamientos históricos complejos', 'Conflictos, reorganizaciones e insolvencia se separan', 'Trámites y tasas se dimensionan'] },
    'Marca, Software y Activos Intangibles Protegidos': { service: 'ip', duration: '3 a 8 semanas', question: '¿La empresa controla jurídicamente los activos que está financiando y explotando?', deliverables: ['Inventario jurídico y cadena de titularidad', 'Análisis de protección y regularización', 'Cesiones, licencias o cláusulas prioritarias', 'Calendario de registros y vigilancia'], limits: ['No garantiza concesión registral', 'Oposiciones y litigios requieren alcance separado', 'Tiempos de autoridad no dependen de Meridiano'] },
    'Empresa Lista para Inversión': { service: 'corporate', duration: '6 a 12 semanas', question: '¿La estructura jurídica resiste una revisión razonable de inversionistas?', deliverables: ['Mapa de brechas y plan de remediación', 'Cap table y arquitectura de gobierno', 'Cadena de titularidad de activos', 'Índice de data room y contingencias'], limits: ['No incluye valoración ni modelación financiera', 'No capta inversionistas', 'Tributación y negociación integral pueden exigir especialistas'] },
    'Programa de Gobernanza de IA': { service: 'ai', duration: '4 a 8 semanas', question: '¿La organización puede demostrar cómo controla los riesgos de sus casos de uso de IA?', deliverables: ['Inventario de casos de uso', 'Matriz de clasificación de riesgo', 'Política, roles y aprobaciones', 'Plan de controles, proveedores e incidentes'], limits: ['No es auditoría técnica del modelo', 'No certifica cumplimiento o desempeño', 'Casos de alto impacto requieren alcance ampliado'] },
    'Proyecto Regulado Estructurado': { service: 'regulated', duration: '3 a 8 semanas', question: '¿Qué condiciona la viabilidad jurídica y qué debe ocurrir antes de contratar, invertir u operar?', deliverables: ['Mapa normativo y de autoridades', 'Matriz de actores y responsabilidades', 'Permisos y condiciones precedentes', 'Hoja de ruta jurídica y contractual'], limits: ['No sustituye estudios técnicos', 'No garantiza decisiones de autoridad', 'Trámites y representación se dimensionan por separado'] },
    'Sistema Contractual Empresarial': { service: 'contracts', duration: '6 a 10 semanas', question: '¿La empresa sabe qué firma, quién aprueba, qué debe administrar y cuándo debe actuar?', deliverables: ['Matriz contractual', 'Playbook de negociación', 'Biblioteca de modelos aprobados', 'Flujo de aprobación y registro de obligaciones'], limits: ['La revisión histórica masiva se dimensiona', 'Negociaciones extraordinarias no están incluidas', 'Integraciones tecnológicas requieren alcance técnico'] },
    'Programa de Protección de Datos y Consumidor': { service: 'ops', duration: '6 a 10 semanas', question: '¿La empresa puede demostrar cómo recoge datos, informa condiciones, atiende reclamos y corrige incidentes?', deliverables: ['Inventario de tratamientos y canales', 'Políticas, avisos y procedimientos', 'Matriz de proveedores y cláusulas', 'Programa de garantías, reclamos y capacitación'], limits: ['No incluye pruebas técnicas de seguridad', 'Investigaciones y litigios se separan', 'Adecuaciones internacionales requieren alcance específico'] },
  };

  const routeMap = { empresa: 'Diagnóstico Jurídico Empresarial', ia: 'Programa de Gobernanza de IA', socios: 'Empresa Lista para Inversión', intangibles: 'Marca, Software y Activos Intangibles Protegidos', regulado: 'Proyecto Regulado Estructurado', operacion: 'Sistema Contractual Empresarial' };
  const menuButton = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('.main-nav');
  const modal = document.getElementById('detail-modal');
  const modalContent = document.getElementById('modal-content');
  let lastTrigger = null;

  const create = (tag, className, text) => { const element = document.createElement(tag); if (className) element.className = className; if (text !== undefined) element.textContent = text; return element; };
  function setMenu(open) { if (!menuButton || !navigation) return; menuButton.setAttribute('aria-expanded', String(open)); navigation.classList.toggle('open', open); }
  menuButton?.addEventListener('click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true'));
  navigation?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('click', (event) => { if (!navigation?.classList.contains('open')) return; if (navigation.contains(event.target) || menuButton?.contains(event.target)) return; setMenu(false); });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape') setMenu(false); });

  const navLinks = [...document.querySelectorAll('.main-nav a[href^="#"]')];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => { const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0]; if (!visible) return; navLinks.forEach((link) => link.classList.toggle('active', link.hash === `#${visible.target.id}`)); }, { rootMargin: '-25% 0px -62% 0px', threshold: [0.08, 0.25] });
    navLinks.map((link) => document.querySelector(link.hash)).filter(Boolean).forEach((section) => observer.observe(section));
  }

  const tabs = [...document.querySelectorAll('.tab')];
  tabs.forEach((tab) => { tab.setAttribute('aria-selected', String(tab.classList.contains('active'))); tab.addEventListener('click', () => { tabs.forEach((item) => { const active = item === tab; item.classList.toggle('active', active); item.setAttribute('aria-selected', String(active)); }); document.querySelectorAll('.product-card').forEach((card) => card.classList.toggle('is-hidden', tab.dataset.filter !== 'all' && card.dataset.category !== tab.dataset.filter)); }); });

  function appendList(parent, items) { const list = create('ul'); items.forEach((item) => list.append(create('li', '', item))); parent.append(list); }
  function renderModal({ title, code, horizon, question, scope, outputs, limits, icon }) {
    if (!modal || !modalContent) return;
    modalContent.replaceChildren();
    const shell = create('div', 'modal-content-shell');
    const aside = create('aside', 'modal-aside');
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', `#${icon || 'i-compass'}`); svg.append(use);
    aside.append(svg, create('span', '', code || 'MERIDIANO LEGAL'), create('small', '', horizon || 'Alcance por definir'));
    const main = create('div', 'modal-main');
    const eyebrow = create('p', 'eyebrow dark', 'FICHA EJECUTIVA');
    const heading = create('h2', '', title); heading.id = 'modal-title';
    const questionElement = create('p', 'question', question);
    const meta = create('div', 'modal-meta'); ['Supervisión profesional', 'Entregables verificables', 'Límites explícitos'].forEach((item) => meta.append(create('span', '', item)));
    const columns = create('div', 'modal-columns');
    const left = create('div'); left.append(create('h3', '', scope ? 'Alcance principal' : 'Entregables principales')); appendList(left, scope || outputs);
    const right = create('div'); right.append(create('h3', '', scope ? 'Entregables' : 'Límites y exclusiones')); appendList(right, scope ? outputs : limits);
    if (scope) { right.append(create('h3', '', 'Límites y exclusiones')); appendList(right, limits); }
    columns.append(left, right);
    const actions = create('div', 'modal-actions');
    const contact = create('a', 'btn btn-navy', 'Solicitar calificación'); contact.href = '#contacto';
    const demo = create('a', 'btn btn-outline-dark', 'Ver experiencia'); demo.href = 'experiencia.html';
    actions.append(contact, demo); main.append(eyebrow, heading, questionElement, meta, columns, actions); shell.append(aside, main); modalContent.append(shell);
    contact.addEventListener('click', () => modal.close()); modal.showModal();
  }

  document.querySelectorAll('[data-service]').forEach((button) => button.addEventListener('click', () => { const service = services[button.dataset.service]; if (!service) return; lastTrigger = button; renderModal(service); }));
  document.querySelectorAll('[data-product]').forEach((button) => button.addEventListener('click', () => { const product = products[button.dataset.product]; if (!product) return; const service = services[product.service]; lastTrigger = button; renderModal({ title: button.dataset.product, code: 'PRODUCTO DE ALCANCE CERRADO', horizon: product.duration, question: product.question, outputs: product.deliverables, limits: product.limits, icon: service?.icon || 'i-compass' }); }));
  document.querySelectorAll('[data-route]').forEach((card) => card.addEventListener('click', () => { const productName = routeMap[card.dataset.route]; const product = products[productName]; const service = services[product?.service]; if (!product) return; lastTrigger = card; renderModal({ title: productName, code: 'PUNTO DE ENTRADA SUGERIDO', horizon: product.duration, question: product.question, outputs: product.deliverables, limits: product.limits, icon: service?.icon }); }));
  document.querySelector('.modal-close')?.addEventListener('click', () => modal?.close());
  modal?.addEventListener('click', (event) => { if (event.target !== modal) return; const bounds = modal.getBoundingClientRect(); const inside = event.clientX >= bounds.left && event.clientX <= bounds.right && event.clientY >= bounds.top && event.clientY <= bounds.bottom; if (!inside) modal.close(); });
  modal?.addEventListener('close', () => lastTrigger?.focus());

  const form = document.getElementById('contact-form');
  form?.addEventListener('submit', async (event) => {
    event.preventDefault(); if (!form.reportValidity()) return; const data = new FormData(form);
    const summary = ['Hola, quiero presentar una necesidad a Meridiano Legal.', '', `Nombre: ${String(data.get('name') || '').trim()}`, `Empresa: ${String(data.get('company') || '').trim() || 'No indicada'}`, `Correo: ${String(data.get('email') || '').trim()}`, `Necesidad: ${String(data.get('need') || '').trim()}`, '', 'Contexto general:', String(data.get('message') || '').trim(), '', 'Confirmo que no estoy enviando información confidencial.'].join('\n');
    const status = form.querySelector('.form-status'); if (status) status.textContent = 'Solicitud preparada. Se abrirá WhatsApp en una nueva ventana.';
    try { await navigator.clipboard?.writeText(summary); } catch { /* opcional */ }
    const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(summary)}`; const opened = window.open(url, '_blank', 'noopener,noreferrer'); if (!opened) window.location.href = url;
  });

  const year = document.getElementById('year'); if (year) year.textContent = String(new Date().getFullYear());
  const topButton = document.querySelector('.floating-actions button'); const updateTopButton = () => topButton?.classList.toggle('visible', window.scrollY > 700); window.addEventListener('scroll', updateTopButton, { passive: true }); topButton?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' })); updateTopButton();

  const catalogEnhancer = document.createElement('script');
  catalogEnhancer.src = 'catalog-home-v32.js';
  document.body.append(catalogEnhancer);
})();
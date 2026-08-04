const products = {
  'Diagnóstico Jurídico Empresarial': {
    question: '¿Dónde está hoy la mayor exposición jurídica de la empresa?',
    duration: '2 a 4 semanas',
    deliverables: [
      'Informe ejecutivo de situación jurídica',
      'Mapa priorizado de riesgos',
      'Plan jurídico de 90 días',
      'Sesión de dirección y recomendaciones',
    ],
    limits: [
      'No es auditoría legal exhaustiva',
      'No incluye remediaciones no contratadas',
      'Depende de la información entregada',
    ],
  },
  'Empresa Jurídicamente Organizada': {
    question: '¿La empresa puede crecer y decidir sin depender de memoria o acuerdos verbales?',
    duration: '6 a 10 semanas',
    deliverables: [
      'Mapa societario y de poderes',
      'Biblioteca contractual priorizada',
      'Políticas esenciales',
      'Calendario jurídico anual',
    ],
    limits: [
      'No incluye litigios ni saneamientos complejos',
      'Trámites y tasas se dimensionan por separado',
    ],
  },
  'Marca, Software y Activos Intangibles Protegidos': {
    question: '¿La empresa controla jurídicamente los activos que está financiando?',
    duration: '3 a 8 semanas',
    deliverables: [
      'Inventario y cadena de titularidad',
      'Estrategia de protección',
      'Cesiones, licencias o cláusulas prioritarias',
      'Calendario de renovaciones',
    ],
    limits: [
      'No garantiza concesión registral',
      'Litigios y oposiciones requieren alcance separado',
    ],
  },
  'Empresa Lista para Inversión': {
    question: '¿La empresa puede explicar su capital, gobierno, contratos y contingencias?',
    duration: '6 a 12 semanas',
    deliverables: [
      'Informe de preparación',
      'Plan de remediación',
      'Cap table y matriz de gobierno',
      'Índice de data room',
    ],
    limits: [
      'No incluye valoración financiera',
      'Estructuración tributaria requiere especialista',
    ],
  },
  'Programa de Gobernanza de IA': {
    question: '¿La organización sabe dónde usa IA, qué datos intervienen y quién responde?',
    duration: '5 a 10 semanas',
    deliverables: [
      'Inventario de casos de uso',
      'Clasificación de riesgos',
      'Política, roles y controles',
      'Protocolo de proveedores e incidentes',
    ],
    limits: [
      'No es auditoría técnica de modelos',
      'No certifica cumplimiento',
    ],
  },
  'Proyecto Regulado Estructurado': {
    question: '¿El proyecto es jurídicamente viable y qué condiciona su ejecución?',
    duration: '4 a 8 semanas',
    deliverables: [
      'Concepto ejecutivo de viabilidad',
      'Matriz de permisos y condicionantes',
      'Arquitectura contractual',
      'Hoja de ruta con responsables',
    ],
    limits: [
      'No incluye estudios técnicos',
      'No garantiza permisos o financiación',
    ],
  },
  'Sistema Contractual Empresarial': {
    question: '¿La empresa sabe qué firma, quién aprueba y cuándo debe actuar?',
    duration: '6 a 10 semanas',
    deliverables: [
      'Matriz contractual',
      'Playbook de negociación',
      'Biblioteca de modelos',
      'Registro de obligaciones y renovaciones',
    ],
    limits: [
      'Revisión histórica masiva requiere dimensionamiento',
      'Negociaciones extraordinarias se cotizan aparte',
    ],
  },
  'Programa de Protección de Datos y Consumidor': {
    question: '¿La empresa puede demostrar cómo recoge datos y atiende reclamos?',
    duration: '6 a 10 semanas',
    deliverables: [
      'Mapa de datos y canales',
      'Políticas, avisos y procedimientos',
      'Matriz de proveedores',
      'Registro de solicitudes e incidentes',
    ],
    limits: [
      'No incluye ciberseguridad técnica',
      'Investigaciones y litigios se atienden por separado',
    ],
  },
};

const routeMap = {
  empresa: 'Diagnóstico Jurídico Empresarial',
  ia: 'Programa de Gobernanza de IA',
  socios: 'Empresa Lista para Inversión',
  intangibles: 'Marca, Software y Activos Intangibles Protegidos',
  regulado: 'Proyecto Regulado Estructurado',
  operacion: 'Sistema Contractual Empresarial',
};

const WHATSAPP_NUMBER = '573008507813';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.main-nav');
const productModal = document.getElementById('product-modal');
const modalContent = document.getElementById('modal-content');
let lastModalTrigger = null;

function setMenu(open) {
  if (!menuButton || !navigation) return;
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('open', open);
}

menuButton?.addEventListener('click', () => {
  const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
  setMenu(!isOpen);
});

navigation?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => setMenu(false));
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') setMenu(false);
});

document.addEventListener('click', (event) => {
  if (!navigation?.classList.contains('open')) return;
  if (navigation.contains(event.target) || menuButton?.contains(event.target)) return;
  setMenu(false);
});

const tabs = [...document.querySelectorAll('.tab')];
tabs.forEach((tab) => {
  tab.setAttribute('role', 'tab');
  tab.setAttribute('aria-selected', String(tab.classList.contains('active')));
  tab.addEventListener('click', () => {
    tabs.forEach((item) => {
      const isActive = item === tab;
      item.classList.toggle('active', isActive);
      item.setAttribute('aria-selected', String(isActive));
    });

    const filter = tab.dataset.filter;
    document.querySelectorAll('.product-card').forEach((card) => {
      card.classList.toggle(
        'is-hidden',
        filter !== 'all' && card.dataset.category !== filter,
      );
    });
  });
});

function renderProduct(productName) {
  const product = products[productName];
  if (!product || !productModal || !modalContent) return;

  modalContent.innerHTML = `
    <p class="eyebrow dark">FICHA EJECUTIVA</p>
    <h2>${productName}</h2>
    <p><strong>${product.question}</strong></p>
    <div class="meta">
      <span>${product.duration}</span>
      <span>Supervisión profesional</span>
      <span>Alcance definido</span>
    </div>
    <h3>Entregables principales</h3>
    <ul>${product.deliverables.map((item) => `<li>${item}</li>`).join('')}</ul>
    <h3>Límites</h3>
    <ul>${product.limits.map((item) => `<li>${item}</li>`).join('')}</ul>
    <a class="btn btn-dark" href="#contacto" data-close-modal>Solicitar propuesta</a>
  `;

  modalContent.querySelector('[data-close-modal]')?.addEventListener('click', () => {
    productModal.close();
  });

  productModal.showModal();
}

document.querySelectorAll('[data-product]').forEach((button) => {
  button.addEventListener('click', () => {
    lastModalTrigger = button;
    renderProduct(button.dataset.product);
  });
});

document.querySelectorAll('.modal-close').forEach((button) => {
  button.addEventListener('click', () => button.closest('dialog')?.close());
});

productModal?.addEventListener('click', (event) => {
  if (event.target !== productModal) return;
  const bounds = productModal.getBoundingClientRect();
  const inside =
    event.clientX >= bounds.left &&
    event.clientX <= bounds.right &&
    event.clientY >= bounds.top &&
    event.clientY <= bounds.bottom;
  if (!inside) productModal.close();
});

productModal?.addEventListener('close', () => {
  lastModalTrigger?.focus();
});

document.querySelectorAll('.need-card').forEach((card) => {
  card.addEventListener('click', () => {
    const productName = routeMap[card.dataset.route];
    const trigger = document.querySelector(`[data-product="${productName}"]`);
    lastModalTrigger = card;
    if (trigger) renderProduct(productName);
  });
});

const contactEmail = document.querySelector('a[href="mailto:contacto@meridianolegal.co"]');
contactEmail?.remove();

const contactPhone = document.querySelector('a[href="tel:+573008507813"]');
if (contactPhone) {
  contactPhone.href = `https://wa.me/${WHATSAPP_NUMBER}`;
  contactPhone.target = '_blank';
  contactPhone.rel = 'noopener noreferrer';
  contactPhone.textContent = 'WhatsApp: +57 300 850 7813';
}

const contactForm = document.getElementById('contact-form');
contactForm?.addEventListener('submit', async (event) => {
  event.preventDefault();

  const data = new FormData(contactForm);
  const summary = [
    'Hola, quiero presentar una necesidad a Meridiano Legal.',
    '',
    `Nombre: ${data.get('name')}`,
    `Empresa: ${data.get('company') || 'No indicada'}`,
    `Correo: ${data.get('email')}`,
    `Necesidad: ${data.get('need')}`,
    '',
    'Contexto general:',
    String(data.get('message')).trim(),
  ].join('\n');

  const status = contactForm.querySelector('.form-status');
  if (status) status.textContent = 'Solicitud preparada. Se abrirá WhatsApp en una nueva ventana.';

  try {
    await navigator.clipboard?.writeText(summary);
  } catch {
    // El portapapeles es opcional; la apertura de WhatsApp continúa.
  }

  const whatsappUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(summary)}`;
  const newWindow = window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
  if (!newWindow) window.location.href = whatsappUrl;
});

const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());

const versionLabel = [...document.querySelectorAll('.footer-bottom span')]
  .find((element) => element.textContent.includes('Versión web GitHub Pages'));
if (versionLabel) versionLabel.textContent = 'Versión web GitHub Pages · v2.29.0';

if (!document.querySelector('script[src="enhancements.js"]')) {
  const enhancements = document.createElement('script');
  enhancements.src = 'enhancements.js';
  enhancements.defer = true;
  document.body.append(enhancements);
}

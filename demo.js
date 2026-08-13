const users = {
  'cliente@empresa-demo.com': {
    password: 'Cliente2026!',
    name: 'Laura Gómez',
    role: 'Cliente demo',
    initials: 'LG',
    actionLabel: 'Nueva solicitud',
  },
  'abogado@meridianolegal.local': {
    password: 'Abogado2026!',
    name: 'Mariana Torres',
    role: 'Abogada responsable',
    initials: 'MT',
    actionLabel: 'Registrar solicitud',
  },
  'admin@meridianolegal.local': {
    password: 'Meridiano2026!',
    name: 'Agustín Rendón',
    role: 'Socio director',
    initials: 'AR',
    actionLabel: 'Nueva instrucción',
  },
};

const titles = {
  dashboard: 'Resumen',
  tickets: 'Solicitudes',
  expedientes: 'Expedientes',
  documentos: 'Documentos guiados',
  archivos: 'Archivos',
  obligaciones: 'Obligaciones',
  calendario: 'Calendario',
  riesgos: 'Riesgos',
  analitica: 'Analítica',
};

const statusLabels = {
  abierto: 'ABIERTO',
  revision: 'EN REVISIÓN',
  espera: 'EN ESPERA',
  cerrado: 'CERRADO',
};

const loginView = document.getElementById('login-view');
const portalView = document.getElementById('portal-view');
const loginForm = document.getElementById('login-form');
const ticketModal = document.getElementById('ticket-modal');
const ticketForm = document.getElementById('ticket-form');

const tickets = [
  { id: 'TK-028', subject: 'Revisión contrato de distribución', area: 'Contratos', owner: 'Mariana T.', status: 'revision', date: '04 ago' },
  { id: 'TK-027', subject: 'Registro de marca nueva línea', area: 'Propiedad intelectual', owner: 'Equipo PI', status: 'abierto', date: '03 ago' },
  { id: 'TK-026', subject: 'Acta de aprobación presupuesto', area: 'Societario', owner: 'Mariana T.', status: 'espera', date: '01 ago' },
  { id: 'TK-025', subject: 'Matriz de permisos proyecto norte', area: 'Regulatorio', owner: 'Carlos R.', status: 'revision', date: '30 jul' },
  { id: 'TK-024', subject: 'Respuesta a solicitud de datos', area: 'Datos', owner: 'Mariana T.', status: 'cerrado', date: '28 jul' },
  { id: 'TK-023', subject: 'Actualización acuerdo de socios', area: 'Societario', owner: 'Agustín R.', status: 'abierto', date: '26 jul' },
];

function escapeHtml(value) {
  return String(value).replace(/[&<>'"]/g, (character) => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    "'": '&#39;',
    '"': '&quot;',
  })[character]);
}

function setSession(email) {
  try {
    sessionStorage.setItem('meridiano-demo-user', email);
  } catch {
    // La demo puede seguir funcionando aunque el navegador bloquee almacenamiento.
  }
}

function getSession() {
  try {
    return sessionStorage.getItem('meridiano-demo-user');
  } catch {
    return null;
  }
}

function clearSession() {
  try {
    sessionStorage.removeItem('meridiano-demo-user');
  } catch {
    // No requiere acción adicional.
  }
}

function openPanel(view) {
  const button = document.querySelector(`.portal-nav[data-view="${view}"]`);
  if (!button || !titles[view]) return;

  document.querySelectorAll('.portal-nav').forEach((item) => {
    const active = item === button;
    item.classList.toggle('active', active);
    item.setAttribute('aria-current', active ? 'page' : 'false');
  });

  document.querySelectorAll('.portal-panel').forEach((panel) => {
    panel.classList.toggle('active', panel.dataset.panel === view);
  });

  document.getElementById('view-title').textContent = titles[view];
  history.replaceState(null, '', `#${view}`);
}

function enterPortal(email) {
  const user = users[email];
  if (!user) return;

  setSession(email);
  document.getElementById('user-name').textContent = user.name;
  document.getElementById('user-role').textContent = user.role;
  document.getElementById('avatar').textContent = user.initials;
  document.getElementById('new-ticket').textContent = user.actionLabel;

  loginView.classList.add('hidden');
  portalView.classList.remove('hidden');

  const requestedView = location.hash.slice(1);
  openPanel(titles[requestedView] ? requestedView : 'dashboard');
}

document.querySelectorAll('.credential-card').forEach((card) => {
  card.addEventListener('click', () => {
    document.getElementById('login-email').value = card.dataset.email;
    document.getElementById('login-password').value = card.dataset.password;
    document.getElementById('login-email').focus();
  });
});

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const email = document.getElementById('login-email').value.trim().toLowerCase();
  const password = document.getElementById('login-password').value;
  const status = document.getElementById('login-status');

  if (users[email]?.password === password) {
    status.textContent = '';
    enterPortal(email);
    return;
  }

  status.textContent = 'Credenciales incorrectas. Use uno de los perfiles demostrativos.';
});

document.getElementById('logout').addEventListener('click', () => {
  clearSession();
  location.href = 'demo.html';
});

document.querySelectorAll('.portal-nav').forEach((button) => {
  button.addEventListener('click', () => openPanel(button.dataset.view));
});

window.addEventListener('hashchange', () => {
  if (portalView.classList.contains('hidden')) return;
  const requestedView = location.hash.slice(1);
  if (titles[requestedView]) openPanel(requestedView);
});

function renderTickets() {
  const query = document.getElementById('ticket-search').value.trim().toLowerCase();
  const filter = document.getElementById('ticket-filter').value;
  const visibleTickets = tickets.filter((ticket) => {
    const matchesStatus = filter === 'all' || ticket.status === filter;
    const searchable = Object.values(ticket).join(' ').toLowerCase();
    return matchesStatus && searchable.includes(query);
  });

  const rows = visibleTickets.map((ticket) => `
    <tr>
      <td><strong>${escapeHtml(ticket.id)}</strong></td>
      <td>${escapeHtml(ticket.subject)}</td>
      <td>${escapeHtml(ticket.area)}</td>
      <td>${escapeHtml(ticket.owner)}</td>
      <td><span class="status-pill ${ticket.status}">${statusLabels[ticket.status]}</span></td>
      <td>${escapeHtml(ticket.date)}</td>
    </tr>
  `).join('');

  document.getElementById('ticket-rows').innerHTML = rows || `
    <tr><td colspan="6">No hay solicitudes que coincidan con la búsqueda.</td></tr>
  `;
}

document.getElementById('ticket-search').addEventListener('input', renderTickets);
document.getElementById('ticket-filter').addEventListener('change', renderTickets);
renderTickets();

function renderCalendar() {
  const events = {
    4: 'Comité jurídico',
    12: 'Hito regulatorio',
    19: 'Renovación',
    27: 'Cierre mensual',
  };

  const cells = [];
  for (let day = 28; day <= 31; day += 1) {
    cells.push(`<div class="day muted">${day}</div>`);
  }
  for (let day = 1; day <= 31; day += 1) {
    const event = events[day];
    cells.push(`<div class="day ${event ? 'has-event' : ''}">${day}${event ? `<i>${event}</i>` : ''}</div>`);
  }
  for (let day = 1; day <= 3; day += 1) {
    cells.push(`<div class="day muted">${day}</div>`);
  }

  document.getElementById('calendar-days').innerHTML = cells.join('');
}
renderCalendar();

document.querySelectorAll('.doc-template').forEach((button) => {
  button.addEventListener('click', () => {
    document.querySelectorAll('.doc-template').forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
    document.getElementById('doc-title').textContent = button.dataset.doc;
    document.getElementById('doc-preview').classList.add('hidden');
  });
});

document.getElementById('generate-doc').addEventListener('click', () => {
  const title = document.getElementById('doc-title').textContent;
  const party = document.getElementById('doc-party').value || '[PARTE PRINCIPAL]';
  const counterparty = document.getElementById('doc-counterparty').value || '[CONTRAPARTE]';
  const object = document.getElementById('doc-object').value || '[OBJETO POR DEFINIR]';
  const preview = document.getElementById('doc-preview');

  preview.innerHTML = `
    <p class="eyebrow dark">VISTA PREVIA FICTICIA</p>
    <h3>${escapeHtml(title)}</h3>
    <p>Entre <strong>${escapeHtml(party)}</strong> y <strong>${escapeHtml(counterparty)}</strong>, se estructura el presente instrumento respecto de: ${escapeHtml(object)}.</p>
    <p>La versión final requeriría validación de capacidad, antecedentes, riesgos, anexos, obligaciones, responsabilidad, vigencia, terminación y demás condiciones aplicables.</p>
    <small>Esta vista previa no constituye documento jurídico ni puede utilizarse para firma.</small>
  `;
  preview.classList.remove('hidden');
});

function closeDialogOnBackdrop(dialog) {
  dialog?.addEventListener('click', (event) => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    const inside =
      event.clientX >= bounds.left &&
      event.clientX <= bounds.right &&
      event.clientY >= bounds.top &&
      event.clientY <= bounds.bottom;
    if (!inside) dialog.close();
  });
}

closeDialogOnBackdrop(ticketModal);

document.getElementById('new-ticket').addEventListener('click', () => {
  ticketForm.querySelector('.form-status').textContent = '';
  ticketModal.showModal();
});

document.querySelectorAll('.modal-close').forEach((button) => {
  button.addEventListener('click', () => button.closest('dialog')?.close());
});

ticketForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const data = new FormData(ticketForm);
  const nextNumber = Math.max(...tickets.map((ticket) => Number(ticket.id.split('-')[1]))) + 1;

  tickets.unshift({
    id: `TK-${String(nextNumber).padStart(3, '0')}`,
    subject: String(data.get('subject')).trim(),
    area: String(data.get('area')).trim(),
    owner: 'Por asignar',
    status: 'abierto',
    date: 'hoy',
  });

  renderTickets();
  ticketForm.querySelector('.form-status').textContent = 'Solicitud ficticia creada en esta sesión.';
  ticketForm.reset();

  setTimeout(() => {
    ticketModal.close();
    openPanel('tickets');
  }, 700);
});

document.querySelector('.portal-panel[data-panel="archivos"] .btn')?.addEventListener('click', (event) => {
  event.currentTarget.textContent = 'Carga deshabilitada en demo';
  event.currentTarget.disabled = true;
});

const savedUser = getSession();
if (savedUser && users[savedUser]) enterPortal(savedUser);

(() => {
  const panels = [...document.querySelectorAll('[data-panel]')];
  const tabs = [...document.querySelectorAll('[data-target]')];

  function openPanel(id, updateHash = true) {
    const panel = panels.find((item) => item.dataset.panel === id);
    if (!panel) return;

    panels.forEach((item) => {
      const active = item === panel;
      item.classList.toggle('active', active);
      item.hidden = !active;
    });

    tabs.forEach((tab) => {
      const active = tab.dataset.target === id;
      tab.classList.toggle('active', active);
      tab.setAttribute('aria-pressed', String(active));
    });

    if (updateHash) history.replaceState(null, '', `#${id}`);
    panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  tabs.forEach((tab) => {
    tab.setAttribute('aria-pressed', String(tab.classList.contains('active')));
    tab.addEventListener('click', () => openPanel(tab.dataset.target));
  });

  const initialPanel = location.hash.slice(1);
  if (panels.some((panel) => panel.dataset.panel === initialPanel)) {
    openPanel(initialPanel, false);
  }

  const tours = {
    10: [
      ['01', 'Contexto', 'Qué es Meridiano Legal y qué problema empresarial resuelve.', '2 minutos'],
      ['02', 'Portafolio', 'Cómo se separan servicios, productos, planes y documentos guiados.', '2 minutos'],
      ['03', 'Método', 'Comprender, priorizar, ejecutar y dar seguimiento.', '2 minutos'],
      ['04', 'Evidencia', 'Ejemplos de mapas, matrices, contratos, políticas y tableros.', '2 minutos'],
      ['05', 'Siguiente paso', 'Calificación inicial, propuesta, aceptación e inicio.', '2 minutos'],
    ],
    20: [
      ['01', 'Contexto', 'Necesidad empresarial, principios de servicio y sectores priorizados.', '3 minutos'],
      ['02', 'Arquitectura', 'Servicios, productos, planes recurrentes y documentos guiados.', '4 minutos'],
      ['03', 'Caso integral', 'Escenario ficticio desde diagnóstico hasta implementación.', '4 minutos'],
      ['04', 'Simulador', 'Construcción privada de una hipótesis de alcance.', '3 minutos'],
      ['05', 'Meridiano Empresas', 'Solicitudes, expedientes, obligaciones, riesgos y analítica.', '4 minutos'],
      ['06', 'Contratación', 'Alcance, exclusiones, cronograma, honorarios, aceptación e inicio.', '2 minutos'],
    ],
  };

  const timeline = document.getElementById('tour-timeline');
  const tourButtons = [...document.querySelectorAll('[data-tour]')];

  function renderTour(duration) {
    if (!timeline || !tours[duration]) return;
    timeline.replaceChildren();
    tours[duration].forEach(([number, title, description, time]) => {
      const item = document.createElement('li');
      const numberElement = document.createElement('span');
      const titleElement = document.createElement('h3');
      const descriptionElement = document.createElement('p');
      const timeElement = document.createElement('small');
      numberElement.textContent = number;
      titleElement.textContent = title;
      descriptionElement.textContent = description;
      timeElement.textContent = time;
      item.append(numberElement, titleElement, descriptionElement, timeElement);
      timeline.append(item);
    });
  }

  tourButtons.forEach((button) => {
    button.addEventListener('click', () => {
      tourButtons.forEach((item) => item.classList.toggle('active', item === button));
      renderTour(button.dataset.tour);
    });
  });
  renderTour('10');

  const recommendations = {
    empresa: {
      entry: 'Diagnóstico Jurídico Empresarial o Empresa Jurídicamente Organizada',
      information: ['Estructura societaria y responsables', 'Contratos y políticas prioritarias', 'Pendientes, decisiones y proyectos próximos'],
    },
    contratos: {
      entry: 'Contratos y Negociaciones o Sistema Contractual Empresarial',
      information: ['Operación y resultado comercial esperado', 'Borradores, anexos y posiciones pendientes', 'Responsables, fechas y niveles de aprobación'],
    },
    socios: {
      entry: 'Sociedades, Socios e Inversión o Empresa Lista para Inversión',
      information: ['Cap table, estatutos y acuerdos existentes', 'Decisión, transacción o conflicto que activa la necesidad', 'Derechos, aprobaciones y fechas relevantes'],
    },
    intangibles: {
      entry: 'Marca, Software y Activos Intangibles Protegidos',
      information: ['Inventario de activos y autores', 'Contratos, cesiones, licencias y registros', 'Mercados, usos y modelo de explotación'],
    },
    ia: {
      entry: 'Programa de Gobernanza de IA',
      information: ['Casos de uso y procesos impactados', 'Datos, proveedores y decisiones automatizadas', 'Responsables, supervisión e incidentes conocidos'],
    },
    regulado: {
      entry: 'Proyecto Regulado Estructurado',
      information: ['Descripción técnica y modelo de operación', 'Territorio, actores y autoridades relacionadas', 'Permisos, contratos, hitos y restricciones'],
    },
    operacion: {
      entry: 'Organización de la Operación Jurídica o Banco Documental y Legal Operations',
      information: ['Tipos y volumen de solicitudes', 'Documentos, canales, responsables y aprobadores', 'Vencimientos, indicadores y herramientas actuales'],
    },
  };

  const modalityByRecurrence = {
    focal: ['Orientación focal', 'Sesión o alcance breve', 'Definir el siguiente paso y el perímetro de análisis.'],
    multiple: ['Diagnóstico', '2 a 4 semanas', 'Priorizar varios frentes y producir una ruta ejecutiva.'],
    project: ['Proyecto jurídico', '4 a 12 semanas', 'Lograr un resultado definido mediante entregables e implementación.'],
    continuous: ['Dirección externa o plan recurrente', 'Cadencia mensual o trimestral', 'Mantener capacidad, gobierno, memoria y seguimiento.'],
  };

  const simulator = document.getElementById('scope-simulator');
  const result = document.getElementById('simulator-result');

  function urgencyNote(value) {
    if (value === 'inmediata') return 'La fecha o exposición inmediata exige confirmar disponibilidad, medidas de contención y responsables desde la primera conversación.';
    if (value === 'proxima') return 'Conviene definir evidencia mínima, decisiones y cronograma antes de comprometer a terceros o recursos.';
    return 'El momento preventivo permite priorizar, organizar evidencia y reducir costos de corrección posterior.';
  }

  function evidenceNote(value) {
    if (value === 'incierta') return 'Debe reservarse una fase inicial de inventario y validación de información.';
    if (value === 'parcial') return 'El alcance debe identificar expresamente vacíos, supuestos y responsables de completar evidencia.';
    return 'La información organizada puede reducir tiempos de diagnóstico, sin eliminar la necesidad de validación.';
  }

  function createResult(data) {
    const recommendation = recommendations[data.need];
    const [modality, duration, purpose] = modalityByRecurrence[data.recurrence];
    if (!recommendation || !modality) return;

    result.replaceChildren();
    const eyebrow = document.createElement('p');
    eyebrow.className = 'eyebrow';
    eyebrow.textContent = 'HIPÓTESIS ORIENTATIVA';
    const title = document.createElement('h3');
    title.textContent = modality;
    const intro = document.createElement('p');
    intro.textContent = purpose;
    const details = document.createElement('dl');
    [
      ['Punto de entrada', recommendation.entry],
      ['Horizonte', duration],
      ['Sector', data.sector],
      ['Momento', urgencyNote(data.urgency)],
      ['Evidencia', evidenceNote(data.evidence)],
    ].forEach(([term, value]) => {
      const dt = document.createElement('dt');
      const dd = document.createElement('dd');
      dt.textContent = term;
      dd.textContent = value;
      details.append(dt, dd);
    });
    const subtitle = document.createElement('h4');
    subtitle.textContent = 'Información mínima para una primera conversación';
    const list = document.createElement('ul');
    recommendation.information.forEach((item) => {
      const li = document.createElement('li');
      li.textContent = item;
      list.append(li);
    });
    const note = document.createElement('p');
    note.className = 'experience-disclaimer';
    note.textContent = 'Resultado demostrativo: no fija honorarios, duración definitiva ni viabilidad. El alcance final requiere revisión de hechos, conflictos, evidencia, capacidad y especialidades aplicables.';
    const actions = document.createElement('div');
    actions.className = 'result-actions';
    const contact = document.createElement('a');
    contact.className = 'btn btn-gold';
    contact.href = `https://wa.me/573008507813?text=${encodeURIComponent(`Hola, revisé el simulador de Meridiano Legal. La hipótesis sugerida fue: ${modality}. Necesidad: ${recommendation.entry}. Sector: ${data.sector}.`)}`;
    contact.target = '_blank';
    contact.rel = 'noopener noreferrer';
    contact.textContent = 'Conversar sobre esta hipótesis';
    const portal = document.createElement('a');
    portal.className = 'btn btn-outline-light';
    portal.href = 'demo.html';
    portal.textContent = 'Ver Meridiano Empresas';
    actions.append(contact, portal);
    result.append(eyebrow, title, intro, details, subtitle, list, note, actions);
  }

  simulator?.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(simulator));
    createResult(data);
  });

  simulator?.addEventListener('reset', () => {
    window.setTimeout(() => {
      result.innerHTML = '<p class="eyebrow dark">RESULTADO ORIENTATIVO</p><h3>Complete las cinco variables.</h3><p>El simulador sugerirá una modalidad, un punto de entrada y la información mínima para una primera conversación.</p>';
    }, 0);
  });
})();

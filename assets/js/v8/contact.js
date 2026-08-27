(() => {
  const form = document.querySelector('[data-v8-contact-form="true"]');
  if (!form) return;

  const status = form.querySelector('[data-v8-contact-status]');
  const panel = form.querySelector('[data-v8-handoff]');
  const panelCopy = form.querySelector('[data-v8-handoff-copy]');
  const reopen = form.querySelector('[data-v8-handoff-reopen]');
  const copy = form.querySelector('[data-v8-handoff-copy-button]');
  const WHATSAPP = '573008507813';
  let draft = null;

  const clean = (value, max = 240) => String(value || '').trim().replace(/\s+/g, ' ').slice(0, max);
  const value = (name, max = 240) => clean(form.elements.namedItem(name)?.value || '', max);
  const label = (name, fallback = 'No definido') => {
    const field = form.elements.namedItem(name);
    if (!field || !field.value) return fallback;
    return clean(field.selectedOptions?.[0]?.textContent || field.value, 160);
  };
  const setStatus = (message, state = '') => {
    if (!status) return;
    status.textContent = message;
    status.dataset.state = state;
  };
  const setDraftActions = (disabled) => {
    if (reopen) reopen.disabled = disabled;
    if (copy) copy.disabled = disabled;
  };
  const emit = (action) => window.dispatchEvent(new CustomEvent('meridiano:v8-handoff', {
    detail: Object.freeze({ stage: action === 'prepared' ? 'handoff' : 'contact', action }),
  }));

  const compose = () => [
    'Hola, Meridiano Legal. Quiero presentar una necesidad jurídica.',
    '',
    `Nombre: ${value('name', 120)}`,
    `Empresa: ${value('company', 160) || 'No indicada'}`,
    `Correo: ${value('email', 180)}`,
    `Necesidad: ${label('need')}`,
    `Momento de decisión: ${label('decision_stage')}`,
    `Urgencia: ${label('urgency')}`,
    `Presupuesto orientativo: ${label('budget', 'Por definir')}`,
    `Contexto: ${value('message', 1600) || 'No indicado'}`,
    '',
    'Entiendo que este mensaje inicia una conversación y no confirma aceptación del encargo ni crea automáticamente una relación profesional.',
  ].join('\n');

  const openDraft = () => {
    if (!draft || draft.stale) return;
    const opened = window.open(draft.url, '_blank', 'noopener,noreferrer');
    if (!opened) window.location.assign(draft.url);
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.checkValidity()) {
      form.reportValidity();
      setStatus('Revise los campos obligatorios antes de preparar la solicitud.', 'invalid');
      return;
    }
    if (value('website', 120)) {
      setStatus('Solicitud recibida para revisión.', 'bot');
      return;
    }
    const summary = compose();
    draft = {
      summary,
      url: `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(summary)}`,
      stale: false,
    };
    if (panel) panel.hidden = false;
    if (panelCopy) panelCopy.textContent = 'WhatsApp se abrió con un resumen preparado. Esta web no puede confirmar si el mensaje fue enviado, entregado o leído.';
    setDraftActions(false);
    setStatus('Solicitud preparada. Revise el texto y confirme el envío directamente en WhatsApp.', 'prepared');
    emit('prepared');
    openDraft();
  });

  const markStale = (event) => {
    if (!draft || draft.stale || event.target.closest('[data-v8-handoff]')) return;
    draft.stale = true;
    setDraftActions(true);
    if (panelCopy) panelCopy.textContent = 'La información cambió después de preparar el mensaje. Vuelva a abrir la solicitud desde el botón principal para generar un resumen actualizado.';
    setStatus('La solicitud preparada quedó desactualizada por cambios en el formulario.', 'stale');
    emit('stale');
  };
  form.addEventListener('input', markStale);
  form.addEventListener('change', markStale);

  reopen?.addEventListener('click', () => {
    if (!draft || draft.stale) return;
    emit('reopen');
    openDraft();
  });

  copy?.addEventListener('click', async () => {
    if (!draft || draft.stale) return;
    try {
      await navigator.clipboard.writeText(draft.summary);
      setStatus('Resumen copiado por su solicitud. La página no lo conserva en almacenamiento persistente.', 'copied');
      emit('copy');
    } catch {
      setStatus('El navegador no permitió copiar automáticamente. El resumen sigue disponible en la ventana de WhatsApp.', 'copy-failed');
      emit('copy-failed');
    }
  });

  window.MeridianoV8Contact = Object.freeze({
    version: '8.0.0-candidate',
    manualSend: true,
    persistentStorage: false,
    networkTransport: false,
    staleDraftProtection: true,
    piiInMeasurement: false,
  });
})();

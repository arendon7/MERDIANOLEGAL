(() => {
  const form = document.getElementById('contact-form');
  const panel = form?.querySelector('[data-handoff-v517="true"]');
  if (!form || !panel) return;

  const referenceNode = panel.querySelector('[data-handoff-reference-v517]');
  const liveNode = panel.querySelector('[data-handoff-live-v517]');
  const reopenButton = panel.querySelector('[data-handoff-reopen-v517]');
  const copyButton = panel.querySelector('[data-handoff-copy-v517]');
  const editButton = panel.querySelector('[data-handoff-edit-v517]');
  let draft = null;

  const clean = (value, max = 240) => String(value || '').trim().replace(/\s+/g, ' ').slice(0, max);
  const setLive = (message) => { if (liveNode) liveNode.textContent = message; };
  const usableDraft = () => draft && panel.dataset.handoffState === 'prepared';
  const setButtonsDisabled = (disabled) => {
    if (reopenButton) reopenButton.disabled = disabled;
    if (copyButton) copyButton.disabled = disabled;
  };

  const renderPrepared = ({ reference, summary, url }) => {
    const safeReference = clean(reference, 40);
    const safeUrl = String(url || '');
    if (!safeReference || !summary || !/^https:\/\/wa\.me\/573008507813\?text=/.test(safeUrl)) return;
    draft = Object.freeze({ reference: safeReference, summary: String(summary), url: safeUrl });
    if (referenceNode) referenceNode.textContent = safeReference;
    panel.hidden = false;
    panel.dataset.handoffState = 'prepared';
    setButtonsDisabled(false);
    setLive('WhatsApp se abrió con el mensaje preparado. Esta web no puede confirmar si usted lo envió; revise el texto y pulse Enviar allí.');
  };

  const markChanged = () => {
    if (!draft || panel.hidden || panel.dataset.handoffState === 'changed') return;
    panel.dataset.handoffState = 'changed';
    setButtonsDisabled(true);
    setLive('La solicitud cambió después de preparar el handoff. Vuelva a pulsar “Abrir solicitud en WhatsApp” para generar un resumen coherente con los datos actuales.');
  };

  window.addEventListener('meridiano:handoff-draft-v517', (event) => {
    renderPrepared(event.detail || {});
  });

  form.addEventListener('input', (event) => {
    if (event.target.closest('[data-handoff-v517="true"]')) return;
    markChanged();
  });
  form.addEventListener('change', (event) => {
    if (event.target.closest('[data-handoff-v517="true"]')) return;
    markChanged();
  });

  reopenButton?.addEventListener('click', () => {
    if (!usableDraft()) return;
    const opened = window.open(draft.url, '_blank', 'noopener,noreferrer');
    if (!opened) window.location.assign(draft.url);
    setLive('WhatsApp se abrió de nuevo con el último resumen preparado. El envío sigue requiriendo su confirmación allí.');
  });

  copyButton?.addEventListener('click', async () => {
    if (!usableDraft()) return;
    try {
      await navigator.clipboard.writeText(draft.summary);
      setLive('Resumen copiado al portapapeles por su solicitud. Esta página no lo conserva en almacenamiento persistente.');
    } catch {
      setLive('El navegador no permitió copiar automáticamente. El mensaje continúa disponible en la ventana de WhatsApp abierta.');
    }
  });

  editButton?.addEventListener('click', () => {
    const target = form.querySelector('textarea[name="message"]') || form.querySelector('input,select,textarea');
    target?.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
    window.setTimeout(() => target?.focus({ preventScroll: true }), 0);
  });

  window.addEventListener('focus', () => {
    if (!usableDraft()) return;
    setLive('Si ya envió el mensaje, la conversación continúa en WhatsApp. Esta web estática no recibe confirmación de entrega, lectura, aceptación ni inicio del encargo.');
  });

  window.MeridianoHandoffV517 = Object.freeze({
    version: '5.17.0',
    manualSend: true,
    automaticClipboard: false,
    staleDraftProtection: true,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false, piiInDomSummary: false }),
  });
})();

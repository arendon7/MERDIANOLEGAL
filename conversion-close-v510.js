(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const decisionStage = form.querySelector('[name="decision_stage"]');
  const need = form.querySelector('[name="need"]');
  const submit = form.querySelector('button[type="submit"]');
  const panel = form.querySelector('[data-close-path-v510="true"]');
  const routeNode = form.querySelector('[data-close-route-v510]');
  const gateTitle = form.querySelector('[data-close-gate-title-v510]');
  const gateCopy = form.querySelector('[data-close-gate-copy-v510]');
  const steps = [...form.querySelectorAll('[data-close-step-v510]')];

  const clean = (value, max = 80) => String(value || '').trim().replace(/\s+/g, ' ').slice(0, max);
  const params = new URL(window.location.href).searchParams;
  const requestedIntent = clean(params.get('commercial_intent'), 24);

  const ROUTES = Object.freeze({
    proposal: Object.freeze({
      label: 'Ruta de propuesta',
      stage: 'Quiero recibir una propuesta',
      cta: 'Preparar solicitud de propuesta en WhatsApp',
      gateTitle: 'Antes de emitir una propuesta',
      gateCopy: 'Meridiano debe confirmar encaje, disponibilidad, posibles conflictos, perímetro, entregables, cronograma y la información mínima necesaria. La intención de contratar acelera la conversación, pero no sustituye esas verificaciones.',
      currentStep: 'fit',
    }),
    scope: Object.freeze({
      label: 'Ruta de alcance',
      stage: 'Necesito definir mejor el alcance',
      cta: 'Preparar llamada de alcance en WhatsApp',
      gateTitle: 'Objetivo de la primera conversación',
      gateCopy: 'Delimitar resultado, perímetro, actores, dependencias, información mínima y modalidad de trabajo antes de cotizar. Después de esa definición puede estructurarse una propuesta comparable y verificable.',
      currentStep: 'fit',
    }),
    orientation: Object.freeze({
      label: 'Ruta de orientación',
      stage: 'Estoy explorando la necesidad',
      cta: 'Preparar orientación inicial en WhatsApp',
      gateTitle: 'Objetivo de este punto de entrada',
      gateCopy: 'Comprender la decisión y determinar si conviene orientación focal, diagnóstico, servicio especializado, producto cerrado, proyecto o plan recurrente. No se fuerza una propuesta antes de entender el problema.',
      currentStep: 'request',
    }),
  });

  const routeForStage = (stage) => {
    if (stage === 'Quiero recibir una propuesta' || stage === 'Estoy comparando alternativas') return 'proposal';
    if (stage === 'Necesito definir mejor el alcance') return 'scope';
    return 'orientation';
  };

  const safeNeed = () => clean(need?.value || '', 80);
  const track = (name, detail = {}) => {
    if (!window.MeridianoTelemetry || typeof window.MeridianoTelemetry.track !== 'function') return;
    window.MeridianoTelemetry.track(name, {
      stage: clean(detail.stage, 48),
      target: clean(detail.target, 80),
      need: clean(detail.need ?? safeNeed(), 80),
    });
  };

  let lastTrackedRoute = '';
  const render = () => {
    const routeCode = routeForStage(decisionStage?.value || '');
    const route = ROUTES[routeCode];
    form.dataset.closeRouteV510 = routeCode;
    if (panel) panel.dataset.closeRoute = routeCode;
    if (routeNode) routeNode.textContent = route.label;
    if (gateTitle) gateTitle.textContent = route.gateTitle;
    if (gateCopy) gateCopy.textContent = route.gateCopy;
    if (submit) submit.textContent = route.cta;

    const order = ['request', 'fit', 'proposal', 'start'];
    const currentIndex = order.indexOf(route.currentStep);
    steps.forEach((step) => {
      const index = order.indexOf(step.dataset.closeStepV510 || '');
      step.dataset.state = index < currentIndex ? 'done' : index === currentIndex ? 'current' : 'next';
    });

    if (lastTrackedRoute !== routeCode) {
      lastTrackedRoute = routeCode;
      track('close_route_view', { stage: routeCode, target: 'contact-close-path' });
    }
  };

  const applyRequestedIntent = () => {
    const route = ROUTES[requestedIntent];
    if (!route || !decisionStage || decisionStage.value) return;
    const option = [...decisionStage.options].find((item) => item.value === route.stage || item.textContent.trim() === route.stage);
    if (!option) return;
    decisionStage.value = option.value;
    form.dataset.closeIntentV510 = requestedIntent;
    decisionStage.dispatchEvent(new Event('change', { bubbles: true }));
    track('close_intent_applied', { stage: requestedIntent, target: 'contact-form' });
  };

  decisionStage?.addEventListener('change', render);
  need?.addEventListener('change', render);
  window.addEventListener('meridiano:qualification-updated', render);
  window.addEventListener('meridiano:lead-prepared', () => {
    const routeCode = form.dataset.closeRouteV510 || routeForStage(decisionStage?.value || '');
    track('close_handoff_prepared', { stage: routeCode, target: 'whatsapp' });
  });

  applyRequestedIntent();
  render();

  window.MeridianoConversionCloseV510 = Object.freeze({
    version: '5.10.0',
    refresh: render,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false }),
  });
})();

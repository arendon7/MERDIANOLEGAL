(() => {
  const contractNode = document.getElementById('recommendation-contract-v514');
  let contract = {};
  try { contract = JSON.parse(contractNode?.textContent || '{}'); } catch (_error) { contract = {}; }
  const RULES = Object.freeze(contract.modalities || {});
  const params = new URL(window.location.href).searchParams;
  const cleanCode = (value) => String(value || '').trim().toLowerCase().replace(/[^a-z-]/g, '').slice(0, 24);
  const explicitIntent = cleanCode(params.get('commercial_intent'));

  const ROUTES = Object.freeze({
    proposal: Object.freeze({ label: 'Propuesta verificable', stage: 'Quiero recibir una propuesta', copy: 'Confirmar alcance, disponibilidad, honorarios, cronograma y condiciones de inicio.' }),
    scope: Object.freeze({ label: 'Definición de alcance', stage: 'Necesito definir mejor el alcance', copy: 'Delimitar resultado, perímetro, actores y dependencias antes de cotizar.' }),
    orientation: Object.freeze({ label: 'Orientación inicial', stage: 'Estoy explorando la necesidad', copy: 'Comprender primero la decisión y confirmar qué modalidad merece avanzar.' }),
  });
  const ROUTE_BY_MODALITY = Object.freeze({ diagnostic: 'scope', audit: 'proposal', product: 'proposal', specialist: 'scope', recurring: 'scope' });

  const form = document.getElementById('contact-form');
  const currentModality = () => {
    const fromForm = cleanCode(form?.dataset.commercialModalityCodeV513);
    const fromUrl = cleanCode(params.get('modality'));
    return RULES[fromForm] ? fromForm : (RULES[fromUrl] ? fromUrl : '');
  };

  const homePanel = document.querySelector('[data-decision-action-live-v515]');
  const homeLabel = homePanel?.querySelector('[data-action-label-v515]');
  const homeFit = homePanel?.querySelector('[data-action-fit-v515]');
  const homeCta = homePanel?.querySelector('[data-action-cta-v515]');
  const renderHome = () => {
    const code = currentModality();
    const rule = code ? RULES[code] : null;
    document.querySelectorAll('[data-decision-action-source-v515]').forEach((card) => {
      if (rule && card.dataset.decisionActionSourceV515 === code) card.dataset.selectedV515 = 'true';
      else delete card.dataset.selectedV515;
    });
    if (!homePanel || !homeLabel || !homeFit || !homeCta) return;
    if (!rule) {
      homeLabel.textContent = 'Elija una modalidad arriba';
      homeFit.textContent = 'Cada opción ya reúne encaje y siguiente acción. Use la comparación ampliada solo si necesita contrastar límites y alternativas.';
      homeCta.textContent = 'Ir al selector →';
      homeCta.setAttribute('href', '#proof-router-v512-title');
      homePanel.dataset.modality = 'unconfirmed';
      return;
    }
    homeLabel.textContent = rule.label;
    homeFit.textContent = rule.fit;
    homeCta.textContent = `${rule.cta} →`;
    homeCta.setAttribute('href', rule.href);
    homePanel.dataset.modality = code;
  };

  const decisionStage = form?.querySelector('[name="decision_stage"]');
  const routePanel = form?.querySelector('[data-route-panel-v515]');
  const routeLabel = routePanel?.querySelector('[data-route-label-v515]');
  const routeCopy = routePanel?.querySelector('[data-route-copy-v515]');
  const routeSource = routePanel?.querySelector('[data-route-source-v515]');
  const routeButton = routePanel?.querySelector('[data-apply-route-v515]');

  const preferredRoute = () => {
    if (ROUTES[explicitIntent]) return { code: explicitIntent, source: 'Punto de entrada', explicit: true };
    const modality = currentModality();
    if (ROUTE_BY_MODALITY[modality]) return { code: ROUTE_BY_MODALITY[modality], source: 'Modalidad considerada', explicit: false };
    return { code: 'orientation', source: 'Contexto aún abierto', explicit: false };
  };

  const renderRoute = () => {
    if (!form || !routePanel || !routeLabel || !routeCopy || !routeSource || !routeButton) return;
    const preferred = preferredRoute();
    const route = ROUTES[preferred.code];
    routePanel.dataset.route = preferred.code;
    routePanel.dataset.routeSource = preferred.explicit ? 'explicit' : 'suggested';
    form.dataset.suggestedRouteV515 = preferred.code;
    routeSource.textContent = preferred.source;
    routeLabel.textContent = route.label;
    routeCopy.textContent = route.copy;
    if (preferred.explicit) {
      routeButton.textContent = 'Ruta ya definida';
      routeButton.disabled = true;
    } else {
      routeButton.textContent = `Usar ${route.label.toLowerCase()}`;
      routeButton.disabled = false;
    }
  };

  routeButton?.addEventListener('click', () => {
    const preferred = preferredRoute();
    const route = ROUTES[preferred.code];
    if (!decisionStage || preferred.explicit) return;
    const option = [...decisionStage.options].find((item) => item.value === route.stage || item.textContent.trim() === route.stage);
    if (!option) return;
    decisionStage.value = option.value;
    form.dataset.actionRouteAppliedV515 = preferred.code;
    decisionStage.dispatchEvent(new Event('change', { bubbles: true }));
    renderRoute();
  });

  renderHome();
  renderRoute();
  window.addEventListener('meridiano:brief-updated', () => { renderHome(); renderRoute(); });
  window.addEventListener('meridiano:recommendation-updated', renderRoute);
  window.addEventListener('meridiano:qualification-updated', renderRoute);

  window.MeridianoDecisionActionV515 = Object.freeze({
    version: '5.15.0',
    routes: ROUTES,
    routeByModality: ROUTE_BY_MODALITY,
    refresh: () => { renderHome(); renderRoute(); },
    automaticChange: false,
    scoring: false,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false }),
  });
})();

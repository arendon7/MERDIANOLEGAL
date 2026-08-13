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

  // MOBILE-UX-V516:START
  const enhanceMobileScrollableRegionsV516 = () => {
    if (!window.matchMedia('(max-width: 760px)').matches) return;
    const regions = [
      ['.principles-grid', 'Principios de trabajo'],
      ['.mockup-nav-v45', 'Navegación del ejemplo de experiencia'],
      ['.contracting-route-v45', 'Ruta visual de contratación'],
    ];
    regions.forEach(([selector, label]) => {
      const node = document.querySelector(selector);
      if (!node) return;
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'region');
      node.setAttribute('aria-label', label);
      node.dataset.mobileScrollableV516 = 'true';
    });
  };

  // COMMERCIAL-FOCUS-V519:START
  // La información jurídica material permanece en el DOM. En móvil se conserva el
  // disclosure v5.16. En escritorio, orientation/scope parten replegados y una
  // intención explícita proposal conserva el detalle expandido. La web no infiere
  // intención ni cambia etapas: solo utiliza el parámetro explícito ya existente.
  const enhanceCommercialDisclosureV519 = () => {
    if (!form) return;
    const isMobile = window.matchMedia('(max-width: 760px)').matches;
    const expandForExplicitProposal = explicitIntent === 'proposal' && !isMobile;

    // CONTACT-COMPRESSION-V523:START
    // Desde v5.23 el HTML canónico ya contiene una única superficie nativa para
    // proceso/límites/condiciones. No se crean dos disclosures internos. La intención
    // explícita proposal puede abrir ese único detalle en cualquier viewport; ninguna
    // etapa se infiere ni se cambia automáticamente.
    const compressedProcess = form.querySelector('[data-contact-process-v523="true"]');
    if (compressedProcess) {
      const expandCompressedV523 = explicitIntent === 'proposal';
      compressedProcess.dataset.defaultStateV523 = expandCompressedV523 ? 'expanded-proposal' : 'collapsed-secondary';
      compressedProcess.dataset.defaultStateV519 = expandCompressedV523 ? 'expanded-proposal' : 'collapsed-secondary';
      compressedProcess.open = expandCompressedV523;
      return;
    }
    // CONTACT-COMPRESSION-V523:END

    const makeDisclosure = (root, keepClass, key, title, copy) => {
      if (!root || root.querySelector(':scope > details[data-mobile-disclosure-v516]')) return;
      const keep = root.querySelector(`:scope > .${keepClass}`);
      if (!keep) return;
      const movable = [...root.children].filter((child) => child !== keep);
      if (!movable.length) return;

      const details = document.createElement('details');
      details.className = 'commercial-disclosure-v516 commercial-disclosure-v519';
      details.dataset.mobileDisclosureV516 = key;
      details.dataset.commercialDisclosureV519 = key;
      details.dataset.defaultStateV519 = expandForExplicitProposal ? 'expanded-proposal' : 'collapsed-secondary';
      details.open = expandForExplicitProposal;
      const summary = document.createElement('summary');
      const strong = document.createElement('strong');
      const span = document.createElement('span');
      strong.textContent = title;
      span.textContent = copy;
      summary.append(strong, span);
      details.append(summary);
      movable.forEach((child) => details.append(child));
      root.append(details);
    };

    makeDisclosure(
      form.querySelector('[data-close-path-v510="true"]'),
      'close-head-v510',
      'proposal-path',
      'Ver ruta completa de solicitud a propuesta',
      'Etapas, anatomía de propuesta, criterio de avance y límites del formulario.'
    );
    makeDisclosure(
      form.querySelector('[data-engagement-v511="true"]'),
      'engagement-head-v511',
      'engagement-start',
      'Ver condiciones de aceptación e inicio',
      'Estados del encargo, verificaciones previas y actos que esta web no ejecuta.'
    );
  };
  // Alias contractual: v5.16 sigue teniendo un punto de entrada identificable para
  // su validator histórico; v5.19 amplía su alcance sin eliminar la capacidad.
  const enhanceMobileDisclosureV516 = enhanceCommercialDisclosureV519;
  enhanceMobileScrollableRegionsV516();
  enhanceMobileDisclosureV516();
  // COMMERCIAL-FOCUS-V519:END
  // MOBILE-UX-V516:END

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
    const alreadyApplied = decisionStage?.value === route.stage;
    routePanel.dataset.route = preferred.code;
    routePanel.dataset.routeSource = preferred.explicit ? 'explicit' : 'suggested';
    form.dataset.suggestedRouteV515 = preferred.code;
    routeSource.textContent = preferred.source;
    routeLabel.textContent = route.label;
    routeCopy.textContent = route.copy;
    if (preferred.explicit) {
      routeButton.textContent = 'Ruta ya definida';
      routeButton.disabled = true;
    } else if (alreadyApplied) {
      routeButton.textContent = 'Ruta aplicada';
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
    mobileUxV516: Object.freeze({ progressiveDisclosure: true, keyboardScrollableRegions: true, maxWidthPx: 760, hiddenMaterialContent: false }),
    commercialFocusV519: Object.freeze({ progressiveDisclosure: true, defaultCollapsed: true, defaultExpandedIntent: 'proposal', explicitIntentOnly: true, automaticDecisionChange: false, hiddenMaterialContent: false }),
    contactCompressionV523: Object.freeze({ singleSynthesis: true, singleProcessDisclosure: true, explicitProposalMayExpand: true, automaticDecisionChange: false, hiddenMaterialContent: false }),
  });
})();
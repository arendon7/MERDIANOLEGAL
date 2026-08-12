(() => {
  const form = document.getElementById('contact-form');
  const contractNode = document.getElementById('recommendation-contract-v514');
  if (!form || !contractNode) return;

  let contract;
  try {
    contract = JSON.parse(contractNode.textContent || '{}');
  } catch (_error) {
    return;
  }
  const RULES = Object.freeze(contract.modalities || {});

  const fitNode = form.querySelector('[data-recommendation-fit-v514]');
  const boundaryNode = form.querySelector('[data-recommendation-boundary-v514]');
  const alternativeNode = form.querySelector('[data-recommendation-alternative-v514]');
  const stateNode = form.querySelector('[data-recommendation-state-v514]');
  const params = new URL(window.location.href).searchParams;
  const cleanCode = (value) => String(value || '').trim().toLowerCase().replace(/[^a-z-]/g, '').slice(0, 24);

  const render = () => {
    const fromDataset = cleanCode(form.dataset.commercialModalityCodeV513);
    const fromUrl = cleanCode(params.get('modality'));
    const code = RULES[fromDataset] ? fromDataset : (RULES[fromUrl] ? fromUrl : '');
    const rule = code ? RULES[code] : null;

    if (rule) {
      form.dataset.recommendationCodeV514 = code;
      form.dataset.recommendationFitV514 = rule.fit;
      form.dataset.recommendationBoundaryV514 = rule.boundary;
      form.dataset.recommendationAlternativeV514 = rule.alternative;
      if (fitNode) fitNode.textContent = rule.fit;
      if (boundaryNode) boundaryNode.textContent = rule.boundary;
      if (alternativeNode) alternativeNode.textContent = rule.alternative;
      if (stateNode) stateNode.textContent = `Criterio aplicado: ${rule.label}. La modalidad definitiva se confirma al validar alcance y dependencias.`;
    } else {
      delete form.dataset.recommendationCodeV514;
      delete form.dataset.recommendationFitV514;
      delete form.dataset.recommendationBoundaryV514;
      delete form.dataset.recommendationAlternativeV514;
      if (fitNode) fitNode.textContent = 'Por confirmar: primero debe entenderse la necesidad y el resultado esperado.';
      if (boundaryNode) boundaryNode.textContent = 'No se recomienda una modalidad sin contexto suficiente para distinguir alcance puntual, cerrado, adaptable o recurrente.';
      if (alternativeNode) alternativeNode.textContent = 'El siguiente paso es delimitar la necesidad antes de comparar modalidades.';
      if (stateNode) stateNode.textContent = 'Sin modalidad preseleccionada. La web no asigna puntajes ni presume una recomendación.';
    }

    window.dispatchEvent(new CustomEvent('meridiano:recommendation-updated', {
      detail: { modality: code || 'unconfirmed', explainable: true, scoreUsed: false },
    }));
  };

  render();
  window.addEventListener('meridiano:brief-updated', render);
  window.addEventListener('meridiano:qualification-updated', render);

  window.MeridianoRecommendationV514 = Object.freeze({
    version: String(contract.version || '5.14.0'),
    rules: RULES,
    refresh: render,
    scoring: false,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false }),
  });
})();

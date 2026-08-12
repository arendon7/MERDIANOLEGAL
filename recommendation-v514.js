(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const RULES = Object.freeze({
    diagnostic: Object.freeze({
      label: 'Diagnóstico jurídico',
      fit: 'Encaja cuando primero debe delimitarse la exposición, priorizar riesgos y decidir qué trabajo posterior es proporcional.',
      boundary: 'No sustituye una auditoría transversal cerrada ni ejecuta por sí solo todas las correcciones identificadas.',
      alternative: 'Cambie a auditoría si necesita evidencia integral y un cierre documentado; a servicio especializado si el asunto ya está claramente delimitado.',
    }),
    audit: Object.freeze({
      label: 'Auditoría jurídica de alcance cerrado',
      fit: 'Encaja cuando necesita revisar un perímetro definido con evidencia, hallazgos, prioridades y criterios de cierre comparables.',
      boundary: 'No equivale a acompañamiento jurídico continuo ni absorbe indefinidamente asuntos que aparezcan después del perímetro pactado.',
      alternative: 'Cambie a acompañamiento recurrente si necesita seguimiento sostenido; a diagnóstico si todavía no sabe qué perímetro merece una auditoría completa.',
    }),
    product: Object.freeze({
      label: 'Producto de alcance cerrado',
      fit: 'Encaja cuando el problema permite fijar desde el inicio cantidades, entregables, cronograma, supuestos y aceptación.',
      boundary: 'Pierde eficiencia cuando hechos, negociación, regulación o terceros obligan a redefinir continuamente el alcance.',
      alternative: 'Cambie a servicio especializado si el asunto exige adaptación profesional continua; a acompañamiento recurrente si la demanda se repite mes a mes.',
    }),
    specialist: Object.freeze({
      label: 'Servicio jurídico especializado',
      fit: 'Encaja cuando la decisión está identificada pero el análisis, la negociación o la ejecución deben adaptarse a hechos y actores concretos.',
      boundary: 'No debe presentarse como paquete estándar si el perímetro depende de contingencias, iteraciones o decisiones de terceros.',
      alternative: 'Cambie a producto cerrado cuando el alcance ya sea estable y repetible; a diagnóstico si aún falta delimitar el problema central.',
    }),
    recurring: Object.freeze({
      label: 'Acompañamiento jurídico recurrente',
      fit: 'Encaja cuando la empresa necesita triage, criterio, memoria, coordinación y seguimiento continuo de una demanda jurídica recurrente.',
      boundary: 'No es la modalidad más eficiente para una única necesidad cerrada con entregable y fecha de terminación claramente definidos.',
      alternative: 'Cambie a producto o servicio especializado si el objetivo es resolver un asunto puntual; a auditoría si primero necesita una revisión integral de situación.',
    }),
  });

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
    version: '5.14.0',
    rules: RULES,
    refresh: render,
    scoring: false,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false }),
  });
})();

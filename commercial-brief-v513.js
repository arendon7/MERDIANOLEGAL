(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const modalityNode = form.querySelector('[data-brief-modality-v513]');
  const proofNode = form.querySelector('[data-brief-proof-v513]');
  const badge = form.querySelector('[data-brief-status-v513]');
  const params = new URL(window.location.href).searchParams;

  const MODALITIES = Object.freeze({
    diagnostic: 'Diagnóstico jurídico',
    audit: 'Auditoría jurídica de alcance cerrado',
    product: 'Producto de alcance cerrado',
    specialist: 'Servicio jurídico especializado',
    recurring: 'Acompañamiento jurídico recurrente',
  });
  const PROOF_STANDARD = 'Método + entregables + formatos + aceptación/cierre';
  const clean = (value, max = 160) => String(value || '').trim().replace(/\s+/g, ' ').slice(0, max);

  const requestedModality = clean(params.get('modality'), 24);
  const requestedProof = clean(params.get('proof_standard'), 24);
  const modalityLabel = MODALITIES[requestedModality] || '';
  const proofLabel = requestedProof === 'source' ? PROOF_STANDARD : '';

  const render = () => {
    if (modalityLabel) {
      form.dataset.commercialModalityCodeV513 = requestedModality;
      form.dataset.commercialModalityV513 = modalityLabel;
    } else {
      delete form.dataset.commercialModalityCodeV513;
      delete form.dataset.commercialModalityV513;
    }
    if (proofLabel) form.dataset.proofExpectationV513 = proofLabel;
    else delete form.dataset.proofExpectationV513;

    if (modalityNode) modalityNode.textContent = modalityLabel || 'Por confirmar según el alcance';
    if (proofNode) proofNode.textContent = proofLabel || 'Se definirá en la propuesta aplicable';
    if (badge) badge.textContent = modalityLabel && proofLabel ? 'Contexto conservado' : 'Contexto por completar';

    window.dispatchEvent(new CustomEvent('meridiano:brief-updated', {
      detail: {
        modality: requestedModality && MODALITIES[requestedModality] ? requestedModality : 'unconfirmed',
        proof: requestedProof === 'source' ? 'source' : 'unconfirmed',
      },
    }));
  };

  render();
  window.addEventListener('meridiano:qualification-updated', render);

  window.MeridianoCommercialBriefV513 = Object.freeze({
    version: '5.13.0',
    modalities: MODALITIES,
    proofStandard: PROOF_STANDARD,
    refresh: render,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false }),
  });
})();

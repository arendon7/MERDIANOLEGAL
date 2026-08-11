(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const need = form.querySelector('[name="need"]');
  const decisionStage = form.querySelector('[name="decision_stage"]');
  const urgency = form.querySelector('[name="urgency"]');
  const budget = form.querySelector('[name="budget"]');
  const panel = form.querySelector('[data-qualification-summary-v59]');
  const contextNode = form.querySelector('[data-qualification-context-v59]');
  const needNode = form.querySelector('[data-qualification-need-v59]');
  const stageNode = form.querySelector('[data-qualification-stage-v59]');
  const urgencyNode = form.querySelector('[data-qualification-urgency-v59]');
  const budgetNode = form.querySelector('[data-qualification-budget-v59]');
  const nextStepNode = form.querySelector('[data-qualification-next-step-v59]');
  const nextStepCopy = form.querySelector('[data-qualification-next-copy-v59]');

  const clean = (value, max = 180) => String(value || '').trim().replace(/\s+/g, ' ').slice(0, max);
  const normalized = (value) => clean(value, 220).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const selectedLabel = (select, fallback) => {
    if (!select || !select.value) return fallback;
    return clean(select.selectedOptions?.[0]?.textContent || select.value, 160);
  };

  const nextStepFor = (stage) => {
    if (stage === 'Quiero recibir una propuesta' || stage === 'Estoy comparando alternativas') {
      return {
        code: 'proposal_ready',
        label: 'Propuesta estructurada',
        copy: 'La conversación puede concentrarse en confirmar alcance, disponibilidad, honorarios, cronograma y condiciones de inicio.',
      };
    }
    if (stage === 'Necesito definir mejor el alcance') {
      return {
        code: 'scope_first',
        label: 'Llamada de alcance',
        copy: 'Primero conviene delimitar resultado, perímetro, información mínima, actores y dependencias antes de cotizar.',
      };
    }
    return {
      code: 'orientation_first',
      label: 'Orientación inicial',
      copy: 'El primer paso es comprender la decisión y determinar si corresponde orientación, diagnóstico, producto, proyecto o plan recurrente.',
    };
  };

  const resolveNeed = (raw) => {
    if (!need || !raw) return;
    const exact = [...need.options].find((option) => option.value === raw || option.textContent.trim() === raw);
    if (exact) {
      need.value = exact.value;
      return;
    }
    const value = normalized(raw);
    const rules = [
      [/diagnost/, 'Diagnóstico jurídico'],
      [/direccion juridica/, 'Dirección jurídica externa'],
      [/contrat|contract/, 'Contratos y negociaciones'],
      [/socio|societ|gobierno|inversion/, 'Socios, gobierno o inversión'],
      [/marca|software|intangib|propiedad intelectual/, 'Marca, software o intangibles'],
      [/inteligencia artificial|gobernanza de ia|programa de gobernanza de ia|\bia\b/, 'Gobernanza de IA'],
      [/regulad|permiso|autoridad/, 'Proyecto regulado'],
      [/legal operations|operacion juridica/, 'Legal Operations'],
      [/plan|recurrente/, 'Plan recurrente'],
      [/documento|confidencialidad|suministro|distribucion|terminos y condiciones/, 'Documento guiado'],
    ];
    for (const [pattern, label] of rules) {
      if (!pattern.test(value)) continue;
      const option = [...need.options].find((item) => item.value === label || item.textContent.trim() === label);
      if (option) need.value = option.value;
      return;
    }
  };

  const getContext = () => {
    const current = new URL(window.location.href);
    return clean(form.dataset.commercialContext || current.searchParams.get('context') || '', 220);
  };

  const render = () => {
    const stage = selectedLabel(decisionStage, 'Por seleccionar');
    const next = nextStepFor(decisionStage?.value || '');
    form.dataset.proposalReadiness = next.code;
    form.dataset.proposalNextStep = next.label;

    if (contextNode) contextNode.textContent = getContext() || 'Necesidad presentada desde la portada';
    if (needNode) needNode.textContent = selectedLabel(need, 'Por seleccionar');
    if (stageNode) stageNode.textContent = stage;
    if (urgencyNode) urgencyNode.textContent = selectedLabel(urgency, 'Por seleccionar');
    if (budgetNode) budgetNode.textContent = selectedLabel(budget, 'Por definir');
    if (nextStepNode) nextStepNode.textContent = next.label;
    if (nextStepCopy) nextStepCopy.textContent = next.copy;
    if (panel) panel.dataset.readiness = next.code;

    window.dispatchEvent(new CustomEvent('meridiano:qualification-updated', {
      detail: {
        stage: next.code,
        target: 'contact-intake',
        need: clean(need?.value || '', 80),
      },
    }));
  };

  const current = new URL(window.location.href);
  resolveNeed(current.searchParams.get('need') || current.searchParams.get('context') || '');

  [need, decisionStage, urgency, budget].filter(Boolean).forEach((field) => {
    field.addEventListener('change', render);
  });

  document.querySelectorAll('[data-commercial-contact]').forEach((trigger) => {
    trigger.addEventListener('click', () => window.setTimeout(render, 0));
  });

  render();

  window.MeridianoCommercialIntakeV59 = Object.freeze({
    version: '5.9.0',
    refresh: render,
    privacy: Object.freeze({ networkTransport: false, persistentStorage: false, piiInTelemetry: false }),
  });
})();

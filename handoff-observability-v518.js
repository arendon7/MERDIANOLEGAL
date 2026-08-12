(() => {
  const ACTIONS = Object.freeze({
    prepared: Object.freeze({ name: 'handoff_prepared', stage: 'handoff', target: 'whatsapp-draft' }),
    reopen_requested: Object.freeze({ name: 'handoff_reopen_requested', stage: 'handoff', target: 'whatsapp' }),
    copy_succeeded: Object.freeze({ name: 'handoff_copy_succeeded', stage: 'handoff', target: 'clipboard' }),
    copy_failed: Object.freeze({ name: 'handoff_copy_failed', stage: 'handoff', target: 'clipboard' }),
    edit_requested: Object.freeze({ name: 'handoff_edit_requested', stage: 'handoff', target: 'contact-form' }),
    draft_stale: Object.freeze({ name: 'handoff_draft_stale', stage: 'handoff', target: 'draft' }),
  });

  const safeAction = (value) => String(value || '').trim().slice(0, 48);

  window.addEventListener('meridiano:handoff-observation-v518', (event) => {
    const action = safeAction(event.detail?.action);
    const mapped = ACTIONS[action];
    if (!mapped) return;

    const payload = Object.freeze({ stage: mapped.stage, target: mapped.target });
    if (window.MeridianoTelemetry && typeof window.MeridianoTelemetry.track === 'function') {
      window.MeridianoTelemetry.track(mapped.name, payload);
    }
    window.dispatchEvent(new CustomEvent('meridiano:handoff-measurement-v518', {
      detail: Object.freeze({ name: mapped.name, ...payload }),
    }));
  });

  window.MeridianoHandoffObservabilityV518 = Object.freeze({
    version: '5.18.0',
    eventNames: Object.freeze(Object.values(ACTIONS).map((item) => item.name)),
    privacy: Object.freeze({
      piiAllowed: false,
      networkTransportIntroduced: false,
      persistentStorage: false,
      crossSessionIdentifier: false,
      formContentAllowed: false,
    }),
    semanticLimits: Object.freeze({
      sentKnown: false,
      deliveredKnown: false,
      readKnown: false,
      acceptedKnown: false,
      engagementStartedKnown: false,
      conversionKnown: false,
    }),
  });
})();

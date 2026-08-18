(() => {
  const config = window.MERIDIANO_PUBLIC_CONFIG || {};
  const analytics = config.analytics || {};
  const STAGES = Object.freeze(['need', 'offer', 'evidence', 'decision', 'contact', 'handoff']);
  const STAGE_SET = new Set(STAGES);
  const SOURCE_STAGE = Object.freeze({
    solution_view: 'offer',
    route_open: 'offer',
    authority_open: 'evidence',
    evidence_open: 'evidence',
    faq_open: 'evidence',
    contact_intent: 'contact',
    lead_prepared: 'handoff',
    handoff_prepared: 'handoff',
    handoff_reopen_requested: 'handoff',
    handoff_copy_succeeded: 'handoff',
    handoff_copy_failed: 'handoff',
    handoff_edit_requested: 'contact',
    handoff_draft_stale: 'handoff',
  });
  const CTA_STAGE = Object.freeze({
    'detail-page': 'offer',
    'sector-page': 'evidence',
    perspective: 'evidence',
    'contact-form': 'contact',
    whatsapp: 'contact',
  });
  const MAX_QUEUE = 24;
  const state = {
    enabled: analytics.enabled === true,
    provider: String(analytics.provider || 'none').trim().toLowerCase(),
    siteId: String(analytics.site_id || '').trim(),
    providerReady: false,
    error: '',
    queue: [],
    emitted: [],
  };

  const safeToken = (value, max = 80) => String(value || '')
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9:_-]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, max);

  const classifyStage = (event) => {
    const name = safeToken(event?.name, 48);
    const detail = event?.detail && typeof event.detail === 'object' ? event.detail : {};
    if (name === 'funnel_checkpoint') {
      const stage = safeToken(detail.stage, 24);
      return STAGE_SET.has(stage) ? stage : '';
    }
    if (name === 'cta_click') {
      return CTA_STAGE[safeToken(detail.target, 48)] || '';
    }
    return SOURCE_STAGE[name] || '';
  };

  const preview = (event) => {
    const stage = classifyStage(event);
    if (!stage) return null;
    return Object.freeze({ name: `meridiano_funnel_${stage}` });
  };

  const remember = (name) => {
    state.emitted.push(name);
    if (state.emitted.length > MAX_QUEUE) state.emitted.shift();
  };

  const flushPlausible = () => {
    if (!state.providerReady || typeof window.plausible !== 'function') return;
    while (state.queue.length) {
      const name = state.queue.shift();
      window.plausible(name);
      remember(name);
    }
  };

  const emit = (safeEvent) => {
    if (!state.enabled || !safeEvent) return false;
    if (state.provider !== 'plausible') return false;
    if (typeof window.plausible !== 'function' || !state.providerReady) {
      state.queue.push(safeEvent.name);
      if (state.queue.length > MAX_QUEUE) state.queue.shift();
      return true;
    }
    window.plausible(safeEvent.name);
    remember(safeEvent.name);
    return true;
  };

  const track = (event) => emit(preview(event));

  const setupPlausible = () => {
    if (!state.enabled || state.provider !== 'plausible') return;
    if (!/^pa-[A-Za-z0-9_-]+$/.test(state.siteId)) {
      state.error = 'invalid-plausible-site-id';
      state.enabled = false;
      return;
    }

    window.plausible = window.plausible || function plausibleQueue() {
      (window.plausible.q = window.plausible.q || []).push(arguments);
    };
    window.plausible.init = window.plausible.init || function plausibleInit(options) {
      window.plausible.o = options || {};
    };
    window.plausible.init();

    const script = document.createElement('script');
    script.async = true;
    script.src = `https://plausible.io/js/${state.siteId}.js`;
    script.dataset.meridianoAnalyticsProvider = 'plausible';
    script.addEventListener('load', () => {
      state.providerReady = true;
      flushPlausible();
    }, { once: true });
    script.addEventListener('error', () => {
      state.error = 'plausible-script-load-failed';
      state.queue.length = 0;
    }, { once: true });
    document.head.append(script);
  };

  setupPlausible();

  window.MeridianoAnalyticsAdapter = Object.freeze({
    version: '6.1.0',
    enabled: state.enabled,
    provider: state.provider,
    track,
    preview,
    snapshot: () => Object.freeze({
      version: '6.1.0',
      enabled: state.enabled,
      provider: state.provider,
      providerReady: state.providerReady,
      error: state.error,
      queuedEventNames: Object.freeze(state.queue.slice()),
      emittedEventNames: Object.freeze(state.emitted.slice()),
      privacy: Object.freeze({
        piiAllowed: false,
        formContentAllowed: false,
        handoffReferenceAllowed: false,
        eventPropertiesAllowed: false,
        persistentStorageIntroduced: false,
        crossSessionIdentifierIntroduced: false,
        fingerprintingIntroduced: false,
      }),
    }),
  });
})();

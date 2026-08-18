(() => {
  const config = window.MERIDIANO_PUBLIC_CONFIG || {};
  const analytics = config.analytics || {};
  const STAGES = Object.freeze(['need', 'offer', 'evidence', 'decision', 'contact', 'handoff']);
  const STAGE_SET = new Set(STAGES);
  const MAX_EVENTS = STAGES.length;
  const state = {
    enabled: analytics.enabled === true,
    provider: String(analytics.provider || 'none').trim().toLowerCase(),
    siteId: String(analytics.site_id || '').trim(),
    providerReady: false,
    error: '',
    queue: [],
    emitted: [],
    seenStages: new Set(),
  };

  const safeToken = (value, max = 80) => String(value || '')
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9:_-]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, max);

  // El único input exportable es la etapa ya normalizada por funnel-observability-v529.
  // event/target y cualquier otro campo del detail se ignoran deliberadamente.
  const preview = (detail) => {
    const stage = safeToken(detail?.stage, 24);
    if (!STAGE_SET.has(stage)) return null;
    return Object.freeze({ name: `meridiano_funnel_${stage}` });
  };

  const remember = (name) => {
    state.emitted.push(name);
    if (state.emitted.length > MAX_EVENTS) state.emitted.shift();
  };

  const flushPlausible = () => {
    if (!state.providerReady || typeof window.plausible !== 'function') return;
    while (state.queue.length) {
      const name = state.queue.shift();
      window.plausible(name);
      remember(name);
    }
  };

  const emitStage = (detail) => {
    if (!state.enabled) return false;
    const stage = safeToken(detail?.stage, 24);
    const safeEvent = preview(detail);
    if (!safeEvent || state.seenStages.has(stage)) return false;
    if (state.provider !== 'plausible') return false;

    state.seenStages.add(stage);
    if (typeof window.plausible !== 'function' || !state.providerReady) {
      state.queue.push(safeEvent.name);
      if (state.queue.length > MAX_EVENTS) state.queue.shift();
      return true;
    }
    window.plausible(safeEvent.name);
    remember(safeEvent.name);
    return true;
  };

  // telemetry-v50.js conserva la firma histórica adapter.track(name, event),
  // pero v6.1 no consume ese payload raw. La exportación nace únicamente del
  // evento saneado meridiano:funnel-v529.
  const track = () => false;

  const setupPlausible = () => {
    if (!state.enabled) return;
    if (state.provider !== 'plausible') {
      state.error = 'unsupported-provider';
      state.enabled = false;
      return;
    }
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

  window.addEventListener('meridiano:funnel-v529', (event) => {
    emitStage(event.detail || {});
  });

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
      observedStageNames: Object.freeze([...state.seenStages]),
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

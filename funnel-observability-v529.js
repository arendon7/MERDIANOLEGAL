(() => {
  const VERSION = '5.29.0';
  const MAX_EVENTS = 48;
  const CHECKPOINT_THRESHOLD = 0.05;
  const STAGE_ORDER = Object.freeze(['awareness', 'need', 'offer', 'evidence', 'decision', 'contact', 'handoff']);
  const STAGE_RANK = Object.freeze(Object.fromEntries(STAGE_ORDER.map((stage, rank) => [stage, rank])));
  const SOURCE_EVENTS = Object.freeze({
    page_view: 'awareness',
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
  const CTA_TARGETS = Object.freeze({
    'detail-page': 'offer',
    'sector-page': 'evidence',
    perspective: 'evidence',
    'contact-form': 'contact',
    whatsapp: 'contact',
  });
  const CHECKPOINTS = Object.freeze([
    Object.freeze({ selector: '#necesidades', stage: 'need', target: 'home:needs' }),
    Object.freeze({ selector: '#servicios', stage: 'offer', target: 'home:services' }),
    Object.freeze({ selector: '#productos', stage: 'offer', target: 'home:products' }),
    Object.freeze({ selector: '#honorarios', stage: 'decision', target: 'home:fees' }),
    Object.freeze({ selector: '#contratacion', stage: 'decision', target: 'home:contracting' }),
    Object.freeze({ selector: '#contacto', stage: 'contact', target: 'home:contact' }),
  ]);

  const safe = (value, max = 80) => String(value || '')
    .trim()
    .replace(/\s+/g, ' ')
    .slice(0, max);

  const events = [];
  const milestones = new Map();
  const checkpointSeen = new Set();
  let furthestStage = '';
  let sequence = 0;

  const classify = (event) => {
    const name = safe(event?.name, 48);
    const target = safe(event?.detail?.target, 80);
    if (name === 'funnel_checkpoint') {
      const stage = safe(event?.detail?.stage, 24);
      return Object.prototype.hasOwnProperty.call(STAGE_RANK, stage) ? stage : '';
    }
    if (name === 'cta_click') return CTA_TARGETS[target] || '';
    return SOURCE_EVENTS[name] || '';
  };

  const ingest = (event, source = 'telemetry') => {
    const stage = classify(event);
    if (!stage) return null;
    sequence += 1;
    const item = Object.freeze({
      sequence,
      stage,
      event: safe(event?.name, 48),
      target: safe(event?.detail?.target, 80),
      need: safe(event?.detail?.need, 80),
      reference: safe(event?.detail?.reference, 32),
      source: safe(source, 24),
    });
    events.push(item);
    if (events.length > MAX_EVENTS) events.shift();
    if (!milestones.has(stage)) milestones.set(stage, item);
    if (!furthestStage || STAGE_RANK[stage] > STAGE_RANK[furthestStage]) furthestStage = stage;
    window.dispatchEvent(new CustomEvent('meridiano:funnel-v529', {
      detail: Object.freeze({ stage, event: item.event, target: item.target }),
    }));
    return item;
  };

  const telemetry = window.MeridianoTelemetry;
  if (telemetry && typeof telemetry.snapshot === 'function') {
    telemetry.snapshot().forEach((event) => ingest(event, 'telemetry-history'));
  }

  window.addEventListener('meridiano:telemetry', (event) => {
    ingest(event.detail || {}, 'telemetry-live');
  });

  const emitCheckpoint = (checkpoint) => {
    if (checkpointSeen.has(checkpoint.target)) return;
    checkpointSeen.add(checkpoint.target);
    const detail = Object.freeze({ stage: checkpoint.stage, target: checkpoint.target, need: '' });
    if (window.MeridianoTelemetry && typeof window.MeridianoTelemetry.track === 'function') {
      window.MeridianoTelemetry.track('funnel_checkpoint', detail);
    } else {
      ingest({ name: 'funnel_checkpoint', detail }, 'checkpoint-local');
    }
  };

  const catalogId = safe(document.body?.dataset.catalogId, 64);
  if (catalogId) emitCheckpoint(Object.freeze({ stage: 'offer', target: `offer:${catalogId}` }));

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting || entry.intersectionRatio < CHECKPOINT_THRESHOLD) return;
        const checkpoint = CHECKPOINTS.find((item) => document.querySelector(item.selector) === entry.target);
        if (!checkpoint) return;
        emitCheckpoint(checkpoint);
        observer.unobserve(entry.target);
      });
    }, { threshold: [CHECKPOINT_THRESHOLD] });
    CHECKPOINTS.forEach((checkpoint) => {
      const node = document.querySelector(checkpoint.selector);
      if (node) observer.observe(node);
    });
  }

  const snapshot = () => Object.freeze({
    version: VERSION,
    furthestStage,
    milestones: Object.freeze(STAGE_ORDER
      .filter((stage) => milestones.has(stage))
      .map((stage) => Object.freeze({ ...milestones.get(stage) }))),
    events: Object.freeze(events.map((event) => Object.freeze({ ...event }))),
  });

  window.MeridianoFunnelV529 = Object.freeze({
    version: VERSION,
    stages: STAGE_ORDER,
    snapshot,
    privacy: Object.freeze({
      piiAllowed: false,
      formContentAllowed: false,
      persistentStorage: false,
      crossSessionIdentifier: false,
      fingerprinting: false,
      networkTransportIntroduced: false,
      usesExistingTelemetryAdapter: true,
    }),
    semanticLimits: Object.freeze({
      sentKnown: false,
      deliveredKnown: false,
      readKnown: false,
      proposalAcceptedKnown: false,
      engagementStartedKnown: false,
      clientConversionKnown: false,
    }),
  });
})();

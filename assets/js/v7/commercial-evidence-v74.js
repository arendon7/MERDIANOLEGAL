(() => {
  const VERSION = '7.4.0';
  const MAX_EVENTS = 24;
  const SOURCE_PREFIX = 'li-';
  const SUBJECTS = Object.freeze({
    'legal-ai-transformation': Object.freeze({ source: 'li-legal-ai-transformation', route: '/servicios/legal-operations.html' }),
    'contract-control': Object.freeze({ source: 'li-contract-control', route: '/productos/sistema-contractual-empresarial.html' }),
    'ai-governance-360': Object.freeze({ source: 'li-ai-governance-360', route: '/productos/programa-gobernanza-ia.html' }),
    'regulatory-control': Object.freeze({ source: 'li-regulatory-control', route: '/productos/proyecto-regulado-estructurado.html' }),
    'legal-desk': Object.freeze({ source: 'li-legal-desk', route: '/soluciones/ordenar-operacion-juridica.html' }),
  });
  const SUBJECT_SET = new Set(Object.keys(SUBJECTS));
  const SOURCE_TO_SUBJECT = new Map(Object.entries(SUBJECTS).map(([id, item]) => [item.source, id]));
  const INTERACTIONS = new Set(['offer_view', 'demo_offer_open', 'contact_intent', 'handoff_prepared']);
  const events = [];
  const seen = new Set();
  let sequence = 0;

  const subjectFromSource = (raw) => SOURCE_TO_SUBJECT.get(String(raw || '').trim()) || '';
  const sourceForSubject = (subject) => SUBJECTS[subject]?.source || '';
  const routeSubject = () => {
    const pathname = window.location.pathname;
    for (const [id, item] of Object.entries(SUBJECTS)) {
      if (id === 'legal-desk') continue;
      if (pathname.endsWith(item.route)) return id;
    }
    return '';
  };
  const querySourceSubject = () => {
    const current = new URL(window.location.href);
    return subjectFromSource(current.searchParams.get('source'));
  };
  const currentSubject = () => querySourceSubject() || routeSubject();

  const emit = (subject, interaction) => {
    if (!SUBJECT_SET.has(subject) || !INTERACTIONS.has(interaction)) return null;
    const key = `${subject}:${interaction}`;
    if (seen.has(key)) return null;
    seen.add(key);
    sequence += 1;
    const item = Object.freeze({ sequence, subject, interaction });
    events.push(item);
    if (events.length > MAX_EVENTS) events.shift();
    window.dispatchEvent(new CustomEvent('meridiano:commercial-evidence-v74', {
      detail: Object.freeze({ subject, interaction }),
    }));
    return item;
  };

  const decorateInternalHref = (link, subject) => {
    const source = sourceForSubject(subject);
    if (!source || !(link instanceof HTMLAnchorElement)) return false;
    const raw = link.getAttribute('href') || '';
    if (!raw || raw.startsWith('mailto:') || raw.startsWith('tel:') || raw.includes('wa.me/')) return false;
    const target = new URL(raw, window.location.href);
    if (target.origin !== window.location.origin) return false;
    target.searchParams.set('source', source);
    link.href = target.href;
    return true;
  };

  const wireDemo = () => {
    if (!window.location.pathname.endsWith('/experiencia.html') && !window.location.pathname.endsWith('experiencia.html')) return;
    document.querySelectorAll('[data-li-demo-scenario]').forEach((card) => {
      const subject = String(card.getAttribute('data-li-demo-scenario') || '').trim();
      if (!SUBJECT_SET.has(subject)) return;
      card.querySelectorAll('a[href]').forEach((link) => {
        if (!decorateInternalHref(link, subject)) return;
        link.addEventListener('click', () => emit(subject, 'demo_offer_open'), { passive: true });
      });
    });
  };

  const wireOffer = () => {
    const subject = currentSubject();
    if (!subject) return;
    if (!window.location.pathname.endsWith('/index.html') && !window.location.pathname.endsWith('/')) {
      emit(subject, 'offer_view');
    }
    document.querySelectorAll('a[href*="#contacto"]').forEach((link) => {
      if (!decorateInternalHref(link, subject)) return;
      link.addEventListener('click', () => emit(subject, 'contact_intent'), { passive: true });
    });
  };

  const wireHandoff = () => {
    const subject = querySourceSubject();
    if (!subject) return;
    window.addEventListener('meridiano:lead-prepared', () => emit(subject, 'handoff_prepared'));
  };

  const previewExternalName = (subject, interaction) => {
    if (!SUBJECT_SET.has(subject) || !INTERACTIONS.has(interaction)) return null;
    return `meridiano_ce_${interaction}_${subject.replace(/-/g, '_')}`;
  };

  wireDemo();
  wireOffer();
  wireHandoff();

  window.MeridianoCommercialEvidenceV74 = Object.freeze({
    version: VERSION,
    status: 'readiness-disabled',
    sourcePrefix: SOURCE_PREFIX,
    subjects: Object.freeze([...SUBJECT_SET]),
    interactions: Object.freeze([...INTERACTIONS]),
    currentSubject,
    previewExternalName,
    snapshot: () => Object.freeze({
      version: VERSION,
      status: 'readiness-disabled',
      currentSubject: currentSubject(),
      events: Object.freeze(events.map((item) => Object.freeze({ ...item }))),
      privacy: Object.freeze({
        piiAllowed: false,
        freeTextAllowed: false,
        formContentAllowed: false,
        persistentStorage: false,
        cookies: false,
        crossSessionIdentifier: false,
        fingerprinting: false,
        networkTransport: false,
        externalAnalyticsEnabled: false,
      }),
      semanticLimits: Object.freeze({
        contactIntentMeansMessageSent: false,
        handoffPreparedMeansMessageSent: false,
        handoffPreparedMeansDelivered: false,
        handoffPreparedMeansRead: false,
        handoffPreparedMeansClientConversion: false,
      }),
    }),
  });
})();

(() => {
  const config = window.MERIDIANO_PUBLIC_CONFIG || {};
  const analytics = config.analytics || {};
  const queue = [];
  const MAX_EVENTS = 40;

  const safeText = (value, max = 80) => String(value || '')
    .trim()
    .replace(/\s+/g, ' ')
    .slice(0, max);

  const push = (name, detail = {}) => {
    const event = {
      name: safeText(name, 48),
      path: window.location.pathname,
      at: Date.now(),
      detail: {
        stage: safeText(detail.stage, 48),
        target: safeText(detail.target, 80),
        need: safeText(detail.need, 80),
        reference: safeText(detail.reference, 32),
      },
    };
    queue.push(event);
    if (queue.length > MAX_EVENTS) queue.shift();

    window.dispatchEvent(new CustomEvent('meridiano:telemetry', { detail: event }));

    const adapter = window.MeridianoAnalyticsAdapter;
    if (analytics.enabled === true && adapter && typeof adapter.track === 'function') {
      adapter.track(event.name, event);
    }
    return event;
  };

  const classifyClick = (element) => {
    if (!(element instanceof Element)) return null;
    const link = element.closest('a,button');
    if (!link) return null;
    const href = link.getAttribute('href') || '';
    if (href.includes('wa.me/')) return { stage: 'contact', target: 'whatsapp' };
    if (href.includes('#contacto') || link.dataset.commercialContact) return { stage: 'contact', target: 'contact-form' };
    if (link.classList.contains('full-detail-link')) return { stage: 'consideration', target: 'detail-page' };
    if (link.classList.contains('sector-deep-link')) return { stage: 'consideration', target: 'sector-page' };
    if (link.classList.contains('perspective-read-link') || link.classList.contains('library-deep-link')) return { stage: 'consideration', target: 'perspective' };
    if (href.includes('experiencia.html') || href.includes('demo.html')) return { stage: 'demo', target: href.split('?')[0].split('#')[0] };
    return null;
  };

  document.addEventListener('click', (event) => {
    const classified = classifyClick(event.target);
    if (classified) push('cta_click', classified);
  }, { passive: true });

  window.addEventListener('meridiano:lead-prepared', (event) => {
    const detail = event.detail || {};
    push('lead_prepared', {
      stage: 'contact',
      target: 'whatsapp',
      need: detail.need,
      reference: detail.reference,
    });
  });

  push('page_view', { stage: 'awareness', target: document.body?.dataset.pageType || document.title });

  window.MeridianoTelemetry = Object.freeze({
    track: push,
    snapshot: () => queue.slice(),
    networkEnabled: analytics.enabled === true,
    provider: analytics.provider || 'none',
  });
})();

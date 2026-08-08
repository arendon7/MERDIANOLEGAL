(() => {
  const body = document.body;
  const safe = (value, max = 80) => String(value || '')
    .trim()
    .replace(/\s+/g, ' ')
    .slice(0, max);

  const need = () => safe(body?.dataset.pageNeed || '', 80);
  const emit = (name, detail = {}) => {
    const payload = Object.freeze({
      stage: safe(detail.stage, 48),
      target: safe(detail.target, 80),
      need: safe(detail.need ?? need(), 80),
    });
    if (window.MeridianoTelemetry && typeof window.MeridianoTelemetry.track === 'function') {
      window.MeridianoTelemetry.track(name, payload);
    }
    window.dispatchEvent(new CustomEvent('meridiano:measurement-v53', {
      detail: Object.freeze({ name: safe(name, 48), ...payload }),
    }));
  };

  const solutionSlug = safe(body?.dataset.solutionSlug || '', 80);
  if (solutionSlug) {
    emit('solution_view', { stage: 'consideration', target: `solution:${solutionSlug}` });
  }

  document.addEventListener('click', (event) => {
    const link = event.target instanceof Element ? event.target.closest('a') : null;
    if (!link) return;
    const href = link.getAttribute('href') || '';

    if (link.dataset.authoritySolution) {
      emit('authority_open', {
        stage: 'consideration',
        target: `solution:${safe(link.dataset.authoritySolution, 64)}`,
      });
      return;
    }

    if (solutionSlug && link.closest('.cro-related-v52') && href.includes('.html')) {
      const target = href.split('/').pop().split(/[?#]/)[0].replace(/\.html$/, '');
      emit('route_open', { stage: 'consideration', target: `solution:${safe(target, 64)}` });
      return;
    }

    if (solutionSlug && (href.includes('../perspectivas/') || href.includes('../sectores/'))) {
      const kind = href.includes('../perspectivas/') ? 'perspective' : 'sector';
      const target = href.split('/').pop().split(/[?#]/)[0].replace(/\.html$/, '');
      emit('evidence_open', { stage: 'consideration', target: `${kind}:${safe(target, 64)}` });
      return;
    }

    if (solutionSlug && (href.includes('#contacto') || href.includes('wa.me/'))) {
      emit('contact_intent', {
        stage: 'contact',
        target: href.includes('wa.me/') ? 'whatsapp' : 'contact-form',
      });
    }
  }, { passive: true });

  document.addEventListener('toggle', (event) => {
    const details = event.target;
    if (!(details instanceof HTMLDetailsElement) || !details.open || !solutionSlug) return;
    const faq = details.closest('.cro-faq-v52');
    if (!faq) return;
    const items = Array.from(faq.querySelectorAll('details'));
    const index = items.indexOf(details);
    emit('faq_open', {
      stage: 'consideration',
      target: `faq:${index >= 0 ? index + 1 : 0}`,
    });
  }, true);

  window.MeridianoMeasurementV53 = Object.freeze({
    version: '5.3.0',
    piiAllowed: false,
    networkTransport: false,
    persistentStorage: false,
  });
})();

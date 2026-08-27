(() => {
  const allowed = new Set(['awareness', 'need', 'offer', 'evidence', 'decision', 'contact', 'handoff']);
  const seen = new Set();
  const history = [];

  const emit = (stage) => {
    if (!allowed.has(stage) || seen.has(stage)) return false;
    seen.add(stage);
    history.push(stage);
    window.dispatchEvent(new CustomEvent('meridiano:funnel-v529', {
      detail: Object.freeze({ stage }),
    }));
    return true;
  };

  emit('awareness');

  const checkpoints = [
    ['[data-v8-home-section="H02"]', 'need'],
    ['[data-v8-home-section="H03"]', 'offer'],
    ['[data-v8-home-section="H07"]', 'evidence'],
    ['[data-v8-home-section="H12"]', 'decision'],
    ['#contacto', 'contact'],
  ];
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting || entry.intersectionRatio < 0.05) return;
        const match = checkpoints.find(([selector]) => document.querySelector(selector) === entry.target);
        if (!match) return;
        emit(match[1]);
        observer.unobserve(entry.target);
      });
    }, { threshold: [0.05] });
    checkpoints.forEach(([selector]) => {
      const node = document.querySelector(selector);
      if (node) observer.observe(node);
    });
  }

  document.addEventListener('click', (event) => {
    const target = event.target.closest?.('a,button');
    if (!target) return;
    const href = target.getAttribute('href') || '';
    if (href === '#contacto' || target.matches('[data-v8-contact-submit]')) emit('contact');
  }, { passive: true });

  window.addEventListener('meridiano:v8-handoff', (event) => {
    if (event.detail?.stage === 'handoff') emit('handoff');
  });

  window.MeridianoV8Measurement = Object.freeze({
    version: '8.0.0-candidate',
    snapshot: () => Object.freeze(history.slice()),
    privacy: Object.freeze({
      piiAllowed: false,
      formContentAllowed: false,
      persistentStorage: false,
      crossSessionIdentifier: false,
      fingerprinting: false,
      directNetworkTransport: false,
      sanitizedAdapterEventOnly: true,
    }),
  });
})();

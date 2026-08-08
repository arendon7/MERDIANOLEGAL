(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;

  const need = form.querySelector('select[name="need"]');
  const message = form.querySelector('textarea[name="message"]');

  const setNeed = (label) => {
    if (!need) return;
    const option = [...need.options].find((item) => item.textContent.trim() === label || item.value === label);
    if (option) need.value = option.value;
  };

  const prepareContact = (label, needLabel = 'Plan recurrente') => {
    setNeed(needLabel);
    if (message && !message.value.trim()) {
      message.value = `Estoy interesado en ${label}. Quiero confirmar el alcance, la capacidad incluida, los tiempos de respuesta, las exclusiones y las condiciones de inicio.`;
    }
    form.dataset.commercialContext = label;
    form.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    window.setTimeout(() => form.querySelector('input[name="name"]')?.focus({ preventScroll: true }), 450);
  };

  document.querySelectorAll('[data-commercial-contact]').forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      prepareContact(link.dataset.commercialContact || 'una solución de Meridiano Legal', link.dataset.need || 'Plan recurrente');
    });
  });

  document.querySelectorAll('[data-commercial-context][href]').forEach((link) => {
    const rawHref = link.getAttribute('href');
    if (!rawHref || rawHref.startsWith('#')) return;
    try {
      const url = new URL(rawHref, window.location.href);
      url.searchParams.set('context', link.dataset.commercialContext || 'Referencia comercial');
      if (link.dataset.need) url.searchParams.set('need', link.dataset.need);
      const base = rawHref.split(/[?#]/)[0];
      const query = url.searchParams.toString();
      const hash = url.hash;
      link.setAttribute('href', `${base}${query ? `?${query}` : ''}${hash}`);
    } catch {
      // El enlace estático sigue siendo funcional aunque no pueda contextualizarse.
    }
  });
})();

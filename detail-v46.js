(() => {
  const toc = document.querySelector('.detail-toc-v46');
  const links = [...document.querySelectorAll('.detail-toc-links-v46 a')];
  const detailPage = document.getElementById('detail-page');
  let observer = null;

  const sectionIds = ['pregunta-title','alcance-title','entregables-title','cronograma-title','limites-title','contacto-title'];

  const setActive = (id) => {
    links.forEach((link) => {
      const active = link.getAttribute('href') === `#${id}`;
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };

  const bindSections = () => {
    observer?.disconnect();
    const targets = sectionIds.map((id) => document.getElementById(id)).filter(Boolean);
    if (!targets.length || !('IntersectionObserver' in window)) return;
    observer = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible[0]?.target?.id) setActive(visible[0].target.id);
    }, { rootMargin: '-22% 0px -62% 0px', threshold: [0, .1, .5] });
    targets.forEach((target) => observer.observe(target));
  };

  links.forEach((link) => link.addEventListener('click', () => {
    const id = link.getAttribute('href')?.slice(1);
    if (id) setActive(id);
  }));

  const decoratePhases = () => {
    const phases = {
      'pregunta-title': 'decidir', 'resultado-title': 'decidir',
      'situaciones-title': 'delimitar', 'alcance-title': 'delimitar', 'perimetro-title': 'delimitar',
      'metodo-title': 'ejecutar', 'entregables-title': 'ejecutar', 'formatos-title': 'ejecutar', 'cronograma-title': 'ejecutar',
      'requisitos-title': 'gobernar', 'responsabilidades-title': 'gobernar', 'aceptacion-title': 'gobernar', 'limites-title': 'gobernar',
      'relacionadas-title': 'continuar', 'contacto-title': 'continuar',
    };
    Object.entries(phases).forEach(([id, phase]) => {
      document.getElementById(id)?.closest('section')?.setAttribute('data-detail-phase', phase);
    });
  };

  const refresh = () => {
    decoratePhases();
    bindSections();
  };

  if (detailPage) {
    new MutationObserver(refresh).observe(detailPage, { childList: true });
  }

  if (toc && links.length) {
    setActive('pregunta-title');
    refresh();
  }
})();

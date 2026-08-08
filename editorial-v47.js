(() => {
  const body = document.body;
  if (!body?.dataset.editorialV47) return;

  const progress = document.createElement('div');
  progress.className = 'reading-progress-v47';
  progress.setAttribute('aria-hidden', 'true');
  progress.innerHTML = '<span></span>';
  document.body.append(progress);
  const progressBar = progress.firstElementChild;
  const updateProgress = () => {
    const doc = document.documentElement;
    const max = Math.max(1, doc.scrollHeight - window.innerHeight);
    const value = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
    progressBar.style.width = `${value}%`;
  };
  updateProgress();
  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress);

  const toggle = document.querySelector('.editorial-menu-toggle-v47');
  const nav = document.getElementById('editorial-nav-v47');
  const closeMenu = ({ focus = false } = {}) => {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Abrir menú');
    nav.classList.remove('open-v47');
    body.classList.remove('editorial-menu-open-v47');
    if (focus) toggle.focus();
  };
  toggle?.addEventListener('click', () => {
    if (!nav) return;
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    nav.classList.toggle('open-v47', open);
    body.classList.toggle('editorial-menu-open-v47', open);
  });
  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav?.classList.contains('open-v47')) closeMenu({ focus: true });
  });
  window.addEventListener('resize', () => {
    if (window.innerWidth > 1050) closeMenu();
  });

  const observeNavigation = (selector) => {
    const links = [...document.querySelectorAll(selector)].filter((link) => link.hash);
    if (!links.length || !('IntersectionObserver' in window)) return;
    const targets = links.map((link) => document.getElementById(decodeURIComponent(link.hash.slice(1)))).filter(Boolean);
    if (!targets.length) return;
    const setActive = (id) => {
      links.forEach((link) => {
        if (link.hash === `#${id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    };
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio);
      if (visible[0]?.target?.id) setActive(visible[0].target.id);
    }, { rootMargin: '-22% 0px -62% 0px', threshold: [0, .1, .4] });
    targets.forEach((target) => observer.observe(target));
  };
  observeNavigation('.article-toc a');
  observeNavigation('.sector-quicknav-v47 a');

  document.querySelectorAll('.portal-nav').forEach((button) => {
    button.addEventListener('click', () => {
      if (window.innerWidth <= 760) {
        requestAnimationFrame(() => button.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' }));
      }
    });
  });
})();

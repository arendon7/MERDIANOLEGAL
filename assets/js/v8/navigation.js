(() => {
  'use strict';

  const root = document.documentElement;
  root.classList.add('ml-js');

  const shell = document.querySelector('[data-ml-shell]');
  if (!shell) return;

  const menuToggle = shell.querySelector('[data-ml-menu-toggle]');
  const navPanel = shell.querySelector('[data-ml-nav-panel]');
  const megaToggle = shell.querySelector('[data-ml-mega-toggle]');
  const mega = shell.querySelector('[data-ml-mega]');
  const mobileQuery = window.matchMedia('(max-width: 959px)');
  let mobileOpen = false;
  let megaOpen = false;

  const focusableSelector = [
    'a[href]:not([tabindex="-1"])',
    'button:not([disabled]):not([tabindex="-1"])',
    '[tabindex]:not([tabindex="-1"])'
  ].join(',');

  const focusableWithin = (container) => {
    if (!container) return [];
    return Array.from(container.querySelectorAll(focusableSelector)).filter((element) => {
      return !element.hidden && element.getAttribute('aria-hidden') !== 'true';
    });
  };

  const closeMega = ({ restoreFocus = false } = {}) => {
    if (!mega || !megaToggle) return;
    mega.hidden = true;
    megaToggle.setAttribute('aria-expanded', 'false');
    megaOpen = false;
    if (restoreFocus) megaToggle.focus();
  };

  const openMega = () => {
    if (!mega || !megaToggle) return;
    mega.hidden = false;
    megaToggle.setAttribute('aria-expanded', 'true');
    megaOpen = true;
    const target = mega.querySelector('a[href], [tabindex="0"]');
    if (mobileQuery.matches && target) target.focus();
  };

  const setScrollLock = (locked) => {
    root.classList.toggle('ml-nav-open', locked);
    document.body.classList.toggle('ml-nav-open', locked);
  };

  const closeMobile = ({ restoreFocus = false } = {}) => {
    if (!menuToggle || !navPanel) return;
    mobileOpen = false;
    menuToggle.setAttribute('aria-expanded', 'false');
    setScrollLock(false);
    closeMega();
    if (mobileQuery.matches) navPanel.hidden = true;
    if (restoreFocus) menuToggle.focus();
  };

  const openMobile = () => {
    if (!menuToggle || !navPanel) return;
    mobileOpen = true;
    navPanel.hidden = false;
    menuToggle.setAttribute('aria-expanded', 'true');
    setScrollLock(true);
    window.requestAnimationFrame(() => {
      const focusable = focusableWithin(navPanel);
      if (focusable.length) focusable[0].focus();
    });
  };

  const syncResponsiveState = () => {
    if (!navPanel || !menuToggle) return;
    if (mobileQuery.matches) {
      navPanel.hidden = !mobileOpen;
    } else {
      mobileOpen = false;
      navPanel.hidden = false;
      menuToggle.setAttribute('aria-expanded', 'false');
      setScrollLock(false);
      closeMega();
    }
  };

  if (menuToggle && navPanel) {
    menuToggle.addEventListener('click', () => {
      if (mobileOpen) closeMobile({ restoreFocus: true });
      else openMobile();
    });

    navPanel.addEventListener('click', (event) => {
      const link = event.target.closest('a[href]');
      if (!link || !mobileQuery.matches) return;
      closeMobile();
    });
  }

  if (megaToggle && mega) {
    megaToggle.addEventListener('click', () => {
      if (megaOpen) closeMega({ restoreFocus: true });
      else openMega();
    });
  }

  document.addEventListener('click', (event) => {
    if (!megaOpen || shell.contains(event.target)) return;
    closeMega();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      if (megaOpen) {
        event.preventDefault();
        closeMega({ restoreFocus: true });
        return;
      }
      if (mobileOpen) {
        event.preventDefault();
        closeMobile({ restoreFocus: true });
      }
      return;
    }

    if (event.key !== 'Tab' || !mobileOpen || !navPanel || navPanel.hidden) return;
    const focusable = focusableWithin(navPanel);
    if (!focusable.length) {
      event.preventDefault();
      menuToggle?.focus();
      return;
    }
    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });

  const onMediaChange = () => syncResponsiveState();
  if (typeof mobileQuery.addEventListener === 'function') {
    mobileQuery.addEventListener('change', onMediaChange);
  } else {
    mobileQuery.addListener(onMediaChange);
  }

  syncResponsiveState();
})();

(() => {
  const prefix = location.pathname.includes('/servicios/') || location.pathname.includes('/productos/') || location.pathname.includes('/sectores/') || location.pathname.includes('/perspectivas/') ? '../' : '';
  const darkLogo = `${prefix}assets/brand/meridiano-logo-horizontal-dark.svg`;
  const lightLogo = `${prefix}assets/brand/meridiano-logo-horizontal-light.svg`;
  const monogram = `${prefix}assets/brand/meridiano-monogram.svg`;

  document.querySelectorAll('header img[src*="logo-meridiano"], .brand img[src*="logo-meridiano"], .detail-brand img[src*="logo-meridiano"], .firm-brand img[src*="logo-meridiano"], .insight-brand img[src*="logo-meridiano"], .app-brand img[src*="logo-meridiano"]').forEach((img) => {
    img.src = darkLogo;
    img.alt = 'Meridiano Legal, Derecho, Empresa y Tecnología';
  });
  document.querySelectorAll('footer img[src*="logo-meridiano"], .detail-footer img[src*="logo-meridiano"], .insight-footer img[src*="logo-meridiano"]').forEach((img) => {
    img.src = lightLogo;
    img.alt = 'Meridiano Legal';
  });

  const hero = document.querySelector('.hero-art > img');
  if (hero) {
    hero.src = 'assets/images/global/home-hero.webp';
    hero.classList.add('visual-home-hero');
    hero.alt = 'Panorama empresarial de Medellín que representa dirección jurídica, empresa y territorio';
    hero.width = 800;
    hero.height = 450;
    hero.loading = 'eager';
    hero.fetchPriority = 'high';
  }

  document.querySelectorAll('.director-mark').forEach((mark) => {
    const image = document.createElement('img');
    image.src = monogram;
    image.alt = '';
    image.width = 82;
    image.height = 82;
    mark.replaceChildren(image);
  });
})();

(() => {
  const STYLE_PATH = 'decision-flow.css';

  if (!document.querySelector(`link[href="${STYLE_PATH}"]`)) {
    const stylesheet = document.createElement('link');
    stylesheet.rel = 'stylesheet';
    stylesheet.href = STYLE_PATH;
    document.head.append(stylesheet);
  }

  const topicConfig = {
    empresa: {
      label: 'Organización jurídica de la empresa',
      serviceTitle: 'Diagnóstico Jurídico Empresarial',
      serviceUrl: 'servicios/diagnostico-juridico-empresarial.html',
      productTitle: 'Empresa Jurídicamente Organizada',
      productUrl: 'productos/empresa-juridicamente-organizada.html',
      need: 'Diagnóstico jurídico',
      reason: 'Permite ordenar estructura, contratos, obligaciones y riesgos antes de ejecutar correcciones aisladas.',
    },
    contratos: {
      label: 'Contratos y negociaciones',
      serviceTitle: 'Contratación Estratégica y Gestión Contractual',
      serviceUrl: 'servicios/contratacion-estrategica.html',
      productTitle: 'Sistema Contractual Empresarial',
      productUrl: 'productos/sistema-contractual-empresarial.html',
      need: 'Contratos y negociaciones',
      reason: 'Conecta la negociación con aprobaciones, obligaciones, evidencia, cambios, preavisos y salida.',
    },
    socios: {
      label: 'Socios, gobierno e inversión',
      serviceTitle: 'Sociedades, Gobierno e Inversión',
      serviceUrl: 'servicios/sociedades-gobierno-inversion.html',
      productTitle: 'Empresa Lista para Inversión',
      productUrl: 'productos/empresa-lista-para-inversion.html',
      need: 'Socios, gobierno o inversión',
      reason: 'Integra capital, autoridad, información, activos, permanencia, inversión y mecanismos de salida.',
    },
    activos: {
      label: 'Marca, software y activos intangibles',
      serviceTitle: 'Propiedad Intelectual y Activos Intangibles',
      serviceUrl: 'servicios/propiedad-intelectual.html',
      productTitle: 'Marca, Software y Activos Intangibles Protegidos',
      productUrl: 'productos/activos-intangibles-protegidos.html',
      need: 'Marca, software o intangibles',
      reason: 'Permite verificar titularidad, protección, licencias, componentes de terceros y capacidad de explotación.',
    },
    ia: {
      label: 'Tecnología e inteligencia artificial',
      serviceTitle: 'Gobernanza Jurídica de Tecnología e Inteligencia Artificial',
      serviceUrl: 'servicios/tecnologia-inteligencia-artificial.html',
      productTitle: 'Programa de Gobernanza de IA',
      productUrl: 'productos/programa-gobernanza-ia.html',
      need: 'Gobernanza de IA',
      reason: 'Ordena casos de uso, datos, proveedores, supervisión humana, incidentes y trazabilidad.',
    },
    regulado: {
      label: 'Proyecto o actividad regulada',
      serviceTitle: 'Estructuración Jurídica de Proyectos Regulados',
      serviceUrl: 'servicios/proyectos-regulados.html',
      productTitle: 'Proyecto Regulado Estructurado',
      productUrl: 'productos/proyecto-regulado-estructurado.html',
      need: 'Proyecto regulado',
      reason: 'Organiza actividad, territorio, autoridades, permisos, actores, contratos y condiciones precedentes.',
    },
    operaciones: {
      label: 'Operación jurídica y cumplimiento',
      serviceTitle: 'Legal Operations y Transformación de la Función Jurídica',
      serviceUrl: 'servicios/legal-operations.html',
      productTitle: 'Programa de Protección de Datos y Consumidor',
      productUrl: 'productos/proteccion-datos-consumidor.html',
      need: 'Legal Operations',
      reason: 'Convierte solicitudes, documentos, obligaciones y controles en un modelo operativo administrable.',
    },
  };

  const choiceSection = document.getElementById('elegir');
  if (choiceSection && !document.getElementById('selector')) {
    const guide = document.createElement('section');
    guide.id = 'selector';
    guide.className = 'section solution-guide-section';
    guide.dataset.component = 'selector-guiado-meridiano';
    guide.innerHTML = `
      <div class="container">
        <div class="section-heading heading-row">
          <div><p class="eyebrow dark">SELECTOR GUIADO</p><h2>Defina el punto de entrada sin tener que conocer el nombre del servicio.</h2></div>
          <p>Responda tres preguntas. La recomendación es orientativa y no sustituye la revisión de contexto, disponibilidad, conflictos ni alcance.</p>
        </div>
        <div class="guide-layout">
          <form class="guide-form" id="solution-guide-form">
            <label><span>1. ¿Qué necesita estructurar?</span>
              <select name="topic" required>
                <option value="">Seleccione una materia</option>
                <option value="empresa">Organización jurídica de la empresa</option>
                <option value="contratos">Contratos y negociaciones</option>
                <option value="socios">Socios, gobierno e inversión</option>
                <option value="activos">Marca, software y activos intangibles</option>
                <option value="ia">Tecnología e inteligencia artificial</option>
                <option value="regulado">Proyecto o actividad regulada</option>
                <option value="operaciones">Operación jurídica y cumplimiento</option>
              </select>
            </label>
            <label><span>2. ¿Qué resultado espera?</span>
              <select name="result" required>
                <option value="">Seleccione un resultado</option>
                <option value="decidir">Criterio para tomar una decisión</option>
                <option value="cerrar">Un resultado cerrado y verificable</option>
                <option value="implementar">Una intervención a la medida</option>
                <option value="acompanar">Capacidad jurídica recurrente</option>
              </select>
            </label>
            <label><span>3. ¿Cuál es el horizonte?</span>
              <select name="horizon" required>
                <option value="">Seleccione un horizonte</option>
                <option value="urgente">Decisión inmediata o próxima</option>
                <option value="semanas">Proyecto de varias semanas</option>
                <option value="continuo">Necesidad mensual o continua</option>
              </select>
            </label>
            <button class="btn btn-navy" type="submit">Obtener recomendación</button>
            <p class="guide-privacy">No incluya nombres, cifras, documentos ni información confidencial.</p>
          </form>
          <div class="guide-result" id="solution-guide-result" aria-live="polite">
            <span>RECOMENDACIÓN ORIENTATIVA</span>
            <h3>Complete las tres preguntas.</h3>
            <p>El selector comparará orientación, servicio, producto y plan para proponer el punto de entrada más proporcional.</p>
          </div>
        </div>
        <div class="guide-comparison" aria-label="Comparación de modalidades">
          <article><strong>Orientación</strong><span>Pregunta focal</span><small>Criterio y ruta inmediata.</small></article>
          <article><strong>Servicio</strong><span>Asunto a la medida</span><small>Análisis, negociación o implementación.</small></article>
          <article><strong>Producto</strong><span>Resultado delimitado</span><small>Metodología y entregables cerrables.</small></article>
          <article><strong>Plan</strong><span>Capacidad recurrente</span><small>Priorización, memoria y seguimiento.</small></article>
        </div>
      </div>`;
    choiceSection.after(guide);
  }

  const contactForm = document.getElementById('contact-form');
  const needField = contactForm?.querySelector('select[name="need"]');
  const messageField = contactForm?.querySelector('textarea[name="message"]');
  let activeContext = '';

  const setNeedValue = (value) => {
    if (!needField || !value) return;
    const option = [...needField.options].find((item) => item.value === value || item.textContent.trim() === value);
    if (option) needField.value = option.value;
  };

  const ensureContextBanner = () => {
    if (!contactForm) return null;
    let banner = contactForm.querySelector('.contact-context');
    if (banner) return banner;
    banner = document.createElement('div');
    banner.className = 'contact-context full';
    banner.hidden = true;
    banner.innerHTML = `
      <div><span>CONTEXTO DEL RECORRIDO</span><strong></strong><small>Se incorporará a la solicitud para evitar que tenga que explicar desde dónde llegó.</small></div>
      <button type="button" aria-label="Quitar contexto">Quitar</button>`;
    contactForm.prepend(banner);
    banner.querySelector('button')?.addEventListener('click', () => {
      activeContext = '';
      banner.hidden = true;
    });
    return banner;
  };

  const applyContactContext = (label, need = '') => {
    if (!contactForm || !label) return;
    activeContext = label;
    setNeedValue(need);
    const banner = ensureContextBanner();
    if (banner) {
      const strong = banner.querySelector('strong');
      if (strong) strong.textContent = label;
      banner.hidden = false;
    }
  };

  const titleFromPath = (path) => {
    const file = decodeURIComponent(path.split('/').pop() || '').replace(/\.html$/i, '');
    return file.replace(/-/g, ' ').replace(/\b\p{L}/gu, (letter) => letter.toUpperCase());
  };

  const inferNeedFromPath = (path) => {
    const value = path.toLowerCase();
    if (/ia|inteligencia-artificial|tecnologia-software/.test(value)) return 'Gobernanza de IA';
    if (/contrat|sistema-contractual/.test(value)) return 'Contratos y negociaciones';
    if (/socios|inversion|sociedades|startup/.test(value)) return 'Socios, gobierno o inversión';
    if (/propiedad-intelectual|intangibles|marca-software/.test(value)) return 'Marca, software o intangibles';
    if (/legal-operations|operaciones-juridicas|proteccion-datos-consumidor/.test(value)) return 'Legal Operations';
    if (/regulad|servicios-publicos|aseo|agroindustria|salud-negocios|proyectos-publicos/.test(value)) return 'Proyecto regulado';
    if (/diagnostico|empresa-juridicamente-organizada/.test(value)) return 'Diagnóstico jurídico';
    return '';
  };

  const pageContextFromLocation = () => {
    const params = new URLSearchParams(window.location.search);
    const explicitContext = params.get('context')?.trim();
    const explicitNeed = params.get('need')?.trim();
    if (explicitContext) return { label: explicitContext, need: explicitNeed || '' };
    if (!document.referrer) return null;
    try {
      const referrer = new URL(document.referrer);
      if (referrer.origin !== window.location.origin || referrer.pathname === window.location.pathname) return null;
      const type = referrer.pathname.includes('/sectores/') ? 'Sector'
        : referrer.pathname.includes('/perspectivas/') ? 'Perspectiva'
        : referrer.pathname.includes('/servicios/') ? 'Servicio'
        : referrer.pathname.includes('/productos/') ? 'Producto'
        : referrer.pathname.endsWith('/firma.html') ? 'Página institucional'
        : '';
      if (!type) return null;
      return { label: `${type}: ${titleFromPath(referrer.pathname)}`, need: inferNeedFromPath(referrer.pathname) };
    } catch {
      return null;
    }
  };

  const initialContext = pageContextFromLocation();
  if (initialContext) applyContactContext(initialContext.label, initialContext.need);

  contactForm?.addEventListener('submit', () => {
    if (!activeContext || !messageField?.value.trim()) return;
    const prefix = `Contexto del recorrido: ${activeContext}`;
    if (!messageField.value.startsWith(prefix)) messageField.value = `${prefix}\n\n${messageField.value.trim()}`;
  }, true);

  const recommendationFor = (topic, result, horizon) => {
    const config = topicConfig[topic];
    if (!config) return null;
    const horizonText = horizon === 'urgente' ? 'Requiere calificación inicial prioritaria.'
      : horizon === 'continuo' ? 'Conviene diseñar capacidad, prioridades y seguimiento recurrente.'
      : 'Puede estructurarse por hitos y entregables durante varias semanas.';

    if (result === 'acompanar' || horizon === 'continuo') {
      return {
        mode: 'PLAN / DIRECCIÓN JURÍDICA EXTERNA',
        title: 'Dirección Jurídica Externa',
        href: 'servicios/direccion-juridica-externa.html',
        need: 'Dirección jurídica externa',
        reason: `La necesidad exige continuidad, memoria institucional y priorización. ${config.reason}`,
        horizon: horizonText,
      };
    }
    if (result === 'cerrar') {
      return {
        mode: 'PRODUCTO DE ALCANCE CERRADO',
        title: config.productTitle,
        href: config.productUrl,
        need: config.need,
        reason: `El resultado puede delimitarse mediante metodología, entregables y criterios de cierre. ${config.reason}`,
        horizon: horizonText,
      };
    }
    if (result === 'implementar') {
      return {
        mode: 'SERVICIO PROFESIONAL A LA MEDIDA',
        title: config.serviceTitle,
        href: config.serviceUrl,
        need: config.need,
        reason: `El asunto requiere análisis e implementación ajustados a hechos, actores y dependencias. ${config.reason}`,
        horizon: horizonText,
      };
    }
    return {
      mode: topic === 'empresa' ? 'DIAGNÓSTICO / ORIENTACIÓN INICIAL' : 'ORIENTACIÓN ESPECIALIZADA',
      title: topic === 'empresa' ? 'Diagnóstico Jurídico Empresarial' : config.serviceTitle,
      href: topic === 'empresa' ? 'productos/diagnostico-juridico-empresarial.html' : config.serviceUrl,
      need: topic === 'empresa' ? 'Diagnóstico jurídico' : config.need,
      reason: `El primer objetivo es calificar el problema y decidir el siguiente paso sin sobredimensionar la intervención. ${config.reason}`,
      horizon: horizonText,
    };
  };

  const guideForm = document.getElementById('solution-guide-form');
  const guideResult = document.getElementById('solution-guide-result');
  guideForm?.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!guideForm.reportValidity() || !guideResult) return;
    const data = new FormData(guideForm);
    const topic = String(data.get('topic') || '');
    const result = String(data.get('result') || '');
    const horizon = String(data.get('horizon') || '');
    const recommendation = recommendationFor(topic, result, horizon);
    if (!recommendation) return;
    const topicLabel = topicConfig[topic]?.label || 'Necesidad jurídica';
    guideResult.innerHTML = `
      <span>${recommendation.mode}</span>
      <h3>${recommendation.title}</h3>
      <p>${recommendation.reason}</p>
      <small>${recommendation.horizon}</small>
      <div class="guide-actions">
        <a class="btn btn-outline-dark" href="${recommendation.href}">Revisar alcance</a>
        <button class="btn btn-gold" type="button">Presentar esta necesidad</button>
      </div>`;
    guideResult.classList.add('has-result');
    guideResult.querySelector('button')?.addEventListener('click', () => {
      applyContactContext(`Selector guiado: ${topicLabel} · ${recommendation.title}`, recommendation.need);
      document.getElementById('contacto')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
      messageField?.focus({ preventScroll: true });
    });
  });

  const menuButton = document.querySelector('.menu-toggle');
  if (menuButton) {
    const syncMenuState = () => document.body.classList.toggle('menu-open', menuButton.getAttribute('aria-expanded') === 'true');
    new MutationObserver(syncMenuState).observe(menuButton, { attributes: true, attributeFilter: ['aria-expanded'] });
    syncMenuState();
  }

  const versionLabel = [...document.querySelectorAll('.footer-bottom span')].find((item) => item.textContent.includes('Web demostrativa'));
  if (versionLabel) versionLabel.textContent = 'Web demostrativa v7.1.0';
})();

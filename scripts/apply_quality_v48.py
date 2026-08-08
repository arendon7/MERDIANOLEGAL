#!/usr/bin/env python3
"""Cierre v4.8: HTML estático, rutas, accesibilidad, SEO y performance."""
from pathlib import Path
import json,re

R=Path(__file__).resolve().parents[1]; I=R/'index.html'; S=R/'site-v3.js'; D=R/'demo.html'; M=R/'sitemap.xml'
V=json.loads((R/'version.json').read_text(encoding='utf-8')); VER=V['version']; DATE=V['release_date']
SEO_A='<!-- QUALITY-V48-SEO:START -->'; SEO_B='<!-- QUALITY-V48-SEO:END -->'
NEEDS={'empresa':'productos/diagnostico-juridico-empresarial.html','ia':'productos/programa-gobernanza-ia.html','socios':'productos/empresa-lista-para-inversion.html','intangibles':'productos/activos-intangibles-protegidos.html','regulado':'productos/proyecto-regulado-estructurado.html','operacion':'servicios/legal-operations.html'}
SERV={'diagnostic':'servicios/diagnostico-juridico-empresarial.html','direction':'servicios/direccion-juridica-externa.html','contracts':'servicios/contratacion-estrategica.html','corporate':'servicios/sociedades-gobierno-inversion.html','ip':'servicios/propiedad-intelectual.html','ai':'servicios/tecnologia-inteligencia-artificial.html','regulated':'servicios/proyectos-regulados.html','ops':'servicios/legal-operations.html'}
PROD={
'Diagnóstico Jurídico Empresarial':('Auditoría Jurídica Empresarial Integral','5 a 6 semanas','Revisión transversal con hasta 80 hallazgos, cinco instrumentos correctivos y plan jurídico de 90 días.','productos/diagnostico-juridico-empresarial.html'),
'Empresa Jurídicamente Organizada':('Empresa Jurídicamente Organizada','6 a 10 semanas','Gobierno, atribuciones, contratos, obligaciones y expediente jurídico organizados como sistema operativo.','productos/empresa-juridicamente-organizada.html'),
'Marca, Software y Activos Intangibles Protegidos':('Marca, Software y Activos Intangibles Protegidos','6 a 8 semanas','Inventario, titularidad, protección, licencias y evidencia para hasta 40 activos intangibles priorizados.','productos/activos-intangibles-protegidos.html'),
'Empresa Lista para Inversión':('Empresa Lista para Inversión','8 a 10 semanas','Red flags, cap table, contratos materiales, regularizaciones y data room jurídico antes de una inversión.','productos/empresa-lista-para-inversion.html'),
'Programa de Gobernanza de IA':('Programa de Gobernanza Jurídica y Uso Responsable de IA','8 a 10 semanas','Hasta 25 casos de uso, clasificación de riesgo, reglas de uso, proveedores, controles, incidentes y capacitación.','productos/programa-gobernanza-ia.html'),
'Proyecto Regulado Estructurado':('Proyecto Regulado Jurídicamente Estructurado','8 a 10 semanas','Autoridades, permisos, predios, contratos, condiciones precedentes y ruta habilitante del proyecto.','productos/proyecto-regulado-estructurado.html'),
'Sistema Contractual Empresarial':('Sistema Contractual Empresarial','8 a 10 semanas','Seis modelos, biblioteca de cláusulas, playbook, aprobaciones, hasta 100 obligaciones y repositorio contractual.','productos/sistema-contractual-empresarial.html'),
'Programa de Protección de Datos y Consumidor':('Programa de Datos, Consumidor y Canales Digitales','8 a 10 semanas','Tratamientos, bases, términos, PQR, incidentes, proveedores y evidencia operativa para datos y consumidor.','productos/proteccion-datos-consumidor.html')}
SECT=[('i-network','Tecnología, software e IA','Desarrollo, licencias, datos, proveedores, activos y gobernanza.','sectores/tecnologia-software-ia.html'),('i-regulated','Servicios públicos, aseo y economía circular','Modelos operativos, actores territoriales, habilitaciones, contratos, obligaciones y aprovechamiento.','sectores/servicios-publicos-aseo-economia-circular.html'),('i-ops','Transformación de operaciones jurídicas','Solicitudes, procesos, documentos, obligaciones, métricas, automatización y gestión del cambio.','sectores/operaciones-juridicas.html'),('i-chart','Agroindustria y fertilizantes','Producción, comercialización, alianzas, activos y regulación sectorial.','sectores/agroindustria-fertilizantes-sostenibilidad.html'),('i-shield','Salud y negocios regulados','Prestadores, alianzas, experiencia del usuario, datos y riesgo regulatorio.','sectores/salud-negocios-regulados.html'),('i-building','Proyectos públicos','Actores, convenios, competencias, cronogramas y cumplimiento.','sectores/proyectos-publicos-territoriales.html'),('i-contract','Comercio y distribución','Canales, consumidor, garantías, marca, metas, territorio y terminación.','sectores/comercio-distribucion.html'),('i-people','Startups e inversión','Fundadores, capital, gobierno, activos, contratos y preparación para inversión.','sectores/startups-inversion.html')]
PERS={'ai':'perspectivas/gobierno-juridico-inteligencia-artificial.html','contracts':'perspectivas/contratos-administrables.html','regulated':'perspectivas/proyectos-regulados-secuencia-viabilidad.html'}

def seo():
    schema={'@context':'https://schema.org','@graph':[{'@type':['Organization','LegalService'],'@id':'https://arendon7.github.io/MERDIANOLEGAL/#organization','name':'Meridiano Legal','url':'https://arendon7.github.io/MERDIANOLEGAL/','description':'Dirección jurídica para empresas, innovación y proyectos regulados.','telephone':'+57 300 850 7813','areaServed':{'@type':'Country','name':'Colombia'},'address':{'@type':'PostalAddress','addressLocality':'Medellín','addressCountry':'CO'}},{'@type':'WebSite','@id':'https://arendon7.github.io/MERDIANOLEGAL/#website','url':'https://arendon7.github.io/MERDIANOLEGAL/','name':'Meridiano Legal','inLanguage':'es-CO','publisher':{'@id':'https://arendon7.github.io/MERDIANOLEGAL/#organization'}}]}
    j=json.dumps(schema,ensure_ascii=False,separators=(',',':'))
    return f'''{SEO_A}\n  <meta name="robots" content="index,follow,max-image-preview:large">\n  <meta property="og:site_name" content="Meridiano Legal">\n  <meta property="og:locale" content="es_CO">\n  <meta property="og:url" content="https://arendon7.github.io/MERDIANOLEGAL/">\n  <meta property="og:image:width" content="800">\n  <meta property="og:image:height" content="450">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:title" content="Meridiano Legal | Dirección jurídica para empresas que avanzan">\n  <meta name="twitter:description" content="Servicios, productos jurídicos y dirección externa para convertir riesgos y decisiones en entregables, responsables y seguimiento.">\n  <meta name="twitter:image" content="https://arendon7.github.io/MERDIANOLEGAL/assets/images/global/home-hero.webp">\n  <link rel="preload" as="image" href="assets/images/global/home-hero.webp" type="image/webp" fetchpriority="high">\n  <script type="application/ld+json">{j}</script>\n{SEO_B}'''

def patch_index():
    t=I.read_text(encoding='utf-8'); t=re.sub(re.escape(SEO_A)+r'[\s\S]*?'+re.escape(SEO_B),'',t,count=1); t=t.replace('  <title>',seo()+'\n  <title>',1)
    t,n=re.subn(r'<div class="hero-art"><img[^>]*>','<div class="hero-art"><img src="assets/images/global/home-hero.webp" alt="Panorama empresarial de Medellín que representa dirección jurídica, empresa y territorio" width="800" height="450" loading="eager" decoding="async" fetchpriority="high">',t,count=1)
    if n!=1: raise RuntimeError('hero')
    def need(m):
        route=m.group(1); href=NEEDS.get(route)
        if not href: raise RuntimeError('need '+route)
        return f'<a class="need-card" href="{href}">{m.group(2)}</a>'
    t=re.sub(r'<button class="need-card" type="button" data-route="([^"]+)">([\s\S]*?)</button>',need,t)
    if t.count('<a class="need-card"')!=6: raise RuntimeError('needs')
    t=re.sub(r'<a class="full-detail-link" href="servicios/[^"]+">[^<]*</a>','',t)
    for k,u in SERV.items():
        t,n=re.subn(rf'(<button type="button" data-service="{k}">Ver alcance →</button>)',rf'\1<a class="full-detail-link" href="{u}">Ver ficha completa</a>',t,count=1)
        if n!=1: raise RuntimeError('service '+k)
    def product(m):
        cat,legacy=m.group(1),m.group(2); x=PROD.get(legacy)
        if not x: raise RuntimeError('product '+legacy)
        title,dur,summary,url=x
        return f'<article class="product-card" data-category="{cat}"><small>{dur}</small><h3>{title}</h3><p>{summary}</p><button type="button" data-product="{legacy}">Vista ejecutiva</button><a class="full-detail-link" href="{url}">Ver ficha completa</a></article>'
    t=re.sub(r'<article class="product-card" data-category="([^"]+)">[\s\S]*?<button type="button" data-product="([^"]+)">[^<]*</button>(?:<a class="full-detail-link"[^>]*>[^<]*</a>)?</article>',product,t)
    if sum(x[0] in t for x in PROD.values())!=8: raise RuntimeError('products')
    cards=''.join(f'<article><svg aria-hidden="true"><use href="#{i}"/></svg><strong>{a}</strong><p>{b}</p><a class="sector-deep-link" href="{u}">Explorar sector</a></article>' for i,a,b,u in SECT)
    t,n=re.subn(r'<div class="sectors-grid">[\s\S]*?</div>',f'<div class="sectors-grid">{cards}</div>',t,count=1)
    if n!=1: raise RuntimeError('sectors')
    t=re.sub(r'<a class="perspective-read-link"[^>]*>[^<]*</a>','',t); t=re.sub(r'<div class="perspective-library-action">[\s\S]*?</div>','',t,count=1)
    for k,u in PERS.items():
        t,n=re.subn(rf'(<button type="button" data-service="{k}">Explorar la práctica →</button>)',rf'\1<a class="perspective-read-link" href="{u}">Leer perspectiva completa</a>',t,count=1)
        if n!=1: raise RuntimeError('perspective '+k)
    heading='<div class="perspective-library-action"><a class="library-deep-link" href="perspectivas.html">Abrir biblioteca de perspectivas</a></div>'
    marker='<section class="section perspectives-section" id="perspectivas">'; pos=t.find(marker)
    if pos<0: raise RuntimeError('perspectives section')
    end=t.find('</div><div class="perspectives-grid">',pos)
    if end<0: raise RuntimeError('perspectives heading')
    t=t[:end]+heading+t[end:]
    t=re.sub(r'<a class="firm-deep-link"[^>]*>[^<]*</a>','',t)
    pat=r'(<section class="section firm-section" id="firma">[\s\S]*?<div class="editorial-copy">[\s\S]*?)(</div></div></section>)'
    t,n=re.subn(pat,r'\1<a class="firm-deep-link" href="firma.html">Conocer la firma y su método</a>\2',t,count=1)
    if n!=1: raise RuntimeError('firm')
    t=t.replace('class="product-tabs" role="tablist" aria-label="Filtrar productos"','class="product-tabs" role="group" aria-label="Filtrar productos"').replace(' aria-selected="true"','').replace(' aria-selected="false"','')
    t=re.sub(r'<button class="tab active" type="button" data-filter="all"(?: aria-pressed="true")?>','<button class="tab active" type="button" data-filter="all" aria-pressed="true">',t,count=1)
    for f in ('entrada','transformacion','proteccion','operacion'): t=re.sub(rf'<button class="tab" type="button" data-filter="{f}"(?: aria-pressed="false")?>',f'<button class="tab" type="button" data-filter="{f}" aria-pressed="false">',t,count=1)
    t=re.sub(r'<span id="year">(?:\d{4})?</span>',f'<span id="year">{DATE[:4]}</span>',t,count=1)
    for tag in ('<link rel="stylesheet" href="page-context.css">','<link rel="stylesheet" href="quality-v48.css">'): t=t.replace('  '+tag+'\n','').replace(tag+'\n','').replace('  '+tag,'').replace(tag,'')
    t=t.replace('</head>','  <link rel="stylesheet" href="page-context.css">\n  <link rel="stylesheet" href="quality-v48.css">\n</head>',1); I.write_text(t,encoding='utf-8')

def patch_js():
    t=S.read_text(encoding='utf-8'); t=re.sub(r"\n  const routeMap = \{[^\n]+\};",'',t,count=1); t=re.sub(r"\n  document\.querySelectorAll\('\[data-route\]'\)\.forEach\([\s\S]*?\n  document\.querySelector\('\.modal-close'\)","\n  document.querySelector('.modal-close')",t,count=1)
    old="function setMenu(open) { if (!menuButton || !navigation) return; menuButton.setAttribute('aria-expanded', String(open)); navigation.classList.toggle('open', open); }"; new="function setMenu(open) { if (!menuButton || !navigation) return; menuButton.setAttribute('aria-expanded', String(open)); menuButton.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú'); navigation.classList.toggle('open', open); document.body.classList.toggle('menu-open', open); }"
    if old in t:t=t.replace(old,new,1)
    elif new not in t:raise RuntimeError('menu')
    old="document.addEventListener('keydown', (event) => { if (event.key === 'Escape') setMenu(false); });"; new="document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && navigation?.classList.contains('open')) { setMenu(false); menuButton?.focus(); } });"
    if old in t:t=t.replace(old,new,1)
    elif new not in t:raise RuntimeError('escape')
    t=t.replace("tab.setAttribute('aria-selected', String(tab.classList.contains('active')))","tab.removeAttribute('aria-selected'); tab.setAttribute('aria-pressed', String(tab.classList.contains('active')))").replace("item.setAttribute('aria-selected', String(active))","item.setAttribute('aria-pressed', String(active))")
    t=t.replace("window.scrollTo({ top: 0, behavior: 'smooth' })","window.scrollTo({ top: 0, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' })")
    S.write_text(t,encoding='utf-8')

def patch_misc():
    t=D.read_text(encoding='utf-8'); t=re.sub(r'<meta name="robots" content="[^"]+">','',t,count=1); anchor='<meta name="theme-color" content="#13263a">'; t=t.replace(anchor,anchor+'<meta name="robots" content="noindex,nofollow">',1); D.write_text(t,encoding='utf-8')
    pages=list(R.glob('*.html'))
    for f in ('servicios','productos','sectores','perspectivas'): pages+=list((R/f).glob('*.html'))
    for p in pages:
        x=p.read_text(encoding='utf-8').replace('<html lang="es">','<html lang="es-CO">',1); p.write_text(x,encoding='utf-8')
    x=M.read_text(encoding='utf-8'); x=re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>',f'<lastmod>{DATE}</lastmod>',x); M.write_text(x,encoding='utf-8')

def main():
    patch_index(); patch_js(); patch_misc(); print(f'Calidad final v{VER} aplicada: static-first, accesibilidad, SEO y performance.'); return 0
if __name__=='__main__': raise SystemExit(main())

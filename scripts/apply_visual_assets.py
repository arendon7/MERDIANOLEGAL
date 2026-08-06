#!/usr/bin/env python3
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
VERSION=json.loads((ROOT/'version.json').read_text(encoding='utf-8'))['version']
STYLE='<link rel="stylesheet" href="{p}visual-v39.css">'
SCRIPT='<script src="{p}visual-v39.js"></script>'
ROOT_PAGES=['index.html','firma.html','perspectivas.html','experiencia.html','demo.html','404.html','aviso-legal.html','privacidad.html','terminos.html']
NESTED=list((ROOT/'servicios').glob('*.html'))+list((ROOT/'productos').glob('*.html'))+list((ROOT/'sectores').glob('*.html'))+list((ROOT/'perspectivas').glob('*.html'))

def patch(path,prefix=''):
    text=path.read_text(encoding='utf-8')
    text=text.replace(f'{prefix}assets/logo-meridiano-v3-light.svg',f'{prefix}assets/brand/meridiano-logo-horizontal-light.svg')
    text=text.replace(f'{prefix}assets/logo-meridiano-v3.svg',f'{prefix}assets/brand/meridiano-logo-horizontal-dark.svg')
    text=text.replace(f'{prefix}assets/logo-meridiano.svg',f'{prefix}assets/brand/meridiano-logo-horizontal-dark.svg')
    text=re.sub(r'<link rel="icon"[^>]*>',f'<link rel="icon" href="{prefix}assets/brand/favicon.svg" type="image/svg+xml">',text,count=1)
    style=STYLE.format(p=prefix); script=SCRIPT.format(p=prefix)
    if style not in text: text=text.replace('</head>',f'  {style}\n</head>')
    if script not in text: text=text.replace('</body>',f'  {script}\n</body>')
    if path.name=='index.html':
        text=re.sub(r'<meta property="og:image" content="[^"]+">','<meta property="og:image" content="https://arendon7.github.io/MERDIANOLEGAL/assets/images/global/home-hero.webp">',text,count=1)
    path.write_text(text,encoding='utf-8')

for name in ROOT_PAGES:
    p=ROOT/name
    if p.exists(): patch(p,'')
for p in NESTED: patch(p,'../')

gen=ROOT/'scripts/build_catalog_shells.py'
if gen.exists():
    t=gen.read_text(encoding='utf-8')
    t=t.replace('../assets/hero-meridiano-v3.svg','../assets/images/global/home-hero.webp')
    t=t.replace('../assets/logo-meridiano-v3.svg','../assets/brand/meridiano-logo-horizontal-dark.svg')
    t=t.replace('../assets/logo-meridiano-v3-light.svg','../assets/brand/meridiano-logo-horizontal-light.svg')
    if '../visual-v39.css' not in t:
        t=t.replace('<link rel="stylesheet" href="../page-context.css">','<link rel="stylesheet" href="../page-context.css">\n  <link rel="stylesheet" href="../visual-v39.css">')
    if '../visual-v39.js' not in t:
        t=t.replace('<script src="../page-context.js"></script>','<script src="../page-context.js"></script>\n  <script src="../visual-v39.js"></script>')
    gen.write_text(t,encoding='utf-8')

manifest={"name":"Meridiano Legal","short_name":"Meridiano","description":"Dirección jurídica para empresas, innovación y proyectos regulados.","start_url":"./index.html","scope":"./","display":"standalone","background_color":"#f5f1e8","theme_color":"#13263a","lang":"es-CO","icons":[{"src":"assets/brand/favicon.svg","sizes":"any","type":"image/svg+xml","purpose":"any maskable"}]}
(ROOT/'manifest.webmanifest').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Identidad visual v{VERSION} aplicada.')

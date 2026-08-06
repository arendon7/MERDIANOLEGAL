#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'version.json').read_text(encoding='utf-8'))['version']
STYLE = '<link rel="stylesheet" href="{p}visual-v39.css">'
SCRIPT = '<script src="{p}visual-v39.js"></script>'
ROOT_PAGES = [
    'index.html', 'firma.html', 'perspectivas.html', 'experiencia.html',
    'demo.html', '404.html', 'aviso-legal.html', 'privacidad.html', 'terminos.html'
]
NESTED = (
    list((ROOT / 'servicios').glob('*.html'))
    + list((ROOT / 'productos').glob('*.html'))
    + list((ROOT / 'sectores').glob('*.html'))
    + list((ROOT / 'perspectivas').glob('*.html'))
)


def remove_managed_tag(text: str, tag: str) -> str:
    """Elimina una copia previa sin alterar el resto de la línea o del documento."""
    for candidate in (f'  {tag}\n', f'{tag}\n', f'  {tag}', tag):
        text = text.replace(candidate, '')
    return text


def patch(path: Path, prefix: str = '') -> None:
    text = path.read_text(encoding='utf-8')
    text = text.replace(
        f'{prefix}assets/logo-meridiano-v3-light.svg',
        f'{prefix}assets/brand/meridiano-logo-horizontal-light.svg',
    )
    text = text.replace(
        f'{prefix}assets/logo-meridiano-v3.svg',
        f'{prefix}assets/brand/meridiano-logo-horizontal-dark.svg',
    )
    text = text.replace(
        f'{prefix}assets/logo-meridiano.svg',
        f'{prefix}assets/brand/meridiano-logo-horizontal-dark.svg',
    )
    text = re.sub(
        r'<link rel="icon"[^>]*>',
        f'<link rel="icon" href="{prefix}assets/brand/favicon.svg" type="image/svg+xml">',
        text,
        count=1,
    )

    style = STYLE.format(p=prefix)
    script = SCRIPT.format(p=prefix)
    text = remove_managed_tag(text, style)
    text = remove_managed_tag(text, script)
    text = text.replace('</head>', f'  {style}\n</head>', 1)
    text = text.replace('</body>', f'  {script}\n</body>', 1)

    if path.name == 'index.html':
        text = re.sub(
            r'<meta property="og:image" content="[^"]+">',
            '<meta property="og:image" content="https://arendon7.github.io/MERDIANOLEGAL/assets/images/global/home-hero.webp">',
            text,
            count=1,
        )
    path.write_text(text, encoding='utf-8')


for name in ROOT_PAGES:
    page = ROOT / name
    if page.exists():
        patch(page)
for page in NESTED:
    patch(page, '../')

# El generador conserva estructura y metadatos. La capa visual se aplica después,
# en una única posición canónica, para que las ejecuciones sean idempotentes.
generator = ROOT / 'scripts/build_catalog_shells.py'
if generator.exists():
    text = generator.read_text(encoding='utf-8')
    text = text.replace('../assets/hero-meridiano-v3.svg', '../assets/images/global/home-hero.webp')
    text = text.replace('../assets/logo-meridiano-v3.svg', '../assets/brand/meridiano-logo-horizontal-dark.svg')
    text = text.replace('../assets/logo-meridiano-v3-light.svg', '../assets/brand/meridiano-logo-horizontal-light.svg')
    text = remove_managed_tag(text, '<link rel="stylesheet" href="../visual-v39.css">')
    text = remove_managed_tag(text, '<script src="../visual-v39.js"></script>')
    generator.write_text(text, encoding='utf-8')

manifest = {
    'name': 'Meridiano Legal',
    'short_name': 'Meridiano',
    'description': 'Dirección jurídica para empresas, innovación y proyectos regulados.',
    'start_url': './index.html',
    'scope': './',
    'display': 'standalone',
    'background_color': '#f5f1e8',
    'theme_color': '#13263a',
    'lang': 'es-CO',
    'icons': [
        {
            'src': 'assets/brand/favicon.svg',
            'sizes': 'any',
            'type': 'image/svg+xml',
            'purpose': 'any maskable',
        }
    ],
}
(ROOT / 'manifest.webmanifest').write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
    encoding='utf-8',
)
print(f'Identidad visual v{VERSION} aplicada.')

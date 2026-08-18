#!/usr/bin/env python3
"""Valida la capa UX/UI v4.6 en las 16 fichas profundas."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = json.loads((ROOT / 'version.json').read_text(encoding='utf-8'))['version']
TARGETS = sorted((ROOT / 'servicios').glob('*.html')) + sorted((ROOT / 'productos').glob('*.html'))

COMMON_PAGE_MARKERS = {
    '../detail-v46.css',
    '../detail-v46.js',
    'DETAIL-V46-MOBILE:START',
    '../firma.html',
    '>Centro demo<',
    'href="#contacto">Presentar necesidad</a>',
    'class="detail-mobile-cta-v46"',
}

LEGACY_NAV_MARKERS = {
    'DETAIL-V46-NAV:START',
    'class="detail-toc-v46"',
    'href="#pregunta-title"',
    'href="#alcance-title"',
    'href="#entregables-title"',
    'href="#cronograma-title"',
    'href="#limites-title"',
    'href="#contacto-title"',
    '>Planes y precios<',
}

V6_NAV_MARKERS = {
    'class="v6-detail-nav"',
    'href="#v6-question"',
    'href="#v6-deliverables"',
    'href="#v6-perimeter"',
    'href="#v6-process"',
    'href="#v6-boundary"',
    'href="#v6-detail-depth"',
    '../index.html#v6-commercial-depth',
}

FORBIDDEN_HEADER_MARKERS = {
    '<div class="detail-header-actions"><a class="btn btn-outline" href="../index.html#servicios">Portafolio</a>',
    '<div class="detail-header-actions"><a class="btn btn-outline" href="../index.html#productos">Portafolio</a>',
    '<div class="detail-header-actions"><a class="btn btn-navy" href="../demo.html">Área de clientes</a>',
}


def validate() -> list[str]:
    errors: list[str] = []
    required_files = {
        'detail-v46.css',
        'detail-v46.js',
        'scripts/apply_detail_ux_v46.py',
        'scripts/validate_detail_ux_v46.py',
    }
    missing = sorted(path for path in required_files if not (ROOT / path).exists())
    if missing:
        return [f'Faltan archivos v4.6: {", ".join(missing)}']

    if len(TARGETS) != 16:
        errors.append(f'Se esperaban 16 fichas profundas y se encontraron {len(TARGETS)}')

    for path in TARGETS:
        text = path.read_text(encoding='utf-8')
        experience_v6 = 'data-experience-system="v6"' in text
        required = COMMON_PAGE_MARKERS | (V6_NAV_MARKERS if experience_v6 else LEGACY_NAV_MARKERS)
        for marker in sorted(required):
            if marker not in text:
                errors.append(f'{path.relative_to(ROOT)}: falta {marker!r}')
        for marker in FORBIDDEN_HEADER_MARKERS:
            if marker in text:
                errors.append(f'{path.relative_to(ROOT)}: conserva cabecera legada {marker!r}')
        if text.count('../detail-v46.css') != 1:
            errors.append(f'{path.relative_to(ROOT)}: detail-v46.css debe cargarse exactamente una vez')
        if text.count('../detail-v46.js') != 1:
            errors.append(f'{path.relative_to(ROOT)}: detail-v46.js debe cargarse exactamente una vez')
        if not experience_v6 and (text.count('DETAIL-V46-NAV:START') != 1 or text.count('DETAIL-V46-NAV:END') != 1):
            errors.append(f'{path.relative_to(ROOT)}: navegación v4.6 duplicada o incompleta')
        if text.count('DETAIL-V46-MOBILE:START') != 1 or text.count('DETAIL-V46-MOBILE:END') != 1:
            errors.append(f'{path.relative_to(ROOT)}: CTA móvil v4.6 duplicado o incompleto')
        if f'Ficha v{VERSION}' not in text:
            errors.append(f'{path.relative_to(ROOT)}: no refleja la versión pública {VERSION}')
        if experience_v6:
            nav_match = re.search(r'<nav class="v6-detail-nav"[\s\S]*?</nav>', text)
            if not nav_match or nav_match.group(0).count('<a ') != 6:
                errors.append(f'{path.relative_to(ROOT)}: la navegación ejecutiva v6 debe contener seis hitos')
        else:
            toc_match = re.search(r'<nav class="detail-toc-v46"[\s\S]*?</nav>', text)
            if not toc_match or toc_match.group(0).count('<a ') != 7:
                errors.append(f'{path.relative_to(ROOT)}: el índice ejecutivo debe contener seis hitos y un CTA')

    css = (ROOT / 'detail-v46.css').read_text(encoding='utf-8') if (ROOT / 'detail-v46.css').exists() else ''
    for marker in (
        '.detail-toc-v46', '.detail-toc-links-v46', '.detail-mobile-cta-v46',
        '.detail-heading', '.limits-intro', '@media(max-width:700px)', '@media print'
    ):
        if marker not in css:
            errors.append(f'detail-v46.css no contiene {marker}')

    js = (ROOT / 'detail-v46.js').read_text(encoding='utf-8') if (ROOT / 'detail-v46.js').exists() else ''
    for marker in ('IntersectionObserver', 'MutationObserver', 'aria-current', 'bindSections', 'decoratePhases'):
        if marker not in js:
            errors.append(f'detail-v46.js no contiene {marker}')

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print('VALIDACIÓN UX/UI PROFUNDA v4.6 FALLIDA')
        for error in errors:
            print(f'- {error}')
        return 1
    print(f'VALIDACIÓN UX/UI PROFUNDA OK: 16 fichas con navegación ejecutiva, CTA contextual, responsive y versión {VERSION}; Experience v6 compatible cuando aplica.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Materializa Wave 6 v6 sobre las siete superficies públicas restantes.

La operación es deliberadamente conservadora: añade el sistema visual/semántico v6,
refuerza la frontera demostrativa y mejora recuperación 404 sin reescribir contenido
institucional, legal ni lógica interactiva existente.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STYLES = [
    "assets/css/v6/tokens.css",
    "assets/css/v6/base.css",
    "assets/css/v6/components.css",
    "assets/css/v6/surfaces.css",
    "assets/css/v6/final-surfaces.css",
]
TARGETS = {
    "firma.html": "firm",
    "experiencia.html": "experience",
    "demo.html": "demo",
    "aviso-legal.html": "legal:notice",
    "privacidad.html": "legal:privacy",
    "terminos.html": "legal:terms",
    "404.html": "404",
}
BOUNDARY_START = "<!-- EXPERIENCE-V60-DEMO-BOUNDARY:START -->"
BOUNDARY_END = "<!-- EXPERIENCE-V60-DEMO-BOUNDARY:END -->"
RECOVERY_START = "<!-- EXPERIENCE-V60-404-RECOVERY:START -->"
RECOVERY_END = "<!-- EXPERIENCE-V60-404-RECOVERY:END -->"


def e(value: object) -> str:
    return escape(str(value), quote=True)


def ensure_styles(text: str) -> str:
    for href in STYLES:
        text = re.sub(rf'(?m)^\s*<link rel="stylesheet" href="{re.escape(href)}">\s*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("superficie final sin </head>")
    links = "\n".join(f'  <link rel="stylesheet" href="{href}">' for href in STYLES)
    return text.replace("</head>", f"{links}\n</head>", 1)


def mark_body(text: str, surface: str) -> str:
    def repl(match: re.Match[str]) -> str:
        tag = match.group(0)
        for attr in ("data-experience-system", "data-experience-wave", "data-experience-surface"):
            tag = re.sub(rf'\s{attr}="[^"]*"', "", tag)
        return tag[:-1] + f' data-experience-system="v6" data-experience-wave="final" data-experience-surface="{e(surface)}">'
    result, count = re.subn(r"<body\b[^>]*>", repl, text, count=1)
    if count != 1:
        raise RuntimeError(f"{surface}: falta body")
    return result


def remove_managed(text: str, start: str, end: str) -> str:
    return re.sub(re.escape(start) + r".*?" + re.escape(end), "", text, flags=re.S)


def demo_boundary(kind: str) -> str:
    if kind == "experience":
        intro = "Experiencia demostrativa · método y flujo"
        title = "Este recorrido muestra cómo trabaja Meridiano; no habilita un portal productivo."
        facts = [
            ("Datos ficticios", "Escenarios, nombres, cifras y resultados son exclusivamente demostrativos."),
            ("Procesamiento local", "El simulador opera en el navegador y no envía la hipótesis a un servidor."),
            ("Sin relación profesional", "Explorar la experiencia no crea una relación abogado-cliente ni una propuesta vinculante."),
        ]
    else:
        intro = "Demo ficticia · Meridiano Empresas"
        title = "Interfaz demostrativa, sin usuarios, archivos ni operaciones reales."
        facts = [
            ("Perfiles ficticios", "Las credenciales y organizaciones existen únicamente para recorrer la demostración."),
            ("Sin carga real", "Los controles de archivos y documentos no reciben información productiva."),
            ("Sin servidor", "La experiencia se ejecuta localmente y no autentica cuentas reales."),
        ]
    items = "".join(f'<div><strong>{e(label)}</strong><span>{e(copy)}</span></div>' for label, copy in facts)
    return f'''{BOUNDARY_START}
<section class="v6-demo-boundary" aria-label="Condiciones de la demostración"><div class="v6-demo-boundary-inner"><div class="v6-demo-boundary-intro"><span class="v6-demo-kicker">{e(intro)}</span><strong>{e(title)}</strong></div>{items}</div></section>
{BOUNDARY_END}'''


def patch_demo_surface(text: str, kind: str) -> str:
    text = remove_managed(text, BOUNDARY_START, BOUNDARY_END)
    block = demo_boundary(kind)
    result, count = re.subn(r"</header>\s*", "</header>\n" + block + "\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"{kind}: falta header")
    return result


def patch_404(text: str) -> str:
    text = remove_managed(text, RECOVERY_START, RECOVERY_END)
    actions = re.search(r'<div class="hero-actions">.*?</div>', text, flags=re.S)
    if not actions:
        raise RuntimeError("404: faltan acciones de recuperación")
    block = f'''{RECOVERY_START}
<div class="v6-recovery-links" aria-label="Rutas recomendadas"><a href="soluciones/index.html">Explorar soluciones</a><a href="perspectivas.html">Leer perspectivas</a><a href="firma.html">Conocer la firma</a></div>
{RECOVERY_END}'''
    after = re.sub(r"^\s*", "\n", text[actions.end():])
    return text[:actions.end()] + "\n" + block + after


def patch(path: Path, surface: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = ensure_styles(text)
    text = mark_body(text, surface)
    if surface in {"experience", "demo"}:
        text = patch_demo_surface(text, surface)
    elif surface == "404":
        text = patch_404(text)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    for relative, surface in TARGETS.items():
        path = ROOT / relative
        if not path.exists():
            raise RuntimeError(f"Wave 6: falta {relative}")
        patch(path, surface)
    print("EXPERIENCE V6 WAVE 6 OK: firma, experiencia, demo, 3 legales y 404 materializados sin alterar capacidades.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

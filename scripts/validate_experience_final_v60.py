#!/usr/bin/env python3
"""Valida Wave 6 v6: firma, experiencia/demo, legales y recuperación 404."""
from __future__ import annotations

from pathlib import Path
import re
import sys

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


def fail(message: str) -> None:
    raise AssertionError(message)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def assert_once(value: str, needle: str, label: str) -> None:
    count = value.count(needle)
    if count != 1:
        fail(f"{label}: esperaba 1 ocurrencia de {needle!r}; encontró {count}")


def validate_common(relative: str, surface: str) -> str:
    value = read(relative)
    for needle in (
        'data-experience-system="v6"',
        'data-experience-wave="final"',
        f'data-experience-surface="{surface}"',
    ):
        if needle not in value:
            fail(f"{relative}: falta {needle}")
    for href in STYLES:
        assert_once(value, f'href="{href}"', f"{relative}: estilos v6")
    return value


def validate_firm(value: str) -> None:
    for needle in (
        "PROFESSIONAL-AUTHORITY-V525-FIRM:START",
        "Agustín Rendón Calle",
        "Universidad EAFIT · 2018",
        "no implica que todas las organizaciones o asuntos hayan sido clientes de la firma",
        "EDITORIAL-SEO:START",
        "EDITORIAL-JOURNEY:START",
    ):
        if needle not in value:
            fail(f"firma.html: falta {needle!r}")
    assert_once(value, "PROFESSIONAL-AUTHORITY-V525-FIRM:START", "firma autoridad")
    if re.search(r"<form\b", value):
        fail("firma.html no debe crear formularios")


def validate_experience(value: str) -> None:
    assert_once(value, BOUNDARY_START, "experiencia frontera")
    assert_once(value, BOUNDARY_END, "experiencia frontera")
    for needle in (
        '<meta name="robots" content="noindex,follow">',
        "Todos los escenarios, nombres, cifras y resultados son ficticios",
        "El simulador opera en el navegador y no envía la hipótesis a un servidor",
        'id="scope-simulator"',
        'id="simulator-result"',
        'id="recorrido"', 'id="entregables"', 'id="caso"', 'id="simulador"',
        "no crea una relación abogado-cliente",
    ):
        if needle not in value:
            fail(f"experiencia.html: falta frontera/función {needle!r}")
    if value.count('id="scope-simulator"') != 1:
        fail("experiencia.html: simulador debe permanecer único")


def validate_demo(value: str) -> None:
    assert_once(value, BOUNDARY_START, "demo frontera")
    assert_once(value, BOUNDARY_END, "demo frontera")
    robots = re.findall(r'<meta\s+name="robots"\s+content="([^"]+)"', value, flags=re.I)
    if len(robots) != 1 or robots[0].replace(" ", "").lower() != "noindex,nofollow":
        fail(f"demo.html: robots inválido {robots}")
    for needle in (
        'data-capability-v521="demo-only"',
        "DEMO FICTICIA",
        "Portal demostrativo",
        "no se envía a ningún servidor",
        'id="login-form"',
        'id="portal-view"',
        'id="ticket-form"',
        "Interfaz demostrativa, sin usuarios, archivos ni operaciones reales.",
    ):
        if needle not in value:
            fail(f"demo.html: falta frontera/función {needle!r}")


def validate_legal(relative: str, value: str) -> None:
    if value.count('class="legal-document"') != 1:
        fail(f"{relative}: documento legal debe ser único")
    if len(re.findall(r"<h2\b", value)) < 8:
        fail(f"{relative}: contenido legal parece truncado")
    for link in ("privacidad.html", "terminos.html", "aviso-legal.html", "index.html#contacto"):
        if link not in value:
            fail(f"{relative}: falta navegación legal {link}")
    if re.search(r"<form\b", value):
        fail(f"{relative}: documento legal no debe contener formularios")
    if relative == "privacidad.html":
        for needle in (
            "no existen cuentas reales de clientes",
            "El formulario de contacto se procesa localmente en el navegador",
            "La analítica de terceros se encuentra actualmente desactivada",
        ):
            if needle not in value:
                fail(f"privacidad.html: falta {needle!r}")
    if relative == "terminos.html" and "la demo no autentica usuarios reales" not in value.lower():
        fail("terminos.html: se perdió frontera del portal demostrativo")


def validate_404(value: str) -> None:
    assert_once(value, RECOVERY_START, "404 recuperación")
    assert_once(value, RECOVERY_END, "404 recuperación")
    for href in ("soluciones/index.html", "perspectivas.html", "firma.html"):
        if f'href="{href}"' not in value:
            fail(f"404.html: falta ruta {href}")
    if '<meta name="robots" content="noindex">' not in value:
        fail("404.html debe conservar noindex")
    if re.search(r"<form\b", value):
        fail("404.html no debe crear formularios")


def main() -> int:
    values = {relative: validate_common(relative, surface) for relative, surface in TARGETS.items()}
    validate_firm(values["firma.html"])
    validate_experience(values["experiencia.html"])
    validate_demo(values["demo.html"])
    for relative in ("aviso-legal.html", "privacidad.html", "terminos.html"):
        validate_legal(relative, values[relative])
    validate_404(values["404.html"])
    print("VALIDATE EXPERIENCE V6 WAVE 6 OK: 7 superficies finales con autoridad, capability truth, lectura legal y recuperación intactas.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATE EXPERIENCE V6 WAVE 6 FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

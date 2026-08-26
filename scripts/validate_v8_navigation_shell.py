#!/usr/bin/env python3
"""Static fail-closed certification for the W5.0B global navigation shell."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

from v8_shell import load_model, render_footer, render_header

ROOT = Path(__file__).resolve().parents[1]
JS = ROOT / "assets/js/v8/navigation.js"
CSS = ROOT / "assets/css/v8/components.css"
INDEX = ROOT / "index.html"


class ShellParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: list[dict[str, str]] = []
        self.buttons: list[dict[str, str]] = []
        self.items: list[tuple[str, str, dict[str, str]]] = []
        self.text_parts: list[str] = []
        self.landmarks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag == "a":
            self.anchors.append(data)
        if tag == "button":
            self.buttons.append(data)
        if tag in {"header", "nav", "footer"}:
            self.landmarks.append(tag)
        item_id = data.get("data-ml-item-id") or data.get("data-ml-footer-id")
        if item_id:
            self.items.append((tag, item_id, data))

    def handle_data(self, data: str) -> None:
        clean = " ".join(data.split())
        if clean:
            self.text_parts.append(clean)


def fail(message: str) -> None:
    raise AssertionError(message)


def check_href(href: str) -> None:
    if href.startswith("#"):
        if href not in {"#contacto", "#sectores", "#soluciones"}:
            fail(f"anchor inesperado en shell: {href}")
        return
    if href.startswith(("http://", "https://", "mailto:", "tel:")):
        fail(f"W5.0B shell no debe introducir destino externo: {href}")
    path = ROOT / href.split("?", 1)[0].split("#", 1)[0]
    if not path.is_file():
        fail(f"href físico inexistente: {href}")


def main() -> int:
    model = load_model()
    header = render_header(model)
    footer = render_footer(model)
    markup = header + footer

    parser = ShellParser()
    parser.feed(markup)
    visible_text = " ".join(parser.text_parts)

    primary = [row[1] for row in model["navigation"]["primary"]]
    for label in primary:
        if label not in visible_text:
            fail(f"falta navegación primaria: {label}")
    for forbidden in ("Productos", "Planes", "Documentos", "LegalAIZ", "Oferta completa"):
        if forbidden in visible_text:
            fail(f"apareció categoría superior prohibida: {forbidden}")

    if "Portal clientes" in visible_text:
        fail("Portal clientes no puede renderizarse sin destino verificado")
    if "Hablar con Meridiano" not in visible_text or "Solicitar diagnóstico" not in visible_text:
        fail("faltan CTAs canónicos del shell")

    if parser.landmarks.count("header") != 1 or parser.landmarks.count("footer") != 1:
        fail("shell debe tener exactamente un header y un footer")
    if parser.landmarks.count("nav") < 2:
        fail("shell debe exponer navegación principal y secundaria semánticas")

    mega_buttons = [button for button in parser.buttons if "data-ml-mega-toggle" in button]
    if len(mega_buttons) != 1:
        fail("debe existir un único trigger de mega menú")
    mega_button = mega_buttons[0]
    if mega_button.get("aria-expanded") != "false" or mega_button.get("aria-controls") != "ml-mega-menu":
        fail("trigger de mega menú carece de estado ARIA inicial correcto")

    mobile_buttons = [button for button in parser.buttons if "data-ml-menu-toggle" in button]
    if len(mobile_buttons) != 1:
        fail("debe existir un único trigger de menú mobile")
    mobile_button = mobile_buttons[0]
    if mobile_button.get("aria-expanded") != "false" or mobile_button.get("aria-controls") != "ml-nav-panel":
        fail("trigger mobile carece de estado ARIA inicial correcto")

    header_item_rows = [entry for entry in parser.items if "data-ml-item-id" in entry[2]]
    header_ids = [entry[1] for entry in header_item_rows]
    expected_ids = [
        row[0]
        for rows in model["navigation"]["mega_groups"].values()
        for row in rows
    ]
    if header_ids != expected_ids:
        fail(f"mega menu no conserva orden/IDs 6+8+2: {header_ids}")
    if len(header_ids) != 16 or len(set(header_ids)) != 16:
        fail("mega menu debe contener 16 IDs únicos")

    rc02_rows = [entry for entry in header_item_rows if entry[1] == "RC02"]
    if len(rc02_rows) != 1:
        fail("RC02 debe aparecer exactamente una vez en mega menu")
    rc02_tag, _code, rc02_attrs = rc02_rows[0]
    if rc02_tag == "a" or "href" in rc02_attrs:
        fail("RC02 no puede ser enlace antes de materialización")
    if rc02_attrs.get("data-ml-capability-status") != "owner-confirmed":
        fail("RC02 debe declarar capability owner-confirmed sin URL inventada")

    for anchor in parser.anchors:
        href = anchor.get("href")
        if not href:
            fail(f"anchor sin href: {anchor}")
        check_href(href)

    # No-JS fallback must remain a real link while JS uses a button.
    fallback_links = [a for a in parser.anchors if "ml-nav-fallback" in a.get("class", "")]
    if len(fallback_links) != 1 or fallback_links[0].get("href") != "#soluciones":
        fail("Qué hacemos necesita fallback no-JS a #soluciones")

    js = JS.read_text(encoding="utf-8")
    required_js = (
        "root.classList.add('ml-js')",
        "data-ml-shell",
        "data-ml-menu-toggle",
        "data-ml-mega-toggle",
        "event.key === 'Escape'",
        "event.key !== 'Tab'",
        "aria-expanded",
        "requestAnimationFrame",
        "matchMedia('(max-width: 959px)')",
        "ml-nav-open",
    )
    for marker in required_js:
        if marker not in js:
            fail(f"navigation.js omite comportamiento requerido: {marker}")
    for forbidden in ("eval(", "new Function", "localStorage", "sessionStorage", "document.cookie"):
        if forbidden in js:
            fail(f"navigation.js introduce API prohibida: {forbidden}")

    css = CSS.read_text(encoding="utf-8")
    required_css = (
        ".ml-site-header",
        ".ml-header-inner",
        ".ml-primary-nav",
        ".ml-mega",
        ".ml-mega-grid",
        ".ml-menu-toggle",
        ".ml-nav-panel",
        ".ml-site-footer",
        ".ml-footer-grid",
        ".ml-js .ml-nav-trigger",
        ".ml-nav-open",
        "min-height: 44px",
        "@media (max-width: 959px)",
    )
    for marker in required_css:
        if marker not in css:
            fail(f"components.css omite shell requirement: {marker}")

    index = INDEX.read_text(encoding="utf-8")
    if "data-ml-shell" in index or "assets/js/v8/navigation.js" in index:
        fail("W5.0B no puede persistir shell en index.html antes de W5.0C/D")

    if len(list(ROOT.rglob("*.html"))) != 49:
        fail("W5.0B debe preservar baseline físico de 49 HTML")

    print("VALIDATE V8 W5 NAVIGATION SHELL OK: semantic desktop/mobile shell; 6+8+2; RC02 non-link; keyboard/Escape/focus contract; Home untouched.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 W5 NAVIGATION SHELL FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

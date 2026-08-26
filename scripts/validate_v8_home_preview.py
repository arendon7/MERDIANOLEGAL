#!/usr/bin/env python3
"""Fail-closed static validation for the ephemeral W5.0C Home preview."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import sys
from urllib.parse import urlsplit

from render_v8_home import render_home
from v8_shell import load_model

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_HOME = ROOT / "index.html"
PREVIEW_DIR = ROOT / ".w5-preview"
EXPECTED_SECTIONS = [f"H{i:02d}" for i in range(1, 13)]
EXPECTED_STYLES = [
    "../assets/css/v8/tokens.css",
    "../assets/css/v8/base.css",
    "../assets/css/v8/components.css",
    "../assets/css/v8/surfaces.css",
]
EXPECTED_SCRIPTS = ["../assets/js/v8/navigation.js"]


class PreviewParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1 = 0
        self.forms = 0
        self.sections: list[str] = []
        self.links: list[str] = []
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.meta_robots: list[str] = []
        self.canonicals: list[str] = []
        self.inline_styles = 0
        self.inline_scripts = 0
        self._script_src_stack: list[bool] = []
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if tag == "h1":
            self.h1 += 1
        if tag == "form":
            self.forms += 1
        if data.get("data-v8-home-section"):
            self.sections.append(data["data-v8-home-section"])
        if tag == "a" and data.get("href"):
            self.links.append(data["href"])
        if tag == "link" and data.get("rel") == "stylesheet":
            self.styles.append(data.get("href", ""))
        if tag == "link" and data.get("rel") == "canonical":
            self.canonicals.append(data.get("href", ""))
        if tag == "script":
            src = data.get("src", "")
            self._script_src_stack.append(bool(src))
            if src:
                self.scripts.append(src)
        if tag == "style":
            self.inline_styles += 1
        if tag == "meta" and data.get("name") == "robots":
            self.meta_robots.append(data.get("content", ""))

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self._script_src_stack:
            self._script_src_stack.pop()

    def handle_data(self, data: str) -> None:
        if self._script_src_stack and not self._script_src_stack[-1] and data.strip():
            self.inline_scripts += 1
        clean = " ".join(data.split())
        if clean:
            self.text.append(clean)


def fail(message: str) -> None:
    raise AssertionError(message)


def local_target(href: str) -> Path | None:
    parts = urlsplit(href)
    if parts.scheme or parts.netloc or href.startswith(("mailto:", "tel:")):
        return None
    if not parts.path:
        return PREVIEW_DIR / "index.html"
    return (PREVIEW_DIR / parts.path).resolve()


def assert_fragment_exists(path: Path, fragment: str, href: str) -> None:
    if not fragment:
        return
    if not path.is_file():
        fail(f"fragment target missing for {href}")
    text = path.read_text(encoding="utf-8")
    quoted = f'id="{fragment}"'
    single = f"id='{fragment}'"
    if quoted not in text and single not in text:
        fail(f"fragment #{fragment} does not exist in {path.relative_to(ROOT)} for {href}")


def main() -> int:
    model = load_model()
    html = render_home(model, prefix="../", contact_href="../index.html#contacto")
    parser = PreviewParser()
    parser.feed(html)

    if parser.h1 != 1:
        fail(f"preview must contain exactly one h1; found {parser.h1}")
    if parser.forms != 0:
        fail("ephemeral Home preview must not duplicate the canonical contact form")
    if parser.sections != EXPECTED_SECTIONS:
        fail(f"preview section order drifted: {parser.sections}")
    if parser.meta_robots != ["noindex,nofollow"]:
        fail(f"preview robots must remain noindex,nofollow; got {parser.meta_robots}")
    if parser.canonicals:
        fail("ephemeral preview must not publish a canonical URL")
    if parser.styles != EXPECTED_STYLES:
        fail(f"preview must load only canonical v8 styles: {parser.styles}")
    if parser.scripts != EXPECTED_SCRIPTS:
        fail(f"preview must load only canonical v8 navigation JS: {parser.scripts}")
    if parser.inline_styles or parser.inline_scripts:
        fail("preview must not introduce inline style/script sedimentation")

    # Dark Home sections must use the actual v8 navy primitive. A historical
    # or invented dark class would silently fall back to a light background and
    # can turn otherwise-accessible inverse/gold text into an axe violation.
    if "ml-section--dark" in html:
        fail("preview uses undefined ml-section--dark instead of canonical ml-section--navy")
    for marker in (
        'class="ml-section ml-section--navy ml-home-method"',
        'class="ml-section ml-section--navy ml-home-final"',
    ):
        if marker not in html:
            fail(f"preview dark-section primitive drifted: {marker}")

    visible = " ".join(parser.text)
    required_text = (
        "Derecho empresarial para decisiones que necesitan avanzar.",
        "Meridiano Contratos",
        "futuras generaciones",
        "revisión jurídica humana",
        "Una función jurídica integrada a su empresa.",
        "Cobertura",
        "Complejidad",
        "Prioridad",
        "SLA / nivel de servicio",
        "Gobierno y reporting",
    )
    for marker in required_text:
        if marker not in visible:
            fail(f"preview omits required content/guardrail: {marker}")

    if "Portal clientes" in visible:
        fail("preview cannot expose Portal clientes without verified destination")
    if "/servicios-continuos/meridiano-contratos.html" in html:
        fail("RC02 target must not be linked or serialized into preview HTML")

    # RC01 may explain that hours are not the commercial frame, but cannot offer
    # a numeric/public hour package.
    lowered = visible.lower()
    forbidden_public_offers = (
        "10 horas al mes",
        "20 horas al mes",
        "40 horas al mes",
        "bolsa mensual de horas",
        "paquete de horas",
    )
    for marker in forbidden_public_offers:
        if marker in lowered:
            fail(f"preview exposes forbidden RC01 hour-package framing: {marker}")

    canonical = CANONICAL_HOME.read_text(encoding="utf-8")
    if canonical.count('id="contact-form"') != 1:
        fail("canonical production Home must keep exactly one physical contact form")
    if 'id="contacto"' not in canonical:
        fail("canonical Home lost #contacto target used by ephemeral preview")
    if 'data-v8-home-shell="candidate"' in canonical or model["home"]["hero"]["title"] in canonical:
        fail("W5 Home was persisted into index.html before Browser/Axe gate")

    allowed_local_anchors = {"#contenido", "#soluciones", "#sectores"}
    for href in parser.links:
        if href.startswith("#"):
            if href not in allowed_local_anchors:
                fail(f"unexpected preview-local anchor: {href}")
            continue
        target = local_target(href)
        if target is None:
            fail(f"ephemeral preview introduced external/contact URL: {href}")
        parts = urlsplit(href)
        if not target.is_file():
            try:
                shown = target.relative_to(ROOT)
            except ValueError:
                shown = target
            fail(f"preview href does not resolve physically: {href} -> {shown}")
        assert_fragment_exists(target, parts.fragment, href)

    if len(list(ROOT.rglob("*.html"))) != 49:
        fail("W5.0C source tree must remain at the certified 49 HTML baseline")

    print("VALIDATE V8 W5 HOME PREVIEW OK: H01-H12; canonical navy dark sections; one H1; no duplicate form; v8-only assets; all links resolve; RC02 non-linked; production Home untouched.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"VALIDATE V8 W5 HOME PREVIEW FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

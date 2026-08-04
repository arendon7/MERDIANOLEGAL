#!/usr/bin/env python3
"""Valida integridad, rutas y activos canónicos del sitio Meridiano Legal."""

from __future__ import annotations

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(ROOT.glob("*.html"))
REQUIRED_FILES = {
    "index.html", "demo.html", "experiencia.html", "404.html",
    "styles.css", "site-v3.css", "enhancements.css", "autocontenida.css", "experiencia.css",
    "app.js", "site-v3.js", "enhancements.js", "demo.js", "experiencia.js",
    "manifest.webmanifest", "version.json", "robots.txt", "sitemap.xml",
    "assets/logo-meridiano.svg", "assets/logo-meridiano-v3.svg", "assets/logo-meridiano-v3-light.svg",
    "assets/hero-meridiano.svg", "assets/hero-meridiano-v3.svg",
    "assets/decision-map.svg", "assets/route-meridiano-v3.svg",
}
CANONICAL_INDEX_MARKERS = {
    "Dirección jurídica para empresas que avanzan",
    "assets/logo-meridiano-v3.svg",
    "assets/hero-meridiano-v3.svg",
    "assets/route-meridiano-v3.svg",
    "site-v3.css",
    "site-v3.js",
    "Diagnóstico Jurídico Empresarial",
    "Dirección Jurídica Externa",
    "Tecnología e inteligencia artificial",
    "Legal Operations",
    "Economía circular y aseo",
    "Meridiano Empresas",
}
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.routes: list[str] = []
        self.references: list[tuple[str, str, int]] = []
        self.images_without_alt: list[int] = []
        self.has_lang = False
        self.has_charset = False
        self.has_viewport = False
        self.has_title = False
        self._inside_title = False
        self._title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html" and values.get("lang", "").strip(): self.has_lang = True
        if tag == "meta" and "charset" in values: self.has_charset = True
        if tag == "meta" and values.get("name", "").lower() == "viewport": self.has_viewport = True
        if tag == "title": self._inside_title = True
        if values.get("id"): self.ids.append(values["id"])
        if values.get("data-panel"): self.routes.append(values["data-panel"])
        if tag in {"a", "link"} and values.get("href"): self.references.append((tag, values["href"], self.getpos()[0]))
        if tag in {"img", "script", "source"} and values.get("src"): self.references.append((tag, values["src"], self.getpos()[0]))
        if tag == "img" and "alt" not in values: self.images_without_alt.append(self.getpos()[0])

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._inside_title = False
            self.has_title = bool("".join(self._title_text).strip())

    def handle_data(self, data: str) -> None:
        if self._inside_title: self._title_text.append(data)


def local_target(source: Path, reference: str) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme.lower() in IGNORED_SCHEMES or reference.startswith("//"): return None
    path = unquote(parsed.path)
    if not path or path == ".": return source
    if path.startswith("/"): raise ValueError("Ruta absoluta no compatible con GitHub Pages de proyecto")
    target = (source.parent / path).resolve()
    try: target.relative_to(ROOT.resolve())
    except ValueError as exc: raise ValueError("Referencia fuera del repositorio") from exc
    return target


def validate() -> list[str]:
    errors: list[str] = []
    missing = sorted(name for name in REQUIRED_FILES if not (ROOT / name).exists())
    if missing: errors.append(f"Faltan archivos requeridos: {', '.join(missing)}")

    index_path = ROOT / "index.html"
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8")
        missing_markers = sorted(marker for marker in CANONICAL_INDEX_MARKERS if marker not in index_text)
        if missing_markers: errors.append(f"index.html no corresponde a la portada canónica v3; faltan: {', '.join(missing_markers)}")

    if not HTML_FILES:
        errors.append("No se encontraron archivos HTML en la raíz")
        return errors

    parsed_pages: dict[Path, SiteParser] = {}
    for page in HTML_FILES:
        parser = SiteParser()
        try: parser.feed(page.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            errors.append(f"{page.name}: no está codificado en UTF-8")
            continue
        parsed_pages[page] = parser
        duplicates = [item for item, count in Counter(parser.ids).items() if count > 1]
        if duplicates: errors.append(f"{page.name}: IDs duplicados: {', '.join(sorted(duplicates))}")
        if not parser.has_lang: errors.append(f"{page.name}: falta atributo lang en <html>")
        if not parser.has_charset: errors.append(f"{page.name}: falta meta charset")
        if not parser.has_viewport: errors.append(f"{page.name}: falta meta viewport")
        if not parser.has_title: errors.append(f"{page.name}: falta un título no vacío")
        if parser.images_without_alt: errors.append(f"{page.name}: imágenes sin alt en líneas {', '.join(map(str, parser.images_without_alt))}")

    for page, parser in parsed_pages.items():
        own_targets = set(parser.ids) | set(parser.routes)
        for _tag, reference, line in parser.references:
            if reference.startswith("#"):
                anchor = unquote(reference[1:])
                if anchor and anchor not in own_targets: errors.append(f"{page.name}:{line}: ancla o ruta inexistente #{anchor}")
                continue
            try: target = local_target(page, reference)
            except ValueError as exc:
                errors.append(f"{page.name}:{line}: {reference!r}: {exc}")
                continue
            if target is None: continue
            if not target.exists():
                errors.append(f"{page.name}:{line}: recurso inexistente {reference!r}")
                continue
            fragment = unquote(urlsplit(reference).fragment)
            if fragment and target.suffix.lower() == ".html":
                target_parser = parsed_pages.get(target)
                if target_parser:
                    targets = set(target_parser.ids) | set(target_parser.routes)
                    if fragment not in targets: errors.append(f"{page.name}:{line}: ancla o ruta #{fragment} inexistente en {target.name}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors: print(f"- {error}")
        return 1
    print(f"VALIDACIÓN OK: {len(HTML_FILES)} páginas, portada v3 y recursos internos íntegros.")
    return 0


if __name__ == "__main__": sys.exit(main())

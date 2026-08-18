#!/usr/bin/env python3
"""Normaliza discovery SEO v6.2 sin inventar verificación ni señales temporales.

La fuente del sitemap son las páginas HTML indexables y su canonical autorreferencial.
Mientras Search Console no tenga un token auténtico en site-config.json, la Home no
publica meta de verificación. `--check` es fail-closed y no escribe.
"""
from __future__ import annotations

from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

from site_config import load_site_config

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/data/v6/search-discovery-readiness-v62.json"
PUBLIC_DIRS = ("servicios", "productos", "soluciones", "sectores", "perspectivas")
VERIFICATION_META = re.compile(
    r"\n?[ \t]*<meta\b(?=[^>]*\bname=[\"']google-site-verification[\"'])[^>]*>[ \t]*\n?",
    re.IGNORECASE,
)


class HeadSignals(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.canonicals: list[str] = []
        self.robots: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        lowered = tag.lower()
        if lowered == "head":
            self.in_head = True
            return
        if not self.in_head:
            return
        values = {str(key).lower(): (value or "") for key, value in attrs}
        if lowered == "link" and "canonical" in values.get("rel", "").lower().split():
            self.canonicals.append(values.get("href", "").strip())
        if lowered == "meta" and values.get("name", "").lower() == "robots":
            self.robots.append(values.get("content", "").strip().lower())

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "head":
            self.in_head = False


def public_html_targets() -> list[Path]:
    targets = list(ROOT.glob("*.html"))
    for folder in PUBLIC_DIRS:
        targets.extend((ROOT / folder).glob("*.html"))
    return sorted(set(targets), key=lambda path: path.relative_to(ROOT).as_posix())


def expected_self_url(path: Path, base_url: str) -> str:
    relative = path.relative_to(ROOT).as_posix()
    if relative == "index.html":
        return base_url
    if relative.endswith("/index.html"):
        return base_url + relative[: -len("index.html")]
    return base_url + relative


def page_signals(path: Path) -> HeadSignals:
    parser = HeadSignals()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def indexable_canonicals(base_url: str) -> list[tuple[Path, str]]:
    entries: list[tuple[Path, str]] = []
    errors: list[str] = []
    for path in public_html_targets():
        signals = page_signals(path)
        relative = path.relative_to(ROOT).as_posix()
        noindex = any("noindex" in {part.strip() for part in value.split(",")} for value in signals.robots)
        if noindex:
            if signals.canonicals:
                # Un canonical en una página noindex no la hace indexable; simplemente no entra al sitemap.
                pass
            continue
        if len(signals.canonicals) != 1:
            errors.append(f"{relative}: página indexable debe declarar exactamente un canonical y tiene {len(signals.canonicals)}")
            continue
        expected = expected_self_url(path, base_url)
        actual = signals.canonicals[0]
        if actual != expected:
            errors.append(f"{relative}: canonical no es autorreferencial; esperado {expected!r}, obtuvo {actual!r}")
            continue
        entries.append((path, actual))
    if errors:
        raise ValueError("\n".join(errors))
    return entries


def render_sitemap(base_url: str) -> str:
    entries = indexable_canonicals(base_url)
    urls = [url for _, url in entries]
    if len(urls) != len(set(urls)):
        raise ValueError("Existen canonicals duplicados entre páginas indexables")
    body = "\n".join(f"  <url><loc>{escape(url)}</loc></url>" for url in urls)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n"
        "</urlset>\n"
    )


def render_home(current: str, token: str) -> str:
    cleaned = VERIFICATION_META.sub("\n", current)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    if not token:
        return cleaned
    marker = '<meta name="google-site-verification" content="{}">'.format(token)
    referrer = '<meta name="referrer" content="strict-origin-when-cross-origin">'
    if referrer in cleaned:
        return cleaned.replace(referrer, referrer + "\n  " + marker, 1)
    head_end = cleaned.find("</head>")
    if head_end < 0:
        raise ValueError("index.html no contiene </head>")
    return cleaned[:head_end] + "  " + marker + "\n" + cleaned[head_end:]


def expected_texts() -> dict[str, str]:
    if not CONTRACT.exists():
        return {}
    config = load_site_config()
    expected = {
        "sitemap.xml": render_sitemap(config["base_url"]),
        "index.html": render_home(
            (ROOT / "index.html").read_text(encoding="utf-8"),
            config["search_console_verification"],
        ),
    }
    return expected


def pending_changes() -> list[str]:
    pending: list[str] = []
    for relative, expected in expected_texts().items():
        path = ROOT / relative
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != expected:
            pending.append(relative)
    return sorted(pending)


def apply() -> list[str]:
    expected = expected_texts()
    changed = pending_changes()
    for relative in changed:
        (ROOT / relative).write_text(expected[relative], encoding="utf-8")
    return changed


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    try:
        pending = pending_changes()
    except (ValueError, KeyError) as exc:
        print("SEARCH DISCOVERY V6.2 FAIL", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1
    if args == ["--check"]:
        if pending:
            print("SEARCH DISCOVERY DRIFT")
            for relative in pending:
                print(f"- {relative}")
            return 1
        print("SEARCH DISCOVERY V6.2 SYNC OK")
        return 0
    if args:
        raise SystemExit(f"uso: {Path(sys.argv[0]).name} [--check]")
    changed = apply()
    print("Search discovery v6.2 normalizado.")
    for relative in changed:
        print(f"- {relative}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""v5.0: consolida configuración pública, dominio, SEO y telemetría local sin terceros."""
from __future__ import annotations

from pathlib import Path
from html import escape
import json
import re

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
VERSION_DATA = json.loads((R / "version.json").read_text(encoding="utf-8"))
VERSION = VERSION_DATA["version"]
RELEASE_DATE = VERSION_DATA["release_date"]
BASE_URL = CONFIG["base_url"]
PUBLIC_PATH = CONFIG["public_path"]
LEGACY_BASES = {
    "https://arendon7.github.io/MERDIANOLEGAL/",
}
RUNTIME_A = "<!-- PRODUCTION-V50-RUNTIME:START -->"
RUNTIME_B = "<!-- PRODUCTION-V50-RUNTIME:END -->"
SEARCH_A = "<!-- PRODUCTION-V50-SEARCH:START -->"
SEARCH_B = "<!-- PRODUCTION-V50-SEARCH:END -->"
PRIVACY_A = "<!-- PRODUCTION-V50-PRIVACY:START -->"
PRIVACY_B = "<!-- PRODUCTION-V50-PRIVACY:END -->"
REFERRER_TAG = '<meta name="referrer" content="strict-origin-when-cross-origin">'


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def html_targets() -> list[Path]:
    targets = list(R.glob("*.html"))
    for folder in ("servicios", "productos", "sectores", "perspectivas"):
        targets.extend((R / folder).glob("*.html"))
    return sorted(set(targets))


def prefix_for(path: Path) -> str:
    relative = path.relative_to(R)
    return "../" if len(relative.parts) > 1 else ""


def public_relative(path: Path) -> str:
    relative = path.relative_to(R).as_posix()
    return "" if relative == "index.html" else relative


def managed_remove(text: str, start: str, end: str) -> str:
    return re.sub(
        re.escape(start) + r"[\s\S]*?" + re.escape(end) + r"\n?",
        "",
        text,
        count=1,
    )


def upsert_meta(text: str, name_or_property: str, value: str, *, prop: bool = False) -> str:
    attr = "property" if prop else "name"
    pattern = rf'<meta {attr}="{re.escape(name_or_property)}" content="[^"]*">'
    tag = f'<meta {attr}="{name_or_property}" content="{escape(value, quote=True)}">'
    if re.search(pattern, text):
        return re.sub(pattern, tag, text, count=1)
    return text.replace("</head>", f"  {tag}\n</head>", 1)


def normalize_referrer_meta(text: str) -> str:
    """Coloca la política referrer tras viewport con whitespace determinista."""
    text = re.sub(
        r'(?m)^[ \t]*<meta name="referrer" content="[^"]*">[ \t]*(?:\r?\n)?',
        "",
        text,
    )
    text = re.sub(r'<meta name="referrer" content="[^"]*">', "", text)
    updated, count = re.subn(
        r'(<meta name="viewport"[^>]*>)[ \t\r\n]*',
        lambda match: match.group(1) + "\n  " + REFERRER_TAG + "\n  ",
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("No se encontró meta viewport para ubicar política referrer")
    return updated


def upsert_canonical(text: str, url: str) -> str:
    tag = f'<link rel="canonical" href="{escape(url, quote=True)}">'
    if re.search(r'<link rel="canonical" href="[^"]*">', text):
        return re.sub(r'<link rel="canonical" href="[^"]*">', tag, text, count=1)
    return text.replace("</head>", f"  {tag}\n</head>", 1)


def patch_html(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for legacy in LEGACY_BASES:
        if legacy != BASE_URL:
            text = text.replace(legacy, BASE_URL)

    robots_match = re.search(r'<meta name="robots" content="([^"]+)">', text)
    noindex = bool(robots_match and "noindex" in robots_match.group(1).lower())
    if path.name == "404.html":
        noindex = True

    text = normalize_referrer_meta(text)
    if not noindex:
        canonical = BASE_URL + public_relative(path)
        text = upsert_canonical(text, canonical)
        text = upsert_meta(text, "og:url", canonical, prop=True)

    text = managed_remove(text, SEARCH_A, SEARCH_B)
    if path.name == "index.html":
        verification = CONFIG["search_console_verification"]
        if verification:
            block = (
                f"{SEARCH_A}\n"
                f'  <meta name="google-site-verification" content="{escape(verification, quote=True)}">\n'
                f"{SEARCH_B}"
            )
            text = text.replace("</head>", f"{block}\n</head>", 1)

    text = managed_remove(text, RUNTIME_A, RUNTIME_B)
    if not noindex:
        prefix = prefix_for(path)
        block = (
            f"{RUNTIME_A}\n"
            f'  <script defer src="{prefix}runtime-config.js"></script>\n'
            f'  <script defer src="{prefix}telemetry-v50.js"></script>\n'
            f"{RUNTIME_B}"
        )
        text = text.replace("</body>", f"{block}\n</body>", 1)

    path.write_text(text, encoding="utf-8")


def patch_page_context() -> None:
    path = R / "page-context.js"
    text = path.read_text(encoding="utf-8")
    for legacy in LEGACY_BASES:
        if legacy != BASE_URL:
            text = text.replace(legacy, BASE_URL)
    text, count = re.subn(
        r"const ROOT_PATH = [\"'][^\"']*[\"'];",
        f"const ROOT_PATH = {json.dumps(PUBLIC_PATH)};",
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("page-context.js: no se pudo sincronizar ROOT_PATH")
    path.write_text(text, encoding="utf-8")


def patch_privacy() -> None:
    path = R / "privacidad.html"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r'<div class="legal-meta"><span>Versión [^<]+</span><span>Actualizada: [^<]+</span><span>Colombia</span></div>',
        '<div class="legal-meta"><span>Versión 1.1</span><span>Actualizada: 8 de agosto de 2026</span><span>Colombia</span></div>',
        text,
        count=1,
    )
    text = re.sub(
        r'<div class="legal-callout"><strong>Alcance actual:</strong>.*?</div>',
        '<div class="legal-callout"><strong>Alcance actual:</strong> esta web pública es estática. El formulario no se almacena en un servidor de Meridiano Legal, no existen cuentas reales de clientes y la analítica de terceros permanece desactivada.</div>',
        text,
        count=1,
    )
    text = re.sub(
        r'<h2>5\. Funcionamiento del formulario</h2><p>.*?</p>',
        '<h2>5. Funcionamiento del formulario</h2><p>El formulario de contacto se procesa localmente en el navegador. Al continuar, la web prepara un mensaje con una referencia única y abre WhatsApp. El contenido no se considera enviado a Meridiano Legal hasta que la persona confirma el envío dentro de WhatsApp. Esta página no conserva una copia del formulario en un servidor propio.</p>',
        text,
        count=1,
    )
    text = re.sub(
        r'[ \t\r\n]*' + re.escape(PRIVACY_A) + r'[\s\S]*?' + re.escape(PRIVACY_B) + r'[ \t\r\n]*',
        "\n        ",
        text,
        count=1,
    )
    analytics_state = "desactivada" if not CONFIG["analytics"]["enabled"] else "habilitada"
    block = (
        f"{PRIVACY_A}<h2>5.1. Contexto de navegación e instrumentación técnica</h2>"
        "<p>La web puede utilizar <code>sessionStorage</code> únicamente para conservar durante la sesión el contexto de navegación comercial —por ejemplo, la solución o sector desde el que una persona llegó al formulario— y evitar que tenga que repetir ese recorrido. Esa información de contexto se elimina al finalizar la sesión del navegador según el funcionamiento del propio navegador.</p>"
        f"<p>La instrumentación técnica de conversión v5.0 mantiene eventos no identificadores únicamente en memoria del navegador para depuración y preparación de medición —por ejemplo, vista de página, apertura de un CTA o preparación de una referencia—. No utiliza cookies, <code>localStorage</code>, píxeles, <code>sendBeacon</code> ni transmite esos eventos a un proveedor externo. La analítica de terceros se encuentra actualmente {analytics_state}. Cualquier activación futura deberá reflejarse previamente en la configuración pública y en esta política.</p>"
        f"{PRIVACY_B}"
    )
    pattern = r'(<h2>5\. Funcionamiento del formulario</h2><p>.*?</p>)[ \t\r\n]*(?=<h2>6\. Autorización y libertad</h2>)'
    updated, count = re.subn(
        pattern,
        lambda match: match.group(1) + "\n        " + block + "\n        ",
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("privacidad.html: no se pudo normalizar el bloque 5.1")
    path.write_text(updated, encoding="utf-8")


def write_runtime_config() -> None:
    safe = {
        "name": CONFIG.get("name", "Meridiano Legal"),
        "baseUrl": BASE_URL,
        "publicPath": PUBLIC_PATH,
        "version": VERSION,
        "releaseDate": RELEASE_DATE,
        "environment": CONFIG.get("environment", "public"),
        "deployment": CONFIG.get("deployment", "github-pages"),
        "contact": CONFIG["contact"],
        "analytics": CONFIG["analytics"],
        "searchConsoleConfigured": bool(CONFIG["search_console_verification"]),
    }
    payload = json.dumps(safe, ensure_ascii=False, separators=(",", ":"))
    (R / "runtime-config.js").write_text(
        f"window.MERIDIANO_PUBLIC_CONFIG = Object.freeze({payload});\n",
        encoding="utf-8",
    )


def write_status() -> None:
    status = {
        "name": CONFIG.get("name", "Meridiano Legal"),
        "version": VERSION,
        "release_date": RELEASE_DATE,
        "environment": CONFIG.get("environment", "public"),
        "deployment": CONFIG.get("deployment", "github-pages"),
        "base_url": BASE_URL,
        "public_path": PUBLIC_PATH,
        "custom_domain": CONFIG["custom_domain"] or None,
        "analytics": "enabled" if CONFIG["analytics"]["enabled"] else "disabled",
        "contact_channel": "whatsapp",
        "demo_indexing": "noindex",
    }
    (R / "site-status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_robots() -> None:
    root = PUBLIC_PATH
    robots = (
        "User-agent: *\n"
        f"Allow: {root}\n"
        f"Disallow: {root}demo.html\n"
        f"Disallow: {root}docs/\n\n"
        f"Sitemap: {BASE_URL}sitemap.xml\n"
    )
    (R / "robots.txt").write_text(robots, encoding="utf-8")


def patch_sitemap() -> None:
    path = R / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    for legacy in LEGACY_BASES:
        if legacy != BASE_URL:
            text = text.replace(legacy, BASE_URL)
    path.write_text(text, encoding="utf-8")


def manage_cname() -> None:
    cname = R / "CNAME"
    domain = CONFIG["custom_domain"]
    if domain:
        cname.write_text(domain + "\n", encoding="utf-8")
    elif cname.exists():
        cname.unlink()


def main() -> int:
    if semver(VERSION) < (5, 0, 0):
        raise SystemExit("v5.0 requiere version.json >= 5.0.0")
    write_runtime_config()
    patch_page_context()
    patch_sitemap()
    write_robots()
    patch_privacy()
    for path in html_targets():
        patch_html(path)
    write_status()
    manage_cname()
    print(
        f"Producción v{VERSION} aplicada: configuración canónica, dominio-ready, "
        "canonical/OG, robots, status y telemetría local."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

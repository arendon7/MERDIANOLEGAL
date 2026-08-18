#!/usr/bin/env python3
"""Valida preparación de producción v5.0: configuración, dominio, SEO y telemetría."""
from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import sys

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
VERSION_DATA = json.loads((R / "version.json").read_text(encoding="utf-8"))
VERSION = VERSION_DATA["version"]
RELEASE_DATE = VERSION_DATA["release_date"]
BASE_URL = CONFIG["base_url"]
PUBLIC_PATH = CONFIG["public_path"]
errors: list[str] = []


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def html_targets() -> list[Path]:
    targets = list(R.glob("*.html"))
    for folder in ("servicios", "productos", "sectores", "perspectivas"):
        targets.extend((R / folder).glob("*.html"))
    return sorted(set(targets))


def public_relative(path: Path) -> str:
    relative = path.relative_to(R).as_posix()
    return "" if relative == "index.html" else relative


if semver(VERSION) < (5, 0, 0):
    errors.append(f"version.json debe ser >= 5.0.0 y registra {VERSION}")
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(RELEASE_DATE)):
    errors.append(f"version.json debe declarar release_date ISO y registra {RELEASE_DATE!r}")

for relative in (
    "site-config.json",
    "runtime-config.js",
    "telemetry-v50.js",
    "site-status.json",
    "scripts/site_config.py",
    "scripts/sync_public_version.py",
    "scripts/apply_production_v50.py",
    "scripts/validate_production_v50.py",
    "scripts/validate_live_v50.py",
):
    path = R / relative
    if not path.exists() or path.stat().st_size < 20:
        errors.append(f"Falta recurso v5.0 {relative}")

status_path = R / "site-status.json"
if status_path.exists():
    status = json.loads(status_path.read_text(encoding="utf-8"))
    expected_status = {
        "version": VERSION,
        "release_date": RELEASE_DATE,
        "base_url": BASE_URL,
        "public_path": PUBLIC_PATH,
        "analytics": "enabled" if CONFIG["analytics"]["enabled"] else "disabled",
        "contact_channel": "whatsapp",
        "demo_indexing": "noindex",
    }
    for key, expected in expected_status.items():
        if status.get(key) != expected:
            errors.append(f"site-status.json: {key}={status.get(key)!r}, se esperaba {expected!r}")

runtime = (R / "runtime-config.js").read_text(encoding="utf-8") if (R / "runtime-config.js").exists() else ""
for marker in (
    "window.MERIDIANO_PUBLIC_CONFIG",
    json.dumps(BASE_URL),
    json.dumps(PUBLIC_PATH),
    json.dumps(VERSION),
    json.dumps(RELEASE_DATE),
):
    if marker not in runtime:
        errors.append(f"runtime-config.js: falta {marker!r}")

telemetry = (R / "telemetry-v50.js").read_text(encoding="utf-8") if (R / "telemetry-v50.js").exists() else ""
for marker in ("meridiano:telemetry", "meridiano:lead-prepared", "page_view", "cta_click", "MeridianoTelemetry"):
    if marker not in telemetry:
        errors.append(f"telemetry-v50.js: falta {marker!r}")
for forbidden in ("fetch(", "XMLHttpRequest", "sendBeacon", "localStorage", "sessionStorage", "document.cookie"):
    if forbidden in telemetry:
        errors.append(f"telemetry-v50.js no debe usar {forbidden!r} en esta release")
if CONFIG["analytics"]["enabled"]:
    errors.append("v5.0 base debe mantener analítica de terceros desactivada hasta configurar proveedor y política")

page_context = (R / "page-context.js").read_text(encoding="utf-8")
if f"const ROOT_PATH = {json.dumps(PUBLIC_PATH)};" not in page_context:
    errors.append("page-context.js no usa public_path canónico")
if BASE_URL not in page_context:
    errors.append("page-context.js no usa base_url canónico")

sitemap = (R / "sitemap.xml").read_text(encoding="utf-8")
locations = re.findall(r"<loc>([^<]+)</loc>", sitemap)
if not locations:
    errors.append("sitemap.xml no contiene URLs")
for location in locations:
    if not location.startswith(BASE_URL):
        errors.append(f"sitemap.xml contiene URL fuera de base_url: {location}")
if any("demo.html" in location for location in locations):
    errors.append("sitemap.xml no debe incluir demo.html")

robots = (R / "robots.txt").read_text(encoding="utf-8")
for marker in (
    f"Allow: {PUBLIC_PATH}",
    f"Disallow: {PUBLIC_PATH}demo.html",
    f"Disallow: {PUBLIC_PATH}docs/",
    f"Sitemap: {BASE_URL}sitemap.xml",
):
    if marker not in robots:
        errors.append(f"robots.txt: falta {marker!r}")

for path in html_targets():
    text = path.read_text(encoding="utf-8")
    robots_match = re.search(r'<meta name="robots" content="([^"]+)">', text)
    noindex = path.name == "404.html" or bool(robots_match and "noindex" in robots_match.group(1).lower())
    if 'meta name="referrer" content="strict-origin-when-cross-origin"' not in text:
        errors.append(f"{path.relative_to(R)}: falta política referrer")
    if noindex:
        if path.name == "demo.html" and "noindex,nofollow" not in text:
            errors.append("demo.html debe conservar noindex,nofollow")
        continue
    canonical = BASE_URL + public_relative(path)
    if f'<link rel="canonical" href="{canonical}">' not in text:
        errors.append(f"{path.relative_to(R)}: canonical incorrecto")
    if f'<meta property="og:url" content="{canonical}">' not in text:
        errors.append(f"{path.relative_to(R)}: og:url incorrecto")
    if text.count("PRODUCTION-V50-RUNTIME:START") != 1:
        errors.append(f"{path.relative_to(R)}: bloque runtime v5.0 ausente o duplicado")
    prefix = "../" if len(path.relative_to(R).parts) > 1 else ""
    for script in (f'{prefix}runtime-config.js', f'{prefix}telemetry-v50.js'):
        if script not in text:
            errors.append(f"{path.relative_to(R)}: falta {script}")

index = (R / "index.html").read_text(encoding="utf-8")
if f"Web pública v{VERSION}" not in index:
    errors.append("index.html debe declarar Web pública con la versión vigente")
verification = CONFIG["search_console_verification"]
if verification:
    if index.count('name="google-site-verification"') != 1 or verification not in index:
        errors.append("index.html no publica la verificación Search Console configurada")
else:
    if 'name="google-site-verification"' in index:
        errors.append("index.html publica una verificación Search Console no configurada")

privacy = (R / "privacidad.html").read_text(encoding="utf-8")
for marker in (
    "Versión 1.1",
    "Contexto de navegación e instrumentación técnica",
    "sessionStorage",
    "No utiliza cookies",
    "analítica de terceros",
):
    if marker not in privacy:
        errors.append(f"privacidad.html: falta {marker!r}")

cname = R / "CNAME"
if CONFIG["custom_domain"]:
    if not cname.exists() or cname.read_text(encoding="utf-8").strip() != CONFIG["custom_domain"]:
        errors.append("CNAME no coincide con custom_domain")
else:
    if cname.exists():
        errors.append("CNAME no debe existir mientras custom_domain esté vacío")

legacy = "https://arendon7.github.io/MERDIANOLEGAL/"
if BASE_URL != legacy:
    for path in [*html_targets(), R / "page-context.js", R / "sitemap.xml", R / "robots.txt"]:
        if legacy in path.read_text(encoding="utf-8"):
            errors.append(f"{path.relative_to(R)} conserva base URL histórica")

for js in ("runtime-config.js", "telemetry-v50.js", "page-context.js"):
    result = subprocess.run(["node", "--check", str(R / js)], capture_output=True, text=True)
    if result.returncode != 0:
        errors.append(f"{js} no supera node --check: {result.stderr.strip()}")

if errors:
    print("VALIDACIÓN DE PRODUCCIÓN V5.0 FALLIDA", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(
    f"VALIDACIÓN DE PRODUCCIÓN V5.0 OK: {VERSION} ({RELEASE_DATE}), configuración canónica, "
    "dominio-ready, SEO, privacidad y telemetría local íntegros."
)

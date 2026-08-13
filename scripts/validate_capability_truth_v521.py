#!/usr/bin/env python3
"""Valida v5.21: ninguna superficie demostrativa puede presentarse como capacidad productiva."""
from __future__ import annotations

from html import unescape
from pathlib import Path
import json
import re
import sys

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "0.0.0")
errors: list[str] = []
DEMO_LINK = re.compile(r'<a\b[^>]*\bhref=["\'](?:\.\./)?demo\.html(?:#[^"\']*)?["\'][^>]*>([\s\S]*?)</a>', re.I)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def is_noindex(text: str) -> bool:
    match = re.search(r'<meta name="robots" content="([^"]+)">', text, re.I)
    return bool(match and "noindex" in match.group(1).lower())


def visible_text(fragment: str) -> str:
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def indexable_html_targets() -> list[Path]:
    targets = list(R.glob("*.html"))
    for folder in ("servicios", "productos", "sectores", "perspectivas", "soluciones"):
        targets.extend((R / folder).glob("*.html"))
    result: list[Path] = []
    for path in sorted(set(targets)):
        text = path.read_text(encoding="utf-8")
        if path.name == "404.html" or is_noindex(text):
            continue
        result.append(path)
    return result


if semver(VERSION) < (5, 21, 0):
    errors.append(f"version.json debe ser >= 5.21.0 y registra {VERSION}")

portal = CONFIG["capabilities"]["client_portal"]

runtime_path = R / "runtime-config.js"
runtime = runtime_path.read_text(encoding="utf-8") if runtime_path.exists() else ""
expected_runtime = json.dumps(
    {"clientPortal": {"enabled": portal["enabled"], "url": portal["url"]}},
    ensure_ascii=False,
    separators=(",", ":"),
)
if '"capabilities":' not in runtime or expected_runtime not in runtime:
    errors.append("runtime-config.js no publica el estado canónico de clientPortal")

status_path = R / "site-status.json"
status = json.loads(status_path.read_text(encoding="utf-8")) if status_path.exists() else {}
expected_state = "enabled" if portal["enabled"] else "disabled"
if status.get("client_portal") != expected_state:
    errors.append(f"site-status.json: client_portal debe ser {expected_state!r}")
if status.get("client_portal_url") != (portal["url"] or None):
    errors.append("site-status.json: client_portal_url no coincide con site-config.json")

demo = (R / "demo.html").read_text(encoding="utf-8")
for marker in (
    'content="noindex,nofollow"',
    'data-capability-v521="demo-only"',
    "DEMO FICTICIA",
    "Portal demostrativo",
    "no se envía a ningún servidor",
):
    if marker not in demo:
        errors.append(f"demo.html: falta frontera demostrativa {marker!r}")

public_demo_links = 0
portal_links = 0
for path in indexable_html_targets():
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(R)
    if not portal["enabled"] and re.search(r">\s*Área de clientes\s*<", text, re.I):
        errors.append(f"{relative}: no puede presentar Área de clientes mientras el portal real está deshabilitado")
    for match in DEMO_LINK.finditer(text):
        public_demo_links += 1
        label = visible_text(match.group(1))
        if not re.search(r"\bdemo(?:strativ[oa])?\b", label, re.I):
            errors.append(f"{relative}: enlace a demo sin etiqueta demostrativa explícita: {label!r}")
    if portal["enabled"] and portal["url"]:
        portal_links += text.count(f'href="{portal["url"]}"') + text.count(f"href='{portal['url']}'")

if public_demo_links < 1:
    errors.append("Debe existir al menos un acceso público explícitamente etiquetado a la demostración")

if portal["enabled"]:
    if portal_links < 1:
        errors.append("client_portal.enabled=true exige al menos un enlace público al portal HTTPS configurado")
else:
    privacy = (R / "privacidad.html").read_text(encoding="utf-8")
    if "no existen cuentas reales de clientes" not in privacy:
        errors.append("privacidad.html debe conservar la declaración de inexistencia de cuentas reales")

for relative in (
    "scripts/apply_capability_truth_v521.py",
    "scripts/validate_capability_truth_v521.py",
):
    if not (R / relative).exists():
        errors.append(f"Falta recurso v5.21 {relative}")

if errors:
    print("CAPABILITY TRUTH V5.21 FALLIDA", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(
    f"CAPABILITY TRUTH V5.21 OK: portal real {expected_state}, demo noindex explícita, "
    f"{public_demo_links} accesos públicos etiquetados sin promesas de capacidad ficticia."
)

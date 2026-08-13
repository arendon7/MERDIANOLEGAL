#!/usr/bin/env python3
"""v5.21: materializa la frontera entre capacidades reales y superficies demostrativas."""
from __future__ import annotations

from html import unescape
from pathlib import Path
import json
import re
import subprocess
import sys

from site_config import load_site_config

R = Path(__file__).resolve().parents[1]
CONFIG = load_site_config()
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8")).get("version", "0.0.0")
DEMO_HREF = re.compile(r'(<a\b[^>]*\bhref=["\'](?:\.\./)?demo\.html(?:#[^"\']*)?["\'][^>]*>)([\s\S]*?)(</a>)', re.I)
ROBOTS_META = re.compile(r'\s*<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*["\']\s*/?>\s*', re.I)
LEGACY_ROBOTS_JS = re.compile(
    r"\A\s*const robotsMeta = document\.createElement\(['\"]meta['\"]\);\s*\n"
    r"robotsMeta\.name = ['\"]robots['\"];\s*\n"
    r"robotsMeta\.content = ['\"]noindex,nofollow['\"];\s*\n"
    r"document\.head\.appendChild\(robotsMeta\);\s*\n+",
    re.M,
)


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def is_noindex(text: str) -> bool:
    match = re.search(r'<meta name="robots" content="([^"]+)">', text, re.I)
    return bool(match and "noindex" in match.group(1).lower())


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


def visible_text(fragment: str) -> str:
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", fragment)).split())


def explicit_demo_label(label: str) -> str:
    normalized = label.strip()
    mapping = {
        "Área de clientes": "Demo de cliente",
        "Abrir Meridiano Empresas": "Abrir portal demo",
        "Documentos guiados": "Documentos guiados · demo",
        "Explorar documentos →": "Explorar demo de documentos →",
        "Explorar documentos": "Explorar demo de documentos",
    }
    if normalized in mapping:
        return mapping[normalized]
    if re.search(r"\bdemo(?:strativ[oa])?\b", normalized, re.I):
        return normalized
    return normalized + " · demo"


def normalize_public_demo_links() -> int:
    changed = 0
    for path in indexable_html_targets():
        before = path.read_text(encoding="utf-8")

        def replace(match: re.Match[str]) -> str:
            body = match.group(2)
            label = visible_text(body)
            if not label or re.search(r"\bdemo(?:strativ[oa])?\b", label, re.I):
                return match.group(0)
            if re.search(r"<[^>]+>", body):
                raise RuntimeError(
                    f"{path.relative_to(R)}: enlace a demo con markup interno requiere etiqueta explícita manual"
                )
            replacement = explicit_demo_label(label)
            return match.group(1) + replacement + match.group(3)

        after = DEMO_HREF.sub(replace, before)
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed += 1
    return changed


def patch_demo_contract() -> None:
    path = R / "demo.html"
    text = path.read_text(encoding="utf-8")
    text = ROBOTS_META.sub("\n", text)
    canonical_robots = '  <meta name="robots" content="noindex,nofollow">\n'
    viewport = re.search(r'(<meta\s+name=["\']viewport["\'][^>]*>\s*)', text, re.I)
    if viewport:
        text = text[: viewport.end()] + canonical_robots + text[viewport.end() :]
    elif "</head>" in text:
        text = text.replace("</head>", canonical_robots + "</head>", 1)
    else:
        raise RuntimeError("demo.html: falta </head> para normalizar robots")

    text = re.sub(r'\sdata-capability-v521="[^"]*"', "", text)
    marker = '<body class="demo-page"'
    if marker not in text:
        raise RuntimeError("demo.html: falta body.demo-page")
    text = text.replace(marker, '<body class="demo-page" data-capability-v521="demo-only"', 1)
    path.write_text(text, encoding="utf-8")


def patch_demo_runtime() -> None:
    path = R / "demo.js"
    text = path.read_text(encoding="utf-8")
    text = LEGACY_ROBOTS_JS.sub("", text, count=1)
    path.write_text(text, encoding="utf-8")


def patch_runtime_config() -> None:
    path = R / "runtime-config.js"
    text = path.read_text(encoding="utf-8")
    match = re.fullmatch(r'window\.MERIDIANO_PUBLIC_CONFIG = Object\.freeze\((\{.*\})\);\s*', text, re.S)
    if not match:
        raise RuntimeError("runtime-config.js: formato canónico no reconocido")
    payload = json.loads(match.group(1))
    portal = CONFIG["capabilities"]["client_portal"]
    payload["capabilities"] = {
        "clientPortal": {"enabled": portal["enabled"], "url": portal["url"]}
    }
    path.write_text(
        "window.MERIDIANO_PUBLIC_CONFIG = Object.freeze("
        + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        + ");\n",
        encoding="utf-8",
    )


def patch_status() -> None:
    path = R / "site-status.json"
    status = json.loads(path.read_text(encoding="utf-8"))
    portal = CONFIG["capabilities"]["client_portal"]
    status["client_portal"] = "enabled" if portal["enabled"] else "disabled"
    status["client_portal_url"] = portal["url"] or None
    path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_materialized_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(R / "scripts/validate_capability_truth_v521.py")],
        cwd=R,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"v5.21 no supera validator de capacidad: {detail}")
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    if semver(VERSION) < (5, 21, 0):
        raise SystemExit("v5.21 requiere version.json >= 5.21.0")
    changed = normalize_public_demo_links()
    patch_demo_contract()
    patch_demo_runtime()
    patch_runtime_config()
    patch_status()
    validate_materialized_contract()
    portal = CONFIG["capabilities"]["client_portal"]
    state = "habilitado" if portal["enabled"] else "deshabilitado"
    print(
        f"CAPABILITY TRUTH V5.21 aplicada: portal real {state}; "
        f"{changed} superficies públicas normalizadas con frontera demo explícita."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

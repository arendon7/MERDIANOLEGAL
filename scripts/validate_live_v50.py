#!/usr/bin/env python3
"""Smoke post-deploy v5.0 contra la URL pública servida."""
from __future__ import annotations

from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json
import os
import sys
import time

R = Path(__file__).resolve().parents[1]
VERSION = json.loads((R / "version.json").read_text(encoding="utf-8"))["version"]
CONFIG = json.loads((R / "site-config.json").read_text(encoding="utf-8"))
CONFIG_BASE = str(CONFIG["base_url"]).rstrip("/") + "/"
BASE = os.environ.get("MERIDIANO_BASE_URL", CONFIG_BASE).rstrip("/") + "/"


def get(path: str, attempts: int = 8, expected_version: str | None = None) -> str:
    canonical_url = BASE + path.lstrip("/")
    last = None
    for attempt in range(attempts):
        separator = "&" if "?" in canonical_url else "?"
        url = f"{canonical_url}{separator}_meridiano_smoke={time.time_ns()}"
        try:
            req = Request(
                url,
                headers={
                    "User-Agent": "MeridianoLiveSmoke/5.0",
                    "Cache-Control": "no-cache",
                    "Pragma": "no-cache",
                },
            )
            with urlopen(req, timeout=12) as response:
                body = response.read().decode("utf-8", errors="replace")
                if response.status == 200:
                    if expected_version is None:
                        return body
                    try:
                        remote_version = json.loads(body).get("version")
                    except json.JSONDecodeError as exc:
                        last = RuntimeError(f"{canonical_url}: JSON inválido durante propagación: {exc}")
                    else:
                        if remote_version == expected_version:
                            return body
                        last = RuntimeError(
                            f"{canonical_url}: HTTP 200 todavía sirve versión {remote_version!r}; "
                            f"esperada {expected_version!r}"
                        )
                        print(
                            f"Esperando propagación de Pages: versión remota {remote_version!r}, "
                            f"esperada {expected_version!r} (intento {attempt + 1}/{attempts})."
                        )
                else:
                    last = RuntimeError(f"{canonical_url}: HTTP {response.status}")
        except (URLError, HTTPError, TimeoutError) as exc:
            last = exc
        if attempt + 1 < attempts:
            time.sleep(4)
    raise RuntimeError(f"No se pudo validar {canonical_url}: {last}")


def main() -> int:
    errors: list[str] = []

    try:
        status = json.loads(get("site-status.json", attempts=16, expected_version=VERSION))
        for key, expected in (
            ("version", VERSION),
            ("base_url", CONFIG_BASE),
            ("analytics", "disabled"),
            ("contact_channel", "whatsapp"),
            ("demo_indexing", "noindex"),
        ):
            if status.get(key) != expected:
                errors.append(f"site-status.json: {key}={status.get(key)!r}, esperado {expected!r}")
    except Exception as exc:
        errors.append(str(exc))

    checks = {
        "": [
            f"Web pública v{VERSION}",
            'data-contact-v49="true"',
            "runtime-config.js",
            "telemetry-v50.js",
            f'<link rel="canonical" href="{CONFIG_BASE}">',
            "Abrir solicitud en WhatsApp",
        ],
        "firma.html": [
            "LA FIRMA",
            f'<link rel="canonical" href="{CONFIG_BASE}firma.html">',
            "runtime-config.js",
        ],
        "servicios/direccion-juridica-externa.html": [
            "Dirección Jurídica Externa",
            f'<link rel="canonical" href="{CONFIG_BASE}servicios/direccion-juridica-externa.html">',
            "../telemetry-v50.js",
        ],
        "productos/programa-gobernanza-ia.html": [
            "Gobernanza",
            f'<link rel="canonical" href="{CONFIG_BASE}productos/programa-gobernanza-ia.html">',
        ],
        "perspectivas.html": ["PERSPECTIVAS MERIDIANO", "telemetry-v50.js"],
        "privacidad.html": [
            "Versión 1.1",
            "Contexto de navegación e instrumentación técnica",
            "analítica de terceros",
        ],
        "demo.html": ['content="noindex,nofollow"', "DEMO FICTICIA"],
        "runtime-config.js": [
            "window.MERIDIANO_PUBLIC_CONFIG",
            json.dumps(CONFIG_BASE),
            json.dumps(VERSION),
        ],
        "telemetry-v50.js": [
            "meridiano:telemetry",
            "lead_prepared",
            "MeridianoTelemetry",
        ],
        "commercial-conversion-v44.js": [
            "rawHref.split(/[?#]/)[0]",
            "const hash = url.hash",
        ],
    }

    for path, markers in checks.items():
        try:
            body = get(path)
            for marker in markers:
                if marker not in body:
                    errors.append(f"{path or '/'}: falta {marker!r}")
        except Exception as exc:
            errors.append(str(exc))

    try:
        sitemap = get("sitemap.xml")
        if "/demo.html" in sitemap:
            errors.append("sitemap.xml no debe indexar demo.html")
        if CONFIG_BASE not in sitemap:
            errors.append("sitemap.xml no usa la base_url configurada")
        for marker in (
            "/firma.html",
            "/servicios/direccion-juridica-externa.html",
            "/productos/programa-gobernanza-ia.html",
        ):
            if marker not in sitemap:
                errors.append(f"sitemap.xml: falta {marker}")
    except Exception as exc:
        errors.append(str(exc))

    try:
        robots = get("robots.txt")
        if f"Sitemap: {CONFIG_BASE}sitemap.xml" not in robots:
            errors.append("robots.txt no declara el sitemap canónico")
        if "demo.html" not in robots:
            errors.append("robots.txt no excluye demo.html")
    except Exception as exc:
        errors.append(str(exc))

    if errors:
        print("SMOKE PÚBLICO V5.0 FALLIDO")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"SMOKE PÚBLICO V5.0 OK: {BASE} sirve {VERSION} con configuración, "
        "canonical, privacidad, telemetría local y rutas críticas íntegras."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

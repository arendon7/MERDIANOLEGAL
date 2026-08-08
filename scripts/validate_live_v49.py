#!/usr/bin/env python3
"""Smoke test post-deploy v4.9 contra la URL pública real."""
import os
import sys
import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BASE = os.environ.get("MERIDIANO_BASE_URL", "https://arendon7.github.io/MERDIANOLEGAL/").rstrip("/") + "/"
EXPECTED_VERSION = os.environ.get("MERIDIANO_EXPECTED_VERSION", "4.9.0")


def get(path, attempts=8):
    url = BASE + path.lstrip("/")
    last = None
    for attempt in range(attempts):
        try:
            req = Request(url, headers={"User-Agent": "MeridianoLiveSmoke/4.9"})
            with urlopen(req, timeout=12) as response:
                body = response.read().decode("utf-8", errors="replace")
                if response.status == 200:
                    return body
                last = RuntimeError(f"{url}: HTTP {response.status}")
        except (URLError, HTTPError, TimeoutError) as exc:
            last = exc
        if attempt + 1 < attempts:
            time.sleep(4)
    raise RuntimeError(f"No se pudo validar {url}: {last}")


def main():
    checks = {
        "": [f"Web demostrativa v{EXPECTED_VERSION}", 'data-contact-v49="true"', "operations-v49.css", "Dirección jurídica para empresas que avanzan"],
        "firma.html": ["LA FIRMA", "Meridiano Legal"],
        "servicios/direccion-juridica-externa.html": ["Dirección Jurídica Externa", "detail-v46.css"],
        "productos/programa-gobernanza-ia.html": ["Gobernanza", "detail-v46.css"],
        "perspectivas.html": ["PERSPECTIVAS MERIDIANO"],
        "experiencia.html": ["Meridiano"],
        "demo.html": ['content="noindex,nofollow"', "DEMO FICTICIA"],
        "commercial-conversion-v44.js": ["rawHref.split(/[?#]/)[0]", "const hash = url.hash"],
    }
    errors = []
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
        for marker in ("/firma.html", "/servicios/direccion-juridica-externa.html", "/productos/programa-gobernanza-ia.html"):
            if marker not in sitemap:
                errors.append(f"sitemap.xml: falta {marker}")
    except Exception as exc:
        errors.append(str(exc))
    try:
        robots = get("robots.txt")
        if "Sitemap:" not in robots:
            errors.append("robots.txt no declara sitemap")
    except Exception as exc:
        errors.append(str(exc))
    if errors:
        print("SMOKE PÚBLICO V4.9 FALLIDO")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SMOKE PÚBLICO V4.9 OK: {BASE} responde con versión {EXPECTED_VERSION} y rutas críticas íntegras.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

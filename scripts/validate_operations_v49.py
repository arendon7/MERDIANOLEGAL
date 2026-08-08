#!/usr/bin/env python3
"""Valida preparación operativa v4.9 del sitio público."""
from pathlib import Path
import json
import sys

R = Path(__file__).resolve().parents[1]


def semver(value):
    return tuple(int(x) for x in value.split(".")[:3])


def main():
    errors = []
    version = json.loads((R / "version.json").read_text(encoding="utf-8"))["version"]
    if semver(version) < (4, 9, 0):
        errors.append("version.json debe ser >= 4.9.0")
    index = (R / "index.html").read_text(encoding="utf-8")
    site = (R / "site-v3.js").read_text(encoding="utf-8")
    commercial = (R / "commercial-conversion-v44.js").read_text(encoding="utf-8")
    css = (R / "operations-v49.css").read_text(encoding="utf-8")

    for marker in ('operations-v49.css','data-contact-v49="true"','name="website"','maxlength="120"','maxlength="160"','maxlength="180"','maxlength="2000"','Abrir solicitud en WhatsApp','La solicitud se completa únicamente cuando usted envía el mensaje allí','Abrir WhatsApp directamente','role="status"'):
        if marker not in index:
            errors.append(f"index.html: falta {marker!r}")
    if index.count('name="website"') != 1:
        errors.append("index.html debe tener exactamente un honeypot")
    if index.find("quality-v48.css") > index.find("operations-v49.css"):
        errors.append("operations-v49.css debe cargar después de quality-v48.css")

    for marker in ("const contactStartedAt = Date.now()","Referencia web:","Contexto comercial:","Origen:","meridiano:lead-prepared","window.location.assign(url)","La solicitud solo queda enviada cuando confirme el envío allí","form.dataset.lastLeadReference"):
        if marker not in site:
            errors.append(f"site-v3.js: falta {marker!r}")
    if "Solicitud preparada. Se abrirá WhatsApp" in site:
        errors.append("site-v3.js conserva el mensaje legado de envío")

    if "rawHref.split('?')[0]" in commercial:
        errors.append("commercial-conversion-v44.js conserva reconstrucción incorrecta de fragmentos")
    for marker in ("rawHref.split(/[?#]/)[0]", "const hash = url.hash", "${hash}"):
        if marker not in commercial:
            errors.append(f"commercial-conversion-v44.js: falta {marker!r}")
    if ".contact-hp-v49" not in css or "position: absolute" not in css:
        errors.append("operations-v49.css no oculta correctamente el honeypot")

    if errors:
        print("VALIDACIÓN OPERATIVA V4.9 FALLIDA")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDACIÓN OPERATIVA V4.9 OK: contacto, anti-bot, contexto, fragmentos y fallback íntegros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

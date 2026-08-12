#!/usr/bin/env python3
"""Valida v5.11: estados comerciales y condiciones previas al inicio real del encargo."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
STYLE = ROOT / "engagement-v511.css"
START = "<!-- ENGAGEMENT-V511:START -->"
END = "<!-- ENGAGEMENT-V511:END -->"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"ENGAGEMENT V5.11 FAIL: {message}")


def main() -> int:
    text = INDEX.read_text(encoding="utf-8")
    css = STYLE.read_text(encoding="utf-8")

    require(text.count(START) == 1 and text.count(END) == 1, "debe existir un único bloque gestionado")
    require('<link rel="stylesheet" href="engagement-v511.css">' in text, "falta stylesheet v5.11")
    require(text.index('conversion-close-v510.css') < text.index('engagement-v511.css'), "v5.11 debe cargar después de v5.10")
    require(text.index("<!-- CLOSE-V510:END -->") < text.index(START), "v5.11 debe seguir a v5.10")

    form_start = text.index('<form class="contact-form" id="contact-form"')
    form_end = text.index('</form>', form_start)
    block_start = text.index(START)
    block_end = text.index(END)
    require(form_start < block_start < block_end < form_end, "el bloque debe permanecer dentro del formulario de contacto")

    require('data-engagement-v511="true"' in text, "falta marcador funcional")
    require(text.count('data-engagement-state-v511=') == 4, "deben existir cuatro estados de contratación")
    for state in ("request", "proposal", "accepted", "started"):
        require(f'data-engagement-state-v511="{state}"' in text, f"falta estado {state}")

    for phrase in (
        "Solicitud preparada",
        "Propuesta emitida",
        "Propuesta aceptada",
        "Encargo iniciado",
        "No acepta contratos",
        "No cobra pagos",
        "No reserva agenda",
        "No crea un expediente",
        "No habilita carga documental",
        "No inicia el encargo",
    ):
        require(phrase in text, f"falta claridad `{phrase}`")

    require('data-engagement-automatic-v511="false"' in text, "debe quedar explícito que no hay automatización contractual")
    require("confidenciales" in text and "canal" in text, "debe preservarse la regla de canal seguro")
    require(".engagement-v511" in css and "@media(max-width:760px)" in css, "CSS v5.11 incompleto o sin responsive")
    require("#5c6974" in css and "#102233" in css, "faltan tonos de texto de contraste alto")

    forbidden = ("firma electrónica", "pasarela de pago", "CRM activo", "carga segura aquí")
    for phrase in forbidden:
        require(phrase not in text, f"no debe declararse integración inexistente: {phrase}")

    print("ENGAGEMENT V5.11 OK: cuatro estados, verificaciones de inicio y límites de automatización presentes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

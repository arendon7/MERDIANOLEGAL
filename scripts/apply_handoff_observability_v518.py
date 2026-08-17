#!/usr/bin/env python3
"""Aplica v5.18 y encadena extensiones canónicas posteriores al handoff."""
from __future__ import annotations

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
SCRIPT = '<script defer src="handoff-observability-v518.js"></script>'
ANCHOR = '<script defer src="telemetry-v50.js"></script>'


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def main() -> int:
    text = HOME.read_text(encoding="utf-8")
    text = re.sub(r'(?m)^[ \t]*' + re.escape(SCRIPT) + r'[ \t]*(?:\r?\n)?', "", text)
    if ANCHOR not in text:
        raise RuntimeError("index.html: falta telemetry-v50.js para ordenar observabilidad v5.18")
    text = text.replace(ANCHOR, ANCHOR + "\n  " + SCRIPT, 1)
    if text.count(SCRIPT) != 1:
        raise RuntimeError("index.html: v5.18 debe cargar una sola vez handoff-observability-v518.js")
    if text.find(ANCHOR) > text.find(SCRIPT):
        raise RuntimeError("index.html: observabilidad v5.18 debe cargar después de telemetry-v50.js")
    HOME.write_text(text, encoding="utf-8")
    print("HANDOFF OBSERVABILITY V5.18 OK: runtime local insertado después de telemetry-v50.js.")

    version = json.loads((ROOT / "version.json").read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) >= (5, 24, 0):
        from canonical_pipeline_v524 import validate_manifest as validate_canonical_pipeline_v524
        validate_canonical_pipeline_v524()
        print("CANONICAL PIPELINE V5.24 CONTRACT OK: builder y segunda pasada conservan el mismo orden.")

    if semver(version) >= (5, 21, 0):
        from apply_capability_truth_v521 import main as apply_capability_truth_v521
        result = apply_capability_truth_v521()
        if result:
            return result
        if semver(version) >= (5, 23, 0):
            from apply_contact_compression_v523 import main as apply_contact_compression_v523
            from normalize_contact_compression_v523 import main as normalize_contact_compression_v523
            result = apply_contact_compression_v523()
            if result:
                return result
            result = normalize_contact_compression_v523()
            if result:
                return result
            if semver(version) >= (5, 25, 0):
                from apply_professional_authority_v525 import main as apply_professional_authority_v525
                result = apply_professional_authority_v525()
                if result:
                    return result
            # v5.26 se ejecuta al final de las capas históricas: las anclas necesarias
            # para v4.5 pueden rehidratarse durante segunda pasada, pero nunca deben
            # quedar presentes en la salida pública simplificada.
            if semver(version) >= (5, 26, 0):
                from apply_integral_visual_v526 import main as apply_integral_visual_v526
                result = apply_integral_visual_v526()
                if result:
                    return result
            # v5.28 corre después de la simplificación visual para mover el único
            # contacto canónico sin que una capa histórica lo reubique de nuevo.
            if semver(version) >= (5, 28, 0):
                from apply_conversion_path_v528 import main as apply_conversion_path_v528
                result = apply_conversion_path_v528()
                if result:
                    return result
            # v5.29 observa el funnel materializado y coloca confianza contextual
            # sin alterar el orden de secciones v5.28.
            if semver(version) >= (5, 29, 0):
                from apply_funnel_trust_v529 import main as apply_funnel_trust_v529
                result = apply_funnel_trust_v529()
                if result:
                    return result
            # v5.30 hace explícita la lógica de contratación de las fichas profundas.
            if semver(version) >= (5, 30, 0):
                from apply_offer_commercial_v530 import main as apply_offer_commercial_v530
                result = apply_offer_commercial_v530()
                if result:
                    return result
            # v5.31 es la normalización final de jerarquía: conserva toda la profundidad
            # y convierte solo soporte decisional secundario a divulgación progresiva.
            if semver(version) >= (5, 31, 0):
                from apply_decision_compression_v531 import main as apply_decision_compression_v531
                return apply_decision_compression_v531()
            return 0
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

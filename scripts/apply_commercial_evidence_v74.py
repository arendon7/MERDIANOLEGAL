#!/usr/bin/env python3
"""Materializa Commercial Evidence Readiness v7.4 en siete superficies públicas.

No activa analítica externa. Solo carga un runtime local/efímero que propaga un
`source` allowlisted y expone eventos comerciales sin PII para QA.

El lifecycle de release es independiente del estado operativo: prototype,
release-candidate y certified mantienen siempre `status=readiness-disabled`.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets" / "data" / "v7" / "commercial-evidence-v74.json"
VERSION = ROOT / "version.json"
RUNTIME = "assets/js/v7/commercial-evidence-v74.js"
START = "<!-- COMMERCIAL-EVIDENCE-V74:START -->"
END = "<!-- COMMERCIAL-EVIDENCE-V74:END -->"
BLOCK_PATTERN = re.compile(
    r"^[ \t]*" + re.escape(START) + r".*?" + re.escape(END) + r"[ \t]*(?:\r?\n)?",
    re.M | re.S,
)
VALID_LIFECYCLE = {
    "prototype": {
        "contract_prefix": "7.4.0-prototype",
        "public_version": "7.3.0",
        "channel": "github-pages-production-legal-intelligence-demo-certified",
    },
    "release-candidate": {
        "contract_exact": "7.4.0",
        "public_version": "7.4.0",
        "channel": "github-pages-commercial-evidence-readiness-candidate",
    },
    "certified": {
        "contract_exact": "7.4.0",
        "public_version": "7.4.0",
        "channel": "github-pages-production-commercial-evidence-readiness-certified",
    },
}


def resolve_lifecycle(data: dict) -> str:
    lifecycle = str(data.get("lifecycle", "") or "").strip()
    version = str(data.get("version", "") or "").strip()
    if not lifecycle and version.startswith("7.4.0-prototype"):
        lifecycle = "prototype"
    if lifecycle not in VALID_LIFECYCLE:
        raise RuntimeError(f"Commercial Evidence v7.4 lifecycle inválido: {lifecycle!r}")
    expected = VALID_LIFECYCLE[lifecycle]
    if "contract_exact" in expected and version != expected["contract_exact"]:
        raise RuntimeError(f"Commercial Evidence v7.4 {lifecycle} debe declarar version {expected['contract_exact']}")
    if "contract_prefix" in expected and not version.startswith(expected["contract_prefix"]):
        raise RuntimeError(f"Commercial Evidence v7.4 {lifecycle} debe usar prefijo {expected['contract_prefix']}")

    public = json.loads(VERSION.read_text(encoding="utf-8"))
    if public.get("version") != expected["public_version"]:
        raise RuntimeError(
            f"Commercial Evidence v7.4 {lifecycle} requiere version pública {expected['public_version']}"
        )
    if public.get("channel") != expected["channel"]:
        raise RuntimeError(
            f"Commercial Evidence v7.4 {lifecycle} requiere canal {expected['channel']}"
        )
    return lifecycle


def load_contract() -> dict:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    resolve_lifecycle(data)
    if data.get("status") != "readiness-disabled":
        raise RuntimeError("Commercial Evidence v7.4 debe permanecer readiness-disabled")
    if data.get("baseline") != "7.3.0":
        raise RuntimeError("Commercial Evidence v7.4 debe preservar baseline 7.3.0")
    activation = data.get("activation") or {}
    if activation.get("external_analytics") is not False or activation.get("network_transport") is not False:
        raise RuntimeError("Commercial Evidence v7.4 no puede activar analytics ni transporte externo")
    if activation.get("provider") != "none":
        raise RuntimeError("Commercial Evidence v7.4 debe mantener provider=none")
    surfaces = data.get("surfaces") or []
    if len(surfaces) != 7 or len(set(surfaces)) != 7:
        raise RuntimeError("Commercial Evidence v7.4 requiere exactamente siete superficies únicas")
    return data


def script_src(relative_path: str) -> str:
    depth = len(Path(relative_path).parts) - 1
    return ("../" * depth) + RUNTIME


def render_block(relative_path: str) -> str:
    src = script_src(relative_path)
    return f'{START}\n<script defer src="{src}"></script>\n{END}'


def materialize(text: str, relative_path: str) -> str:
    text = BLOCK_PATTERN.sub("", text)
    if text.count(RUNTIME) != 0:
        raise RuntimeError(f"{relative_path}: runtime v7.4 no administrado detectado")
    closing = text.rfind("</body>")
    if closing < 0:
        raise RuntimeError(f"{relative_path}: falta </body>")
    block = render_block(relative_path)
    prefix = text[:closing].rstrip()
    suffix = text[closing:]
    return prefix + "\n" + block + "\n" + suffix


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    contract = load_contract()
    changed: list[str] = []
    for relative_path in contract["surfaces"]:
        path = ROOT / relative_path
        if not path.exists():
            raise RuntimeError(f"Commercial Evidence v7.4: falta superficie {relative_path}")
        before = path.read_text(encoding="utf-8")
        after = materialize(before, relative_path)
        if after != before:
            changed.append(relative_path)
            if not args.check:
                path.write_text(after, encoding="utf-8")
    if args.check and changed:
        raise SystemExit("Commercial Evidence v7.4 no está materializado: " + ", ".join(changed))
    print(f"Commercial Evidence v7.4: {'CHECK PASS' if args.check else 'materializado'} en {len(contract['surfaces'])} superficies")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

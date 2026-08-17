#!/usr/bin/env python3
"""v5.31: reduce exposición decisional permanente sin borrar profundidad jurídica/comercial."""
from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = ROOT / "version.json"
CONTRACT = ROOT / "decision-compression-v531.json"
DETAILS = sorted((ROOT / "servicios").glob("*.html")) + sorted((ROOT / "productos").glob("*.html"))
SOLUTIONS = sorted(path for path in (ROOT / "soluciones").glob("*.html") if path.name != "index.html")
STYLE = '<link rel="stylesheet" href="../decision-compression-v531.css">'
OFFER_START = "<!-- OFFER-NARRATIVE-V522:START -->"
OFFER_END = "<!-- OFFER-NARRATIVE-V522:END -->"

DEEP_OPEN = '''<!-- DECISION-COMPRESSION-V531:DEEP-START -->
<details class="decision-depth-v531" data-decision-compression-v531="offer-narrative">
  <summary><span>PROFUNDIDAD ADICIONAL</span><strong>Comparar modalidad, alternativa y lente jurídica</strong></summary>
'''
DEEP_CLOSE = '''
</details>
<!-- DECISION-COMPRESSION-V531:DEEP-END -->'''
PAIR_OPEN = '''<!-- DECISION-COMPRESSION-V531:PAIR-START -->
<div class="decision-result-v531" data-decision-compression-v531="decision-result">
'''
PAIR_CLOSE = '''
</div>
<!-- DECISION-COMPRESSION-V531:PAIR-END -->'''

SECONDARY = {
    "objections": (
        "<!-- CRO-V52-OBJECTIONS:START -->",
        "<!-- CRO-V52-OBJECTIONS:END -->",
        "EXPECTATIVAS Y OBJECIONES",
        "Aclaraciones que conviene revisar solo si todavía hay dudas sobre el encaje",
    ),
    "faq": (
        "<!-- CRO-V52-FAQ:START -->",
        "<!-- CRO-V52-FAQ:END -->",
        "PREGUNTAS FRECUENTES",
        "Resolver dudas adicionales antes de definir el alcance",
    ),
    "related": (
        "<!-- CRO-V52-RELATED:START -->",
        "<!-- CRO-V52-RELATED:END -->",
        "RUTAS RELACIONADAS",
        "Explorar alternativas si el problema cambia al profundizar",
    ),
}


def semver(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else (0, 0, 0)


def ensure_style(text: str) -> str:
    text = re.sub(r'(?m)^[ \t]*' + re.escape(STYLE) + r'[ \t]*(?:\r?\n)?', "", text)
    if "</head>" not in text:
        raise RuntimeError("página sin </head> para cargar decision-compression-v531.css")
    return text.replace("</head>", f"  {STYLE}\n</head>", 1)


def strip_deep_wrappers(text: str) -> str:
    for token in (DEEP_OPEN, DEEP_CLOSE, PAIR_OPEN, PAIR_CLOSE):
        text = text.replace(token, "")
    return text


def solution_open(key: str, eyebrow: str, label: str) -> str:
    return (
        f'<!-- DECISION-COMPRESSION-V531:SOLUTION-{key.upper()}-START -->\n'
        f'<details class="solution-depth-v531" data-decision-compression-v531="solution-{key}">\n'
        f'  <summary><span>{eyebrow}</span><strong>{label}</strong></summary>\n'
    )


def solution_close(key: str) -> str:
    return f'\n</details>\n<!-- DECISION-COMPRESSION-V531:SOLUTION-{key.upper()}-END -->'


def strip_solution_wrappers(text: str) -> str:
    for key, (_, _, eyebrow, label) in SECONDARY.items():
        text = text.replace(solution_open(key, eyebrow, label), "")
        text = text.replace(solution_close(key), "")
    text = text.replace(
        solution_open("proof", "PRUEBA Y CONTEXTO", "Validar criterio, sector y método antes de contactar"), ""
    )
    text = text.replace(solution_close("proof"), "")
    return text


def wrap_between(text: str, start: str, end: str, opener: str, closer: str, label: str) -> str:
    first = text.find(start)
    last = text.find(end, first + len(start)) if first >= 0 else -1
    if first < 0 or last < 0:
        raise RuntimeError(f"falta bloque {label}")
    last += len(end)
    block = text[first:last]
    return text[:first] + opener + block + closer + text[last:]


def patch_detail(path: Path) -> None:
    text = strip_deep_wrappers(path.read_text(encoding="utf-8"))
    text = ensure_style(text)

    pair_pattern = re.compile(
        r'(<section class="detail-section" aria-labelledby="pregunta-title">.*?</section>\s*'
        r'<section class="detail-section ivory" aria-labelledby="resultado-title">.*?</section>)',
        re.S,
    )
    match = pair_pattern.search(text)
    if not match:
        raise RuntimeError(f"{path.relative_to(ROOT)}: no se localizaron pregunta + resultado")
    text = text[:match.start()] + PAIR_OPEN + match.group(1) + PAIR_CLOSE + text[match.end():]

    start = text.find(OFFER_START)
    end = text.find(OFFER_END, start + len(OFFER_START)) if start >= 0 else -1
    if start < 0 or end < 0:
        raise RuntimeError(f"{path.relative_to(ROOT)}: falta narrativa v5.22")
    end += len(OFFER_END)
    block = text[start:end]
    text = text[:start] + DEEP_OPEN + block + DEEP_CLOSE + text[end:]

    if text.count('data-decision-compression-v531="decision-result"') != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: pareja decisión/resultado v5.31 no es única")
    if text.count('data-decision-compression-v531="offer-narrative"') != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: narrativa progresiva v5.31 no es única")
    path.write_text(text, encoding="utf-8")


def patch_solution(path: Path) -> None:
    text = strip_solution_wrappers(path.read_text(encoding="utf-8"))
    text = ensure_style(text)
    for key, (start, end, eyebrow, label) in SECONDARY.items():
        text = wrap_between(
            text, start, end, solution_open(key, eyebrow, label), solution_close(key), f"{path.name}:{key}"
        )

    proof_pattern = re.compile(r'(<section class="growth-section-v51 growth-proof-page-v51">.*?</section>)', re.S)
    match = proof_pattern.search(text)
    if not match:
        raise RuntimeError(f"{path.relative_to(ROOT)}: falta bloque de prueba secundaria")
    opener = solution_open("proof", "PRUEBA Y CONTEXTO", "Validar criterio, sector y método antes de contactar")
    text = text[:match.start()] + opener + match.group(1) + solution_close("proof") + text[match.end():]

    for key in (*SECONDARY.keys(), "proof"):
        if text.count(f'data-decision-compression-v531="solution-{key}"') != 1:
            raise RuntimeError(f"{path.relative_to(ROOT)}: wrapper {key} v5.31 no es único")
    path.write_text(text, encoding="utf-8")


def validate() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_decision_compression_v531.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError((result.stderr or result.stdout).strip())
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> int:
    version = json.loads(VERSION.read_text(encoding="utf-8")).get("version", "0.0.0")
    if semver(version) < (5, 31, 0):
        return 0
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    if contract.get("version") != "5.31.0":
        raise RuntimeError("decision-compression-v531.json debe declarar 5.31.0")
    if len(DETAILS) != 16 or len(SOLUTIONS) != 6:
        raise RuntimeError(f"v5.31 esperaba 16 fichas y 6 rutas; encontró {len(DETAILS)} y {len(SOLUTIONS)}")
    for path in DETAILS:
        patch_detail(path)
    for path in SOLUTIONS:
        patch_solution(path)
    validate()
    print("DECISION COMPRESSION V5.31 OK: 16 fichas + 6 rutas con profundidad secundaria progresiva, sin borrar contenido.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

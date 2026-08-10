#!/usr/bin/env python3
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH_DIR = ROOT / "graphify-out"

def count(pattern: str) -> int:
    return len(list(ROOT.glob(pattern)))

def main() -> None:
    graph = json.loads((GRAPH_DIR / "graph.json").read_text(encoding="utf-8"))
    version = json.loads((ROOT / "version.json").read_text(encoding="utf-8"))
    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", graph.get("links", []))
    wiki_notes = list((GRAPH_DIR / "wiki").glob("*.md"))

    counts = {
        "html_total": sum(count(pattern) for pattern in ["*.html", "productos/*.html", "servicios/*.html", "soluciones/*.html", "sectores/*.html", "perspectivas/*.html"]),
        "products_source": count("catalog-products-v41/*.json"),
        "services_source": count("catalog-services-v42/*.json"),
        "solutions_html": count("soluciones/*.html"),
        "sectors_html": count("sectores/*.html"),
        "perspectives_html": count("perspectivas/*.html"),
        "python_scripts": count("scripts/*.py"),
        "javascript_sources": count("*.js") + count("scripts/*.mjs"),
        "e2e_specs": count("tests/e2e/*.mjs"),
    }

    meta = {
        "project": "Meridiano Legal",
        "source_commit": source_commit,
        "version": version.get("version"),
        "channel": version.get("channel"),
        "graphify_version": os.environ.get("GRAPHIFY_VERSION", "unknown"),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "graph": {"nodes": len(nodes), "edges": len(edges), "wiki_notes": len(wiki_notes)},
        "counts": counts,
    }
    (GRAPH_DIR / "BUILD_META.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Meridiano Legal — Graphify Project Snapshot",
        "",
        "> Memoria automática y regenerable. Si contradice `main`, gana `main`.",
        "",
        f"- Built from commit: `{source_commit}`",
        f"- Versión pública declarada: `{version.get('version', 'desconocida')}`",
        f"- Canal: `{version.get('channel', 'desconocido')}`",
        f"- Graphify: `{meta['graphify_version']}`",
        f"- Generado UTC: `{meta['generated_at_utc']}`",
        "",
        "## Grafo",
        "",
        f"- Nodos: **{len(nodes)}**",
        f"- Relaciones: **{len(edges)}**",
        f"- Notas wiki: **{len(wiki_notes)}**",
        "",
        "## Superficies/fuentes detectadas",
        "",
    ]
    for key, value in counts.items():
        lines.append(f"- `{key}`: **{value}**")
    lines += [
        "",
        "## Uso",
        "",
        "1. Compruebe que `Built from commit` coincide con `main`.",
        "2. Use `wiki/index.md` y `GRAPH_REPORT.md` para reducir el conjunto de impacto.",
        "3. Verifique siempre en `main` las fuentes/tests antes de modificar.",
        "4. Trate relaciones `INFERRED` como hipótesis, no como prueba.",
    ]
    (GRAPH_DIR / "PROJECT_SNAPSHOT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()

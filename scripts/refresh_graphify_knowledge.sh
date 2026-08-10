#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GRAPHIFY_VERSION="${GRAPHIFY_VERSION:-0.9.26}"
GRAPHIFY_FULL_OBSIDIAN="${GRAPHIFY_FULL_OBSIDIAN:-0}"
cd "$ROOT"

if command -v uvx >/dev/null 2>&1; then
  GRAPHIFY=(uvx --from "graphifyy[sql]==${GRAPHIFY_VERSION}" graphify)
elif command -v graphify >/dev/null 2>&1; then
  GRAPHIFY=(graphify)
else
  echo "ERROR: instala uv (recomendado) o graphifyy antes de continuar." >&2
  exit 1
fi

rm -rf graphify-out
"${GRAPHIFY[@]}" extract . --code-only
test -s graphify-out/graph.json
"${GRAPHIFY[@]}" cluster-only . --no-viz
test -s graphify-out/GRAPH_REPORT.md
"${GRAPHIFY[@]}" export wiki
test -s graphify-out/wiki/index.md

GRAPHIFY_VERSION="$GRAPHIFY_VERSION" python scripts/build_graphify_snapshot.py
test -s graphify-out/BUILD_META.json
test -s graphify-out/PROJECT_SNAPSHOT.md

if [ "$GRAPHIFY_FULL_OBSIDIAN" = "1" ]; then
  rm -rf knowledge/90_GRAPHIFY_AUTO
  mkdir -p knowledge/90_GRAPHIFY_AUTO
  "${GRAPHIFY[@]}" export obsidian --dir knowledge/90_GRAPHIFY_AUTO
fi

printf '%s\n' "Graphify listo: graph.json, GRAPH_REPORT.md, wiki, BUILD_META.json y PROJECT_SNAPSHOT.md"

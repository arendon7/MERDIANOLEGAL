#!/usr/bin/env python3
"""Instala una sola vez el catálogo v4.1 y delega en el generador canónico extraído."""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "bootstrap" / "v41"
EXPECTED_SHA256 = "dda9f6b3ee502705a611fbba5e3449f1560e0d337f5ded4dfa61eb0789d3ec64"
ARCHIVE = ROOT / ".meridiano-products-v41.tar.gz"


def safe_extract(archive: tarfile.TarFile, destination: Path) -> None:
    destination = destination.resolve()
    for member in archive.getmembers():
        target = (destination / member.name).resolve()
        if target != destination and destination not in target.parents:
            raise RuntimeError(f"Ruta no permitida en el paquete: {member.name}")
    archive.extractall(destination)


def main() -> None:
    parts = sorted(PARTS_DIR.glob("part-*"))
    if not parts:
        raise RuntimeError("No se encontraron los bloques del catálogo v4.1.")

    digest = hashlib.sha256()
    with ARCHIVE.open("wb") as output:
        for part in parts:
            data = part.read_bytes()
            digest.update(data)
            output.write(data)

    actual = digest.hexdigest()
    if actual != EXPECTED_SHA256:
        raise RuntimeError(f"Integridad inválida: {actual}")

    with tarfile.open(ARCHIVE, "r:gz") as package:
        safe_extract(package, ROOT)

    ARCHIVE.unlink(missing_ok=True)
    shutil.rmtree(PARTS_DIR)
    bootstrap_root = ROOT / "bootstrap"
    if bootstrap_root.exists() and not any(bootstrap_root.iterdir()):
        bootstrap_root.rmdir()

    for temporary_workflow in (
        ROOT / ".github" / "workflows" / "apply-products-v41.yml",
        ROOT / ".github" / "workflows" / "bootstrap-v40.yml",
    ):
        temporary_workflow.unlink(missing_ok=True)

    # El workflow canónico solo añade explícitamente los archivos derivados.
    # Dejamos los fuentes y las eliminaciones ya preparados en el índice para
    # que el commit final sea atómico e incluya todo el catálogo.
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=True)

    extracted_generator = ROOT / "scripts" / "build_catalog_shells.py"
    subprocess.run([sys.executable, str(extracted_generator)], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()

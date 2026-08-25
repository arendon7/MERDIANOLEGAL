# W4.6 handoff

W4.5 queda certificado con run `32907133921`.

Frente vigente: **W4.6 — Pipeline Compatibility Candidate**.

Objetivo inmediato: certificar coexistencia del árbol `49 HTML = 46 legacy + 3 v8` con Builder y Pages sin despliegue, sin indexación, sin cambio de canónicos y sin mover `main`/`stable`.

Contrato: `assets/data/v8/pipeline-compat-v80.json`.
Validator: `scripts/validate_v8_pipeline_compat.py`.
Workflow candidate: `.github/workflows/v80-pipeline-compat-candidate.yml`.

La validación v6 histórica permanece estricta; W4.6 usa una proyección temporal de 46 HTML únicamente para los validators con topología cerrada.

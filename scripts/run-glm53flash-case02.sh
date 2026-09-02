#!/usr/bin/env bash
# R04 follow-up (2026-09-02): fill the missing case-02 reproduction
# (Auton 2015 / 1000 Genomes Phase 3, benchmark 1000Genomes-Phase3-v1)
# with the system `dsh-science × GLM-5.3-Flash`, as a one-shot headless run.
#
# - Model: zai / glm-5.3-flash (agent-default-model in ~/.dsh/settings.yaml;
#   key injected at runtime from ~/.dsh/.credentials.yaml -> ZAI_API_KEY).
# - Harness: dsh headless profile + science overlay
#   (scripts/overlays/headless-science.yml) which patches the science persona
#   into system-prompt and inserts the science engine rows
#   (research-loop / artifact-registry / remote-compute) — equivalent to the
#   科学模式 preset used by the R04 GUI sessions.
# - Fixed task prompt: scripts/case02-task-prompt.txt (verbatim from
#   benchmarks/humangenomics/README.md, task prompt row).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OVERLAY="${SCRIPT_DIR}/overlays/headless-science.yml"
TASK_FILE="${SCRIPT_DIR}/case02-task-prompt.txt"
WORKSPACE="/Volumes/repo/ciao/Harness-bench/dsh-glm-5.3-flash"

TASK="$(cat "${TASK_FILE}")"

cd "${WORKSPACE}"
echo "[run-glm53flash-case02] workspace=${WORKSPACE}"
echo "[run-glm53flash-case02] overlay=${OVERLAY}"
echo "[run-glm53flash-case02] start=$(date -Iseconds)"
exec dsh --profile headless --patch "${OVERLAY}" "${TASK}"

#!/usr/bin/env bash
set -euo pipefail
mkdir -p /app/out
python /app/harness/run_eval.py --seeds /app/harness/seeds.txt --out /app/out
echo "Done. Outputs in /app/out"

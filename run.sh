#!/usr/bin/env bash
set -e

MODE=${1:-smoke}

if [ "$MODE" = "smoke" ]; then
  echo "Running smoke training with sample data..."
  python scripts/train.py --data data/sample/tamil_sample.csv --epochs 1 --save-dir models/smoke
else
  echo "Mode not recognized. Use: smoke"
fi


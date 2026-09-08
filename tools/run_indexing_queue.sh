#!/usr/bin/env bash
set -euo pipefail

ROOT="${DTT_INDEXING_ROOT:-/home/ubuntu/dtt-indexing-queue}"
PYTHON="${PYTHON:-/usr/bin/python3}"
SITE="${DTT_SITE:-https://doctieuthuyet.com}"
LOOKBACK_HOURS="${DTT_INDEX_LOOKBACK_HOURS:-72}"
MAX_POSTS="${DTT_INDEX_MAX_POSTS:-120}"
WORKERS="${DTT_INDEX_WORKERS:-8}"
TIMEOUT="${DTT_INDEX_TIMEOUT:-10}"

mkdir -p "$ROOT/output"
exec /usr/bin/flock -n "$ROOT/indexing.lock" \
  "$PYTHON" "$ROOT/indexing_queue.py" \
  --site "$SITE" \
  --lookback-hours "$LOOKBACK_HOURS" \
  --max-posts "$MAX_POSTS" \
  --workers "$WORKERS" \
  --timeout "$TIMEOUT" \
  --out-dir "$ROOT/output"

#!/usr/bin/env bash
set -euo pipefail

ROOT="${DTT_INDEXING_ROOT:-/home/ubuntu/dtt-indexing-queue}"
PYTHON="${PYTHON:-/usr/bin/python3}"
SITE="${DTT_SITE:-https://doctieuthuyet.com}"
LOOKBACK_HOURS="${DTT_INDEX_LOOKBACK_HOURS:-72}"
MAX_POSTS="${DTT_INDEX_MAX_POSTS:-120}"
WORKERS="${DTT_INDEX_WORKERS:-8}"
TIMEOUT="${DTT_INDEX_TIMEOUT:-10}"
GSC_CREDENTIALS="${DTT_GSC_CREDENTIALS:-$ROOT/private/gsc-oauth.json}"
GSC_SITE_URL="${DTT_GSC_SITE_URL:-sc-domain:doctieuthuyet.com}"
GSC_LIMIT="${DTT_GSC_LIMIT:-120}"
GSC_WORKERS="${DTT_GSC_WORKERS:-4}"
GSC_ADC="${DTT_GSC_ADC:-0}"

mkdir -p "$ROOT/output"
GSC_ARGS=()
if [ "$GSC_ADC" = "1" ]; then
  GSC_ARGS+=(
    --gsc-adc
    --gsc-site-url "$GSC_SITE_URL"
    --gsc-limit "$GSC_LIMIT"
    --gsc-workers "$GSC_WORKERS"
  )
elif [ -f "$GSC_CREDENTIALS" ]; then
  GSC_ARGS+=(
    --gsc-credentials "$GSC_CREDENTIALS"
    --gsc-site-url "$GSC_SITE_URL"
    --gsc-limit "$GSC_LIMIT"
    --gsc-workers "$GSC_WORKERS"
  )
fi
exec /usr/bin/flock -n "$ROOT/indexing.lock" \
  "$PYTHON" "$ROOT/indexing_queue.py" \
  --site "$SITE" \
  --lookback-hours "$LOOKBACK_HOURS" \
  --max-posts "$MAX_POSTS" \
  --workers "$WORKERS" \
  --timeout "$TIMEOUT" \
  --out-dir "$ROOT/output" \
  "${GSC_ARGS[@]}"

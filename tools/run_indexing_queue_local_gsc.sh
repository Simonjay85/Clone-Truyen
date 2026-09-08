#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_ROOT="${DTT_GSC_LOCAL_STATE:-$HOME/.local/state/dtt-indexing-gsc}"
PYTHON="${PYTHON:-/opt/homebrew/bin/python3}"
REMOTE_HOST="${DTT_GSC_REMOTE_HOST:-templystudio}"
REMOTE_ROOT="${DTT_GSC_REMOTE_ROOT:-/home/ubuntu/dtt-indexing-queue/gsc}"

mkdir -p "$STATE_ROOT/output"
LOCK_DIR="$STATE_ROOT/run.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "gsc_local_already_running"
  exit 0
fi
trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT INT TERM

"$PYTHON" "$REPO_ROOT/tools/indexing_queue.py" \
  --site https://doctieuthuyet.com \
  --lookback-hours "${DTT_INDEX_LOOKBACK_HOURS:-72}" \
  --max-posts "${DTT_INDEX_MAX_POSTS:-120}" \
  --workers "${DTT_INDEX_WORKERS:-8}" \
  --timeout "${DTT_INDEX_TIMEOUT:-20}" \
  --out-dir "$STATE_ROOT/output" \
  --gsc-adc \
  --gsc-site-url sc-domain:doctieuthuyet.com \
  --gsc-limit "${DTT_GSC_LIMIT:-120}" \
  --gsc-workers "${DTT_GSC_WORKERS:-1}"

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
REMOTE_JSON="$REMOTE_ROOT/.latest.json.$STAMP.tmp"
REMOTE_TXT="$REMOTE_ROOT/.latest.txt.$STAMP.tmp"

/usr/bin/ssh -o BatchMode=yes "$REMOTE_HOST" "mkdir -p '$REMOTE_ROOT'"
/usr/bin/scp -q "$STATE_ROOT/output/latest.json" "$REMOTE_HOST:$REMOTE_JSON"
/usr/bin/scp -q "$STATE_ROOT/output/latest.txt" "$REMOTE_HOST:$REMOTE_TXT"
/usr/bin/ssh -o BatchMode=yes "$REMOTE_HOST" \
  "mv '$REMOTE_JSON' '$REMOTE_ROOT/latest.json' && mv '$REMOTE_TXT' '$REMOTE_ROOT/latest.txt'"

echo "gsc_local_sync_ok $STAMP"

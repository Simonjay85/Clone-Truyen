#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'planning' / 'master_manifest.json'
LEDGER = ROOT / 'continuity' / 'ledger.json'


def deep_merge(dst, src):
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            deep_merge(dst[k], v)
        else:
            dst[k] = v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('state_json', help='JSON containing start,end,entries,current_state_patch,timeline_day')
    args = ap.parse_args()
    state_path = Path(args.state_json)
    if not state_path.is_absolute():
        state_path = ROOT / state_path
    state = json.loads(state_path.read_text(encoding='utf-8'))
    start = int(state['start']); end = int(state['end'])
    if start < 1 or end > 800 or start > end:
        raise SystemExit('invalid range')
    entries = state.get('entries', [])
    nums = sorted(int(e['chapter']) for e in entries)
    if nums != list(range(start, end + 1)):
        raise SystemExit(f'entries must cover every chapter {start}-{end}; got {nums}')

    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    for n in range(start, end + 1):
        p = ROOT / f'chapters/chapter_{n:03d}.md'
        if not p.exists():
            raise SystemExit(f'missing {p}')
        heading = p.read_text(encoding='utf-8').splitlines()[0].lstrip('#').strip()
        row = manifest['chapters'][n-1]
        if int(row['chapter']) != n:
            raise SystemExit('manifest index mismatch')
        row['title'] = heading
        row['title_status'] = 'draft_locked'
        row['status'] = 'draft_passed_qa'
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')

    ledger = json.loads(LEDGER.read_text(encoding='utf-8'))
    kept = [e for e in ledger.get('entries', []) if not (start <= int(e.get('chapter', 0)) <= end)]
    kept.extend(entries)
    ledger['entries'] = sorted(kept, key=lambda e: int(e['chapter']))
    ledger['last_completed_chapter'] = max(int(ledger.get('last_completed_chapter', 0)), end)
    if 'timeline_day' in state:
        ledger['timeline_day'] = state['timeline_day']
    deep_merge(ledger.setdefault('current_state', {}), state.get('current_state_patch', {}))
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'checkpointed chapters {start:03d}-{end:03d}; ledger last={ledger["last_completed_chapter"]}')

if __name__ == '__main__':
    main()

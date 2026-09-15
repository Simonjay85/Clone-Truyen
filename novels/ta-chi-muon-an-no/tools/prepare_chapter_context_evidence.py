#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def sha(p:Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--chapter',type=int,required=True)
    args=ap.parse_args(); n=args.chapter
    if not 1 <= n <= 800: raise SystemExit('chapter must be 1..800')
    bible=ROOT/'story_bible.md'; contract=ROOT/'writer_contract.md'; manifest_p=ROOT/'planning/master_manifest.json'; ledger_p=ROOT/'continuity/ledger.json'
    manifest=json.loads(manifest_p.read_text(encoding='utf-8'))['chapters'][n-1]
    ledger=json.loads(ledger_p.read_text(encoding='utf-8'))
    prev=[]
    for k in range(max(1,n-5),n):
        cp=ROOT/f'chapters/chapter_{k:03d}.md'
        if cp.exists(): prev.append({'chapter':k,'path':str(cp.relative_to(ROOT)),'sha256':sha(cp),'title':cp.read_text(encoding='utf-8').splitlines()[0]})
    latest_review=None
    br=ROOT/'reports/block_reviews'
    if br.exists():
        cand=sorted(br.glob('*_review.md'))
        if cand: latest_review=str(cand[-1].relative_to(ROOT))
    current=ledger.get('current_state',{})
    hooks=[h for h in ledger.get('unresolved_hooks',[]) if h.get('status')!='paid']
    out=ROOT/'reports/chapter_context'/f'chapter_{n:03d}_context.md'; out.parent.mkdir(parents=True,exist_ok=True)
    lines=[f'# Chapter {n:03d} Context Evidence','',f'- story_bible.md SHA256: `{sha(bible)}`',f'- writer_contract.md SHA256: `{sha(contract)}`',f'- master_manifest.json SHA256: `{sha(manifest_p)}`',f'- continuity/ledger.json SHA256: `{sha(ledger_p)}`',f'- latest block review: `{latest_review or "none"}`','','## Manifest record','```json',json.dumps(manifest,ensure_ascii=False,indent=2),'```','','## Current state','```json',json.dumps(current,ensure_ascii=False,indent=2),'```','','## Unresolved hooks','```json',json.dumps(hooks,ensure_ascii=False,indent=2),'```','','## Required previous five full-chapter sources']
    for x in prev: lines += [f'- Ch{x["chapter"]:03d}: `{x["path"]}` — `{x["sha256"]}` — {x["title"]}']
    lines += ['','## Pre-draft review fields','- Current location/time: FILL_AFTER_READING','- Character states: FILL_AFTER_READING','- Must be new in this chapter: FILL_AFTER_READING','- Motifs/scenes NOT to repeat from previous five: FILL_AFTER_READING','- Intended state change: FILL_AFTER_READING','- Intended cliffhanger/payoff: FILL_AFTER_READING','- Confirmation: story bible + writer contract + manifest + ledger + all five prior chapters were read in full before drafting: PENDING','','> This file is evidence/checklist only. It does not replace actually reading the referenced sources.']
    out.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(out)
if __name__=='__main__': main()

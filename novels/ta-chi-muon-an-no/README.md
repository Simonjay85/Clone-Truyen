# Ta Chỉ Muốn Ăn No, Sao Lại Thành Tiên Đế?

Long-form novel workspace. Local draft only; no publish action is authorized by this folder.

## Canon files
- `story_bible.md` — character/world/power/romance/mystery canon.
- `writer_contract.md` — per-chapter and batch writing rules.
- `planning/master_manifest.json` — 800 planned chapter records / 80 sub-arcs / 16 volumes.
- `continuity/ledger.json` — evolving story state after each completed chapter.
- `chapters/chapter_NNN.md` — final prose files.
- `reports/` — QA and batch reports.
- `compiled/` — generated volume/full-novel builds.

## Safe commands
```bash
python3 novels/ta-chi-muon-an-no/planning/build_manifest.py
python3 novels/ta-chi-muon-an-no/tools/qa_novel.py --range 1-5
python3 novels/ta-chi-muon-an-no/tools/compile_novel.py
```

## Production loop
1. Read Story Bible + Writer Contract.
2. Read the next five manifest records.
3. Read the last two completed chapters and latest continuity entries.
4. Write five chapter files.
5. Update continuity ledger.
6. Run QA on that batch and fix hard failures.
7. Record Goal Runner checkpoint/evidence.
8. Continue until 800 chapters; then run global QA + compile + editorial audit.

## Hard boundary
Do not call external writing APIs from this pipeline. Do not run WordPress publishers. The active ChatGPT/Codex session authors prose; local scripts only validate, organize and compile it.

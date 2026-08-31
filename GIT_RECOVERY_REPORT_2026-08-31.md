# Git Recovery Report — 2026-08-31

## Scope and checkpoint

This report records the Git integrity recovery performed before the SEO Batch 15 continuation. The repository was inspected at `/Users/aaronnguyen/Developer/doctieuthuyet` on 2026-08-31. No `git reset --hard`, working-tree deletion, reclone-over-write, `.git` replacement, force-push, or replacement of local source files from an old remote snapshot was performed.

Filesystem checkpoint created before Git repair:

- Working tree copy: `/Users/aaronnguyen/Developer/doctieuthuyet-recovery-20260831T170817/working-tree/`
- Full `.git` copy: `/Users/aaronnguyen/Developer/doctieuthuyet-recovery-20260831T170817/git/`
- Invalid-ref evidence: `/Users/aaronnguyen/Developer/doctieuthuyet-recovery-20260831T170817/git-corruption-evidence/`
- The checkpoint contains the working tree, `.git`, generated reports, Batch 13/14 source files, Batch 15 artifacts, and uncommitted work.

Before any repair, `cmp` confirmed that the three Batch 14 runtime targets and the existing SEO reports were identical between the repository and the checkpoint copy.

## Initial observed corruption

The initial repository state was:

- Current branch: `main`
- Local `HEAD`: `67fd83de7b9906dee4e560ba62bf259f19a0bc57`
- Existing remote-tracking ref: `origin/main` at `6ec31719724b8ba8cdd28a720d7fde3717db7625`
- `git status --short --branch` failed with a bad revision range because parent object `85ec00c2e2709c759b808b88fd21b1a622b11d14` was missing.
- `git log` could not traverse the parent chain beyond `6ec31719724b8ba8cdd28a720d7fde3717db7625`.
- `git fsck --full` reported a missing reachable commit, broken tree/blob links, `refs/.DS_Store` as an invalid ref, and `refs/stash` as an invalid SHA-1 pointer to `051f3915fe769f33326df02c9270e7069bf96543`.
- The object store contained stale `tmp_pack_*` files. They were reported by `git count-objects` as garbage and had no index files.
- The index remained readable. The working tree had 22 tracked modified files and 457 untracked entries; these were preserved.

## Recovery actions

1. A first targeted fetch failed with `pack has 9 unresolved deltas` because the corrupt local object graph was used during negotiation.
2. A full `--refetch` was started, but it began transferring the complete large remote object set. It was interrupted at approximately 558 MB after the partial pack was preserved; it was not used as a source of truth.
3. A blob-filtered recovery fetch succeeded:

   ```text
   git -c protocol.version=2 fetch --refetch --filter=blob:none --no-tags --keep origin refs/heads/main:refs/remotes/recovery/origin-main
   ```

   This recovered the missing commit `85ec00c2e2709c759b808b88fd21b1a622b11d14`, created `refs/remotes/recovery/origin-main` at `c93d7d929360b211ae0365938ccb7b4bd273fb8b`, and updated `origin/main` to the same currently advertised remote SHA. Local `main` was not moved or merged.

4. `refs/stash` was checked after recovery. Its target remained absent, no stash reflog existed, and the remote did not contain the target object. The original ref file was copied to the evidence directory, then deleted with an exact-value `git update-ref -d` operation.
5. `.git/refs/.DS_Store` was copied to evidence and removed because it was macOS metadata in the ref namespace, not a valid Git ref.
6. All 25 stale/partial `tmp_pack_*` files, including the interrupted fetch pack, were moved intact to `git-corruption-evidence/temp-packs/`. They were not deleted.

## Post-repair verification

The required commands now work:

- `git status --short --branch`: works; reports `main...origin/main [ahead 4, behind 1]` plus the pre-existing modified/untracked work.
- `git rev-parse --verify HEAD`: `67fd83de7b9906dee4e560ba62bf259f19a0bc57`.
- `git log --oneline --decorate`: works and traverses 52 commits through the recovered `85ec00c` parent.
- `git diff --no-ext-diff --stat`: works and preserves the 22 tracked modifications.
- `git fsck --full --no-reflogs --connectivity-only`: no missing/broken/fatal object was reported after ref and garbage cleanup. Remaining output is limited to non-fatal dangling historical commits/trees retained by the repository.
- `git count-objects -v`: reports `garbage: 0` after the temporary packs were preserved outside `.git/objects/pack`.

The filtered recovery intentionally configured the repository as a partial/promisor clone (`remote.origin.promisor=true`, `remote.origin.partialclonefilter=blob:none`). At this checkpoint, `git rev-list --objects --missing=print HEAD` still identifies 4,311 lazy promisor blobs. They are not missing commit/tree links and `git fsck --full` treats them as promised by the configured remote. Full blob hydration was tested but deliberately not run across thousands of objects because the client fetches them one request at a time; no content or runtime verification depends on blindly hydrating the entire historical repository.

## Recovery conclusion

**Phase 0 structural Git gate: PASS with one documented non-critical promisor warning.** The local branch, commit ancestry, refs, status, log, and diff are usable; the original local source and uncommitted work remain intact. The local branch remains intentionally separate from the newer remote `main` SHA. A narrow checkpoint commit for this report has been created before proceeding, with no unrelated files staged.

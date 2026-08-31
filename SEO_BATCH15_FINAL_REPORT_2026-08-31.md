# SEO Batch 15 — Final Report

**Project:** `/Users/aaronnguyen/Developer/doctieuthuyet`

**Site:** `https://doctieuthuyet.com`

**Scope:** Hoàn Mỹ Thế Giới / Perfect World, 220-page SEO architecture, bounded theme deployment, live QA, sitemap regression, internal-link regression, Git recovery, and GSC opportunity gate

**Date:** 2026-08-31 (Asia/Ho_Chi_Minh)

## Final disposition

**NOT DONE — evidence-gated.**

The deployed breadcrumb/schema repair and all current live quality checks passed. The Batch 15 220-page cluster is present and clean on the live site. The overall Batch 15 acceptance gate is intentionally not marked `DONE` because three evidence gates remain unresolved:

1. The fresh current sitemap contains 3,923 unique URLs, while the supplied Batch 14 baseline records 4,149. The current sitemap is internally clean, but the 226-entry difference cannot be explained from the available baseline summaries because the raw 4,149-URL baseline list is not present.
2. The private Google Search Console exports required by the opportunity loop were not found. No clicks, impressions, CTR, position, search volume, index count, or traffic uplift has been invented.
3. The current 24-page pilot subset passes live QA, but the existing artifacts do not prove that this subset was gated before the remaining 196 pages were expanded. That historical pilot gate cannot be reconstructed honestly after the fact.

No mass refresh, mass rewrite, mass deletion, invented URL, noindex change, or unbounded publishing action was performed to hide any of these gaps.

## 1. Git integrity and recovery

### Recovery backup

A filesystem checkpoint was created before Git repair:

`/Users/aaronnguyen/Developer/doctieuthuyet-recovery-20260831T170817`

It contains:

- `working-tree/`: rsync copy of the working tree excluding `.git`.
- `git/`: full `.git` copy.
- `git-corruption-evidence/`: preserved invalid refs and all discovered temporary pack files, including the interrupted full-fetch pack.

The required Batch 14 source files, named SEO reports, and existing uncommitted work were compared against the checkpoint and preserved.

### Initial failure and least-destructive repair

The initial repository could not complete normal status/ref inspection. The observed errors included an unreadable parent commit `85ec00c2e2709c759b808b88fd21b1a622b11d14`, a broken `refs/stash` pointing to an unavailable object, an invalid `.git/refs/.DS_Store`, unresolved temporary pack deltas, and missing/broken objects in the initial connectivity check.

The repair used the upstream `main` ref only as a recovery source. A normal fetch was rejected because of unresolved deltas. A full refetch was interrupted and its temporary pack was preserved as evidence. The successful repair used a blob-filtered refetch into a separate recovery ref:

`git -c protocol.version=2 fetch --refetch --filter=blob:none --no-tags --keep origin refs/heads/main:refs/remotes/recovery/origin-main`

Only the confirmed-invalid local metadata was repaired: the absent upstream stash ref was removed after preserving its exact contents, and the invalid `.DS_Store` ref file was removed. The local `main` branch was not reset, force-updated, rebased, or replaced.

### Git verification after repair

| Check | Result |
|---|---|
| Current branch | `main` |
| Recovery checkpoint HEAD | `48499bafa0856573ede73f1a019b1a828c58490e` |
| Checkpoint commit | `48499ba Document Git recovery checkpoint 2026-08-31` |
| Current remote `origin/main` | `c93d7d929360b211ae0365938ccb7b4bd273fb8b` |
| Required status/rev-parse/log/diff commands | PASS |
| `git fsck --full --no-reflogs --connectivity-only` | Exit 0; no missing/broken/fatal/error/invalid problem lines; only dangling historical objects remain |
| `git diff --check` | PASS |
| `git diff --cached --check` | PASS |
| Staged files after verification | 0 |

The repository is now a partial/promisor clone (`blob:none`). Some promised historical blobs remain unhydrated; this is documented in `GIT_RECOVERY_REPORT_2026-08-31.md` and did not prevent validation of `HEAD`, the current branch, the target source files, or the live-readback work. The worktree remains intentionally dirty: the final check observed 23 tracked modifications and 1,649 untracked paths, with no mass staging or cleanup of user work.

Full recovery evidence: [GIT_RECOVERY_REPORT_2026-08-31.md](GIT_RECOVERY_REPORT_2026-08-31.md)

## 2. Canonical local/live source reconciliation

The final read-only FTP reconciliation used verified live Batch 14 source as the source-of-truth comparison. All three mandated files matched local-to-live byte-for-byte:

| File | Local SHA-256 | Live SHA-256 | Result |
|---|---|---|---|
| `tehi-theme/single-truyen.php` | `89d5fe6a93d735cb5428ae32ccab2cb93969c9c4ffe7c2e3bd4406513236cabd` | same | PASS |
| `tehi-theme/inc/dtt-seo-goal.php` | `68e8f6ad41a0bfd53de47d727cae41acf8e790d639c40b6d679eaa23339e44a5` | same | PASS |
| `tehi-theme/assets/css/single-story-premium.css` | `520d599bd91fc6e6702c49f550d1cf437b51ed39b1907a47aa792d09c65cd1d7` | same | PASS |

The visible B15 breadcrumb styling was deployed in the separately allowlisted `tehi-theme/assets/css/single-post-sync.css`; the mandated `single-story-premium.css` remained unchanged and still reconciles exactly.

Evidence: `backups/deployments/seo-b15-live-reconcile-20260831T183623/reconciliation-manifest.json`.

The following required artifacts were preserved and hash-checked without replacement:

- `SEO_BATCH11_FINAL_REPORT_2026-08-30.md` — SHA-256 `d43a05663f0ea57dc52d5ea20e4a07164881334c3a33a275f21b800b46e6a334`
- `SEO_BATCH12_FINAL_REPORT_2026-08-30.md` — SHA-256 `a36e1eaa95fb3c0ef790c7eed062744ed34c55ab09be369fb0402996d43c1a90`
- `SEO_BATCH13_CONTEXTUAL_LINKS_FINAL_REPORT_2026-08-30.md` — SHA-256 `0c645409e0601a227304c85649053f2b58fd96f7e086f8900e6288964bf94fe1`
- `SEO_BATCH14_STORY_SEO_CONVERSION_FINAL_REPORT_2026-08-31.md` — SHA-256 `e19be429811973fa00a463e643730daefa1d2eb6e0c1d3dc0956d7c78c1fbf7a`
- `SEO_BATCH15_SELECTION_MEMO_2026-08-31.md` — SHA-256 `e8b351eda694fbdf44817c41146cf442453477fd0fef7dd5a121add16f4a2459`
- `SEO_GSC_OPPORTUNITY_LOOP.md` — SHA-256 `25193d11f7d433afd9766a82db0df0e0afa0e748aaf38000868902cdf3dfca81`

## 3. Batch 15 architecture, collision, and editorial audit

The selected IP is **Hoàn Mỹ Thế Giới**. The manifest contains exactly 220 targets:

| Role | Count |
|---|---:|
| Canonical root | 1 |
| Topic subhubs | 9 |
| Intent-specific children | 210 |
| **Total** | **220** |

Child-bucket counts are: adaptation 9, characters 108, cultivation 16, factions 8, foreign-immortal 16, items 19, techniques 8, timeline 2, and world 24.

Manifest and generation checks:

- Expected articles: 220; generated articles: 220.
- Missing, extra, malformed-part, foreign-script, short-content, bad-H2, and duplicate-content groups: all zero.
- Final cluster audit: 220 rows; minimum word count 1,251; root/subhub/child word-floor failures: zero.
- Missing markers, missing H2, no-inbound, no-outbound, title/meta failures, duplicate title groups, and duplicate content groups: all zero.
- Contextual links added by the readiness artifact: 519.
- `seo-b15-publish-result-20260831.json`: total 220, created 0, already present 220, conflicts 0, failures empty. This turn did not republish the already-present 220 posts.

Collision audit against the current live WordPress inventory observed 1,637 published posts and category 179 with 220 posts:

- Exact expected target slugs present: 220/220.
- Missing target slugs: 0.
- Exact title collisions outside the expected target set: 0.
- Potential entity-intent overlaps after the narrowed audit rule: 0.
- Twelve alias-match groups were retained as manual-review leads, not treated as automatic collisions or instructions to merge, redirect, noindex, or rename.
- Two Già Thiên bridge candidates and one Thần Đông title/slug mention were recorded as controlled contextual references, not as alternate canonical owners.

Novel canon, donghua/adaptation facts, and community/reference material remain separated in the architecture audit. No verbatim novel prose was used as an editorial requirement.

Evidence:

- `output/seo-b15-final-manifest-20260831.json`
- `output/seo-b15-article-generation-audit-20260831.json`
- `output/seo-b15-final-cluster-audit-20260831.json`
- `output/seo-b15-collision-audit-live-20260831.json`
- `output/seo-b15-architecture-audit-20260831.json`

## 4. Bounded deployment and rollback safety

The pre-change source backup and hash guard were created at:

`backups/deployments/seo-b15-breadcrumb-prechange-20260831T180501`

The successful bounded operation is recorded at:

`backups/deployments/seo-b15-breadcrumb-deploy-20260831T180923`

The allowlist contained exactly:

- `tehi-theme/single.php`
- `tehi-theme/inc/dtt-seo-goal.php`
- `tehi-theme/assets/css/single-post-sync.css`

The first apply attempt uploaded and read back the files, then failed at the cache-purge import stage. The guarded exception path restored the pre-upload versions; its pre-upload hashes were verified against the pre-change backup. The corrected second apply then completed successfully.

Successful operation facts:

- Before-change SHA guard: PASS.
- Post-upload exact remote readback for all three files: PASS.
- Automatic rollback list: empty for the successful operation.
- Nginx FastCGI cache purge: attempted and successful; remaining cache entries reported as 0.
- No other files touched: true.
- Final local/live source reconciliation after deployment: exact match.

Deployment evidence: `backups/deployments/seo-b15-breadcrumb-deploy-20260831T180923/*result*.json`.

## 5. Fresh live QA

### B15 cluster crawl

`output/seo-b15-live-crawl-fresh-20260831.json` recorded:

- 220 target pages fetched and 220 rows checked.
- 210 children, 9 subhubs, and 1 root.
- HTTP, H1, self-canonical, index/follow, title, meta description, OG, JSON-LD, visible breadcrumb, answer-first, marker, and link checks: all zero issues.
- Minimum article word count 1,341; maximum 4,219.
- Unique HTML titles: 220; unique meta descriptions: 220.

The visible breadcrumb/schema repair closed the only issue found by the pre-deployment B15 crawl. The final fresh crawl has no B15 issue count.

### Representative-site QA

The 12-route representative QA passed with 0 issues, including the homepage, archives, a representative story, a chapter, existing Già Thiên/Quỷ Bí Chi Chủ/Kiếm Lai/Tiên Nghịch hubs, and B15 root/subhub/child samples.

Evidence: `output/seo-b15-representative-qa-fresh-20260831.json`.

### B15 internal-link HTTP audit

The 220 B15 source pages produced 223 unique internal page targets. Results:

- Broken or redirecting targets: 0.
- Source pages with non-200 response: 0.
- Source pages with no meaningful internal links: 0.
- B15 pages with no cluster outbound links: 0.
- B15 pages with no cluster inbound links: 0.

Evidence: `output/seo-b15-internal-link-http-audit-fresh-20260831.json`.

### Full published-post internal-link regression

The fresh full-post audit matched the supplied Batch 14 baseline:

- Published posts checked: 1,637.
- Unique internal destinations: 1,637.
- Broken targets: 0.
- Redirecting targets: 0.
- Posts with no outbound internal link: 0.
- Published posts with no inbound link from the post corpus: 0.

Evidence: `output/seo-b15-full-post-internal-link-audit-fresh-20260831.json`.

## 6. Full sitemap regression and unresolved count drift

The current fresh crawl fetched 25 child sitemaps plus the sitemap index, for 26 sitemap files total. It found 3,923 raw entries and 3,923 unique entries, and crawled all 3,923 rows.

Current family counts:

- Post sitemaps: 1,634.
- Page sitemap: 11.
- Truyện sitemaps: 225.
- Chương sitemaps: 2,026.
- Category sitemap: 1.
- `the_loai` sitemap: 26.

All current quality counters were zero: sitemap fetch failures, duplicate sitemap URLs, initial/final non-200 responses, redirects, noindex, nofollow, missing/mismatched canonical, title-range failures, description-range failures, missing or multiple H1, missing OG image, JSON-LD schema errors, and request errors.

However, the supplied Batch 14 server evidence at `/home/ubuntu/dtt-deploy-backups/seo-b14-final-qa-20260831T093734/` records 4,149 raw and unique sitemap entries across the same 26-file shape. The fresh current result is therefore **226 entries lower**.

The server backup directory contains summary artifacts, not the raw 4,149-URL list. The available evidence cannot establish whether 226 URLs are missing, whether the older count included stale entries, or which sitemap family accounts for the difference. Accordingly:

- Count parity: BLOCKED.
- Quality regression proven: false.
- URL invention/deletion/noindex/mass refresh to force parity: not performed.

Evidence: `output/seo-b15-full-sitemap-crawl-fresh-20260831.json` and `output/seo-b15-sitemap-count-drift-20260831.json`.

## 7. GSC Opportunity Gate

The prescribed `tools/gsc_opportunity_loop.py` and `SEO_GSC_OPPORTUNITY_LOOP.md` were checked. The repository, Downloads, and Desktop searches found no private DTT GSC export containing the required performance columns.

Recorded state:

`BLOCKED_MISSING_PRIVATE_GSC_EXPORT`

Property scope: `sc-domain:doctieuthuyet.com`.

Required inputs remain:

- 28-day Search results Performance export with Query, Page, Clicks, Impressions, CTR, and Position.
- 90-day Search results Performance export with the same columns.
- Page indexing export or screenshot.
- Sitemaps export or screenshot.

The opportunity loop was not run against unrelated GA4, template, or third-party CSV files. No metric, opportunity, index count, or traffic conclusion was produced.

Evidence: `output/gsc-opportunity-status-20260831.json`.

## 8. Pilot gate status

The defined current subset was:

- 1 root.
- 3 subhubs: characters, world, adaptation.
- 20 children.
- 24 pages total.

All 24 selected pages are live and passed the current QA subset with no issues. The artifact explicitly records `pre_expansion_evidence_available: false` because the publish result already showed all 220 pages present and does not prove that the 24-page subset was approved before the remaining pages were expanded.

Evidence: `output/seo-b15-pilot-qa-20260831.json`.

## 9. Acceptance matrix

| Gate | State | Evidence |
|---|---|---|
| Git recovery, backup, structural fsck, checkpoint | PASS | `GIT_RECOVERY_REPORT_2026-08-31.md` |
| Required local/live source reconciliation | PASS | `backups/deployments/seo-b15-live-reconcile-20260831T183623/reconciliation-manifest.json` |
| 220-item architecture and collision audit | PASS | B15 manifest, architecture, collision, and cluster audit JSON files |
| B15 current live SEO/HTML QA | PASS | `output/seo-b15-live-crawl-fresh-20260831.json` |
| Representative-site QA | PASS | `output/seo-b15-representative-qa-fresh-20260831.json` |
| B15 internal-link HTTP audit | PASS | `output/seo-b15-internal-link-http-audit-fresh-20260831.json` |
| Full published-post internal-link regression | PASS | `output/seo-b15-full-post-internal-link-audit-fresh-20260831.json` |
| PHP lint / Python compile / Git diff checks | PASS | Final command verification on 2026-08-31 |
| GSC opportunity gate | BLOCKED | `BLOCKED_MISSING_PRIVATE_GSC_EXPORT` |
| Full sitemap quality | PASS | 3,923/3,923 current rows, all quality counters 0 |
| Full sitemap count parity with Batch 14 | BLOCKED | 3,923 current vs 4,149 baseline, delta -226 |
| Historical pilot-before-expansion proof | NOT PROVABLE | `pre_expansion_evidence_available: false` |
| Overall Batch 15 completion | **NOT DONE** | Evidence gates above remain open |

## 10. Safe continuation criteria

To close the remaining gates without weakening the evidence standard:

1. Supply the raw Batch 14 4,149-URL sitemap list, or produce an equivalent trusted snapshot from the same baseline run. Diff it against the current 3,923 URL list and classify every delta before considering any repair.
2. Supply the private 28-day and 90-day GSC exports plus Page indexing and Sitemaps evidence. Run the existing opportunity loop, preserving its real labels and source provenance.
3. Treat the current 24-page pilot as a passed live subset validation only. Do not rewrite history to claim a pre-expansion gate that the artifacts cannot prove.
4. If a sitemap repair is later justified, use the existing bounded backup/hash/allowlist/rollback pattern, then rerun the full sitemap crawl and full post internal-link audit before changing the final disposition.

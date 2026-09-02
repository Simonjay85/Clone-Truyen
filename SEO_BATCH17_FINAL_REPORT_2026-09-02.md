# SEO Batch 17 — Thánh Khư Final Report

**Date:** 2026-09-02
**Site:** https://doctieuthuyet.com
**Scope:** Thánh Khư / The Sacred Ruins knowledge cluster, pilot-gated publish, runtime SEO integration, full-site regression QA.

## Final disposition

**Batch 17: DONE.**

The 180-page Thánh Khư cluster is live and the final technical acceptance gates pass. No unresolved Batch 17 SEO regression remains.

## 1. Architecture and generation

- Total pages: **180**
- Root hub: **1**
- Topic subhubs: **9**
- Child articles: **170**
- Live slug collisions before publish: **0/180**
- Local generation QA: **PASS 180/180**
- Minimum article word count after bounded polish: **659**
- Median article word count: **1129.5**
- H2 minimum: **5**
- Missing/extra slug, title mismatch, source-ref mismatch, title/meta/excerpt length, H1-in-content, H2 floor, word floor, foreign-script residue, process-language residue, missing root/parent links, self-links, exact duplicates and 16-word source overlap: **all 0**.

Evidence:
- `output/seo-b17-manifest-validation.json`
- `output/seo-b17-generation-qa-final-20260902.json`
- `output/seo-b17-generated-180-final-20260902.json`
- `output/seo-b17-live-collision-audit-20260902.json`

## 2. Pilot gate

A bounded 24-page pilot was published first:

- 1 root
- 3 subhubs
- 20 children
- Created: **24/24**
- Conflict: **0**
- Failure: **0**
- Pilot pages PASS: **24/24**
- Broken internal targets: **0**
- Redirecting internal targets: **0**
- `/category/thanh-khu/` correctly returns **301** to `/thanh-khu-wiki/`
- Pilot pages in sitemap: **24/24**
- Category alias in sitemap: **false**

Pilot rollback IDs and pre-full SHA/content snapshots were stored before expansion.

Evidence:
- `output/seo-b17-pilot-publish-result-20260902.json`
- `output/seo-b17-pilot-live-qa-20260902.json`
- `output/seo-b17-pilot-state-before-full-20260902.json`
- `backups/deployments/seo-b17-pilot-20260902T022159/`

## 3. Full publish

The remaining expansion was applied in six bounded chunks with SHA guards for the 24 pilot posts.

- Initial pilot creates: **24**
- Full-phase new creates: **156**
- Pilot posts upgraded to full graph: **24**
- Conflict: **0**
- SHA mismatch: **0**
- Failed mutations: **0**
- Final live cluster state: **180 posts**
- Full markers: **180**
- Pilot markers remaining: **0**
- Cluster metadata mismatch: **0**
- Final role counts: root 1 / subhub 9 / child 170

One post contained a canonical internal-link alias after expansion. It was changed from `/he-thong-tien-hoa-thanh-khu/` to `/he-thong-tien-hoa-thanh-khu-thanh-khu/` under a one-post SHA guard; subsequent QA returned zero redirecting internal links.

Evidence:
- `output/seo-b17-full-apply-summary-20260902.json`
- `output/seo-b17-live-final-state-20260902.json`
- `output/seo-b17-linkfix-result-20260902.json`
- `backups/deployments/seo-b17-full-20260902T022700/`

## 4. Runtime SEO integration

Category ID **180** (`thanh-khu`) was integrated into the existing SEO runtime:

- category canonical redirect → `/thanh-khu-wiki/` via a B17-scoped SEO hook
- category sitemap exclusion via a B17-scoped Rank Math sitemap guard
- unique cluster OG/social-card mapping
- answer-first hub mapping
- canonical BreadcrumbList support for category-180 posts

The existing live Batch 16 Hoàn Mỹ FAQ schema hook was preserved during reconciliation.

Final local/live SHA-256 matches:

- `tehi-theme/functions.php` — `a339bfe23365d9c508dce0a58e9b041a552d7eb4d590d97132bfd30c6c72300e`
- `tehi-theme/inc/dtt-seo-goal.php` — `ec291f6ebf47294801fb05568aa3142fe722b2730143f46ba1d9d94d207eaa58`
- `tehi-theme/inc/dtt-seo-batch2.php` — `e94347b909e6a659162699f4a91dfab0954de53a3db9d48d1cc2a94d7f817bc7`

PHP lint PASS and `git diff --check` PASS on target runtime files. FastCGI cache was purged after deployment and after the canonical-link fix.

## 5. Batch 17 live QA

B17-specific final rendered QA:

- Pages checked: **180**
- Passed: **180**
- Page issue rows: **0**
- Unique internal targets: **199**
- Broken targets: **0**
- Redirecting targets: **0**
- B17 URLs in sitemap: **180/180**
- Category alias in sitemap: **false**

DB read-back also matched the approved payload exactly for all 180 posts, including content SHA, SEO title, description, focus keyword, category, role and bucket metadata.

## 6. Full-site sitemap regression

Namespace-correct final crawl:

- Sitemap index: **200**
- Child sitemaps: **26**
- Non-200 sitemap files: **0**
- Canonical page URLs: **4103**
- Duplicate page URLs: **0**
- Image `<image:loc>` entries: **226**
- URLs crawled: **4103**
- Tracked issue counters: **0**
- Result: **PASS**

This is the expected expansion from the prior 3,923 canonical page URLs to **4,103** after adding 180 Thánh Khư pages.

Evidence: `output/seo-b17-full-sitemap-crawl-final-20260902.json` (final runtime); the earlier pre-housekeeping crawl is preserved separately.

## 7. Full published-post internal-link regression

Across all published regular posts after Batch 17:

- Published posts: **1817**
- Unique internal page targets: **1817**
- Posts with no outbound internal links: **0**
- Posts with no inbound link from the post corpus: **0**
- Broken internal targets: **0**
- Redirecting internal targets: **0**
- Result: **PASS**

Evidence: `output/seo-b17-full-post-internal-link-audit-20260902.json`.

## 8. Representative regression

Representative live routes covered homepage, `/truyen/`, `/bai-viet/`, story detail, chapter detail, Già Thiên, Quỷ Bí Chi Chủ, Kiếm Lai, Tiên Nghịch, Hoàn Mỹ Thế Giới, and Thánh Khư root/subhub/child pages.

- Routes checked: **13**
- Passed: **13**
- Issues: **0**
- Result: **PASS**

Evidence: `output/seo-b17-representative-regression-20260902.json`.

## 9. External GSC gate

Private DTT Google Search Console 28-day/90-day exports are still unavailable. No clicks, impressions, CTR, position, ranking or traffic uplift is invented. This remains a separate opportunity-analysis phase and is **not** a Batch 17 technical-completion blocker.

## Final acceptance

**DONE** — Batch 17 content, pilot gate, full publish, runtime integration, B17 live QA, 4,103-URL sitemap crawl, 1,817-post internal-link regression, representative regression, cache purge and local/live runtime reconciliation all pass.

# Changelog

## 4.2.0 - 2026-08-19

- Added `/patch-post-content`, `/bulk-patch-post-content`, `/upsert-post-related-links`, `/bulk-set-rank-math-meta`, `/bulk-set-post-terms`, `/find-posts-linking-to`, `/audit-post-internal-links`, and `/bulk-audit-post-internal-links`.
- Normal-post writes now support `expected_modified_gmt` and return `CONTENT_CONFLICT` details when the read version is stale.
- `update-post` duplicate checks are explicit-field-only and always exclude the post being updated.
- Normal-post list/search and category/tag responses include bounded pagination metadata.
- Content patch read-back verifies that immutable post identity/status, taxonomy, author, and SEO state were preserved.
- Related-link and internal-link operations normalize URLs, reject unsafe schemes, inspect actual anchor targets, and keep bulk failures independent.
- Health now reports bridge version 4.2.0, tool count 64, and normal-post editing capabilities.

Tests are fixture-only. No live WordPress content was changed.

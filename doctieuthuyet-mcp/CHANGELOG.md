# Changelog

## 4.2.0 - 2026-08-19

- Added the eight normal-post content, SEO, taxonomy, related-links, backlink, and internal-link-audit tools; the MCP registry is now exactly 64 unique tools.
- Hardened `update_post` duplicate validation so omitted title/slug fields are not checked, the current post is always excluded, and content/excerpt-only edits do not manufacture identity conflicts.
- Added `expected_modified_gmt` optimistic locking to normal-post content, SEO, and taxonomy writes with `CONTENT_CONFLICT` details containing expected and actual timestamps.
- Added bounded pagination metadata to normal-post list/search and category/tag routes.
- Added read-back verification for exact content patches, including preservation checks for status, identity, author, taxonomy, and SEO metadata.
- Added fixture coverage for unsafe related-link URLs, idempotent related blocks, independent bulk results, backlink resolution, self/broken/duplicate links, and orphan summaries.
- Updated service/bridge health metadata, version documentation, and the MU-plugin deployment source to the same 4.2.0 implementation.

No production WordPress content or live database was modified by this release's tests.

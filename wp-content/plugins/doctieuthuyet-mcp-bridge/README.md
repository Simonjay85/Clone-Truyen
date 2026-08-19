# DocTieuThuyet MCP Bridge v4.2.0

Version 4.2.0 preserves the v3 truyen/chuong routes and provides a fixed, capability-checked workflow for normal WordPress posts, image media, `category`/`post_tag`, Rank Math/Yoast SEO fields, bounded content patches, related-reading blocks, and internal-link auditing. Media upload accepts MCP file payloads (`filename`, `mime_type`, `data_base64`) only; arbitrary filesystem paths and arbitrary post meta are not supported. Publishing is always a separate explicit route, and deletion moves normal posts to Trash.

This WordPress bridge provides the guarded backend for the DTT MCP workflow:

`create draft -> read -> update content -> validate -> pre-publish -> publish -> verify -> audit`

The bridge is deliberately narrow. It is not a generic WordPress REST proxy and it does not expose SQL, PHP execution, arbitrary post types, arbitrary taxonomies, arbitrary meta writes, or hard delete operations.

## Routes

All routes are `POST` under `/wp-json/doctieuthuyet-mcp/v1` and return the standard envelope:

```json
{
  "ok": true,
  "request_id": "request-id",
  "data": {},
  "warnings": [],
  "error": null
}
```

### Reads and lookups

- `/health`
- `/list-recent`
- `/get-truyen`
- `/get-chuong`
- `/list-the-loai`
- `/list-chuong-by-truyen`
- `/get-story-package`
- `/find-truyen`
- `/find-chuong`
- `/validate-truyen`
- `/validate-chuong`
- `/check-story-integrity`
- `/get-post`
- `/list-posts`
- `/search-posts`
- `/get-post-terms`
- `/get-rank-math-meta`
- `/find-posts-linking-to`
- `/audit-post-internal-links`
- `/bulk-audit-post-internal-links`

### Draft and content writes

- `/create-truyen`
- `/create-chuong`
- `/create-story-package`
- `/update-truyen`
- `/update-chuong`
- `/update-truyen-status`
- `/update-chuong-status`
- `/upsert-truyen`
- `/upsert-chuong`
- `/bulk-upsert-chapters`
- `/create-post`
- `/update-post`
- `/patch-post-content`
- `/bulk-patch-post-content`
- `/upsert-post-related-links`
- `/set-post-terms`
- `/bulk-set-post-terms`
- `/update-seo-meta`
- `/set-rank-math-meta`
- `/bulk-set-rank-math-meta`
- `/publish-post`
- `/unpublish-post`
- `/trash-post`
- `/delete-post`

Creates always force `post_status=draft`. A request with `status=publish`, `status=pending`, or any other non-draft create status returns `CREATE_STATUS_FORBIDDEN`. Content updates reject `status` and `schedule_at`; status changes are separate routes. A status update may use `draft`, `pending`, `private`, or `future`, but `publish` is rejected outside the explicit publish routes.

### Normal-post, media, taxonomy, and SEO routes

- `/create-post`, `/get-post`, `/update-post`, `/list-posts`, `/search-posts`
- `/publish-post`, `/unpublish-post`, `/trash-post`, `/delete-post`
- `/upload-media`, `/get-media`, `/search-media`, `/find-media`, `/set-featured-image`, `/remove-featured-image`, `/update-media-metadata`
- `/list-categories`, `/search-categories`, `/create-category`, `/list-tags`, `/search-tags`, `/create-tag`, `/get-post-terms`, `/set-post-terms`
- `/update-seo-meta`, `/get-rank-math-meta`, `/set-rank-math-meta`
- `/patch-post-content`, `/bulk-patch-post-content`, `/upsert-post-related-links`
- `/bulk-set-rank-math-meta`, `/bulk-set-post-terms`
- `/find-posts-linking-to`, `/audit-post-internal-links`, `/bulk-audit-post-internal-links`

Normal-post collection routes expose `pagination` with `page`, `per_page`, `returned`, `total_items`, and `total_pages`; legacy `count`/`items` fields remain present. The bridge health payload reports `version: 4.2.0`, `tool_count: 64`, and the exposed WordPress editing capabilities.

### Confirmation-token publish writes

- `/pre-publish-story-package`
- `/publish-truyen`
- `/publish-chuong`
- `/publish-story-package`
- `/unpublish-truyen`
- `/unpublish-chuong`

`/pre-publish-story-package` validates the exact story and chapter set and creates a short-lived, one-time token. The token is bound to `truyen_id`, sorted `chapter_ids`, and a SHA-256 `content_version` containing the current content, status, modified time, and chapter numbers. Any content/status change invalidates the token.

### Normal-post v4.2 operations

Normal-post routes are fixed to `post` and return pagination metadata where a collection is returned. `create-post` is draft-only. `update-post` only checks duplicate identity when `title` or `slug` is explicitly supplied, excludes the current post from every duplicate query, and allows content/excerpt-only edits without a duplicate check. It returns `modified` and `modified_gmt`. All content, SEO, and taxonomy writes accept optional `expected_modified_gmt`; a mismatch returns `CONTENT_CONFLICT` with `expected_modified_gmt` and `actual_modified_gmt` and performs no write.

`patch-post-content` supports `append`, `prepend`, `replace_exact`, `insert_before`, `insert_after`, `remove_exact`, and exact-ID `replace_section_id`. It sanitizes the inserted fragment, uses bounded exact matching, reads the post back, and verifies status, title, slug, author, taxonomy, and SEO metadata are unchanged. The bulk patch/SEO/taxonomy routes process bounded independent operations and return per-item success or failure results.

`upsert-post-related-links` creates or updates one identified HTML block, deduplicates normalized URLs, preserves the post status, and rejects unsafe URL schemes. The link finder and auditors inspect actual anchor `href` values, normalize internal URLs, report broken/self/duplicate links, exclude a target post's own self-link from backlink sources, and never mutate content.

The `/health` response identifies `plugin`, `version`, `tool_count: 64`, and the normal-post editing capabilities. This bridge source is mirrored into the repository's MU-plugin deployment surface; use one active copy in production.

## Existing data contract

The bridge writes only these known structures:

- post types: `truyen`, `chuong`
- taxonomy: `the_loai`
- relation meta: `_truyen_id`

The v4 normal-post surface additionally uses the fixed `post` type, WordPress `category` and `post_tag`, and provider-specific Rank Math/Yoast keys already owned by the active SEO plugin. The normal-post tools never accept an arbitrary post type, taxonomy, or meta key.

No new relationship or chapter-number meta key is written. The current site can opt in to an already-existing key through a narrow filter:

```php
add_filter('dttmcp_existing_meta_key', function ($key, $field, $post_type) {
    if ($field === 'chapter_number' && $post_type === 'chuong') {
        return '_the_existing_chapter_number_key';
    }
    return $key;
}, 10, 3);
```

The example is a placeholder only: replace it with a key confirmed from the live website before enabling it. Without a mapping, chapter ordering uses a title pattern such as `Chương 12` and returns `CHAPTER_NUMBER_META_MAPPING_NOT_CONFIGURED_TITLE_FALLBACK_USED`. The bridge never invents a new `_dtt_*` field.

`story_status` and SEO writes are similarly disabled unless explicit existing-key mappings are supplied. All HTML content passes through `wp_kses_post`. Terms, titles, slugs, IDs, schedules, and statuses are separately sanitized/validated.

## Authentication and permissions

Configure a long random bridge token outside the repository, normally in `wp-config.php` or the hosting secret manager:

```php
define('DOCTIEUTHUYET_MCP_TOKEN', getenv('DOCTIEUTHUYET_MCP_TOKEN'));
define('DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS', true);
```

Callers send:

```http
Authorization: Bearer <bridge-token>
Content-Type: application/json
X-Request-ID: <safe-request-id>
```

The token is compared with `hash_equals`. It is never included in responses, audit events, or logs. With `DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS=true`:

- reads require `read`
- create/content/status writes require `edit_posts`
- publish/unpublish writes require `publish_posts`

The `dttmcp_permission_check` filter can provide a narrowly scoped service-account decision. It must return a boolean and must not become a generic REST bypass.

## Idempotency and optimistic locking

`/create-story-package` and `/publish-story-package` accept an optional `idempotency_key`. The bridge stores a fingerprinted envelope for the bounded TTL. Retrying the same key and request replays the stored result with `IDEMPOTENT_REPLAY`; changing the request with the same key returns `IDEMPOTENCY_CONFLICT`.

`/update-truyen`, `/update-chuong`, status updates, and unpublish accept `expected_modified_gmt`. A mismatch returns `OPTIMISTIC_LOCK_CONFLICT` and does not write. Normal-post content, taxonomy, and SEO writes use the same optimistic-locking idea and return `CONTENT_CONFLICT` with the expected and actual timestamps.

## Package publish and rollback

`/publish-story-package` performs this sequence:

1. Validate the package and consume the one-time confirmation token.
2. Snapshot each post status and publish date.
3. Publish the story.
4. Publish chapters in numeric order, using the safe existing-number mapping or title fallback.
5. Read each changed post back and verify its status.
6. If any write/read-back fails, restore the snapshots in reverse order and return detailed per-post results plus `rolled_back=true` when compensation succeeded.

On `PUBLISH_ROLLBACK_FAILED`, stop and inspect the audit event and returned post details. Do not blindly retry. The consumed token is not reusable; after the data is reconciled, run pre-publish again for a new token. `unpublish` only sets a post to `draft`; it never deletes content.

## Audit events

Every successful or failed create, update, status, publish, unpublish, package, and token issuance operation emits `dttmcp_audit_log` with a safe event containing:

- component and action
- request ID
- target post IDs
- success flag
- sanitized outcome code
- rollback detail when relevant

The default error log intentionally omits request bodies, HTML, tokens, headers, SQL, and PHP. Production deployments should route the `dttmcp_audit_log` action to their existing audit sink with appropriate retention.

## Fixture tests

The bridge fixture defines a fake WordPress store in memory and never connects to a live site:

```bash
php -l doctieuthuyet-mcp-bridge.php
php tests/bridge-fixture.test.php
```

It covers health, get/update story and chapter, normal-post duplicate hardening, content-only updates, optimistic locking, exact content patch operations, related-links idempotency and URL validation, independent bulk writes, taxonomy omission/clear semantics, backlink resolution, internal-link audits, invalid IDs, permission denial, taxonomy lookup, idempotency and duplicate package requests, pre-publish validation, successful package publish, partial package publish failure with compensating rollback, one-time token use, unpublish, integrity checks, sanitization, relation preservation, audit events, and the absence of a hard-delete route.

## Installation boundary

Use exactly one active copy of this bridge: the normal plugin or the MU-plugin copy, according to the deployment’s established path. Do not activate both copies as separate code revisions. This source update is local and fixture-verified; it does not deploy to WordPress or publish/edit real content. A production rollout must deploy a reviewed allowlist, then verify remote health, route auth, and read-back behavior before any real write is considered available.

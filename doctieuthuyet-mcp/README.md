# DTT MCP v4.1.1

`doctieuthuyet-mcp` is the local MCP service for the DocTieuThuyet story workflow. It exposes a fixed, typed tool surface and forwards only allowlisted operations to the WordPress bridge.

This release implements the intended lifecycle:

`create draft -> read -> update content -> validate -> pre-publish -> publish -> read-back verify -> audit`

The repository is local-first. The tests use fixtures and do not publish or edit real WordPress content. Deploying the Node service or either WordPress bridge copy is a separate, explicitly approved action.

## Runtime

- MCP HTTP endpoint: `POST /mcp`
- Diagnostics: `GET /health`
- Default local port: `8792`
- Node: `>=20`
- Service version: `4.1.1`

The MCP service authenticates its caller with `MCP_BEARER_TOKEN`. The WordPress client uses a separate `WP_BRIDGE_TOKEN`; neither token is returned by health checks or written to logs. Every bridge call receives an `X-Request-ID` and every tool returns the same response envelope.

## Standard response envelope

```json
{
  "ok": true,
  "request_id": "2d99f5c4-8e3f-4a9d-9e2f-3bc8e0f6c9aa",
  "data": {},
  "warnings": [],
  "error": null
}
```

Failures use the same shape:

```json
{
  "ok": false,
  "request_id": "2d99f5c4-8e3f-4a9d-9e2f-3bc8e0f6c9aa",
  "data": {},
  "warnings": [],
  "error": {
    "code": "OPTIMISTIC_LOCK_CONFLICT",
    "message": "The post was modified after the caller read it.",
    "details": {
      "expected_modified_gmt": "2026-08-11 10:00:01",
      "actual_modified_gmt": "2026-08-11 10:00:02"
    }
  }
}
```

`request_id` is generated at the MCP boundary, forwarded to WordPress, and returned even when the bridge is unreachable or authentication fails. Errors are normalized without exposing raw headers, tokens, SQL, PHP, or upstream stack traces.

## MCP tools

The v4.1 discovery contract exposes exactly 56 unique tools. The Node registration and the MCP `tools/list` response are tested against the same catalog; the bridge does not hide a tool because a provider or optional capability is unavailable. A provider-dependent call returns a standard error envelope instead.

### Story and chapter workflow

`health_check`, `list_recent_truyen`, `list_recent_chuong`, `get_truyen`, `get_chuong`, `list_the_loai`, `list_chuong_by_truyen`, `get_story_package`, `create_truyen_draft`, `create_chuong_draft`, `update_truyen`, `update_chuong`, `update_truyen_status`, `update_chuong_status`, `create_story_package_draft`, `pre_publish_story_package`, `publish_truyen`, `publish_chuong`, `publish_story_package`, `unpublish_truyen`, `unpublish_chuong`, `check_story_integrity`.

`create_story_package_draft` always creates draft content. If a package chapter omits `chapter_number`, v4.1 assigns sequential numbers starting at 1; the title does not need a numeric prefix. If a later chapter fails, the bridge attempts to permanently remove only the newly created package drafts and returns `PACKAGE_ROLLED_BACK`; an incomplete rollback is reported explicitly as `PARTIAL_FAILURE` with IDs.

### Normal WordPress posts

`create_post_draft`, `get_post`, `update_post`, `list_posts`, `search_posts`, `publish_post`, `unpublish_post`, `trash_post`, `delete_post`.

These tools are fixed to post type `post`. Creation is draft-only and preserves Gutenberg-compatible HTML through the WordPress HTML sanitizer. `delete_post` is a safe compatibility name for moving a post to WordPress Trash; permanent deletion is not exposed. `search_posts` accepts `query`, `title`, and/or `slug`, plus `status` and the fixed `post_type: "post"`, and returns `id`, `title`, `slug`, `status`, `post_type`, `link`, and related list metadata.

### Taxonomy

`list_categories`, `search_categories`, `create_category`, `list_tags`, `search_tags`, `create_tag`, `get_post_terms`, `set_post_terms`.

Normal posts use WordPress `category` and `post_tag`. `set_post_terms` accepts category and tag ID arrays independently and only replaces the taxonomy fields explicitly supplied by the caller.

### Rank Math SEO

`get_rank_math_meta`, `set_rank_math_meta`, `update_seo_meta`.

The focused Rank Math tools support partial updates for SEO title, meta description, focus keyword, canonical URL, the four supported robots combinations, and optional Facebook/Twitter title, description, and image fields. The generic tool remains available for the detected supported provider; no arbitrary post meta is exposed.

### Media

`upload_media`, `get_media`, `search_media`, `find_media`, `set_featured_image`, `remove_featured_image`, `update_media_metadata`.

Only JPEG, PNG, and WebP uploads are accepted after filename, declared MIME, and actual image-content checks. `remove_featured_image` removes the relationship only; it does not delete the attachment.

### Backward-compatible lookup, upsert, and validation

`find_truyen`, `find_chuong`, `upsert_truyen`, `upsert_chuong`, `bulk_upsert_chapters`, `validate_truyen`, `validate_chuong`.

All tools above use fixed allowlists and the same response envelope. No tool can select an arbitrary post type, taxonomy, REST path, or meta key.

## Schemas and safe workflow

### 1. Create drafts

Create tools do not expose a publish status. The Node client always sends `status: "draft"` as a defense-in-depth marker, and the bridge rejects any create request containing a status other than `draft`.

```json
{
  "title": "Fixture Story",
  "content": "<p>A sanitized story description.</p>",
  "excerpt": "Short description",
  "genres": [12, "Fantasy"]
}
```

A chapter draft is linked to the existing story relationship:

```json
{
  "truyen_id": 101,
  "chapter_number": 1,
  "title": "Chương 1",
  "content": "<p>Chapter content.</p>"
}
```

A package accepts one story and one or more chapters. `idempotency_key` is optional but recommended for retries. A replay with the same key and identical request returns the original result; reusing the key for different content returns `IDEMPOTENCY_CONFLICT`.

### 2. Read and update

`get_truyen`, `get_chuong`, and `get_story_package` return `modified_gmt`. Pass that value back as `expected_modified_gmt` to make an update conditional:

```json
{
  "truyen_id": 101,
  "title": "Fixture Story - revised",
  "expected_modified_gmt": "2026-08-11 10:00:01"
}
```

Content updates and status updates are separate actions. `update_truyen` and `update_chuong` reject `status` and `schedule_at`. Use `update_truyen_status` or `update_chuong_status` for non-publish statuses (`draft`, `pending`, `private`, `future`). `publish` is rejected by those endpoints and is available only through the confirmation-token publish tools.

### 3. Validate and issue a confirmation token

```json
{
  "truyen_id": 101,
  "chapter_ids": [202, 203]
}
```

`pre_publish_story_package` checks the allowlisted post types, the fixed `_truyen_id` relation, chapter numbering/content, duplicate identities, and story validity. On success it returns:

- `confirmation_token`
- `expires_at`
- `truyen_id`
- sorted `chapter_ids`
- `content_version`

The token is stored server-side, expires after a short TTL, is deleted on first consumption, and is bound to the exact story, chapter set, and SHA-256 content/status version. Any edit after pre-publish validation requires a new token.

### 4. Publish and verify

```json
{
  "truyen_id": 101,
  "chapter_ids": [202, 203],
  "confirmation_token": "returned-by-pre-publish",
  "idempotency_key": "publish-101-v1"
}
```

`publish_story_package` snapshots the current post statuses and publish dates, publishes the story first, then chapters in numeric order. It reads each post back after every write. The response includes per-post results, `verified`, and `rolled_back`:

```json
{
  "ok": true,
  "data": {
    "truyen_id": 101,
    "chapter_ids": [202, 203],
    "results": {
      "truyen": {"id": 101, "ok": true, "status_after": "publish"},
      "chapters": [
        {"id": 202, "chapter_number": 1, "ok": true, "status_after": "publish"},
        {"id": 203, "chapter_number": 2, "ok": true, "status_after": "publish"}
      ]
    },
    "rolled_back": false,
    "verified": true
  },
  "warnings": [],
  "error": null
}
```

If a later write fails, the bridge restores the snapshot for every post already changed and reports `PUBLISH_ROLLED_BACK` or `PUBLISH_ROLLBACK_FAILED`. A rollback failure is an operational stop condition: do not retry blindly; inspect the detailed response and WordPress audit event first. A consumed token is never reused.

`unpublish_truyen` and `unpublish_chuong` set status back to `draft` and never delete a post. `check_story_integrity` is read-only.

## WordPress data contract

The bridge writes only the existing allowlisted structures:

- post types: `truyen`, `chuong`
- taxonomy: `the_loai`
- relationship meta: `_truyen_id`
- optional chapter-number, story-status, and SEO mappings only when the deployment supplies an explicit `dttmcp_existing_meta_key` or `dttmcp_seo_meta_keys` mapping to an already-used key

No new relationship or chapter-number meta key is created by this release. If no existing chapter-number key is mapped, the bridge derives a safe fallback from titles such as `Chương 12` and returns a warning. This preserves the current website schema until its exact field/meta usage is confirmed.

Content is sanitized with `wp_kses_post`; titles, slugs, IDs, statuses, terms, and schedule values are validated separately. Arbitrary post types, taxonomies, meta writes, REST forwarding, SQL, PHP execution, and hard-delete operations are not exposed.

## Configuration

Copy `.env.example` and supply secrets through the process environment or a secret manager:

```dotenv
PORT=8792
MCP_BEARER_TOKEN=replace-with-mcp-secret
WP_BRIDGE_BASE_URL=https://example.invalid/wp-json/doctieuthuyet-mcp/v1
WP_BRIDGE_TOKEN=replace-with-wordpress-bridge-secret
WP_REQUEST_TIMEOUT_MS=20000
DTT_MAX_BULK_CHAPTERS=50
DTT_MCP_VERSION=4.1.1
```

Do not commit `.env`, print tokens, or put credentials in fixture data. The bridge token and MCP token are intentionally separate trust boundaries.

## Permissions

The MCP bearer token authenticates the service caller. The bridge bearer token authenticates the service-to-WordPress hop. WordPress capability checks are opt-in because some existing deployments use a service-level token boundary:

```php
define('DOCTIEUTHUYET_MCP_TOKEN', getenv('DOCTIEUTHUYET_MCP_TOKEN'));
define('DOCTIEUTHUYET_MCP_REQUIRE_WP_CAPS', true);
```

When capability checks are enabled, reads require `read`, draft/content writes require `edit_posts`, and publish/unpublish writes require `publish_posts`. A deployment may provide `dttmcp_permission_check` for a narrowly scoped service account decision. Permission-denied attempts return `PERMISSION_DENIED` and are included in the bridge audit stream.

## Tests

All tests are fixture-only and do not call a live WordPress site:

```bash
npm install
npm test
php -l ../wp-content/plugins/doctieuthuyet-mcp-bridge/doctieuthuyet-mcp-bridge.php
php ../wp-content/plugins/doctieuthuyet-mcp-bridge/tests/bridge-fixture.test.php
```

The Node suite covers auth, health, tool registration, fixed endpoints, envelope normalization, permission/locking/idempotency errors, draft enforcement, publish confirmation forwarding, unpublish, and invalid IDs. The PHP fixture covers health, reads/updates, invalid IDs, permission denial, optimistic locking, taxonomy lookup, package idempotency, pre-publish validation, successful package publish, one-time token use, partial failure rollback, unpublish, story integrity, sanitization, relation preservation, hard-delete absence, and audit events.

## Deployment boundary

A passing local build or fixture is not proof of a deployed bridge, provider acceptance, public WordPress behavior, or a real publish. Before any production rollout, package the exact built `dist`, inspect the allowlisted source files, deploy only the reviewed MCP and bridge copies, then perform remote health/read-back verification. Do not use the fixture to connect to or mutate real content.

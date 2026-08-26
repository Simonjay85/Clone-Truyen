import assert from "node:assert/strict";
import { test } from "node:test";
import { registerTools } from "../dist/tools.js";

function registry(resultFor = {}) {
  const tools = new Map();
  const calls = [];
  const client = {
    health: async (_context) => resultFor.health ?? { ok: true, request_id: "health", data: { mcp: "online" }, warnings: [], error: null },
    call: async (endpoint, body, context) => {
      calls.push({ endpoint, body, context });
      return resultFor[endpoint] ?? { ok: true, request_id: context.requestId, data: { endpoint, body }, warnings: [], error: null };
    },
  };
  registerTools({ tool(name, description, schema, handler) { tools.set(name, { name, description, schema, handler }); } }, client);
  return { tools, calls };
}

async function invoke(value, name, input) {
  assert.equal(value.tools.has(name), true, `missing tool ${name}`);
  return value.tools.get(name).handler(input);
}

function body(result) {
  return JSON.parse(result.content[0].text);
}

test("phase 1 and phase 2 tools are all registered", () => {
  const r = registry();
  for (const name of [
    "get_truyen", "get_chuong", "update_truyen", "update_chuong", "list_the_loai", "list_chuong_by_truyen", "get_story_package",
    "pre_publish_story_package", "publish_truyen", "publish_chuong", "publish_story_package", "unpublish_truyen", "unpublish_chuong", "check_story_integrity",
  ]) assert.equal(r.tools.has(name), true, `missing ${name}`);
});

test("v4 post, media, taxonomy and SEO tools are registered on fixed routes", async () => {
  const r = registry();
  const names = [
    "create_post_draft", "get_post", "update_post", "list_posts", "search_posts", "publish_post", "unpublish_post", "trash_post", "delete_post",
    "upload_media", "get_media", "search_media", "set_featured_image", "remove_featured_image", "update_media_metadata", "find_media",
    "list_categories", "search_categories", "list_tags", "search_tags", "get_post_terms", "set_post_terms", "create_category", "create_tag", "update_seo_meta", "get_rank_math_meta", "set_rank_math_meta",
  ];
  for (const name of names) assert.equal(r.tools.has(name), true, `missing ${name}`);
  assert.equal(r.tools.size, 56, "the complete v4.1 catalog must be registered");
  assert.equal(new Set(r.tools.keys()).size, r.tools.size, "tool names must be unique");

  await invoke(r, "create_post_draft", { title: "Article", content: "<p>Draft</p>", categories: [2], tags: [3] });
  assert.equal(r.calls.at(-1).endpoint, "/create-post");
  assert.equal(r.calls.at(-1).body.status, "draft");
  assert.equal("status" in r.tools.get("create_post_draft").schema, false);

  await invoke(r, "set_featured_image", { post_id: 10, media_id: 0 });
  assert.deepEqual(r.calls.at(-1).body, { post_id: 10, media_id: 0 });
  await invoke(r, "set_post_terms", { post_id: 10, categories: [2] });
  assert.deepEqual(r.calls.at(-1).body, { post_id: 10, categories: [2] });
  assert.equal("tags" in r.calls.at(-1).body, false);

  await invoke(r, "delete_post", { post_id: 10 });
  assert.equal(r.calls.at(-1).endpoint, "/delete-post");
  await invoke(r, "remove_featured_image", { post_id: 10 });
  assert.equal(r.calls.at(-1).endpoint, "/remove-featured-image");
  await invoke(r, "get_media", { media_id: 11 });
  await invoke(r, "search_media", { query: "cover" });
  await invoke(r, "search_categories", { query: "news" });
  await invoke(r, "search_tags", { query: "seo" });
  await invoke(r, "get_post_terms", { post_id: 10 });
  await invoke(r, "get_rank_math_meta", { post_id: 10 });
  await invoke(r, "set_rank_math_meta", { post_id: 10, seo_title: "SEO title" });
  assert.deepEqual(r.calls.slice(-9).map((item) => item.endpoint), [
    "/delete-post", "/remove-featured-image", "/get-media", "/search-media", "/search-categories", "/search-tags", "/get-post-terms", "/get-rank-math-meta", "/set-rank-math-meta",
  ]);
});

test("v4 schemas reject filesystem paths, unsafe MIME values and unsupported robots directives", () => {
  const r = registry();
  const fileSchema = r.tools.get("upload_media").schema.file;
  assert.equal(fileSchema.safeParse({ path: "/tmp/image.png" }).success, false);
  assert.equal(fileSchema.safeParse({ filename: "x.svg", mime_type: "image/svg+xml", data_base64: "abcdefghijklmnop" }).success, false);
  assert.equal(fileSchema.safeParse({ filename: "x.webp", mime_type: "image/webp", data_base64: "abcdefghijklmnop" }).success, true);
  const robots = r.tools.get("update_seo_meta").schema.robots;
  assert.equal(robots.safeParse("noindex,nofollow").success, true);
  assert.equal(robots.safeParse("noarchive,all").success, false);
});

test("create actions force draft and do not expose status input", async () => {
  const r = registry();
  await invoke(r, "create_truyen_draft", { title: "Draft story", content: "<p>x</p>" });
  assert.deepEqual(r.calls.at(-1).body, { title: "Draft story", content: "<p>x</p>", status: "draft" });
  await invoke(r, "create_chuong_draft", { truyen_id: 10, chapter_number: 1, title: "Chương 1", content: "x" });
  assert.equal(r.calls.at(-1).body.status, "draft");
  assert.equal("status" in r.tools.get("create_truyen_draft").schema, false);
});

test("content and status updates use separate endpoints", async () => {
  const r = registry();
  await invoke(r, "update_truyen", { truyen_id: 10, title: "Changed", expected_modified_gmt: "2026-08-11T01:02:03" });
  assert.equal(r.calls.at(-1).endpoint, "/update-truyen");
  assert.equal("status" in r.calls.at(-1).body, false);
  await invoke(r, "update_truyen_status", { truyen_id: 10, status: "pending" });
  assert.equal(r.calls.at(-1).endpoint, "/update-truyen-status");
  assert.equal(r.calls.at(-1).body.status, "pending");
});

test("read, taxonomy, package and integrity routes use fixed allowlisted endpoints", async () => {
  const r = registry();
  await invoke(r, "get_truyen", { truyen_id: 10 });
  await invoke(r, "get_chuong", { chuong_id: 20 });
  await invoke(r, "list_the_loai", { per_page: 20 });
  await invoke(r, "list_chuong_by_truyen", { truyen_id: 10 });
  await invoke(r, "get_story_package", { truyen_id: 10 });
  await invoke(r, "check_story_integrity", { truyen_id: 10 });
  assert.deepEqual(r.calls.map((item) => item.endpoint).slice(-6), [
    "/get-truyen", "/get-chuong", "/list-the-loai", "/list-chuong-by-truyen", "/get-story-package", "/check-story-integrity",
  ]);
});

test("idempotency keys and confirmation token are forwarded without mutation", async () => {
  const r = registry();
  await invoke(r, "create_story_package_draft", {
    story_title: "Package",
    chapters: [{ chapter_number: 1, title: "Chương 1", content: "x" }],
    idempotency_key: "create-key-1",
  });
  assert.equal(r.calls.at(-1).body.idempotency_key, "create-key-1");
  await invoke(r, "pre_publish_story_package", { truyen_id: 10, chapter_ids: [20, 21] });
  assert.equal(r.calls.at(-1).endpoint, "/pre-publish-story-package");
  await invoke(r, "publish_story_package", { truyen_id: 10, chapter_ids: [20, 21], confirmation_token: "token", idempotency_key: "publish-key-1" });
  assert.equal(r.calls.at(-1).body.confirmation_token, "token");
  assert.equal(JSON.stringify(r.calls).includes("Bearer"), false);
});

test("package drafts assign missing chapter numbers without parsing the title", async () => {
  const r = registry();
  await invoke(r, "create_story_package_draft", {
    story_title: "Unnumbered package",
    chapters: [{ title: "Opening scene", content: "one" }, { title: "The return", content: "two" }, { chapter_number: 9, title: "Bonus", content: "nine" }],
  });
  assert.deepEqual(r.calls.at(-1).body.chapters.map((chapter) => chapter.chapter_number), [1, 2, 9]);
  assert.equal(r.calls.at(-1).body.chapters[0].title, "Opening scene");
});

test("publish and unpublish are explicit writes", async () => {
  const r = registry();
  await invoke(r, "publish_truyen", { truyen_id: 10, chapter_ids: [], confirmation_token: "token" });
  await invoke(r, "publish_chuong", { chuong_id: 20, truyen_id: 10, chapter_ids: [20], confirmation_token: "token" });
  await invoke(r, "unpublish_truyen", { truyen_id: 10 });
  await invoke(r, "unpublish_chuong", { chuong_id: 20 });
  assert.deepEqual(r.calls.map((item) => item.endpoint).slice(-4), ["/publish-truyen", "/publish-chuong", "/unpublish-truyen", "/unpublish-chuong"]);
});

test("invalid IDs are rejected by MCP schemas", () => {
  const r = registry();
  assert.equal(r.tools.get("get_truyen").schema.truyen_id.safeParse(0).success, false);
  assert.equal(r.tools.get("get_chuong").schema.chuong_id.safeParse(-1).success, false);
  assert.equal(r.tools.get("publish_story_package").schema.chapter_ids.safeParse([]).success, false);
});

test("permission denied, optimistic conflict and duplicate package errors stay in the standard envelope", async () => {
  const denied = registry({ "/update-truyen": { ok: false, request_id: "r1", data: null, warnings: [], error: { code: "PERMISSION_DENIED", message: "no" } } });
  const deniedResult = await invoke(denied, "update_truyen", { truyen_id: 10, title: "x" });
  assert.equal(deniedResult.isError, true);
  assert.equal(body(deniedResult).error.code, "PERMISSION_DENIED");

  const conflict = registry({ "/update-chuong": { ok: false, request_id: "r2", data: null, warnings: [], error: { code: "OPTIMISTIC_LOCK_CONFLICT", message: "changed" } } });
  const conflictResult = await invoke(conflict, "update_chuong", { chuong_id: 20, content: "x", expected_modified_gmt: "old" });
  assert.equal(body(conflictResult).error.code, "OPTIMISTIC_LOCK_CONFLICT");

  const duplicate = registry({ "/create-story-package": { ok: false, request_id: "r3", data: null, warnings: [], error: { code: "DUPLICATE_PACKAGE", message: "duplicate" } } });
  const duplicateResult = await invoke(duplicate, "create_story_package_draft", { story_title: "same", chapters: [{ title: "Chương 1", content: "x" }] });
  assert.equal(body(duplicateResult).error.code, "DUPLICATE_PACKAGE");
});

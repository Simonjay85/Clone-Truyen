import { randomUUID } from "crypto";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { config } from "./config.js";
import {
  errorToEnvelope,
  normalizeEnvelope,
  type StandardEnvelope,
  type WordPressBridgeClient,
  wpBridge,
} from "./wp-bridge.js";

const statusSchema = z.enum(["draft", "pending", "private", "future"]);
const postListStatusSchema = z.enum(["draft", "publish", "pending", "private", "any"]);
const idempotencySchema = z.string().trim().min(1).max(200);
const expectedModifiedSchema = z.string().trim().min(1).max(80);
const termValueSchema = z.union([
  z.number().int().positive(),
  z.string().trim().min(1).max(120),
]);

const seoSchema = z.object({
  title: z.string().trim().max(300).optional(),
  description: z.string().trim().max(500).optional(),
  focus_keyword: z.string().trim().max(160).optional(),
  canonical_url: z.string().url().max(2048).optional(),
}).partial().optional();

const storyFields = {
  title: z.string().trim().min(1).max(300).optional(),
  slug: z.string().trim().min(1).max(200).optional(),
  content: z.string().optional().describe("HTML story description/content."),
  description: z.string().optional().describe("Alias for content."),
  excerpt: z.string().optional(),
  author: z.number().int().positive().optional().describe("Existing WordPress author ID."),
  genres: z.array(termValueSchema).max(30).optional().describe("Existing the_loai term IDs or names."),
  the_loai: z.array(termValueSchema).max(30).optional(),
  tags: z.array(z.string().trim().min(1).max(120)).max(50).optional(),
  story_status: z.string().trim().max(80).optional().describe("Only accepted when an explicit existing meta mapping is configured."),
  featured_image: z.number().int().positive().optional().describe("Existing WordPress attachment ID."),
  seo: seoSchema,
};

const chapterFields = {
  truyen_id: z.number().int().positive().optional(),
  chapter_number: z.number().int().positive().optional(),
  title: z.string().trim().min(1).max(300).optional(),
  slug: z.string().trim().min(1).max(200).optional(),
  content: z.string().optional(),
  seo: seoSchema,
};

const chapterDraftSchema = z.object({
  chapter_number: z.number().int().positive().optional(),
  title: z.string().trim().min(1).max(300),
  slug: z.string().trim().min(1).max(200).optional(),
  content: z.string().optional(),
  seo: seoSchema,
});

const postIdSchema = z.number().int().positive();
const patchOperationSchema = z.enum([
  "append",
  "prepend",
  "replace_exact",
  "insert_before",
  "insert_after",
  "remove_exact",
  "replace_section_id",
]);
const postFields = {
  title: z.string().trim().min(1).max(300),
  content: z.string(),
  excerpt: z.string().optional(),
  slug: z.string().trim().min(1).max(200).optional(),
  categories: z.array(postIdSchema).max(100).optional(),
  tags: z.array(postIdSchema).max(100).optional(),
};
const seoPostSchema = {
  post_id: postIdSchema,
  seo_title: z.string().trim().max(300).optional(),
  meta_description: z.string().trim().max(500).optional(),
  focus_keyword: z.string().trim().max(160).optional(),
  canonical_url: z.string().url().max(2048).optional(),
  robots: z.enum(["index,follow", "noindex,follow", "index,nofollow", "noindex,nofollow"]).optional(),
  expected_modified_gmt: expectedModifiedSchema.optional(),
};

const rankMathFields = {
  seo_title: seoPostSchema.seo_title,
  meta_description: seoPostSchema.meta_description,
  focus_keyword: seoPostSchema.focus_keyword,
  canonical_url: seoPostSchema.canonical_url,
  robots: seoPostSchema.robots,
  facebook_title: z.string().trim().max(300).optional(),
  facebook_description: z.string().trim().max(500).optional(),
  facebook_image: z.string().url().max(2048).optional(),
  twitter_title: z.string().trim().max(300).optional(),
  twitter_description: z.string().trim().max(500).optional(),
  twitter_image: z.string().url().max(2048).optional(),
};

const patchOperationFields = {
  post_id: postIdSchema,
  operation: patchOperationSchema,
  html: z.string().max(500_000).optional(),
  needle: z.string().max(100_000).optional(),
  occurrence: z.number().int().positive().max(10_000).optional(),
  section_id: z.string().trim().min(1).max(120).optional(),
  expected_modified_gmt: expectedModifiedSchema.optional(),
};

const patchOperationObject = z.object(patchOperationFields);
const relatedLinkObject = z.object({
  url: z.string().trim().min(1).max(2048),
  anchor: z.string().trim().min(1).max(300),
  description: z.string().max(1_000).optional(),
});
const rankMathOperationObject = z.object({
  post_id: postIdSchema,
  ...rankMathFields,
  expected_modified_gmt: expectedModifiedSchema.optional(),
});
const termsOperationObject = z.object({
  post_id: postIdSchema,
  categories: z.array(postIdSchema).max(100).optional(),
  tags: z.array(postIdSchema).max(100).optional(),
  expected_modified_gmt: expectedModifiedSchema.optional(),
});

type ToolResult = {
  content: Array<{ type: "text"; text: string }>;
  isError?: boolean;
};

function compact<T extends Record<string, unknown>>(value: T): Record<string, unknown> {
  return Object.fromEntries(Object.entries(value).filter(([, item]) => item !== undefined));
}

function storyPayload(input: Record<string, unknown>, forceStatus?: "draft"): Record<string, unknown> {
  const { description, ...rest } = input;
  const content = rest.content ?? description;
  return compact({ ...rest, ...(content !== undefined ? { content } : {}), ...(forceStatus ? { status: forceStatus } : {}) });
}

function chapterPayload(input: Record<string, unknown>, forceStatus?: "draft"): Record<string, unknown> {
  return compact({ ...input, ...(forceStatus ? { status: forceStatus } : {}) });
}

function idContext(id: number): { targetId: number } {
  return { targetId: id };
}

function standardize(value: unknown, requestId: string): StandardEnvelope {
  return normalizeEnvelope(value, requestId);
}

function textResult(value: StandardEnvelope, isError = false): ToolResult {
  return {
    content: [{ type: "text", text: JSON.stringify(value, null, 2) }],
    ...(isError ? { isError: true } : {}),
  };
}

async function executeTool(
  toolName: string,
  operation: string,
  action: (requestId: string) => Promise<unknown>
): Promise<ToolResult> {
  const requestId = randomUUID();
  try {
    const result = standardize(await action(requestId), requestId);
    if (!result.ok) {
      console.error(JSON.stringify({ component: "mcp-tool", tool: toolName, operation, request_id: requestId, success: false, code: result.error?.code }));
    }
    return textResult(result, !result.ok);
  } catch (error) {
    const envelope = errorToEnvelope(error, requestId);
    console.error(JSON.stringify({ component: "mcp-tool", tool: toolName, operation, request_id: requestId, success: false, code: envelope.error?.code }));
    return textResult(envelope, true);
  }
}

function call(
  client: WordPressBridgeClient,
  endpoint: string,
  body: Record<string, unknown>,
  operation: string,
  requestId: string,
  targetId?: number,
  tool?: string
): Promise<unknown> {
  return client.call(endpoint, body, { operation, requestId, ...(tool ? { tool } : {}), ...(targetId ? { targetId } : {}) });
}

/** Register the legacy surface plus the complete draft/read/update/publish/audit workflow. */
export function registerTools(server: McpServer, client: WordPressBridgeClient = wpBridge): void {
  server.tool(
    "health_check",
    "Return safe MCP and WordPress bridge diagnostics. Tokens and raw headers are never returned.",
    {},
    async () => executeTool("health_check", "health", (requestId) => client.health({ operation: "health_check", tool: "health_check", requestId }))
  );

  server.tool(
    "list_recent_truyen",
    "List recent stories using the fixed truyen post type.",
    { per_page: z.number().int().min(1).max(100).optional() },
    async ({ per_page }) => executeTool("list_recent_truyen", "list_recent_truyen", (requestId) => call(client, "/list-recent", { post_type: "truyen", per_page: per_page ?? 10 }, "list_recent_truyen", requestId, undefined, "list_recent_truyen"))
  );

  server.tool(
    "list_recent_chuong",
    "List recent chapters, optionally scoped to one truyen.",
    { per_page: z.number().int().min(1).max(100).optional(), truyen_id: z.number().int().positive().optional() },
    async ({ per_page, truyen_id }) => executeTool("list_recent_chuong", "list_recent_chuong", (requestId) => call(client, "/list-recent", compact({ post_type: "chuong", per_page: per_page ?? 10, truyen_id }), "list_recent_chuong", requestId, truyen_id, "list_recent_chuong"))
  );

  server.tool(
    "get_truyen",
    "Read one complete truyen by ID, including modified_gmt for optimistic locking.",
    { truyen_id: z.number().int().positive() },
    async ({ truyen_id }) => executeTool("get_truyen", "get_truyen", (requestId) => call(client, "/get-truyen", { truyen_id }, "get_truyen", requestId, truyen_id, "get_truyen"))
  );

  server.tool(
    "get_chuong",
    "Read one complete chuong by ID, including its verified _truyen_id relationship and modified_gmt.",
    { chuong_id: z.number().int().positive() },
    async ({ chuong_id }) => executeTool("get_chuong", "get_chuong", (requestId) => call(client, "/get-chuong", { chuong_id }, "get_chuong", requestId, chuong_id, "get_chuong"))
  );

  server.tool(
    "list_the_loai",
    "Look up the allowlisted the_loai taxonomy only.",
    { search: z.string().trim().max(120).optional(), per_page: z.number().int().min(1).max(100).optional() },
    async ({ search, per_page }) => executeTool("list_the_loai", "list_the_loai", (requestId) => call(client, "/list-the-loai", compact({ search, per_page: per_page ?? 100 }), "list_the_loai", requestId, undefined, "list_the_loai"))
  );

  server.tool(
    "list_chuong_by_truyen",
    "List chapters belonging to one truyen, numerically ordered when a verified chapter-number mapping exists and otherwise by safe title fallback.",
    { truyen_id: z.number().int().positive(), per_page: z.number().int().min(1).max(200).optional() },
    async ({ truyen_id, per_page }) => executeTool("list_chuong_by_truyen", "list_chuong_by_truyen", (requestId) => call(client, "/list-chuong-by-truyen", { truyen_id, per_page: per_page ?? 200 }, "list_chuong_by_truyen", requestId, truyen_id, "list_chuong_by_truyen"))
  );

  server.tool(
    "get_story_package",
    "Read a story and all related chapters through the verified _truyen_id relationship.",
    { truyen_id: z.number().int().positive(), per_page: z.number().int().min(1).max(200).optional() },
    async ({ truyen_id, per_page }) => executeTool("get_story_package", "get_story_package", (requestId) => call(client, "/get-story-package", { truyen_id, per_page: per_page ?? 200 }, "get_story_package", requestId, truyen_id, "get_story_package"))
  );

  server.tool(
    "create_truyen_draft",
    "Create a new story. The bridge always forces draft and rejects any non-draft status.",
    { ...storyFields, title: z.string().trim().min(1).max(300) },
    async (input) => executeTool("create_truyen_draft", "create_truyen", (requestId) => call(client, "/create-truyen", storyPayload(input, "draft"), "create_truyen", requestId, undefined, "create_truyen_draft"))
  );

  server.tool(
    "create_chuong_draft",
    "Create a new chapter draft linked to a truyen. No publish status is accepted.",
    { ...chapterFields, truyen_id: z.number().int().positive(), title: z.string().trim().min(1).max(300) },
    async (input) => executeTool("create_chuong_draft", "create_chuong", (requestId) => call(client, "/create-chuong", chapterPayload(input, "draft"), "create_chuong", requestId, input.truyen_id, "create_chuong_draft"))
  );

  server.tool(
    "update_truyen",
    "Update story content/metadata only. Status changes are deliberately unavailable here; use update_truyen_status or a publish/unpublish tool. expected_modified_gmt prevents overwrites.",
    { truyen_id: z.number().int().positive(), ...storyFields, expected_modified_gmt: expectedModifiedSchema.optional() },
    async ({ truyen_id, expected_modified_gmt, ...input }) => executeTool("update_truyen", "update_truyen", (requestId) => call(client, "/update-truyen", compact({ truyen_id, ...storyPayload(input), expected_modified_gmt }), "update_truyen", requestId, truyen_id, "update_truyen"))
  );

  server.tool(
    "update_chuong",
    "Update chapter content/relationship metadata only. Status changes are a separate action. expected_modified_gmt prevents overwrites.",
    { chuong_id: z.number().int().positive(), ...chapterFields, expected_modified_gmt: expectedModifiedSchema.optional() },
    async ({ chuong_id, expected_modified_gmt, ...input }) => executeTool("update_chuong", "update_chuong", (requestId) => call(client, "/update-chuong", compact({ chuong_id, ...chapterPayload(input), expected_modified_gmt }), "update_chuong", requestId, chuong_id, "update_chuong"))
  );

  server.tool(
    "update_truyen_status",
    "Change a story status without changing content. publish is rejected here and requires a confirmation token.",
    { truyen_id: z.number().int().positive(), status: statusSchema, schedule_at: z.string().trim().max(80).optional(), expected_modified_gmt: expectedModifiedSchema.optional() },
    async ({ truyen_id, ...input }) => executeTool("update_truyen_status", "update_truyen_status", (requestId) => call(client, "/update-truyen-status", { truyen_id, ...input }, "update_truyen_status", requestId, truyen_id, "update_truyen_status"))
  );

  server.tool(
    "update_chuong_status",
    "Change a chapter status without changing content. publish is rejected here and requires a confirmation token.",
    { chuong_id: z.number().int().positive(), status: statusSchema, schedule_at: z.string().trim().max(80).optional(), expected_modified_gmt: expectedModifiedSchema.optional() },
    async ({ chuong_id, ...input }) => executeTool("update_chuong_status", "update_chuong_status", (requestId) => call(client, "/update-chuong-status", { chuong_id, ...input }, "update_chuong_status", requestId, chuong_id, "update_chuong_status"))
  );

  server.tool(
    "create_story_package_draft",
    "Create a story and chapters as drafts only. idempotency_key makes retries safe; duplicate content is still rejected.",
    {
      story: z.object(storyFields).optional(),
      story_title: z.string().trim().min(1).max(300).optional(),
      story_intro: z.string().optional(),
      story_excerpt: z.string().optional(),
      the_loai: z.array(termValueSchema).max(30).optional(),
      chapters: z.array(chapterDraftSchema).min(1).max(config.maxBulkChapters),
      idempotency_key: idempotencySchema.optional(),
    },
    async ({ story, story_title, story_intro, story_excerpt, the_loai, chapters, idempotency_key }) => executeTool("create_story_package_draft", "create_story_package", (requestId) => {
      const packageStory = story ?? { title: story_title, content: story_intro, excerpt: story_excerpt, the_loai };
      return call(client, "/create-story-package", {
        story: storyPayload(packageStory, "draft"),
        chapters: chapters.map((chapter, index) => chapterPayload({
          ...chapter,
          chapter_number: chapter.chapter_number ?? index + 1,
        }, "draft")),
        ...(idempotency_key ? { idempotency_key } : {}),
      }, "create_story_package", requestId, undefined, "create_story_package_draft");
    })
  );

  server.tool(
    "pre_publish_story_package",
    "Validate a fixed story/chapter set and issue a short-lived one-time confirmation token bound to IDs and content version.",
    { truyen_id: z.number().int().positive(), chapter_ids: z.array(z.number().int().positive()).max(200) },
    async ({ truyen_id, chapter_ids }) => executeTool("pre_publish_story_package", "pre_publish_story_package", (requestId) => call(client, "/pre-publish-story-package", { truyen_id, chapter_ids }, "pre_publish_story_package", requestId, truyen_id, "pre_publish_story_package"))
  );

  server.tool(
    "publish_truyen",
    "Publish one story only with a confirmation token created by pre_publish_story_package. Token IDs and content version must match.",
    { truyen_id: z.number().int().positive(), chapter_ids: z.array(z.number().int().positive()).default([]), confirmation_token: z.string().trim().min(1).max(300) },
    async (input) => executeTool("publish_truyen", "publish_truyen", (requestId) => call(client, "/publish-truyen", input, "publish_truyen", requestId, input.truyen_id, "publish_truyen"))
  );

  server.tool(
    "publish_chuong",
    "Publish one chapter only with a one-time confirmation token created for that exact story/chapter set.",
    { chuong_id: z.number().int().positive(), truyen_id: z.number().int().positive(), chapter_ids: z.array(z.number().int().positive()).length(1), confirmation_token: z.string().trim().min(1).max(300) },
    async (input) => executeTool("publish_chuong", "publish_chuong", (requestId) => call(client, "/publish-chuong", input, "publish_chuong", requestId, input.chuong_id, "publish_chuong"))
  );

  server.tool(
    "publish_story_package",
    "Publish story first and chapters in numeric order with snapshot, compensating rollback, detailed per-post results, and read-back verification.",
    { truyen_id: z.number().int().positive(), chapter_ids: z.array(z.number().int().positive()).min(1).max(200), confirmation_token: z.string().trim().min(1).max(300), idempotency_key: idempotencySchema.optional() },
    async (input) => executeTool("publish_story_package", "publish_story_package", (requestId) => call(client, "/publish-story-package", input, "publish_story_package", requestId, input.truyen_id, "publish_story_package"))
  );

  server.tool(
    "unpublish_truyen",
    "Move a story back to draft without deleting it. Optional optimistic lock protects concurrent edits.",
    { truyen_id: z.number().int().positive(), expected_modified_gmt: expectedModifiedSchema.optional() },
    async (input) => executeTool("unpublish_truyen", "unpublish_truyen", (requestId) => call(client, "/unpublish-truyen", input, "unpublish_truyen", requestId, input.truyen_id, "unpublish_truyen"))
  );

  server.tool(
    "unpublish_chuong",
    "Move a chapter back to draft without deleting it. Optional optimistic lock protects concurrent edits.",
    { chuong_id: z.number().int().positive(), expected_modified_gmt: expectedModifiedSchema.optional() },
    async (input) => executeTool("unpublish_chuong", "unpublish_chuong", (requestId) => call(client, "/unpublish-chuong", input, "unpublish_chuong", requestId, input.chuong_id, "unpublish_chuong"))
  );

  server.tool(
    "check_story_integrity",
    "Check story/chapter relationships, duplicate numeric chapter identities, and missing content without mutation.",
    { truyen_id: z.number().int().positive(), chapter_ids: z.array(z.number().int().positive()).max(200).optional() },
    async (input) => executeTool("check_story_integrity", "check_story_integrity", (requestId) => call(client, "/check-story-integrity", input, "check_story_integrity", requestId, input.truyen_id, "check_story_integrity"))
  );

  // v4 normal post/media/taxonomy/SEO workflow. Status changes remain explicit.
  server.tool("create_post_draft", "Create a normal WordPress post as draft only; duplicate slug/title identities are rejected.", {
    title: postFields.title, content: postFields.content, excerpt: postFields.excerpt, slug: postFields.slug,
    categories: postFields.categories, tags: postFields.tags,
  }, async (input) => executeTool("create_post_draft", "create_post", (requestId) => call(client, "/create-post", { ...input, status: "draft" }, "create_post", requestId, undefined, "create_post_draft")));

  server.tool("get_post", "Read the complete editable state of one normal WordPress post, including SEO metadata when available.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("get_post", "get_post", (requestId) => call(client, "/get-post", { post_id }, "get_post", requestId, post_id, "get_post")));
  server.tool("update_post", "Update only explicitly supplied post fields; never changes status. expected_modified_gmt prevents overwriting a newer edit.", {
    post_id: postIdSchema, title: postFields.title.optional(), content: z.string().optional(), excerpt: z.string().optional(), slug: postFields.slug, expected_modified_gmt: expectedModifiedSchema.optional(),
  }, async ({ post_id, ...input }) => executeTool("update_post", "update_post", (requestId) => call(client, "/update-post", { post_id, ...input }, "update_post", requestId, post_id, "update_post")));
  server.tool("list_posts", "List normal WordPress posts with bounded pagination and total counts.", { per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional(), status: postListStatusSchema.optional() }, async (input) => executeTool("list_posts", "list_posts", (requestId) => call(client, "/list-posts", { per_page: input.per_page ?? 20, page: input.page ?? 1, status: input.status ?? "draft" }, "list_posts", requestId, undefined, "list_posts")));
  server.tool("search_posts", "Search normal posts by keyword/content, exact title, or slug. The post_type is fixed to post.", { query: z.string().trim().min(1).max(200).optional(), title: z.string().trim().min(1).max(300).optional(), slug: z.string().trim().min(1).max(200).optional(), post_type: z.literal("post").optional(), status: postListStatusSchema.optional(), per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional(), exclude_post_id: postIdSchema.optional() }, async (input) => executeTool("search_posts", "search_posts", (requestId) => call(client, "/search-posts", { ...input, post_type: "post", status: input.status ?? "any", per_page: input.per_page ?? 20, page: input.page ?? 1 }, "search_posts", requestId, undefined, "search_posts")));
  server.tool("publish_post", "Explicitly publish one normal post after review.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("publish_post", "publish_post", (requestId) => call(client, "/publish-post", { post_id }, "publish_post", requestId, post_id, "publish_post")));
  server.tool("unpublish_post", "Move one normal post back to draft.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("unpublish_post", "unpublish_post", (requestId) => call(client, "/unpublish-post", { post_id }, "unpublish_post", requestId, post_id, "unpublish_post")));
  server.tool("trash_post", "Move one normal post to WordPress Trash; permanent deletion is unavailable.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("trash_post", "trash_post", (requestId) => call(client, "/trash-post", { post_id }, "trash_post", requestId, post_id, "trash_post")));
  server.tool("delete_post", "Safely delete one normal post by moving it to WordPress Trash; permanent deletion is unavailable.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("delete_post", "delete_post", (requestId) => call(client, "/delete-post", { post_id }, "delete_post", requestId, post_id, "delete_post")));

  server.tool("upload_media", "Upload an image supplied through MCP as base64 file data; filesystem paths are not accepted.", {
    file: z.object({ filename: z.string().trim().min(1).max(255), mime_type: z.enum(["image/jpeg", "image/png", "image/webp"]), data_base64: z.string().min(16).max(14_000_000) }),
    title: z.string().trim().max(300).optional(), alt_text: z.string().trim().max(300).optional(), caption: z.string().max(1000).optional(), description: z.string().max(5000).optional(),
  }, async (input) => executeTool("upload_media", "upload_media", (requestId) => call(client, "/upload-media", input, "upload_media", requestId, undefined, "upload_media")));
  server.tool("set_featured_image", "Set or remove a normal post featured image; media_id 0 removes it.", { post_id: postIdSchema, media_id: z.number().int().min(0) }, async (input) => executeTool("set_featured_image", "set_featured_image", (requestId) => call(client, "/set-featured-image", input, "set_featured_image", requestId, input.post_id, "set_featured_image")));
  server.tool("update_media_metadata", "Update allowlisted image SEO metadata.", { media_id: postIdSchema, title: z.string().trim().max(300).optional(), alt_text: z.string().trim().max(300).optional(), caption: z.string().max(1000).optional(), description: z.string().max(5000).optional() }, async (input) => executeTool("update_media_metadata", "update_media_metadata", (requestId) => call(client, "/update-media-metadata", input, "update_media_metadata", requestId, input.media_id, "update_media_metadata")));
  server.tool("find_media", "Find existing image attachments before uploading duplicates.", { query: z.string().trim().min(1).max(200), per_page: z.number().int().min(1).max(100).optional() }, async (input) => executeTool("find_media", "find_media", (requestId) => call(client, "/find-media", { ...input, per_page: input.per_page ?? 20 }, "find_media", requestId, undefined, "find_media")));
  server.tool("search_media", "Search existing image attachments by filename, title, or content.", { query: z.string().trim().min(1).max(200), per_page: z.number().int().min(1).max(100).optional() }, async (input) => executeTool("search_media", "search_media", (requestId) => call(client, "/search-media", { ...input, per_page: input.per_page ?? 20 }, "search_media", requestId, undefined, "search_media")));
  server.tool("get_media", "Read one existing image attachment with its metadata and URL.", { media_id: postIdSchema }, async ({ media_id }) => executeTool("get_media", "get_media", (requestId) => call(client, "/get-media", { media_id }, "get_media", requestId, media_id, "get_media")));
  server.tool("remove_featured_image", "Remove the featured image from one normal post without deleting the media attachment.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("remove_featured_image", "remove_featured_image", (requestId) => call(client, "/remove-featured-image", { post_id }, "remove_featured_image", requestId, post_id, "remove_featured_image")));
  server.tool("list_categories", "List normal post categories only with bounded pagination and totals.", { search: z.string().trim().max(120).optional(), per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional() }, async (input) => executeTool("list_categories", "list_categories", (requestId) => call(client, "/list-categories", { ...input, per_page: input.per_page ?? 100, page: input.page ?? 1 }, "list_categories", requestId, undefined, "list_categories")));
  server.tool("search_categories", "Search normal post categories by name or slug with bounded pagination and totals.", { query: z.string().trim().min(1).max(120), per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional() }, async ({ query, per_page, page }) => executeTool("search_categories", "search_categories", (requestId) => call(client, "/search-categories", { search: query, per_page: per_page ?? 100, page: page ?? 1 }, "search_categories", requestId, undefined, "search_categories")));
  server.tool("list_tags", "List normal post tags only with bounded pagination and totals.", { search: z.string().trim().max(120).optional(), per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional() }, async (input) => executeTool("list_tags", "list_tags", (requestId) => call(client, "/list-tags", { ...input, per_page: input.per_page ?? 100, page: input.page ?? 1 }, "list_tags", requestId, undefined, "list_tags")));
  server.tool("search_tags", "Search normal post tags by name or slug with bounded pagination and totals.", { query: z.string().trim().min(1).max(120), per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional() }, async ({ query, per_page, page }) => executeTool("search_tags", "search_tags", (requestId) => call(client, "/search-tags", { search: query, per_page: per_page ?? 100, page: page ?? 1 }, "search_tags", requestId, undefined, "search_tags")));
  server.tool("get_post_terms", "Read the category and tag assignments for one normal post.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("get_post_terms", "get_post_terms", (requestId) => call(client, "/get-post-terms", { post_id }, "get_post_terms", requestId, post_id, "get_post_terms")));
  server.tool("set_post_terms", "Replace only the explicitly supplied category/tag taxonomy on a normal post.", { post_id: postIdSchema, categories: z.array(postIdSchema).max(100).optional(), tags: z.array(postIdSchema).max(100).optional(), expected_modified_gmt: expectedModifiedSchema.optional() }, async (input) => executeTool("set_post_terms", "set_post_terms", (requestId) => call(client, "/set-post-terms", input, "set_post_terms", requestId, input.post_id, "set_post_terms")));
  server.tool("create_category", "Create a category after exact duplicate checks.", { name: z.string().trim().min(1).max(200), slug: z.string().trim().max(200).optional(), description: z.string().max(1000).optional(), parent: z.number().int().min(0).optional() }, async (input) => executeTool("create_category", "create_category", (requestId) => call(client, "/create-category", input, "create_category", requestId, undefined, "create_category")));
  server.tool("create_tag", "Create a tag after exact duplicate checks.", { name: z.string().trim().min(1).max(200), slug: z.string().trim().max(200).optional() }, async (input) => executeTool("create_tag", "create_tag", (requestId) => call(client, "/create-tag", input, "create_tag", requestId, undefined, "create_tag")));
  server.tool("update_seo_meta", "Update only documented SEO fields for the detected provider; no arbitrary post meta is exposed.", seoPostSchema, async (input) => executeTool("update_seo_meta", "update_seo_meta", (requestId) => call(client, "/update-seo-meta", input, "update_seo_meta", requestId, input.post_id, "update_seo_meta")));
  server.tool("get_rank_math_meta", "Read Rank Math SEO metadata for one normal post. Returns a clear provider-unavailable error when Rank Math is not active.", { post_id: postIdSchema }, async ({ post_id }) => executeTool("get_rank_math_meta", "get_rank_math_meta", (requestId) => call(client, "/get-rank-math-meta", { post_id }, "get_rank_math_meta", requestId, post_id, "get_rank_math_meta")));
  server.tool("set_rank_math_meta", "Partially update Rank Math SEO metadata for one normal post; omitted fields are preserved and arbitrary meta is not exposed.", { post_id: postIdSchema, ...rankMathFields, expected_modified_gmt: expectedModifiedSchema.optional() }, async (input) => executeTool("set_rank_math_meta", "set_rank_math_meta", (requestId) => call(client, "/set-rank-math-meta", input, "set_rank_math_meta", requestId, input.post_id, "set_rank_math_meta")));

  // Backward-compatible lookup/upsert/validation tools retained from the previous local release.
  server.tool("find_truyen", "Find a story by exact ID, slug, or normalized title.", { truyen_id: z.number().int().positive().optional(), title: z.string().trim().min(1).max(300).optional(), slug: z.string().trim().min(1).max(200).optional() }, async (input) => executeTool("find_truyen", "find_truyen", (requestId) => call(client, "/find-truyen", input, "find_truyen", requestId, input.truyen_id, "find_truyen")));
  server.tool("find_chuong", "Find chapters by parent, number, title, or slug.", { truyen_id: z.number().int().positive().optional(), chapter_number: z.number().int().positive().optional(), title: z.string().trim().min(1).max(300).optional(), slug: z.string().trim().min(1).max(200).optional() }, async (input) => executeTool("find_chuong", "find_chuong", (requestId) => call(client, "/find-chuong", input, "find_chuong", requestId, input.truyen_id, "find_chuong")));
  server.tool("upsert_truyen", "Legacy safe story upsert; status changes remain separate.", { ...storyFields, title: z.string().trim().min(1).max(300) }, async (input) => executeTool("upsert_truyen", "upsert_truyen", (requestId) => call(client, "/upsert-truyen", storyPayload(input), "upsert_truyen", requestId, undefined, "upsert_truyen")));
  server.tool("upsert_chuong", "Legacy safe chapter upsert by truyen_id plus chapter_number.", { ...chapterFields, truyen_id: z.number().int().positive(), chapter_number: z.number().int().positive(), title: z.string().trim().min(1).max(300), content: z.string() }, async (input) => executeTool("upsert_chuong", "upsert_chuong", (requestId) => call(client, "/upsert-chuong", chapterPayload(input), "upsert_chuong", requestId, input.truyen_id, "upsert_chuong")));
  server.tool("bulk_upsert_chapters", "Legacy bounded chapter upsert; max 200 and no delete operation.", { truyen_id: z.number().int().positive(), chapters: z.array(chapterDraftSchema).min(1).max(config.maxBulkChapters) }, async ({ truyen_id, chapters }) => executeTool("bulk_upsert_chapters", "bulk_upsert_chapters", (requestId) => call(client, "/bulk-upsert-chapters", { truyen_id, chapters }, "bulk_upsert_chapters", requestId, truyen_id, "bulk_upsert_chapters")));
  server.tool("validate_truyen", "Non-mutating story validation.", { truyen_id: z.number().int().positive() }, async ({ truyen_id }) => executeTool("validate_truyen", "validate_truyen", (requestId) => call(client, "/validate-truyen", { truyen_id }, "validate_truyen", requestId, truyen_id, "validate_truyen")));
  server.tool("validate_chuong", "Non-mutating chapter validation.", { chuong_id: z.number().int().positive() }, async ({ chuong_id }) => executeTool("validate_chuong", "validate_chuong", (requestId) => call(client, "/validate-chuong", { chuong_id }, "validate_chuong", requestId, chuong_id, "validate_chuong")));

  // v4.2 normal-post content, taxonomy, SEO, and internal-link tools are appended after the legacy catalog.
  server.tool("patch_post_content", "Safely patch a bounded part of one normal post's content without changing its status, identity, taxonomy, or SEO metadata.", patchOperationFields, async (input) => executeTool("patch_post_content", "patch_post_content", (requestId) => call(client, "/patch-post-content", input, "patch_post_content", requestId, input.post_id, "patch_post_content")));
  server.tool("bulk_patch_post_content", "Apply up to 20 independent safe content patches and return every per-post result.", { operations: z.array(patchOperationObject).min(1).max(20) }, async ({ operations }) => executeTool("bulk_patch_post_content", "bulk_patch_post_content", (requestId) => call(client, "/bulk-patch-post-content", { operations }, "bulk_patch_post_content", requestId, undefined, "bulk_patch_post_content")));
  server.tool("upsert_post_related_links", "Create or update one idempotent internal related-reading block without rewriting the rest of a normal post.", { post_id: postIdSchema, section_id: z.string().trim().min(1).max(120), heading: z.string().trim().min(1).max(300), links: z.array(relatedLinkObject).min(1).max(50), placement: z.enum(["append", "prepend", "before", "after"]).optional(), needle: z.string().max(100_000).optional(), expected_modified_gmt: expectedModifiedSchema.optional() }, async (input) => executeTool("upsert_post_related_links", "upsert_post_related_links", (requestId) => call(client, "/upsert-post-related-links", input, "upsert_post_related_links", requestId, input.post_id, "upsert_post_related_links")));
  server.tool("bulk_set_rank_math_meta", "Apply up to 50 independent allowlisted Rank Math metadata updates.", { operations: z.array(rankMathOperationObject).min(1).max(50) }, async ({ operations }) => executeTool("bulk_set_rank_math_meta", "bulk_set_rank_math_meta", (requestId) => call(client, "/bulk-set-rank-math-meta", { operations }, "bulk_set_rank_math_meta", requestId, undefined, "bulk_set_rank_math_meta")));
  server.tool("bulk_set_post_terms", "Apply up to 50 independent taxonomy updates; omitted categories or tags remain unchanged.", { operations: z.array(termsOperationObject).min(1).max(50) }, async ({ operations }) => executeTool("bulk_set_post_terms", "bulk_set_post_terms", (requestId) => call(client, "/bulk-set-post-terms", { operations }, "bulk_set_post_terms", requestId, undefined, "bulk_set_post_terms")));
  server.tool("find_posts_linking_to", "Find normal posts with actual href links to one target post or URL.", { target_post_id: postIdSchema.optional(), target_url: z.string().url().max(2048).optional(), status: postListStatusSchema.optional(), category_id: postIdSchema.optional(), per_page: z.number().int().min(1).max(100).optional(), page: z.number().int().min(1).max(10000).optional() }, async (input) => executeTool("find_posts_linking_to", "find_posts_linking_to", (requestId) => call(client, "/find-posts-linking-to", { ...input, status: input.status ?? "any", per_page: input.per_page ?? 20, page: input.page ?? 1 }, "find_posts_linking_to", requestId, input.target_post_id, "find_posts_linking_to")));
  server.tool("audit_post_internal_links", "Audit outbound, incoming, duplicate, self, and broken internal links for one normal post without mutation.", { post_id: postIdSchema, include_incoming_sources: z.boolean().optional(), max_incoming_sources: z.number().int().min(1).max(100).optional() }, async (input) => executeTool("audit_post_internal_links", "audit_post_internal_links", (requestId) => call(client, "/audit-post-internal-links", input, "audit_post_internal_links", requestId, input.post_id, "audit_post_internal_links")));
  server.tool("bulk_audit_post_internal_links", "Audit up to 20 normal posts and return per-post link-health results plus an aggregate summary.", { post_ids: z.array(postIdSchema).min(1).max(20), include_incoming_sources: z.boolean().optional(), max_incoming_sources: z.number().int().min(1).max(100).optional() }, async (input) => executeTool("bulk_audit_post_internal_links", "bulk_audit_post_internal_links", (requestId) => call(client, "/bulk-audit-post-internal-links", input, "bulk_audit_post_internal_links", requestId, undefined, "bulk_audit_post_internal_links")));
}

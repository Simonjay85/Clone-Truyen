import assert from "node:assert/strict";
import { createServer } from "node:http";
import { once } from "node:events";
import { test } from "node:test";
import { authFailureReason, createApplication, extractBearerToken, timingSafeEqualString } from "../dist/index.js";
import { WordPressBridgeClient } from "../dist/wp-bridge.js";

function cfg(overrides = {}) {
  return {
    port: 8792,
    mcpAuthMode: "bearer",
    mcpBearerToken: "mcp-test-secret",
    wpBridgeBaseUrl: "https://example.test/wp-json/doctieuthuyet-mcp/v1",
    wpBridgeToken: "wp-test-secret",
    requestTimeoutMs: 1000,
    maxBulkChapters: 50,
    serviceVersion: "test",
    ...overrides,
  };
}

async function running(application) {
  const server = createServer(application.app);
  server.listen(0, "127.0.0.1");
  await once(server, "listening");
  return { server, base: `http://127.0.0.1:${server.address().port}` };
}

function mcpRequest(base, token, body, session) {
  const headers = { authorization: `Bearer ${token}`, "content-type": "application/json", accept: "application/json, text/event-stream" };
  if (session) headers["mcp-session-id"] = session;
  return fetch(`${base}/mcp`, { method: "POST", headers, body: JSON.stringify(body) });
}

async function sseJson(response) {
  const text = await response.text();
  const line = text.split("\n").find((item) => item.startsWith("data:"));
  return JSON.parse(line ? line.slice(5).trim() : text);
}

test("health, bearer helpers, and bridge request-id forwarding are safe", async () => {
  assert.equal(extractBearerToken("bearer   abc  "), "abc");
  assert.equal(extractBearerToken("Basic abc"), null);
  assert.equal(timingSafeEqualString("same", "same"), true);
  assert.equal(timingSafeEqualString("same", "different"), false);
  assert.equal(authFailureReason(undefined, "secret"), "missing_authorization_header");
  assert.equal(authFailureReason("Basic secret", "secret"), "invalid_authorization_scheme");
  assert.equal(authFailureReason("Bearer Bearer secret", "secret"), "invalid_authorization_scheme");
  assert.equal(authFailureReason("Bearer stale", "secret"), "token_mismatch");
  assert.equal(authFailureReason("Bearer secret", ""), "server_secret_missing");
  assert.equal(authFailureReason("Bearer secret", "secret"), null);
  const calls = [];
  const client = new WordPressBridgeClient(cfg(), {
    fetchImpl: async (_url, options) => { calls.push(options); return new Response(JSON.stringify({ ok: true, request_id: options.headers["X-Request-ID"], data: { mcp: "online" }, warnings: [], error: null }), { status: 200 }); },
    logger: () => {},
  });
  const health = await client.health({ operation: "health_check", requestId: "test-request" });
  assert.equal(health.ok, true);
  assert.equal(calls[0].headers["X-Request-ID"], "test-request");
  assert.equal(JSON.stringify(calls).includes("wp-test-secret"), true);
});

test("missing and wrong MCP auth are rejected, authenticated tools/list works", async (t) => {
  const calls = [];
  const fakeBridge = {
    health: async () => ({ ok: true, request_id: "health", data: { mcp: "online" }, warnings: [], error: null }),
    call: async (endpoint, body, context) => { calls.push({ endpoint, body }); return { ok: true, request_id: context.requestId, data: { endpoint, body }, warnings: [], error: null }; },
  };
  const app = createApplication({ appConfig: cfg(), bridgeClient: fakeBridge });
  const live = await running(app);
  t.after(() => live.server.close());

  const health = await fetch(`${live.base}/health`);
  assert.equal(health.status, 200);
  const healthBody = await health.json();
  assert.equal(healthBody.ok, true);
  assert.equal(typeof healthBody.request_id, "string");
  assert.equal(healthBody.data.plugin, "doctieuthuyet-mcp-bridge");
  assert.equal(healthBody.data.plugin_version, "test");
  assert.equal(healthBody.data.tool_count, 64);
  assert.deepEqual(healthBody.warnings, []);

  const payload = { jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-03-26", capabilities: {}, clientInfo: { name: "fixture", version: "1" } } };
  const missing = await fetch(`${live.base}/mcp`, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
  assert.equal(missing.status, 401);
  assert.equal((await missing.json()).error.code, "MCP_AUTH_FAILED");
  assert.equal((await mcpRequest(live.base, "wrong", payload)).status, 401);
  const initialized = await mcpRequest(live.base, "mcp-test-secret", payload);
  assert.equal(initialized.status, 200);
  const session = initialized.headers.get("mcp-session-id");
  assert.ok(session);
  const initBody = await sseJson(initialized);
  assert.equal(initBody.result.serverInfo.name, "doctieuthuyet-mcp");

  const listed = await mcpRequest(live.base, "mcp-test-secret", { jsonrpc: "2.0", id: 2, method: "tools/list", params: {} }, session);
  const listedBody = await sseJson(listed);
  const listedTools = listedBody.result.tools;
  const names = new Set(listedTools.map((tool) => tool.name));
  console.log(`TOTAL_REGISTERED_TOOLS=${names.size}`);
  console.log(`TOTAL_EXPOSED_TOOLS=${listedTools.length}`);
  assert.equal(names.size, 64);
  assert.equal(listedTools.length, names.size);
  for (const tool of listedTools) {
    assert.equal(typeof tool.name, "string");
    assert.equal(tool.inputSchema.type, "object", `malformed schema for ${tool.name}`);
    assert.equal(typeof tool.inputSchema.properties, "object", `missing schema properties for ${tool.name}`);
  }
  for (const name of ["get_truyen", "get_chuong", "update_truyen", "update_chuong", "list_the_loai", "list_chuong_by_truyen", "get_story_package", "pre_publish_story_package", "publish_truyen", "publish_chuong", "publish_story_package", "unpublish_truyen", "unpublish_chuong", "check_story_integrity"]) assert.equal(names.has(name), true, `missing ${name}`);
  for (const name of ["create_post_draft", "get_post", "search_posts", "update_post", "delete_post", "publish_post", "unpublish_post", "list_categories", "search_categories", "create_category", "list_tags", "search_tags", "create_tag", "get_post_terms", "set_post_terms", "get_rank_math_meta", "set_rank_math_meta", "upload_media", "get_media", "search_media", "set_featured_image", "remove_featured_image", "patch_post_content", "bulk_patch_post_content", "upsert_post_related_links", "bulk_set_rank_math_meta", "bulk_set_post_terms", "find_posts_linking_to", "audit_post_internal_links", "bulk_audit_post_internal_links"]) assert.equal(names.has(name), true, `missing ${name}`);

  const call = await mcpRequest(live.base, "mcp-test-secret", { jsonrpc: "2.0", id: 3, method: "tools/call", params: { name: "get_truyen", arguments: { truyen_id: 123 } } }, session);
  assert.equal((await sseJson(call)).result.isError, undefined);
  assert.equal(calls.at(-1).endpoint, "/get-truyen");
});

test("public No Auth mode matches ChatGPT developer plugins while WordPress auth remains configured", async (t) => {
  const fakeBridge = {
    health: async () => ({ ok: true, request_id: "health", data: { mcp: "online" }, warnings: [], error: null }),
    call: async (_endpoint, body, context) => ({ ok: true, request_id: context.requestId, data: body, warnings: [], error: null }),
  };
  const app = createApplication({ appConfig: cfg({ mcpAuthMode: "none", mcpBearerToken: "" }), bridgeClient: fakeBridge });
  const live = await running(app);
  t.after(() => live.server.close());

  const payload = { jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-03-26", capabilities: {}, clientInfo: { name: "fixture", version: "1" } } };
  const initialized = await fetch(`${live.base}/mcp`, { method: "POST", headers: { "content-type": "application/json", accept: "application/json, text/event-stream" }, body: JSON.stringify(payload) });
  assert.equal(initialized.status, 200);
  assert.ok(initialized.headers.get("mcp-session-id"));
  const secondInitialize = await fetch(`${live.base}/mcp`, { method: "POST", headers: { "content-type": "application/json", accept: "application/json, text/event-stream" }, body: JSON.stringify({ ...payload, id: 2 }) });
  assert.equal(secondInitialize.status, 200);
  assert.ok(secondInitialize.headers.get("mcp-session-id"));
  assert.equal(cfg({ mcpAuthMode: "none" }).wpBridgeToken, "wp-test-secret");
});

test("bridge permission and optimistic locking errors are not flattened", async () => {
  const client = {
    health: async () => ({ ok: true, request_id: "h", data: {}, warnings: [], error: null }),
    call: async () => ({ ok: false, request_id: "r", data: null, warnings: ["fixture"], error: { code: "PERMISSION_DENIED", message: "denied" } }),
  };
  const app = createApplication({ appConfig: cfg(), bridgeClient: client });
  const live = await running(app);
  const payload = { jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-03-26", capabilities: {}, clientInfo: { name: "fixture", version: "1" } } };
  const init = await mcpRequest(live.base, "mcp-test-secret", payload);
  const session = init.headers.get("mcp-session-id");
  const response = await mcpRequest(live.base, "mcp-test-secret", { jsonrpc: "2.0", id: 2, method: "tools/call", params: { name: "update_truyen", arguments: { truyen_id: 10, title: "x", expected_modified_gmt: "old" } } }, session);
  const result = await sseJson(response);
  const parsed = JSON.parse(result.result.content[0].text);
  assert.equal(result.result.isError, true);
  assert.equal(parsed.error.code, "PERMISSION_DENIED");
  live.server.close();
});

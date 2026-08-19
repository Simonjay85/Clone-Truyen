#!/usr/bin/env node

/**
 * Safe public MCP diagnostic.
 *
 * It checks transport health, unauthenticated rejection, authenticated
 * initialize, and session-correct tools/list. It never prints a token, raw
 * Authorization header, .env value, or full remote response body.
 */

const baseUrl = (process.env.MCP_BASE_URL || "https://mcp.doctieuthuyet.com").replace(/\/$/, "");
const token = process.env.MCP_AUTH_TOKEN?.trim();

async function request(path, options = {}) {
  try {
    const response = await fetch(`${baseUrl}${path}`, {
      redirect: "manual",
      signal: AbortSignal.timeout(20_000),
      ...options,
    });
    const contentType = response.headers.get("content-type") || "";
    const body = await response.text();
    let parsed = null;
    const dataLine = body.split("\n").find((line) => line.startsWith("data:"));
    try {
      parsed = dataLine ? JSON.parse(dataLine.slice(5).trim()) : body ? JSON.parse(body) : null;
    } catch {
      parsed = null;
    }
    return {
      status: response.status,
      contentType,
      location: response.headers.get("location"),
      sessionId: response.headers.get("mcp-session-id"),
      bodyIsJson: parsed !== null,
      body: parsed,
    };
  } catch (error) {
    return {
      status: 0,
      error: error instanceof Error ? error.message : "Connection failed",
    };
  }
}

const initializeBody = (id) => ({
  jsonrpc: "2.0",
  id,
  method: "initialize",
  params: {
    protocolVersion: "2025-03-26",
    capabilities: {},
    clientInfo: { name: "dtt-auth-check", version: "2.0.0" },
  },
});

function printResult(label, value) {
  console.log(`${label}: ${value}`);
}

async function main() {
  console.log(`Checking MCP server at ${baseUrl}`);

  const health = await request("/health");
  printResult("health_status", health.status);
  if (health.status === 0) {
    console.error(`health_error: ${health.error}`);
    process.exitCode = 1;
    return;
  }
  if (!health.bodyIsJson) {
    console.warn("health_warning: response is not the structured health JSON from this build");
  } else {
    printResult("health_ok", Boolean(health.body?.ok));
    printResult("health_version", health.body?.version || "unknown");
    printResult("auth_configured", Boolean(health.body?.authConfigured));
    printResult("wp_bridge_configured", Boolean(health.body?.wpBridgeConfigured));
  }

  const unauthenticated = await request("/mcp", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
    },
    body: JSON.stringify(initializeBody(1)),
  });
  printResult("unauthenticated_status", unauthenticated.status);
  if (unauthenticated.status !== 401) {
    console.error("auth_error: unauthenticated initialize did not return 401");
    process.exitCode = 1;
    return;
  }

  if (!token) {
    console.warn("authenticated_check: skipped because MCP_AUTH_TOKEN is not set");
    process.exitCode = 2;
    return;
  }

  const authenticated = await request("/mcp", {
    method: "POST",
    headers: {
      authorization: `Bearer ${token}`,
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
    },
    body: JSON.stringify(initializeBody(2)),
  });
  printResult("authenticated_status", authenticated.status);
  if (authenticated.status === 401 || authenticated.status === 403) {
    console.error("auth_error: configured MCP token was rejected by the public service");
    process.exitCode = 1;
    return;
  }
  if (authenticated.status < 200 || authenticated.status >= 300 || !authenticated.sessionId) {
    console.error(`transport_error: initialize did not create a usable MCP session (${authenticated.status})`);
    if (authenticated.location) console.error("redirect_present: true");
    process.exitCode = 1;
    return;
  }

  const listed = await request("/mcp", {
    method: "POST",
    headers: {
      authorization: `Bearer ${token}`,
      "content-type": "application/json",
      accept: "application/json, text/event-stream",
      "mcp-session-id": authenticated.sessionId,
    },
    body: JSON.stringify({ jsonrpc: "2.0", id: 3, method: "tools/list", params: {} }),
  });
  printResult("tools_list_status", listed.status);
  const tools = Array.isArray(listed.body?.result?.tools) ? listed.body.result.tools : [];
  printResult("tools_count", tools.length);
  if (listed.status < 200 || listed.status >= 300 || tools.length === 0) {
    console.error("tools_error: session-correct tools/list did not return tools");
    process.exitCode = 1;
    return;
  }

  console.log("result: authenticated MCP transport and tools/list passed");
}

main().catch((error) => {
  console.error(`diagnostic_error: ${error instanceof Error ? error.message : "unknown"}`);
  process.exitCode = 1;
});

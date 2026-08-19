import { randomUUID } from "crypto";
import { config, type AppConfig } from "./config.js";

export interface BridgeCallContext {
  operation: string;
  tool?: string;
  targetId?: number;
  requestId?: string;
}

export interface StandardError {
  code: string;
  message: string;
  details?: Record<string, unknown>;
}

export interface StandardEnvelope<T = unknown> {
  ok: boolean;
  request_id: string;
  data: T;
  warnings: string[];
  error: StandardError | null;
}

export interface BridgeLogEvent extends BridgeCallContext {
  durationMs: number;
  success: boolean;
  httpStatus: number | null;
  code?: string;
}

export type BridgeLogger = (event: BridgeLogEvent) => void;

export interface WordPressBridgeErrorOptions {
  code: string;
  status?: number | null;
  retryable?: boolean;
  details?: Record<string, unknown>;
}

export class WordPressBridgeError extends Error {
  readonly code: string;
  readonly status: number | null;
  readonly retryable: boolean;
  readonly details: Record<string, unknown>;

  constructor(message: string, options: WordPressBridgeErrorOptions) {
    super(message);
    this.name = "WordPressBridgeError";
    this.code = options.code;
    this.status = options.status ?? null;
    this.retryable = options.retryable ?? false;
    this.details = options.details ?? {};
  }
}

export interface WordPressBridgeClientOptions {
  fetchImpl?: typeof fetch;
  logger?: BridgeLogger;
}

interface BackendErrorBody {
  code?: unknown;
  message?: unknown;
  error?: { code?: unknown; message?: unknown; details?: unknown } | null;
}

function safeString(value: unknown, fallback: string): string {
  if (typeof value !== "string") return fallback;
  const normalized = value.replace(/[\u0000-\u001f\u007f]/g, " ").trim();
  return normalized ? normalized.slice(0, 300) : fallback;
}

function safeCode(value: unknown, fallback = "WORDPRESS_REQUEST_FAILED"): string {
  if (typeof value !== "string") return fallback;
  const code = value.replace(/[^a-zA-Z0-9_-]/g, "_").slice(0, 80).toUpperCase();
  return code || fallback;
}

function errorCodeFor(status: number, backendCode?: unknown): string {
  if (status === 401) return "WORDPRESS_AUTH_FAILED";
  if (status === 403) return "WORDPRESS_PERMISSION_DENIED";
  if (status === 404) return "WORDPRESS_NOT_FOUND";
  return safeCode(backendCode, status >= 500 ? "WORDPRESS_SERVER_ERROR" : "WORDPRESS_REQUEST_FAILED");
}

function errorMessageFor(status: number, backendMessage?: unknown): string {
  if (status === 401) return "WordPress bridge authentication failed.";
  if (status === 403) return "WordPress bridge permission denied.";
  if (status === 404) return "WordPress bridge endpoint or resource was not found.";
  return safeString(backendMessage, `WordPress bridge request failed with HTTP ${status}.`);
}

function defaultLogger(event: BridgeLogEvent): void {
  console.log(JSON.stringify({ component: "wordpress-bridge", ...event }));
}

function isEnvelope(value: unknown): value is Partial<StandardEnvelope> {
  return typeof value === "object" && value !== null && "ok" in value && "request_id" in value;
}

/** Normalize both the current bridge envelope and the old success shape. */
export function normalizeEnvelope<T>(value: unknown, requestId: string = randomUUID()): StandardEnvelope<T> {
  if (isEnvelope(value)) {
    const candidate = value as Partial<StandardEnvelope<T>>;
    return {
      ok: candidate.ok === true,
      request_id: safeString(candidate.request_id, requestId),
      data: (candidate.data ?? null) as T,
      warnings: Array.isArray(candidate.warnings) ? candidate.warnings.filter((item): item is string => typeof item === "string") : [],
      error: candidate.error && typeof candidate.error === "object"
        ? {
            code: safeCode((candidate.error as StandardError).code, "WORDPRESS_REQUEST_FAILED"),
            message: safeString((candidate.error as StandardError).message, "WordPress bridge request failed."),
            ...((candidate.error as StandardError).details ? { details: (candidate.error as StandardError).details } : {}),
          }
        : null,
    };
  }

  if (typeof value === "object" && value !== null && (value as { success?: unknown }).success === false) {
    const old = value as { code?: unknown; message?: unknown; details?: Record<string, unknown> };
    return {
      ok: false,
      request_id: requestId,
      data: null as T,
      warnings: [],
      error: {
        code: safeCode(old.code, "WORDPRESS_REQUEST_FAILED"),
        message: safeString(old.message, "WordPress bridge request failed."),
        ...(old.details ? { details: old.details } : {}),
      },
    };
  }

  return { ok: true, request_id: requestId, data: value as T, warnings: [], error: null };
}

export class WordPressBridgeClient {
  private readonly fetchImpl: typeof fetch;
  private readonly logger: BridgeLogger;

  constructor(
    private readonly appConfig: AppConfig = config,
    options: WordPressBridgeClientOptions = {}
  ) {
    this.fetchImpl = options.fetchImpl ?? fetch;
    this.logger = options.logger ?? defaultLogger;
  }

  async call<T = unknown>(
    endpoint: string,
    body: Record<string, unknown> = {},
    context: BridgeCallContext = { operation: endpoint }
  ): Promise<StandardEnvelope<T>> {
    const startedAt = Date.now();
    const requestId = context.requestId ?? randomUUID();
    let httpStatus: number | null = null;
    let success = false;
    const finish = (code?: string): void => {
      this.logger({
        ...context,
        requestId,
        durationMs: Date.now() - startedAt,
        success,
        httpStatus,
        ...(code ? { code } : {}),
      });
    };

    if (!this.appConfig.wpBridgeBaseUrl || !this.appConfig.wpBridgeToken) {
      const error = new WordPressBridgeError("WordPress bridge authentication is not configured.", {
        code: "WORDPRESS_AUTH_NOT_CONFIGURED",
        status: 503,
      });
      finish(error.code);
      throw error;
    }

    const normalizedEndpoint = endpoint.startsWith("/") ? endpoint : `/${endpoint}`;
    const url = `${this.appConfig.wpBridgeBaseUrl}${normalizedEndpoint}`;
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), this.appConfig.requestTimeoutMs);

    try {
      let response: Response;
      try {
        response = await this.fetchImpl(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
            Authorization: `Bearer ${this.appConfig.wpBridgeToken}`,
            "X-Request-ID": requestId,
          },
          body: JSON.stringify(body),
          signal: controller.signal,
        });
      } catch (cause) {
        const error = new WordPressBridgeError(
          controller.signal.aborted ? "WordPress bridge request timed out." : "WordPress bridge could not be reached.",
          {
            code: controller.signal.aborted ? "WORDPRESS_TIMEOUT" : "WORDPRESS_UNREACHABLE",
            status: null,
            retryable: true,
            details: { cause: cause instanceof Error ? cause.name : "network_error" },
          }
        );
        finish(error.code);
        throw error;
      }

      httpStatus = response.status;
      const rawBody = await response.text();
      let parsed: unknown = null;
      if (rawBody.trim()) {
        try {
          parsed = JSON.parse(rawBody);
        } catch {
          const error = new WordPressBridgeError(
            response.ok ? "WordPress bridge returned invalid JSON." : errorMessageFor(response.status),
            {
              code: response.ok ? "WORDPRESS_INVALID_RESPONSE" : errorCodeFor(response.status),
              status: response.status,
              retryable: response.status >= 500,
            }
          );
          finish(error.code);
          throw error;
        }
      }

      if (!response.ok) {
        const backend = (parsed ?? {}) as BackendErrorBody;
        const nested = backend.error ?? {};
        const code = errorCodeFor(response.status, nested.code ?? backend.code);
        const message = errorMessageFor(response.status, nested.message ?? backend.message);
        const error = new WordPressBridgeError(message, {
          code,
          status: response.status,
          retryable: response.status >= 500,
          details: response.status === 401 || response.status === 403
            ? {}
            : (typeof nested.details === "object" && nested.details ? nested.details as Record<string, unknown> : {}),
        });
        finish(error.code);
        throw error;
      }

      const envelope = normalizeEnvelope<T>(parsed, requestId);
      success = envelope.ok;
      finish(envelope.ok ? undefined : envelope.error?.code);
      return envelope;
    } finally {
      clearTimeout(timeout);
    }
  }

  health(context: BridgeCallContext = { operation: "health_check" }): Promise<StandardEnvelope<unknown>> {
    return this.call("/health", {}, context);
  }
}

export const wpBridge = new WordPressBridgeClient();

export function callWpBridge<T = unknown>(
  endpoint: string,
  body: Record<string, unknown> = {},
  context?: BridgeCallContext
): Promise<StandardEnvelope<T>> {
  return wpBridge.call<T>(endpoint, body, context);
}

export function errorToEnvelope(error: unknown, requestId: string = randomUUID()): StandardEnvelope<null> {
  if (error instanceof WordPressBridgeError) {
    return {
      ok: false,
      request_id: requestId,
      data: null,
      warnings: [],
      error: {
        code: error.code,
        message: error.message,
        ...(Object.keys(error.details).length ? { details: error.details } : {}),
      },
    };
  }
  return {
    ok: false,
    request_id: requestId,
    data: null,
    warnings: [],
    error: { code: "INTERNAL_ERROR", message: "The MCP operation failed unexpectedly." },
  };
}

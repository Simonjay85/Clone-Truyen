<?php
declare(strict_types=1);

define('ABSPATH', __DIR__ . '/');
define('DOCTIEUTHUYET_MCP_TOKEN', 'php-test-token');
define('DAY_IN_SECONDS', 86400);

function add_action(string $name, callable $callback): void {}
function get_option(string $name, mixed $default = ''): mixed { return $default; }
function wp_json_encode(mixed $value, int $flags = 0): string|false { return json_encode($value, $flags); }
function sanitize_key(string $value): string { return strtolower(preg_replace('/[^a-zA-Z0-9_-]/', '_', $value) ?? ''); }
function wp_strip_all_tags(string $value): string { return trim(strip_tags($value)); }
function remove_accents(string $value): string { return iconv('UTF-8', 'ASCII//TRANSLIT//IGNORE', $value) ?: $value; }
function absint(mixed $value): int { return abs((int) $value); }

class WP_Error {
    public function __construct(private string $code, private string $message, private array $data = []) {}
    public function get_error_code(): string { return $this->code; }
    public function get_error_message(): string { return $this->message; }
}

class WP_REST_Request {
    public function __construct(private array $headers = [], private array $params = []) {}
    public function get_header(string $name): string { return $this->headers[strtolower($name)] ?? ''; }
    public function get_json_params(): array { return $this->params; }
}

require __DIR__ . '/../../wp-content/plugins/doctieuthuyet-mcp-bridge/doctieuthuyet-mcp-bridge.php';

function check(bool $condition, string $message): void {
    if (!$condition) {
        throw new RuntimeException($message);
    }
}

check(dttmcp_extract_chapter_number('Chương 12: Mở đầu') === 12, 'chapter number extraction failed');
check(dttmcp_extract_chapter_number('Chapter 3') === 3, 'English chapter number extraction failed');
check(dttmcp_normalize_title('  BI  DUOI  ') === 'bi duoi', 'title normalization failed');
check(dttmcp_create_status_guard(['status' => 'draft']) === true, 'draft create status should be supported');
check(dttmcp_create_status_guard(['status' => 'publish']) instanceof WP_Error, 'publish create status should fail');
check(dttmcp_media_extension_matches('cover.jpg', 'image/jpeg') === true, 'JPEG extension should match MIME');
check(dttmcp_media_extension_matches('cover.png', 'image/jpeg') === false, 'mismatched extension/MIME should fail');
check(dttmcp_allowed_robots('noindex,nofollow') === true, 'supported robots value should pass');
check(dttmcp_allowed_robots('noarchive,all') === false, 'unsupported robots value should fail');

$valid = dttmcp_auth(new WP_REST_Request(['authorization' => 'Bearer php-test-token']));
check($valid === true, 'valid bearer token was rejected');

$missing = dttmcp_auth(new WP_REST_Request([]));
check($missing instanceof WP_Error && $missing->get_error_code() === 'AUTH_MISSING', 'missing auth was not rejected safely');

$invalid = dttmcp_auth(new WP_REST_Request(['authorization' => 'Bearer wrong-token']));
check($invalid instanceof WP_Error && $invalid->get_error_code() === 'AUTH_FAILED', 'invalid auth was not rejected safely');

fwrite(STDOUT, "PHP bridge contract tests passed\n");

<?php
declare(strict_types=1);

define('ABSPATH', __DIR__ . '/');
define('DOCTIEUTHUYET_MCP_TOKEN', 'php-test-token');
define('DAY_IN_SECONDS', 86400);
define('DTTMCP_TESTING', true);
define('RANK_MATH_VERSION', 'fixture');

$GLOBALS['fake_posts'] = [];
$GLOBALS['fake_meta'] = [];
$GLOBALS['fake_terms'] = [
    (object) ['term_id' => 1, 'name' => 'Fantasy', 'slug' => 'fantasy', 'count' => 2],
    (object) ['term_id' => 2, 'name' => 'Romance', 'slug' => 'romance', 'count' => 1],
];
$GLOBALS['fake_post_terms'] = [];
$GLOBALS['fake_next_id'] = 100;
$GLOBALS['fake_modified_tick'] = 0;
$GLOBALS['fake_permission_override'] = null;
$GLOBALS['fake_fail_publish_id'] = 0;
$GLOBALS['fake_audits'] = [];
$GLOBALS['routes'] = [];

function add_action(string $name, callable $callback): void {}
function do_action(string $name, ...$args): void { if ($name === 'dttmcp_audit_log') $GLOBALS['fake_audits'][] = $args[0]; }
function apply_filters(string $name, $value, ...$args) {
    if ($name === 'dttmcp_permission_check') return $GLOBALS['fake_permission_override'];
    if ($name === 'dttmcp_confirmation_ttl') return 600;
    return $value;
}
function register_rest_route(string $namespace, string $route, array $args): void { $GLOBALS['routes'][$route] = $args; }
function is_wp_error($value): bool { return $value instanceof WP_Error; }
function absint($value): int { return abs((int) $value); }
function wp_json_encode($value, int $flags = 0): string|false { return json_encode($value, $flags); }
function wp_generate_uuid4(): string { return 'fixture-request-id'; }
function wp_generate_password(int $length = 64, bool $special = true, bool $extra = false): string { return str_repeat('fixture', 12); }
function wp_strip_all_tags(string $value): string { return trim(strip_tags($value)); }
function remove_accents(string $value): string { return iconv('UTF-8', 'ASCII//TRANSLIT//IGNORE', $value) ?: $value; }
function sanitize_text_field(string $value): string { return trim(strip_tags($value)); }
function wp_kses_post(string $value): string { return strip_tags($value, '<p><br><strong><em><ul><ol><li><a><blockquote><div><h2><h3><span>'); }
function sanitize_title(string $value): string { $value = strtolower(remove_accents(strip_tags($value))); $value = preg_replace('/[^a-z0-9]+/', '-', $value) ?? ''; return trim($value, '-'); }
function home_url(): string { return 'https://fixture.test'; }
function get_permalink(int $id): string { $post = $GLOBALS['fake_posts'][$id] ?? null; return 'https://fixture.test/' . (($post && !empty($post->post_name)) ? trim((string) $post->post_name, '/') . '/' : '?p=' . $id); }
function get_post_thumbnail_id(int $id): int { return (int) ($GLOBALS['fake_meta'][$id]['_thumbnail_id'] ?? 0); }
function set_post_thumbnail(int $post_id, int $attachment): bool { $GLOBALS['fake_meta'][$post_id]['_thumbnail_id'] = $attachment; return true; }
function taxonomy_exists(string $taxonomy): bool { return in_array($taxonomy, ['the_loai', 'post_tag'], true); }
function is_object_in_taxonomy(string $post_type, string $taxonomy): bool { return $taxonomy === 'the_loai'; }
function wp_get_post_terms(int $post_id, string $taxonomy): array { return $GLOBALS['fake_post_terms'][$post_id][$taxonomy] ?? []; }
function wp_set_post_terms(int $post_id, array $terms, string $taxonomy, bool $append = false): array { $GLOBALS['fake_post_terms'][$post_id][$taxonomy] = array_map(fn($term) => (object) ['term_id' => is_numeric($term) ? (int) $term : 0, 'name' => (string) $term, 'slug' => sanitize_title((string) $term), 'count' => 0], $terms); return array_map(fn($term) => is_numeric($term) ? (int) $term : 0, $terms); }
function term_exists(int $term_id, string $taxonomy = ''): int|false { foreach ($GLOBALS['fake_terms'] as $term) if ((int) $term->term_id === $term_id) return $term_id; return false; }
function get_terms(array $args): array { return $GLOBALS['fake_terms']; }
function get_post(int $id) { return $GLOBALS['fake_posts'][$id] ?? null; }
function get_post_meta(int $post_id, string $key, bool $single = false) { return $GLOBALS['fake_meta'][$post_id][$key] ?? ($single ? '' : []); }
function update_post_meta(int $post_id, string $key, $value): bool { $GLOBALS['fake_meta'][$post_id][$key] = $value; return true; }
function fake_dates(object $post): void { $GLOBALS['fake_modified_tick']++; $post->post_modified = '2026-08-11 10:00:' . str_pad((string) $GLOBALS['fake_modified_tick'], 2, '0', STR_PAD_LEFT); $post->post_modified_gmt = $post->post_modified; }
function wp_insert_post(array $data, bool $wp_error = false) {
    $id = ++$GLOBALS['fake_next_id']; $post = (object) array_merge(['ID' => $id, 'post_author' => 1, 'post_date' => '2026-08-11 10:00:00', 'post_date_gmt' => '2026-08-11 10:00:00'], $data); fake_dates($post); $GLOBALS['fake_posts'][$id] = $post; return $id;
}
function wp_update_post(array $data, bool $wp_error = false) {
    $id = (int) ($data['ID'] ?? 0); if (!$id || !isset($GLOBALS['fake_posts'][$id])) return new WP_Error('not_found', 'Post not found.', ['status' => 404]);
    if (($data['post_status'] ?? '') === 'publish' && $GLOBALS['fake_fail_publish_id'] === $id) return new WP_Error('fixture_publish_failed', 'Fixture publish failed.', ['status' => 500]);
    foreach ($data as $key => $value) if ($key !== 'ID') $GLOBALS['fake_posts'][$id]->{$key} = $value; fake_dates($GLOBALS['fake_posts'][$id]); return $id;
}
function get_posts(array $args): array {
    $items = array_values($GLOBALS['fake_posts']);
    $items = array_values(array_filter($items, function ($post) use ($args) {
        if (isset($args['post_type']) && $post->post_type !== $args['post_type']) return false;
        if (isset($args['post_status']) && $args['post_status'] !== 'any' && (is_array($args['post_status']) ? !in_array($post->post_status, $args['post_status'], true) : $post->post_status !== $args['post_status'])) return false;
        if (isset($args['name']) && $args['name'] !== $post->post_name) return false;
        if (isset($args['post__not_in']) && in_array((int) $post->ID, array_map('intval', (array) $args['post__not_in']), true)) return false;
        if (isset($args['s']) && $args['s'] !== '' && stripos((string) $post->post_title . ' ' . (string) $post->post_content, (string) $args['s']) === false) return false;
        if (isset($args['meta_key']) && (string) ($GLOBALS['fake_meta'][$post->ID][$args['meta_key']] ?? '') !== (string) ($args['meta_value'] ?? '')) return false;
        return true;
    }));
    usort($items, fn($a, $b) => $b->ID <=> $a->ID); $per_page = max(1, (int) ($args['posts_per_page'] ?? 200)); $page = max(1, (int) ($args['paged'] ?? 1)); return array_slice($items, ($page - 1) * $per_page, $per_page);
}
function wp_timezone(): DateTimeZone { return new DateTimeZone('Asia/Ho_Chi_Minh'); }

class WP_Error {
    public function __construct(private string $code, private string $message, private array $data = []) {}
    public function get_error_code(): string { return $this->code; }
    public function get_error_message(): string { return $this->message; }
    public function get_error_data(): array { return $this->data; }
}
class WP_REST_Request {
    public function __construct(private array $params = [], private array $headers = ['authorization' => 'Bearer php-test-token']) {}
    public function get_json_params(): array { return $this->params; }
    public function get_header(string $name): string { return $this->headers[strtolower($name)] ?? ''; }
}
class WP_REST_Response {
    public function __construct(private mixed $data, private int $status = 200) {}
    public function get_data(): mixed { return $this->data; }
    public function get_status(): int { return $this->status; }
}

require dirname( __DIR__ ) . '/doctieuthuyet-mcp-bridge.php';
dttmcp_register_routes();

function check(bool $condition, string $message): void { if (!$condition) throw new RuntimeException($message); }
function call_route(string $route, array $body = [], array $headers = ['authorization' => 'Bearer php-test-token']): array { $response = ($GLOBALS['routes'][$route]['callback'])(new WP_REST_Request($body, $headers)); check($response instanceof WP_REST_Response, 'route did not return WP_REST_Response: ' . $route); return [$response->get_status(), $response->get_data()]; }
function ok(array $result): array { check($result[1]['ok'] === true, 'expected route success, got ' . json_encode($result)); return $result[1]['data']; }
function fail(array $result, string $code): array { check($result[1]['ok'] === false, 'expected route failure'); check($result[1]['error']['code'] === $code, 'expected ' . $code . ', got ' . json_encode($result[1]['error'])); return $result[1]; }

check(count($GLOBALS['routes']) >= 28, 'all routes were not registered');
check(array_key_exists('/health', $GLOBALS['routes']), 'health route missing');
check(array_key_exists('/publish-story-package', $GLOBALS['routes']), 'publish package route missing');
check(!array_key_exists('/delete', $GLOBALS['routes']), 'hard delete route must not exist');

$health = call_route('/health'); check($health[0] === 200 && $health[1]['ok'] === true, 'health failed'); check(isset($health[1]['request_id'], $health[1]['data']['relation_meta_key']), 'health envelope incomplete'); check($health[1]['data']['plugin'] === 'doctieuthuyet-mcp-bridge' && $health[1]['data']['version'] === '4.2.0' && $health[1]['data']['tool_count'] === 64, 'health version/tool count contract failed');
fail(call_route('/get-truyen', ['truyen_id' => 99999]), 'TRUYEN_NOT_FOUND');
fail(call_route('/get-chuong', ['chuong_id' => 99999]), 'CHUONG_NOT_FOUND');
fail(call_route('/create-truyen', ['title' => 'Unsafe', 'status' => 'publish']), 'CREATE_STATUS_FORBIDDEN');

$story = ok(call_route('/create-truyen', ['title' => 'Fixture Story', 'content' => '<p>safe</p><script>bad()</script>', 'genres' => [1]]));
$story_id = (int) $story['id']; check(str_contains($GLOBALS['fake_posts'][$story_id]->post_content, '<p>safe</p>'), 'content was not kept'); check(!str_contains($GLOBALS['fake_posts'][$story_id]->post_content, '<script>'), 'HTML was not sanitized'); check($GLOBALS['fake_posts'][$story_id]->post_status === 'draft', 'story did not default draft');
$chapter1 = ok(call_route('/create-chuong', ['truyen_id' => $story_id, 'chapter_number' => 1, 'title' => 'Chương 1', 'content' => '<p>one</p>']));
$chapter2 = ok(call_route('/create-chuong', ['truyen_id' => $story_id, 'chapter_number' => 2, 'title' => 'Chương 2', 'content' => '<p>two</p>']));
$ch1 = (int) $chapter1['id']; $ch2 = (int) $chapter2['id']; check((int) get_post_meta($ch1, '_truyen_id', true) === $story_id, 'relation meta changed');
fail(call_route('/create-chuong', ['truyen_id' => $story_id, 'chapter_number' => 1, 'title' => 'Duplicate 1', 'content' => 'x']), 'DUPLICATE_CHAPTER');

$read = ok(call_route('/get-truyen', ['truyen_id' => $story_id])); $version = $read['truyen']['modified_gmt']; ok(call_route('/update-truyen', ['truyen_id' => $story_id, 'title' => 'Fixture Story Updated', 'expected_modified_gmt' => $version])); fail(call_route('/update-truyen', ['truyen_id' => $story_id, 'title' => 'Stale', 'expected_modified_gmt' => $version]), 'OPTIMISTIC_LOCK_CONFLICT');
$chapter_read = ok(call_route('/get-chuong', ['chuong_id' => $ch1])); ok(call_route('/update-chuong', ['chuong_id' => $ch1, 'content' => '<p>changed</p>', 'expected_modified_gmt' => $chapter_read['chuong']['modified_gmt']]));
fail(call_route('/update-truyen', ['truyen_id' => $story_id, 'title' => 'Content and status must be separate', 'status' => 'draft']), 'STATUS_UPDATE_SEPARATE');
fail(call_route('/update-chuong', ['chuong_id' => $ch1, 'content' => 'status is separate', 'status' => 'draft']), 'STATUS_UPDATE_SEPARATE');
$GLOBALS['fake_permission_override'] = false; fail(call_route('/update-truyen', ['truyen_id' => $story_id, 'title' => 'Denied']), 'PERMISSION_DENIED'); $GLOBALS['fake_permission_override'] = null;

$taxonomy = ok(call_route('/list-the-loai', ['search' => 'Fantasy'])); check($taxonomy['taxonomy'] === 'the_loai' && count($taxonomy['items']) === 2, 'taxonomy lookup failed'); $package = ok(call_route('/get-story-package', ['truyen_id' => $story_id])); check(count($package['chapters']) === 2, 'story package read failed'); $ordered = ok(call_route('/list-chuong-by-truyen', ['truyen_id' => $story_id])); check($ordered['items'][0]['chapter_number'] === 1, 'chapter ordering failed');

$pkg = ok(call_route('/create-story-package', ['idempotency_key' => 'pkg-1', 'story' => ['title' => 'Idempotent Package'], 'chapters' => [['chapter_number' => 1, 'title' => 'Chương 1', 'content' => 'x']]])); $replay = call_route('/create-story-package', ['idempotency_key' => 'pkg-1', 'story' => ['title' => 'Idempotent Package'], 'chapters' => [['chapter_number' => 1, 'title' => 'Chương 1', 'content' => 'x']]]); check($replay[1]['ok'] === true && in_array('IDEMPOTENT_REPLAY', $replay[1]['warnings'], true), 'idempotency replay failed'); fail(call_route('/create-story-package', ['idempotency_key' => 'pkg-1', 'story' => ['title' => 'Different'], 'chapters' => [['chapter_number' => 1, 'title' => 'Chương 1', 'content' => 'x']]]), 'IDEMPOTENCY_CONFLICT');

$pre = ok(call_route('/pre-publish-story-package', ['truyen_id' => $story_id, 'chapter_ids' => [$ch1, $ch2]])); $token = $pre['confirmation_token']; check($token !== '', 'confirmation token missing'); $publish = ok(call_route('/publish-story-package', ['truyen_id' => $story_id, 'chapter_ids' => [$ch1, $ch2], 'confirmation_token' => $token, 'idempotency_key' => 'pub-1'])); check($publish['verified'] === true && $publish['rolled_back'] === false, 'successful package publish failed'); check($GLOBALS['fake_posts'][$story_id]->post_status === 'publish' && $GLOBALS['fake_posts'][$ch1]->post_status === 'publish', 'package did not publish posts'); $pubReplay = call_route('/publish-story-package', ['truyen_id' => $story_id, 'chapter_ids' => [$ch1, $ch2], 'confirmation_token' => 'not-used', 'idempotency_key' => 'pub-1']); check($pubReplay[1]['ok'] === true && in_array('IDEMPOTENT_REPLAY', $pubReplay[1]['warnings'], true), 'publish idempotency replay failed'); fail(call_route('/publish-story-package', ['truyen_id' => $story_id, 'chapter_ids' => [$ch1, $ch2], 'confirmation_token' => $token]), 'CONFIRMATION_INVALID_OR_EXPIRED');

$bad = ok(call_route('/create-story-package', ['story' => ['title' => 'Invalid Package'], 'chapters' => [['chapter_number' => 1, 'title' => 'Chương 1', 'content' => '']]])); $bad_id = (int) $bad['story']['id']; $bad_chapter = (int) $bad['chapters']['items'][0]['id']; fail(call_route('/pre-publish-story-package', ['truyen_id' => $bad_id, 'chapter_ids' => [$bad_chapter]]), 'VALIDATION_FAILED');

$rollback_package = ok(call_route('/create-story-package', ['story' => ['title' => 'Rollback Package'], 'chapters' => [['chapter_number' => 1, 'title' => 'Chương 1', 'content' => 'x'], ['chapter_number' => 2, 'title' => 'Chương 2', 'content' => 'y']]])); $rollback_story = (int) $rollback_package['story']['id']; $rollback_ch1 = (int) $rollback_package['chapters']['items'][0]['id']; $rollback_ch2 = (int) $rollback_package['chapters']['items'][1]['id']; $rollback_pre = ok(call_route('/pre-publish-story-package', ['truyen_id' => $rollback_story, 'chapter_ids' => [$rollback_ch1, $rollback_ch2]])); $GLOBALS['fake_fail_publish_id'] = $rollback_ch2; $rollback = call_route('/publish-story-package', ['truyen_id' => $rollback_story, 'chapter_ids' => [$rollback_ch1, $rollback_ch2], 'confirmation_token' => $rollback_pre['confirmation_token']]); check($rollback[1]['ok'] === false && $rollback[1]['error']['code'] === 'PUBLISH_ROLLED_BACK' && $rollback[1]['data']['rolled_back'] === true, 'rollback response failed'); check($GLOBALS['fake_posts'][$rollback_story]->post_status === 'draft' && $GLOBALS['fake_posts'][$rollback_ch1]->post_status === 'draft', 'compensating rollback failed'); $GLOBALS['fake_fail_publish_id'] = 0;

$integrity = ok(call_route('/check-story-integrity', ['truyen_id' => $story_id, 'chapter_ids' => [$ch1, $ch2]])); check($integrity['valid'] === true, 'integrity check failed'); ok(call_route('/unpublish-truyen', ['truyen_id' => $story_id])); ok(call_route('/unpublish-chuong', ['chuong_id' => $ch1])); check($GLOBALS['fake_posts'][$story_id]->post_status === 'draft' && $GLOBALS['fake_posts'][$ch1]->post_status === 'draft', 'unpublish failed');

$normal = ok(call_route('/create-post', ['title' => 'Kiếm Lai Wiki', 'slug' => 'kiem-lai-wiki', 'content' => '<p>original</p>', 'excerpt' => 'first excerpt']));
$normal_id = (int) $normal['id'];
$content_only = ok(call_route('/update-post', ['post_id' => $normal_id, 'content' => '<p>content-only</p>'])); check($content_only['id'] === $normal_id && $content_only['modified'] !== '' && $content_only['modified_gmt'] !== '' && $content_only['modified_gmt'] !== $normal['modified_gmt'], 'content-only update failed or lacks new modified_gmt');
$excerpt_only = ok(call_route('/update-post', ['post_id' => $normal_id, 'excerpt' => 'excerpt-only'])); check($excerpt_only['excerpt'] === 'excerpt-only', 'excerpt-only update failed');
$own_slug = ok(call_route('/update-post', ['post_id' => $normal_id, 'slug' => 'kiem-lai-wiki'])); check($own_slug['slug'] === 'kiem-lai-wiki', 'same own slug was rejected');
$own_title = ok(call_route('/update-post', ['post_id' => $normal_id, 'title' => 'Kiếm Lai Wiki'])); check($own_title['title'] === 'Kiếm Lai Wiki', 'same own title was rejected');
$other = ok(call_route('/create-post', ['title' => 'Another Article', 'slug' => 'different-duplicate-title', 'content' => '<p>other</p>'])); $other_id = (int) $other['id'];
$duplicate_slug = fail(call_route('/update-post', ['post_id' => $normal_id, 'slug' => 'different-duplicate-title']), 'DUPLICATE_SLUG'); check($duplicate_slug['error']['details']['matched_post_id'] === $other_id, 'duplicate slug details missing');
$duplicate_title = fail(call_route('/update-post', ['post_id' => $normal_id, 'title' => 'Another Article']), 'DUPLICATE_SLUG'); check($duplicate_title['error']['details']['matched_title'] === 'Another Article', 'duplicate title details missing');
$trashed_identity = ok(call_route('/create-post', ['title' => 'Trashed Identity', 'slug' => 'trashed-identity', 'content' => '<p>trash</p>'])); $trashed_identity_id = (int) $trashed_identity['id']; wp_update_post(['ID' => $trashed_identity_id, 'post_status' => 'trash'], true); $trash_duplicate = fail(call_route('/create-post', ['title' => 'New Trashed Identity', 'slug' => 'trashed-identity', 'content' => '<p>collision</p>']), 'DUPLICATE_POST'); check($trash_duplicate['error']['details']['matched_status'] === 'trash', 'trash duplicate identity was not protected');
$locked_read = ok(call_route('/get-post', ['post_id' => $normal_id])); $locked_version = $locked_read['modified_gmt']; wp_update_post(['ID' => $normal_id, 'post_content' => '<p>changed elsewhere</p>'], true); $conflict = fail(call_route('/update-post', ['post_id' => $normal_id, 'content' => '<p>must not overwrite</p>', 'expected_modified_gmt' => $locked_version]), 'CONTENT_CONFLICT'); check($conflict['error']['details']['expected_modified_gmt'] === $locked_version, 'content conflict expected value missing');
$GLOBALS['fake_permission_override'] = false; fail(call_route('/patch-post-content', ['post_id' => $normal_id, 'operation' => 'append', 'html' => '<p>denied</p>']), 'PERMISSION_DENIED'); fail(call_route('/find-posts-linking-to', ['target_post_id' => $normal_id]), 'PERMISSION_DENIED'); $GLOBALS['fake_permission_override'] = null;
$list_page = ok(call_route('/list-posts', ['status' => 'any', 'per_page' => 1, 'page' => 2])); check($list_page['pagination']['page'] === 2 && $list_page['pagination']['returned'] === 1 && $list_page['pagination']['total_items'] >= 2 && $list_page['pagination']['total_pages'] >= 2, 'list pagination metadata failed');
$excluded_search = ok(call_route('/search-posts', ['title' => 'Kiếm Lai Wiki', 'exclude_post_id' => $normal_id, 'status' => 'any', 'per_page' => 20, 'page' => 1])); check(count($excluded_search['items']) === 0 && $excluded_search['pagination']['total_items'] === 0, 'search exclude_post_id failed');

$patch_post = ok(call_route('/create-post', ['title' => 'Patch Fixture', 'slug' => 'patch-fixture', 'content' => '<p>Alpha</p><p>Needle</p><p>Needle</p><p>Append marker</p><div id="section-one"><p>Old</p></div>', 'categories' => [1], 'tags' => [1, 2]])); $patch_id = (int) $patch_post['id']; update_post_meta($patch_id, '_rank_math_title', 'Preserve SEO'); ok(call_route('/publish-post', ['post_id' => $patch_id]));
$patch_before = ok(call_route('/get-post', ['post_id' => $patch_id]));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'append', 'html' => '<p>Appended</p>']));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'prepend', 'html' => '<p>Prepended</p>']));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'replace_exact', 'needle' => '<p>Needle</p>', 'html' => '<p>Replaced</p>', 'occurrence' => 2]));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'insert_before', 'needle' => '<p>Alpha</p>', 'html' => '<p>Before Alpha</p>']));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'insert_after', 'needle' => '<p>Alpha</p>', 'html' => '<p>After Alpha</p>']));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'remove_exact', 'needle' => '<p>Append marker</p>']));
ok(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'replace_section_id', 'section_id' => 'section-one', 'html' => '<div id="section-one"><p>New</p></div>']));
$patched_read = ok(call_route('/get-post', ['post_id' => $patch_id])); check($patched_read['status'] === 'publish' && $patched_read['title'] === $patch_before['title'] && $patched_read['slug'] === $patch_before['slug'], 'content patch changed post identity/status'); check($patched_read['categories'] === $patch_before['categories'] && $patched_read['tags'] === $patch_before['tags'], 'content patch changed taxonomy'); check($patched_read['seo']['seo_title'] === 'Preserve SEO', 'content patch changed Rank Math metadata'); check(str_contains($patched_read['content'], '<p>New</p>') && !str_contains($patched_read['content'], 'Append marker'), 'content patch operations did not apply');
fail(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'append', 'html' => '']), 'INVALID_ARGUMENT'); fail(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'replace_exact', 'needle' => 'does-not-exist', 'html' => '<p>x</p>']), 'NEEDLE_NOT_FOUND'); fail(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'replace_exact', 'needle' => '<p>Alpha</p>', 'html' => '<p>x</p>', 'occurrence' => 0]), 'INVALID_OCCURRENCE'); fail(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'replace_section_id', 'section_id' => 'missing-section', 'html' => '<div id="missing-section">x</div>']), 'SECTION_NOT_FOUND'); fail(call_route('/patch-post-content', ['post_id' => $patch_id, 'operation' => 'append', 'html' => '<p>stale</p>', 'expected_modified_gmt' => $patch_before['modified_gmt']]), 'CONTENT_CONFLICT'); fail(call_route('/patch-post-content', ['post_id' => 999999, 'operation' => 'append', 'html' => '<p>x</p>']), 'POST_NOT_FOUND');

$related = ok(call_route('/create-post', ['title' => 'Related Fixture', 'slug' => 'related-fixture', 'content' => '<p>Main body</p>'])); $related_id = (int) $related['id']; ok(call_route('/publish-post', ['post_id' => $related_id]));
$related_request = ['post_id' => $related_id, 'section_id' => 'related-fixture-links', 'heading' => 'Đọc thêm', 'links' => [['url' => get_permalink($patch_id), 'anchor' => 'Patch Fixture'], ['url' => get_permalink($patch_id), 'anchor' => 'Duplicate input']]];
$related_first = ok(call_route('/upsert-post-related-links', $related_request)); check($related_first['action'] === 'created' && $related_first['link_count'] === 1, 'related block was not created/deduplicated'); $related_second = ok(call_route('/upsert-post-related-links', $related_request)); check($related_second['action'] === 'updated' && substr_count($GLOBALS['fake_posts'][$related_id]->post_content, 'id="related-fixture-links"') === 1 && str_contains($GLOBALS['fake_posts'][$related_id]->post_content, 'Main body'), 'related block was not idempotent or untouched content was lost');
$related_add = ok(call_route('/upsert-post-related-links', ['post_id' => $related_id, 'section_id' => 'related-fixture-links', 'heading' => 'Đọc thêm', 'links' => [['url' => get_permalink($normal_id), 'anchor' => 'Kiếm Lai Wiki']]])); check($related_add['link_count'] === 2, 'new related URL did not update the existing block'); fail(call_route('/upsert-post-related-links', ['post_id' => $related_id, 'section_id' => 'bad-links', 'heading' => 'Bad', 'links' => [['url' => 'javascript:alert(1)', 'anchor' => 'Bad']]]), 'INVALID_ARGUMENT'); fail(call_route('/upsert-post-related-links', ['post_id' => $related_id, 'section_id' => 'bad-data', 'heading' => 'Bad', 'links' => [['url' => 'data:text/html,bad', 'anchor' => 'Bad']]]), 'INVALID_ARGUMENT'); fail(call_route('/upsert-post-related-links', ['post_id' => $related_id, 'section_id' => 'bad-file', 'heading' => 'Bad', 'links' => [['url' => 'file:///tmp/bad', 'anchor' => 'Bad']]]), 'INVALID_ARGUMENT'); check($GLOBALS['fake_posts'][$related_id]->post_status === 'publish', 'related links changed published status');
fail(call_route('/upsert-post-related-links', ['post_id' => $related_id, 'section_id' => 'missing-needle', 'heading' => 'Bad', 'placement' => 'before', 'links' => [['url' => get_permalink($normal_id), 'anchor' => 'Kiếm Lai Wiki']]]), 'INVALID_ARGUMENT'); $placed = ok(call_route('/upsert-post-related-links', ['post_id' => $related_id, 'section_id' => 'related-before', 'heading' => 'Đọc thêm trước', 'placement' => 'before', 'needle' => '<p>Main body</p>', 'links' => [['url' => get_permalink($normal_id), 'anchor' => 'Kiếm Lai Wiki']]])); check($placed['action'] === 'created' && strpos($GLOBALS['fake_posts'][$related_id]->post_content, 'id="related-before"') < strpos($GLOBALS['fake_posts'][$related_id]->post_content, '<p>Main body</p>'), 'related before placement failed');
$bulk_patch = ok(call_route('/bulk-patch-post-content', ['operations' => [['post_id' => $related_id, 'operation' => 'append', 'html' => '<p>bulk</p>'], ['post_id' => 999999, 'operation' => 'append', 'html' => '<p>no</p>']]])); check($bulk_patch['success_count'] === 1 && $bulk_patch['failure_count'] === 1 && count($bulk_patch['results']) === 2, 'bulk patch did not return independent results');
$bulk_seo = ok(call_route('/bulk-set-rank-math-meta', ['operations' => [['post_id' => $related_id, 'seo_title' => 'Bulk SEO'], ['post_id' => 999999, 'seo_title' => 'Bad']]])); check($bulk_seo['success_count'] === 1 && $bulk_seo['failure_count'] === 1, 'bulk Rank Math results were not independent');
$bulk_terms = ok(call_route('/bulk-set-post-terms', ['operations' => [['post_id' => $related_id, 'categories' => [1], 'tags' => [2]], ['post_id' => $patch_id, 'categories' => [2]]]])); check($bulk_terms['success_count'] === 2, 'bulk taxonomy update failed'); check(count(dttmcp_terms($patch_id, 'post_tag')) === 2, 'omitted tags did not preserve tags'); ok(call_route('/bulk-set-post-terms', ['operations' => [['post_id' => $patch_id, 'tags' => []]]])); check(count(dttmcp_terms($patch_id, 'post_tag')) === 0, 'explicit empty tags did not clear tags');

$post_b = ok(call_route('/create-post', ['title' => 'Link Target B', 'slug' => 'link-target-b', 'content' => '<p>B</p>'])); $post_b_id = (int) $post_b['id'];
$post_c = ok(call_route('/create-post', ['title' => 'Link Target C', 'slug' => 'link-target-c', 'content' => '<p>C</p>'])); $post_c_id = (int) $post_c['id'];
$post_d = ok(call_route('/create-post', ['title' => 'Orphan D', 'slug' => 'orphan-d', 'content' => '<p>D</p>'])); $post_d_id = (int) $post_d['id'];
$post_a = ok(call_route('/create-post', ['title' => 'Link Source A', 'slug' => 'link-source-a', 'content' => '<p><a href="' . get_permalink($post_b_id) . '">B</a> <a href="/missing-link/">Missing</a></p>'])); $post_a_id = (int) $post_a['id'];
ok(call_route('/create-post', ['title' => 'Link Source B', 'slug' => 'link-source-b', 'content' => '<p><a href="' . get_permalink($post_c_id) . '">C one</a> <a href="' . get_permalink($post_c_id) . '">C two</a></p>'])); $post_b_source_id = (int) $GLOBALS['fake_next_id'];
wp_update_post(['ID' => $post_c_id, 'post_content' => '<p><a href="' . get_permalink($post_c_id) . '">Self</a> <a href="' . get_permalink($post_a_id) . '">A</a></p>'], true);
foreach ([$post_b_id, $post_c_id, $post_d_id, $post_a_id, $post_b_source_id] as $id) ok(call_route('/publish-post', ['post_id' => $id]));
$backlinks = ok(call_route('/find-posts-linking-to', ['target_post_id' => $post_c_id, 'status' => 'publish', 'per_page' => 100])); check(count($backlinks['items']) === 1 && $backlinks['items'][0]['slug'] === 'link-source-b', 'find backlinks did not resolve actual hrefs');
$audit_a = ok(call_route('/audit-post-internal-links', ['post_id' => $post_a_id, 'include_incoming_sources' => true])); check(count($audit_a['outbound_internal_links']) === 2 && count($audit_a['broken_internal_links']) === 1, 'source A internal link audit failed');
$audit_b = ok(call_route('/audit-post-internal-links', ['post_id' => $post_b_id, 'include_incoming_sources' => true])); check(count($audit_b['incoming_sources']) === 1, 'target B incoming audit failed');
$audit_c = ok(call_route('/audit-post-internal-links', ['post_id' => $post_c_id])); check(count($audit_c['self_links']) === 1 && count($audit_c['duplicate_internal_links']) === 0, 'target C self-link audit failed');
$audit_bulk = ok(call_route('/bulk-audit-post-internal-links', ['post_ids' => [$post_a_id, $post_b_id, $post_c_id, $post_d_id]])); check($audit_bulk['summary']['total_posts'] === 4 && $audit_bulk['summary']['orphan_post_count'] === 1, 'bulk link audit summary/orphan calculation failed');

check(count($GLOBALS['fake_audits']) >= 10, 'write audit log was not recorded'); fwrite(STDOUT, "PHP bridge fixture tests passed\n");

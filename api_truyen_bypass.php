<?php
/**
 * Tệp Bypass API - Dành cho Clone Truyện App
 * Chức năng: Vượt qua tường lửa Nginx/LiteSpeed, gọi thẳng vào lõi WordPress REST API.
 * Hướng dẫn: Upload file này lên thư mục gốc của website (cùng chỗ với wp-config.php)
 */

// Tắt hiển thị lỗi HTML để đảm bảo luôn trả về JSON sạch
ini_set('display_errors', 0);
header('Content-Type: application/json');

// Chặn truy cập trực tiếp bằng trình duyệt (GET)
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    http_response_code(405);
    echo json_encode(['error' => 'Chỉ hỗ trợ phương thức POST từ App']);
    exit;
}

// Đọc payload từ App gửi lên
$raw_input = file_get_contents('php://input');
$input = json_decode($raw_input, true);

// Token bảo mật cực mạnh để tránh bị người lạ lạm dụng (Trùng với token trong route.ts)
$secret_token = "ZEN_TRUYEN_2026_BYPASS";

if (!isset($input['secret_token']) || $input['secret_token'] !== $secret_token) {
    http_response_code(401);
    echo json_encode(['error' => 'Từ chối truy cập: Sai Secret Token!']);
    exit;
}

// Nạp lõi WordPress
require_once('wp-load.php');

// Tự động tìm tài khoản Admin đầu tiên trong hệ thống và đăng nhập ngầm
$admins = get_users(['role' => 'administrator', 'number' => 1]);
if (empty($admins)) {
    http_response_code(500);
    echo json_encode(['error' => 'Không tìm thấy tài khoản Administrator nào trên web']);
    exit;
}
$admin_id = $admins[0]->ID;
wp_set_current_user($admin_id);

// Phân tích Endpoint và Method
$method = isset($input['method']) ? strtoupper($input['method']) : 'POST';
$endpoint_raw = isset($input['endpoint']) ? $input['endpoint'] : '';

if (empty($endpoint_raw)) {
    http_response_code(400);
    echo json_encode(['error' => 'Thiếu endpoint']);
    exit;
}

// Tách URL route và Query parameters (VD: the_loai?search=hanh-dong)
$endpoint_parts = explode('?', $endpoint_raw);
$route = '/' . ltrim($endpoint_parts[0], '/');
$request = new WP_REST_Request($method, '/wp/v2' . $route);

// Nạp Query parameters nếu có
if (isset($endpoint_parts[1])) {
    parse_str($endpoint_parts[1], $query_params);
    $request->set_query_params($query_params);
}

// Nạp Body Payload nếu có
if (!empty($input['payload'])) {
    if ($method === 'POST' || $method === 'PUT') {
        $request->set_body_params($input['payload']);
    } else if ($method === 'GET') {
        $request->set_query_params(array_merge($request->get_query_params(), $input['payload']));
    }
}

// Bắn request thẳng vào lõi WordPress (Tuyệt chiêu Bypass: rest_do_request)
$response = rest_do_request($request);

// Lấy dữ liệu trả về và đẩy lại cho App
$server = rest_get_server();
$data = $server->response_to_data($response, false);

http_response_code($response->get_status());
echo wp_json_encode($data);

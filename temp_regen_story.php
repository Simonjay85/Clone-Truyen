<?php
require('./wp-load.php');
require_once(ABSPATH . 'wp-content/plugins/temply-ai-factory/includes/openai-api.php');

$truyens = get_posts(['post_type' => 'truyen', 'name' => 'bong-sen-do-giua-bien-mau', 'posts_per_page' => 1]);
if(empty($truyens)) die("Not found story");
$t = $truyens[0];
$id = $t->ID;

// Delete all chapters
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $id,
    'posts_per_page' => -1
]);
$count = 0;
foreach($chaps as $c) {
    wp_delete_post($c->ID, true);
    $count++;
}

// Update meta to HARDCORE
update_post_meta($id, '_temply_ai_genre', 'Hành động, Giật gân, Xã hội đen, Cẩu huyết, Dark Fantasy');
update_post_meta($id, '_temply_ai_world', 'Thế giới ngầm của một siêu đô thị mục nát, nơi các băng đảng Mafia và các tổ chức sát thủ tàn độc thống trị. Mạng người như cỏ rác, công lý được mua bằng súng và máu.');
update_post_meta($id, '_temply_ai_characters', 'Nathan: Một cực sát thủ mệnh danh "Cuồng Ma" đã rửa tay gác kiếm làm kiến trúc sư để lẩn trốn, lạnh lùng, tàn nhẫn, sở hữu bộ kỹ năng giết người đáng sợ. Max: Tên trùm tổ chức "Bông Sen Đỏ", thủ đoạn tàn độc nhưng luôn mỉm cười. Emma: Nữ hacker mang mối thù gia tộc.');
update_post_meta($id, '_temply_ai_script', 'Truyện là một chuỗi rượt đuổi nghẹt thở và trả thù đẫm máu. Tổ chức Bông Sen Đỏ tìm ra Nathan và ép anh phải phục vụ chúng. Kịch bản bùng nổ khi Nathan tàn sát tất cả cản đường, từng bước vạch trần âm mưu thâm độc và thanh trừng giới giang hồ.');

// Update post status so AutoPilot picks it up
update_post_meta($id, 'truyen_status', 'ongoing'); // ensure ongoing

echo "Deleted $count chapters. Story meta updated dramatically. Generating Chapter 1...<br>";

// We trigger one chapter generation!
$model = get_option('temply_ai_model', 'gemini-1.5-flash');
// Brainstorm
$sys = "Bạn là THE ARCHITECT - Bậc thầy xây dựng cốt truyện kịch tính nảy lửa. Nhiệm vụ: Tóm tắt 100 chữ Chương 1.";
$user = "Nội dung: Mở màn hoành tráng, băng đảng của Max tìm ra nơi Nathan lẩn trốn tròng bọc kiến trúc sư. Gọi là Sự trỗi dậy của bóng tối. Có một trận chiến đẫm máu mở màn.";
$summary = temply_call_ai($sys, $user, 0.9, $model);

$sys_writer = "VAI TRÒ: THE GHOSTWRITER. Bạn là Tiểu Thuyết Gia Hàng Đầu. Viết Chương 1 dài >=800 chữ.

LUẬT: Đầy máu me, rượt đuổi, đánh nhau chân thực. Kết thúc mở bất ngờ.
TITLE: [Tên chương ấn tượng]";
$content = temply_call_ai_quality($sys_writer, "Dựa vào tóm tắt:
" . $summary, 0.9, $model);

$response_trimmed = trim(preg_replace('/```(?:html|json)?|```/', '', $content));
$chap_title = "Sự Trở Lại Của Ác Quỷ";
if(preg_match('/(?:^|
)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*(.*)/i', $response_trimmed, $m)) {
    $chap_title = trim(str_replace(['*', '#', '[', ']'], '', $m[1]));
    $parts = preg_split('/(?:^|
)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*
/i', $response_trimmed, 2);
    $chap_content = trim($parts[1] ?? '');
    if(empty($chap_content)) $chap_content = trim(preg_replace('/(?:^|
)\s*(?:\*\*|#)?\s*TITLE\s*:\s*(?:\*\*)?\s*.*/i', '', $response_trimmed, 1));
} else {
    $lines = explode("
", $response_trimmed);
    if(count($lines)>2) { $chap_title = trim(str_replace(['*', '#', '[', ']'], '', array_shift($lines))); $chap_content = trim(implode("
", $lines)); } 
    else { $chap_content = $response_trimmed; }
}

$post_id = wp_insert_post([
    'post_title'   => "Chương 1: $chap_title",
    'post_content' => wp_kses_post($chap_content),
    'post_status'  => 'publish',
    'post_type'    => 'chuong'
]);
update_post_meta($post_id, '_truyen_id', $id);

echo "Success! New Chapter 1 ID: $post_id";
?>
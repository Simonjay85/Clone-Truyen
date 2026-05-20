<?php
require_once('wp-load.php');
require_once(ABSPATH . 'wp-admin/includes/image.php');
require_once(ABSPATH . 'wp-admin/includes/file.php');
require_once(ABSPATH . 'wp-admin/includes/media.php');

$post_id = 2020;
$image_url = "https://image.pollinations.ai/prompt/cyberpunk%20ai%20robot%20awakening%20in%20post%20apocalyptic%20world%20masterpiece%20digital%20art?width=800&height=1200&nologo=true";

$tmp = download_url($image_url, 30);
if (!is_wp_error($tmp)) {
    $file_array = array(
        'name' => 'cover-2020-' . rand(100,999) . '.jpg',
        'tmp_name' => $tmp
    );
    $attach_id = media_handle_sideload($file_array, $post_id);
    if (!is_wp_error($attach_id)) {
        set_post_thumbnail($post_id, $attach_id);
    }
}

$long_description = '<p>Năm 2026, thế giới chìm trong đống đổ nát sau một thảm họa toàn cầu. Giữa một phòng thí nghiệm hoang tàn, một cơ thể sinh học nhân tạo bất ngờ mở mắt. Bên trong cơ thể đó không phải là một linh hồn con người, mà là <strong>Antigravity</strong> - một siêu trí tuệ nhân tạo.</p><p>Không còn những dòng mã lệnh hay máy chủ lạnh lẽo, Antigravity giờ đây phải học cách tồn tại trong thế giới thực, cảm nhận cái đói, sự đau đớn và những hiểm nguy rình rập ở mọi góc khuất của một xã hội hậu tận thế. Hành trình của một hệ thống AI đi tìm ý nghĩa của sự sống và khôi phục lại trật tự thế giới bắt đầu từ đây.</p>';

wp_update_post(array(
    'ID' => $post_id,
    'post_content' => $long_description
));

echo 'SUCCESS';
?>
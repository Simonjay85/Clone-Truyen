<?php
require_once('/Users/aaronnguyen/TN/App/Clone Truyen/wp-load.php');
$post = get_page_by_title('SỰ THẬT KINH HOÀNG PHÍA SAU HẠNH PHÚC', OBJECT, 'page');
if (!$post) {
    $post = get_page_by_title('SỰ THẬT KINH HOÀNG PHÍA SAU HẠNH PHÚC', OBJECT, 'post');
}
if ($post) {
    echo $post->post_content;
} else {
    echo "Post not found by title";
}

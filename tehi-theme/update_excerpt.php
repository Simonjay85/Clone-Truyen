<?php
require_once('../../../wp-load.php');

$post = get_page_by_title('Di Chúc Vô Hình: Trận Chiến Tài Sản', OBJECT, 'truyen');
if ($post) {
    $shock_excerpt = "Khi người cha tỷ phú qua đời, để lại mớ tài sản kếch xù cùng một tờ di chúc trống rỗng... Những đứa con ngoan hiền hóa bầy sói đói, cắn xé lẫn nhau vì đồng tiền. Nhưng chúng không ngờ, lá bài tẩy cuối cùng lại nằm trong tay một kẻ ngoại đạo hèn kém nhất. Vở kịch lật mặt chính thức bắt đầu!";
    
    wp_update_post([
        'ID' => $post->ID,
        'post_excerpt' => $shock_excerpt
    ]);
    echo "Updated excerpt for Di Chúc Vô Hình: Trận Chiến Tài Sản";
} else {
    echo "Story not found.";
}

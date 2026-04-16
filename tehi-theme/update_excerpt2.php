<?php
require_once('../../../wp-load.php');

$post = get_page_by_title('Đế Vương Số Ẩn Mình: Ông Lão Ăn Bám Vả Mặt Toàn Cầu', OBJECT, 'truyen');
if ($post) {
    $shock_excerpt = "Bị gia đình vợ sỉ vả là 'ông lão ăn bám', Dương Thiên Cửu chỉ biết cắn răng cam chịu suốt nhiều năm. Nhưng không một ai biết, người đàn ông lụ khụ, nghèo hèn bần tiện đang quét nhà rửa bát kia... thực chất là Đế Vương Số - vị thần thao túng toàn bộ mạng lưới tư bản. Một cái búng tay của ông đủ làm sụp đổ kinh tế toàn cầu. Ngày kịch bản thử lòng hạ màn, cũng là lúc Hắc Long lộ diện vả nát mặt gia tộc kiêu ngạo!";
    
    wp_update_post([
        'ID' => $post->ID,
        'post_excerpt' => $shock_excerpt
    ]);
    echo "Updated excerpt properly for Đế Vương Số Ẩn Mình.";
} else {
    echo "Story not found.";
}

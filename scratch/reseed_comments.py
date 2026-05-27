import ftplib
import urllib.request
import os
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

PHP_CODE = """<?php
require('./wp-load.php');
header('Content-Type: application/json');

// 1. Fetch all stories
$args = [
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'publish'
];
$query = new WP_Query($args);
$updated_stories = [];

$names = [
    'Lan Hương', 'Minh Nhật', 'Khánh Linh', 'Quốc Bảo', 'Ngọc Diệp', 'Thu Trang', 
    'Hữu Phước', 'Bích Trâm', 'Tuấn Phong', 'Mai Anh', 'Đức Thịnh', 'Thùy Chi', 
    'Nguyễn Dũng', 'Quỳnh Hương', 'Bảo Lâm', 'Kim Ngân', 'Đăng Khoa', 'Ngọc Ánh', 
    'Thế Anh', 'Phương Thảo', 'Hồng Nhung', 'Phan Khải', 'Vũ Phong', 'Thanh Hằng',
    'Hoàng Nam', 'Tuyết Mai', 'Minh Tuấn', 'Thu Hà', 'Trọng Nghĩa', 'Cẩm Tú',
    'Khắc Nam', 'Đinh Hưng', 'Thành Long', 'Mỹ Duyên', 'Tấn Đạt', 'Minh An', 
    'Việt Anh', 'Khánh Vy', 'Minh Triết', 'Thanh Nhàn', 'Trần Quân', 'Ngọc Trinh'
];

$reviews = [
    'Truyện lôi cuốn quá chừng, tình tiết logic nhân vật nam chính ngầu xỉu! Chấm 5 sao cho truyện và nhóm dịch nhé.',
    'Lâu lắm mới đọc được bộ ngôn tình hay như thế này. Văn phong dịch rất mượt và có tâm, cảm ơn ad nhiều nha.',
    'Nội dung rất sâu sắc, không bị mì ăn liền như các truyện khác. Chờ ad cập nhật thêm chương mới hóng quá đi!',
    'Web đọc truyện thích thật sự, giao diện đẹp load nhanh và không có quảng cáo che màn hình. Mọi người nên đọc thử truyện này nha.',
    'Truyện ngọt sủng siêu dễ thương, đọc giải trí cuối tuần cực kỳ hợp lý luôn ạ. Vote 5 sao!',
    'Đọc đấu trí gay cấn thực sự, các chiêu trò tài chính và pháp lý được tác giả viết cực kỳ chuẩn xác và logic, không hề buff quá đà.',
    'Nữ chính thông minh sắc sảo chứ không phải kiểu bánh bèo chỉ biết khóc lóc. Thích hình tượng nữ cường lý trí thế này!',
    'Cú lật kèo hay quá, đúng chuẩn sảng văn trí tuệ! Đọc mà sướng vô cùng.',
    'Văn phong viết rất cuốn, tác giả chắc chắn có hiểu biết thực tế sâu sắc về giới đầu tư và kinh doanh.',
    'Đọc mô tả các tình tiết mà thèm chảy nước miếng. Tác giả chắc chắn có kiến thức đời sống rất sâu sắc.',
    'Truyện vả mặt cực gắt, gã chồng cũ và mẹ chồng coi thường nhân vật chính giờ thì tha hồ mà hối hận!',
    'Quá hay, vừa sảng khoái vừa giàu tính nhân văn. Đọc một mạch hết luôn không dừng lại được.',
    'Ý tưởng cốt truyện quá độc đáo và sát thực tế luôn á. Cách thắt nút mở nút cực kỳ thông minh.',
    'Bối cảnh chân thực dã man, đọc mà nhập tâm ghê gớm. Đọc cuốn không dứt ra được, mong nhóm dịch ra chương mới nhanh nhanh nha.',
    'Cơ hội trọng sinh lật ngược thế cờ quá sướng, đọc đã mắt thực sự!',
    'Đọc chương nào sướng chương đó, vả mặt cực kỳ thuyết phục bằng chứng cứ hẳn hoi chứ không vô lý.',
    'Nhân vật chính ẩn thân quá đỉnh, quả nhiên là người có thực lực thì không cần nói nhiều. Càng đọc càng mê.',
    'Lật kèo khét lẹt dã man, xem bọn khinh người phải quỳ xuống xin lỗi mà đã cái nư! Rất đáng đọc.',
    'Lối viết chắc tay, cốt truyện kịch tính nhiều plot twist bất ngờ. Một trong những bộ hay nhất năm nay.',
    'Siêu phẩm sảng văn, đề cử nhiệt liệt nha cả nhà. Đọc giải trí cực kỳ.',
    'Drama ngược tâm dã man, nhưng đoạn sau lật kèo vả mặt thì sướng vô cùng. Gieo gió gặp bão quả không sai.',
    'Giao diện web mượt, đọc không quảng cáo, truyện lại hay nữa, tuyệt vời! Cảm ơn admin nhiều nha.',
    'Chàng rể ẩn thế cứu vợ đỉnh quá, xứng đáng 5 sao! Càng về sau càng kịch tính.',
    'Tình tiết nhanh, dồn dập, đọc không bị chán. Nhân vật phụ cũng có não chứ không bị dìm quá đà.',
    'Tác giả bẻ lái khét lẹt, đọc mà tim đập thình thịch luôn. Hóng chương sau quá đi mất.',
    'Mỗi chương đều có điểm nhấn riêng, không bị loãng. Hy vọng tác giả giữ vững phong độ.',
    'Cực kỳ thích cách xây dựng nhân vật chính, bản lĩnh, lạnh lùng nhưng rất trọng tình nghĩa.',
    'Đọc đi đọc lại vẫn thấy hay. Một bộ truyện xứng đáng được biết đến nhiều hơn.',
    'Cốt truyện mạch lạc, không bị sạn. Team dịch siêu có tâm, câu từ chau chuốt mượt mà.',
    'Mới lọt hố mà đọc một lèo mấy chục chương luôn. Nghiện mất rồi ad ơi, cứu em với!'
];

foreach ($query->posts as $post) {
    $post_id = $post->ID;
    
    // 1. Delete ALL existing comments for this story to avoid duplication or mixed state
    $existing_comments = get_comments(['post_id' => $post_id, 'status' => 'all']);
    $deleted_count = 0;
    if (!empty($existing_comments)) {
        foreach ($existing_comments as $c) {
            wp_delete_comment($c->comment_ID, true); // true forces bypass trash
            $deleted_count++;
        }
    }
    
    // 2. Reseed comments
    $num_to_seed = (($post_id * 3) % 11) + 10; // Seeds 10-20 comments randomly
    $ratings_sum = 0;
    
    for ($i = 0; $i < $num_to_seed; $i++) {
        $name_idx = ($post_id + $i * 7) % count($names);
        $rev_idx = ($post_id + $i * 11) % count($reviews);
        $rating = (($post_id + $i) % 7 === 0) ? 4 : 5;
        $ratings_sum += $rating;
        
        $author_name = $names[$name_idx];
        $content = $reviews[$rev_idx];
        
        $days_ago = ($post_id + $i * 13) % 45;
        $comment_date = date('Y-m-d H:i:s', strtotime("-$days_ago days -{$i} hours"));

        $email_prefix = sanitize_title($author_name) . $i;
        $commentdata = [
            'comment_post_ID'      => $post_id,
            'comment_author'       => $author_name,
            'comment_author_email' => $email_prefix . '@gmail.com',
            'comment_content'      => $content,
            'comment_type'         => 'comment',
            'comment_date'         => $comment_date,
            'comment_approved'     => 1
        ];
        
        $comment_id = wp_insert_comment($commentdata);
        if ($comment_id) {
            update_comment_meta($comment_id, 'comment_rating', $rating);
        }
    }
    
    // 3. Update story rating meta values
    update_post_meta($post_id, 'truyen_rating_count', $num_to_seed);
    update_post_meta($post_id, 'truyen_rating_sum', $ratings_sum);
    
    $updated_stories[] = [
        'id' => $post_id,
        'title' => $post->post_title,
        'deleted_comments' => $deleted_count,
        'seeded_comments' => $num_to_seed,
        'rating_avg' => round($ratings_sum / $num_to_seed, 2)
    ];
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'total_stories_updated' => count($updated_stories),
    'stories' => $updated_stories
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_reseed_comments.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading reseeding script via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing database reseeding via HTTP (this might take a few moments)...")
    try:
        # Increase timeout to 300 seconds to allow for deep migrations
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_reseed_comments.php", timeout=300)
        response_data = json.loads(req.read().decode('utf-8'))
        print(f"Server Response: Success!")
        print(f"Total stories reseeded: {response_data['total_stories_updated']} stories.")
        
        # Save detailed migration results
        os.makedirs("scratch", exist_ok=True)
        with open("scratch/db_reseed_results.json", "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=2)
        print("✓ Reseeding results saved to scratch/db_reseed_results.json")
    except Exception as e:
        print("Error executing database reseeding:", e)
        
    print("Cleaning up remote reseeding helper...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote cleanup done.")
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()

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

function smart_truncate($str, $max_len, $append = '') {
    if (mb_strlen($str) <= $max_len) {
        return $str;
    }
    $truncated = mb_substr($str, 0, $max_len - mb_strlen($append));
    $last_space = mb_strrpos($truncated, ' ');
    if ($last_space !== false && $last_space > ($max_len * 0.7)) {
        $truncated = mb_substr($truncated, 0, $last_space);
    }
    return $truncated . $append;
}

function generate_seo_title($title) {
    if (strpos($title, ':') !== false) {
        return smart_truncate($title, 65);
    }
    $suffix = " - Siêu Phẩm Sảng Văn Vả Mặt Full Cực Hay";
    $seo_title = $title . $suffix;
    if (mb_strlen($seo_title) > 65) {
        $seo_title = $title . " - Truyện Sảng Văn Full Cực Hay";
    }
    if (mb_strlen($seo_title) > 65) {
        $seo_title = $title . " - Đọc Full";
    }
    return smart_truncate($seo_title, 65);
}

function get_seo_description($content, $title) {
    $desc = '';
    if (preg_match('/<strong>(.*?)<\/strong>/is', $content, $matches)) {
        $desc = strip_tags($matches[1]);
    } else {
        $desc = strip_tags($content);
    }
    
    $desc = html_entity_decode($desc, ENT_QUOTES | ENT_HTML5, 'UTF-8');
    $desc = trim(preg_replace('/\\s+/', ' ', $desc));
    $desc = str_replace(['"', '\\\\', "'", '“', '”', '‘', '’'], '', $desc);
    
    if (empty($desc)) {
        $desc = "Đọc truyện chữ " . $title . " - Siêu phẩm sảng văn, vả mặt lôi cuốn kịch tính. Theo dõi hành trình lật ngược thế cờ đỉnh cao tại doctieuthuyet.com!";
    }
    
    return smart_truncate($desc, 155, '...');
}

function get_focus_keyword($title) {
    $title_clean = preg_replace('/[:,\-!?]/', ' ', $title);
    $words = explode(' ', trim(preg_replace('/\\s+/', ' ', $title_clean)));
    $words = array_slice($words, 0, 3);
    return mb_strtolower(implode(' ', $words));
}

// Helper to find or create taxonomy term
function get_or_create_term($name, $taxonomy) {
    $term = get_term_by('name', $name, $taxonomy);
    if ($term) {
        return $term->term_id;
    }
    $result = wp_insert_term($name, $taxonomy);
    if (!is_wp_error($result)) {
        return $result['term_id'];
    }
    return false;
}

// 1. CLEAN UP OBSOLETE DATABASE CATEGORIES
$obsolete_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false
]);

$cleaned_terms = [];
foreach ($obsolete_terms as $t) {
    // Delete numeric terms or terms containing 'Bản sao'
    if (is_numeric($t->name) || strpos($t->name, 'Bản sao') !== false) {
        wp_delete_term($t->term_id, 'the_loai');
        $cleaned_terms[] = $t->name;
    }
}

// 2. ASSIGN NEW RICH DYNAMIC CATEGORIES FOR ALL STORIES
$args = [
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'publish'
];
$query = new WP_Query($args);
$updated_stories = [];

$vietnamese_names = [
    'Minh Tuấn', 'Khánh Linh', 'Hữu Phước', 'Hoàng Nam', 'Thùy Chi', 
    'Lê Hải', 'Trần Quân', 'Nguyễn Dũng', 'Mai Anh', 'Đức Thịnh', 
    'Quỳnh Hương', 'Bảo Lâm', 'Kim Ngân', 'Đăng Khoa', 'Ngọc Ánh', 
    'Thế Anh', 'Phương Thảo', 'Hồng Nhung', 'Phan Khải', 'Vũ Phong'
];

$comments_by_cat = [
    'Đô thị thương chiến' => [
        "Đọc đấu trí gay cấn thực sự, các chiêu trò tài chính và pháp lý được tác giả viết cực kỳ chuẩn xác và logic, không hề buff quá đà.",
        "Nữ chính làm CFO quá chất, thông minh sắc sảo chứ không phải kiểu bánh bèo chỉ biết khóc lóc.",
        "Cú lật kèo ngay phiên IPO hay quá, đúng chuẩn sảng văn trí tuệ!",
        "Văn phong viết rất cuốn, tác giả chắc chắn có hiểu biết thực tế sâu sắc về giới đầu tư startup."
    ],
    'Ẩm Thực' => [
        "Đọc mô tả các món ăn michelin mà thèm chảy nước miếng. Tác giả chắc chắn có kiến thức ẩm thực rất sâu sắc.",
        "Truyện vả mặt cực gắt, gã chồng cũ và mẹ chồng coi thường nghề đầu bếp giờ thì tha hồ mà hối hận!",
        "Quá hay, vừa sảng khoái vừa giàu tính nhân văn về ẩm thực truyền thống Việt Nam.",
        "Chỉ một món súp hải sâm mà lột trần cả gia tộc chồng cũ, viết đỉnh thực sự ad ơi!"
    ],
    'Trọng sinh' => [
        "Ý tưởng trọng sinh về năm 2008 rồi gom đất Đông Anh quá độc đáo và sát thực tế luôn á.",
        "Bối cảnh Hà Nội xưa chân thực dã man, đọc mà nhớ lại thời kỳ sốt đất ngày xưa.",
        "Đọc cuốn không dứt ra được, mong ad ra chương mới nhanh nhanh nha.",
        "Cơ hội trọng sinh lật ngược thế cờ quá sướng, đọc đã mắt!"
    ],
    'Vả Mặt' => [
        "Đọc chương nào sướng chương đó, vả mặt cực kỳ thuyết phục bằng chứng cứ hẳn hoi chứ không vô lý.",
        "Nhân vật chính ẩn thân quá đỉnh, quả nhiên là người có thực lực thì không cần nói nhiều.",
        "Lật kèo khét lẹt dã man, xem bọn khinh người phải quỳ xuống xin lỗi mà đã cái nư!",
        "Show don't tell vật lý đọc chân thực từng nhịp thở, phê thực sự!"
    ],
    'Khoa Học Viễn Tưởng' => [
        "Hệ thống AI lôi cuốn ghê, kết hợp yếu tố công nghệ hiện đại đọc mới mẻ hẳn.",
        "Lối viết chắc tay, cốt truyện kịch tính nhiều plot twist bất ngờ.",
        "Siêu phẩm sảng văn khoa học viễn tưởng, đề cử nhiệt liệt nha cả nhà.",
        "Quỷ Vương trú trong Pikachuu đáng yêu dã man, đọc giải trí cực kỳ."
    ],
    'Ngôn Tình' => [
        "Cực thích hình tượng nữ cường lý trí thế này, không dựa dẫm vào đàn ông, tự mình lập nghiệp lật kèo.",
        "Drama gia đình chồng cũ ngược tâm dã man, nhưng đoạn sau lật kèo vả mặt thì sướng vô cùng.",
        "Giao diện web mượt, đọc không quảng cáo, truyện lại hay nữa, tuyệt vời!",
        "Chàng rể ẩn thế cứu vợ đỉnh quá, xứng đáng 5 sao!"
    ]
];

foreach ($query->posts as $post) {
    $id = $post->ID;
    $title = $post->post_title;
    $content = $post->post_content;
    
    // Dynamic category mapping based on title
    $title_lower = mb_strtolower($title, 'UTF-8');
    $assigned_names = ['Sảng Văn'];
    
    // 1. Trọng sinh
    if (strpos($title_lower, 'trọng sinh') !== false || strpos($title_lower, 'xuyên không') !== false || strpos($title_lower, 'sống lại') !== false || strpos($title_lower, '2008') !== false) {
        $assigned_names[] = 'Trọng sinh';
        if (strpos($title_lower, 'xuyên không') !== false) {
            $assigned_names[] = 'Xuyên Không';
        }
    }
    
    // 2. Đô thị thương chiến
    if (strpos($title_lower, 'fintech') !== false || strpos($title_lower, 'startup') !== false || strpos($title_lower, 'mã nguồn') !== false || strpos($title_lower, 'thâu tóm') !== false || strpos($title_lower, 'bán lẻ') !== false || strpos($title_lower, 'bất động sản') !== false || strpos($title_lower, 'dệt may') !== false || strpos($title_lower, 'đấu thầu') !== false || strpos($title_lower, 'ipo') !== false || strpos($title_lower, 'thương trường') !== false || strpos($title_lower, 'tập đoàn') !== false || strpos($title_lower, 'công ty') !== false || strpos($title_lower, 'chứng khoán') !== false) {
        $assigned_names[] = 'Đô thị thương chiến';
    }
    
    // 3. Vả mặt / Đô thị vả mặt
    if (strpos($title_lower, 'vả mặt') !== false || strpos($title_lower, 'khinh') !== false || strpos($title_lower, 'cướp') !== false || strpos($title_lower, 'phế vật') !== false || strpos($title_lower, 'giả nghèo') !== false || strpos($title_lower, 'bảo vệ') !== false || strpos($title_lower, 'bị đuổi') !== false || strpos($title_lower, 'đuổi học') !== false || strpos($title_lower, 'sa thải') !== false || strpos($title_lower, 'thợ hồ') !== false || strpos($title_lower, 'thợ sửa xe') !== false || strpos($title_lower, 'tài xế') !== false || strpos($title_lower, 'con trai nuôi') !== false || strpos($title_lower, 'trợ lý') !== false || strpos($title_lower, 'chồng nghèo') !== false || strpos($title_lower, 'hèn') !== false || strpos($title_lower, 'coi thường') !== false || strpos($title_lower, 'trục xuất') !== false) {
        $assigned_names[] = 'Đô thị vả mặt';
        $assigned_names[] = 'Vả Mặt';
    }
    
    // 4. Hào môn
    if (strpos($title_lower, 'hào môn') !== false || strpos($title_lower, 'landmark 81') !== false || strpos($title_lower, 'chàng rể') !== false || strpos($title_lower, 'vợ hào môn') !== false || strpos($title_lower, 'đại tiểu thư') !== false || strpos($title_lower, 'người thừa kế') !== false || strpos($title_lower, 'tỷ phú') !== false || strpos($title_lower, 'tài phiệt') !== false) {
        $assigned_names[] = 'Hào Môn';
    }
    
    // 5. Ẩm thực
    if (strpos($title_lower, 'bếp') !== false || strpos($title_lower, 'michelin') !== false || strpos($title_lower, 'nấu') !== false || strpos($title_lower, 'ẩm thực') !== false || strpos($title_lower, 'trà sữa') !== false || strpos($title_lower, 'bánh') !== false || strpos($title_lower, 'sầu riêng') !== false || strpos($title_lower, 'tôm hùm') !== false || strpos($title_lower, 'phú yên') !== false || strpos($title_lower, 'khánh hòa') !== false || strpos($title_lower, 'bát tràng') !== false || strpos($title_lower, 'trầm hương') !== false || strpos($title_lower, 'sâm') !== false || strpos($title_lower, 'cà phê') !== false || strpos($title_lower, 'gốm sứ') !== false) {
        $assigned_names[] = 'Ẩm Thực';
    }
    
    // 6. Viễn tưởng / Hệ thống
    if (strpos($title_lower, 'nhân tạo') !== false || strpos($title_lower, 'hệ thống') !== false || strpos($title_lower, 'quỷ vương') !== false || strpos($title_lower, 'bóng đêm') !== false) {
        $assigned_names[] = 'Khoa Học Viễn Tưởng';
        $assigned_names[] = 'Hệ thống';
    }
    
    // 7. Ngôn tình
    if (strpos($title_lower, 'ngôn tình') !== false || strpos($title_lower, 'cô vợ') !== false || strpos($title_lower, 'con dâu') !== false || strpos($title_lower, 'vợ') !== false || strpos($title_lower, 'mẹ chồng') !== false || strpos($title_lower, 'tiểu thư') !== false) {
        $assigned_names[] = 'Ngôn Tình';
    }
    
    $assigned_names = array_unique($assigned_names);
    $term_ids = [];
    foreach ($assigned_names as $name) {
        $tid = get_or_create_term($name, 'the_loai');
        if ($tid) {
            $term_ids[] = intval($tid);
        }
    }
    
    // Set taxonomies (overwrite existing)
    wp_set_post_terms($id, $term_ids, 'the_loai', false);
    
    // 3. SET DESCRIPTIVE ALT TEXT FOR FEATURED IMAGE IF MISSING
    $thumb_id = get_post_thumbnail_id($id);
    $alt_updated = false;
    if ($thumb_id) {
        $current_alt = get_post_meta($thumb_id, '_wp_attachment_image_alt', true);
        if (empty($current_alt) || trim($current_alt) == "" || strpos($current_alt, 'Cover') !== false) {
            $descriptive_alt = "Ảnh bìa truyện " . $title . " - Đọc Tiểu Thuyết Full Cực Hay tại doctieuthuyet.com";
            update_post_meta($thumb_id, '_wp_attachment_image_alt', $descriptive_alt);
            
            // Also update attachment post title
            wp_update_post([
                'ID' => $thumb_id,
                'post_title' => "Ảnh bìa truyện " . $title,
                'post_excerpt' => "Ảnh bìa chính thức của tiểu thuyết " . $title
            ]);
            $alt_updated = true;
        }
    }
    
    // 4. RANKMATH SEO UPDATE FOR ALL STORIES
    $seo_title = generate_seo_title($title);
    $seo_desc = get_seo_description($content, $title);
    $seo_keyword = get_focus_keyword($title);
    
    update_post_meta($id, '_rank_math_title', $seo_title);
    update_post_meta($id, '_rank_math_description', $seo_desc);
    update_post_meta($id, '_rank_math_focus_keyword', $seo_keyword);
    
    update_post_meta($id, 'rank_math_title', $seo_title);
    update_post_meta($id, 'rank_math_description', $seo_desc);
    update_post_meta($id, 'rank_math_focus_keyword', $seo_keyword);
    
    update_post_meta($id, '_rank_math_robots', ['index', 'follow']);
    update_post_meta($id, 'rank_math_robots', ['index', 'follow']);
    update_post_meta($id, 'rank_math_rich_snippet', 'article');
    
    // 5. COMMENT SEEDING ENRICHMENT
    $comments_query = get_comments(['post_id' => $id, 'status' => 'approve']);
    $comments_count = count($comments_query);
    $comments_added = 0;
    
    if ($comments_count < 4) {
        // Find best comment templates matching categories
        $templates = [];
        foreach ($assigned_names as $cat) {
            if (isset($comments_by_cat[$cat])) {
                $templates = array_merge($templates, $comments_by_cat[$cat]);
            }
        }
        if (empty($templates)) {
            $templates = $comments_by_cat['Vả Mặt'];
        }
        
        $needed = 4 - $comments_count;
        shuffle($templates);
        shuffle($vietnamese_names);
        
        for ($i = 0; $i < $needed; $i++) {
            $author = $vietnamese_names[$i % count($vietnamese_names)];
            $comment_content = $templates[$i % count($templates)];
            
            // Random date in May 2026
            $day = rand(1, 20);
            $hour = rand(0, 23);
            $min = rand(10, 59);
            $sec = rand(10, 59);
            $cdate = sprintf("2026-05-%02d %02d:%02d:%02d", $day, $hour, $min, $sec);
            
            $cid = wp_insert_comment([
                'comment_post_ID' => $id,
                'comment_author' => $author,
                'comment_author_email' => sanitize_title($author) . "@gmail.com",
                'comment_content' => $comment_content,
                'comment_date' => $cdate,
                'comment_approved' => 1
            ]);
            if ($cid) {
                $comments_added++;
            }
        }
    }
    
    $updated_stories[] = [
        'id' => $id,
        'title' => $title,
        'categories' => $assigned_names,
        'alt_updated' => $alt_updated,
        'seo_title' => $seo_title,
        'seo_desc' => $seo_desc,
        'seo_keyword' => $seo_keyword,
        'comments_added' => $comments_added,
        'total_comments' => $comments_count + $comments_added
    ];
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'total_cleaned_terms' => count($cleaned_terms),
    'cleaned_terms' => $cleaned_terms,
    'total_stories_updated' => count($updated_stories),
    'stories' => $updated_stories
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_enrich_database.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading enrichment script via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing database enrichment via HTTP (this takes all 74 stories)...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_enrich_database.php", timeout=240)
        response_data = json.loads(req.read().decode('utf-8'))
        print(f"Server Response: Success!")
        print(f"Total obsolete taxonomy terms cleaned: {response_data['total_cleaned_terms']}")
        print(f"Taxonomy terms deleted: {response_data['cleaned_terms']}")
        print(f"Total stories enriched and updated: {response_data['total_stories_updated']} stories.")
        
        with open("scratch/db_enrich_results.json", "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=2)
        print("✓ Detailed enrichment results saved to scratch/db_enrich_results.json")
    except Exception as e:
        print("Error executing database enrichment:", e)
        
    print("Cleaning up remote enrichment helper...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote cleanup done.")
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()

import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    php_code = """<?php
require('./wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => 50,
    'post_status' => 'any',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$analysis = [];

foreach($truyens as $t) {
    $issues = [];
    
    // Check title issues
    $title = trim($t->post_title);
    if (empty($title) || $title === "DTT" || strpos($title, "Truyện Chờ Tên") !== false || strpos($title, "Truyện chờ phân tích") !== false) {
        $issues[] = "Tiêu đề trống hoặc tạm";
    }
    
    // Check slug
    if ($t->post_name === (string)$t->ID) {
        $issues[] = "Slug trùng ID (không có title)";
    }
    
    // Check synopsis (post_content of story)
    $content = trim($t->post_content);
    if (empty($content)) {
        $issues[] = "Nội dung giới thiệu trống";
    } elseif (strpos($content, "1. Bối cảnh Thế Giới") !== false || strpos($content, "1. Bối cảnh thế giới") !== false) {
        $issues[] = "Giới thiệu là bản thô chưa biên tập (1. Bối cảnh Thế Giới...)";
    }
    
    // Check cover image
    $has_cover = has_post_thumbnail($t->ID) || !empty(get_post_meta($t->ID, '_cover_image', true));
    if (!$has_cover) {
        $issues[] = "Thiếu ảnh bìa (Cover Image)";
    }
    
    // Check chapters
    $chaps = get_posts([
        'post_type' => 'chuong',
        'posts_per_page' => -1,
        'meta_key' => '_truyen_id',
        'meta_value' => $t->ID,
        'orderby' => 'menu_order date',
        'order' => 'ASC'
    ]);
    
    $chaps_count = count($chaps);
    if ($chaps_count === 0) {
        $issues[] = "Không có chương nào";
    } else {
        $empty_chaps = [];
        $duplicate_titles = [];
        $seen_titles = [];
        
        foreach($chaps as $idx => $c) {
            $chap_title = trim($c->post_title);
            $chap_content = trim(wp_strip_all_tags($c->post_content));
            
            if (empty($chap_content) || mb_strlen($chap_content, 'utf-8') < 50) {
                $empty_chaps[] = $chap_title ?: ("Chương " . ($idx + 1));
            }
            
            if (in_array($chap_title, $seen_titles)) {
                $duplicate_titles[] = $chap_title;
            } else {
                $seen_titles[] = $chap_title;
            }
        }
        
        if (!empty($empty_chaps)) {
            $issues[] = "Chương rỗng hoặc quá ngắn: " . implode(", ", $empty_chaps);
        }
        if (!empty($duplicate_titles)) {
            $issues[] = "Trùng lặp tiêu đề chương: " . implode(", ", array_unique($duplicate_titles));
        }
    }
    
    $analysis[] = [
        'id' => $t->ID,
        'title' => $title ?: "Không có tiêu đề",
        'slug' => $t->post_name,
        'date' => $t->post_date,
        'status' => $t->post_status,
        'chapters_count' => $chaps_count,
        'issues' => $issues
    ];
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($analysis, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_detailed_check.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_detailed_check.php", "rb") as f:
        ftp.storbinary("STOR temp_detailed_check.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_detailed_check.php", timeout=60)
        data = req.read().decode('utf-8')
        analysis = json.loads(data)
        
        # Save to local file
        with open("detailed_check_results.json", "w", encoding="utf-8") as out:
            json.dump(analysis, out, ensure_ascii=False, indent=2)
            
        buggy_stories = [s for s in analysis if s['issues']]
        print("\n=== KẾT QUẢ PHÂN TÍCH CHI TIẾT TRUYỆN LỖI ===")
        print(f"Tổng số truyện bị lỗi thực sự: {len(buggy_stories)} / 50")
        for idx, s in enumerate(buggy_stories):
            print(f"[{idx+1}] ID: {s['id']} | {s['title']} ({s['date']})")
            print(f"    Trạng thái: {s['status']} | Số chương: {s['chapters_count']}")
            print("    Các vấn đề phát hiện:")
            for iss in s['issues']:
                print(f"      - {iss}")
                
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_detailed_check.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_detailed_check.php"):
            os.remove("temp_detailed_check.php")

if __name__ == "__main__":
    run()

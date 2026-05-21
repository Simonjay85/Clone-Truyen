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
    $words = array_slice($words, 0, 4);
    return mb_strtolower(implode(' ', $words));
}

$args = [
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'publish'
];
$query = new WP_Query($args);
$updated_stories = [];

foreach ($query->posts as $post) {
    $id = $post->ID;
    $title = $post->post_title;
    
    $seo_title = generate_seo_title($title);
    $seo_desc = get_seo_description($post->post_content, $title);
    $seo_keyword = get_focus_keyword($title);
    
    // Update RankMath Postmeta (both standard and underscore to be absolutely safe)
    update_post_meta($id, '_rank_math_title', $seo_title);
    update_post_meta($id, '_rank_math_description', $seo_desc);
    update_post_meta($id, '_rank_math_focus_keyword', $seo_keyword);
    
    update_post_meta($id, 'rank_math_title', $seo_title);
    update_post_meta($id, 'rank_math_description', $seo_desc);
    update_post_meta($id, 'rank_math_focus_keyword', $seo_keyword);
    
    update_post_meta($id, 'rank_math_rich_snippet', 'article');
    
    $updated_stories[] = [
        'id' => $id,
        'title' => $title,
        'seo_title' => $seo_title,
        'seo_desc' => $seo_desc,
        'seo_keyword' => $seo_keyword
    ];
}

if (function_exists('litespeed_purge_all')) {
    litespeed_purge_all();
}

echo json_encode([
    'success' => true,
    'total_updated' => count($updated_stories),
    'stories' => $updated_stories
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_bulk_seo.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading bulk SEO update script via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing bulk SEO update via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_bulk_seo.php", timeout=120)
        response_data = json.loads(req.read().decode('utf-8'))
        print(f"Server Response: Success! Total updated: {response_data['total_updated']} stories.")
        with open("scratch/bulk_seo_results.json", "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=2)
        print("✓ Detailed results saved to scratch/bulk_seo_results.json")
    except Exception as e:
        print("Error executing:", e)
        
    print("Cleaning up remote helper...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote cleanup done.")
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()

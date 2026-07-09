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
    return trim($truncated) . $append;
}

function generate_seo_title($title) {
    $title_clean = html_entity_decode($title, ENT_QUOTES | ENT_HTML5, 'UTF-8');
    $title_clean = trim(preg_replace('/\\s+/', ' ', $title_clean));
    
    // Strictly under 60 characters
    if (mb_strlen($title_clean) <= 58) {
        return $title_clean;
    }
    
    return smart_truncate($title_clean, 58, '...');
}

function generate_seo_description($post_content, $title) {
    $desc = '';
    if (preg_match('/<strong>(.*?)<\/strong>/is', $post_content, $matches)) {
        $desc = strip_tags($matches[1]);
    } else {
        $desc = strip_tags($post_content);
    }
    
    $desc = html_entity_decode($desc, ENT_QUOTES | ENT_HTML5, 'UTF-8');
    $desc = trim(preg_replace('/\\s+/', ' ', $desc));
    $desc = str_replace(['"', '\\\\', "'", '“', '”', '‘', '’'], '', $desc);
    
    $current_len = mb_strlen($desc);
    
    // Strictly optimize to ~155-160 characters
    if ($current_len > 158) {
        return smart_truncate($desc, 155, '...');
    }
    
    if ($current_len < 140) {
        $suffix = " Đọc ngay siêu phẩm sảng văn y học cổ truyền, cung đấu vả mặt kịch tính, bản dịch full mới nhất tại doctieuthuyet.com!";
        $needed = 158 - $current_len;
        if ($needed > 15) {
            $truncated_suffix = mb_substr($suffix, 0, $needed);
            $last_space = mb_strrpos($truncated_suffix, ' ');
            if ($last_space !== false && $last_space > ($needed * 0.7)) {
                $truncated_suffix = mb_substr($truncated_suffix, 0, $last_space);
            }
            $desc = $desc . rtrim($truncated_suffix, ' .!,') . '...';
        }
    }
    
    return $desc;
}

function get_focus_keyword($title) {
    $title_clean = preg_replace('/[:,\\-!?]/', ' ', $title);
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
global $wpdb;

foreach ($query->posts as $post) {
    $id = $post->ID;
    $title = $post->post_title;
    
    // 1. Optimize Title and Description
    $seo_title = generate_seo_title($title);
    $seo_desc = generate_seo_description($post->post_content, $title);
    $seo_keyword = get_focus_keyword($title);
    
    // 2. Optimize Permalink (slug) to strictly under 75 characters
    $slug = sanitize_title($title);
    if (strlen($slug) > 72) {
        $slug = substr($slug, 0, 72);
        $slug = rtrim($slug, '-');
    }
    
    // Update slug in database
    $wpdb->update($wpdb->posts, ['post_name' => $slug], ['ID' => $id]);
    
    // Update RankMath postmeta
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
        'slug' => $slug,
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
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_bulk_seo.php", timeout=180)
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

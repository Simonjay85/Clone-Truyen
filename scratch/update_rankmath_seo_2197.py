import ftplib
import urllib.request
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
STORY_ID = 2197

# Extremely optimized SEO clickbait texts
SEO_TITLE = "Chê Anh Thợ Hồ Nghèo Hèn, Giây Sau Chết Lặng Biết Thân Phận"
SEO_DESC = '"Mẹ vợ khinh bỉ đuổi tôi: \\\'Thằng thợ hồ rẻ rách!\\\' Ai ngờ 3 năm ẩn thân kết thúc, Chủ tịch Tập đoàn chính thức thức tỉnh, thâu tóm siêu dự án nghìn tỷ!"'
SEO_KEYWORD = "thợ hồ nghìn tỷ"

PHP_CODE = f"""<?php
require('./wp-load.php');
header('Content-Type: application/json');

$story_id = {STORY_ID};
$title = "{SEO_TITLE}";
$desc = '{SEO_DESC}';
$keyword = "{SEO_KEYWORD}";

// Update RankMath SEO Postmeta (both with and without underscore to be absolutely safe)
update_post_meta($story_id, '_rank_math_title', $title);
update_post_meta($story_id, '_rank_math_description', $desc);
update_post_meta($story_id, '_rank_math_focus_keyword', $keyword);

update_post_meta($story_id, 'rank_math_title', $title);
update_post_meta($story_id, 'rank_math_description', $desc);
update_post_meta($story_id, 'rank_math_focus_keyword', $keyword);

// Also set rich snippets & schemas
update_post_meta($story_id, 'rank_math_rich_snippet', 'article');

if (function_exists('litespeed_purge_all')) {{
    litespeed_purge_all();
}}

// Fetch updated values to confirm
echo json_encode([
    'success' => true,
    'story_id' => $story_id,
    'updated' => [
        'rank_math_title' => get_post_meta($story_id, '_rank_math_title', true),
        'rank_math_description' => get_post_meta($story_id, '_rank_math_description', true),
        'rank_math_focus_keyword' => get_post_meta($story_id, '_rank_math_focus_keyword', true)
    ]
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_update_rankmath.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading RankMath update helper via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing update via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_update_rankmath.php")
        print("Server Response:", req.read().decode('utf-8'))
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

import ftplib
import urllib.request
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

PHP_CODE = """<?php
require('./wp-load.php');
header('Content-Type: application/json');

$story_id = 2197;
$post = get_post($story_id);

if (!$post) {
    echo json_encode(['error' => 'Post not found']);
    exit;
}

$rank_math_title = get_post_meta($story_id, 'rank_math_title', true);
$rank_math_description = get_post_meta($story_id, 'rank_math_description', true);
$rank_math_focus_keyword = get_post_meta($story_id, 'rank_math_focus_keyword', true);

// Under score versions
$u_rank_math_title = get_post_meta($story_id, '_rank_math_title', true);
$u_rank_math_description = get_post_meta($story_id, '_rank_math_description', true);
$u_rank_math_focus_keyword = get_post_meta($story_id, '_rank_math_focus_keyword', true);

echo json_encode([
    'title' => $post->post_title,
    'excerpt' => $post->post_excerpt,
    'content_preview' => mb_substr(strip_tags($post->post_content), 0, 500),
    'rank_math' => [
        'title' => $rank_math_title,
        'description' => $rank_math_description,
        'keyword' => $rank_math_focus_keyword,
        '_title' => $u_rank_math_title,
        '_description' => $u_rank_math_description,
        '_keyword' => $u_rank_math_focus_keyword
    ]
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_read_post.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_read_post.php")
        print(req.read().decode('utf-8'))
    except Exception as e:
        print("Error fetching:", e)
        
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    main()

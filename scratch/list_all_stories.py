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

$args = [
    'post_type' => 'truyen',
    'posts_per_page' => -1,
    'post_status' => 'publish'
];
$query = new WP_Query($args);
$stories = [];

foreach ($query->posts as $post) {
    $id = $post->ID;
    $stories[] = [
        'id' => $id,
        'title' => $post->post_title,
        'slug' => $post->post_name,
        'excerpt' => $post->post_excerpt,
        'rank_math' => [
            'title' => get_post_meta($id, '_rank_math_title', true),
            'description' => get_post_meta($id, '_rank_math_description', true),
            'keyword' => get_post_meta($id, '_rank_math_focus_keyword', true)
        ]
    ];
}

echo json_encode($stories, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_list_stories.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_list_stories.php")
        data = json.loads(req.read().decode('utf-8'))
        print(f"Total stories found: {len(data)}")
        with open("scratch/all_stories_info.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✓ Saved to scratch/all_stories_info.json")
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

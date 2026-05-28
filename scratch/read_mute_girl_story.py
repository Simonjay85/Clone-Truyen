import urllib.request
import json
import ftplib
import os

php_code = """<?php
require('./wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'name' => 'co-gai-cam-mo-tiem-hoa-noi-ngon-ngu-cua-hoa-thay-loi-co-khong-noi-duoc',
    'posts_per_page' => 1
]);

if (empty($truyens)) {
    // Try custom search by keyword
    $truyens = get_posts([
        'post_type' => 'truyen',
        's' => 'Cô Gái Câm',
        'posts_per_page' => 1
    ]);
}

if (empty($truyens)) {
    echo json_encode(["error" => "Story not found"], JSON_PRETTY_PRINT);
    exit;
}

$t = $truyens[0];
$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $t->ID,
    'posts_per_page' => -1,
    'orderby' => 'ID',
    'order' => 'ASC'
]);

$stats = [
    "id" => $t->ID,
    "title" => $t->post_title,
    "slug" => $t->post_name,
    "intro" => wp_strip_all_tags($t->post_content),
    "excerpt" => wp_strip_all_tags($t->post_excerpt),
    "chapters" => []
];

foreach ($chaps as $c) {
    $content_clean = wp_strip_all_tags($c->post_content);
    // Count Vietnamese words by space splitting
    $vi_word_count = count(explode(' ', trim(preg_replace('/\\s+/', ' ', $content_clean))));
    $stats["chapters"][] = [
        "id" => $c->ID,
        "title" => $c->post_title,
        "word_count" => $vi_word_count,
        "content" => $content_clean
    ];
}

header('Content-Type: application/json');
echo json_encode($stats, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

def main():
    print("Writing temp_mute_girl.php locally...")
    with open("temp_mute_girl.php", "w", encoding="utf-8") as f:
        f.write(php_code)
        
    print("Uploading temp_mute_girl.php to remote via FTP...")
    try:
        ftp = ftplib.FTP("51.79.53.190")
        ftp.login("alotoinghe", "Nghia234!")
        with open("temp_mute_girl.php", "rb") as f:
            ftp.storbinary("STOR temp_mute_girl.php", f)
        ftp.quit()
        print("✓ Uploaded.")
        
        print("Fetching stats from URL...")
        url = "https://doctieuthuyet.com/temp_mute_girl.php"
        req = urllib.request.urlopen(url)
        response_data = req.read().decode('utf-8')
        
        # Save JSON output locally for evaluation
        out_path = "scratch/mute_girl_stats.json"
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(response_data)
        print(f"✓ Saved story data to {out_path}")
        
        # Cleanup remote
        print("Cleaning up remote temp_mute_girl.php...")
        ftp = ftplib.FTP("51.79.53.190")
        ftp.login("alotoinghe", "Nghia234!")
        ftp.delete("temp_mute_girl.php")
        ftp.quit()
        
        if os.path.exists("temp_mute_girl.php"):
            os.remove("temp_mute_girl.php")
            
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

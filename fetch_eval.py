import urllib.request
import json
import ftplib

php_code = """<?php
require('./wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => 2,
    'post_status' => 'publish',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$results = [];
foreach($truyens as $t) {
    $results[] = [
        'title' => $t->post_title,
        'synopsis' => wp_strip_all_tags($t->post_excerpt),
        'world' => get_post_meta($t->ID, '_temply_ai_world', true),
        'chars' => get_post_meta($t->ID, '_temply_ai_characters', true),
        'script' => get_post_meta($t->ID, '_temply_ai_script', true)
    ];
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($results, JSON_UNESCAPED_UNICODE);
?>"""

with open("temp_eval.php", "w") as f:
    f.write(php_code)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_eval.php", "rb") as f:
        ftp.storbinary("STOR temp_eval.php", f)
    ftp.quit()
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_eval.php")
    data = json.loads(req.read().decode('utf-8'))
    for idx, t in enumerate(data):
        print(f"=== TRUYỆN {idx+1} ===")
        print(f"TITLE: {t['title']}")
        print(f"SYNOPSIS:\n{t['synopsis']}\n")
        
except Exception as e:
    print("Error:", e)

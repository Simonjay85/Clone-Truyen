import urllib.request
import json
import ftplib
import urllib.parse
import ssl

php_code = """<?php
require_once('./wp-load.php');
$post_id = 3633;
$t = get_post($post_id);
if(empty($t)) die("Not found");

$chaps = get_posts([
    'post_type' => 'chuong',
    'meta_key' => '_truyen_id',
    'meta_value' => $post_id,
    'posts_per_page' => -1,
    'orderby' => 'meta_value_num',
    'meta_key' => '_chap_order',
    'order' => 'ASC'
]);

// If order is empty, fallback to ID order
if (empty($chaps)) {
    $chaps = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $post_id,
        'posts_per_page' => -1,
        'orderby' => 'ID',
        'order' => 'ASC'
    ]);
}

$genre_names = [];
$terms = wp_get_post_terms($post_id, 'the_loai');
foreach($terms as $term) {
    $genre_names[] = $term->name;
}

$rm_title = get_post_meta($post_id, 'rank_math_title', true);
$rm_desc = get_post_meta($post_id, 'rank_math_description', true);
$rm_keyword = get_post_meta($post_id, 'rank_math_focus_keyword', true);
$rm_title_u = get_post_meta($post_id, '_rank_math_title', true);
$rm_desc_u = get_post_meta($post_id, '_rank_math_description', true);
$rm_keyword_u = get_post_meta($post_id, '_rank_math_focus_keyword', true);

$thumb_id = get_post_thumbnail_id($post_id);
$alt_text = get_post_meta($thumb_id, '_wp_attachment_image_alt', true);

$output = [
    'id' => $t->ID,
    'title' => $t->post_title,
    'slug' => $t->post_name,
    'excerpt' => $t->post_excerpt,
    'genres' => $genre_names,
    'thumb_id' => $thumb_id,
    'thumb_alt' => $alt_text,
    'rank_math_title' => $rm_title ? $rm_title : $rm_title_u,
    'rank_math_description' => $rm_desc ? $rm_desc : $rm_desc_u,
    'rank_math_focus_keyword' => $rm_keyword ? $rm_keyword : $rm_keyword_u,
    'chapters' => []
];

foreach($chaps as $c) {
    $output['chapters'][] = [
        'id' => $c->ID,
        'title' => $c->post_title,
        'content' => wp_strip_all_tags($c->post_content)
    ];
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($output, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

with open("temp_read_sen.php", "w", encoding="utf-8") as f:
    f.write(php_code)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_read_sen.php", "rb") as f:
        ftp.storbinary("STOR temp_read_sen.php", f)
    ftp.quit()
    
    # disable ssl check just in case
    ctx = ssl._create_unverified_context()
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_read_sen.php", context=ctx)
    res_text = req.read().decode('utf-8')
    
    # Save the output
    with open("scratch/sen_tea_info.json", "w", encoding="utf-8") as f:
        f.write(res_text)
    
    # parse as json to print summary
    data = json.loads(res_text)
    print("Story ID:", data['id'])
    print("Title:", data['title'])
    print("Slug:", data['slug'])
    print("Genres:", data['genres'])
    print("Thumb ID:", data['thumb_id'])
    print("Thumb Alt:", data['thumb_alt'])
    print("SEO Focus:", data['rank_math_focus_keyword'])
    print("SEO Desc:", data['rank_math_description'])
    print("Number of Chapters:", len(data['chapters']))
    
except Exception as e:
    print("Error:", e)

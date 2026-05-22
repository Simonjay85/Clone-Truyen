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
    
    // Get categories/taxonomies of 'the_loai'
    $terms = wp_get_post_terms($id, 'the_loai');
    $genres = [];
    foreach ($terms as $t) {
        $genres[] = [
            'term_id' => $t->term_id,
            'name' => $t->name,
            'slug' => $t->slug
        ];
    }
    
    // Get featured image alt text
    $thumb_id = get_post_thumbnail_id($id);
    $alt_text = '';
    if ($thumb_id) {
        $alt_text = get_post_meta($thumb_id, '_wp_attachment_image_alt', true);
    }
    
    // Get comments count and list
    $comments_query = get_comments(['post_id' => $id, 'status' => 'approve']);
    $comments = [];
    foreach ($comments_query as $c) {
        $comments[] = [
            'author' => $c->comment_author,
            'content' => $c->comment_content,
            'date' => $c->comment_date
        ];
    }
    
    // Get RankMath SEO metadata
    $rm_title = get_post_meta($id, '_rank_math_title', true);
    $rm_desc = get_post_meta($id, '_rank_math_description', true);
    $rm_keyword = get_post_meta($id, '_rank_math_focus_keyword', true);
    
    $stories[] = [
        'id' => $id,
        'title' => $post->post_title,
        'slug' => $post->post_name,
        'genres' => $genres,
        'alt_text' => $alt_text,
        'comments_count' => count($comments),
        'comments' => $comments,
        'rank_math' => [
            'title' => $rm_title,
            'description' => $rm_desc,
            'keyword' => $rm_keyword
        ]
    ];
}

// Get all terms of the_loai to see what categories are available on the site
$all_terms = get_terms([
    'taxonomy' => 'the_loai',
    'hide_empty' => false
]);
$available_genres = [];
foreach ($all_terms as $t) {
    $available_genres[] = [
        'term_id' => $t->term_id,
        'name' => $t->name,
        'slug' => $t->slug,
        'count' => $t->count
    ];
}

echo json_encode([
    'success' => true,
    'total_stories' => count($stories),
    'available_genres' => $available_genres,
    'stories' => $stories
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
?>"""

def main():
    temp_file = "temp_audit_all.php"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading audit script via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(temp_file, "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing audit script via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_audit_all.php", timeout=120)
        response_data = json.loads(req.read().decode('utf-8'))
        print(f"Total stories found on WordPress: {response_data['total_stories']}")
        print(f"Available categories in taxonomy 'the_loai': {[g['name'] for g in response_data['available_genres']]}")
        
        with open("scratch/full_site_audit.json", "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=2)
        print("✓ Detailed audit saved to scratch/full_site_audit.json")
    except Exception as e:
        print("Error executing audit:", e)
        
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

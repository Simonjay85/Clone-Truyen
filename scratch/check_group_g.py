import ftplib
import urllib.request
import json

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
GROUP_G_IDS = [2023, 2035, 2044, 2052, 2067]

PHP_CODE = """<?php
require_once('wp-load.php');
header('Content-Type: application/json; charset=utf-8');

$ids = [2023, 2035, 2044, 2052, 2067];
$list = [];

foreach ($ids as $id) {
    $post = get_post($id);
    if ($post) {
        $chapters = get_posts([
            'post_type' => 'chuong',
            'posts_per_page' => -1,
            'meta_key' => '_truyen_id',
            'meta_value' => $id,
            'orderby' => 'ID',
            'order' => 'ASC',
            'post_status' => 'any'
        ]);
        
        $chaps_list = [];
        foreach ($chapters as $c) {
            $chaps_list[] = [
                'id' => $c->ID,
                'title' => $c->post_title,
                'status' => $c->post_status
            ];
        }
        
        $list[$id] = [
            'id' => $post->ID,
            'title' => $post->post_title,
            'status' => $post->post_status,
            'intro' => $post->post_content,
            'focus_keyword' => get_post_meta($id, 'rank_math_focus_keyword', true),
            'seo_title' => get_post_meta($id, 'rank_math_title', true),
            'seo_description' => get_post_meta($id, 'rank_math_description', true),
            'chapter_count' => count($chapters),
            'chapters' => $chaps_list
        ];
    } else {
        $list[$id] = null;
    }
}

echo json_encode($list, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

def main():
    temp_file = "temp_check_group_g.php"
    with open(f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/{temp_file}", "w", encoding="utf-8") as f:
        f.write(PHP_CODE)
        
    print("Uploading temp_check_group_g.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    with open(f"/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/{temp_file}", "rb") as f:
        ftp.storbinary(f"STOR {temp_file}", f)
    ftp.quit()
    print("✓ Uploaded.")
    
    print("Executing check via HTTP...")
    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_check_group_g.php", timeout=60)
        data = json.loads(req.read().decode('utf-8'))
        
        for id_str, story in data.items():
            print("\n" + "=" * 50)
            if story is None:
                print(f"Story ID {id_str}: NOT FOUND")
                continue
            print(f"Story ID {id_str}: {story['title']}")
            print(f"  Status: {story['status']}")
            print(f"  SEO Keyword: {story['focus_keyword']}")
            print(f"  SEO Title: {story['seo_title']}")
            print(f"  SEO Description: {story['seo_description']}")
            print(f"  Chapters count: {story['chapter_count']}")
            if story['chapters']:
                print("  Chapters sample (first & last):")
                print(f"    - First: {story['chapters'][0]['title']} (ID: {story['chapters'][0]['id']})")
                print(f"    - Last: {story['chapters'][-1]['title']} (ID: {story['chapters'][-1]['id']})")
            
    except Exception as e:
        print("Error:", e)
        
    print("\nCleaning up...")
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.delete(temp_file)
    ftp.quit()
    print("✓ Remote cleanup done.")

if __name__ == "__main__":
    main()

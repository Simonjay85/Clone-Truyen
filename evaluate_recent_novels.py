import ftplib
import urllib.request
import json
import os

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"

def run():
    php_code = """<?php
require('./wp-load.php');
$truyens = get_posts([
    'post_type' => 'truyen',
    'posts_per_page' => 50,
    'post_status' => 'any',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$results = [];
foreach($truyens as $t) {
    // Get chapters
    $chaps = get_posts([
        'post_type' => 'chuong',
        'posts_per_page' => -1,
        'meta_key' => '_truyen_id',
        'meta_value' => $t->ID,
        'orderby' => 'menu_order date',
        'order' => 'ASC',
        'fields' => 'ids'
    ]);
    
    // Check first and last chapter content
    $first_chap_title = "";
    $first_chap_len = 0;
    $first_chap_content = "";
    $last_chap_title = "";
    $last_chap_len = 0;
    
    if (count($chaps) > 0) {
        $first_chap = get_post($chaps[0]);
        $first_chap_title = $first_chap->post_title;
        $first_chap_content = wp_strip_all_tags($first_chap->post_content);
        $first_chap_len = mb_strlen($first_chap_content, 'utf-8');
        
        $last_chap = get_post($chaps[count($chaps)-1]);
        $last_chap_title = $last_chap->post_title;
        $last_chap_len = mb_strlen(wp_strip_all_tags($last_chap->post_content), 'utf-8');
    }
    
    // Get tags/categories
    $genres = wp_get_post_terms($t->ID, 'the_loai', ['fields' => 'names']);
    
    $results[] = [
        'id' => $t->ID,
        'title' => $t->post_title,
        'slug' => $t->post_name,
        'status' => $t->post_status,
        'date' => $t->post_date,
        'synopsis' => wp_strip_all_tags($t->post_excerpt),
        'chapters_count' => count($chaps),
        'first_chap_title' => $first_chap_title,
        'first_chap_len' => $first_chap_len,
        'first_chap_excerpt' => mb_substr($first_chap_content, 0, 150, 'utf-8'),
        'last_chap_title' => $last_chap_title,
        'last_chap_len' => $last_chap_len,
        'genres' => $genres,
        'author' => get_post_meta($t->ID, '_author', true)
    ];
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>"""

    print("Uploading evaluate_helper.php via FTP...")
    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("evaluate_helper.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("evaluate_helper.php", "rb") as f:
        ftp.storbinary("STOR evaluate_helper.php", f)
    ftp.quit()
    print("Uploaded successfully!")

    try:
        print("Calling evaluate_helper.php over HTTP...")
        req = urllib.request.urlopen("https://doctieuthuyet.com/evaluate_helper.php", timeout=60)
        data = req.read().decode('utf-8')
        print("Response received! Parsing JSON...")
        
        # Save to local review file
        with open("recent_50_stories_detailed.json", "w", encoding="utf-8") as out:
            out.write(data)
        print("Saved detailed stories to recent_50_stories_detailed.json")
        
        stories = json.loads(data)
        
        # Perform some automated basic evaluation
        issues = []
        for s in stories:
            s_issues = []
            if not s['title'] or s['title'] == "DTT" or "Truyện Chờ Tên" in s['title'] or "Truyện chờ phân tích" in s['title']:
                s_issues.append("Tiêu đề rỗng/tạm")
            if s['slug'] == str(s['id']):
                s_issues.append("Slug là ID (không có title lúc tạo)")
            if not s['synopsis'] or "1. Bối cảnh Thế Giới" in s['synopsis'] or s['synopsis'].strip() == "1. Bối cảnh Thế Giới 2. Nhân Vật 3. Kịch Bản":
                s_issues.append("Văn án rỗng (Fallback HTML)")
            if s['chapters_count'] < 5:
                s_issues.append(f"Ít chương ({s['chapters_count']})")
            if s['first_chap_len'] < 100:
                s_issues.append(f"Nội dung chương 1 quá ngắn ({s['first_chap_len']} ký tự)")
            if s['last_chap_len'] < 100:
                s_issues.append(f"Nội dung chương cuối quá ngắn ({s['last_chap_len']} ký tự)")
            
            if s_issues:
                issues.append({
                    'id': s['id'],
                    'title': s['title'],
                    'slug': s['slug'],
                    'chapters': s['chapters_count'],
                    'issues': s_issues
                })
        
        print("\n=== KẾT QUẢ ĐÁNH GIÁ TỰ ĐỘNG ===")
        print(f"Tổng số truyện đã đánh giá: {len(stories)}")
        print(f"Số truyện phát hiện có lỗi: {len(issues)}")
        for idx, iss in enumerate(issues):
            print(f"[{idx+1}] ID: {iss['id']} | Tên: {iss['title']} | Chương: {iss['chapters']} | Lỗi: {', '.join(iss['issues'])}")
            
    except Exception as e:
        print(f"Error calling URL: {e}")
    finally:
        print("Deleting evaluate_helper.php from server...")
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("evaluate_helper.php")
            print("Deleted successfully!")
        except Exception as e:
            print(f"Error deleting file: {e}")
        ftp.quit()
        if os.path.exists("evaluate_helper.php"):
            os.remove("evaluate_helper.php")

if __name__ == "__main__":
    run()

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
    'post_status' => 'publish',
    'orderby' => 'date',
    'order' => 'DESC'
]);

$results = [];

foreach($truyens as $t) {
    $chaps = get_posts([
        'post_type' => 'chuong',
        'meta_key' => '_truyen_id',
        'meta_value' => $t->ID,
        'posts_per_page' => -1,
        'orderby' => 'menu_order date',
        'order' => 'ASC'
    ]);
    
    $story_errors = [];
    
    foreach($chaps as $idx => $c) {
        $content = $c->post_content;
        $chap_errors = [];
        
        // 1. Check if markdown code block leaked
        if (strpos($content, '```') !== false) {
            $chap_errors[] = "Rò rỉ ký tự markdown (```)";
        }
        
        // 2. Check if content is too short
        $clean_len = mb_strlen(wp_strip_all_tags($content), 'utf-8');
        if ($clean_len < 500) {
            $chap_errors[] = "Nội dung quá ngắn (" . $clean_len . " ký tự)";
        }
        
        // 3. Check if there are no <p> tags at all
        if (strpos($content, '<p>') === false) {
            $chap_errors[] = "Thiếu thẻ phân đoạn <p>";
        }
        
        // 4. Check for unescaped HTML tags or AI meta text leaking
        if (preg_match('/TITLE\s*:/i', $content) || preg_match('/CONTENT\s*:/i', $content)) {
            $chap_errors[] = "Rò rỉ nhãn phân đoạn AI (TITLE: hoặc CONTENT:)";
        }
        
        // 5. Check if it has escaped quotes like \\"
        if (strpos($content, '\\"') !== false) {
            $chap_errors[] = "Lỗi thoát ký tự dấu nháy (\\\")";
        }
        
        if (!empty($chap_errors)) {
            $story_errors[] = [
                'chap_id' => $c->ID,
                'chap_title' => $c->post_title,
                'index' => $idx + 1,
                'errors' => $chap_errors
            ];
        }
    }
    
    if (!empty($story_errors)) {
        $results[] = [
            'id' => $t->ID,
            'title' => $t->post_title,
            'slug' => $t->post_name,
            'chapters_count' => count($chaps),
            'errors' => $story_errors
        ];
    }
}

header('Content-Type: application/json; charset=utf-8');
echo json_encode($results, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
exit;
?>"""

    ftp = ftplib.FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    with open("temp_deep_audit.php", "w", encoding="utf-8") as f:
        f.write(php_code)
    
    with open("temp_deep_audit.php", "rb") as f:
        ftp.storbinary("STOR temp_deep_audit.php", f)
    ftp.quit()

    try:
        req = urllib.request.urlopen("https://doctieuthuyet.com/temp_deep_audit.php", timeout=90)
        data = req.read().decode('utf-8')
        
        # Save to local file
        with open("deep_audit_results.json", "w", encoding="utf-8") as out:
            out.write(data)
            
        results = json.loads(data)
        print("\n=== KẾT QUẢ ĐÁNH GIÁ CHUYÊN SÂU NỘI DUNG CHƯƠNG ===")
        print(f"Tổng số truyện phát hiện lỗi nội dung chương: {len(results)}")
        
        for idx, s in enumerate(results):
            print(f"\n[{idx+1}] ID: {s['id']} | {s['title']}")
            print(f"    Số chương: {s['chapters_count']} | Link: https://doctieuthuyet.com/{s['slug']}")
            print("    Các chương lỗi phát hiện:")
            for err in s['errors']:
                print(f"      - {err['chap_title']} (ID: {err['chap_id']}) [Chương {err['index']}]:")
                for e in err['errors']:
                    print(f"        * {e}")
                    
    except Exception as e:
        print("Error:", e)
    finally:
        ftp = ftplib.FTP(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)
        try:
            ftp.delete("temp_deep_audit.php")
        except:
            pass
        ftp.quit()
        if os.path.exists("temp_deep_audit.php"):
            os.remove("temp_deep_audit.php")

if __name__ == "__main__":
    run()

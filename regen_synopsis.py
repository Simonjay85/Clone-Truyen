import ftplib
import urllib.request
import json
import time

php_code = """<?php
require('./wp-load.php');
$action = $_GET['action'] ?? '';

if($action === 'list') {
    $truyens = get_posts(['post_type' => 'truyen', 'posts_per_page' => -1]);
    $ids = [];
    foreach($truyens as $t) {
        if(empty($t->post_excerpt) || strpos($t->post_excerpt, '1. Bối cảnh') !== false || strlen(trim($t->post_excerpt)) < 60) {
            $ids[] = $t->ID;
        }
    }
    echo json_encode($ids);
    exit;
}

if($action === 'regen') {
    require_once(ABSPATH . 'wp-content/plugins/temply-ai-factory/includes/openai-api.php');
    $id = intval($_GET['id']);
    
    $chaps = get_posts(['post_type' => 'chuong', 'meta_key' => '_truyen_id', 'meta_value' => $id, 'posts_per_page' => 1, 'orderby' => 'ID', 'order' => 'ASC']);
    $content = wp_strip_all_tags(get_post_field('post_content', $id));
    if(!empty($chaps)) {
        $content .= "\n\n" . wp_strip_all_tags($chaps[0]->post_content);
    }
    $content = mb_substr($content, 0, 3000);
    
    $sys = "Bạn là biên tập viên tiểu thuyết tài ba. Nhiệm vụ: viết ĐOẠN TÓM TẮT lôi cuốn từ thông tin thô.";
    $user = "NỘI DUNG THÔ:\n" . $content . "\n\nYÊU CẦU: Dựa vào thông tin trên, viết một bảng Tóm tắt Truyện (Synopsis) siêu cuốn hút dài tầm 150-200 chữ. Mở đầu bằng một HOOK (câu thả thính/cẩu huyết/gây tò mò) được bôi đậm (in đậm). TRẢ VỀ DUY NHẤT LỜI TÓM TẮT.";
    
    $model = get_option('temply_ai_model', 'gemini-1.5-flash');
    $res = temply_call_ai($sys, $user, 0.7, $model);
    
    if(!is_wp_error($res) && !empty($res)) {
        $clean = trim(preg_replace('/```(?:html|json)?|```/', '', $res));
        // Replace **hook** with <strong>hook</strong>
        $clean = preg_replace('/\*\*(.*?)\*\*/', '<strong>$1</strong>', $clean);
        
        // Cấu trúc lại post content cho đẹp
        $new_content_html = "<div class='ai-synopsis' style='font-size:15px; line-height:1.7;'>" . nl2br($clean) . "</div>";
        
        wp_update_post([
            'ID' => $id,
            'post_excerpt' => wp_trim_words(wp_strip_all_tags($clean), 40, '...'),
            'post_content' => $new_content_html
        ]);
        echo "OK - " . $id;
    } else {
        echo "ERR - " . $id;
    }
}
?>"""

with open("temp_regen.php", "w") as f:
    f.write(php_code)

try:
    ftp = ftplib.FTP("51.79.53.190")
    ftp.login("alotoinghe", "Nghia234!")
    with open("temp_regen.php", "rb") as f:
        ftp.storbinary("STOR temp_regen.php", f)
    ftp.quit()
    
    print("Fetching IDs...")
    req = urllib.request.urlopen("https://doctieuthuyet.com/temp_regen.php?action=list")
    ids = json.loads(req.read().decode("utf-8"))
    print(f"Tracking {len(ids)} missing synopses...")
    
    for rid in ids:
        time.sleep(1) # Rate limit protection
        try:
            r = urllib.request.urlopen(f"https://doctieuthuyet.com/temp_regen.php?action=regen&id={rid}", timeout=45)
            print(r.read().decode("utf-8"))
        except Exception as ex:
            print("Failed ID", rid, ":", ex)

except Exception as e:
    print("Error:", e)

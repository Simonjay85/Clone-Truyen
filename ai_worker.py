import os
import time
import requests
import argparse
from crawler import get_novel_details, get_chapter_content, get_fanqie_details, get_fanqie_chapter, push_to_wordpress, HEADERS
import openai

# Cấu hình Cố định
POLL_INTERVAL = 10 # Giây

def report_status(wp_url, auth_headers, job_id, status, novel_title=None, total_chapters=None, crawled_chapters=None, error_log=None):
    api = f"{wp_url.rstrip('/')}/index.php/wp-json/crawler/v1/update-status"
    data = {
        "job_id": job_id,
        "status": status
    }
    if novel_title is not None: data["novel_title"] = novel_title
    if total_chapters is not None: data["total_chapters"] = total_chapters
    if crawled_chapters is not None: data["crawled_chapters"] = crawled_chapters
    if error_log is not None: data["error_log"] = error_log
    
    try:
        requests.post(api, json=data, headers=auth_headers, timeout=10)
    except Exception as e:
        print(f"[{job_id}] Lỗi báo cáo trạng thái WP: {e}")

def rewrite_content_with_ai(original_text, openai_key):
    if not openai_key or len(original_text) < 50:
        return original_text
        
    try:
        openai.api_key = openai_key
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Bạn là dịch giả truyện tuyệt đỉnh. MỆNH LỆNH TỐI THƯỢNG: Tuyệt đối chỉ sử dụng 100% TIẾNG VIỆT tự nhiên. Cấm tuyệt đối việc chèn, mix bất kỳ từ vựng Tiếng Anh nào (vd: murmured, sighed, hello...) vào nội dung. Nếu có thì phải dịch mượt sang Tiếng Việt. Phản hồi trực tiếp bản dịch hoàn chỉnh."},
                {"role": "user", "content": original_text[:4000]} # Giới hạn chữ nếu quá dài
            ],
            max_tokens=2000,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Lỗi AI Rewrite: {e}")
        return original_text # Giữ nguyên văn bản gốc nếu API sập

def process_job(job, wp_url, wp_user, wp_pass, openai_key):
    job_id = job['id']
    url = job['novel_url']
    ai_rewrite = int(job.get('ai_rewrite', 0)) == 1
    
    import base64
    auth_token = base64.b64encode(f"{wp_user}:{wp_pass}".encode('utf-8')).decode('utf-8')
    auth_headers = {"Authorization": f"Basic {auth_token}", "Content-Type": "application/json"}
    
    print(f"\n[JOB {job_id}] Bắt đầu xử lý: {url}")
    
    try:
        # Bước 1: Lấy chi tiết truyện
        if 'fanqienovel.com' in url or url.startswith('fanqie-'):
            print(f"[{job_id}] Kích hoạt bộ quét sơ cua FanqieNovel...")
            novel_data = get_fanqie_details(url)
            # Ép luôn bật AI Translation vì đây là Tiếng Trung
            ai_rewrite = True 
        else:
            novel_data = get_novel_details(url)
        if not novel_data:
            report_status(wp_url, auth_headers, job_id, "error", error_log="Không thể nạp nội dung truyện từ URL.")
            return

        total_chapters = len(novel_data['chapters'])
        novel_title = novel_data['title']
        
        report_status(wp_url, auth_headers, job_id, "processing", novel_title, total_chapters, 0)
        
        # Bước 2: Bắn Job Lên WP (Truyện)
        truyen_api = f"{wp_url.rstrip('/')}/index.php/wp-json/wp/v2/truyen"
        
        # Extract fake_meta
        fake_meta = None
        fake_meta_str = job.get('fake_meta', '')
        if fake_meta_str:
            try:
                import json
                fake_meta = json.loads(fake_meta_str)
            except: pass

        intro_content = novel_data.get("intro", "")
        if ai_rewrite:
            print(f"[{job_id}] AI đang viết lại Tóm Tắt...")
            intro_content = rewrite_content_with_ai(intro_content, openai_key)
            time.sleep(1)
            
        truyen_payload = {
            "title": novel_title,
            "content": intro_content,
            "status": "publish",
            "meta": {}
        }
        
        if fake_meta:
            if 'date' in fake_meta and fake_meta['date']:
                truyen_payload['date'] = fake_meta['date'] + " 00:00:00"
            if 'views' in fake_meta:
                truyen_payload['meta']['_views'] = int(fake_meta['views'])
            if 'hot' in fake_meta:
                truyen_payload['meta']['_is_hot'] = int(fake_meta['hot'])

        res = requests.post(truyen_api, json=truyen_payload, headers=auth_headers)
        res.raise_for_status()
        wp_truyen_id = res.json()["id"]
        
        # Bước 3: Vòng lặp bắn từng chương
        chuong_api = f"{wp_url.rstrip('/')}/index.php/wp-json/wp/v2/chuong"
        crawled = 0
        
        for chap in novel_data['chapters']:
            print(f"  -> Cào chương: {chap['title']}")
            if 'fanqienovel.com' in url or chap['url'].startswith('fanqie-'):
                chap_content = get_fanqie_chapter(chap["url"])
            else:
                chap_content = get_chapter_content(chap["url"])
            
            if ai_rewrite:
                print(f"  -> AI đang viết lại chương...")
                chap_content = rewrite_content_with_ai(chap_content, openai_key)
                
            chuong_payload = {
                "title": chap["title"],
                "content": chap_content,
                "status": "publish",
                "meta": { "_truyen_id": wp_truyen_id }
            }
            
            # Post lên WP
            requests.post(chuong_api, json=chuong_payload, headers=auth_headers)
            crawled += 1
            
            # Cập nhật tiến độ mỗi chương
            if crawled % 2 == 0 or crawled == total_chapters:
                report_status(wp_url, auth_headers, job_id, "processing", crawled_chapters=crawled)
                
            time.sleep(1.5) # Tránh Rate Limit chống phá hoại

        # Hoàn tất tiến trình
        report_status(wp_url, auth_headers, job_id, "completed", crawled_chapters=crawled)
        print(f"[{job_id}] HOÀN THÀNH.")
        
    except Exception as e:
        error_msg = str(e)[:200]
        report_status(wp_url, auth_headers, job_id, "error", error_log=error_msg)
        print(f"[{job_id}] LỖI: {error_msg}")

def run_worker(wp_url, wp_user, wp_pass, openai_key):
    print("="*50)
    print("🤖 AUTO CRAWLER AI WORKER - Đang lắng nghe nhiệm vụ...")
    print(f"📍 Target API: {wp_url}")
    print("="*50)
    
    api_endpoint = f"{wp_url.rstrip('/')}/index.php/wp-json/crawler/v1/get-task"
    
    while True:
        try:
            # Lấy Cấu Hình (OpenAI Key từ WP) nếu user không truyền bằng CLI
            if not openai_key:
                settings_api = f"{wp_url.rstrip('/')}/index.php/wp-json/crawler/v1/settings"
                settings_api_nocache = f"{settings_api}?t={time.time()}"
                try:
                    set_res = requests.get(settings_api_nocache, timeout=5)
                    openai_key = set_res.json().get('openai_key', '')
                    if openai_key:
                        print(f" [!] Đã nạp thành công API Key OpenAI từ Website: {openai_key[:5]}***")
                except Exception as ex:
                    print(f" [Cảnh báo] Lỗi lấy API Key: {ex}")

            # Chống bộ nhớ đệm (Cache) của máy chủ bằng timestamp
            api_endpoint_nocache = f"{api_endpoint}?t={time.time()}"
            res = requests.get(api_endpoint_nocache, timeout=10)
            data = res.json()
            
            if data.get("success") and data.get("task"):
                job = data["task"]
                process_job(job, wp_url, wp_user, wp_pass, openai_key)
            else:
                pass # No task
        except Exception as e:
            print(f"Lỗi mạng hoặc tải nhiệm vụ: {e}")
            import traceback; traceback.print_exc()
            time.sleep(5)
            
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chạy Worker AI ngầm")
    parser.add_argument("--wp-url", type=str, required=True, help="Domain wp")
    parser.add_argument("--wp-user", type=str, required=True, help="Tài khoản WP")
    parser.add_argument("--wp-pass", type=str, required=True, help="Password WP")
    parser.add_argument("--openai-key", type=str, default="", help="Khoá API của OpenAI (Bắt buộc nếu bật AI Rewrite)")
    
    args = parser.parse_args()
    run_worker(args.wp_url, args.wp_user, args.wp_pass, args.openai_key)

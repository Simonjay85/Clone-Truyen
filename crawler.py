import requests
from bs4 import BeautifulSoup
import json
import time
import os
import argparse
import urllib.parse
import re
import base64

DATA_DIR = "data"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

def setup_env():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def get_wp_auth_header(user, password):
    token = base64.b64encode(f"{user}:{password}".encode('utf-8')).decode('utf-8')
    return {"Authorization": f"Basic {token}"}

def push_to_wordpress(wp_url, wp_user, wp_pass, novel_data):
    print(f"\n[WP Sync] Đang đồng bộ truyện: {novel_data['title']}")
    headers = get_wp_auth_header(wp_user, wp_pass)
    headers["Content-Type"] = "application/json"
    
    # 1. Tạo Truyện
    truyen_api = f"{wp_url.rstrip('/')}/wp-json/wp/v2/truyen"
    truyen_payload = {
        "title": novel_data["title"],
        "content": novel_data.get("intro", ""),
        "status": "publish"
    }
    
    try:
        res = requests.post(truyen_api, json=truyen_payload, headers=headers)
        res.raise_for_status()
        wp_truyen_id = res.json()["id"]
        print(f"  -> Đã tạo truyện thành công trên WP (ID: {wp_truyen_id})")
    except Exception as e:
        print(f"  -> Lỗi khi tạo truyện: {e}")
        if 'res' in locals(): print(res.text)
        return
        
    # 2. Tạo các Chương và gắn Meta _truyen_id
    chuong_api = f"{wp_url.rstrip('/')}/wp-json/wp/v2/chuong"
    total = len(novel_data['chapters'])
    
    for i, chap in enumerate(novel_data['chapters'], 1):
        print(f"  -> Đồng bộ chương {i}/{total}: {chap['title']}")
        chuong_payload = {
            "title": chap["title"],
            "content": chap["content"],
            "status": "publish",
            "meta": {
                "_truyen_id": wp_truyen_id
            }
        }
        try:
            c_res = requests.post(chuong_api, json=chuong_payload, headers=headers)
            c_res.raise_for_status()
        except Exception as e:
            print(f"     -> Lỗi tạo chương: {e}")
        time.sleep(0.5) # Tránh nghẽn server WP

def crawl_category(category_url_or_slug, max_pages=1):
    print(f"Bắt đầu crawl danh mục với {max_pages} trang...")
    all_novels = []
    api_url = "https://tehitruyen.com/sources/ajax/mongdaovien/load-truyen-hoan-thanh.php"
    
    for page in range(1, max_pages + 1):
        print(f" Đang tải trang {page}...")
        try:
            res = requests.post(api_url, data={"page": page}, headers=HEADERS, timeout=10)
            res.raise_for_status()
            text = res.text.encode('utf-8').decode('utf-8-sig')
            data = json.loads(text)
            
            html = data.get("html", "")
            if not html: break
                
            soup = BeautifulSoup(html, "html.parser")
            for a in soup.find_all("a", href=True):
                href = a["href"]
                title_tag = a.find("h3", class_="truyen-comic-title")
                title = title_tag.text.strip() if title_tag else ""
                
                novel = {
                    "url": urllib.parse.urljoin("https://tehitruyen.com", href),
                    "title": title,
                }
                if novel["url"] not in [n["url"] for n in all_novels]:
                    all_novels.append(novel)
            print(f"   -> Đã lấy {len(all_novels)} truyện tính đến trang {page}")
        except Exception as e:
            print(f"Lỗi khi load trang {page}: {e}")
            break
        time.sleep(1.5)
    return all_novels

def get_novel_details(novel_url):
    print(f"\nLấy dữ liệu truyện: {novel_url}")
    try:
        res = requests.get(novel_url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        title_tag = soup.find('div', class_='mdv-san-pham-show-name')
        title = title_tag.text.strip() if title_tag else "Unknown Title"
        
        intro_tag = soup.find('div', class_='mdv-san-pham-show-gioi-thieu')
        intro = intro_tag.text.strip() if intro_tag else ""
        
        chapters = []
        for a in soup.select('.mdv-san-pham-show-dsc-table-chuong a'):
            chap_url = urllib.parse.urljoin("https://tehitruyen.com", a["href"])
            chapters.append({
                "title": a.text.strip(),
                "url": chap_url,
                "content": "" 
            })
        
        return {
            "title": title,
            "url": novel_url,
            "intro": intro,
            "chapters": chapters
        }
    except Exception as e:
        print(f" Lỗi lấy thông tin: {e}")
        return None

def get_chapter_content(chapter_url):
    try:
        res = requests.get(chapter_url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        content_div = soup.find('div', id='noi_dung_truyen')
        if content_div:
            return content_div.get_text(separator="\n\n", strip=True)
        return ""
    except Exception as e:
        print(f"Lỗi tải {chapter_url}: {e}")
        return ""

def crawl_full_novel(novel_url, wp_url=None, wp_user=None, wp_pass=None):
    setup_env()
    novel_data = get_novel_details(novel_url)
    if not novel_data: return
        
    print(f"Bắt đầu crawl {len(novel_data['chapters'])} chương của '{novel_data['title']}'...")
    
    for chap in novel_data['chapters']:
        print(f" Cào {chap['title']}...")
        chap["content"] = get_chapter_content(chap["url"])
        time.sleep(1)
        
    slug = re.sub(r'[^a-zA-Z0-9_\-]', '_', novel_url.split("/")[-1].replace(".html", ""))
    output_path = os.path.join(DATA_DIR, f"{slug}.json")
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(novel_data, f, ensure_ascii=False, indent=4)
    print(f"Hoàn tất lưu File: {output_path}")

    # Push to WP if info provides
    if wp_url and wp_user and wp_pass:
        push_to_wordpress(wp_url, wp_user, wp_pass, novel_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TeHiTruyen Crawler Bot (có Sync WP)")
    parser.add_argument("--mode", type=str, choices=["category", "novel"], default="novel", help="Chế độ cào")
    parser.add_argument("--url", type=str, default="", help="Link truyện (nếu mode=novel)")
    parser.add_argument("--pages", type=int, default=1, help="Số lượng danh sách")
    
    parser.add_argument("--wp-url", type=str, help="Domain wp, ví dụ: https://myweb.com")
    parser.add_argument("--wp-user", type=str, help="Tài khoản admin WP")
    parser.add_argument("--wp-pass", type=str, help="Application Password của WP")

    args = parser.parse_args()
    setup_env()
    
    if args.mode == "category":
        novels = crawl_category(max_pages=args.pages)
        for nov in novels:
            crawl_full_novel(nov["url"], args.wp_url, args.wp_user, args.wp_pass)
    elif args.mode == "novel":
        if not args.url:
            print("Cần tham số --url")
        else:
            crawl_full_novel(args.url, args.wp_url, args.wp_user, args.wp_pass)


def get_fanqie_details(url, cookies=None):
    # Kiến trúc trích xuất truyện từ Fanqie
    # LƯU Ý: FanqieNovel hiện chặn gắt gao các luồng lấy dữ liệu. Hàm này cần có Session Cookie thật để không bị 404.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }
    if cookies: headers['Cookie'] = cookies
    
    # Giả lập trả về cấu trúc cho AI Worker (Để anh test trước hệ thống Dịch AI)
    # Vì Fanqie block 404, em dùng Fake Data chuẩn form để kích hoạt Pipeline AI Translation.
    return {
        "title": "[Fanqie] Tiêu đề Truyện Mẫu (Đang Fake do bị chặn Captcha)",
        "intro": "Đây là giới thiệu truyện tiếng Trung. Trong tương lai sẽ viết regex HTML parse ở đây.",
        "chapters": [
            {"title": "第1章 楔子", "url": "fanqie-1"},
            {"title": "第2章 穿越", "url": "fanqie-2"}
        ]
    }

def get_fanqie_chapter(url, cookies=None):
    return "这是一段测试中文文本。你需要使用AI将其翻译成越南语。" # Mock tiếng Trung

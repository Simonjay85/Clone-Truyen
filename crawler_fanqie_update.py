import re

with open("crawler.py", "r", encoding="utf-8") as f:
    crawler = f.read()

fanqie_functions = """
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
"""

if "get_fanqie_details" not in crawler:
    crawler += "\n" + fanqie_functions
    with open("crawler.py", "w", encoding="utf-8") as f:
        f.write(crawler)
    print("Added Fanqie skeletons to crawler.py")

with open("ai_worker.py", "r", encoding="utf-8") as f:
    worker = f.read()

# Update import
worker = worker.replace(
    "from crawler import get_novel_details, get_chapter_content", 
    "from crawler import get_novel_details, get_chapter_content, get_fanqie_details, get_fanqie_chapter"
)

# Update AI Prompt for Translation
old_ai = '{"role": "system", "content": "Bạn là một biên tập viên viết lại truyện đọc. Hãy viết lại nội dung sau sao cho lôi cuốn hơn, thay đổi văn phong một chút nhưng giữ nguyên mạch truyện cốt lõi."}'
new_ai = '{"role": "system", "content": "Bạn là dịch giả truyện Trung Quốc chuyên nghiệp. Hãy biên dịch đoạn văn bản tiếng Trung (hoặc cải thiện tiếng Việt) sau đây sang tiếng Việt một cách mượt mà, thuần Việt, đúng văn phong tiên hiệp/ngôn tình. Trả về trực tiếp nội dung dịch, không chèn chú thích dư thừa."}'
worker = worker.replace('model="gpt-3.5-turbo", # Hoặc gpt-4', 'model="gpt-4o-mini",')
worker = worker.replace(old_ai, new_ai)

# Update process_job routing
# Currently: novel_data = get_novel_details(url)
routing_logic = """
        if 'fanqienovel.com' in url or url.startswith('fanqie-'):
            print(f"[{job_id}] Kích hoạt bộ quét sơ cua FanqieNovel...")
            novel_data = get_fanqie_details(url)
            # Ép luôn bật AI Translation vì đây là Tiếng Trung
            ai_rewrite = True 
        else:
            novel_data = get_novel_details(url)
"""
worker = re.sub(r'novel_data = get_novel_details\(url\)', routing_logic.strip(), worker)

# Update chapter content routing
chap_routing = """
            if 'fanqienovel.com' in url or chap['url'].startswith('fanqie-'):
                chap_content = get_fanqie_chapter(chap["url"])
            else:
                chap_content = get_chapter_content(chap["url"])
"""
worker = re.sub(r'chap_content = get_chapter_content\(chap\["url"\]\)', chap_routing.strip(), worker)

with open("ai_worker.py", "w", encoding="utf-8") as f:
    f.write(worker)

print("Updated ai_worker.py pipeline!")

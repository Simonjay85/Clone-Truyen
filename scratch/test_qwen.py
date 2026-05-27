import requests
import json
import time

def test():
    local_url = "http://127.0.0.1:8000/v1/chat/completions"
    
    system_prompt = """Bạn là biên tập viên văn học và bậc thầy sảng văn/vả mặt (web novel) hàng đầu Việt Nam.
Nhiệm vụ của bạn là lập kế hoạch cho một bộ truyện sảng văn/vả mặt 10/10 cực kỳ đặc sắc, lấy bối cảnh 100% tại Việt Nam.

QUY TẮC PHẢI TUÂN THỦ:
1. GIỚI THIỆU TRUYỆN (INTRO) HƯỚNG 1 (CỰC KỲ NGẮN & KỊCH TÍNH):
   - Phải bắt đầu bằng một câu thoại/trích dẫn sỉ nhục cực sốc in đậm bọc trong <p><strong>"..."</strong></p>.
   - Theo sau là đúng 2-3 đoạn văn ngắn (tổng cộng tối đa 120-150 từ, mỗi đoạn bọc trong <p>...</p>) giới thiệu mâu thuẫn khốc liệt và đòn lật kèo thâu tóm ngược, có nhắc đến nữ chính thông minh đồng hành.
   - Tuyệt đối không viết lan man dài dòng hay danh sách dài để tránh tràn khung màn hình điện thoại di động (mobile overflow).
2. DÀN Ý 10 CHƯƠNG:
   - Hãy thiết lập dàn ý chi tiết kịch tính cho đúng 10 chương."""

    user_prompt = """Hãy lập dàn ý 10 chương và giới thiệu truyện cực kịch tính ngắn gọn theo tiêu chuẩn hướng 1 cho tác phẩm:
- Tiêu đề: Bà Chủ Mỹ Phẩm Organic Đà Lạt: Bị Vu Oan Bán Hàng Giả, Tôi Thâu Tóm Cả Thị Trường
- Tác giả: Phan Ngọc Huyền
- Nam chính: Đặng Hoàng Nam, tiến sĩ hóa dược, chuyên gia chiết xuất thảo dược tự nhiên
- Nữ chính: Phan Ngọc Huyền, CEO startup mỹ phẩm organic bị đối thủ vu oan sản phẩm chứa chì
- Bối cảnh: Đà Lạt, vùng thảo dược Lạc Dương, nhà máy mỹ phẩm, Cục Quản lý Dược
- Xung đột chủ đạo: Tập đoàn mỹ phẩm ngoại quốc mua chuộc phòng kiểm nghiệm, giả mạo kết quả xét nghiệm chứa chì

Hãy xuất ra cấu trúc JSON nguyên bản tuyệt đối, không chứa ```json hay ```:
{
  "title": "Bà Chủ Mỹ Phẩm Organic Đà Lạt: Bị Vu Oan Bán Hàng Giả, Tôi Thâu Tóm Cả Thị Trường",
  "author": "Phan Ngọc Huyền",
  "genre": "Sảng Văn",
  "intro": "Mở đầu in đậm câu nói sỉ nhục, sau đó là 2 đoạn kịch tính cực ngắn bọc trong các thẻ <p>",
  "outlines": [
    { "chap_num": 1, "outline": "Tóm tắt mâu thuẫn khốc liệt chương 1..." },
    { "chap_num": 2, "outline": "Tóm tắt chương 2..." },
    ...
    { "chap_num": 10, "outline": "Tóm tắt chương 10..." }
  ]
}"""

    payload = {
        "model": "default",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 3000
    }
    
    print("Calling Qwen API...")
    start = time.time()
    try:
        res = requests.post(local_url, json=payload, timeout=240)
        print("Status Code:", res.status_code)
        print("Time elapsed:", time.time() - start)
        if res.status_code == 200:
            print("Success!")
            print(res.text[:1000])
        else:
            print("Error response:", res.text)
    except Exception as e:
        print("Exception:", e)

if __name__ == "__main__":
    test()

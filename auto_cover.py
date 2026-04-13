import requests
import time
import base64
import urllib.parse
import random

wp_url = "https://doctieuthuyet.com"

print("🔥 Bắt đầu kiểm tra và backfill ảnh đại diện...")

while True:
    # Lấy danh sách cần backfill
    try:
        res = requests.get(f"{wp_url}/wp-json/temply/v1/missing-covers", timeout=20).json()
    except Exception as e:
        print("Lỗi get missing covers: ", e)
        time.sleep(5)
        continue

    if res.get('status') == 'done' or not res.get('items'):
        print("🎉 TẤT CẢ POSTS/PAGES ĐỀU ĐÃ CÓ ẢNH ĐẠI DIỆN!")
        break
    
    items = res['items']
    print(f"👉 Tìm thấy {len(items)} trang/bài viêt thiếu ảnh. Bắt đầu generate và upload...")

    for item in items:
        title = item['title']
        post_id = item['id']
        ptype = item['type']
        
        # Tạo prompt cho chatgpt API / Pollinations
        if ptype == 'truyen':
            prompt = f"Vietnamese web novel book cover art, illustration, fantasy anime style, professional digital painting, title concept: {title} masterpiece"
        else:
            prompt = f"A simple, clean, minimalist flat vector illustration representing: {title} web design, corporate aesthetics, 8k"
        
        print(f"[{post_id}] Đang tạo ảnh: {title} ...")
        img_url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}?width=800&height=600&seed={random.randint(1,99999)}&nologo=true"
        
        # Download ảnh local (local không bị chặn)
        try:
            img_res = requests.get(img_url, timeout=30)
            if img_res.status_code == 429:
                print("⏳ Quá tải (429)! Chờ 15s rồi thử lại...")
                time.sleep(15)
                continue
            img_res.raise_for_status()
            img_b64 = base64.b64encode(img_res.content).decode('utf-8')
            time.sleep(3) # Tránh dính 429
        except Exception as e:
            print("Lỗi tải ảnh qua AI: ", e)
            time.sleep(5)
            continue
        
        # Upload ảnh lên WordPress qua API tự tạo
        print(f"[{post_id}] Đã sinh ảnh xong, đẩy lên server...")
        try:
            up_res = requests.post(f"{wp_url}/wp-json/temply/v1/upload-cover", data={
                'post_id': post_id,
                'image_b64': img_b64
            }, timeout=30).json()
            
            if up_res.get('status') == 'success':
                print(f"✅ Đã up xong ảnh đại diện cho ID {post_id}")
            else:
                print(f"❌ Lỗi Upload: {up_res}")
        except Exception as e:
            print("Lỗi Upload Server: ", e)
    
    # Nghỉ xíu tránh nghẽn
    time.sleep(1)

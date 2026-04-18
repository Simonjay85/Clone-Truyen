import os

files = [
    "src/components/MicroDramaView.tsx",
    "src/components/GeminiDramaView.tsx",
    "src/components/GrokDramaView.tsx",
    "src/components/ClaudeDramaView.tsx",
    "src/components/ComboEconomicView.tsx",
    "src/components/ComboRoyalView.tsx"
]

old_title_prompt = '"super_title": "Tên truyện cực ngầu (VD: Ma Tôn Truyền Kỳ, Đại Tỷ Hồi Sinh)"'
new_title_prompt = '"super_title": "Tự động sáng tạo 1 Tên Truyện duy nhất, chấn động, giật gân và hợp trend truyện mạng hiện nay. TUYỆT ĐỐI KHÔNG TRÙNG LẶP ĐUÔI VERSION."'

old_summary_prompt = '"summary": "Tóm tắt truyện (3 câu - Phải nhồi nhét hook chấn động, giật gân, tạo sự tò mò tột độ để thu hút độc giả click vào đọc)"'
new_summary_prompt = '"summary": "Tóm tắt truyện (Viết thật dài, miêu tả chi tiết sâu sắc nỗi đau/sự kịch tính, nhồi nhét liên tục các HOOK giật gân, đảm bảo người đọc liếc qua là máu dồn lên não lôi cuốn đọc ngay lập tức!)"'

old_auto_title = "title: (title || 'Truyện') + ` (Version ${idx+1})`"
new_auto_title = "title: pitchOptions[idx].super_title || `Truyện Chấn Động ${idx+1}`"

old_auto_title_2 = "title: pitchOptions[idx].super_title || (title || 'Truyện') + ` (Version ${idx+1})`"

for p in files:
    with open(p, "r") as f:
        c = f.read()
    
    c = c.replace(old_title_prompt, new_title_prompt)
    c = c.replace(old_summary_prompt, new_summary_prompt)
    
    c = c.replace(old_auto_title_2, new_auto_title)
    c = c.replace(old_auto_title, new_auto_title)
    
    with open(p, "w") as f:
        f.write(c)
    print("Updated", p)


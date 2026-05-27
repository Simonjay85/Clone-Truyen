#!/usr/bin/env python3
import json
import os
import sys
import random
import re

# Add scratch to path to import novel_editor
sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

RING_VARIATIONS = [
    "Cô tháo chiếc nhẫn đính hôn ra, dứt khoát đặt lên mặt bàn trơn láng. Tiếng kim loại va chạm với mặt gỗ vang lên một tiếng cạch khô khốc, báo hiệu sự đứt gãy không thể hàn gắn.",
    "Chiếc nhẫn đính hôn được cô rút ra rồi đặt lặng lẽ lên bậu cửa sổ, ánh kim loại mờ nhạt dần chìm vào bóng tối cuối chiều.",
    "Cô tháo chiếc nhẫn đính hôn ra, thả rơi tự do xuống mặt bàn gỗ lim. Tiếng kim loại vang lên dứt khoát, đặt dấu chấm hết hoàn toàn cho mối duyên sáu năm.",
    "Cô tháo chiếc nhẫn ra, nhẹ nhàng đặt lên tập tài liệu dự án liên doanh. Hành động lạnh lùng ấy dập tắt chút hy vọng cuối cùng của tình nghĩa xưa cũ."
]

CARD_VARIATIONS = [
    "thu hồi thẻ công tác nội bộ và khóa quyền truy cập hệ thống",
    "đình chỉ quyền truy cập tài khoản phòng Lab và thu hồi thẻ nhân viên",
    "khóa tài khoản quản trị máy chủ nội bộ và áp giải ra ngoài"
]

AUTHORITY_VARIATIONS = [
    "Đoàn thanh tra chuyên ngành liên kết với cơ quan Cục Cảnh sát điều tra",
    "Ban kiểm soát độc lập phối hợp với cơ quan thanh tra pháp chế",
    "Đoàn liên ngành điều tra kinh tế thuộc Bộ Công an"
]

BANK_VARIATIONS = [
    "hệ thống Techcombank",
    "tài khoản ngân hàng thương mại",
    "ngân hàng Techcombank chi nhánh Hà Nội"
]

def clean_cliches(text):
    # 1. Ring cliché replacement
    ring_pat = r"Phan Mỹ Hạnh rút chiếc nhẫn đính hôn bằng bạc trên ngón tay ra, ném thẳng vào mặt Phong không thương tiếc\. Chiếc nhẫn rơi xuống nền gạch, nảy lên mấy vòng rồi nằm im lìm trong góc tối\."
    if re.search(ring_pat, text):
        text = re.sub(ring_pat, random.choice(RING_VARIATIONS), text)
        
    # General ring cliché replacement for other names
    general_ring = r"rút chiếc nhẫn đính hôn.*?ném thẳng vào mặt.*?Chiếc nhẫn rơi xuống nền gạch, nảy lên mấy vòng rồi nằm im lìm trong góc tối\."
    text = re.sub(general_ring, random.choice(RING_VARIATIONS), text)

    # 2. License snapping replacement
    text = text.replace("bẻ gãy thẻ hành nghề", random.choice(CARD_VARIATIONS))
    text = text.replace("bẻ gãy thẻ nhân viên", random.choice(CARD_VARIATIONS))

    # 3. Bank and authority variety
    text = text.replace("C03 Bộ Công an", random.choice(AUTHORITY_VARIATIONS))
    text = text.replace("hệ thống Vietcombank", random.choice(BANK_VARIATIONS))
    text = text.replace("tài khoản Vietcombank", random.choice(BANK_VARIATIONS))

    return text

def main():
    json_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/recent_50_stories_detailed.json"
    if not os.path.exists(json_path):
        print("Error: detailed JSON not found")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        stories = json.load(f)

    print(f"Loaded {len(stories)} stories for bulk cliché cleaning.")
    
    # We will upload the helper
    print("Uploading novel_editor.php helper to production...")
    novel_editor.upload_helper()

    try:
        # We will loop through the top stories that are published and need cliché cleaning
        # Let's target the active recently published stories (ID 3954, 3930, 3920, 3873, etc. from our statistics)
        # To avoid making this script take too long, we will do a targeted cleaning of the 10 most recent published stories
        # where we found high frequencies of these clichés.
        target_stories = [3954, 3930, 3920, 3873, 3861, 3849, 3837, 3825, 3813, 3801]
        
        for sid in target_stories:
            print(f"\n--- Cleaning clichés for Story ID {sid} ---")
            res = novel_editor.get_story_chapters(sid)
            if not res.get("success"):
                print(f"❌ Failed to fetch chapters for Story ID {sid}: {res.get('error')}")
                continue

            chapters = res.get("chapters", [])
            print(f"Found {len(chapters)} chapters to review.")

            for idx, ch in enumerate(chapters):
                ch_id = ch["id"]
                title = ch["title"]
                content = ch["content"]

                # Clean content
                cleaned_content = clean_cliches(content)

                if cleaned_content != content:
                    print(f"   ✓ Clichés detected and cleaned in Chapter {idx+1}: {title} (ID: {ch_id})")
                    # Update
                    upd_res = novel_editor.update_chapter(ch_id, title, cleaned_content)
                    if upd_res.get("success"):
                        print(f"     ✅ Success! Updated on production.")
                    else:
                        print(f"     ❌ Error updating: {upd_res.get('error')}")
                else:
                    print(f"   - No clichés found in Chapter {idx+1}")

        print("\n✓ Bulk cliché cleaning completed successfully for target stories!")

    finally:
        print("Cleaning up production helper...")
        novel_editor.remove_helper()
        print("✓ Operations finished.")

if __name__ == "__main__":
    main()

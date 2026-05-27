#!/usr/bin/env python3
import json
import os
import subprocess

def main():
    print("🚀 UPDATING STORY 3940 INTRODUCTION WITH PUNCHY HOOK...")
    
    new_intro_html = (
        '<p><strong>"Đôi bàn tay bốc thuốc Nam rách rưới của anh không đáng chạm vào chiếc váy cưới trăm triệu của tôi! Loại lang băm nghèo hèn như anh chỉ làm cản trở tôi bước chân vào giới thượng lưu!"</strong></p>\n'
        '<p>Vị hôn thê Phan Mỹ Hạnh lạnh lùng tháo nhẫn đính hôn ném thẳng vào mặt Vũ Hoài Lâm, ngay khi anh bị người thầy kính yêu vu oan và tống cổ khỏi Viện Phổi Quốc tế dưới đêm mưa giông Hà Nội. Chúng cướp đoạt công trình phế nang đột phá của anh để dâng cho tập đoàn NexaCorp hòng tiến tới thương vụ tỷ đô.</p>\n'
        '<p>Nhưng chúng không ngờ, Đông y dưới tay Lâm không phải là lá cây rác rưởi, mà là thần dược tối cao! Được Trịnh Khánh Vy - nữ tổng tài kiêu sa của Vạn An Capital chống lưng, Lâm châm cứu "Cửu Châm Đoạt Mệnh" kéo siêu tỷ phú từ cõi chết trở về, dùng nhật ký commit Git gốc, kiểm toán Big 4 EY và lệnh bắt từ C03 Bộ Công an để nghiền nát tất cả những kẻ phản bội.</p>\n'
        '<p><strong>Bọn họ từng gọi anh là kẻ lang băm đê tiện, cho đến khi cả Hội thảo Y khoa Quốc tế phải run rẩy quỳ sụp dưới chân anh để cầu xin một cơ hội sống!</strong></p>'
    )
    
    # 1. Update scratch/story_3940_deploy_ready.json
    json_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/story_3940_deploy_ready.json"
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        data["intro"] = new_intro_html
        
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✓ Updated intro in {json_path}")
    else:
        print(f"❌ Error: {json_path} not found!")
        return

    # 2. Update existing_novels.json
    registry_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
    if os.path.exists(registry_path):
        with open(registry_path, "r", encoding="utf-8") as f:
            novels = json.load(f)
            
        updated = False
        for novel in novels:
            if novel.get("id") == 3940:
                novel["intro"] = new_intro_html
                updated = True
                break
                
        if updated:
            with open(registry_path, "w", encoding="utf-8") as f:
                json.dump(novels, f, indent=4, ensure_ascii=False)
            print(f"✓ Updated intro in {registry_path}")
        else:
            print("❌ Warning: Story 3940 not found in registry!")
    else:
        print(f"❌ Warning: {registry_path} not found!")

    # 3. Deploy live using the deployment script
    print("Sending deployment command to WordPress...")
    deploy_script = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/deploy_v13_story.py"
    cmd = ["python3", deploy_script, json_path]
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(res.stdout)
        print("🎉 LIVE UPDATE COMPLETED SUCCESSFULLY!")
    except subprocess.CalledProcessError as e:
        print("❌ Deployment command failed!")
        print(e.stdout)
        print(e.stderr)

if __name__ == "__main__":
    main()

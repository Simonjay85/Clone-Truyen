import os
import json
import time
import requests
import sys
from ftplib import FTP

FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"
STORY_ID = 3633

def deploy():
    json_path = "scratch/rewrite_3633_v13.json"
    print(f"📖 Starting deployment from local JSON: {json_path}")
    if not os.path.exists(json_path):
        print(f"❌ JSON file does not exist: {json_path}")
        return False
        
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            story_json = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load/parse JSON file: {e}")
        return False
        
    story_id = story_json.get("story_id", STORY_ID)
    title = story_json.get("title")
    intro = story_json.get("intro")
    chapters = story_json.get("chapters")
    
    if not story_id or not title or not intro or not chapters:
        print(f"❌ Story JSON is missing required fields (story_id, title, intro, chapters)")
        return False
        
    print(f"✓ Story loaded: ID={story_id}, Title='{title}'")
    print(f"✓ Total chapters: {len(chapters)}")
    
    # Enrich fields according to V13 standards
    seo = {
        "focus_keyword": "trà sen Tây Hồ",
        "seo_title": "Trà Sen Tây Hồ Bách Diệp Cổ Truyền Quảng An: Nghệ Nhân Phục Hận",
        "seo_description": "Hành trình giữ gìn trà sen Tây Hồ Bách Diệp Quảng An cổ truyền của nghệ nhân trà trẻ tuổi Duy Anh trước âm mưu cướp đầm của trà công nghiệp Hoài Nam. Đầy kịch tính!"
    }
    
    genres = ['Sảng Văn', 'Ẩm Thực', 'Đô thị vả mặt', 'Vả Mặt', 'Đô thị thương chiến', 'Hào Môn']
    
    comments = [
        {
            "comment_author": "Phan Văn Minh",
            "comment_content": "Không ngờ phân tích GC-MS lại vạch trần được chiêu trò bẩn thỉu của Lê Hoài Nam nhanh như vậy! Trà sen Tây Hồ Bách Diệp chuẩn cổ truyền vẫn luôn là đẳng cấp khác biệt!"
        },
        {
            "comment_author": "Lâm Hoài Thu",
            "comment_content": "Nữ chính Lâm Khánh Chi đỉnh thật sự, đàm phán 100 tỷ lấy 30% sòng phẳng, đúng chất CFO của Vạn An Capital chứ không phải kiểu cứu giúp não tàn vô điều kiện."
        },
        {
            "comment_author": "Trần Anh Tuấn",
            "comment_content": "C03 vào cuộc xử lý Lê Hoài Nam cùng bè lũ thanh tra Trần Văn Bản là hoàn toàn chính xác. Pháp luật nghiêm minh!"
        },
        {
            "comment_author": "Bác Sĩ Hoàng Hải",
            "comment_content": "Bài thuốc Liên Diệp Cam Thảo và bấm huyệt Nội Quan, Nhân Trung trong cấp cứu cơn hen của ngài Pierre Laurent được miêu tả rất khoa học và thực tế. Truyện viết chắc tay quá!"
        }
    ]
    
    alt_text = "Nghệ nhân trà sen Tây Hồ Bách Diệp cổ truyền Quảng An Hà Nội"
    
    # 1. Connect FTP and upload update_story_sen.php
    print("Connecting to FTP (timeout=30)...")
    try:
        ftp = FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        print("✓ Connected to FTP. Uploading update_story_sen.php...")
        
        # Read the update_story_sen.php helper
        helper_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/update_story_sen.php"
        with open(helper_path, "rb") as f:
            ftp.storbinary("STOR update_story_sen.php", f)
        print("✓ update_story_sen.php uploaded successfully.")
        ftp.quit()
    except Exception as e:
        print(f"❌ FTP upload error: {e}")
        return False
        
    # 2. Call the deploy API
    print("Gửi request POST tới WordPress để cập nhật truyện (timeout=120)...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "story_id": story_id,
        "title": title,
        "intro": intro,
        "chapters": chapters,
        "seo": seo,
        "genres": genres,
        "comments": comments,
        "alt_text": alt_text
    }
    
    deploy_success = False
    try:
        api_url = f"{WP_URL}/update_story_sen.php"
        # Disable SSL check warning if using verify=False
        res = requests.post(api_url, json=payload, verify=False, timeout=120)
        print(f"WordPress Response Status: {res.status_code}")
        
        try:
            res_data = res.json()
            if res_data.get("success"):
                print(f"🎉 SUCCESS: Published Sen Tea Story ID {story_id} to live website!")
                print(f"   Deleted Chapters: {res_data.get('deleted_chapters_count')}")
                print(f"   New Chapters: {res_data.get('chapters_count')}")
                print(f"   Seeded Comments: {res_data.get('comments_seeded')}")
                print(f"   Alt Text Updated: {res_data.get('thumb_alt_updated')}")
                deploy_success = True
            else:
                print(f"❌ WordPress API error: {res_data}")
        except Exception as e:
            print(f"❌ WordPress returned invalid JSON: {res.text[:1000]}")
    except Exception as e:
        print(f"❌ API connection or execution failed: {e}")
        
    # 3. Always clean up FTP
    print("Reconnecting to FTP to clean up update_story_sen.php...")
    try:
        ftp = FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.delete("update_story_sen.php")
        print("✓ Successfully deleted update_story_sen.php from server.")
        ftp.quit()
    except Exception as e:
        print(f"⚠️ Clean up FTP helper error: {e}")
        
    return deploy_success

if __name__ == "__main__":
    success = deploy()
    if success:
        print("🚀 SEN TEA NOVEL DEPLOYMENT COMPLETED WITH SUCCESS!")
        sys.exit(0)
    else:
        print("❌ DEPLOYMENT FAILED.")
        sys.exit(1)

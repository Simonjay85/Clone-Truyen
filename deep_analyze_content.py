import json
import re
import os

def run():
    json_path = "recent_50_stories_detailed.json"
    if not os.path.exists(json_path):
        print("Detailed stories JSON not found!")
        return
        
    with open(json_path, "r", encoding="utf-8") as f:
        stories = json.load(f)
        
    print(f"Loaded {len(stories)} stories for deep content analysis.")
    
    analysis = []
    
    # Helper lists to detect duplicates
    all_protagonists = []
    all_love_interests = []
    all_antagonists = []
    all_companies = []
    all_settings = []
    
    for s in stories:
        content = s.get("first_chap_excerpt", "") + " " + s.get("synopsis", "") + " " + s.get("title", "")
        
        # Simple heuristic to extract potential names (Capitalized Vietnamese names)
        # Match sequences like "Lâm Tuấn Kiệt", "Trần Hoài Nam", "Nguyễn Khánh An"
        name_patterns = re.findall(r'\b[A-ZĐ][a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ][a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]*\s+[A-ZĐ][a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]*\s+[A-ZĐ][a-zàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]*\b', content)
        
        # Clean extracted names from noise (like "Metropole Hà Nội", "Thành phố Hồ Chi Minh", "Cộng hòa Xã hội")
        noise = ["Thành phố Hồ", "Phú Mỹ Hưng", "Metropole Hà", "Quỹ Vạn An", "Landmark 81", "Bệnh viện đa", "Cục Cảnh sát", "Đại học Quốc", "Sở Kế hoạch", "Sở Thông tin", "Cộng hòa Xã", "Việt Nam Cực", "Chopin Competition", "Vạn An Corp", "Tân Cảng Sài", "Tập đoàn Bảo", "Tập đoàn Hóa", "Công ty Cổ", "Bệnh viện Pháp"]
        clean_names = []
        for name in name_patterns:
            is_noise = False
            for n in noise:
                if n in name:
                    is_noise = True
                    break
            if not is_noise and name not in clean_names:
                clean_names.append(name)
                
        # Classify the setting
        setting = "Đô thị (Chung)"
        if "Hà Nội" in content or "Hồ Tây" in content or "Tây Hồ" in content or "Ba Vì" in content or "Đông Anh" in content:
            setting = "Hà Nội"
        elif "Sài Gòn" in content or "TP.HCM" in content or "Thảo Điền" in content or "Bitexco" in content or "Cần Giờ" in content or "Gò Vấp" in content:
            setting = "Sài Gòn / TP.HCM"
        elif "Phú Quốc" in content:
            setting = "Phú Quốc"
        elif "Miền Tây" in content or "Bến Tre" in content or "Đồng Tháp" in content:
            setting = "Miền Tây"
        elif "Bình Dương" in content:
            setting = "Bình Dương"
        elif "Đà Lạt" in content:
            setting = "Đà Lạt"
        elif "Hải Phòng" in content or "Đình Vũ" in content:
            setting = "Hải Phòng"
        elif "Đà Nẵng" in content or "Tân Cảng" in content or "Tiên Sa" in content:
            setting = "Đà Nẵng"
            
        # Classify main theme/trope
        theme = "Ẩn danh / Giả nghèo"
        if "Trà" in s['title'] or "Chè" in s['title']:
            theme = "Trà / Chè"
        elif "Y" in s['title'] or "Bác Sĩ" in s['title'] or "Vắc Xin" in s['title']:
            theme = "Y học / Dược phẩm"
        elif "Cacao" in s['title'] or "Socola" in s['title'] or "Bánh Mì" in s['title'] or "Nấu Ăn" in s['title'] or "Ẩm Thực" in s['title'] or "Sầu Riêng" in s['title'] or "Tôm Hùm" in s['title']:
            theme = "Nông nghiệp / Ẩm thực"
        elif "Sơn Mài" in s['title'] or "Gốm Sứ" in s['title'] or "Tranh" in s['title'] or "Họa Sĩ" in s['title']:
            theme = "Nghệ thuật / Thủ công mỹ nghệ"
        elif "Blockchain" in s['title'] or "Fintech" in s['title'] or "Lập Trình" in s['title'] or "Mã Nguồn" in s['title']:
            theme = "Công nghệ / Tài chính số"
        elif "Đất" in s['title'] or "Bất Động Sản" in s['title'] or "Resort" in s['title'] or "Đảo" in s['title'] or "Tòa Nhà" in s['title'] or "Biệt Thự" in s['title']:
            theme = "Bất động sản / Resort"
        elif "Võ Thần" in s['title'] or "Vệ Sĩ" in s['title'] or "Bảo Vệ" in s['title'] or "Đặc Nhiệm" in s['title']:
            theme = "Chiến thần / Bảo vệ ẩn thân"
            
        analysis.append({
            'id': s['id'],
            'title': s['title'],
            'date': s['date'],
            'chapters': s['chapters_count'],
            'setting': setting,
            'theme': theme,
            'extracted_names': clean_names
        })
        
        all_settings.append(setting)
        
    # Analyze distributions
    from collections import Counter
    setting_counts = Counter(all_settings)
    theme_counts = Counter([s['theme'] for s in analysis])
    
    # Save the output
    with open("plot_analysis_results.json", "w", encoding="utf-8") as out:
        json.dump({
            'setting_distribution': dict(setting_counts),
            'theme_distribution': dict(theme_counts),
            'stories': analysis
        }, out, ensure_ascii=False, indent=2)
        
    print("\n=== BÁO CÁO THỐNG KÊ PLOT ===")
    print("\n1. Phân bố bối cảnh địa lý:")
    for k, v in setting_counts.items():
        print(f"  - {k}: {v} truyện")
        
    print("\n2. Phân bố chủ đề / Trope cốt truyện:")
    for k, v in theme_counts.items():
        print(f"  - {k}: {v} truyện")
        
if __name__ == "__main__":
    run()

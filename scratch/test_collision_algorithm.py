import json
import os
import re
import random

# Datasets definition
PROTAGONISTS = [
    "Lê Quốc Khánh", "Đặng Thái Sơn", "Vũ Hoài Lâm", "Cao Tiến Dũng",
    "Bùi Lạc Phong", "Phùng Nhất Huy", "Trương Minh Triết", "Đỗ Trọng Nhân",
    "Tô Hoài Nam", "Đặng Thế Dân", "Phan Chí Trung", "Nguyễn Lâm Bách",
    "Võ Hoàng Minh", "Trịnh Gia Bảo", "Phạm Tuấn Kiệt", "Lâm Quốc Việt",
    "Nguyễn Đăng Khoa", "Lê Thanh Tùng", "Trần Đình Khang", "Vũ Nhật Anh",
    "Đặng Văn Lâm", "Hoàng Thế Anh", "Phùng Xuân Đông", "Tống Khánh Duy",
    "Bùi Thế Vinh", "Cao Thiên Lạc", "Lê Khắc Nam", "Trần Thế Hải",
    "Nguyễn Tấn Đạt", "Phạm Tuấn Anh", "Hoàng Việt", "Nguyễn Đức Trí",
    "Trịnh Gia Huy", "Nguyễn Hoàng Minh", "Lê Gia Bách", "Nguyễn Hải Long",
    "Trần Minh Hoàng", "Lê Quang Minh", "Hoàng Văn Nam", "Lâm Thế Khải"
]

FEMALE_LEADS = [
    "Nguyễn Hoàng Mai Chi", "Đỗ Thục Đoan", "Trịnh Khánh Quỳnh", "Phạm Nhã Phương",
    "Lê Cát Tiên", "Vũ Khánh An", "Trần Ngọc Diệp", "Đặng Mỹ Dung",
    "Cao Hoài An", "Bùi Phương Thảo", "Trịnh Hoàng Yến", "Nguyễn Minh Thư",
    "Lê Minh Thư", "Nguyễn Khánh Vy", "Trần Mỹ Duyên", "Lê Minh An",
    "Nguyễn Minh Tuyền", "Lâm Gia Hân", "Lâm Vy", "Trần Diệu Nhi",
    "Ngô Thị Hương", "Lê Mai Chi", "Trần Thanh Mai", "Lâm Vy Anh",
    "Phạm Quỳnh Chi", "Đặng Thu Thảo", "Hoàng Bảo Trâm", "Vũ Phương Trinh"
]

VILLAINS = [
    "Tạ Đình Phong", "Hứa Gia Ấn", "Phan Thanh Bình", "Lê Hữu Phước",
    "Hoàng Thế Vinh", "Trần Vĩnh Thịnh", "Đỗ Quốc Oai", "Trương Vô Kỵ",
    "Cao Hữu Hoài", "Lâm Vĩnh Nghiệp", "Lý Bách", "Nguyễn Hữu Hoài",
    "Trần Khánh Vy", "Đỗ Văn Thắng", "Phạm Gia Bảo", "Lý Bách Hoài",
    "Hoàng Kim Định", "Phạm Gia Hưng", "Vũ Hoài Nam", "Nguyễn Văn Hải",
    "Trần Quốc Thắng", "Tạ Minh Tuấn", "Vũ Minh Quân"
]

GOOD_COMPANIES = [
    "Quỹ Khởi Nguyên", "Siêu quỹ Thái Bình", "Tập đoàn Tràng An", "LogiVina",
    "Dược phẩm Bách Thảo", "Nông sản Cát Tường", "Công nghệ VinaBlock",
    "Quỹ Vạn Lộc", "Quỹ Vạn An", "Vạn An Corp", "Tập đoàn Thép Đông Hải",
    "Đế chế Bách Nghệ", "Dược Thảo Ngọc Linh", "Bảo Long Tea", "LogiChain",
    "Công nghệ PayBlock", "Đại Việt Logistics", "Năng lượng Xanh Việt"
]

EVIL_COMPANIES = [
    "Tập đoàn Thịnh Phát", "Tập đoàn Đông Á", "SouthernRealty", "PrimeTech",
    "AgroChem Việt Nam", "CyberShield", "Royal Sip", "Tập đoàn Bán lẻ Hoàng Gia",
    "Dược phẩm Vạn Xuân", "Thương mại Tín Nghĩa", "Bất động sản Đất Vàng"
]

SETTINGS = [
    "Hà Nội",
    "Sài Gòn / TP.HCM",
    "Phú Quốc",
    "Miền Tây",
    "Hải Phòng",
    "Đà Lạt",
    "Đà Nẵng",
    "Nha Trang / Khánh Hòa",
    "Tây Nguyên"
]

NARRATIVE_DISRUPTORS = [
    "Sự cố sập hệ thống máy chủ và tấn công DDoS quy mô lớn từ Thụy Sĩ gây gián đoạn dịch vụ toàn quốc, làm suy giảm nghiêm trọng uy tín dự án mới.",
    "Sự phản bội và bán đứng mã nguồn/bí mật kinh doanh từ người cộng sự thân tín nhất thuở lập nghiệp.",
    "Thay đổi đột ngột về chính sách hải quan xuất khẩu và các rào cản thuế quan phi kỹ thuật của thị trường châu Âu gây tắc nghẽn toàn bộ lô hàng đầu tiên.",
    "Khủng hoảng thanh khoản liên hoàn và đợt rút tiền hàng loạt (bank run) đột biến do tin đồn phá sản giả mạo lan truyền trên báo chí.",
    "Phản diện mua chuộc KOL bẩn và sử dụng công nghệ deepfake tinh vi để dựng scandal thực phẩm nhiễm độc hoặc ô nhiễm môi trường trên mạng xã hội."
]

def load_existing_novels():
    if os.path.exists("existing_novels.json"):
        with open("existing_novels.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def get_used_text(existing_novels):
    used_text = ""
    for novel in existing_novels:
        used_text += " " + novel.get("title", "")
        used_text += " " + novel.get("intro", "")
    return used_text

def select_unique_name(name_list, used_text, category_name="Entity"):
    valid_names = []
    for name in name_list:
        # Check full name
        full_collision = name.lower() in used_text.lower()
        
        # Check middle + first name (e.g. "Quốc Khánh" from "Lê Quốc Khánh")
        parts = name.split()
        mid_first_collision = False
        if len(parts) >= 2:
            mid_first = " ".join(parts[1:]).lower()
            mid_first_collision = mid_first in used_text.lower()
            
        if not full_collision and not mid_first_collision:
            valid_names.append(name)
            
    if valid_names:
        chosen = random.choice(valid_names)
        print(f"✓ Selected unique {category_name}: {chosen} (Out of {len(valid_names)} valid options from {len(name_list)})")
        return chosen
    else:
        chosen = random.choice(name_list)
        print(f"⚠️ No valid unique {category_name} found! Fallback to random: {chosen}")
        return chosen

def rotate_setting(existing_novels):
    setting_freq = {s: 0 for s in SETTINGS}
    
    used_text = ""
    for novel in existing_novels:
        used_text += " " + novel.get("title", "")
        used_text += " " + novel.get("intro", "")
        
    for s in SETTINGS:
        keyword = s.split("/")[0].strip() # Take the primary city name
        setting_freq[s] = used_text.count(keyword)
        
    sorted_settings = sorted(setting_freq.items(), key=lambda x: x[1])
    
    print("\nGeographical settings usage frequency:")
    for s, freq in sorted_settings:
        print(f"  - {s}: {freq} matches")
        
    min_freq = sorted_settings[0][1]
    least_used = [s for s, freq in sorted_settings if freq == min_freq]
    chosen = random.choice(least_used)
    
    print(f"\n✓ Rotated geographical setting: {chosen} (Min frequency is {min_freq})")
    return chosen

def main():
    print("=" * 60)
    print("🧪 TESTING IMPROVED NAME ANTI-COLLISION & ROTATION ALGORITHMS")
    print("=" * 60)
    
    novels = load_existing_novels()
    print(f"Loaded {len(novels)} existing novels.")
    
    used_text = get_used_text(novels)
    print(f"Compiled {len(used_text)} characters of text for exact substring matching.\n")
    
    # Select unique names
    protagonist = select_unique_name(PROTAGONISTS, used_text, "Protagonist")
    helper = select_unique_name(FEMALE_LEADS, used_text, "Female Helper")
    villain = select_unique_name(VILLAINS, used_text, "Villain")
    good_company = select_unique_name(GOOD_COMPANIES, used_text, "Good Company")
    evil_company = select_unique_name(EVIL_COMPANIES, used_text, "Evil Company")
    
    # Rotate setting
    setting = rotate_setting(novels)
    
    # Choose dynamic twist
    twist = random.choice(NARRATIVE_DISRUPTORS)
    print(f"\n✓ Selected dynamic Chapter 4 twist: {twist}")
    print("=" * 60)

if __name__ == "__main__":
    main()

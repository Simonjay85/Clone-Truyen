# MASTER COVER PROMPT — doctieuthuyet.com
# Chuẩn thiết kế ảnh bìa cho toàn bộ truyện trên hệ thống
# Cập nhật mới nhất: Phong cách Ảnh thật Điện ảnh Kịch tính (Cinematic Photorealism)
# Cập nhật: 2026-05-23

> [!IMPORTANT]
> **CHỈ DÙNG CHATGPT IMAGE GENERATION CHO HÌNH ẢNH MỚI**
> - Cover mới phải được tạo bằng ChatGPT Image Generation hoặc lấy từ file local đã được duyệt.
> - Tuyệt đối không gọi API sinh ảnh bên thứ ba trong script/pipeline.
> - Ảnh sau khi tạo phải được lưu local, kiểm tra preview, rồi upload/gắn featured image bằng workflow cover của repo.

---

## PHẦN 1 — AI IMAGE GENERATION PROMPT (ChatGPT Image Generation)

Để giữ chân người đọc ngay lập tức, toàn bộ hệ thống chuyển sang **phong cách ảnh chụp thật siêu thực, kịch tính cao (Cinematic Photorealistic Drama)**.
❌ KHÔNG dùng phong cách vẽ tay anime, hoạt hình hay minh họa màu nước.
✅ BẮT BUỘC dùng phong cách poster phim truyền hình Việt Nam chất lượng cao, tràn ngập cảm xúc, bi kịch và đòn phản kích.

### Template chuẩn:

```text
Square format, ultra-realistic cinematic real-life photo, high-stakes intense Vietnamese drama movie scene, photorealistic characters, realistic human skin and clothing textures, award-winning dramatic high-contrast lighting, 8k resolution,
[DRAMATIC_SCENE_AND_CONFLICT],
[CHARACTER_DESCRIPTION],
[BACKGROUND_SCENE],
dark at the TOP 30% of image for premium text overlay readability,
no text, no letters, no watermarks, no logos, no chapter numbers, no badges, no frames, no borders.
Square 1:1 composition.
```

### [DRAMATIC_SCENE_AND_CONFLICT] - Công thức kịch tính sảng văn:
*Bí quyết: Phải thể hiện sự đối lập tuyệt đối giữa kẻ chiến thắng kiêu hãnh (giàu sang, điềm tĩnh) và kẻ thua cuộc hối hận (quỳ gối, khóc lóc, cầu xin).*
- **Thần y trả thù**: `a peak drama revenge scene: an elegant wealthy man getting into a premium black limousine while his crying ex-wife in a beautiful designer dress is pleading on her knees in the rain, holding a medical report in her hand, looking up with deep despair and regret.`
- **CEO nghèo giả dạng**: `a powerful corporate confrontation: a stunning wealthy female CEO pointing accusingly at a corrupt executive who is sweating profusely, dropping his folders, while a handsome confident young man in casual clothes looks on with a calm knowing smile.`
- **Thợ xây đổi đời**: `an epic triumph: a strong handsome young Vietnamese engineer in a sleek custom suit standing on top of a luxury penthouse overlooking a construction site at sunset, while his former arrogant boss is forced to bow down and present a gold-trimmed deed contract.`
- **Dịch vụ/Logistics**: `a high-society dispute: a young Vietnamese captain in a clean white uniform stepping onto a luxury yacht, while an arrogant rich playboy is being escorted off by security guards under the neon lights of the port.`

### [CHARACTER_DESCRIPTION] theo nhân vật:
- **1 nam chính**: `a handsome, confident 30-year-old Vietnamese man, determined sharp expression, dressed in premium tailored suits or smart casual clothing.`
- **Nữ chính**: `a stunningly beautiful, sophisticated Vietnamese female executive or CFO, wearing an elegant business blazer or modern designer dress, highly intelligent and sharp look.`
- **Nhân vật phụ phản diện**: `an arrogant wealthy playboy or corrupt official, sweating, panic-stricken, kneeling in regret or bowing down.`

### [BACKGROUND_SCENE] theo bối cảnh Việt Nam thực tế:
- `a dark rain-slicked city street in Saigon with beautiful ambient neon reflections.`
- `Ho Chi Minh City skyline with the glowing Landmark 81 seen through a luxury penthouse glass window at golden hour.`
- `a high-end corporate boardroom in Hanoi with modern mahogany tables and glass walls overlooking the city lights at dusk.`
- `a bustling construction site in Binh Duong at sunset with giant scaffolding and a towering orange gantry crane.`

---

## PHẦN 2 — IMAGE OVERLAY RULES (Áp dụng sau khi có ảnh AI)

Hệ thống sử dụng **Layout Card Tràn Viền Hiện Đại (Modern Card Full-Bleed Layout)** giống như các nền tảng TikTok và Fanqie để tạo ấn tượng tối thượng.

### Kích thước chuẩn:
- Canvas: **2000 x 2000 px** (square, 1:1)
- Định dạng xuất: **PNG** (chất lượng cao)
- **Không có bất kỳ viền mạ vàng hay khung bao quanh nào** (Full bleed).
- **Không có nhãn dán cứng hay hộp đen/nâu ở đáy**.

### Lớp tối phía trên (Top & Bottom Dark Gradient Overlay) — BẮT BUỘC:
- **Top gradient**: Đen từ RGBA `(0,0,0,200)` tại `y=0` → `(0,0,0,0)` tại `y=750`.
- **Bottom gradient**: Đen từ RGBA `(0,0,0,80)` tại `y=2000` → `(0,0,0,0)` tại `y=1700` (giúp giữ thăng bằng bố cục và làm mờ các chi tiết thừa ở đáy).

### TITLE TEXT (Tiêu đề chính) - Bản đồ 3 Dòng Khối Màu:
- **Font**: Arial Bold (Chữ đậm không chân, sắc lẹm).
- **Cỡ chữ**: Khởi tạo từ **145px**, tự động giảm xuống tối thiểu 100px để vừa vặn trong chiều rộng 1850px.
- **Sắp xếp dòng và màu chữ**:
  - Dòng 1: **TRẮNG** `(255, 255, 255, 255)`
  - Dòng 2: **ĐỎ** `(255, 40, 60, 255)` (hoặc Vàng nếu chỉ có 2 dòng)
  - Dòng 3: **VÀNG** `(255, 210, 0, 255)`
- **Stroke đen viền chữ**: `width=12px`, `fill=(0,0,0,255)`.
- **Shadow layer**: Đổ bóng đen nhòe `GaussianBlur(radius=8)` cách gốc 6px ngang, 10px dọc nằm phía sau chữ chính giúp nổi bật trên mọi hậu cảnh phức tạp.
- **Vị trí Y bắt đầu**: `y = 120px` (Căn giữa ngang hoàn toàn).
- **Case**: Luôn in HOA toàn bộ (.upper()).
- **Line spacing**: `font_size * 1.15`.

### SUBTITLE TEXT (Phụ đề):
- **Font**: Arial Bold, **42px**.
- **Màu chữ**: Trắng mờ `(255, 255, 255, 220)` kèm stroke đen 3px.
- **Vị trí Y**: Bắt đầu sau dòng tiêu đề cuối cùng + **30px** (giữa màn hình).

### TUYỆT ĐỐI KHÔNG VẼ VÀO COVER FILE:
- ❌ **Biểu tượng con mắt và số lượt xem (👁 84.6K)**.
- ❌ **Biểu tượng đồng hồ và thời gian cập nhật (🕒 2 giờ trước)**.
- ❌ **Hộp chương số (Ch.5 badge)**.
*Giải thích: Đây là những tính năng động được render trực tiếp bởi theme WordPress của doctieuthuyet.com. Vẽ sẵn vào hình sẽ gây lỗi giao diện chồng chéo.*

---

## PHẦN 3 — QUY TRÌNH SINH BÌA SIÊU KỊCH TÍNH

```
Bước 1: Chọn đề tài sảng văn & Phân tích xung đột đỉnh điểm của câu chuyện.
Bước 2: Xây dựng Prompt tiếng Anh theo mẫu PHẦN 1. Nhấn mạnh "ultra-realistic cinematic real-life photo" và các chi tiết tương phản vật lý khóc/quỳ.
Bước 3: Gọi tool generate_image để vẽ ảnh nền 2000x2000.
Bước 4: Chạy script cover_overlay_standard.py để tự động chia 3 dòng và áp màu khối Trắng-Đỏ-Vàng cùng đổ bóng mờ lên ảnh.
Bước 5: Sideload bìa chất lượng cao qua FTP lên WordPress.
```

# MASTER COVER PROMPT — doctieuthuyet.com
# Chuẩn thiết kế ảnh bìa cho toàn bộ truyện trên hệ thống
# Phân tích từ 8 bìa mẫu: 2207, 2217, 2238, 2249, 2052, 2190, 2259, 2269, 2279, 2289
# Cập nhật: 2026-05-22

---

## PHẦN 1 — AI IMAGE GENERATION PROMPT (Pollinations/Flux)

### Template chuẩn:

Square format Vietnamese web novel book cover illustration, realistic live-action cinematic movie poster style, high-budget Vietnamese drama film look, dramatic lighting, high detail, masterpiece, 8k resolution, photorealistic characters,
[VISUAL_DIRECTION],
[CHARACTER_DESCRIPTION],
[BACKGROUND_SCENE],
dark at the TOP 30% of image for text overlay readability,
elegant cinematic lighting, rich color grading, high detail,
no text, no letters, no watermarks, no logos, no chapter numbers, no badges.
Square 1:1 composition.
```

### [VISUAL_DIRECTION] theo thể loại:
- CEO/Doanh nhân:      `luxury corporate drama, modern glass skyscraper interior, warm golden hour`
- Ẩm thực:             `gourmet restaurant or traditional kitchen, Vietnamese food, warm lantern glow`
- Cảng/Logistics:      `dramatic port scene, container ships, golden sunset over the sea`
- Bất động sản:        `premium penthouse, city skyline at night, sophisticated lighting`
- Dệt may/Công nghiệp: `modern factory floor, industrial machinery, twilight atmosphere`
- Y tế/Đông y:         `traditional medicine clinic, Chinese quarter atmosphere, evening lights`
- Chứng khoán:         `stock trading room, multiple monitors with candlestick charts, night city`
- Nghệ thuật/Vũ công:  `grand opera house interior, stage spotlights, golden baroque decor`
- Cà phê/Nông nghiệp:  `highland coffee plantation, red volcanic soil, misty mountains`
- Thời trang:          `fashion week runway, dramatic lighting, mannequins, vibrant dress`
- Mật vụ/Hành động:    `tense intelligence scene, tactical gear, urban night backdrop`
- Công nghệ/Startup:   `modern tech office, holographic UI displays, neon city lights`
- Xây dựng/Thợ hồ:    `major Vietnamese construction site, luxury high-rise building under construction, scaffolding at sunset, hard hat and blueprints`

### [CHARACTER_DESCRIPTION] theo nhân vật:
- 1 nam chính:   `a handsome confident Vietnamese man in [nghề nghiệp trang phục], determined expression`
- 2 nhân vật:    `a handsome Vietnamese man and an elegant Vietnamese woman, [context], standing together`
- Nam CEO:       `a tall handsome Vietnamese CEO in navy blue 3-piece suit, commanding presence`
- Nữ chính:      `a beautiful elegant Vietnamese woman in [áo dài / business suit / chef uniform]`
- Thợ/Kỹ thuật: `a skilled Vietnamese construction worker with hard hat, strong confident build, professional gear`

### [BACKGROUND_SCENE] theo bối cảnh:
- `Da Nang Tien Sa port with massive container ships, golden sunset`
- `Hoi An ancient town lanterns and Thu Bon river at night`
- `Ho Chi Minh City skyline seen through penthouse floor-to-ceiling windows at golden hour`
- `Binh Duong industrial zone VSIP, factory buildings at dusk`
- `Dak Lak highland coffee plantation with red volcanic soil and mountain mist`
- `Hanoi stock exchange trading floor with multiple screens showing green and red charts`
- `Vietnam Fashion Week runway stage with bright spotlights`
- `Luxury construction site in Binh Duong, towering crane and concrete skeleton building`

---

## PHẦN 2 — IMAGE OVERLAY RULES (Áp dụng sau khi có ảnh AI)

### Kích thước chuẩn:
- Canvas: **2000 x 2000 px** (square, 1:1)
- Định dạng xuất: **PNG** (chất lượng cao)

### Lớp tối phía trên (Top Dark Gradient Overlay) — BẮT BUỘC:
- Gradient màu đen từ RGBA `(0,0,0,210)` tại `y=0` → `(0,0,0,0)` tại `y=620`
- Mục đích: Làm nền tối đủ để chữ luôn đọc được bất kể nền gốc sáng hay tối

### Border Frame (Khung viền mạ vàng):
- **Outer frame**: Rect `(60,60)` → `(1940,1940)`, outline gold `#EBC350`, width **6px**
- **Inner frame**: Rect `(100,100)` → `(1900,1900)`, outline gold `#EBC350`, width **2px**
- **Corner ornaments** tại mỗi góc của inner frame:
  - Ô vuông lớn 100x100px (outline gold, 2px)
  - Ô vuông nhỏ 50x50px (outline gold, 1px)
  - Chấm solid gold 8x8px

### TITLE TEXT (Tiêu đề chính):
- **Font**: Arial Bold (macOS: `/System/Library/Fonts/Supplemental/Arial Bold.ttf`)
- **Cỡ chữ**: Auto-fit bắt đầu từ **120px**, giảm 4px/lần đến khi fit trong `max_width=1800px`
- **Màu chữ**: `(235, 195, 80)` — Vàng gold — KHÔNG dùng trắng cho title
- **Stroke đen**: `width=8px`, `fill=(0,0,0,255)`
- **Shadow layer**: Vẽ trên layer riêng với `GaussianBlur(radius=10)` TRƯỚC khi vẽ chữ nét
- **Vị trí Y bắt đầu**: `y = 140px`
- **Căn giữa** theo chiều ngang
- **Case**: `.upper()` — tất cả in HOA
- **Line spacing**: `font_size + 28px`

### SUBTITLE TEXT (Phụ đề):
- **Font**: Arial Bold, auto-fit từ **52px**, `max_width=1750px`
- **Màu chữ**: `(255, 255, 255, 225)` — Trắng gần hoàn toàn
- **Stroke đen**: `width=4px`
- **Vị trí Y**: Ngay sau dòng cuối title + **25px**
- **Căn giữa** theo chiều ngang
- **Case**: Giữ nguyên hoa thường (không .upper())

### BOTTOM LABEL "TIỂU THUYẾT VIỆT NAM":
- **Font**: Arial Bold, **36px**
- **Màu chữ**: Trắng `(255,255,255,255)`
- **Nền**: Rect tối `(10,8,5,215)` với border gold `#EBC350` 2px
- **Vị trí**: Căn giữa, y từ `1862` → `1938` (dưới cùng)
- **Width**: khoảng 680px (center of image)

### KHÔNG vẽ vào cover image:
- ❌ Chapter badge (Ch.5, Ch.12...) — do WordPress theme tự render
- ❌ View count / timestamp / logo website
- ❌ Tên tác giả (tùy chọn — chỉ dùng nếu muốn)

---

## PHẦN 3 — COLOR PALETTE CHUẨN

| Mục đích          | RGBA                        | Hex       |
|-------------------|-----------------------------|-----------|
| Title gold        | (235, 195, 80, 255)         | #EBC350   |
| Subtitle white    | (255, 255, 255, 225)        | —         |
| Border frame      | (235, 195, 80, 255)         | #EBC350   |
| Top overlay start | (0, 0, 0, 210) at y=0       | —         |
| Top overlay end   | (0, 0, 0, 0) at y=620       | —         |
| Bottom label bg   | (10, 8, 5, 215)             | —         |
| Text stroke       | (0, 0, 0, 255)              | #000000   |
| Shadow blur       | (0, 0, 0, 180) → blurred    | —         |

---

## PHẦN 4 — QUY TRÌNH SINH BÌA CHUẨN

```
Step 1: Xác định thông tin truyện
  - title_display   : Tiêu đề hiển thị trên bìa (dạng clickbait ngắn gọn)
  - subtitle         : Phụ đề / tagline ngắn
  - genre/setting    : Thể loại + bối cảnh địa điểm
  - characters       : Số nhân vật + nghề nghiệp + trang phục

Step 2: Build AI image prompt từ template PHẦN 1

Step 3: Gửi prompt → Pollinations Flux API → base image 2000x2000

Step 4: Chạy overlay script (cover_overlay_standard.py):
  - Apply top dark gradient (y=0 to y=620)
  - Draw gold double border + corner ornaments  
  - Render title (gold, center, top, .upper())
  - Render subtitle (white, below title)
  - Render bottom label

Step 5: Export PNG → Upload lên WordPress via FTP sideload
```

---

## PHẦN 5 — COVERS MẪU THAM KHẢO

| ID   | Tiêu đề                                   | Điểm nổi bật                              |
|------|-------------------------------------------|-------------------------------------------|
| 2207 | Thuyền Trưởng Tỷ Phú Cảng Tiên Sa        | Plaque trắng + serif title trong khung     |
| 2217 | Kỹ Sư Smart Grid EVN                      | Title gold on dark, tech book frame        |
| 2238 | Triều Đại Cà Phê Bazan Đắk Lắk           | Title gold lớn trực tiếp, full frame       |
| 2249 | Nhà Thiết Kế Tàng Hình VN Fashion Week    | Title gold + white, minimal border         |
| 2052 | Thần Y Phòng Khám 5 Quận 5                | Title gold top, corner ornament frame      |
| 2190 | Thần Tài Chứng Khoán Phố Wall Hà Nội     | 3-line title gold, subtitle white italic   |
| 2259 | Đầu Bếp Hội An Sao Michelin Đà Nẵng       | 2-line title cực lớn, no panel            |
| 2279 | Ông Hoàng Địa Ốc Ẩn Thế Phú Mỹ Hưng     | Dark wood plaque + gold title serif        |
| 2269 | CEO Giấu Mặt Tập Đoàn Dệt May Bình Dương  | Dark book cover + gold ornate frame        |
| 2289 | Vũ Công Hoàng Gia Đế Chế Nhà Hát Lớn     | Full ornate scroll frame, title at top     |

**BEST PRACTICE**: Title gold TRỰC TIẾP trên nền tối (gradient overlay),
KHÔNG dùng plaque/panel đen chắn ngang hình. Border vàng bao quanh toàn bìa.
Nhân vật tả thực chiếm 60-70% phần dưới, nhường 30-35% phía trên cho tiêu đề.

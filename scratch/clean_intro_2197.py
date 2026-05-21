import sys
sys.path.append("/Users/aaronnguyen/TN/App/doctieuthuyet/scratch")
import novel_editor

story_id = 2197
clean_intro = (
    "<p>\"Ngày tôi đến ra mắt, bà ấy nhìn đôi ủng xi măng trên chân tôi rồi phẩy tay: 'Thợ hồ mà dám đòi cưới con gái tôi?</p>"
    "<p>Cút ngay ra khỏi nhà, để dây bẩn lên gạch lát của tôi thêm một giây nữa là tôi gọi bảo vệ!'\" Nguyễn Thanh Hùng đứng trước cổng biệt thự triệu đô ở phường Phú Mỹ, Thủ Dầu Một — mồ hôi thấm qua lớp áo lao động bạc màu, đôi tay chai sần vì hàng chục năm trên công trường — mà không nói một lời.</p>"
    "<p>Bởi vì anh biết, gói thầu xây dựng Khu công nghiệp VSIP Bình Dương 3 — trị giá 2.000 tỷ đồng — đang chờ tên anh trên bàn ký kết.</p>"
)

print("🚀 Starting cleanup for Novel 2197...")
novel_editor.upload_helper()

try:
    print(f"Updating intro for story {story_id}...")
    res = novel_editor.update_story_meta(story_id=story_id, intro=clean_intro)
    print("Response:", res)
finally:
    novel_editor.remove_helper()
    print("✓ Cleanup script finished.")

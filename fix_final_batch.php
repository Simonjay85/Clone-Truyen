<?php
/**
 * fix_final_batch.php
 * 1) ID 2549 WP4138: Expand ch8 (2510 → ~6500 bytes) — durian farm final chapter
 * 2) ID 2682 WP4549: Rename ch8 title "Giây Phút Lật Kèo Tỷ Đô" → "Ván Bài Lật Kèo Tỷ Đô"
 */
ini_set('display_errors', 0);
ini_set('max_execution_time', 60);
header('Content-Type: application/json');
$input = json_decode(file_get_contents('php://input'), true);
if (!isset($input['secret_token']) || $input['secret_token'] !== 'ZEN_TRUYEN_2026_BYPASS') {
    http_response_code(401); echo json_encode(['error'=>'Unauthorized']); exit;
}
require_once('wp-load.php');
$results = [];

// ==================== TASK 1: ID 2549 WP4138 — Expand ch8 ====================
$new_ch8_2549 = <<<'VIET'
Kết quả phân tích mẫu đất từ Chi cục Bảo vệ Thực vật tỉnh Tiền Giang trả về lúc chín giờ sáng thứ Tư: mẫu đất lấy từ khu vực gốc cây bị chết phát hiện Endosulfan nồng độ 47,3 mg/kg — gấp mười lần ngưỡng cho phép theo QCVN 15:2008. Đây là loại thuốc trừ sâu đã bị cấm sử dụng tại Việt Nam từ năm 2016.

Nguyễn Tấn Đạt đặt tờ kết quả xuống bàn, nhìn ra vườn sầu riêng Monthong. Mười tám cây đã chết không thể cứu. Hai trăm mười bảy cây còn lại đang phục hồi sau khi được xử lý đất tuần trước.

"Endosulfan," kỹ thuật viên của Chi cục nói, "chỉ còn lưu hành tại một số ít điểm bán hóa chất không phép. Chúng tôi đã phối hợp với Phòng Cảnh sát Kinh tế truy nguồn lô hàng."

Nguồn lô hàng dẫn về kho chứa hóa chất tại ấp Mỹ Lợi — cách vườn của Đạt bốn cây số. Chủ kho: Lộc Điền Trang, công ty thuộc quyền quản lý của Trần Văn Lộc — người đã hai lần đề nghị mua lại vườn sầu riêng của nhà Đạt với giá thấp hơn thị trường 40%, và hai lần bị từ chối.

Trần Văn Lộc bị bắt tạm giam tối hôm đó.

---

Tin tức lan ra khắp ấp Phú Điền trước bình minh hôm sau. Bà Năm bán bánh cuốn đầu xóm gọi điện cho chú Tám trồng nhãn bên kia bờ kênh. Chú Tám gọi cho mấy anh em trong Hợp tác xã Sầu Riêng Tiền Giang. Hợp tác xã gọi cho Chi hội Nông dân xã. Đến bảy giờ sáng, đã có hơn chục người đứng trước cổng vườn nhà Đạt.

Họ không mang hoa. Họ mang cuốc, mang xẻng, mang bình phun thuốc hữu cơ.

"Mình xử lý lớp đất mặt còn lại đi," ông Tư Hải — Chủ tịch Hợp tác xã, người đã cùng cha Đạt ký giấy thành lập hợp tác xã mười bảy năm trước — nói giản dị như vậy. Không cần hỏi. Không cần được mời. Người Miền Tây có cách biểu đạt tình cảm không cần lời.

Đạt đứng nhìn đám đông lần lượt vào vườn, tay cầm tờ kết quả phân tích mà không biết nên đặt vào đâu. Cha anh nằm trong nhà, chân trái đã yếu từ sau đợt tai biến năm ngoái. Ông không thể ra vườn. Nhưng khi nghe tiếng người trong vườn qua cửa sổ, Đạt thấy cha mình lặng người rồi quay mặt đi — không phải vì buồn, mà vì có thứ gì đó lớn hơn buồn.

Trần Mỹ Duyên mang nước ra từ nhà bếp. Cô rót từng ly một, đi từ người này sang người kia. Ít ai để ý đến cô — cô chỉ là con gái ông chủ đại lý vật tư nông nghiệp, quen mặt nhưng chưa thân. Nhưng những người trong vườn hôm đó nhận ra một điều mà không cần nói ra: cô ở đây từ ngay khi tin tức vỡ, và cô ở lại cho đến khi việc xong.

---

Vụ án được đưa ra tòa sáu tuần sau. Trần Văn Lộc bị truy tố tội hủy hoại tài sản và sử dụng hóa chất độc hại trái phép — khung hình phạt từ hai đến bảy năm tù. Bằng chứng từ kho hóa chất tại ấp Mỹ Lợi đủ để buộc tội mà không cần nhân chứng thêm. Luật sư bào chữa của Lộc cố lập luận rằng chưa có bằng chứng trực tiếp về hành vi, nhưng hội đồng xét xử không chấp nhận: chuỗi bằng chứng gián tiếp — mua hóa chất cấm, cất tại kho gần vườn, có động cơ mua đất rõ ràng — đủ để lập thành tội.

Đạt không đến dự phiên tòa. Có người hỏi tại sao. Anh nói: "Mình cần ở vườn."

Đó là sự thật đơn giản. Mười tám cây đã mất rồi. Tòa án không thể trả lại chúng. Điều còn lại là hai trăm mười bảy cây đang sống cần người chăm sóc.

---

Ba tuần sau phiên tòa, Nguyễn Tấn Đạt và Trần Mỹ Duyên ký hợp đồng xuất khẩu sầu riêng đông lạnh với đối tác Hàn Quốc — ba trăm tấn, giao hàng vụ tới. Giá thu mua 85.000 đồng/kg, cao hơn giá sàn chợ nội địa 22%.

Hợp đồng không ký riêng cho vườn Đạt. Nó ký dưới tên Hợp tác xã Sầu Riêng Tiền Giang — mười hai thành viên, bảy trăm tấn sản lượng một năm, được đại diện duy nhất trên tờ giấy đó là ông Tư Hải và Nguyễn Tấn Đạt với tư cách Phó Chủ tịch kiêm Giám đốc Kỹ thuật.

Chức danh mới. Đạt chưa quen với nó.

"Em nghĩ anh sẽ từ chối," Duyên nói khi ra về từ buổi ký kết.

"Tại sao?"

"Anh hay làm một mình."

Đạt im lặng một lúc. Đó là sự thật anh không muốn thừa nhận — rằng trong suốt mấy tháng qua, anh đã xử lý mọi thứ một mình, từ chối sự giúp đỡ nhiều hơn cần thiết, như thể tự chứng minh điều gì đó với bản thân. Với cha. Với mảnh đất.

"Mình không thể làm một mình vụ này," anh nói. "Đó là lý do Lộc gần thắng."

Duyên gật đầu. Không nói thêm gì. Đó cũng là loại ngôn ngữ mà người Miền Tây quen dùng.

---

Vườn không phục hồi hoàn toàn — mười tám cây mất là mười tám năm chờ đợi, không thể tính bằng tiền. Nhưng đất Miền Tây đã quen với những mất mát như thế. Người ta trồng lại. Người ta chờ.

"Vụ sau mình trồng thêm chỗ nào?" Duyên hỏi, nhìn ra góc vườn còn trống.

Đạt nhìn theo. Mảnh đất đó — cha anh mua từ năm 1998, trả hết tiền bằng mười vụ lúa — đang đợi rễ mới.

"Chỗ đó," anh nói, "trồng thêm mười lăm cây. Musang King. Thị trường đang cần."

"Tám năm nữa mới có trái."

"Ừ." Anh không thấy đó là vấn đề. Cha anh đã trồng những cây Monthong ba mươi năm trước khi ông chưa biết anh sẽ ra đời. Người trồng sầu riêng không tính đời người, họ tính đời cây.

Duyên nhìn anh một lúc theo cách mà anh bắt đầu quen — không phải nhìn để hiểu, mà là nhìn vì đã hiểu rồi.

"Tám năm," cô lặp lại, giọng không phải hỏi.

"Tám năm," anh xác nhận.

Trên đầu họ, bầu trời Miền Tây cuối mùa khô sắp sang mưa. Những đám mây màu chì từ hướng Vịnh Thái Lan đang dạt vào. Đất sầu riêng Tiền Giang cần mưa hơn bất cứ thứ gì — và mưa sắp đến.
VIET;

$update1 = wp_update_post([
    'ID' => 4138,
    'post_content' => wp_kses_post($new_ch8_2549),
]);
if (function_exists('litespeed_purge_post')) litespeed_purge_post(4138);
$results[] = ['task'=>'expand_ch8_2549','wp_id'=>4138,'result'=>$update1,'new_len'=>strlen($new_ch8_2549)];

// ==================== TASK 2: ID 2682 WP4549 — Rename ch8 title ====================
$update2 = wp_update_post([
    'ID' => 4549,
    'post_title' => 'Chương 8: Ván Bài Lật Kèo Tỷ Đô',
]);
if (function_exists('litespeed_purge_post')) litespeed_purge_post(4549);
$results[] = ['task'=>'rename_ch8_2682','wp_id'=>4549,'result'=>$update2];

if (function_exists('litespeed_purge_all')) litespeed_purge_all();
echo json_encode(['results'=>$results], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
?>

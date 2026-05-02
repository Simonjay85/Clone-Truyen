export type StoryGenreId = 
  | 'ngon_tinh' 
  | 'tien_hiep' 
  | 'huyen_ao' 
  | 'kinh_di' 
  | 'dam_my_bach_hop' 
  | 'romantasy' 
  | 'sci_fi' 
  | 'zhihu_short' 
  | 'micro_drama';

export interface StoryGenre {
  id: StoryGenreId;
  name: string;
  description: string;
  suggestedTags: Record<string, string[]>;
  getPitchPrompt: (target: number, min: number, max: number) => string;
  overridePrompt: string;
}

export const STORY_GENRES: Record<StoryGenreId, StoryGenre> = {
  ngon_tinh: {
    id: 'ngon_tinh',
    name: 'Ngôn Tình (Romance)',
    description: 'Tập trung vào tình yêu nam nữ. Bao gồm Hiện đại, Cổ đại, Thanh xuân vườn trường.',
    suggestedTags: {
      "🌍 Bối Cảnh": ["Hiện đại", "Cổ đại", "Thanh xuân vườn trường", "Hào môn thế gia"],
      "🔥 Motif Trend": ["Trọng sinh", "Xuyên không", "Hợp đồng hôn nhân", "Cưới trước yêu sau", "Gương vỡ lại lành"],
      "❤️ Hình Tượng 2026": ["Nữ cường", "Ngược tra", "Vả mặt", "Tổng tài bá đạo", "Trà xanh", "Cứu rỗi"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là chuyên gia sáng tác tiểu thuyết Ngôn Tình.
Nhiệm vụ: Tạo ra ${target} kịch bản truyện Ngôn Tình (có thể tùy biến theo bối cảnh Hiện đại, Cổ đại, v.v.).
Yêu cầu kịch bản:
1. "super_title": Tên truyện cực kỳ cuốn hút, giật gân, ngôn tình. Dài từ 5-10 chữ.
2. "protagonist": Giới thiệu chi tiết cặp đôi nam nữ chính (hoàn cảnh, tính cách, nhược điểm).
3. "summary": Tóm tắt cốt truyện chính (Khởi đầu, Xung đột, Chuyển biến tình cảm, Kết thúc). Tập trung vào chemistry và mâu thuẫn tình cảm.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê các tags (thể loại con, ví dụ: Hào môn, Trọng sinh, Ngược tra).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 20,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC NGÔN TÌNH: Hãy viết với văn phong lãng mạn, trau chuốt ngôn từ. Tập trung miêu tả thật sâu sắc nội tâm nhân vật, những rung động, đau khổ, dằn vặt hoặc ngọt ngào. Mọi mâu thuẫn gia tộc hay sự nghiệp cuối cùng đều phải phục vụ cho sự phát triển tuyến tình cảm của nam nữ chính."
  },

  tien_hiep: {
    id: 'tien_hiep',
    name: 'Tiên Hiệp / Kiếm Hiệp',
    description: 'Thế giới võ thuật, tu tiên, bay lượn, sức mạnh siêu nhiên.',
    suggestedTags: {
      "🌍 Bối Cảnh": ["Tu tiên giới", "Giang hồ võ lâm", "Tông môn", "Thượng cổ thần giới"],
      "🔥 Motif Trend": ["Trọng sinh", "Xuyên không", "Vô địch lưu", "Phế vật lưu", "Hệ thống tu tiên"],
      "⚔️ Đặc Trưng": ["Độ kiếp", "Luyện đan", "Bí cảnh", "Pháp bảo", "Đạo lữ"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là một đại tông sư sáng tác tiểu thuyết Tiên Hiệp / Kiếm Hiệp.
Nhiệm vụ: Tạo ra ${target} kịch bản truyện Tu Tiên / Võ Hiệp với không khí hào hùng, thế giới quan rộng lớn.
Yêu cầu kịch bản:
1. "super_title": Tên truyện mang âm hưởng hùng tráng, kỳ ảo (VD: Nghịch Thiên Tà Thần, Đạo Tình). Dài từ 5-10 chữ.
2. "protagonist": Giới thiệu nam/nữ chính (Bàn tay vàng, căn cốt, tính cách sát phạt quyết đoán hay cẩn trọng).
3. "summary": Hành trình tu luyện, đối mặt cừu nhân, tranh đoạt bí cảnh, vượt thiên kiếp.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Tu tiên, Phế vật lưu, Hệ thống).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 25,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC TIÊN HIỆP: Văn phong mang đậm nét cổ phong, sử dụng từ ngữ tu chân (cảnh giới, pháp bảo, linh căn). Khắc họa thế giới tàn khốc 'cá lớn nuốt cá bé'. Nhân vật phải trải qua sinh tử, cơ trí, sát phạt quyết đoán. Cảnh chiến đấu phải hoành tráng, chiêu thức uy lực kinh thiên động địa."
  },

  huyen_ao: {
    id: 'huyen_ao',
    name: 'Huyền Ảo (Fantasy)',
    description: 'Phép thuật, rồng, quái vật, các thế giới giả tưởng phương Tây.',
    suggestedTags: {
      "🌍 Bối Cảnh": ["Đế chế phương Tây", "Học viện ma thuật", "Đại lục giả tưởng", "Thế giới ngầm"],
      "🔥 Motif Trend": ["Trọng sinh", "Xuyên không", "Triệu hồi sư", "Hệ thống phép thuật", "Ma vương"],
      "⚔️ Yếu Tố": ["Rồng", "Yêu tinh (Elf)", "Thần linh", "Quái vật", "Hiệp sĩ"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là một tác giả Fantasy (Huyền Ảo) phương Tây xuất sắc.
Nhiệm vụ: Tạo ra ${target} kịch bản truyện Fantasy với phép thuật, thần linh, rồng và những cuộc phiêu lưu sử thi.
Yêu cầu kịch bản:
1. "super_title": Tên truyện mang màu sắc phương Tây sử thi (Epic). Dài từ 4-10 chữ.
2. "protagonist": Anh hùng, hiệp sĩ, pháp sư, hay kẻ bị ruồng bỏ với vận mệnh lớn lao.
3. "summary": Hành trình chống lại thế lực bóng tối, khám phá đại lục bí ẩn, thu thập thánh khí.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Xuyên không, Phép thuật, Ma vương).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 20,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC HUYỀN ẢO: Xây dựng hệ thống sức mạnh (ma pháp, đấu khí) logic và chi tiết. Miêu tả bối cảnh rộng lớn, những trận chiến ma thuật rực rỡ, những chủng tộc đa dạng (Elf, Orc, Rồng). Khắc họa sự tàn khốc của vương quyền và vận mệnh."
  },

  kinh_di: {
    id: 'kinh_di',
    name: 'Kinh Dị / Linh Dị',
    description: 'Ma quái, tâm linh, phá án ly kỳ có yếu tố rùng rợn.',
    suggestedTags: {
      "🌍 Bối Cảnh": ["Thành thị tâm linh", "Ngôi nhà hoang", "Trường học cấm kỵ", "Làng quê ám ảnh"],
      "🔥 Motif Trend": ["Vô hạn lưu", "Hệ thống sinh tồn", "Xuyên nhanh kinh dị", "Phòng tối"],
      "👻 Yếu Tố": ["Quỷ hồn", "Phá án ly kỳ", "Trò chơi tử thần", "Quy tắc sinh tồn", "Thực thể tà ác"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là bậc thầy truyện Kinh Dị, Linh Dị, Hồi Hộp.
Nhiệm vụ: Tạo ra ${target} kịch bản gây ám ảnh tâm lý, có yếu tố tâm linh hoặc phá án rùng rợn.
Yêu cầu kịch bản:
1. "super_title": Tên truyện gợi sự tò mò, sợ hãi. Càng ngắn gọn càng ám ảnh.
2. "protagonist": Người vô tình bị kéo vào lời nguyền, trò chơi tử thần, hoặc người có khả năng đặc biệt.
3. "summary": Sự kiện kỳ bí khởi đầu, quá trình đấu trí sinh tồn, những cú twist xoắn não kinh hoàng.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Vô hạn lưu, Sinh tồn, Quy tắc).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 15,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC KINH DỊ: Tập trung miêu tả bầu không khí ngột ngạt, u ám và căng thẳng. Không lạm dụng jumpscare rẻ tiền mà dùng nỗi sợ tâm lý, sự méo mó của thực tại. Tuân thủ nghiêm ngặt các quy tắc sinh tồn nếu có. Twist phải logic và gây rùng mình ở những dòng cuối chương."
  },

  dam_my_bach_hop: {
    id: 'dam_my_bach_hop',
    name: 'Đam Mỹ / Bách Hợp',
    description: 'Tình yêu đồng giới nam-nam hoặc nữ-nữ.',
    suggestedTags: {
      "🌍 Thể Loại": ["Đam Mỹ (Nam-Nam)", "Bách Hợp (Nữ-Nữ)"],
      "🌍 Bối Cảnh": ["Hiện đại đô thị", "Cổ đại cung đình", "Hào môn thế gia", "Võng du", "Tinh tế"],
      "🔥 Motif Trend": ["Trọng sinh", "Xuyên không", "Hệ thống", "Cưới trước yêu sau", "Gương vỡ lại lành"],
      "❤️ Hình Tượng": ["Cường cường", "Ngược luyến", "Ngọt sủng", "Trà xanh"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là một tác giả cực kỳ am hiểu văn hóa Đam Mỹ / Bách Hợp.
Nhiệm vụ: Tạo ra ${target} kịch bản xuất sắc tập trung vào tình yêu đồng giới.
Yêu cầu kịch bản:
1. "super_title": Tên truyện lãng mạn hoặc ẩn dụ sâu sắc.
2. "protagonist": Giới thiệu chi tiết cặp đôi (Công - Thụ), thiết lập hình tượng rõ ràng (Cường cường, Ôn nhu, Ngạo kiều...).
3. "summary": Quá trình gặp gỡ, những định kiến hoặc khó khăn phải vượt qua, những khoảnh khắc kéo đẩy (push-pull) tình cảm.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Đam Mỹ, Trọng sinh, Ngọt sủng).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 20,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC ĐAM MỸ/BÁCH HỢP: Tập trung khai thác những khía cạnh tinh tế trong tâm lý và tương tác giữa cặp đôi chính. Miêu tả những đụng chạm nhỏ, những ánh mắt, sự giằng xé nội tâm. Hình tượng nhân vật phải đồng nhất, đặc biệt nhấn mạnh vào sự thấu hiểu và cứu rỗi lẫn nhau."
  },

  romantasy: {
    id: 'romantasy',
    name: 'Romantasy (2026)',
    description: 'Sự kết hợp giữa tình yêu lãng mạn và thế giới phép thuật kỳ ảo.',
    suggestedTags: {
      "🌍 Bối Cảnh": ["Học viện phép thuật", "Vương quốc sụp đổ", "Khu rừng cấm", "Cung điện hoàng gia"],
      "🔥 Motif Trend": ["Kẻ thù thành người yêu (Enemies to lovers)", "Vận mệnh ràng buộc", "Hôn nhân chính trị"],
      "⚔️ Hình Tượng": ["Nữ cường chiến binh", "Ma tôn / Bạo quân", "Hiệp sĩ bảo hộ"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là chuyên gia về thể loại Romantasy (Romance + Fantasy) cực kỳ thịnh hành.
Nhiệm vụ: Tạo ra ${target} kịch bản kết hợp hoàn hảo giữa những cảnh lãng mạn bốc lửa và những trận chiến phép thuật khốc liệt.
Yêu cầu kịch bản:
1. "super_title": Tên truyện mang hơi hướng thần thoại và tình yêu cay đắng.
2. "protagonist": Nữ cường nhân dũng cảm + Nam chính nguy hiểm/kẻ thù/bạo chúa.
3. "summary": Cốt truyện song song: Cứu thế giới/Vương quốc và Mối tình ngang trái 'Enemies to lovers'.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Romantasy, Nữ cường, Kẻ thù thành tình nhân).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 20,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC ROMANTASY: Phải giữ thế cân bằng 50/50 giữa cốt truyện kỳ ảo (đánh nhau, chính trị) và tình cảm lãng mạn bốc lửa. Xây dựng những đoạn đối thoại sắc bén (bantering) giữa hai nhân vật chính. Cảm xúc mãnh liệt, vừa yêu vừa hận, 'thế giới sụp đổ cũng không bằng việc mất đi người ấy'."
  },

  sci_fi: {
    id: 'sci_fi',
    name: 'Khoa Học Viễn Tưởng (Sci-Fi)',
    description: 'Tương lai gần, trí tuệ nhân tạo (AI), cyberpunk, đạo đức công nghệ.',
    suggestedTags: {
      "🌍 Bối Cảnh": ["Tương lai gần", "Cyberpunk đô thị", "Trạm vũ trụ", "Hậu tận thế (Mạt thế)"],
      "🔥 Chủ Đề": ["Trí tuệ nhân tạo (AI)", "Đột biến gen", "Thực tế ảo (VR)", "Du hành thời gian"],
      "⚔️ Xung Đột": ["Đạo đức công nghệ", "Sinh tồn mạt thế", "Khởi nghĩa người máy", "Tập đoàn độc quyền"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là một tiểu thuyết gia Sci-Fi và Speculative Fiction tầm cỡ Hugo Award.
Nhiệm vụ: Tạo ra ${target} kịch bản bối cảnh tương lai, khoa học, phản ánh góc tối của công nghệ.
Yêu cầu kịch bản:
1. "super_title": Tên truyện mang màu sắc công nghệ, lạnh lẽo, ấn tượng.
2. "protagonist": Kỹ sư, hacker, AI có ý thức, hoặc người sống sót cuối cùng.
3. "summary": Khám phá ra bí mật kinh hoàng của xã hội tương lai, đấu tranh giữa nhân tính và máy móc.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Cyberpunk, AI, Mạt thế).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 15,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC SCI-FI: Văn phong logic, sử dụng các thuật ngữ công nghệ nhưng dễ hiểu. Miêu tả một thế giới tương lai chân thực, lạnh lẽo, đèn neon (nếu là Cyberpunk). Nhấn mạnh vào những mâu thuẫn triết học: 'Điều gì làm nên con người?', sự kiểm soát của AI, và sự giằng xé đạo đức."
  },

  zhihu_short: {
    id: 'zhihu_short',
    name: 'Đoản Văn Zhihu',
    description: 'Truyện cực ngắn, kể ngôi thứ nhất, twist cuối, mì liền.',
    suggestedTags: {
      "🔥 Đặc Trưng": ["Ngôi thứ nhất (Tôi)", "Plot Twist chấn động", "Đọc nhanh (Mì liền)", "Kết mở / SE / HE"],
      "⚔️ Chủ Đề": ["Tình cảm gia đình", "Trả thù tàn khốc", "Tâm lý học", "Chuyện kỳ bí đời thường"],
      "❤️ Motif Trend": ["Vả mặt tát tai", "Ngược tra tồi tệ", "Thay mận đổi đào", "Con giáp thứ 13"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là chuyên gia sáng tác Đoản văn phong cách Zhihu / Reddit mượt mà.
Nhiệm vụ: Tạo ra ${target} kịch bản truyện siêu ngắn SẢNG VĂN (đọc là sướng, vả mặt ác liệt), đọc nhanh giải trí, chốt hạ bằng một cú plot twist bất ngờ 100%.
Yêu cầu kịch bản (Tuân thủ CẤU TRÚC 7 NHỊP — MỖI NHỊP = 1 SỰ KIỆN, KHÔNG KÉO DÀI):
1. "super_title": Tên truyện giật gân y như tiêu đề bài bóc phốt trên MXH. Dài từ 8-15 chữ.
2. "protagonist": Nhân vật "Tôi" (xưng ngôi thứ nhất) - CẤM NGỐC NGHẾCH. Thông minh, thâm tàng bất lộ. Có điểm yếu bề ngoài để che giấu sức mạnh bên trong. KHÔNG được thụ động quá 2 cảnh liên tiếp mà không phản đòn.
3. "summary": Cốt truyện bám sát:
   NHỊP 1: Bị sỉ nhục TRƯỚC MẶT NHIỀU NGƯỜI.
   NHỊP 2: Bị dồn ép tưởng chừng đã thua — nhưng "Tôi" đã cài sẵn bẫy.
   NHỊP 3: Leo thang căng thẳng — tình thế có vẻ tệ hơn.
   NHỊP 4: Vả mặt lần đầu TRỰC TIẾP TRƯỚC ĐÁM ĐÔNG.
   NHỊP 5: Hé lộ sự thật tàn khốc về kẻ thù HOẶC về chính "Tôi".
   NHỊP 6: Màn vả mặt cuối — kẻ thù nhục nhã không thể gỡ gạc.
   NHỊP 7: Twist 100% bất ngờ — lật ngược nhận thức toàn bộ câu chuyện. TUYỆT ĐỐI không gợi ý trước chương áp cuối.
   GIỚI HẠN nhân vật phụ: TỐI ĐA 3 người, mỗi người phải xuất hiện ít nhất 3 lần. CẤM tạo nhân vật chỉ để cảnh báo rồi biến mất.
   Logic thực tế: CẤM súng đạn, bắt cóc phi lý ở VN hiện đại.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}). Ưu tiên ÍT chương, mỗi chương súc tích.
5. "genres": Liệt kê tags (VD: Ngược tra, Vả mặt, Ngôi thứ nhất).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 10,
    "genres": "..."
  }
]`,
    overridePrompt: `LỆNH BẢN GỐC ZHIHU - CHUẨN ĐOẢN VĂN MẠNG (SẢNG VĂN - PHIÊN BẢN TỐI ƯU):
Bắt buộc viết bằng NGÔI THỨ NHẤT ('Tôi'). CẤM TUYỆT ĐỐI 'nhật ký nội tâm' ỉ ôi, sướt mướt.

LUẬT 1 - NHỊP ĐỘ:
- Mỗi chương = DUY NHẤT 1 sự kiện lớn. Không nhồi nhét, không kể lể.
- CẤM tả cảnh thiên nhiên, cảnh vật, thời tiết trừ khi nó trực tiếp gây ra xung đột.
- CẤM mở đầu chương bằng 'Tôi ngồi nghĩ...' / 'Tôi nhớ lại...' nếu không có hành động ngay câu tiếp theo.
- Hội thoại chiếm 70%, phải sắc bén, đốp chát, châm biếm, mang sức nặng cảm xúc.
- Mỗi chương BẮT BUỘC kết bằng 1 hành động gây sốc hoặc 1 câu thoại đánh thẳng vào mặt đối thủ.

LUẬT 2 - VẢ MẶT TRỰC TIẾP:
- Phải có ÍT NHẤT 2 cảnh vả mặt TRỰC TIẾP TRƯỚC ĐÁM ĐÔNG (không phải riêng tư, không phải sau cánh gà).
- Khi vả mặt: viết chậm, chi tiết cảm xúc của KẺ BỊ VẢ (hoảng loạn, nhục nhã, không nói được). Đây là khoảnh khắc độc giả chờ đợi nhất.
- Lời thoại vả mặt phải SẮC, NGẮN, CHÍNH XÁC. VD: không phải 'Anh sai rồi' mà là 'Anh quên mất: tôi đã ghi âm toàn bộ từ 3 tháng trước.'
- Trả thù TÂM LÝ (nhục nhã trước đám đông, mất địa vị, bị vạch mặt) phải đau hơn trả thù thể xác.

LUẬT 3 - NHÂN VẬT PHỤ:
- TỐI ĐA 3 nhân vật phụ có vai trò. Mỗi người phải xuất hiện ÍT NHẤT 3 lần và có vai trò rõ ràng đến cuối.
- CẤM tạo nhân vật chỉ để cảnh báo nhân vật chính rồi biến mất. Đây là 'filler' làm loãng truyện.

LUẬT 4 - ẨN TWIST:
- Nếu có twist danh tính hoặc twist tình huống, TUYỆT ĐỐI không để lộ gợi ý trước chương áp cuối.
- Mọi chi tiết cài cắm phải đủ mơ hồ để độc giả hiểu theo hướng khác. Chỉ khi reveal mới 'chốt' lại.
- Câu cuối truyện phải khiến người đọc muốn đọc lại từ đầu.

LUẬT 5 - LOGIC THỰC TẾ (VN & TRUNG QUỐC):
- Nếu bối cảnh VIỆT NAM hiện đại: CẤM dùng súng nổ, bắt cóc ngoài đường ban ngày, xã hội đen lộ liễu không bị công an xử lý. Trả thù hợp lý phải qua: tố cáo cơ quan, bằng chứng ghi âm/video, dư luận MXH, hoặc đòn kinh tế/pháp lý.
- Nếu bối cảnh TRUNG QUỐC hiện đại: CẤM tình tiết phi lý với văn hóa TQ (VD: phụ nữ bình dân tát công khai đại gia mà không bị hệ lụy). Trả thù hợp lý theo văn hóa TQ: "thân bại danh liệt" (mất danh dự gia tộc), bị gạt ra khỏi giới thượng lưu, vạch mặt tại bàn tiệc gia đình, lật tẩy trước đối tác kinh doanh. Tận dụng văn hóa "mặt mũi" (面子) — mất mặt trước đám đông là hình phạt nặng nề nhất.
- Nếu bối cảnh CỔ ĐẠI/CUNG ĐÌNH: Quyền lực thay đổi qua mưu kế, bằng chứng thư tín/di chúc, hoặc lộ bí mật trước triều đình. CẤM các tình tiết quá hiện đại (điện thoại, internet).
- NGUYÊN TẮC CHUNG: Trả thù bằng TRÍ TUỆ, BẰNG CHỨNG, hoặc ĐÒN TÂM LÝ XÃ HỘI — không phải bạo lực thô.`
  },

  micro_drama: {
    id: 'micro_drama',
    name: 'Kịch Tính (Micro Drama)',
    description: 'Truyện kịch tính cao, vả mặt, tranh đấu liên tục.',
    suggestedTags: {
      "🔥 Xung Đột": ["Vả mặt cực mạnh", "Gia đấu (Mẹ chồng nàng dâu)", "Cung đấu", "Thương trường"],
      "🌍 Bối Cảnh": ["Hào môn thế gia", "Cung đình", "Giới giải trí", "Đô thị"],
      "⚔️ Motif Trend": ["Trọng sinh báo thù", "Xuyên không", "Hệ thống vả mặt", "Giấu nghề / Giả heo ăn hổ"]
    },
    getPitchPrompt: (target, min, max) => `Bạn là bậc thầy kịch bản Micro-Drama (Phim ngắn/Truyện kịch tính TikTok, Kuaishou, Douyin).
Nhiệm vụ: Tạo ra ${target} kịch bản truyện tập trung vào sự vả mặt (Face-slapping), sảng văn, drama dồn dập không ngừng nghỉ.
Yêu cầu kịch bản:
1. "super_title": Tên truyện cực kỳ giật gân, khơi gợi sự tò mò mạnh. (VD: Tỷ Phú Giả Nghèo Vả Mặt Trà Xanh).
2. "protagonist": Main bị sỉ nhục, giấu nghề, hoặc trùng sinh báo thù. Có bàn tay vàng cực mạnh.
3. "summary": Khởi đầu bị chà đạp tận cùng, sau đó lật bài tẩy, vả mặt từng kẻ thù một cách tàn nhẫn, sảng khoái.
4. "target_chapters": Gợi ý số chương (từ ${min} đến ${max}).
5. "genres": Liệt kê tags (VD: Vả mặt, Gia đấu, Hào môn, Sảng văn).

YÊU CẦU TRẢ VỀ CHỈ MỘT MẢNG JSON ARRAY:
[
  {
    "super_title": "...",
    "protagonist": "...",
    "summary": "...",
    "target_chapters": 20,
    "genres": "..."
  }
]`,
    overridePrompt: "LỆNH BẢN GỐC MICRO DRAMA: Nhịp độ truyện phải NHANH NHƯ CHỚP. Cứ 3-5 câu là phải có 1 đoạn hội thoại châm biếm, sỉ nhục. Mọi nhân vật phụ phản diện phải ngu ngốc, phô trương để làm nền cho sự bùng nổ của nhân vật chính. Khi vả mặt, phải viết sao cho người đọc cảm thấy cực kỳ thỏa mãn, hạ nhục đối thủ không thương tiếc."
  }
};

export const STORY_GENRE_LIST = Object.values(STORY_GENRES);

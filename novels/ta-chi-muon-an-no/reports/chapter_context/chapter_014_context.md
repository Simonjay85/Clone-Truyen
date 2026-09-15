# Chapter 014 Context Evidence

- story_bible.md SHA256: `886211f0fa5c15b06a93d7b3cffec03b08d2ad4aa834ca56ec4adef8c214a747`
- writer_contract.md SHA256: `5cb18d4f8717fc27d7f80fd292488adbac19bf5bb542ecea39cf7a9e527a6df9`
- master_manifest.json SHA256: `93dc655b2e0b8531195772b7e4f56fc93d1613886d11dd3df70113c5e14f5490`
- continuity/ledger.json SHA256: `b670e38622223925904dcfaf233677a1c3587c802a22ec184cbbe640cb9e1ba2`
- latest block review: `none`

## Manifest record
```json
{
  "chapter": 14,
  "volume": 1,
  "volume_title": "Thiên Hạ Sao Yếu Vậy?",
  "subarc": "V01A2",
  "subarc_title": "Không Phải Ta Mạnh",
  "title": "Chương 14: Không Phải Ta Mạnh — Dấu Vết",
  "title_status": "provisional_until_batch_draft",
  "beat_function": "investigation",
  "objective": "Đưa bằng chứng mystery/foreshadow cụ thể nhưng chưa giải quá mốc; tăng câu hỏi đúng hướng. Trọng tâm riêng chương: Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "conflict": "Thương đội bị cướp tu sĩ; hắn muốn trốn nhưng không chịu nhìn trẻ con bị giết.",
  "character_beat": "Chưa romance; định hình giới hạn đạo đức của main.",
  "mystery_beat": "Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "power_guardrail": "Lần đầu thử Dẫn Khí thất bại trên bề mặt; sức thân thể đánh văng Dẫn Khí cao tầng.",
  "foreshadow_or_payoff": "Linh khí vào người biến mất; nồi đen phản ứng với linh thạch.",
  "cliffhanger_type": "evidence",
  "status": "planned",
  "draft_file": "chapters/chapter_014.md"
}
```

## Current state
```json
{
  "ta_tieu_bao": {
    "age": 13,
    "cultivation": "chưa nhập Dẫn Khí; thử cảm khí thất bại trên bề mặt",
    "location": "nhánh khe hẹp phía nam Hắc Nha Pha",
    "injuries": [
      "vết cắt lòng bàn tay rách lại",
      "chấn thương sườn phải, đau khi xoay/hít sâu"
    ],
    "inventory": [
      "ba đồng tiền cũ",
      "dao cũ đã mài",
      "nồi đen gia cố quai",
      "quần áo",
      "thuốc bà Mạnh",
      "muối",
      "ít bánh/thịt khô còn lại"
    ],
    "relationship_with_thanh_nghi": "chưa gặp",
    "known_truths": [
      "Lạc Kê vẫn là nhà dù hắn rời đi",
      "người ngoài có hệ Dẫn Khí/Khai Mạch/Trúc Đài",
      "linh thạch là tiền của tu sĩ",
      "tu sĩ có thể dùng phù/pháp khí",
      "bản thân chưa cảm được linh khí theo cách thông thường",
      "Tán Linh Tán áp chế tu sĩ nhưng gần như không tác dụng lên bản thân",
      "linh lực ngoại lai chạm vào cơ thể bản thân có thể biến mất không rõ nguyên nhân"
    ]
  },
  "luc_thanh_nghi": {
    "age": 17,
    "cultivation": "Thiên tài kiếm đạo, chi tiết cảnh giới sẽ khóa khi xuất hiện",
    "location": "ngoài màn truyện",
    "injuries": [],
    "relationship_with_tieu_bao": "chưa gặp",
    "known_truths": [
      "mình thuộc Lục gia",
      "mình được gia tộc kỳ vọng như kiếm tu thiên tài"
    ]
  },
  "o_gia": {
    "state": "gà đen, huyết mạch bị khóa; tự ý theo Tiểu Bảo ra khỏi Lạc Kê",
    "location": "cùng Tiểu Bảo tại Hắc Nha Pha",
    "speech": false
  }
}
```

## Unresolved hooks
```json
[
  {
    "id": "H001",
    "seed_range": "1-10",
    "question": "Dân Lạc Kê thật sự là ai?",
    "reveal_target": "601-650",
    "status": "planned"
  },
  {
    "id": "H002",
    "seed_range": "1-20",
    "question": "Vì sao việc nhà Lạc Kê giống đại đạo?",
    "reveal_target": "301-350/601-650",
    "status": "planned"
  },
  {
    "id": "H003",
    "seed_range": "3-19",
    "question": "Cái nồi đen là gì?",
    "reveal_target": "97/580+/620+",
    "status": "planned"
  },
  {
    "id": "H004",
    "seed_range": "10-100",
    "question": "Vì sao linh khí vào người Tiểu Bảo biến mất?",
    "reveal_target": "98/150+/580+",
    "status": "planned"
  },
  {
    "id": "H005",
    "seed_range": "47-100",
    "question": "Vì sao đá linh căn phản ứng dị thường?",
    "reveal_target": "580+",
    "status": "planned"
  },
  {
    "id": "H006",
    "seed_range": "79-200",
    "question": "Ai đang theo dõi Tiểu Bảo?",
    "reveal_target": "191-200",
    "status": "planned"
  },
  {
    "id": "H007",
    "seed_range": "98",
    "question": "Nhân Gian Lô là gì?",
    "reveal_target": "580/620/760",
    "status": "planned"
  },
  {
    "id": "H008",
    "seed_range": "125-350",
    "question": "Vì sao người Lạc Kê xuất hiện trong di tích cổ?",
    "reveal_target": "325/601-650",
    "status": "planned"
  },
  {
    "id": "H009",
    "seed_range": "201-250",
    "question": "Quá khứ Mộc Vô Nhai và sai lầm 'vì đại cục' là gì?",
    "reveal_target": "231-240",
    "status": "planned"
  },
  {
    "id": "H010",
    "seed_range": "401-500",
    "question": "Thiên Môn thu hoạch gì và cho ai?",
    "reveal_target": "431-500",
    "status": "planned"
  },
  {
    "id": "H011",
    "seed_range": "451-600",
    "question": "Tại sao Thiên Mệnh Điện cần thu hoạch các giới?",
    "reveal_target": "571-590",
    "status": "planned"
  },
  {
    "id": "H012",
    "seed_range": "501-700",
    "question": "Thiên Ngoại là gì?",
    "reveal_target": "691-710",
    "status": "planned"
  },
  {
    "id": "H013",
    "seed_range": "601-640",
    "question": "Cha mẹ Tiểu Bảo là ai và vì sao hắn thành Nhân Gian Lô?",
    "reveal_target": "621-640",
    "status": "planned"
  },
  {
    "id": "H014",
    "seed_range": "651-700",
    "question": "Cửu Thiên từng là gì và vì sao bị chia?",
    "reveal_target": "681-700",
    "status": "planned"
  },
  {
    "id": "H015",
    "seed_range": "741-770",
    "question": "Reset Cửu Thiên phải trả giá gì?",
    "reveal_target": "761-770",
    "status": "planned"
  }
]
```

## Required previous five full-chapter sources
- Ch009: `chapters/chapter_009.md` — `89b16e330b7c9cae28c41234c8657347a477cfe261ab28e82316422ead81f597` — # Chương 9: Tu Tiên Thật Đáng Sợ
- Ch010: `chapters/chapter_010.md` — `5a6ffcded63ed191c96e4b844639466c47792150a10f1c971ddef8822d98e362` — # Chương 10: Ước Mơ Mới Của Tạ Tiểu Bảo
- Ch011: `chapters/chapter_011.md` — `18b5153559021cdac0855045af345f48ae5129da938732e7d40c560f7e5b6ed3` — # Chương 11: Hắc Nha Pha Mở Cửa
- Ch012: `chapters/chapter_012.md` — `fb55112c85aa48b987b89b7b9727c5e5b018fd08b9e779b28ab07a295687f558` — # Chương 12: Có Một Việc Không Đúng
- Ch013: `chapters/chapter_013.md` — `d0b8e0503abf46dfcb7da44123213d839d86859b917c541d140448afd901ab88` — # Chương 13: Giá Của Một Lựa Chọn

## Pre-draft review fields
- Current location/time: Đêm ngày 4, nhánh khe hẹp phía nam Hắc Nha Pha; dân thường đã rút xa, Tiểu Bảo bị thương sườn/tay và đang cầm chân hai tu sĩ cướp.
- Character states: Tiểu Bảo chưa nhập Dẫn Khí; sườn phải đau khi xoay/hít sâu, lòng bàn tay rách lại; giữ sợi dây thép. Ô Kê đang đi cùng dân thường. Chu/Hà ở tuyến chính còn chịu Tán Linh Tán.
- Must be new in this chapter: Đưa bằng chứng vật lý mới cho mystery cái nồi đen: một mảnh linh thạch/linh lực gần nồi khiến nồi nóng và ánh linh trên đá suy đi. Đồng thời lấy được dấu vết vật liệu của Tán Linh Tán để hiểu phe cướp chuẩn bị kỹ.
- Motifs/scenes NOT to repeat from previous five: Không làm thêm choice đạo đức; không one-shot tu sĩ; không tiếp tục “linh lực chui vào người” như payload chính; không dùng giá tiền linh thạch; không để Ô Kê cứu trận.
- Intended state change: Tiểu Bảo thoát khỏi hai đối thủ bằng địa hình, quay về tuyến chính với bằng chứng rằng cái nồi có tương tác bí ẩn với linh khí/linh thạch; vết tay được xử lý sơ bộ nhưng sườn vẫn đau.
- Intended cliffhanger/payoff: Mảnh linh thạch mất ánh sáng khi nằm sát nồi; Tiểu Bảo chưa kịp kiểm tra vì tuyến chính lại phát tín hiệu nguy cấp.
- Confirmation: story bible + writer contract + manifest + ledger + all five prior chapters Ch009–Ch013 were read in full before drafting: CONFIRMED 2026-09-16

> This file is evidence/checklist only. It does not replace actually reading the referenced sources.

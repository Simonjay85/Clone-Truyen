import json

final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9.json"
with open(final_file_path, "r", encoding="utf-8") as f:
    novel_data = json.load(f)

# Chapter 9
ch9 = novel_data["chapters"][8]
sentences = [s.replace("<p>", "").replace("</p>", "").strip() for s in ch9["content"].split("\n") if s.strip()]

extra_sentences = [
    "Những phím đàn piano lướt đi mát rượi dưới mười đầu ngón tay của Phúc, mỗi nốt nhạc vang lên như một phần xương thịt cậu.",
    "Hơi thở dồn dập nhưng vô cùng nhịp nhàng của cậu hòa cùng nhịp đũa chỉ huy của nhạc trưởng Andrzej Boreyko.",
    "Nhạc trưởng khẽ gật đầu mỉm cười khích lệ, ánh mắt toát lên sự ngưỡng mộ sâu sắc trước bản lĩnh phi thường của chàng trai Việt Nam.",
    "Bầu không khí trong khán phòng lớn Philharmonic Hall lúc này như được cô đặc lại bởi dòng năng lượng âm nhạc mãnh liệt.",
    "Từng tràng vỗ tay đứng kéo dài như muốn thổi bay mái vòm cổ kính của thánh đường âm nhạc Warsaw.",
    "Phúc cảm thấy mọi giọt mồ hôi rơi xuống đêm nay hoàn toàn xứng đáng cho sự tái sinh huy hoàng của cuộc đời mình."
]

sentences.extend(extra_sentences)
ch9["content"] = "\n".join([f"<p>{s}</p>" for s in sentences])
novel_data["chapters"][8] = ch9

with open(final_file_path, "w", encoding="utf-8") as f:
    json.dump(novel_data, f, ensure_ascii=False, indent=2)

print("Chapter 9 expanded successfully.")

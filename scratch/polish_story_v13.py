import json
import re

def polish_content(text):
    # Typo corrections
    text = text.replace("Định Định Giá", "Định Giá")
    text = text.replace("giao động", "dao động")
    
    # 1. Replace "lý tính" with contextual premium words
    text = text.replace("đôi mắt lý tính của cô khẽ dao động", "đôi mắt sắc sảo của cô khẽ dao động")
    text = text.replace("đôi mắt lý tính của cô khẽ", "đôi mắt sắc sảo của cô khẽ")
    text = text.replace("Đôi mắt lý tính, sắc sảo", "Đôi mắt tinh anh, nhạy bén")
    text = text.replace("sự lý tính, rõ ràng", "sự tinh tường, rõ ràng")
    text = text.replace("vẻ lạnh lùng, sắc bén", "vẻ điềm tĩnh, nhạy bén")
    text = text.replace("cực kỳ lý tính", "cực kỳ nhạy bén")
    text = text.replace("đứng sau những con số lạnh lùng", "đằng sau những con số vô cảm")
    text = text.replace("những con số lý tính", "những con số thực tế")
    text = text.replace("hai tâm hồn kiêu hãnh và lý tính", "hai tâm hồn kiêu hãnh và trí tuệ")
    text = text.replace("lý tính", "sắc sảo") # generic fallback

    # 2. Replace "sòng phẳng" with contextual premium words
    text = text.replace("kinh doanh sòng phẳng", "kinh doanh phân minh")
    text = text.replace("đầu tư sòng phẳng", "đầu tư nhất quán")
    text = text.replace("Sự đầu tư sòng phẳng", "Sự đầu tư minh bạch")
    text = text.replace("rõ ràng và sòng phẳng", "rõ ràng và dứt khoát")
    text = text.replace("cạnh tranh sòng phẳng", "cạnh tranh công bằng")
    text = text.replace("hợp đồng pháp lý sòng phẳng", "hợp đồng pháp lý minh bạch")
    text = text.replace("sòng phẳng, chặt chẽ nhất", "phân minh, chặt chẽ nhất")
    text = text.replace("ấm áp và sòng phẳng", "ấm áp và phân minh")
    text = text.replace("50-50 sòng phẳng", "50-50 phân minh")
    text = text.replace("sòng phẳng", "phân minh") # generic fallback

    # 3. Replace "lạnh lùng" with contextual premium words
    text = text.replace("lạnh lùng, đanh thép", "đanh thép, trầm ấm")
    text = text.replace("đôi mắt lạnh lùng của cô", "đôi mắt hờ hững của cô")
    text = text.replace("giả dối lạnh lùng", "giả dối băng giá")
    text = text.replace("vẻ lạnh lùng, sắc bén", "vẻ điềm nhiên, nhạy bén")
    text = text.replace("vẻ lạnh lùng, cứng nhắc", "vẻ lãnh đạm, cứng nhắc")
    text = text.replace("ánh mắt lạnh lùng, dửng dưng", "ánh mắt lãnh đạm, hờ hững")
    text = text.replace("lạnh lùng", "lãnh đạm") # generic fallback

    # 4. Replace "tột cùng" with contextual premium words
    text = text.replace("khinh miệt và ghê tởm tột cùng", "khinh miệt và ghê tởm vô hạn")
    text = text.replace("kinh ngạc tột cùng", "kinh ngạc tột bực")
    text = text.replace("hoảng hốt tột cùng", "hoảng hốt tột bực")
    text = text.replace("tự mãn đến tột cùng", "tự mãn đến cực điểm")
    text = text.replace("đau đớn tột cùng", "đau đớn khôn cùng")
    text = text.replace("đắc thắng tột cùng", "đắc thắng tột bực")
    text = text.replace("kiêu ngạo tột cùng", "kiêu ngạo đỉnh điểm")
    text = text.replace("hoảng loạn tột cùng", "hoảng loạn tột bực")
    text = text.replace("sợ hãi tột cùng", "sợ hãi khôn tả")
    text = text.replace("tột cùng", "tột bực") # generic fallback

    # 5. Clean up redundant spaces and format HTML nicely
    text = re.sub(r'\s+', ' ', text)
    text = text.replace("<p> ", "<p>").replace(" </p>", "</p>")
    text = text.replace("</p> <p>", "</p>\n<p>")
    
    return text

with open("scratch/story_3940_dump.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Polish main story info
if "story" in data:
    data["story"]["title"] = data["story"]["title"].replace("Kiểm Kiểm Chứng", "Kiểm Chứng")
    data["story"]["content"] = polish_content(data["story"]["content"])

# Polish chapters
for ch in data["chapters"]:
    ch["title"] = ch["title"].replace("Kiểm Kiểm Chứng", "Kiểm Chứng")
    ch["title"] = ch["title"].replace("Trái Tim Lý Tính", "Nhịp Đập Trí Tuệ")
    ch["content"] = polish_content(ch["content"])

with open("scratch/story_3940_polished.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✓ Polishing complete. Saved to scratch/story_3940_polished.json")

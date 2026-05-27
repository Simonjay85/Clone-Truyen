import re

def clean_and_split_sentences(html_content):
    html_content = html_content.replace("```html", "").replace("```", "").strip()
    paragraphs = re.findall(r'<p>(.*?)</p>', html_content, re.DOTALL)
    if not paragraphs:
        clean_text = re.sub(r'<[^>]+>', '', html_content).strip()
        paragraphs = clean_text.split('\n')
    v13_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        raw_sentences = re.split(r'(?<=[.!?])\s+', p)
        for s in raw_sentences:
            s = s.strip()
            if s:
                v13_paragraphs.append(f"<p>{s}</p>")
    return "\n".join(v13_paragraphs) + "\n"

def test_recovery(chap_raw):
    try:
        # Let's search for title
        title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
        title = title_match.group(1) if title_match else "Chương không rõ"
        
        # Match content even if it doesn't have a closing quote
        content_match = re.search(r'"content"\s*:\s*"(.*)', chap_raw, re.DOTALL)
        if content_match:
            content_str = content_match.group(1)
            # Remove any trailing JSON syntax if present
            # We look for trailing quote, braces, etc.
            # Let's clean from the right
            content_str = content_str.strip()
            if content_str.endswith('"}'):
                content_str = content_str[:-2]
            elif content_str.endswith('}'):
                content_str = content_str[:-1].strip()
                if content_str.endswith('"'):
                    content_str = content_str[:-1]
            elif content_str.endswith('"'):
                content_str = content_str[:-1]
                
            # Replace escaped characters
            recovered_content = content_str.replace('\\"', '"').replace('\\n', '\n').replace('\\t', '\t')
            
            # Close any unclosed <p> tags
            # Let's count open vs closed <p> tags
            open_p = recovered_content.count("<p>")
            close_p = recovered_content.count("</p>")
            if open_p > close_p:
                recovered_content += "</p>" * (open_p - close_p)
                
            v13_content = clean_and_split_sentences(recovered_content)
            print("RECOVERED TITLE:", title)
            print("RECOVERED CONTENT LENGTH:", len(v13_content))
            print("RECOVERED CONTENT PREVIEW:")
            print(v13_content[:200])
            print("...")
            print(v13_content[-200:])
            return True
        else:
            print("Content match failed!")
            return False
    except Exception as e:
        print("Recovery failed:", e)
        return False

# Simulate truncated JSON
truncated = """{
  "title": "Chương 1: Sự thật trần trụi sau bản báo cáo tài chính",
  "content": "<p>Đặng Hoàng Nam xoay xoay chiếc bút Montblanc trong tay, mắt không rời khỏi tập tài liệu dày cộm trên bàn.</p><p>Phan Ngọc Huyền ngồi đối diện, gương mặt thanh tú lộ rõ vẻ mệt mỏi nhưng đôi mắt vẫn ngời lên sự kiên định.</p><p>Căn phòng làm việc nhỏ ở Đà Lạt ngập tràn mùi hương thơm dịu của tinh dầu oải hương organic.</p><p>Nhưng bầu không khí lúc này lại đặc quánh và căng thẳng tột độ."
"""

test_recovery(truncated)

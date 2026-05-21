import re

def split_sentences(text):
    # Strip existing HTML tags (simple version, assuming it's mostly <p> and <br>)
    text = re.sub(r'</?p>', ' ', text)
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Simple regex to split by . ! ? followed by space and Capital letter or quote
    # The delimiter is kept by capturing it
    parts = re.split(r'([.!?]["”]?\s+)(?=[A-ZĐÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"“])', text)
    
    sentences = []
    current_sentence = ""
    for i in range(0, len(parts), 2):
        chunk = parts[i]
        delim = parts[i+1] if i+1 < len(parts) else ""
        current_sentence += chunk + delim
        if delim:
            sentences.append(current_sentence.strip())
            current_sentence = ""
            
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
        
    return sentences

print(split_sentences('Đây là câu 1. "Và đây là câu 2!" Anh ta nói thế. Thật không thể tin được... Lại còn thế này nữa? Đúng vậy.'))

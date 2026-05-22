import json
import re
import os

path = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/rewrite_3633_v13.json"

if not os.path.exists(path):
    print(f"File not found: {path}")
    exit(1)

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("="*60)
print(f"AUDITING STORY ID 3633 V13 JSON")
print(f"Title: {data.get('title')}")
print(f"Intro: {data.get('intro')}")
print("="*60)

chapters = data.get("chapters", [])
print(f"Total Chapters: {len(chapters)}")

for idx, chap in enumerate(chapters):
    title = chap.get("title")
    content = chap.get("content", "")
    
    # Word count
    text_only = re.sub(r'<[^>]+>', ' ', content)
    words = text_only.split()
    word_count = len(words)
    
    # Paragraph structure check
    paragraphs = content.strip().split('\n')
    invalid_paragraphs = []
    multiple_sentences = []
    
    for p_idx, p in enumerate(paragraphs):
        p = p.strip()
        if not p:
            continue
        if not (p.startswith("<p>") and p.endswith("</p>")):
            invalid_paragraphs.append((p_idx + 1, p))
            
        # Check if multiple sentences are in one <p>
        # Let's clean the HTML first
        clean_p = re.sub(r'<[^>]+>', '', p).strip()
        # Find sentence endings (. ! ? ...)
        # Ignore things like "Mr.", "Dr." or decimals, but in Vietnamese we don't have those much.
        # Check if there are multiple endings followed by space and uppercase or dialogue dash
        sentences = re.split(r'[.!?]+(?:\s+|$)', clean_p)
        sentences = [s for s in sentences if s.strip()]
        if len(sentences) > 1:
            multiple_sentences.append((p_idx + 1, len(sentences), clean_p))

    # Check for AI keywords
    ai_buzzwords = ["api", "chatgpt", "trợ lý ảo", "mô hình ai", "assistant", "thuật toán", "trí tuệ nhân tạo"]
    found_buzzwords = []
    for word in ai_buzzwords:
        if word in content.lower():
            found_buzzwords.append(word)

    print(f"Chapter {idx+1}: {title}")
    print(f"  - Word Count: {word_count} words")
    print(f"  - Paragraphs: {len(paragraphs)}")
    print(f"  - Invalid Tags: {len(invalid_paragraphs)}")
    if invalid_paragraphs:
        for p_num, p_text in invalid_paragraphs[:3]:
            print(f"    * Line {p_num}: {p_text[:80]}...")
    print(f"  - Multi-sentence paragraphs: {len(multiple_sentences)}")
    if multiple_sentences:
        print(f"    * Sample multi-sentence (Line {multiple_sentences[0][0]}, {multiple_sentences[0][1]} sentences): {multiple_sentences[0][2][:120]}...")
    print(f"  - AI Buzzwords: {found_buzzwords if found_buzzwords else 'None'}")
    print("-" * 60)

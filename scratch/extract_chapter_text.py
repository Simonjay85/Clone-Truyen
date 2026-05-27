import re

def main():
    filepath = "/Users/aaronnguyen/.gemini/antigravity/brain/6bdd5442-03a1-4f39-8dc7-1b2fcb5563f6/.system_generated/steps/386/content.md"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We want to extract paragraphs, which usually reside between <p> and </p> tags
    # or inside some main content div. Let's find matches for <p>...</p> tags that are not links
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
    
    clean_paragraphs = []
    for p in paragraphs:
        # Strip HTML tags
        p_clean = re.sub(r'<[^>]+>', '', p).strip()
        # Decode some basic entities
        p_clean = p_clean.replace("&ldquo;", "\"").replace("&rdquo;", "\"").replace("&nbsp;", " ").replace("&hellip;", "...")
        if len(p_clean) > 80 and "doctieuthuyet.com" not in p_clean and "đăng nhập" not in p_clean.lower() and "bình luận" not in p_clean.lower():
            clean_paragraphs.append(p_clean)
            
    print(f"Extracted {len(clean_paragraphs)} paragraphs.")
    print("\n--- FIRST 15 PARAGRAPHS OF CHAPTER 1 ---\n")
    for idx, p in enumerate(clean_paragraphs[:15]):
        print(f"[{idx+1}] {p}\n")

if __name__ == "__main__":
    main()

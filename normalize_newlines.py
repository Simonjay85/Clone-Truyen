import json

final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9.json"
with open(final_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, ch in enumerate(data["chapters"]):
    content = ch["content"]
    
    # We want to split the paragraphs
    # Since they are enclosed in <p>...</p>, we can replace </p> with </p>###SPLIT### and split by ###SPLIT###
    content_clean = content.replace("</p>", "</p>###SPLIT###")
    paragraphs = [p.strip() for p in content_clean.split("###SPLIT###") if p.strip()]
    
    # Let's ensure each starts with <p> and ends with </p>
    cleaned_paragraphs = []
    for p in paragraphs:
        # strip any newlines inside
        p_clean = p.replace("\n", "").replace("\r", "").strip()
        if p_clean:
            cleaned_paragraphs.append(p_clean)
            
    # Join them with actual newline characters
    ch["content"] = "\n".join(cleaned_paragraphs)

with open(final_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully normalized all chapters to have separate lines for each paragraph.")

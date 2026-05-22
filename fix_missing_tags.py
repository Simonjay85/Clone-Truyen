import json
import re

final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9.json"
with open(final_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, ch in enumerate(data["chapters"]):
    content = ch["content"]
    
    # We want to find all text inside <p>...</p> or even plain text lines
    # Let's clean the string by removing all <p> and </p> tags
    cleaned_content = content.replace("<p>", "").replace("</p>", "")
    
    # Split by newlines or literal \\n to get individual sentences
    # Sometimes it might have been split by \n or \\n
    lines = re.split(r'\n|\\n', cleaned_content)
    
    cleaned_sentences = []
    for line in lines:
        line_clean = line.strip()
        if line_clean:
            cleaned_sentences.append(line_clean)
            
    # Now wrap each sentence in exactly <p>...</p> and join with a single newline \n
    formatted_content = "\n".join([f"<p>{s}</p>" for s in cleaned_sentences])
    ch["content"] = formatted_content

with open(final_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully cleaned up and formatted all chapters.")

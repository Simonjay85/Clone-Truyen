import json

final_file_path = "/Users/aaronnguyen/TN/App/doctieuthuyet/pending_novel_9.json"
with open(final_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for ch in data["chapters"]:
    content = ch["content"]
    # Replace literal '\\n' with actual '\n'
    content = content.replace("\\n", "\n")
    ch["content"] = content

with open(final_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully replaced all literal \\n with actual newlines in JSON.")

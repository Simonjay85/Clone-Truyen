import json
import re
import sys

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    title = data.get("title", "")
    content = data.get("content", "")
    
    # Word count
    # Strip HTML tags
    text_only = re.sub(r'<[^>]+>', ' ', content)
    words = text_only.split()
    word_count = len(words)
    
    # Check paragraph rules
    paragraphs = content.strip().split('\n')
    errors = []
    
    # Make sure every line starts with <p> and ends with </p>
    for i, p in enumerate(paragraphs):
        p = p.strip()
        if not p:
            continue
        if not (p.startswith("<p>") and p.endswith("</p>")):
            errors.append(f"Line {i+1} does not start with <p> or end with </p>: '{p}'")
        
        # Check if contains multiple sentences. 
        # A simple check: if a line has multiple periods/exclamations followed by capital letters or spaces.
        # But dialogues might have complex structures. Let's make sure it's actually split properly.
        # We can just count punctuation marks. A sentence ends with . or ! or ? or ...
        clean_p = re.sub(r'<[^>]+>', '', p).strip()
        sentence_endings = re.findall(r'[.!?](\s+|$)', clean_p)
        # If there are multiple endings, let's log it as a warning or check.
        # Wait, inside dialogues like "— Chào cô. Cô đi đâu?" there are multiple sentences. 
        # The user rules: "Every single sentence MUST be wrapped in its own <p>...</p>\n. No blocks of multiple sentences."
        # Let's count them.
        
    print(f"File: {path}")
    print(f"Title: {title}")
    print(f"Word count: {word_count}")
    print(f"Paragraph count: {len(paragraphs)}")
    if errors:
        print("Formatting errors found:")
        for err in errors:
            print(f"  - {err}")
    else:
        print("Formatting is correct (starts/ends with <p>...</p>)!")
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        check_file(sys.argv[1])
    else:
        print("Usage: python check_word_count.py <path>")

import json
import re
import sys
import time

# Import helper functions
sys.path.insert(0, '.')
from scratch.novel_editor import *

def split_sentences(text):
    if not text: return ""
    
    # Simple replace to remove <p> and </p> tags
    text = re.sub(r'</?p>', ' ', text)
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'<strong>', '', text)
    text = re.sub(r'</strong>', '', text)
    text = re.sub(r'<em>', '', text)
    text = re.sub(r'</em>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Regex to split sentences (keeping the delimiter)
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
        
    # Format with <p>
    html_content = "".join([f"<p>{s}</p>" for s in sentences])
    return html_content

def main():
    print("Uploading novel_editor.php...")
    upload_helper()
    
    try:
        with open('existing_novels.json', 'r', encoding='utf-8') as f:
            novels = json.load(f)
            
        print(f"Found {len(novels)} novels to process.")
        
        for novel in novels:
            story_id = novel['id']
            print(f"\nProcessing Story ID: {story_id} - {novel['title']}")
            
            # Update intro
            old_intro = novel.get('intro', '')
            if old_intro:
                new_intro = split_sentences(old_intro)
                novel['intro'] = new_intro # Update in memory
                res = update_story_meta(story_id, intro=new_intro)
                if 'success' in res:
                    print("  ✓ Intro updated")
                else:
                    print(f"  ✗ Intro update failed: {res.get('error')}")
            
            # Fetch and update chapters
            res = get_story_chapters(story_id)
            if 'chapters' in res:
                chapters = res['chapters']
                print(f"  Found {len(chapters)} chapters")
                for ch in chapters:
                    ch_id = ch['id']
                    ch_title = ch['title']
                    old_content = ch['content']
                    new_content = split_sentences(old_content)
                    
                    if old_content != new_content:
                        upd = update_chapter(ch_id, ch_title, new_content)
                        if 'success' in upd:
                            print(f"    ✓ Updated chapter {ch_id}")
                        else:
                            print(f"    ✗ Failed chapter {ch_id}: {upd.get('error')}")
                    else:
                        print(f"    - No changes for chapter {ch_id}")
                    time.sleep(0.5) # Anti-rate limit
            else:
                print(f"  ✗ Failed to get chapters: {res.get('error')}")
                
        # Save back the updated intro to existing_novels.json
        with open('existing_novels.json', 'w', encoding='utf-8') as f:
            json.dump(novels, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("\nCleaning up novel_editor.php...")
        remove_helper()
        print("Done!")

if __name__ == "__main__":
    main()

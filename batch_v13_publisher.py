#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_v13_publisher.py — Automated V13 Gold Standard Batch Publisher
=====================================================================
Orchestrates the creation, design, and publication of 10 new original
Vietnamese sảng văn novels on doctieuthuyet.com.
"""

import os
import sys
import json
import time
import random
import re
import urllib.parse
import subprocess
import ftplib
import requests
import shutil

# ─── CONFIGURATION ────────────────────────────────────────────────────────────
OPENAI_KEY = "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"
FTP_HOST = "51.79.53.190"
FTP_USER = "alotoinghe"
FTP_PASS = "Nghia234!"
WP_URL = "https://doctieuthuyet.com"

TARGET_INDICES = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# ─── UTILITY FUNCTIONS ────────────────────────────────────────────────────────
def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}")
    sys.stdout.flush()

def robust_json_parse(raw_str):
    cleaned = raw_str.strip()
    
    # Remove markdown code fences if present
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()
    
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned).strip()
        
    try:
        return json.loads(cleaned)
    except Exception as parse_err:
        try:
            start_idx = cleaned.find("{")
            end_idx = cleaned.rfind("}")
            if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
                json_candidate = cleaned[start_idx:end_idx+1]
                return json.loads(json_candidate)
        except Exception:
            pass
        raise parse_err

def call_openai(system_prompt, user_prompt, max_tokens=2500, temperature=0.7):
    # Route all requests to the local high-performance Qwen-3.5-9B API server
    local_url = "http://127.0.0.1:8000/v1/chat/completions"
    
    payload = {
        "model": "default",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {"type": "json_object"}
    }
    
    # Cooldown sleep for concurrent safety
    time.sleep(0.5)
    
    for attempt in range(5):
        try:
            log(f"🤖 Calling Local Qwen API (attempt {attempt+1})...")
            res = requests.post(local_url, json=payload, timeout=600)
            if res.status_code == 200:
                res_data = res.json()
                content = res_data["choices"][0]["message"]["content"].strip()
                if content:
                    return content
            log(f"⚠️ Local Qwen API returned status {res.status_code}. Retrying...")
        except Exception as e:
            log(f"⚠️ Local Qwen API failed: {e}. Retrying...")
            
        sleep_time = 2 + attempt * 2
        time.sleep(sleep_time)
            
    raise SystemExit("Fatal: Failed to connect to Local Qwen API after multiple attempts.")


# ─── V13 SENTENCE SPLITTER & POST-PROCESSOR ──────────────────────────────────
def clean_and_split_sentences(html_content):
    """
    Enforces the strict V13 Standard: Every single sentence must be wrapped in its own <p>...</p> block.
    """
    # Remove any outer markdown code wrappers
    html_content = html_content.replace("```html", "").replace("```", "").strip()
    
    # Extract clean text within any existing <p> tags, or split text lines
    paragraphs = re.findall(r'<p>(.*?)</p>', html_content, re.DOTALL)
    if not paragraphs:
        # Fallback if no <p> tags were returned by LLM
        clean_text = re.sub(r'<[^>]+>', '', html_content).strip()
        paragraphs = clean_text.split('\n')
        
    v13_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        
        # Split on sentence boundaries (. ! ?) while avoiding splitting on standard abbreviations like IPO, CEO, Big 4, V.I.P
        # We split on punctuation followed by a space, quote, or end of line.
        raw_sentences = re.split(r'(?<=[.!?])\s+', p)
        for s in raw_sentences:
            s = s.strip()
            if s:
                v13_paragraphs.append(f"<p>{s}</p>")
                
    return "\n".join(v13_paragraphs) + "\n"

# ─── EXECUTION PIPELINE FOR A SINGLE NOVEL ────────────────────────────────────
def process_concept(c):
    idx = c["idx"]
    title = c["title"]
    author = c["author"]
    setting = c["setting"]
    male_lead = c["male_lead"]
    female_lead = c["female_lead"]
    conflict = c["conflict"]
    num_chaps = 10 # standard 10 chapters
    
    log(f"============================================================")
    log(f"📖 STARTING NOVEL INDEX {idx}: {title}")
    log(f"============================================================")
    
    # ─── 1. COVER OVERLAY DESIGN ──────────────────────────────────────────────
    base_cover_file = f"base_cover_{idx}.png"
    pending_cover_file = "pending_cover.png"
    
    if not os.path.exists(base_cover_file):
        log(f"❌ Error: Base cover file {base_cover_file} not found! Skipping novel index {idx}.")
        return False
        
    log(f"🎨 Running cover overlay engine for base cover: {base_cover_file}...")
    try:
        # Determine a subtle premium subtitle
        subtitle_text = f"Bản hùng ca sảng văn của {female_lead.split(',')[0]} & {male_lead.split(',')[0]}"
        cmd = [
            "python3", "cover_overlay_standard.py",
            "--input", base_cover_file,
            "--output", pending_cover_file,
            "--title", title,
            "--subtitle", subtitle_text
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            log(f"⚠️ Cover overlay failed with error:\n{res.stderr}")
            # fallback: copy base cover directly
            shutil.copy(base_cover_file, pending_cover_file)
            log("⚠️ Fallback to direct base cover copy.")
        else:
            log("✓ Cover overlay created successfully.")
    except Exception as ce:
        log(f"❌ Cover overlay system exception: {ce}")
        return False

    # ─── 2. GENERATE COMPACT INTRO & DYNAMIC OUTLINES ──────────────────────────
    log("📝 Generating short/punchy V13 introduction & outlines via OpenAI...")
    system_concept_prompt = """Bạn là biên tập viên văn học và bậc thầy sảng văn/vả mặt (web novel) hàng đầu Việt Nam.
Nhiệm vụ của bạn là lập kế hoạch cho một bộ truyện sảng văn/vả mặt 10/10 cực kỳ đặc sắc, lấy bối cảnh 100% tại Việt Nam.

QUY TẮC PHẢI TUÂN THỦ:
1. GIỚI THIỆU TRUYỆN (INTRO) HƯỚNG 1 (CỰC KỲ NGẮN & KỊCH TÍNH):
   - Phải bắt đầu bằng một câu thoại/trích dẫn sỉ nhục cực sốc in đậm bọc trong <p><strong>"..."</strong></p>.
   - Theo sau là đúng 2-3 đoạn văn ngắn (tổng cộng tối đa 120-150 từ, mỗi đoạn bọc trong <p>...</p>) giới thiệu mâu thuẫn khốc liệt và đòn lật kèo thâu tóm ngược, có nhắc đến nữ chính thông minh đồng hành.
   - Tuyệt đối không viết lan man dài dòng hay danh sách dài để tránh tràn khung màn hình điện thoại di động (mobile overflow).
2. DÀN Ý 10 CHƯƠNG:
   - Hãy thiết lập dàn ý chi tiết kịch tính cho đúng 10 chương."""

    user_concept_prompt = f"""Hãy lập dàn ý 10 chương và giới thiệu truyện cực kịch tính ngắn gọn theo tiêu chuẩn hướng 1 cho tác phẩm:
- Tiêu đề: {title}
- Tác giả: {author}
- Nam chính: {male_lead}
- Nữ chính: {female_lead}
- Bối cảnh: {setting}
- Xung đột chủ đạo: {conflict}

Hãy xuất ra cấu trúc JSON nguyên bản tuyệt đối, không chứa ```json hay ```:
{{
  "title": "{title}",
  "author": "{author}",
  "genre": "Sảng Văn",
  "intro": "Mở đầu in đậm câu nói sỉ nhục, sau đó là 2 đoạn kịch tính cực ngắn bọc trong các thẻ <p>",
  "outlines": [
    {{ "chap_num": 1, "outline": "Tóm tắt mâu thuẫn khốc liệt chương 1..." }},
    {{ "chap_num": 2, "outline": "Tóm tắt chương 2..." }},
    ...
    {{ "chap_num": 10, "outline": "Tóm tắt chương 10..." }}
  ]
}}"""
    user_concept_prompt += f"\n[Generation ID: {time.time()} - {random.randint(1000, 9999)}]"
    concept_raw = call_openai(system_concept_prompt, user_concept_prompt, max_tokens=3000, temperature=0.2)
    try:
        novel_blueprint = robust_json_parse(concept_raw)
        log(f"✓ Blueprint generated. Title: {novel_blueprint['title']}")
    except Exception as e:
        log("❌ Failed to parse novel blueprint JSON:")
        log(concept_raw)
        return False

    # ─── 3. GENERATE CHAPTERS SEQUENTIALLY ────────────────────────────────────
    chapters_content = []
    
    for i in range(1, 11):
        outline_item = novel_blueprint["outlines"][i-1]
        log(f"✍️ Writing Chapter {i}/10: {outline_item['outline'][:80]}...")
        
        system_writer_prompt = """Bạn là THE GHOSTWRITER - Nhà văn truyện mạng sảng văn/vả mặt số 1 Việt Nam. Bạn có văn phong miêu tả cực kỳ sống động, chân thực, sắc sảo.
QUY TẮC VIẾT 10/10 CHUYÊN NGHIỆP:
1. SHOW, DON'T TELL: Miêu tả chi tiết hành động vật lý, nét mặt, sự run rẩy, giọt mồ hôi, hay tiếng giày gót nhọn giẫm xuống sàn bê tông. Tránh các tính từ sáo rỗng như 'vô biên', 'tột cùng', 'kinh hoàng'.
2. HỘI THOẠI ĐINH TAI NHỨC ÓC: Các câu thoại sắc lẹm, thể hiện sự kiêu ngạo của kẻ thù trước khi bị vả mặt, và sự điềm tĩnh tối thượng của nhân vật chính.
3. CHI TIẾT KINH DOANH & ĐỜI SỐNG THỰC TẾ TẠI VIỆT NAM: Sử dụng các chi tiết thật về cơ cấu cổ đông, sao kê tài chính ngân hàng Việt Nam, luật doanh nghiệp Việt Nam, cơ quan nhà nước (C03, Bộ Công an, Ủy ban Chứng khoán), kiểm toán Big 4, và thói quen sinh hoạt bản địa.
4. ĐỘ DÀI (600 - 900 TỪ): Viết cực kỳ chi tiết, chậm rãi, phát triển sâu sắc tâm lý nhân vật và các đoạn hội thoại gay cấn dài lâu. Dung lượng khoảng 600 đến 900 từ. Tuyệt đối không viết tóm tắt hay kết thúc chương quá nhanh.
5. ĐỊNH DẠNG: Chỉ sử dụng các thẻ HTML cơ bản như <p>, <strong>, <em>. Tách mỗi câu thành một thẻ <p> riêng biệt."""
        prev_chaps_str = ""
        if chapters_content:
            titles = [c["title"] for c in chapters_content]
            prev_chaps_str = f"- Các chương trước đã viết: {json.dumps(titles, ensure_ascii=False)}"

        user_writer_prompt = f"""Dựa trên bản thiết kế truyện sau:
- Tựa truyện: {novel_blueprint['title']}
- Giới thiệu thế giới quan & nhân vật: {novel_blueprint['intro']}
- Tác giả: {novel_blueprint['author']}

Hãy viết CHI TIẾT CHƯƠNG {i} của bộ truyện.
- Dàn ý Chương {i}: {outline_item['outline']}
{prev_chaps_str}

YÊU CẦU ĐẶC BIỆT VỀ ĐỘ DÀI:
Bắt buộc nội dung trong phần 'content' phải có độ dài khoảng 600 đến 900 từ. Viết cực kỳ chậm rãi, chi tiết hóa mọi hội thoại và nét mặt.

YÊU CẦU TRẢ VỀ dạng JSON chính xác không chứa ```json:
{{
  "title": "Chương {i}: Tên chương giật gân, cuốn hút",
  "content": "Nội dung chương viết hoàn chỉnh bằng Tiếng Việt 100%, định dạng HTML với các thẻ <p>..."
}}"""
        user_writer_prompt += f"\n[Generation ID: {time.time()} - {random.randint(1000, 9999)}]"

        chap_raw = call_openai(system_writer_prompt, user_writer_prompt, max_tokens=4500, temperature=0.3)
        try:
            chap_data = robust_json_parse(chap_raw)
            v13_content = clean_and_split_sentences(chap_data["content"])
            chapters_content.append({
                "title": chap_data["title"],
                "content": v13_content
            })
            log(f"  -> ✓ Finished Chapter {i}: {chap_data['title']} (Length: {len(v13_content)} chars)")
        except Exception as e:
            log(f"⚠️ Failed to parse Chapter {i} JSON, attempting robust recovery...")
            try:
                title_match = re.search(r'"title"\s*:\s*"(.*?)"', chap_raw)
                title = title_match.group(1) if title_match else f"Chương {i}"
                
                content_match = re.search(r'"content"\s*:\s*"(.*)', chap_raw, re.DOTALL)
                if content_match:
                    content_str = content_match.group(1).strip()
                    if content_str.endswith('"}'):
                        content_str = content_str[:-2]
                    elif content_str.endswith('}'):
                        content_str = content_str[:-1].strip()
                        if content_str.endswith('"'):
                            content_str = content_str[:-1]
                    elif content_str.endswith('"'):
                        content_str = content_str[:-1]
                        
                    recovered_content = content_str.replace('\\"', '"').replace('\\n', '\n')
                    
                    open_p = recovered_content.count("<p>")
                    close_p = recovered_content.count("</p>")
                    if open_p > close_p:
                        recovered_content += "</p>" * (open_p - close_p)
                        
                    v13_content = clean_and_split_sentences(recovered_content)
                    chapters_content.append({
                        "title": title,
                        "content": v13_content
                    })
                    log(f"  -> ✓ Recovered Chapter {i} via robust regex (Length: {len(v13_content)} chars)")
                else:
                    raise e
            except Exception as re_err:
                log(f"❌ Fatal error generating Chapter {i}: {re_err}")
                log(f"--- RAW RESPONSE START (First 500 chars) ---")
                log(chap_raw[:500])
                log(f"--- RAW RESPONSE END ---")
                return False
        
        time.sleep(2)

    # ─── 4. FTP COVER SIDELOADING ─────────────────────────────────────────────
    random_id = random.randint(100000, 999999)
    cover_local_filename = f"cover_sideload_{random_id}.png"
    log(f"📤 Uploading premium cover to FTP root: wp-content/uploads/{cover_local_filename}...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd("wp-content/uploads")
        with open(pending_cover_file, "rb") as f:
            ftp.storbinary(f"STOR {cover_local_filename}", f)
        ftp.quit()
        log("✓ Sideloaded cover uploaded via FTP successfully.")
    except Exception as fe:
        log(f"❌ FTP Sideload Cover Error: {fe}")
        return False

    # ─── 5. UPLOAD PUBLISH ENDPOINT HELPER (DISABLED FOR CONCURRENT SAFETY) ────
    # Helper is uploaded once by the main orchestrator at start and cleaned up at the end.
    log("✓ Assuming publish_novel.php helper script is already uploaded by main orchestrator.")

    # ─── 6. TRIGGER ATOMIC WORDPRESS PUBLICATION ──────────────────────────────
    log("🌐 Triggering publication via HTTP POST request...")
    payload = {
        "secret_token": "ZEN_TRUYEN_2026_BYPASS",
        "title": novel_blueprint['title'],
        "intro": novel_blueprint['intro'],
        "author": novel_blueprint['author'],
        "genre": "Sảng Văn",
        "cover_local_filename": cover_local_filename,
        "chapters": chapters_content
    }
    
    try:
        api_url = f"{WP_URL}/publish_novel.php"
        res = requests.post(api_url, json=payload, timeout=120)
        res_data = res.json()
        
        if res_data.get('success'):
            log(f"🎉 NOVEL {idx} PUBLISHED SUCCESSFULLY!")
            log(f"  -> Story ID: {res_data['story_id']}")
            log(f"  -> Cover Status: {res_data['cover_status']}")
            log(f"  -> Chapters: {res_data['chapters_count']} chapters published.")
            
            # Clean up remote helper (DISABLED FOR CONCURRENT SAFETY)
            log("✓ Skipping dynamic remote cleanup of publish_novel.php.")
                
            # Clean up local pending files
            if os.path.exists(pending_cover_file):
                os.remove(pending_cover_file)
                log("✓ Cleaned up local pending_cover.png.")
                
            # Update local database existing_novels.json
            existing_path = "existing_novels.json"
            existing = []
            if os.path.exists(existing_path):
                try:
                    with open(existing_path, "r", encoding="utf-8") as f:
                        existing = json.load(f)
                except Exception:
                    pass
            
            new_novel_entry = {
                "id": res_data['story_id'],
                "title": res_data['title'],
                "slug": res_data['title'].lower().replace(" ", "-"),
                "intro": novel_blueprint['intro']
            }
            existing.append(new_novel_entry)
            with open(existing_path, "w", encoding="utf-8") as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            log("✓ Updated existing_novels.json local database.")
            return True
        else:
            log(f"❌ API Publication error response: {res_data}")
            return False
            
    except Exception as ae:
        log(f"❌ API HTTP POST Exception: {ae}")
        return False

# ─── MAIN BATCH ORCHESTRATOR ──────────────────────────────────────────────────
def main():
    log("🚀 BATCH V13 GOLD STANDARD NOVEL PUBLISHER ACTIVATED")
    
    # Dynamic command line argument parsing for subagents
    import argparse
    parser = argparse.ArgumentParser(description="V13 Batch Publisher")
    parser.add_argument("--indices", nargs="+", type=int, default=None, help="Target concept indices to process")
    args, unknown = parser.parse_known_args()
    
    run_indices = args.indices if args.indices is not None else TARGET_INDICES
    log(f"Target concepts indices: {run_indices}")
    
    # Step 1: Upload publish_novel.php helper script via FTP
    log("📤 Uploading publish_novel.php endpoint to FTP root...")
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        with open("publish_novel.php", "rb") as f:
            ftp.storbinary("STOR publish_novel.php", f)
        log("✓ Uploaded publish_novel.php to server.")
        ftp.quit()
    except Exception as e:
        log(f"❌ FTP Upload Error for helper script: {e}")
        sys.exit(1)
        
    try:
        with open("novel_concepts_50.json", "r", encoding="utf-8") as f:
            concepts = json.load(f)
            
        target_concepts = [c for c in concepts if c["idx"] in run_indices]
        log(f"Loaded {len(target_concepts)} target concepts successfully.")
        
        success_count = 0
        failed_indices = []
        
        for c in target_concepts:
            success = False
            # Retry up to 2 times for transient network/LLM issues
            for attempt in range(2):
                try:
                    if process_concept(c):
                        success = True
                        success_count += 1
                        break
                    else:
                        log(f"⚠️ Attempt {attempt+1} failed for novel index {c['idx']}. Retrying in 10s...")
                        time.sleep(10)
                except Exception as exc:
                    log(f"⚠️ Exception on attempt {attempt+1} for novel index {c['idx']}: {exc}")
                    time.sleep(10)
                    
            if not success:
                log(f"❌ Failed to publish novel index {c['idx']} after all attempts.")
                failed_indices.append(c["idx"])
                
            # Cooldown between stories
            time.sleep(10)
            
        log(f"============================================================")
        log(f"🏁 BATCH PROCESS FINISHED")
        log(f"  -> Total successfully published: {success_count}/{len(target_concepts)}")
        if failed_indices:
            log(f"  -> Failed indices: {failed_indices}")
        log(f"============================================================")
        
    finally:
        # Clean up the publish helper script from remote for security
        log("🧹 Cleaning up publish_novel.php helper from remote server...")
        try:
            ftp = ftplib.FTP(FTP_HOST, timeout=30)
            ftp.login(FTP_USER, FTP_PASS)
            ftp.delete("publish_novel.php")
            log("✓ Deleted publish_novel.php helper from remote server for security.")
            ftp.quit()
        except Exception as e:
            log(f"⚠️ Could not delete publish_novel.php remote helper: {e}")

if __name__ == "__main__":
    main()

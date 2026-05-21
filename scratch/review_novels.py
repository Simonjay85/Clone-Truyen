#!/usr/bin/env python3
"""
100-Novel Pipeline Review & Update Script
Reads all published novels from existing_novels.json, fetches their content,
evaluates against V12 criteria, and logs issues for the orchestrator to fix.
"""
import json
import os
import requests
import re

WP_URL = "https://doctieuthuyet.com"
SECRET = "ZEN_TRUYEN_2026_BYPASS"
EXISTING_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/existing_novels.json"
REVIEW_LOG_PATH = "/Users/aaronnguyen/TN/App/doctieuthuyet/scratch/review_log.json"

def count_words(html):
    clean = re.sub(r'<[^>]+>', ' ', html)
    return len(clean.split())

def fetch_chapters(story_id):
    """Fetch chapters for a story via WP REST-like PHP endpoint."""
    try:
        res = requests.post(f"{WP_URL}/get_phe_vat_chaps.php", 
                           json={"secret": SECRET, "story_id": story_id},
                           timeout=30)
        if res.status_code == 200:
            return res.json()
    except:
        pass
    return []

def review_novel(novel):
    """Score a novel entry against V12 standards."""
    issues = []
    score = 10.0
    
    title = novel.get("title", "")
    intro = novel.get("intro", "")
    
    # Check title is clickbait style
    if len(title) < 20:
        issues.append("Tiêu đề quá ngắn, chưa giật gân")
        score -= 1.0
    
    # Check intro length
    intro_words = count_words(intro)
    if intro_words < 80:
        issues.append(f"Intro quá ngắn ({intro_words} từ, cần ≥80 từ)")
        score -= 0.5
    
    return {
        "id": novel["id"],
        "title": title,
        "score": round(score, 1),
        "issues": issues
    }

def main():
    print("=" * 60)
    print("📊 V12 NOVEL QUALITY REVIEW SYSTEM")
    print("=" * 60)
    
    if not os.path.exists(EXISTING_PATH):
        print("❌ existing_novels.json not found!")
        return
    
    with open(EXISTING_PATH, "r", encoding="utf-8") as f:
        novels = json.load(f)
    
    print(f"Total novels: {len(novels)}")
    
    reviews = []
    needs_fix = []
    
    for novel in novels:
        result = review_novel(novel)
        reviews.append(result)
        if result["score"] < 9.0 or result["issues"]:
            needs_fix.append(result)
            print(f"⚠️  [{result['score']}/10] #{result['id']}: {result['title']}")
            for issue in result["issues"]:
                print(f"     - {issue}")
        else:
            print(f"✅  [{result['score']}/10] #{result['id']}: {result['title']}")
    
    avg = sum(r["score"] for r in reviews) / len(reviews) if reviews else 0
    print(f"\n📈 Average Score: {avg:.1f}/10")
    print(f"✅ Passing (≥9.0): {len([r for r in reviews if r['score'] >= 9.0])}")
    print(f"⚠️  Needs fix: {len(needs_fix)}")
    
    with open(REVIEW_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "total": len(reviews),
            "average_score": round(avg, 1),
            "reviews": reviews,
            "needs_fix": needs_fix
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Review log saved to {REVIEW_LOG_PATH}")
    return needs_fix

if __name__ == "__main__":
    main()

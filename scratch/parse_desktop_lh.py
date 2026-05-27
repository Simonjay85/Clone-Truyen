import re
import json

with open('/Users/aaronnguyen/TN/App/doctieuthuyet/lighthouse_desktop_final_result.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'window\.__LIGHTHOUSE_JSON__\s*=\s*(\{.*?\});', html, re.DOTALL)
if not match:
    match = re.search(r'const\s+lhrunnerresults\s*=\s*(\{.*?\});', html, re.DOTALL)
if not match:
    match = re.search(r'<script[^>]*>\s*(?:window\.)?lhrunnerresults\s*=\s*(\{.*?\})\s*</script>', html, re.DOTALL)

if match:
    data = json.loads(match.group(1))
    categories = data.get('categories', {})
    print("LIGHTHOUSE DESKTOP SCORES:")
    for cat_id, cat in categories.items():
        print(f"- {cat.get('title')}: {cat.get('score') * 100:.1f}")
    
    print("\nFAILED/WARNING AUDITS (< 0.9):")
    audits = data.get('audits', {})
    for audit_id, audit in audits.items():
        score = audit.get('score')
        if score is not None and isinstance(score, (int, float)) and score < 0.9:
            print(f"[{audit.get('score') * 100:.0f}] {audit.get('title')} ({audit_id})")
            display_value = audit.get('displayValue')
            if display_value:
                print(f"  Value: {display_value}")
            details = audit.get('details', {})
            items = details.get('items', [])
            if items:
                print(f"  Affected items (first 5):")
                for item in items[:5]:
                    clean_item = {k: v for k, v in item.items() if k in ['url', 'node', 'selector', 'wastedBytes', 'msSavings', 'totalBytes']}
                    print(f"    - {clean_item}")
else:
    print("Could not parse JSON")

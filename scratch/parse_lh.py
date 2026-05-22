import re
import json

with open('/Users/aaronnguyen/TN/App/doctieuthuyet/lighthouse_report.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'window\.__LIGHTHOUSE_JSON__\s*=\s*(\{.*?\});', html, re.DOTALL)
if not match:
    match = re.search(r'const\s+lhrunnerresults\s*=\s*(\{.*?\});', html, re.DOTALL)
if not match:
    match = re.search(r'<script[^>]*>\s*(?:window\.)?lhrunnerresults\s*=\s*(\{.*?\})\s*</script>', html, re.DOTALL)

if match:
    data = json.loads(match.group(1))
    categories = data.get('categories', {})
    print("LIGHTHOUSE SCORES:")
    for cat_id, cat in categories.items():
        print(f"- {cat.get('title')}: {cat.get('score') * 100:.1f}")
    
    print("\nFAILED/WARNING AUDITS (< 0.9):")
    audits = data.get('audits', {})
    for audit_id, audit in audits.items():
        score = audit.get('score')
        # Check if score is a float/int and less than 0.9
        if score is not None and isinstance(score, (int, float)) and score < 0.9:
            print(f"[{audit.get('score') * 100:.0f}] {audit.get('title')} ({audit_id})")
            display_value = audit.get('displayValue')
            if display_value:
                print(f"  Value: {display_value}")
            explanation = audit.get('explanation')
            if explanation:
                print(f"  Explanation: {explanation}")
            description = audit.get('description')
            if description:
                # Truncate description if too long
                desc = re.sub(r'\[Learn more.*$', '', description)
                print(f"  Desc: {desc[:150]}")
            
            # Print items if available
            details = audit.get('details', {})
            items = details.get('items', [])
            if items:
                print(f"  Affected items (first 3):")
                for item in items[:3]:
                    # Print interesting keys
                    clean_item = {k: v for k, v in item.items() if k in ['url', 'node', 'selector', 'label', 'source', 'wastedBytes', 'msSavings', 'totalBytes']}
                    print(f"    - {clean_item}")
else:
    print("Could not parse JSON")

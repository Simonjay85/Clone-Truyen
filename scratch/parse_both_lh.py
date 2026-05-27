import re
import json

def parse_html(filepath, name):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        match = re.search(r'window\.__LIGHTHOUSE_JSON__\s*=\s*(\{.*?\});', html, re.DOTALL)
        if not match:
            match = re.search(r'const\s+lhrunnerresults\s*=\s*(\{.*?\});', html, re.DOTALL)
        if not match:
            match = re.search(r'<script[^>]*>\s*(?:window\.)?lhrunnerresults\s*=\s*(\{.*?\})\s*</script>', html, re.DOTALL)
        
        if match:
            data = json.loads(match.group(1))
            categories = data.get('categories', {})
            print(f"=== FINAL LIGHTHOUSE {name} SCORES ===")
            for cat_id, cat in categories.items():
                print(f"- {cat.get('title')}: {cat.get('score') * 100:.1f}")
        else:
            print(f"Could not parse JSON for {name} ({filepath})")
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")

parse_html('/Users/aaronnguyen/TN/App/doctieuthuyet/lighthouse_mobile_final_result.html', 'MOBILE')
parse_html('/Users/aaronnguyen/TN/App/doctieuthuyet/lighthouse_desktop_final_result.html', 'DESKTOP')

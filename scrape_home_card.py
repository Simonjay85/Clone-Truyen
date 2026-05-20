import requests
import re

def main():
    url = "https://doctieuthuyet.com/"
    print(f"Fetching {url}...")
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        html = r.text
        
        # Look for cards in the HTML using regular expressions
        # We can find all class="mkm-card" blocks
        # Let's find card containers
        cards = re.findall(r'<div class="mkm-card">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
        print(f"Found {len(cards)} card regex matches.")
        
        found = False
        for card in cards:
            if "Bức Thư" in card:
                print("\n--- Match found ---")
                print(card)
                found = True
                
        if not found:
            # Fallback search inside the whole HTML
            print("\nDid not match standard regex. Searching for 'Bức Thư' in raw HTML context:")
            pos = html.find("Bức Thư")
            if pos != -1:
                start = max(0, pos - 800)
                end = min(len(html), pos + 1200)
                print(html[start:end])
            else:
                print("Could not find 'Bức Thư' in the homepage HTML.")
                
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

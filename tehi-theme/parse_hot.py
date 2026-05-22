import urllib.request
import re

def parse_hot():
    url = "https://doctieuthuyet.com/"
    print("Fetching homepage...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print("Error:", e)
        return

    # Find the "Truyện hot" section in the HTML
    hot_idx = html.find("Truyện hot")
    if hot_idx == -1:
        print("Could not find 'Truyện hot'")
        return
        
    # Get the grid block that follows it
    grid_start = html.find('<div class="mkm-grid">', hot_idx)
    if grid_start == -1:
        print("Could not find grid after 'Truyện hot'")
        return
        
    grid_end = html.find('<!-- TRUYỆN FULL -->', grid_start)
    if grid_end == -1:
        grid_end = grid_start + 10000
        
    grid_html = html[grid_start:grid_end]
    
    # Let's find all card blocks in grid_html
    cards = re.split(r'<div class="mkm-card">', grid_html)[1:]
    print(f"Found {len(cards)} cards in grid:")
    
    for i, card in enumerate(cards):
        name_match = re.search(r'<p class="mkm-card-name">(.*?)</p>', card, re.DOTALL)
        name = name_match.group(1).strip() if name_match else "Unknown"
        
        img_match = re.search(r'<img\s+src="([^"]+)"', card)
        img_src = img_match.group(1) if img_match else "No image src"
        
        style_match = re.search(r'style="--card-bg:\s*url\(\'([^\']+)\'\);"', card)
        card_bg = style_match.group(1) if style_match else "No card-bg style"
        
        print(f"Card {i+1}: {name}")
        print(f"  Image src: {img_src}")
        print(f"  Card BG:   {card_bg}")

if __name__ == "__main__":
    parse_hot()

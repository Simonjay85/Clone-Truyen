import urllib.request
import ssl
import re

ctx = ssl._create_unverified_context()
url = "https://doctieuthuyet.com/"

try:
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
        html = r.read().decode('utf-8')
        
    print(f"✓ Downloaded HTML: {len(html)} bytes")
    
    # Save the html
    with open("scratch/live_homepage.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    # Let's search for any inline style blocks
    style_blocks = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    print(f"Found {len(style_blocks)} <style> blocks in HTML.")
    
    # Check if there are any style blocks containing display: none
    print("\nInline style rules containing 'display: none':")
    for idx, block in enumerate(style_blocks, 1):
        # Look for display: none in this style block
        matches = re.finditer(r'([^{}\n]+)\{[^}]*display\s*:\s*none[^}]*\}', block, re.IGNORECASE)
        m_list = list(matches)
        if m_list:
            print(f"  --- Style Block {idx} ---")
            for m in m_list:
                print(f"    {m.group(1).strip()} {{ ... display: none; ... }}")
                
    # Check if there are any style blocks containing opacity: 0
    print("\nInline style rules containing 'opacity: 0':")
    for idx, block in enumerate(style_blocks, 1):
        matches = re.finditer(r'([^{}\n]+)\{[^}]*opacity\s*:\s*0[^}]*\}', block, re.IGNORECASE)
        m_list = list(matches)
        if m_list:
            print(f"  --- Style Block {idx} ---")
            for m in m_list:
                print(f"    {m.group(1).strip()} {{ ... opacity: 0; ... }}")
                
    # Search for all inline style="..." attributes in HTML elements
    inline_styles = re.findall(r'style="([^"]*display\s*:\s*none[^"]*)"', html, re.IGNORECASE)
    print(f"\nFound {len(inline_styles)} elements with style=\"...display: none...\"")
    for style in inline_styles:
        print(f"  style=\"{style}\"")
        
    # Search for visibility: hidden
    inline_visibility = re.findall(r'style="([^"]*visibility\s*:\s*hidden[^"]*)"', html, re.IGNORECASE)
    print(f"\nFound {len(inline_visibility)} elements with style=\"...visibility: hidden...\"")
    for style in inline_visibility:
        print(f"  style=\"{style}\"")
        
except Exception as e:
    print("Error:", e)

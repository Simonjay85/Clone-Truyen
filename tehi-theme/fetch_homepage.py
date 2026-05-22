import urllib.request
import re

def fetch_hot_stories():
    url = "https://doctieuthuyet.com/"
    print("Fetching homepage HTML...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print("Error fetching home:", e)
        return

    # Find the "Truyện hot" section
    # Let's search for "Truyện hot" or the CSS block
    start_idx = html.find("Truyện hot")
    if start_idx == -1:
        print("Could not find 'Truyện hot' in HTML")
        # Let's write the HTML to a file to inspect if needed
        with open("homepage.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Wrote whole HTML to homepage.html")
        return
        
    print("Found 'Truyện hot' at position", start_idx)
    # Grab 5000 characters around it
    snippet = html[start_idx:start_idx + 10000]
    print("Snippet:")
    print(snippet)

if __name__ == "__main__":
    fetch_hot_stories()

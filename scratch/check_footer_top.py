with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Presence of 'mkm-footer-top' in live HTML:", "mkm-footer-top" in html)

# Let's extract the block containing mkm-footer-top
start_idx = html.find('class="mkm-footer-top"')
if start_idx != -1:
    print("\n--- FOUND class=\"mkm-footer-top\" ---")
    print(html[start_idx:start_idx+1000])
else:
    print("Could not find class=\"mkm-footer-top\" in HTML")

from crawler import get_novel_details, get_chapter_content

print("Testing novel scrape...")
novel = get_novel_details("https://tehitruyen.com/ga-cho-dai-lao-phan-dien-4004.html")
if novel:
    print(f"Title: {novel['title']}")
    print(f"Chapters count: {len(novel['chapters'])}")
    if novel['chapters']:
        first_chap_url = novel['chapters'][0]['url']
        print(f"Testing chapter scrape: {first_chap_url}")
        content = get_chapter_content(first_chap_url)
        print(f"Content length: {len(content)}")
        print(f"Content preview: {content[:200]}")
    else:
        print("No chapters found.")
else:
    print("Novel data is None.")

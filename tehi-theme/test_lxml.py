from lxml import html

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    text = f.read()

idx = text.rfind('<body')
doc = html.fromstring(text[idx:])
layout = doc.find('.//div[@class="studio-layout"]')
if layout is not None:
    print("Children of studio-layout:")
    for child in layout:
        if type(child.tag) == str:
            print(f"- {child.tag} id={child.get('id')} class={child.get('class')}")

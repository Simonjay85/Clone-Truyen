from html.parser import HTMLParser

class DivParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.tags = []

    def handle_starttag(self, tag, attrs):
        if tag in ['br', 'img', 'input', 'meta', 'link', 'hr']:
            return
        attrs_dict = dict(attrs)
        self.depth += 1
        
        if tag in ['div', 'aside', 'main']:
            self.tags.append((tag, attrs_dict.get('id'), attrs_dict.get('class'), self.depth))

    def handle_endtag(self, tag):
        if tag in ['br', 'img', 'input', 'meta', 'link', 'hr']:
            return
        self.depth -= 1

parser = DivParser()
with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    text = f.read()

idx = text.rfind('<body')
parser.feed(text[idx:])
for t in parser.tags:
    if t[0] == 'main':
        print(f"MAIN DEPTH: {t[3]}")
    if t[1] == 'panel-scrape':
        print(f"PANEL-SCRAPE DEPTH: {t[3]}")
print(f"Final Depth: {parser.depth}")


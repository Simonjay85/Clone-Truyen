from html.parser import HTMLParser

class DivParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        if tag not in ['br', 'img', 'input', 'meta', 'link', 'hr', 'script']:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag not in ['br', 'img', 'input', 'meta', 'link', 'hr', 'script']:
            self.depth -= 1

parser = DivParser()
with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    text = f.read()

idx = text.rfind('<body')
parser.feed(text[idx:])
print(parser.depth)


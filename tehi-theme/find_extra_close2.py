from html.parser import HTMLParser

VOID = {'br','img','input','meta','link','hr','area','base','col','embed','param','source','track','wbr'}

class DivParser(HTMLParser):
    def __init__(self, lines):
        super().__init__()
        self.depth = 0
        self.lines = lines
        self.history = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID and tag != 'script' and tag != 'style':
            self.depth += 1
            self.history.append(('+', tag, self.getpos()[0], self.depth))

    def handle_endtag(self, tag):
        if tag not in VOID and tag != 'script' and tag != 'style':
            self.depth -= 1
            self.history.append(('-', tag, self.getpos()[0], self.depth))

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    content = f.read()
    raw_lines = content.splitlines()

idx = content.rfind('<body')
body_start_line = content[:idx].count('\n') + 1

parser = DivParser(raw_lines)
parser.feed(content[idx:])

# Show last 20 entries (close to where depth goes to 0 or negative)
for h in parser.history[-30:]:
    actual_line = body_start_line + h[2] - 1
    print(f"  [{h[1]:10}] {h[0]}  depth={h[3]}  relative_line={h[2]}  file_line≈{actual_line}")

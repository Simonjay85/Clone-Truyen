from html.parser import HTMLParser

VOID = {'br','img','input','meta','link','hr','area','base','col','embed','param','source','track','wbr'}

class DivParser(HTMLParser):
    def __init__(self, raw_lines):
        super().__init__()
        self.depth = 0
        self.raw_lines = raw_lines
        self.layout_depth = None

    def handle_starttag(self, tag, attrs):
        if tag in VOID or tag in ('script', 'style'):
            return
        self.depth += 1
        attrs_dict = dict(attrs)
        if attrs_dict.get('class') == 'studio-layout':
            self.layout_depth = self.depth
            print(f"studio-layout OPENS at depth={self.depth}, line={self.getpos()[0]}")

    def handle_endtag(self, tag):
        if tag in VOID or tag in ('script', 'style'):
            return
        if self.layout_depth and self.depth == self.layout_depth:
            line = self.getpos()[0]
            context = self.raw_lines[line-1].strip() if line <= len(self.raw_lines) else '?'
            print(f"studio-layout CLOSES at depth={self.depth}, tag=</{tag}>, relative_line={line}, context={context!r}")
            self.layout_depth = None
        self.depth -= 1

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    content = f.read()
    raw_lines = content.splitlines()

idx = content.rfind('<body')
offset = content[:idx].count('\n')

parser = DivParser(raw_lines)
parser.feed(content[idx:])

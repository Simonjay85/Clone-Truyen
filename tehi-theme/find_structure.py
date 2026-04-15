from html.parser import HTMLParser

VOID = {'br','img','input','meta','link','hr','area','base','col','embed','param','source','track','wbr'}

class DivParser(HTMLParser):
    def __init__(self, raw_lines):
        super().__init__()
        self.depth = 0
        self.raw_lines = raw_lines
        self.output = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        if tag in ('script', 'style'):
            return
        self.depth += 1
        attrs_dict = dict(attrs)
        pid = attrs_dict.get('id','')
        pcls = attrs_dict.get('class','')
        rel = self.getpos()[0]
        if tag in ('div','aside','main','nav','section') or pid in ('panel-scrape','panel-create','studio-layout','ss-schedule-panel'):
            self.output.append((tag, pid, pcls, self.depth, rel))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag in ('script', 'style'):
            return
        self.depth -= 1

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    content = f.read()
    raw_lines = content.splitlines()

idx = content.rfind('<body')
offset = content[:idx].count('\n')

parser = DivParser(raw_lines)
parser.feed(content[idx:])

for t in parser.output:
    tag, pid, pcls, d, rel = t
    actual_line = offset + rel
    print(f"L{actual_line:4d}  depth={d}  <{tag}> id={pid!r:20} cls={pcls!r}")


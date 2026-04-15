from html.parser import HTMLParser
import re

class DivParser(HTMLParser):
    def __init__(self, lines):
        super().__init__()
        self.depth = 0
        self.lines = lines
        self.char_pos = 0
        self.problem_lines = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['br', 'img', 'input', 'meta', 'link', 'hr', 'script', 'style']:
            self.depth += 1

    def handle_endtag(self, tag):
        if tag not in ['br', 'img', 'input', 'meta', 'link', 'hr', 'script', 'style']:
            self.depth -= 1
            if self.depth < 0:
                line_num = self.getpos()[0]
                self.problem_lines.append((line_num, tag, self.lines[line_num-1].strip() if line_num <= len(self.lines) else '?'))

with open('/Users/aaronnguyen/TN/App/Clone Truyen/tehi-theme/page-story-studio.php', 'r') as f:
    content = f.read()
    lines = content.splitlines()

# Get second <body> tag position
idx = content.rfind('<body')
body_start_line = content[:idx].count('\n') + 1
print(f"Second <body> starts at line: {body_start_line}")

parser = DivParser(lines)
parser.feed(content[idx:])
print("Problem lines (where depth went negative):")
for pl in parser.problem_lines:
    print(f"  File line ~{body_start_line + pl[0] - 1}: </{pl[1]}> -- context: {pl[2]}")

